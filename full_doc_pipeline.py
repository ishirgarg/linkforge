"""
Full Documentation Pipeline
Combines web crawling and Gemini processing to create markdown documentation.
"""

import os
import json
import time
from pathlib import Path
from dotenv import load_dotenv

# Import our modules
from manual_url_crawler import crawl_manual_urls
from queue_based_processor import QueueBasedProcessor

# Load environment variables
load_dotenv()

def run_full_pipeline(documentation_url: str, max_urls: int = 20, max_workers: int = 5):
    """
    Run the complete documentation pipeline.
    
    Args:
        documentation_url: The documentation site to crawl
        max_urls: Maximum number of URLs to process
    """
    print("🚀 Full Documentation Pipeline")
    print("=" * 50)
    print(f"📚 Target: {documentation_url}")
    print(f"📊 Max URLs: {max_urls}")
    print()
    
    # Step 1: Crawl the documentation site
    print("🕷️ STEP 1: Crawling documentation site...")
    print("-" * 40)
    
    scraped_data = crawl_manual_urls(
        documentation_url=documentation_url,
        max_urls=max_urls,
        max_workers=max_workers
    )
    
    if not scraped_data:
        print("❌ No data scraped. Exiting.")
        return
    
    print(f"✅ Crawled {len(scraped_data)} pages")
    print()
    
    # Step 2: Process with Gemini
    print("🤖 STEP 2: Processing with Multi-Model Gemini...")
    print("-" * 40)
    
    processor = QueueBasedProcessor()
    processed_data = processor.process_multiple_documents(scraped_data)
    
    # Step 3: Create index
    print("📋 STEP 3: Creating documentation index...")
    print("-" * 40)
    
    index_file = processor.create_index_file(processed_data)
    
    # Step 4: Save results
    print("💾 STEP 4: Saving results...")
    print("-" * 40)
    
    timestamp = int(time.time())
    results_file = f"full_pipeline_results_{timestamp}.json"
    
    pipeline_results = {
        "pipeline_info": {
            "documentation_url": documentation_url,
            "max_urls": max_urls,
            "processed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_pages": len(processed_data),
            "successful_pages": len([p for p in processed_data if p.get('markdown_file')]),
            "failed_pages": len([p for p in processed_data if not p.get('markdown_file')])
        },
        "processed_data": processed_data
    }
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(pipeline_results, f, indent=2, ensure_ascii=False)
    
    # Final summary
    print("\n🎉 PIPELINE COMPLETED!")
    print("=" * 50)
    print(f"📁 Markdown files: {processor.output_dir}")
    print(f"📋 Index file: {index_file}")
    print(f"💾 Full results: {results_file}")
    
    successful = len([p for p in processed_data if p.get('markdown_file')])
    failed = len(processed_data) - successful
    
    print(f"\n📊 Final Summary:")
    print(f"  - Total pages: {len(processed_data)}")
    print(f"  - Successfully processed: {successful}")
    print(f"  - Failed: {failed}")
    print(f"  - Success rate: {(successful/len(processed_data)*100):.1f}%")
    
    print(f"\n📖 Your documentation is ready in the '{processor.output_dir}' folder!")

def main():
    """Main function to run the pipeline."""
    # Configuration
    documentation_url = "https://openai.github.io/openai-agents-python/"
    max_urls = 15  # Adjust as needed
    max_workers = 5  # Concurrent workers (adjust based on API limits)
    
    # Check if API keys are available
    gemini_key = os.getenv('GEMINI_API_KEY')
    brightdata_key = os.getenv('BRIGHT_DATA_API_TOKEN')
    
    if not gemini_key:
        print("❌ GEMINI_API_KEY not found in environment variables.")
        print("Please add it to your .env file:")
        print("GEMINI_API_KEY=your_gemini_api_key_here")
        return
    
    if not brightdata_key:
        print("❌ BRIGHT_DATA_API_TOKEN not found in environment variables.")
        print("Please add it to your .env file:")
        print("BRIGHT_DATA_API_TOKEN=your_brightdata_api_key_here")
        return
    
    print("✅ API keys found. Starting pipeline...")
    print()
    
    # Run the pipeline
    run_full_pipeline(documentation_url, max_urls, max_workers)

if __name__ == "__main__":
    main()
