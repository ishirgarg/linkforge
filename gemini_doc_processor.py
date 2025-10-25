"""
Gemini Documentation Processor
Uses Google Gemini API to convert HTML content into summarized markdown documentation.
"""

import os
import json
import requests
import time
from typing import List, Dict, Any
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GeminiDocProcessor:
    def __init__(self, api_key: str = None, max_calls_per_minute: int = 10):
        """Initialize the Gemini documentation processor."""
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent"
        self.headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': self.api_key
        }
        
        # Rate limiting
        self.max_calls_per_minute = max_calls_per_minute
        self.api_calls = []  # Track timestamps of API calls
        
        # Create output directory
        self.output_dir = Path("documentation_markdown")
        self.output_dir.mkdir(exist_ok=True)
        
        print("🤖 Gemini Documentation Processor initialized!")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"⏱️ Rate limit: {max_calls_per_minute} calls per minute")
    
    def _clean_old_calls(self):
        """Remove API calls older than 1 minute."""
        current_time = time.time()
        self.api_calls = [call_time for call_time in self.api_calls if current_time - call_time < 60]
    
    def _wait_for_rate_limit(self):
        """Wait if we're at the rate limit."""
        self._clean_old_calls()
        
        if len(self.api_calls) >= self.max_calls_per_minute:
            # Calculate how long to wait
            oldest_call = min(self.api_calls)
            wait_time = 60 - (time.time() - oldest_call) + 1  # Add 1 second buffer
            
            if wait_time > 0:
                print(f"⏳ Rate limit reached. Waiting {wait_time:.1f} seconds...")
                time.sleep(wait_time)
                self._clean_old_calls()
    
    def _record_api_call(self):
        """Record that we made an API call."""
        self.api_calls.append(time.time())
    
    def get_rate_limit_status(self):
        """Get current rate limit status."""
        self._clean_old_calls()
        remaining_calls = self.max_calls_per_minute - len(self.api_calls)
        return {
            'calls_made': len(self.api_calls),
            'max_calls': self.max_calls_per_minute,
            'remaining_calls': remaining_calls,
            'reset_in_seconds': 60 - (time.time() - min(self.api_calls)) if self.api_calls else 0
        }
    
    def chunk_html_content(self, html_content: str, max_chunk_size: int = 30000) -> list:
        """
        Intelligently chunk content for processing (handles both HTML and markdown-like content).
        
        Args:
            html_content: Raw content (HTML or markdown-like)
            max_chunk_size: Maximum characters per chunk
            
        Returns:
            List of content chunks
        """
        if len(html_content) <= max_chunk_size:
            return [html_content]
        
        import re
        
        # First, try to detect if this is HTML or markdown-like content
        is_html = bool(re.search(r'<[^>]+>', html_content))
        
        if is_html:
            # Split by major sections (h1, h2, h3 tags)
            heading_pattern = r'(<h[1-3][^>]*>.*?</h[1-3]>)'
            parts = re.split(heading_pattern, html_content, flags=re.IGNORECASE | re.DOTALL)
        else:
            # Split by markdown headings (# ## ###)
            heading_pattern = r'(^#{1,3}\s+.*$)'
            parts = re.split(heading_pattern, html_content, flags=re.MULTILINE)
        
        chunks = []
        current_chunk = ""
        
        for part in parts:
            if len(current_chunk + part) <= max_chunk_size:
                current_chunk += part
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = part
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        # If we still have chunks that are too large, split them further
        final_chunks = []
        for chunk in chunks:
            if len(chunk) <= max_chunk_size:
                final_chunks.append(chunk)
            else:
                # Split by paragraphs or code blocks
                sub_chunks = self._split_large_chunk(chunk, max_chunk_size)
                final_chunks.extend(sub_chunks)
        
        return final_chunks
    
    def _split_large_chunk(self, chunk: str, max_size: int) -> list:
        """Split a large chunk into smaller pieces."""
        import re
        
        # Try to split by code blocks first (works for both HTML and markdown)
        code_pattern = r'(```[^`]*```|<pre[^>]*>.*?</pre>|<code[^>]*>.*?</code>)'
        parts = re.split(code_pattern, chunk, flags=re.IGNORECASE | re.DOTALL)
        
        if len(parts) > 1:
            sub_chunks = []
            current = ""
            for part in parts:
                if len(current + part) <= max_size:
                    current += part
                else:
                    if current:
                        sub_chunks.append(current.strip())
                    current = part
            if current:
                sub_chunks.append(current.strip())
            return sub_chunks
        
        # Try to split by double newlines (markdown paragraphs)
        para_pattern = r'(\n\s*\n)'
        parts = re.split(para_pattern, chunk)
        
        if len(parts) > 1:
            sub_chunks = []
            current = ""
            for part in parts:
                if len(current + part) <= max_size:
                    current += part
                else:
                    if current:
                        sub_chunks.append(current.strip())
                    current = part
            if current:
                sub_chunks.append(current.strip())
            return sub_chunks
        
        # If no paragraphs, split by single newlines
        line_pattern = r'(\n)'
        parts = re.split(line_pattern, chunk)
        
        sub_chunks = []
        current = ""
        for part in parts:
            if len(current + part) <= max_size:
                current += part
            else:
                if current:
                    sub_chunks.append(current.strip())
                current = part
        if current:
            sub_chunks.append(current.strip())
        
        return sub_chunks

    def process_html_to_markdown(self, html_content: str, url: str) -> str:
        """
        Convert HTML content to summarized markdown using Gemini with smart chunking.
        
        Args:
            html_content: Raw HTML content
            url: The URL of the page
            
        Returns:
            Summarized markdown content
        """
        print(f"🔄 Processing: {url}")
        
        # Chunk the HTML content
        print(f"📏 Content length: {len(html_content)} characters")
        chunks = self.chunk_html_content(html_content, max_chunk_size=8000)  # Smaller chunks for better reliability
        print(f"📄 Split into {len(chunks)} chunks")
        
        # Debug: Show chunk sizes
        for i, chunk in enumerate(chunks):
            print(f"  Chunk {i+1}: {len(chunk)} characters")
        
        if len(chunks) == 1:
            # Single chunk - process normally
            return self._process_single_chunk(chunks[0], url, is_first=True, is_last=True)
        
        # Multiple chunks - process each and combine
        processed_chunks = []
        
        for i, chunk in enumerate(chunks):
            print(f"  📝 Processing chunk {i+1}/{len(chunks)}")
            is_first = (i == 0)
            is_last = (i == len(chunks) - 1)
            
            chunk_result = self._process_single_chunk(chunk, url, is_first, is_last, chunk_index=i+1, total_chunks=len(chunks))
            processed_chunks.append(chunk_result)
            
            # Rate limiting is now handled automatically in _make_gemini_request
        
        # Combine the results
        return self._combine_chunks(processed_chunks, url)
    
    def _process_single_chunk(self, html_chunk: str, url: str, is_first: bool = True, is_last: bool = True, chunk_index: int = 1, total_chunks: int = 1) -> str:
        """Process a single HTML chunk with retry logic."""
        max_retries = 3
        retry_delay = 2
        
        for attempt in range(max_retries):
            try:
                return self._make_gemini_request(html_chunk, url, is_first, is_last, chunk_index, total_chunks)
            except Exception as e:
                print(f"  ⚠️ Attempt {attempt + 1}/{max_retries} failed for chunk {chunk_index}: {str(e)}")
                if attempt < max_retries - 1:
                    print(f"  🔄 Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    print(f"  ❌ All retry attempts failed for chunk {chunk_index}")
                    return f"# Error Processing Chunk {chunk_index}\n\nFailed to process after {max_retries} attempts.\n\nError: {str(e)}"
    
    def _make_gemini_request(self, html_chunk: str, url: str, is_first: bool, is_last: bool, chunk_index: int, total_chunks: int) -> str:
        """Make the actual Gemini API request."""
        # Create appropriate prompt based on chunk position
        if is_first and is_last:
            # Single chunk
            prompt = f"""
            Convert the following HTML content from a documentation page into clean, well-structured markdown.
            
            URL: {url}
            
            Requirements:
            1. Extract the main content and structure
            2. Convert headings, lists, code blocks, and links properly
            3. Remove navigation elements, sidebars, and non-content elements
            4. Create a clear hierarchy with proper markdown headings
            5. Preserve code examples and technical details
            6. Make it readable and well-formatted
            7. Add a title at the top based on the page content
            8. Include the original URL as a reference
            
            HTML Content:
            {html_chunk}
            """
        elif is_first:
            # First chunk
            prompt = f"""
            Convert the following HTML content (first part of {total_chunks}) from a documentation page into clean, well-structured markdown.
            
            URL: {url}
            
            Requirements:
            1. Extract the main content and structure
            2. Convert headings, lists, code blocks, and links properly
            3. Remove navigation elements, sidebars, and non-content elements
            4. Create a clear hierarchy with proper markdown headings
            5. Preserve code examples and technical details
            6. Make it readable and well-formatted
            7. Add a title at the top based on the page content
            8. Include the original URL as a reference
            9. This is the FIRST part - include the main title and introduction
            
            HTML Content:
            {html_chunk}
            """
        elif is_last:
            # Last chunk
            prompt = f"""
            Convert the following HTML content (last part of {total_chunks}) from a documentation page into clean, well-structured markdown.
            
            URL: {url}
            
            Requirements:
            1. Extract the main content and structure
            2. Convert headings, lists, code blocks, and links properly
            3. Remove navigation elements, sidebars, and non-content elements
            4. Create a clear hierarchy with proper markdown headings
            5. Preserve code examples and technical details
            6. Make it readable and well-formatted
            7. This is the LAST part - include conclusion and final sections
            8. Do NOT include a title (it should be in the first chunk)
            
            HTML Content:
            {html_chunk}
            """
        else:
            # Middle chunk
            prompt = f"""
            Convert the following HTML content (part {chunk_index} of {total_chunks}) from a documentation page into clean, well-structured markdown.
            
            URL: {url}
            
            Requirements:
            1. Extract the main content and structure
            2. Convert headings, lists, code blocks, and links properly
            3. Remove navigation elements, sidebars, and non-content elements
            4. Create a clear hierarchy with proper markdown headings
            5. Preserve code examples and technical details
            6. Make it readable and well-formatted
            7. This is a MIDDLE part - continue the content flow
            8. Do NOT include a title (it should be in the first chunk)
            
            HTML Content:
            {html_chunk}
            """
        
        try:
            # Check rate limit before making request
            self._wait_for_rate_limit()
            
            # Make API request to Gemini
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json={
                    "contents": [
                        {
                            "parts": [
                                {
                                    "text": prompt
                                }
                            ]
                        }
                    ],
                    "generationConfig": {
                        "temperature": 0.1,
                        "maxOutputTokens": 6000,  # Increased for better content
                        "topP": 0.8,
                        "topK": 10
                    }
                },
                timeout=60  # Increased timeout for large chunks
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # Better error handling for response structure
                if 'candidates' not in result:
                    raise Exception(f"Invalid response: missing 'candidates' field. Response: {result}")
                
                if len(result['candidates']) == 0:
                    raise Exception(f"No candidates in response. Response: {result}")
                
                candidate = result['candidates'][0]
                if 'content' not in candidate:
                    raise Exception(f"Invalid candidate: missing 'content' field. Candidate: {candidate}")
                
                if 'parts' not in candidate['content']:
                    raise Exception(f"Invalid content: missing 'parts' field. Content: {candidate['content']}")
                
                if len(candidate['content']['parts']) == 0:
                    raise Exception(f"No parts in content. Content: {candidate['content']}")
                
                if 'text' not in candidate['content']['parts'][0]:
                    raise Exception(f"Invalid part: missing 'text' field. Part: {candidate['content']['parts'][0]}")
                
                markdown_content = candidate['content']['parts'][0]['text']
                print(f"  ✅ Chunk {chunk_index} processed successfully")
                
                # Record this API call for rate limiting
                self._record_api_call()
                
                return markdown_content
            else:
                error_msg = f"API Error {response.status_code}"
                try:
                    error_detail = response.json()
                    error_msg += f": {error_detail}"
                except:
                    error_msg += f": {response.text}"
                raise Exception(error_msg)
                
        except requests.exceptions.Timeout:
            raise Exception("Request timed out after 60 seconds")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")
        except KeyError as e:
            raise Exception(f"Unexpected response format - missing key: {str(e)}")
        except Exception as e:
            raise Exception(f"Processing error: {str(e)}")
    
    def _combine_chunks(self, processed_chunks: list, url: str) -> str:
        """Combine processed chunks into a single markdown document."""
        print(f"🔗 Combining {len(processed_chunks)} chunks...")
        
        # Filter out error chunks and count them
        valid_chunks = []
        error_chunks = []
        
        for i, chunk in enumerate(processed_chunks):
            if chunk.startswith('# Error Processing Chunk') or chunk.startswith('# API Error Chunk') or chunk.startswith('# Processing Error Chunk'):
                error_chunks.append(i + 1)
            else:
                valid_chunks.append((i, chunk))
        
        if error_chunks:
            print(f"⚠️ Warning: {len(error_chunks)} chunks failed to process: {error_chunks}")
        
        if not valid_chunks:
            return f"# Error Processing Page\n\nAll chunks failed to process for: {url}\n\nThis page could not be converted to markdown."
        
        # Start with the first valid chunk (should have the title)
        combined = valid_chunks[0][1]
        
        # Add subsequent valid chunks, removing duplicate titles
        for i, chunk in valid_chunks[1:]:
            # Remove any duplicate titles from subsequent chunks
            lines = chunk.split('\n')
            filtered_lines = []
            skip_title = True
            
            for line in lines:
                if skip_title and (line.startswith('# ') or line.startswith('**Original URL:**')):
                    continue
                elif line.startswith('---') and skip_title:
                    skip_title = False
                    continue
                else:
                    skip_title = False
                    filtered_lines.append(line)
            
            # Add the filtered chunk
            if filtered_lines:
                combined += '\n\n' + '\n'.join(filtered_lines)
        
        # Add error summary if there were failed chunks
        if error_chunks:
            combined += f"\n\n---\n\n**Note:** Some sections of this page failed to process (chunks {', '.join(map(str, error_chunks))}). The content above represents the successfully processed portions."
        
        print(f"✅ Successfully combined {len(valid_chunks)} valid chunks")
        return combined
    
    def save_markdown(self, markdown_content: str, url: str, index: int) -> str:
        """
        Save markdown content to a file.
        
        Args:
            markdown_content: The markdown content to save
            url: The original URL
            index: Page index number
            
        Returns:
            The filename where content was saved
        """
        # Create filename from URL
        url_parts = url.replace('https://', '').replace('http://', '').split('/')
        domain = url_parts[0]
        path_parts = url_parts[1:] if len(url_parts) > 1 else []
        
        # Clean up path parts
        clean_parts = []
        for part in path_parts:
            # Remove file extensions and clean up
            clean_part = part.replace('.html', '').replace('.htm', '')
            if clean_part and clean_part != 'index':
                clean_parts.append(clean_part)
        
        # Create filename
        if clean_parts:
            filename = f"{index:03d}_{'_'.join(clean_parts)}.md"
        else:
            filename = f"{index:03d}_homepage.md"
        
        # Ensure filename is safe
        filename = "".join(c for c in filename if c.isalnum() or c in "._-")
        
        filepath = self.output_dir / filename
        
        # Save the markdown content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"💾 Saved: {filepath}")
        return str(filepath)
    
    def process_scraped_data(self, scraped_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process all scraped data and convert to markdown.
        
        Args:
            scraped_data: List of scraped page data
            
        Returns:
            List of processed data with markdown content
        """
        print(f"🚀 Processing {len(scraped_data)} pages with Gemini...")
        
        processed_data = []
        
        for i, page_data in enumerate(scraped_data, 1):
            print(f"\n--- Processing {i}/{len(scraped_data)} ---")
            
            # Show rate limit status
            status = self.get_rate_limit_status()
            print(f"📊 Rate limit: {status['calls_made']}/{status['max_calls']} calls used, {status['remaining_calls']} remaining")
            
            url = page_data['url']
            
            if page_data['status'] == 'success' and page_data.get('raw_result'):
                # Get raw HTML content
                html_content = str(page_data['raw_result'])
                
                # Process with Gemini
                markdown_content = self.process_html_to_markdown(html_content, url)
                
                # Save markdown file
                markdown_file = self.save_markdown(markdown_content, url, i)
                
                # Update page data
                page_data['markdown_content'] = markdown_content
                page_data['markdown_file'] = markdown_file
                page_data['processed_at'] = time.time()
                
            else:
                print(f"⚠️ Skipping {url} - no content or error")
                page_data['markdown_content'] = f"# Error\n\nCould not process this page: {url}\n\nStatus: {page_data.get('status', 'unknown')}"
                page_data['markdown_file'] = None
                page_data['processed_at'] = time.time()
            
            processed_data.append(page_data)
            
            # Rate limiting is now handled automatically per API call
        
        return processed_data
    
    def create_index_file(self, processed_data: List[Dict[str, Any]]) -> str:
        """Create an index file listing all processed documentation."""
        index_content = "# Documentation Index\n\n"
        index_content += f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        index_content += f"Total pages processed: {len(processed_data)}\n\n"
        
        index_content += "## Pages\n\n"
        
        for i, page_data in enumerate(processed_data, 1):
            url = page_data['url']
            status = page_data['status']
            markdown_file = page_data.get('markdown_file', 'Not processed')
            
            if markdown_file and markdown_file != 'Not processed':
                filename = os.path.basename(markdown_file)
                index_content += f"{i}. [{url}]({filename}) - {status}\n"
            else:
                index_content += f"{i}. {url} - {status} (Not processed)\n"
        
        # Save index file
        index_file = self.output_dir / "README.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"📋 Created index file: {index_file}")
        return str(index_file)


def main():
    """Example usage of the Gemini documentation processor."""
    print("🤖 Gemini Documentation Processor")
    print("=" * 50)
    
    # Initialize processor with rate limiting
    processor = GeminiDocProcessor(max_calls_per_minute=30)
    
    # Check if we have scraped data to process
    # Look for the most recent manual crawl results
    import glob
    
    result_files = glob.glob("manual_crawl_results_*.json")
    if not result_files:
        print("❌ No scraped data found. Please run manual_url_crawler.py first.")
        return
    
    # Use the most recent file
    latest_file = max(result_files, key=os.path.getctime)
    print(f"📂 Loading scraped data from: {latest_file}")
    
    # Load scraped data
    with open(latest_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    scraped_data = data.get('scraped_data', [])
    
    if not scraped_data:
        print("❌ No scraped data found in the file.")
        return
    
    print(f"📊 Found {len(scraped_data)} pages to process")
    
    # Process all pages
    processed_data = processor.process_scraped_data(scraped_data)
    
    # Create index file
    index_file = processor.create_index_file(processed_data)
    
    # Save processed results
    timestamp = int(time.time())
    results_file = f"gemini_processed_results_{timestamp}.json"
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Processing completed!")
    print(f"📁 Markdown files saved to: {processor.output_dir}")
    print(f"📋 Index file: {index_file}")
    print(f"💾 Full results saved to: {results_file}")
    
    # Show summary
    successful = len([p for p in processed_data if p.get('markdown_file')])
    failed = len(processed_data) - successful
    
    print(f"\n📊 Summary:")
    print(f"  - Total pages: {len(processed_data)}")
    print(f"  - Successfully processed: {successful}")
    print(f"  - Failed: {failed}")


if __name__ == "__main__":
    main()
