"""
MCP Documentation Server
Processes documentation URLs and provides semantic search capabilities
Compatible with FastMCP for HTTP transport
"""

import time
import uuid
import asyncio
from typing import Dict, Any
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import logging
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# FastMCP imports
from fastmcp import FastMCP

# FastAPI imports for REST endpoints
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Import your existing modules
from full_doc_pipeline import run_full_pipeline
from vector_db import ChromaVectorDB

# ChromaDB imports
import chromadb
from chromadb.config import Settings

# Claude API imports
import anthropic
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    "documentation-server",
    instructions="""This server processes documentation websites and provides semantic search capabilities.

WORKFLOW:
1. Use 'process_documentation_url' to crawl and embed a documentation website.
2. Wait for processing to complete via 'get_processing_status'.
3. Use 'query_documentation' to search embedded documentation.
4. Use 'list_collections' to see all available collections.

PROCESSING TIME: 30-120 seconds depending on number of pages."""
)

# Create separate FastAPI app for REST endpoints
rest_app = FastAPI(title="LinkForge REST API")

# Add CORS middleware
rest_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global state
processing_jobs: Dict[str, Dict[str, Any]] = {}
executor = ThreadPoolExecutor(max_workers=3)

# Initialize a single ChromaDB client at startup
try:
    chroma_client = chromadb.PersistentClient(
        path="./chroma_db",
        settings=Settings(anonymized_telemetry=False)
    )
    logger.info("✅ ChromaDB client initialized successfully")
except Exception as e:
    chroma_client = None
    logger.warning(f"Could not initialize ChromaDB client: {e}")

# Initialize Claude client
try:
    CLAUDE_AVAILABLE = True
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    if CLAUDE_API_KEY:
        claude_client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
        logger.info("✅ Claude API initialized successfully")
    else:
        CLAUDE_AVAILABLE = False
        logger.warning("⚠️ CLAUDE_API_KEY not found in environment variables")
except ImportError:
    CLAUDE_AVAILABLE = False
    logger.warning("⚠️ anthropic package not installed. Install with: pip install anthropic")


# Pydantic models for REST endpoints
class ProcessDocRequest(BaseModel):
    url: str
    max_urls: int = 20
    crawler_workers: int = 50
    collection_name: str = None


def get_vector_db(collection_name: str) -> ChromaVectorDB:
    """Retrieve a ChromaVectorDB object for a given collection using the shared client."""
    if not chroma_client:
        raise RuntimeError("ChromaDB client is not initialized")
    
    return ChromaVectorDB(
        path="./chroma_db",
        collection_name=collection_name,
        chunk_size=500,
        chunk_overlap=50
    )

def _run_pipeline_background(job_id: str, url: str, max_urls: int,
                             crawler_workers: int, collection_name: str):
    """Run the full documentation processing pipeline in a background thread."""
    try:
        # Update job status
        processing_jobs[job_id].update({
            "status": "processing",
            "progress": 10,
            "message": "Crawling and processing documentation..."
        })

        # Run the pipeline
        run_full_pipeline(
            documentation_url=url,
            crawl_result_filename=f"docs/crawl_{job_id}.json",
            markdown_output_path=f"docs/docs_{job_id}/",
            max_urls=max_urls,
            crawler_workers=crawler_workers,
            enable_vector_db=True,
            collection_name=collection_name
        )

        # Update status to completed
        processing_jobs[job_id].update({
            "status": "completed",
            "progress": 100,
            "message": "Documentation processing completed successfully!",
            "completed_at": time.time(),
            "mcp_server_url": "http://localhost:8001/mcp"
        })

        # Ensure the collection exists and is ready for queries
        get_vector_db(collection_name)
        logger.info(f"Vector DB ready for collection: {collection_name}")

    except Exception as e:
        logger.error(f"Pipeline failed for job {job_id}: {str(e)}")
        processing_jobs[job_id].update({
            "status": "failed",
            "error": str(e),
            "message": f"Processing failed: {str(e)}"
        })


# ============================================================================
# REST API ENDPOINTS
# ============================================================================

