# LinkForge 🔗

A powerful web scraper built with Bright Data's API that extracts comprehensive data from any website URL.

## Features

- **Single URL Scraping**: Extract all data from any website
- **Batch Processing**: Scrape multiple URLs concurrently for optimal performance
- **Web Search**: Search the web using Bright Data's SERP API
- **Multiple Formats**: Support for JSON and raw data formats
- **Error Handling**: Robust error handling and logging
- **Data Export**: Save results to JSON files

## Quick Start

### 1. Installation

```bash
pip install -r requirements.txt
```

### 2. Basic Usage

```python
from scraper import LinkForgeScraper

# Initialize scraper
scraper = LinkForgeScraper()

# Scrape a single website
result = scraper.scrape_url("https://example.com")
print(result['parsed_content'])

# Scrape multiple websites
urls = ["https://site1.com", "https://site2.com"]
results = scraper.scrape_multiple_urls(urls)

# Search the web
search_results = scraper.search_web("python web scraping")
```

### 3. Run Examples

```bash
python example_usage.py
```

## API Reference

### LinkForgeScraper Class

#### `scrape_url(url, format_type="json", country="US")`
Scrape a single URL and return comprehensive data.

**Parameters:**
- `url` (str): The website URL to scrape
- `format_type` (str): Response format - "json" or "raw"
- `country` (str): Two-letter country code for location-based scraping

**Returns:** Dictionary containing scraped data

#### `scrape_multiple_urls(urls, format_type="json", country="US")`
Scrape multiple URLs concurrently for optimal performance.

**Parameters:**
- `urls` (List[str]): List of website URLs to scrape
- `format_type` (str): Response format - "json" or "raw"
- `country` (str): Two-letter country code for location-based scraping

**Returns:** List of dictionaries containing scraped data for each URL

#### `search_web(query, search_engine="google", country="US")`
Search the web using Bright Data's SERP API.

**Parameters:**
- `query` (str): Search query
- `search_engine` (str): "google", "bing", or "yandex"
- `country` (str): Two-letter country code

**Returns:** Dictionary containing search results

## Configuration

The scraper uses your Bright Data API key. You can either:

1. **Pass it directly:**
   ```python
   scraper = LinkForgeScraper(api_token="your_api_key")
   ```

2. **Set environment variable:**
   ```bash
   export BRIGHTDATA_API_TOKEN="your_api_key"
   ```

## Examples

See `example_usage.py` for detailed usage examples including:
- Single website scraping
- Batch processing
- Web search functionality
- Data export

## Requirements

- Python 3.7+
- Bright Data API key
- Internet connection

## Dependencies

- `brightdata-sdk`: Bright Data's official Python SDK
- `python-dotenv`: Environment variable management

## License

MIT License