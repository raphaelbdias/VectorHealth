import chromadb
from app.rag.embeddings import embed_one
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
VECTOR_DB_DIR = BASE_DIR / "db" / "vector"

# load vector DB
client = chromadb.PersistentClient(path=str(VECTOR_DB_DIR))

# FIXED: use correct new collection name
collection = client.get_or_create_collection(
    name="ontario_health",
    metadata={"hnsw:space": "cosine"}
)

def retrieve_topk(query: str, top_k: int = 5):
    """
    Returns the top-k most relevant chunks using the Ontario Health vectorstore.
    """

    q_emb = embed_one(query)

    results = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k
    )

    docs = []
    for i in range(len(results["documents"][0])):
        docs.append({
            "id": results["ids"][0][i],
            "document": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return docs
