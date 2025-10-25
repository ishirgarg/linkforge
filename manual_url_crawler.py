"""
Manual URL Crawler
Extracts all URLs from a documentation page, then scrapes each URL individually.
"""

from brightdata import bdclient
import json
import re
import time
import os
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_all_urls_from_page(page_url: str) -> List[str]:
    """
    Extract all URLs from a single page.
    
    Args:
        page_url: The documentation page to extract URLs from
        
    Returns:
        List of all URLs found on the page
    """
    print(f"🔍 Extracting URLs from: {page_url}")
    
    # Initialize Bright Data client
    api_token = os.getenv('BRIGHT_DATA_API_TOKEN')
    if not api_token:
        raise ValueError("BRIGHT_DATA_API_TOKEN not found in environment variables. Please check your .env file.")
    
    client = bdclient(api_token=api_token)
    
    try:
        # Scrape the page to get its content
        result = client.scrape(
            url=page_url,
            data_format="raw",  # Get raw HTML for better link extraction
            country="US",
            timeout=30
        )
        
        if not result:
            print("❌ No content received from the page")
            return []
        
        # Extract URLs from the content
        urls = extract_urls_from_html(str(result), page_url)
        
        print(f"✅ Found {len(urls)} URLs on the page")
        return urls
        
    except Exception as e:
        print(f"❌ Error extracting URLs: {str(e)}")
        return []

def extract_urls_from_html(html_content: str, base_url: str) -> List[str]:
    """Extract all URLs from HTML content."""
    if not html_content:
        return []
    
    # Find all href attributes
    href_pattern = r'href=["\']([^"\']+)["\']'
    href_links = re.findall(href_pattern, html_content, re.IGNORECASE)
    
    # Find all src attributes (for images, scripts, etc.)
    src_pattern = r'src=["\']([^"\']+)["\']'
    src_links = re.findall(src_pattern, html_content, re.IGNORECASE)
    
    # Find all URLs in text content
    url_pattern = r'https?://[^\s<>"\'{}|\\^`\[\]]+'
    text_urls = re.findall(url_pattern, html_content)
    
    # Combine all found URLs
    all_links = href_links + src_links + text_urls
    
    # Convert relative URLs to absolute URLs
    absolute_urls = []
    for link in all_links:
        try:
            absolute_link = urljoin(base_url, link)
            absolute_urls.append(absolute_link)
        except:
            continue
    
    # Remove duplicates and filter out invalid URLs
    unique_urls = list(set(absolute_urls))
    valid_urls = [url for url in unique_urls if is_valid_url(url)]
    
    return valid_urls

def is_valid_url(url: str) -> bool:
    """Check if URL is valid."""
    try:
        parsed = urlparse(url)
        return parsed.scheme in ['http', 'https'] and parsed.netloc
    except:
        return False

def scrape_single_url(url: str) -> Dict[str, Any]:
    """
    Scrape a single URL using Bright Data API.
    
    Args:
        url: The URL to scrape
        
    Returns:
        Dictionary with scraped data
    """
    print(f"🔍 Scraping: {url}")
    
    # Initialize Bright Data client
    api_token = os.getenv('BRIGHT_DATA_API_TOKEN')
    if not api_token:
        raise ValueError("BRIGHT_DATA_API_TOKEN not found in environment variables. Please check your .env file.")
    
    client = bdclient(api_token=api_token)
    
    try:
        # Scrape the URL
        result = client.scrape(
            url=url,
            data_format="markdown",
            country="US",
            timeout=30
        )
        
        # Parse content
        parsed_content = client.parse_content(result) if result else ""
        
        return {
            "url": url,
            "content": parsed_content,
            "raw_result": result,
            "status": "success",
            "content_length": len(parsed_content),
            "timestamp": time.time()
        }
        
    except Exception as e:
        print(f"❌ Error scraping {url}: {str(e)}")
        return {
            "url": url,
            "content": "",
            "raw_result": None,
            "status": "error",
            "error": str(e),
            "timestamp": time.time()
        }

def crawl_manual_urls(documentation_url: str, max_urls: int = 50) -> List[Dict[str, Any]]:
    """
    Extract URLs from documentation page and scrape each one.
    
    Args:
        documentation_url: The documentation page to extract URLs from
        max_urls: Maximum number of URLs to scrape
        
    Returns:
        List of scraped data for each URL
    """
    print(f"📚 Starting manual URL extraction from: {documentation_url}")
    print(f"📊 Max URLs to scrape: {max_urls}")
    
    # Step 1: Extract all URLs from the documentation page
    all_urls = extract_all_urls_from_page(documentation_url)
    
    if not all_urls:
        print("❌ No URLs found on the documentation page")
        return []
    
    # Limit the number of URLs to scrape
    urls_to_scrape = all_urls[:max_urls]
    
    print(f"\n📋 URLs to scrape ({len(urls_to_scrape)}):")
    for i, url in enumerate(urls_to_scrape, 1):
        print(f"  {i}. {url}")
    
    print(f"\n🚀 Starting to scrape {len(urls_to_scrape)} URLs...")
    
    # Step 2: Scrape each URL individually
    scraped_data = []
    
    for i, url in enumerate(urls_to_scrape, 1):
        print(f"\n--- Scraping {i}/{len(urls_to_scrape)} ---")
        
        # Scrape the URL
        result = scrape_single_url(url)
        scraped_data.append(result)
        
        # Add delay between requests
        time.sleep(1)
    
    # Step 3: Save results
    timestamp = int(time.time())
    filename = f"manual_crawl_results_{timestamp}.json"
    
    summary = {
        "crawl_info": {
            "documentation_url": documentation_url,
            "total_urls_found": len(all_urls),
            "urls_scraped": len(scraped_data),
            "successful_scrapes": len([r for r in scraped_data if r["status"] == "success"]),
            "failed_scrapes": len([r for r in scraped_data if r["status"] == "error"]),
            "crawled_at": time.strftime("%Y-%m-%d %H:%M:%S")
        },
        "all_urls_found": all_urls,
        "scraped_data": scraped_data
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Manual crawling completed!")
    print(f"📊 Results:")
    print(f"  - URLs found: {len(all_urls)}")
    print(f"  - URLs scraped: {len(scraped_data)}")
    print(f"  - Successful: {len([r for r in scraped_data if r['status'] == 'success'])}")
    print(f"  - Failed: {len([r for r in scraped_data if r['status'] == 'error'])}")
    print(f"💾 Results saved to: {filename}")
    
    return scraped_data

def main():
    """Example usage."""
    print("🕷️ Manual URL Crawler")
    print("=" * 50)
    
    # Example: Extract URLs from Bright Data documentation
    documentation_url = "https://openai.github.io/openai-agents-python/"
    
    # Or use any other documentation page
    # documentation_url = "https://your-documentation-site.com"
    
    results = crawl_manual_urls(
        documentation_url=documentation_url,
        max_urls=20  # Adjust as needed
    )
    
    print(f"\n🎉 Manual crawling complete!")
    print(f"Check the generated JSON file for all scraped content.")

if __name__ == "__main__":
    main()
