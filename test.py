#!/usr/bin/env python3
"""
Load markdown files from groq_documentation_markdown/ into ChromaDB (persistent),
then run a test query and print the top matches.

Requires:
  pip install chromadb sentence-transformers
  (and the Qwen model available for sentence-transformers; may require extra setup)
"""

import os
import glob
import json
from typing import List
import chromadb
from sentence_transformers import SentenceTransformer
import numpy as np
from vector_db import ChromaVectorDB

# ---------- Configuration ----------
DOCS_DIR = "groq_documentation_markdown"
CHROMA_DB_PATH = "./chroma_db"
COLLECTION_NAME = "markdown_docs"

CHUNK_SIZE = 200
CHUNK_OVERLAP = 50

def load_markdown_files(folder: str) -> List[dict]:
    """Load all .md files from folder and return list of dicts {id, text, filename}"""
    md_files = sorted(glob.glob(os.path.join(folder, "*.md")))
    docs = []
    for path in md_files:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        basename = os.path.basename(path)
        doc_id = os.path.splitext(basename)[0]
        docs.append({"id": doc_id, "text": text, "filename": path})
    return docs

def main():
    if not os.path.isdir(DOCS_DIR):
        print(f"Docs directory not found: {DOCS_DIR}")
        return

    docs = load_markdown_files(DOCS_DIR)
    if not docs:
        print(f"No markdown files found in {DOCS_DIR}.")
        return

    # Initialize DB (this will load the embedding model)
    db = ChromaVectorDB(path=CHROMA_DB_PATH, collection_name=COLLECTION_NAME, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

    # Prepare document texts and ids for insertion
    documents = [d["text"] for d in docs]
    ids = [d["id"] for d in docs]

    # Insert into Chroma
    db.insert(documents=documents, ids=ids)

    # Test query - change this query to something relevant to your docs
    test_query = "How do I use the Groq docs to convert HTML to markdown?"
    print("\nRunning test query:", test_query)
    results = db.query(test_query, n_results=5)

    # results often shaped like dict with lists-of-lists (for multi-query input).
    # We'll handle typical chromadb return shapes.
    ids = results.get("ids", [])
    documents = results.get("documents", [])
    distances = results.get("distances", [])
    metadatas = results.get("metadatas", [])

    # If single query, chroma returns nested lists: take the first row
    if isinstance(ids, list) and len(ids) and isinstance(ids[0], list):
        ids = ids[0]
    if isinstance(documents, list) and len(documents) and isinstance(documents[0], list):
        documents = documents[0]
    if isinstance(distances, list) and len(distances) and isinstance(distances[0], list):
        distances = distances[0]
    if isinstance(metadatas, list) and len(metadatas) and isinstance(metadatas[0], list):
        metadatas = metadatas[0]

    print("\nTop results:")
    for idx, (doc_id, doc_text, dist, md) in enumerate(zip(ids, documents, distances, metadatas), start=1):
        snippet = (doc_text[:300] + "...") if doc_text and len(doc_text) > 300 else (doc_text or "<empty>")
        print(f"\n[{idx}] id: {doc_id}")
        print(f"    distance: {dist}")
        print(f"    metadata: {md}")
        print(f"    snippet:\n{snippet}")

if __name__ == "__main__":
    main()