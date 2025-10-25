from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import torch
import re

def get_markdown_embedding(markdown_text: str, model_name: str = "Qwen/Qwen3-Embedding-0.6B"):
    """
    Given a markdown document, returns a vector embedding using a Qwen model.
    """
    model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
    return model.encode(markdown_text)
