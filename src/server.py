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
from dotenv import load_dotenv
import logging as logger

# Load environment variables
load_dotenv()

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# FastMCP imports
from fastmcp import FastMCP

# Import our existing modules
from full_doc_pipeline import run_full_pipeline
from vector_db import ChromaVectorDB

# Anthropic Claude imports
try:
    import anthropic
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

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server with detailed instructions
mcp = FastMCP(
    "documentation-server",
    instructions="""This server processes documentation websites and provides semantic search capabilities.

WORKFLOW:
1. First, use 'process_documentation_url' to crawl and embed a documentation website
2. Wait for processing to complete by checking 'get_processing_status' 
3. Once complete, use 'query_documentation' to search the embedded documentation
4. Use 'list_collections' to see all available documentation collections

IMPORTANT NOTES:
- Processing takes 30-120 seconds depending on the number of pages
- Always check the processing status before querying
- The collection_name is returned when you start processing (e.g., 'docs_example_com')
- You can query existing collections without processing them again

EXAMPLE USAGE:
1. Process: process_documentation_url(url="https://docs.example.com", max_urls=10)
   Returns: job_id and collection_name
2. Check: get_processing_status(job_id="abc-123")
   Returns: status (processing/completed/failed)
3. Query: query_documentation(query="how to authenticate", collection_name="docs_example_com")
   Returns: relevant documentation chunks with similarity scores"""
)

# Global state
processing_jobs: Dict[str, Dict[str, Any]] = {}
vector_dbs: Dict[str, ChromaVectorDB] = {}
executor = ThreadPoolExecutor(max_workers=3)


def _run_pipeline_background(job_id: str, url: str, max_urls: int, 
                            crawler_workers: int, collection_name: str):
    """Run the pipeline in background thread."""
    try:
        # Update status
        processing_jobs[job_id].update({
            "status": "processing",
            "progress": 10,
            "message": "Crawling and processing documentation..."
        })
        
        # Run the pipeline
        run_full_pipeline(
            documentation_url=url,
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
            "completed_at": time.time()
        })
        
        # Initialize vector DB for querying
        try:
            vector_db = ChromaVectorDB(
                path="./chroma_db",
                collection_name=collection_name,
                chunk_size=500,
                chunk_overlap=50
            )
            vector_dbs[collection_name] = vector_db
            logger.info(f"Vector DB initialized for collection: {collection_name}")
        except Exception as e:
            logger.warning(f"Could not initialize vector DB: {e}")
        
    except Exception as e:
        logger.error(f"Pipeline failed for job {job_id}: {str(e)}")
        processing_jobs[job_id].update({
            "status": "failed",
            "error": str(e),
            "message": f"Processing failed: {str(e)}"
        })


