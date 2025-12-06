# backend/app/rag/embeddings.py

from functools import lru_cache
from sentence_transformers import SentenceTransformer
from typing import List

MODEL_NAME = "all-MiniLM-L6-v2"

@lru_cache(maxsize=1)
def _get_model() -> SentenceTransformer:
    return SentenceTransformer(MODEL_NAME)

def embed(texts: List[str]) -> List[List[float]]:
    """
    Embed a list of texts. Returns list of lists of floats.
    """
    model = _get_model()
    return model.encode(texts, normalize_embeddings=True).tolist()

def embed_one(text: str) -> List[float]:
    """
    Convenience wrapper for single-text embedding.
    """
    return embed([text])[0]
