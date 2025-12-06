import json
from pathlib import Path
import chromadb
from .embeddings import embed

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHUNKS_FILE = BASE_DIR / "app" / "rag" / "output" / "ontario_health_chunks.json"
VECTOR_DB_DIR = BASE_DIR / "db" / "vector"

def sanitize_metadata(md: dict):
    clean = {}
    for k, v in md.items():
        clean[k] = "unknown" if v is None else v
    return clean

def build_vectorstore():
    print("[VECTOR] Initializing Chroma at:", VECTOR_DB_DIR)

    client = chromadb.PersistentClient(path=str(VECTOR_DB_DIR))

    collection = client.get_or_create_collection(
        name="ontario_health",
        metadata={"hnsw:space": "cosine"}
    )

    print("[VECTOR] Loading:", CHUNKS_FILE.name)
    raw = CHUNKS_FILE.read_text(encoding="utf-8", errors="replace")
    chunks = json.loads(raw)
    print(f"[VECTOR] Total chunks: {len(chunks)}")

    ids, embeddings, documents, metadatas = [], [], [], []

    print("[VECTOR] Embedding chunks...")

    for i, chunk in enumerate(chunks):
        if i % 200 == 0:
            print(f"  → {i}/{len(chunks)}")

        text = chunk.get("document") or chunk.get("text")
        if not text:
            continue  # skip malformed entries

        ids.append(chunk["id"])
        documents.append(text)
        md = sanitize_metadata(chunk["metadata"])
        metadatas.append(md)

        emb = embed(text)
        embeddings.append(emb)

    print("[VECTOR] Adding to Chroma in batches...")

    batch_size = 500
    n = len(ids)

    for start in range(0, n, batch_size):
        end = start + batch_size
        print(f"  \u2192 Adding batch {start}/{n}")

        collection.add(
            ids=ids[start:end],
            documents=documents[start:end],
            embeddings=embeddings[start:end],
            metadatas=metadatas[start:end],
        )

    print("[VECTOR] DONE — all batches added!")

    print("✅ Vector DB saved:", VECTOR_DB_DIR)


if __name__ == "__main__":
    build_vectorstore()
