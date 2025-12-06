from app.rag.retrieval import retrieve_topk

q = "What is the AJCC staging rule for C02 malignant neoplasm of tongue?"
results = retrieve_topk(q, top_k=3)

for r in results:
    print("\n---")
    print("ID:", r["id"])
    print("distance:", r["distance"])
    print("metadata:", r["metadata"])
    print(r["document"][:400])
