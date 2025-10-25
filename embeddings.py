from transformers import AutoTokenizer, AutoModel
import torch
import re

def get_markdown_embedding(markdown_text: str, model_name: str = "Qwen/Qwen3-Embedding-0.6B"):
    """
    Given a markdown document, returns a vector embedding using a Qwen model.
    """

    # Load tokenizer and model (cached after first load)
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_name, trust_remote_code=True)

    # Tokenize and embed
    inputs = tokenizer(markdown_text, return_tensors="pt", truncation=True, max_length=4096)
    with torch.no_grad():
        outputs = model(**inputs)
        # use the mean pooling of last hidden state
        embedding = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()

    return embedding