"""
Multi-Model Gemini Documentation Processor
Uses multiple Gemini models with their respective rate limits for maximum throughput.
"""

import os
import json
import requests
import time
import random
from typing import List, Dict, Any
from pathlib import Path
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Load environment variables
load_dotenv()

class MultiModelGeminiProcessor:
    def __init__(self, api_key: str = None):
        """Initialize the multi-model Gemini processor."""
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        self.headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': self.api_key
        }
        
        # Multi-model configuration with rate limits
        self.models = {
            'gemini-2.5-pro': {
                'base_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent',
                'rpm': 5,
                'max_tokens': 125000,
                'calls': [],
                'lock': threading.Lock()
            },
            'gemini-2.5-flash': {
                'base_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent',
                'rpm': 10,
                'max_tokens': 250000,
                'calls': [],
                'lock': threading.Lock()
            },
            'gemini-2.5-flash-preview': {
                'base_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview:generateContent',
                'rpm': 10,
                'max_tokens': 250000,
                'calls': [],
                'lock': threading.Lock()
            },
            'gemini-2.5-flash-lite': {
                'base_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent',
                'rpm': 15,
                'max_tokens': 250000,
                'calls': [],
                'lock': threading.Lock()
            },
            'gemini-2.5-flash-lite-preview': {
                'base_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite-preview:generateContent',
                'rpm': 15,
                'max_tokens': 250000,
                'calls': [],
                'lock': threading.Lock()
            },
            'gemini-2.0-flash': {
                'base_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent',
                'rpm': 15,
                'max_tokens': 1000000,
                'calls': [],
                'lock': threading.Lock()
            },
            'gemini-2.0-flash-lite': {
                'base_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent',
                'rpm': 30,
                'max_tokens': 1000000,
                'calls': [],
                'lock': threading.Lock()
            }
        }
        
        # Create output directory
        self.output_dir = Path("documentation_markdown")
        self.output_dir.mkdir(exist_ok=True)
        
        # Calculate total theoretical throughput
        total_rpm = sum(model['rpm'] for model in self.models.values())
        
        print("🚀 Multi-Model Gemini Processor initialized!")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"⚡ Total theoretical throughput: {total_rpm} calls/minute")
        print(f"🤖 Available models: {len(self.models)}")
        for model_name, config in self.models.items():
            print(f"  - {model_name}: {config['rpm']} RPM, {config['max_tokens']:,} tokens")
    
    def _clean_old_calls(self, model_name: str):
        """Remove API calls older than 1 minute for a specific model."""
        with self.models[model_name]['lock']:
            current_time = time.time()
            self.models[model_name]['calls'] = [
                call_time for call_time in self.models[model_name]['calls'] 
                if current_time - call_time < 60
            ]
    
    def _get_available_model(self) -> str:
        """Get the best available model based on current rate limits."""
        available_models = []
        
        for model_name, config in self.models.items():
            self._clean_old_calls(model_name)
            with config['lock']:
                remaining_calls = config['rpm'] - len(config['calls'])
                if remaining_calls > 0:
                    available_models.append((model_name, remaining_calls, config['rpm']))
        
        if not available_models:
            return None
        
        # Prefer models with higher remaining capacity
        available_models.sort(key=lambda x: x[1], reverse=True)
        return available_models[0][0]
    
    def _wait_for_model_availability(self, model_name: str):
        """Wait for a specific model to become available."""
        config = self.models[model_name]
        
        while True:
            self._clean_old_calls(model_name)
            with config['lock']:
                if len(config['calls']) < config['rpm']:
                    return
                
                # Calculate wait time
                oldest_call = min(config['calls'])
                wait_time = 60 - (time.time() - oldest_call) + 1
                
                if wait_time > 0:
                    print(f"⏳ {model_name} rate limit reached. Waiting {wait_time:.1f}s...")
                    time.sleep(wait_time)
    
    def _record_api_call(self, model_name: str):
        """Record an API call for a specific model."""
        with self.models[model_name]['lock']:
            self.models[model_name]['calls'].append(time.time())
    
    def _make_gemini_request(self, html_chunk: str, url: str, model_name: str, 
                           is_first: bool = True, is_last: bool = True, 
                           chunk_index: int = 1, total_chunks: int = 1) -> str:
        """Make a Gemini API request using a specific model."""
        config = self.models[model_name]
        
        # Wait for model availability
        self._wait_for_model_availability(model_name)
        
        # Create prompt based on chunk position
        if is_first and is_last:
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
            # Make API request
            response = requests.post(
                config['base_url'],
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
                        "maxOutputTokens": min(6000, config['max_tokens']),
                        "topP": 0.8,
                        "topK": 10
                    }
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # Validate response structure
                if 'candidates' not in result or len(result['candidates']) == 0:
                    raise Exception(f"Invalid response: {result}")
                
                candidate = result['candidates'][0]
                if 'content' not in candidate or 'parts' not in candidate['content'] or len(candidate['content']['parts']) == 0:
                    raise Exception(f"Invalid candidate structure: {candidate}")
                
                if 'text' not in candidate['content']['parts'][0]:
                    raise Exception(f"Missing text in response: {candidate['content']['parts'][0]}")
                
                markdown_content = candidate['content']['parts'][0]['text']
                
                # Record successful API call
                self._record_api_call(model_name)
                
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
        except Exception as e:
            raise Exception(f"Processing error: {str(e)}")
    
    def chunk_html_content(self, html_content: str, max_chunk_size: int = 8000) -> list:
        """Intelligently chunk content for processing."""
        if len(html_content) <= max_chunk_size:
            return [html_content]
        
        import re
        
        # Detect if this is HTML or markdown-like content
        is_html = bool(re.search(r'<[^>]+>', html_content))
        
        if is_html:
            heading_pattern = r'(<h[1-3][^>]*>.*?</h[1-3]>)'
            parts = re.split(heading_pattern, html_content, flags=re.IGNORECASE | re.DOTALL)
        else:
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
        
        # Further split large chunks
        final_chunks = []
        for chunk in chunks:
            if len(chunk) <= max_chunk_size:
                final_chunks.append(chunk)
            else:
                # Split by paragraphs
                para_pattern = r'(\n\s*\n)'
                parts = re.split(para_pattern, chunk)
                
                sub_chunks = []
                current = ""
                for part in parts:
                    if len(current + part) <= max_chunk_size:
                        current += part
                    else:
                        if current:
                            sub_chunks.append(current.strip())
                        current = part
                if current:
                    sub_chunks.append(current.strip())
                
                final_chunks.extend(sub_chunks)
        
        return final_chunks
    
    def process_html_to_markdown(self, html_content: str, url: str) -> str:
        """Convert HTML content to markdown using multi-model approach."""
        print(f"🔄 Processing: {url}")
        
        # Chunk the content
        chunks = self.chunk_html_content(html_content, max_chunk_size=8000)
        print(f"📄 Split into {len(chunks)} chunks")
        
        if len(chunks) == 1:
            # Single chunk - get best available model
            model_name = self._get_available_model()
            if not model_name:
                return f"# Error\n\nNo models available for processing: {url}"
            
            print(f"🤖 Using model: {model_name}")
            return self._make_gemini_request(chunks[0], url, model_name, is_first=True, is_last=True)
        
        # Multiple chunks - process concurrently
        processed_chunks = []
        
        with ThreadPoolExecutor(max_workers=min(len(chunks), 7)) as executor:
            # Submit all chunks
            future_to_chunk = {}
            
            for i, chunk in enumerate(chunks):
                # Get available model for this chunk
                model_name = self._get_available_model()
                if not model_name:
                    # Wait a bit and try again
                    time.sleep(1)
                    model_name = self._get_available_model()
                    if not model_name:
                        model_name = 'gemini-2.0-flash-lite'  # Fallback to highest capacity model
                
                is_first = (i == 0)
                is_last = (i == len(chunks) - 1)
                
                future = executor.submit(
                    self._make_gemini_request, 
                    chunk, url, model_name, is_first, is_last, i+1, len(chunks)
                )
                future_to_chunk[future] = (i, model_name)
            
            # Process completed chunks
            for future in as_completed(future_to_chunk):
                chunk_index, model_name = future_to_chunk[future]
                
                try:
                    result = future.result()
                    processed_chunks.append((chunk_index, result))
                    print(f"  ✅ Chunk {chunk_index + 1} completed with {model_name}")
                except Exception as e:
                    print(f"  ❌ Chunk {chunk_index + 1} failed with {model_name}: {str(e)}")
                    processed_chunks.append((chunk_index, f"# Error Processing Chunk {chunk_index + 1}\n\nError: {str(e)}"))
        
        # Sort chunks by index and combine
        processed_chunks.sort(key=lambda x: x[0])
        combined_chunks = [chunk[1] for chunk in processed_chunks]
        
        return self._combine_chunks(combined_chunks, url)
    
    def _combine_chunks(self, processed_chunks: list, url: str) -> str:
        """Combine processed chunks into a single markdown document."""
        print(f"🔗 Combining {len(processed_chunks)} chunks...")
        
        # Filter out error chunks
        valid_chunks = []
        error_chunks = []
        
        for i, chunk in enumerate(processed_chunks):
            if chunk.startswith('# Error Processing Chunk'):
                error_chunks.append(i + 1)
            else:
                valid_chunks.append((i, chunk))
        
        if error_chunks:
            print(f"⚠️ Warning: {len(error_chunks)} chunks failed: {error_chunks}")
        
        if not valid_chunks:
            return f"# Error Processing Page\n\nAll chunks failed to process for: {url}"
        
        # Start with first valid chunk
        combined = valid_chunks[0][1]
        
        # Add subsequent chunks, removing duplicate titles
        for i, chunk in valid_chunks[1:]:
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
            
            if filtered_lines:
                combined += '\n\n' + '\n'.join(filtered_lines)
        
        if error_chunks:
            combined += f"\n\n---\n\n**Note:** Some sections failed to process (chunks {', '.join(map(str, error_chunks))})."
        
        print(f"✅ Successfully combined {len(valid_chunks)} valid chunks")
        return combined
    
    def save_markdown(self, markdown_content: str, url: str, index: int) -> str:
        """Save markdown content to a file."""
        url_parts = url.replace('https://', '').replace('http://', '').split('/')
        domain = url_parts[0]
        path_parts = url_parts[1:] if len(url_parts) > 1 else []
        
        clean_parts = []
        for part in path_parts:
            clean_part = part.replace('.html', '').replace('.htm', '')
            if clean_part and clean_part != 'index':
                clean_parts.append(clean_part)
        
        if clean_parts:
            filename = f"{index:03d}_{'_'.join(clean_parts)}.md"
        else:
            filename = f"{index:03d}_homepage.md"
        
        filename = "".join(c for c in filename if c.isalnum() or c in "._-")
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"💾 Saved: {filepath}")
        return str(filepath)
    
    def process_scraped_data(self, scraped_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process all scraped data using multi-model approach."""
        print(f"🚀 Processing {len(scraped_data)} pages with Multi-Model Gemini...")
        
        processed_data = []
        
        for i, page_data in enumerate(scraped_data, 1):
            print(f"\n--- Processing {i}/{len(scraped_data)} ---")
            
            # Show current model status
            available_models = []
            for model_name, config in self.models.items():
                self._clean_old_calls(model_name)
                with config['lock']:
                    remaining = config['rpm'] - len(config['calls'])
                    available_models.append(f"{model_name}({remaining})")
            
            print(f"📊 Available models: {', '.join(available_models)}")
            
            url = page_data['url']
            
            if page_data['status'] == 'success' and page_data.get('raw_result'):
                html_content = str(page_data['raw_result'])
                markdown_content = self.process_html_to_markdown(html_content, url)
                markdown_file = self.save_markdown(markdown_content, url, i)
                
                page_data['markdown_content'] = markdown_content
                page_data['markdown_file'] = markdown_file
                page_data['processed_at'] = time.time()
            else:
                print(f"⚠️ Skipping {url} - no content or error")
                page_data['markdown_content'] = f"# Error\n\nCould not process: {url}"
                page_data['markdown_file'] = None
                page_data['processed_at'] = time.time()
            
            processed_data.append(page_data)
        
        return processed_data


def main():
    """Example usage of the multi-model processor."""
    print("🚀 Multi-Model Gemini Documentation Processor")
    print("=" * 60)
    
    # Initialize processor
    processor = MultiModelGeminiProcessor()
    
    # Load scraped data
    import glob
    result_files = glob.glob("manual_crawl_results_*.json")
    if not result_files:
        print("❌ No scraped data found. Please run manual_url_crawler.py first.")
        return
    
    latest_file = max(result_files, key=os.path.getctime)
    print(f"📂 Loading scraped data from: {latest_file}")
    
    with open(latest_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    scraped_data = data.get('scraped_data', [])
    if not scraped_data:
        print("❌ No scraped data found in the file.")
        return
    
    print(f"📊 Found {len(scraped_data)} pages to process")
    
    # Process all pages
    processed_data = processor.process_scraped_data(scraped_data)
    
    # Save results
    timestamp = int(time.time())
    results_file = f"multimodel_processed_results_{timestamp}.json"
    
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Multi-model processing completed!")
    print(f"📁 Markdown files saved to: {processor.output_dir}")
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
