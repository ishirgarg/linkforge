import os
import json
from dotenv import load_dotenv
from groq import Groq
from typing import List, Dict, Any
from dataclasses import dataclass

load_dotenv()

@dataclass
class ChunkTask:
    """Represents a chunk processing task."""
    chunk_id: str
    content: str
    url: str
    is_first: bool
    is_last: bool
    chunk_index: int
    total_chunks: int

# ------------------------------
# Smart chunking function (from queue_based_processor.py)
# ------------------------------
def chunk_html_content(html_content: str, max_chunk_size: int = 8000) -> List[str]:
    """Chunk HTML content for processing."""
    import re
    if len(html_content) <= max_chunk_size:
        return [html_content]
    
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

# ------------------------------
# Create context-aware prompts (from queue_based_processor.py)
# ------------------------------
def create_prompt(task: ChunkTask) -> str:
    """Create a prompt for the given task."""
    if task.is_first and task.is_last:
        return f"""
        Convert the following HTML content from a documentation page into clean, well-structured markdown.
        
        URL: {task.url}
        
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
        {task.content}
        """
    elif task.is_first:
        return f"""
        Convert the following HTML content (first part of {task.total_chunks}) from a documentation page into clean, well-structured markdown.
        
        URL: {task.url}
        
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
        {task.content}
        """
    elif task.is_last:
        return f"""
        Convert the following HTML content (last part of {task.total_chunks}) from a documentation page into clean, well-structured markdown.
        
        URL: {task.url}
        
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
        {task.content}
        """
    else:
        return f"""
        Convert the following HTML content (part {task.chunk_index} of {task.total_chunks}) from a documentation page into clean, well-structured markdown.
        
        URL: {task.url}
        
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
        {task.content}
        """

# ------------------------------
# Combine processed chunks (smart deduplication)
# ------------------------------
def combine_chunks(processed_chunks: List[str], url: str) -> str:
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

# ------------------------------
# Groq client initialization (lazy loading)
# ------------------------------
_client = None

def get_groq_client():
    """Get or create Groq client (lazy loading)."""
    global _client
    if _client is None:
        _client = Groq(api_key=os.getenv("Grok"))
    return _client

# ------------------------------
# Main processing function
# ------------------------------
def process_documents_with_groq(scraped_data: List[Dict[str, Any]], output_dir: str = "documentation_markdown") -> List[Dict[str, Any]]:
    """
    Process scraped documents with Groq using smart chunking.
    
    Args:
        scraped_data: List of scraped document data
        output_dir: Directory to save markdown files
        
    Returns:
        List of processed documents with markdown content
    """
    from pathlib import Path
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    processed_data = []
    client = get_groq_client()
    
    print(f"📊 Found {len(scraped_data)} pages to process")

    for i, page in enumerate(scraped_data, 1):
        url = page.get("url", f"doc_{i}")
        status = page.get("status")
        raw_result = page.get("raw_result", "")

        print(f"\n📄 Processing {i}/{len(scraped_data)}: {url}")

        if status != "success" or not raw_result:
            print(f"⚠️ Skipping (no content or error)")
            page["markdown_content"] = None
            page["markdown_file"] = None
            processed_data.append(page)
            continue

        try:
            # Chunk the HTML content
            html_content = str(raw_result)
            chunks = chunk_html_content(html_content)
            print(f"   Split into {len(chunks)} chunks")
            
            # Process each chunk with context-aware prompts
            processed_chunks = []
            for j, chunk in enumerate(chunks, 1):
                print(f"   Processing chunk {j}/{len(chunks)}...", end=" ")
                
                # Create ChunkTask for context-aware processing
                task = ChunkTask(
                    chunk_id=f"{url}_chunk_{j}",
                    content=chunk,
                    url=url,
                    is_first=(j == 1),
                    is_last=(j == len(chunks)),
                    chunk_index=j,
                    total_chunks=len(chunks)
                )
                
                try:
                    response = client.chat.completions.create(
                        messages=[{"role": "user", "content": create_prompt(task)}],
                        model="llama-3.3-70b-versatile"
                    )
                    processed_chunks.append(response.choices[0].message.content)
                    print("✅")
                except Exception as chunk_error:
                    print(f"❌ Chunk {j} failed: {str(chunk_error)}")
                    processed_chunks.append(f"# Error Processing Chunk {j}\n\n{str(chunk_error)}")
            
            # Combine chunks with smart deduplication
            markdown_content = combine_chunks(processed_chunks, url)
            
            # Save markdown in organized folder
            url_safe = url.replace('https://', '').replace('http://', '').replace('/', '_')
            filename = f"{i:03d}_{url_safe}.md"
            filepath = output_path / filename
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_content)

            page["markdown_content"] = markdown_content
            page["markdown_file"] = str(filepath)
            processed_data.append(page)

            print(f"   💾 Saved: {filepath}")
            
        except Exception as e:
            print(f"   ❌ Error processing: {str(e)}")
            page["markdown_content"] = None
            page["markdown_file"] = None
            page["error"] = str(e)
            processed_data.append(page)

    return processed_data

# ------------------------------
# Standalone execution (for testing)
# ------------------------------
if __name__ == "__main__":
    # Load test data for standalone execution
    with open("manual_crawl_results_1761367644.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    scraped_data = data.get("scraped_data", [])
    if not scraped_data:
        print("❌ No scraped data found in the file.")
        exit(1)

    processed_data = process_documents_with_groq(scraped_data)
    
    # Save final processed JSON
    with open("test_processed.json", "w", encoding="utf-8") as f:
        json.dump({"scraped_data": processed_data}, f, indent=2, ensure_ascii=False)

    print("✅ Processing complete, results saved to test_processed.json")
