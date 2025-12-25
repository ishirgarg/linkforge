"""
Script to embed all markdown files from a folder into ChromaDB
Processes all .md files and adds them to the vector database
"""

import os
import glob
from pathlib import Path
from vector_db import ChromaVectorDB
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
MARKDOWN_FOLDER = "groq_documentation_markdown"
COLLECTION_NAME = "streamlit_api_50"  # Existing collection name
DB_PATH = "./chroma_db"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def process_markdown_folder():
    """Embed all markdown files from the folder into ChromaDB"""
    
    print("🚀 Embedding Markdown Documentation into ChromaDB")
    print("=" * 60)
    print(f"📁 Folder: {MARKDOWN_FOLDER}")
    print(f"💾 Database: {DB_PATH}")
    print(f"📚 Collection: {COLLECTION_NAME}")
    print("=" * 60)
    print()
    
    # Check if folder exists
    if not os.path.exists(MARKDOWN_FOLDER):
        print(f"❌ Error: Folder '{MARKDOWN_FOLDER}' not found!")
        return
    
    # Find all markdown files
    md_files = glob.glob(os.path.join(MARKDOWN_FOLDER, "*.md"))
    
    if not md_files:
        print(f"❌ No .md files found in '{MARKDOWN_FOLDER}'")
        return
    
    print(f"📄 Found {len(md_files)} markdown files\n")
    
    # Initialize vector database
    try:
        print(f"🔧 Initializing ChromaDB...")
        vector_db = ChromaVectorDB(
            path=DB_PATH,
            collection_name=COLLECTION_NAME,
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        print("✅ ChromaDB initialized successfully\n")
    except Exception as e:
        print(f"❌ Error initializing ChromaDB: {e}")
        return
    
    # Process each markdown file
    total_chunks = 0
    successful_files = 0
    failed_files = []
    
    for i, file_path in enumerate(sorted(md_files), 1):
        try:
            filename = os.path.basename(file_path)
            print(f"[{i}/{len(md_files)}] Processing: {filename}")
            
            # Read markdown content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Skip empty files
            if not content.strip():
                print(f"   ⚠️  Empty file, skipping")
                continue
            
            # Get file metadata for embedding
            file_id = filename.replace(".md", "")
            # Extract URL from filename if possible
            source_url = f"https://{filename.replace('.md', '').replace('_', '/')}"
            
            # Add document to vector database
            # Using insert method which handles chunking and embedding
            vector_db.insert(
                documents=[content],
                ids=[file_id]
            )
            
            # Count chunks (rough estimate: chunk_size words)
            import math
            word_count = len(content.split())
            chunks = math.ceil(word_count / CHUNK_SIZE)
            total_chunks += chunks
            successful_files += 1
            
            print(f"   ✅ Added {chunks} chunk(s)")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            failed_files.append((filename, str(e)))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Embedding Summary")
    print("=" * 60)
    print(f"✅ Successfully processed: {successful_files}/{len(md_files)} files")
    print(f"📦 Total chunks embedded: {total_chunks}")
    print(f"💾 Collection: {COLLECTION_NAME}")
    
    if failed_files:
        print(f"\n❌ Failed files ({len(failed_files)}):")
        for filename, error in failed_files:
            print(f"   - {filename}: {error}")
    
    print("\n✅ Done! The documentation is now queryable via the MCP server.")
    print(f"\n💡 Query using:")
    print(f'   collection_name="{COLLECTION_NAME}"')


if __name__ == "__main__":
    process_markdown_folder()