@rest_app.post("/api/process")
async def process_documentation_endpoint(request: ProcessDocRequest):
    """Simple HTTP endpoint to process documentation."""
    job_id = str(uuid.uuid4())
    
    collection_name = request.collection_name
    if not collection_name:
        parsed = urlparse(request.url)
        domain = parsed.netloc.replace('www.', '').replace('.', '_')
        collection_name = f"docs_{domain}"

    # Initialize job status
    processing_jobs[job_id] = {
        "status": "processing",
        "url": request.url,
        "collection_name": collection_name,
        "max_urls": request.max_urls,
        "crawler_workers": request.crawler_workers,
        "started_at": time.time(),
        "progress": 0,
        "message": "Processing started...",
    }

    # Start processing in background
    loop = asyncio.get_event_loop()
    loop.run_in_executor(
        executor,
        _run_pipeline_background,
        job_id, request.url, request.max_urls, request.crawler_workers, collection_name
    )

    return {
        "success": True,
        "job_id": job_id,
        "url": request.url,
        "collection_name": collection_name,
        "max_urls": request.max_urls,
        "message": "Documentation processing started"
    }

@rest_app.get("/api/status/{job_id}")
async def get_job_status_endpoint(job_id: str):
    """Simple HTTP endpoint to get job status."""
    if job_id not in processing_jobs:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    job = processing_jobs[job_id]
    
    response = {
        "job_id": job_id,
        "status": job['status'],
        "url": job['url'],
        "collection_name": job['collection_name'],
        "progress": job['progress'],
        "message": job['message'],
        "started_at": job['started_at'],
        "mcp_server_url": job['mcp_server_url']
    }

    if job['status'] == 'completed':
        response['completed_at'] = job.get('completed_at')
        response['elapsed_time'] = job.get('completed_at', 0) - job['started_at']
    elif job['status'] == 'failed':
        response['error'] = job.get('error', 'Unknown error')
    else:
        response['elapsed_time'] = time.time() - job['started_at']

    return response

# ============================================================================
# MCP TOOL ENDPOINTS (Original)
# ============================================================================

@mcp.tool()
async def process_documentation_url(url: str, collection_name: str, max_urls: int = 20, crawler_workers: int = 50) -> str:
    """STEP 1: Process a documentation website and embed it for semantic search."""
    job_id = str(uuid.uuid4())

    if not collection_name:
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '').replace('.', '_')
        collection_name = f"docs_{domain}"

    # Initialize job status
    processing_jobs[job_id] = {
        "status": "processing",
        "url": url,
        "collection_name": collection_name,
        "max_urls": max_urls,
        "crawler_workers": crawler_workers,
        "started_at": time.time(),
        "progress": 0,
        "message": "Processing started...",
    }

    # Start processing in background
    loop = asyncio.get_event_loop()
    loop.run_in_executor(
        executor,
        _run_pipeline_background,
        job_id, url, max_urls, crawler_workers, collection_name
    )

    return (f"✅ Documentation processing started!\n\n"
            f"Job ID: {job_id}\n"
            f"URL: {url}\n"
            f"Collection: {collection_name}\n"
            f"Max URLs: {max_urls}\n\n"
            f"Use get_processing_status with job_id '{job_id}' to check progress.\n"
            f"Once complete, use query_documentation with collection_name '{collection_name}' to search.")


