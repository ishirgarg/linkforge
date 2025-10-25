"""
Full Documentation Pipeline
Simple pipeline: Scrape → Markdown (Groq) → Embed (ChromaDB) → Query
"""

import os
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from typing import List
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Import our modules
from manual_url_crawler import crawl_manual_urls
from vector_db import ChromaVectorDB
from groq_processor import process_documents_with_groq

# Load environment variables
load_dotenv()


# chunk_html_content, combine_chunks, create_prompt, and ChunkTask are imported from groq_processor


# process_single_document function removed - now using groq_processor.process_documents_with_groq


def run_full_pipeline(documentation_url: str, max_urls: int = 20, 
                      crawler_workers: int = 50,
                      enable_vector_db: bool = True, 
                      collection_name: str = None):
    """
    Run the complete documentation pipeline.
    
    Args:
        documentation_url: The documentation site to crawl
        max_urls: Maximum number of URLs to process
        crawler_workers: Number of concurrent workers for web scraping (default: 50)
        enable_vector_db: Enable ChromaDB integration for embeddings
        collection_name: Name for the ChromaDB collection (auto-generated if None)
    """
    print("Full Documentation Pipeline (Groq + ChromaDB)")
    print("=" * 60)
    print(f"Target: {documentation_url}")
    print(f"Max URLs: {max_urls}")
    print(f"Crawler Workers: {crawler_workers}")
    print(f"Vector DB: {'Enabled' if enable_vector_db else 'Disabled'}")
    print()
    
    # Auto-generate collection name from URL if not provided
    if collection_name is None and enable_vector_db:
        parsed = urlparse(documentation_url)
        domain = parsed.netloc.replace('www.', '').replace('.', '_')
        collection_name = f"docs_{domain}"
        print(f"📚 Collection name: {collection_name}")
        print()
    
    # Initialize Groq client
    groq_api_key = os.getenv("Grok")
    if not groq_api_key:
        print("❌ Grok API key not found in environment variables.")
        return
    
    groq_client = Groq(api_key=groq_api_key)
    print("Groq client initialized")
    
    # Initialize Vector DB
    vector_db = None
    if enable_vector_db:
        try:
            vector_db = ChromaVectorDB(
                path="./chroma_db",
                collection_name=collection_name,
                chunk_size=500,  # Words per chunk
                chunk_overlap=50  # Overlapping words
            )
            print(f"Vector database initialized (Qwen 0.6B embeddings)")
            print(f"   Collection: {collection_name}")
            print(f"   Chunk size: 500 words with 50 word overlap")
            
            # Test model loading explicitly
            print(f"   Testing model loading...")
            test_embedding = vector_db.get_text_embedding(["test"])
            print(f"   Model loaded successfully - embedding shape: {test_embedding.shape}")
        except Exception as e:
            print(f"⚠️ Could not initialize vector database: {str(e)}")
            enable_vector_db = False
    print()
    
    # Step 1: Crawl the documentation site
    print("🕷️ STEP 1: Crawling documentation site...")
    print("-" * 60)
    
    scraped_data = crawl_manual_urls(
        documentation_url=documentation_url,
        max_urls=max_urls,
        max_workers=crawler_workers
    )
    
    if not scraped_data:
        print("❌ No data scraped. Exiting.")
        return
    
    print(f"✅ Crawled {len(scraped_data)} pages")
    
    # Create organized output directories
    output_dir = Path("documentation_markdown")
    crawl_dir = Path("manual_crawl_results")
    output_dir.mkdir(exist_ok=True)
    crawl_dir.mkdir(exist_ok=True)
    
    # Save crawl results to dedicated folder
    timestamp = int(time.time())
    crawl_file = crawl_dir / f"crawl_results_{timestamp}.json"
    with open(crawl_file, 'w', encoding='utf-8') as f:
        json.dump({
            "crawl_info": {
                "documentation_url": documentation_url,
                "max_urls": max_urls,
                "crawled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "total_pages": len(scraped_data),
                "successful_pages": len([p for p in scraped_data if p.get('status') == 'success']),
                "failed_pages": len([p for p in scraped_data if p.get('status') != 'success'])
            },
            "scraped_data": scraped_data
        }, f, indent=2, ensure_ascii=False)
    print(f"💾 Crawl results saved to: {crawl_file}")
    print()
    
    # Step 2: Process with Groq to create markdown
    print("🤖 STEP 2: Converting to Markdown with Groq...")
    print("-" * 60)
    
    # Process documents with Groq (sequential for now, can be made concurrent later)
    processed_data = process_documents_with_groq(scraped_data, str(output_dir))
    
    # Count successful/failed
    successful = len([p for p in processed_data if p.get('markdown_content')])
    failed = len(processed_data) - successful
    
    # Step 3: Embed into vector database
    if enable_vector_db and vector_db:
        print(f"\n🔍 STEP 3: Embedding into vector database...")
        print("-" * 60)
        
        embedded_count = 0
        total_to_embed = len([p for p in processed_data if p.get('markdown_content')])
        print(f"📊 Embedding {total_to_embed} documents...")
        
        for i, page in enumerate(processed_data, 1):
            if page.get('markdown_content'):
                try:
                    print(f"🔄 Embedding document {i}/{total_to_embed}: {page['url']}...", end=" ")
                    doc_id = f"doc_{i}_{page['url'].split('/')[-1]}"
                    
                    # Try embedding with better error handling
                    try:
                        vector_db.insert(
                            documents=[page['markdown_content']],
                            ids=[doc_id]
                        )
                        embedded_count += 1
                        print("✅")
                    except Exception as embed_error:
                        print("❌")
                        print(f"❌ Failed to embed document {i}: {str(embed_error)}")
                        print(f"   Error type: {type(embed_error).__name__}")
                        # Don't print full traceback for embedding errors to avoid spam
                        
                except Exception as e:
                    print(f"❌ Failed to embed document {i}: {str(e)}")
                    import traceback
                    traceback.print_exc()
        
        print(f"\n📊 Embedding Summary:")
        print(f"  - Total documents: {len(processed_data)}")
        print(f"  - Documents with content: {total_to_embed}")
        print(f"  - Successfully embedded: {embedded_count}")
        print(f"  - Failed: {total_to_embed - embedded_count}")
    
    # Step 4: Save results
    print("\n💾 STEP 3: Saving results...")
    print("-" * 60)
    
    timestamp = int(time.time())
    results_file = f"full_pipeline_results_{timestamp}.json"
    
    pipeline_results = {
        "pipeline_info": {
            "documentation_url": documentation_url,
            "max_urls": max_urls,
            "processed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_pages": len(processed_data),
            "successful_pages": successful,
            "failed_pages": failed,
            "vector_db_enabled": enable_vector_db,
            "collection_name": collection_name if enable_vector_db else None
        },
        "processed_data": processed_data
    }
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(pipeline_results, f, indent=2, ensure_ascii=False)
    
    # Final summary
    print("\n🎉 PIPELINE COMPLETED!")
    print("=" * 60)
    print(f"📁 Markdown files: {output_dir}")
    print(f"💾 Full results: {results_file}")
    
    print(f"\n📊 Final Summary:")
    print(f"  - Total pages: {len(processed_data)}")
    print(f"  - Successfully processed: {successful}")
    print(f"  - Failed: {failed}")
    print(f"  - Success rate: {(successful/len(processed_data)*100):.1f}%")
    
    if enable_vector_db and vector_db:
        try:
            count = vector_db.collection.count()
            print(f"\n🔍 Vector Database:")
            print(f"  - Total chunks embedded: {count}")
            print(f"  - Collection: {collection_name}")
            print(f"  - Ready for semantic search!")
        except Exception as e:
            print(f"\n⚠️ Could not retrieve vector DB stats: {str(e)}")
    
    print(f"\n📖 Your documentation is ready in the '{output_dir}' folder!")
    if enable_vector_db:
        print(f"🔎 Use search_docs.py to query the documentation!")
        
        # Test ChromaDB with a simple query
        print(f"\n🔍 STEP 4: Testing ChromaDB with sample query...")
        print("-" * 60)
        try:
            test_query = "How to create a Streamlit app?"
            print(f"Query: '{test_query}'")
            
            results = vector_db.query(test_query, n_results=3)
            
            if results['documents'] and results['documents'][0]:
                print(f"✅ Found {len(results['documents'][0])} relevant results:")
                for i, doc in enumerate(results['documents'][0], 1):
                    doc_id = results['ids'][0][i-1] if 'ids' in results and results['ids'] else f"doc_{i}"
                    distance = results['distances'][0][i-1] if 'distances' in results and results['distances'] else 0.0
                    print(f"\n  Result {i} (ID: {doc_id}, Distance: {distance:.4f}):")
                    print(f"  {doc[:200]}...")
            else:
                print("❌ No results found")
        except Exception as e:
            print(f"❌ Query test failed: {str(e)}")


def main():
    """Main function to run the pipeline."""
    # Configuration
    documentation_url = "https://docs.streamlit.io/develop/api-reference"
    max_urls = 1  # Adjust as needed
    crawler_workers = 200  # Concurrent web scraping
    
    # Check if API keys are available
    groq_key = os.getenv('Grok')
    brightdata_key = os.getenv('BRIGHT_DATA_API_TOKEN')
    
    if not groq_key:
        print("❌ Grok API key not found in environment variables.")
        print("Please add it to your .env file:")
        print("Grok=your_groq_api_key_here")
        return
    
    if not brightdata_key:
        print("❌ BRIGHT_DATA_API_TOKEN not found in environment variables.")
        print("Please add it to your .env file:")
        print("BRIGHT_DATA_API_TOKEN=your_brightdata_api_key_here")
        return
    
    print("API keys found. Starting pipeline...")
    print()
    
    # Run the pipeline
    run_full_pipeline(
        documentation_url=documentation_url,
        max_urls=max_urls,
        crawler_workers=crawler_workers,
        enable_vector_db=True
    )


if __name__ == "__main__":
    main()
