"""
Documentation Search Interface
Query the vector database to find relevant documentation.
"""

import sys
from vector_db import ChromaVectorDB
from typing import Optional


def search_documentation(query: str, collection_name: str = "documentation", n_results: int = 5):
    """
    Search the documentation vector database.
    
    Args:
        query: Search query
        collection_name: Name of the ChromaDB collection
        n_results: Number of results to return
    """
    print(f"🔍 Searching for: '{query}'")
    print(f"📚 Collection: {collection_name}")
    print("=" * 60)
    
    try:
        # Initialize vector DB
        db = ChromaVectorDB(
            path="./chroma_db",
            collection_name=collection_name,
            chunk_size=500,
            chunk_overlap=50
        )
        
        # Get database stats
        count = db.collection.count()
        print(f"\n📊 Database contains {count} chunks")
        print(f"   Embedding model: Qwen/Qwen3-Embedding-0.6B")
        
        # Perform search
        results = db.query(query, n_results=n_results)
        
        if not results['documents'] or not results['documents'][0]:
            print(f"\n❌ No results found for '{query}'")
            return
        
        documents = results['documents'][0]
        ids = results['ids'][0] if 'ids' in results else []
        distances = results['distances'][0] if 'distances' in results else [0] * len(documents)
        
        print(f"\n✅ Found {len(documents)} results:\n")
        
        # Display results
        for i, (doc, doc_id, distance) in enumerate(zip(documents, ids, distances), 1):
            print(f"{'=' * 60}")
            print(f"Result {i} (Distance: {distance:.4f})")
            print(f"{'=' * 60}")
            print(f"📄 Document ID: {doc_id}")
            
            print(f"\n📝 Content:")
            print("-" * 60)
            # Show first 500 characters
            content_preview = doc[:500]
            if len(doc) > 500:
                content_preview += "..."
            print(content_preview)
            print()
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


def list_collections():
    """List all available collections in the vector database."""
    print("📚 Available Collections")
    print("=" * 60)
    
    try:
        import chromadb
        from chromadb.config import Settings
        
        client = chromadb.PersistentClient(
            path="./chroma_db",
            settings=Settings(anonymized_telemetry=False)
        )
        
        collections = client.list_collections()
        
        if not collections:
            print("❌ No collections found")
            return
        
        print(f"\nFound {len(collections)} collection(s):\n")
        
        for collection in collections:
            print(f"  📚 {collection.name}")
            print(f"     Documents: {collection.count()}")
            print()
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")


def interactive_search(collection_name: str = "documentation"):
    """Interactive search mode."""
    print("🔍 Interactive Documentation Search")
    print("=" * 60)
    print(f"Collection: {collection_name}")
    print("Type 'quit' or 'exit' to stop")
    print("Type 'stats' to see database statistics")
    print("Type 'collections' to list all collections")
    print("=" * 60)
    print()
    
    db = None
    
    try:
        db = ChromaVectorDB(
            path="./chroma_db",
            collection_name=collection_name,
            chunk_size=500,
            chunk_overlap=50
        )
    except Exception as e:
        print(f"❌ Could not load collection '{collection_name}': {str(e)}")
        return
    
    while True:
        try:
            query = input("\n🔍 Enter search query: ").strip()
            
            if not query:
                continue
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if query.lower() == 'stats':
                count = db.collection.count()
                print(f"\n📊 Database Statistics:")
                print(f"  - Total chunks: {count}")
                print(f"  - Collection: {db.collection.name}")
                print(f"  - Embedding model: Qwen/Qwen3-Embedding-0.6B")
                print(f"  - Chunk size: {db.chunk_size} words")
                print(f"  - Chunk overlap: {db.chunk_overlap} words")
                continue
            
            if query.lower() == 'collections':
                list_collections()
                continue
            
            # Perform search
            results = db.query(query, n_results=3)
            
            if not results['documents'] or not results['documents'][0]:
                print(f"❌ No results found")
                continue
            
            documents = results['documents'][0]
            ids = results['ids'][0] if 'ids' in results else []
            distances = results['distances'][0] if 'distances' in results else [0] * len(documents)
            
            print(f"\n✅ Top {len(documents)} results:\n")
            
            for i, (doc, doc_id, distance) in enumerate(zip(documents, ids, distances), 1):
                print(f"{'-' * 60}")
                print(f"{i}. {doc_id} (Distance: {distance:.4f})")
                print(f"\n   {doc[:200]}...")
                print()
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python search_docs.py <query> [collection_name] [n_results]")
        print("  python search_docs.py --interactive [collection_name]")
        print("  python search_docs.py --list-collections")
        print()
        print("Examples:")
        print("  python search_docs.py 'how to use agents'")
        print("  python search_docs.py 'authentication' docs_openai 10")
        print("  python search_docs.py --interactive")
        print("  python search_docs.py --interactive docs_openai")
        return
    
    if sys.argv[1] == '--list-collections':
        list_collections()
        return
    
    if sys.argv[1] == '--interactive':
        collection_name = sys.argv[2] if len(sys.argv) > 2 else "documentation"
        interactive_search(collection_name)
        return
    
    # Regular search
    query = sys.argv[1]
    collection_name = sys.argv[2] if len(sys.argv) > 2 else "documentation"
    n_results = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    
    search_documentation(query, collection_name, n_results)


if __name__ == "__main__":
    main()