@mcp.tool()
async def query_documentation(
    query: str, 
    collection_name: str, 
    max_results: int = 10, 
    enhance_with_claude: bool = True
) -> str:
    """Search the embedded documentation using semantic search with optional Claude enhancement."""
    try:
        # Use the shared ChromaDB client to create the vector DB object for this collection
        vector_db = ChromaVectorDB(
            path="./chroma_db",
            collection_name=collection_name,
            chunk_size=500,
            chunk_overlap=50
        )

        # Perform search
        results = vector_db.query(query, n_results=max_results)

        if not results['documents'] or not results['documents'][0]:
            return f"No results found for query: '{query}'"

        documents = results['documents'][0]
        ids = results['ids'][0] if 'ids' in results else []
        distances = results['distances'][0] if 'distances' in results else [0] * len(documents)

        # Combine all retrieved chunks for Claude
        combined_docs = "\n\n---\n\n".join(documents)

        result_text = f"🔍 Search Results for: '{query}'\n"
        result_text += f"📚 Collection: {collection_name}\n"
        result_text += f"Found {len(documents)} results\n\n"

        # Enhance with Claude if available
        if enhance_with_claude and CLAUDE_AVAILABLE and CLAUDE_API_KEY:
            try:
                result_text += "🤖 Claude-Enhanced Response\n"
                result_text += "=" * 60 + "\n\n"

                claude_prompt = f"""Based on the following documentation chunks, provide a comprehensive answer to the user's question: "{query}"

Your response should:
1. Provide a clear, concise explanation
2. Include practical code examples (if applicable)
3. Highlight key concepts and best practices
4. Reference specific details from the documentation

Documentation chunks:
{combined_docs}

Please provide a well-structured response with code examples where appropriate."""

                message = claude_client.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=2000,
                    messages=[{"role": "user", "content": claude_prompt}]
                )

                claude_response = message.content[0].text
                result_text += claude_response + "\n\n"
                result_text += "=" * 60 + "\n\n"

            except Exception as e:
                logger.error(f"Claude enhancement failed: {e}")
                result_text += f"⚠️ Claude enhancement unavailable: {str(e)}\n\n"
                result_text += "=" * 60 + "\n\n"

        # Add original documentation chunks
        result_text += "📖 Original Documentation Chunks\n"
        result_text += "=" * 60 + "\n\n"

        for i, (doc, doc_id, distance) in enumerate(zip(documents, ids, distances), 1):
            similarity = 1 - distance
            result_text += f"📄 Chunk {i} (Similarity: {similarity:.2%})\n"
            result_text += f"Document ID: {doc_id}\n"
            result_text += "-" * 60 + "\n"
            result_text += f"{doc[:800]}{'...' if len(doc) > 800 else ''}\n\n"
            result_text += "=" * 60 + "\n\n"

        return result_text

    except Exception as e:
        return f"Error querying documentation: {str(e)}"


@mcp.tool()
async def get_processing_status(job_id: str) -> str:
    """STEP 2: Get the status of a documentation processing job."""
    if job_id not in processing_jobs:
        return f"❌ Job {job_id} not found"

    job = processing_jobs[job_id]
    status_icon = {"processing": "⏳", "completed": "✅", "failed": "❌"}.get(job['status'], "ℹ️")

    status_text = f"{status_icon} Job Status\n\n"
    status_text += f"Job ID: {job_id}\n"
    status_text += f"Status: {job['status'].upper()}\n"
    status_text += f"URL: {job['url']}\n"
    status_text += f"Collection: {job['collection_name']}\n"
    status_text += f"Progress: {job['progress']}%\n"
    status_text += f"Message: {job['message']}\n"

    if job['status'] == 'completed':
        elapsed = job.get('completed_at', 0) - job['started_at']
        status_text += f"\n✅ Completed in {elapsed:.1f} seconds\n"
        status_text += f"\nYou can now query this documentation using:\n"
        status_text += f"  query_documentation(query='your question', collection_name='{job['collection_name']}')"
    elif job['status'] == 'failed':
        status_text += f"\n❌ Error: {job.get('error', 'Unknown error')}\n"
    else:
        elapsed = time.time() - job['started_at']
        status_text += f"\n⏳ Elapsed time: {elapsed:.1f} seconds\n"

    return status_text


@mcp.tool()
async def list_collections() -> str:
    """List all available documentation collections using the shared ChromaDB client."""
    if not chroma_client:
        return "No collections found. The vector database may not be initialized yet."

    try:
        collections = chroma_client.list_collections()
        if not collections:
            return "No collections found. Process a documentation URL first!"

        result_text = f"📚 Available Documentation Collections\n\nFound {len(collections)} collection(s):\n\n"
        for collection in collections:
            try:
                result_text += f"📖 {collection.name}\n"
                result_text += f"   Chunks: {collection.count()}\n"
                result_text += f"   Ready to query!\n\n"
            except Exception as e:
                result_text += f"📖 {collection.name}\n"
                result_text += f"   Error fetching details: {str(e)}\n\n"

        return result_text
    except Exception as e:
        logger.error(f"Error listing collections: {e}")
        return f"Error listing collections: {str(e)}"


if __name__ == "__main__":
    import threading
    
    logger.info("🚀 Starting Documentation Server")
    logger.info("   REST API: http://localhost:8000/api/process")
    logger.info("   MCP Protocol: http://localhost:8001/mcp")
    
    # Run REST API in a separate thread
    def run_rest_api():
        uvicorn.run(rest_app, host="localhost", port=8000, log_level="info")
    
    rest_thread = threading.Thread(target=run_rest_api, daemon=True)
    rest_thread.start()
    
    # Run MCP server on different port
    mcp.run(transport="streamable-http", host="localhost", port=8001)