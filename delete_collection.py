"""
Script to delete a collection from ChromaDB
Use this to remove old or unwanted documentation collections
"""

import sys
import chromadb
from chromadb.config import Settings
import argparse

# Configuration
DB_PATH = "./chroma_db"


def list_collections():
    """List all collections in the database"""
    try:
        client = chromadb.PersistentClient(
            path=DB_PATH,
            settings=Settings(anonymized_telemetry=False)
        )
        
        collections = client.list_collections()
        
        if not collections:
            print("📭 No collections found in the database")
            return []
        
        print("📚 Available Collections:")
        print("=" * 60)
        for i, collection in enumerate(collections, 1):
            try:
                count = collection.count()
                print(f"{i}. {collection.name} ({count} chunks)")
            except Exception as e:
                print(f"{i}. {collection.name} (error getting count: {e})")
        
        print("=" * 60)
        return [c.name for c in collections]
        
    except Exception as e:
        print(f"❌ Error accessing database: {e}")
        return []


def delete_collection(collection_name: str, confirm: bool = False):
    """Delete a collection from the database"""
    
    print(f"\n🗑️  Deleting Collection: {collection_name}")
    print("=" * 60)
    
    if not confirm:
        print("⚠️  WARNING: This will permanently delete the collection!")
        print(f"Collection: {collection_name}")
        response = input("\nAre you sure you want to delete? (yes/no): ")
        if response.lower() not in ['yes', 'y']:
            print("❌ Deletion cancelled")
            return
    
    try:
        client = chromadb.PersistentClient(
            path=DB_PATH,
            settings=Settings(anonymized_telemetry=False)
        )
        
        # Get collection info before deletion
        try:
            collection = client.get_collection(collection_name)
            count = collection.count()
            print(f"📊 Found {count} chunks in collection")
        except Exception:
            print(f"⚠️  Collection '{collection_name}' not found")
            return
        
        # Delete the collection
        client.delete_collection(collection_name)
        print(f"✅ Collection '{collection_name}' deleted successfully!")
        
    except Exception as e:
        print(f"❌ Error deleting collection: {e}")


def main():
    """Main function with CLI"""
    parser = argparse.ArgumentParser(
        description="Delete a collection from ChromaDB"
    )
    parser.add_argument(
        'collection_name',
        nargs='?',
        help='Name of the collection to delete'
    )
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help='List all available collections'
    )
    parser.add_argument(
        '-y', '--yes',
        action='store_true',
        help='Skip confirmation prompt'
    )
    
    args = parser.parse_args()
    
    # HARD CODED: Delete these collections
    TARGET_COLLECTIONS = [
        "streamlit_api",      # 24 chunks - old/empty
        "markdown_docs",      # 9 chunks - old
        "documentation",      # 0 chunks - empty
        "streamlit_docs",     # 0 chunks - empty
        "docs_streamlit_io",  # 0 chunks - empty
        "docs_docs_streamlit_io"  # 5 chunks - empty
    ]
    
    if args.list:
        list_collections()
    elif args.collection_name:
        delete_collection(args.collection_name, confirm=args.yes)
    else:
        # Delete all hard-coded collections
        print("🗑️  ChromaDB Collection Deletion Tool")
        print("=" * 60)
        print(f"Will delete {len(TARGET_COLLECTIONS)} collections:")
        for coll in TARGET_COLLECTIONS:
            print(f"  - {coll}")
        print()
        
        # Confirm
        response = input(f"Are you sure you want to delete {len(TARGET_COLLECTIONS)} collections? (yes/no): ")
        if response.lower() not in ['yes', 'y']:
            print("❌ Deletion cancelled")
            return
        
        # Delete each collection
        for collection in TARGET_COLLECTIONS:
            print()
            delete_collection(collection, confirm=True)
        
        print("\n✅ All collections deleted!")


if __name__ == "__main__":
    main()