@mcp.tool()
async def process_documentation_url(url: str, max_urls: int = 20, crawler_workers: int = 50, collection_name: str = None) -> str:
    """STEP 1: Process a documentation website URL and embed it into vector database for querying.
    
    This tool crawls a documentation website, converts HTML to markdown using Groq LLM,
    generates embeddings, and stores them in ChromaDB for semantic search.
    
    PROCESSING TIME: 30-120 seconds depending on number of pages
    
    Args:
        url: The documentation website URL to process (e.g., "https://docs.example.com")
        max_urls: Maximum number of URLs to crawl (default: 20, recommended: 5-50)
        crawler_workers: Number of concurrent crawler workers (default: 50, recommended: 50-200)
        collection_name: Name for the vector database collection (auto-generated from domain if not provided)
    
    Returns:
        Status message with:
        - job_id: Use this with get_processing_status to check progress
        - collection_name: Use this with query_documentation to search
    
    NEXT STEP: Use get_processing_status(job_id) to check when processing is complete
    """
    # Generate job ID
    job_id = str(uuid.uuid4())
    
    # Auto-generate collection name if not provided
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
async def query_documentation(query: str, collection_name: str, max_results: int = 5, enhance_with_claude: bool = True) -> str:
    """STEP 3: Search the embedded documentation using semantic search with Claude enhancement.
    
    This tool performs semantic search on processed documentation using vector embeddings,
    then uses Claude to enhance the results with better explanations and code examples.
    
    PREREQUISITE: Documentation must be processed first (use process_documentation_url)
    
    Args:
        query: Natural language search query (e.g., "how to authenticate users")
        collection_name: Name of the collection to search (returned from process_documentation_url)
        max_results: Maximum number of results to return (default: 5, recommended: 3-10)
        enhance_with_claude: Use Claude to enhance results with examples (default: True)
    
    Returns:
        Search results with:
        - Claude-enhanced explanation and code examples (if enabled)
        - Original documentation chunks with similarity scores
        - Document IDs and sources
    
    TIP: Use specific queries for better results. Instead of "authentication", try "how to implement user authentication"
    """
    try:
        # Get or create vector DB
        if collection_name not in vector_dbs:
            vector_db = ChromaVectorDB(
                path="./chroma_db",
                collection_name=collection_name,
                chunk_size=500,
                chunk_overlap=50
            )
            vector_dbs[collection_name] = vector_db
        
        vector_db = vector_dbs[collection_name]
        
        # Perform search
        results = vector_db.query(query, n_results=max_results)
        
        if not results['documents'] or not results['documents'][0]:
            return f"No results found for query: '{query}'"
        
        # Format results
        documents = results['documents'][0]
        ids = results['ids'][0] if 'ids' in results else []
        distances = results['distances'][0] if 'distances' in results else [0] * len(documents)
        
        # Combine all retrieved chunks for Claude
        combined_docs = "\n\n---\n\n".join(documents)
        
        result_text = f"🔍 Search Results for: '{query}'\n"
        result_text += f"📚 Collection: {collection_name}\n"
        result_text += f"Found {len(documents)} results\n\n"
        
        # Enhance with Claude if available and enabled
        if enhance_with_claude and CLAUDE_AVAILABLE and CLAUDE_API_KEY:
            try:
                result_text += "🤖 Claude-Enhanced Response\n"
                result_text += "=" * 60 + "\n\n"
                
                # Create prompt for Claude
                claude_prompt = f"""Based on the following documentation chunks, provide a comprehensive answer to the user's question: "{query}"

Your response should:
1. Provide a clear, concise explanation
2. Include practical code examples (if applicable)
3. Highlight key concepts and best practices
4. Reference specific details from the documentation

Documentation chunks:
{combined_docs}

Please provide a well-structured response with code examples where appropriate."""

                # Call Claude API
                # Using Claude Sonnet 4.5 - the smartest model for complex agents and coding
                message = claude_client.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=2000,
                    messages=[
                        {"role": "user", "content": claude_prompt}
                    ]
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
    """STEP 2: Get the status of a documentation processing job.
    
    Use this tool to check if documentation processing is complete before querying.
    Processing typically takes 30-120 seconds.
    
    Args:
        job_id: The job ID returned from process_documentation_url
    
    Returns:
        Job status information including:
        - Status: processing, completed, or failed
        - Progress: percentage complete
        - Collection name: for use with query_documentation
        - Elapsed time
        - Error message (if failed)
    
    WHEN TO USE: Poll this every 5-10 seconds after calling process_documentation_url
    NEXT STEP: Once status is "completed", use query_documentation with the collection_name
    """
    if job_id not in processing_jobs:
        return f"❌ Job {job_id} not found"
    
    job = processing_jobs[job_id]
    
    status_icon = {
        "processing": "⏳",
        "completed": "✅",
        "failed": "❌"
    }.get(job['status'], "ℹ️")
    
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
    """List all available documentation collections that can be queried.
    
    Use this tool to see what documentation has already been processed and is ready to search.
    You can query any listed collection without processing it again.
    
    Returns:
        List of collections with:
        - Collection names (use these with query_documentation)
        - Number of chunks in each collection
        - Ready status
    
    WHEN TO USE:
    - To see what documentation is already available
    - To get the exact collection_name for querying
    - To avoid re-processing documentation that already exists
    """
    try:
        import chromadb
        from chromadb.config import Settings
        
        # Initialize client
        try:
            client = chromadb.PersistentClient(
                path="./chroma_db",
                settings=Settings(anonymized_telemetry=False)
            )
        except Exception as e:
            logger.warning(f"Could not initialize PersistentClient: {e}")
            return "No collections found. The vector database may not be initialized yet. Process a documentation URL first!"
        
        # List collections
        try:
            collections = client.list_collections()
        except Exception as e:
            logger.error(f"Error listing collections: {e}")
            return f"Error accessing collections: {str(e)}"
        
        if not collections or len(collections) == 0:
            return "No collections found. Process a documentation URL first!"
        
        result_text = f"📚 Available Documentation Collections\n\n"
        result_text += f"Found {len(collections)} collection(s):\n\n"
        
        for collection in collections:
            try:
                # Get collection metadata
                name = collection.name
                count = collection.count()
                result_text += f"📖 {name}\n"
                result_text += f"   Chunks: {count}\n"
                result_text += f"   Ready to query!\n\n"
            except Exception as e:
                logger.warning(f"Error getting info for collection: {e}")
                result_text += f"📖 {collection.name if hasattr(collection, 'name') else 'Unknown'}\n"
                result_text += f"   Error getting details: {str(e)}\n\n"
        
        return result_text
        
    except Exception as e:
        logger.error(f"Unexpected error in list_collections: {e}")
        return f"Error listing collections: {str(e)}\n\nMake sure the vector database is initialized by processing a documentation URL first."


if __name__ == "__main__":
    # Run the server on localhost:8000
    # Using 'http' transport for simpler web client compatibility
    # streamable-http requires session management and is better for persistent connections
    logger.info("🚀 Starting Documentation MCP Server on http://localhost:8000/mcp")
    mcp.run(transport="http", host="localhost", port=8000, path="/mcp")

