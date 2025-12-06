import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

from app.rag.retrieval import retrieve_topk
from app.rag.prompt_builder import build_prompt
from app.llm.ollama_client import stream_llama, generate_full


app = FastAPI(title="Ontario Health RAG Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# MODELS
# -------------------------
class ChatRequest(BaseModel):
    query: str
    k: int | None = 5


# -------------------------
# HEALTH CHECK
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------
# NORMAL JSON CHAT (good for debugging)
# -------------------------
@app.post("/chat")
def chat_json(req: ChatRequest):
    retrieved = retrieve_topk(req.query, top_k=req.k or 5)
    prompt = build_prompt(req.query, retrieved)
    answer = generate_full(prompt)

    return {
        "answer": answer,
        "retrieved": retrieved,       # Frontend can show citation preview
        "prompt_used": prompt         # For debugging / transparency
    }


# -------------------------
# STREAMING CHAT (SSE)
# -------------------------
@app.post("/chat_stream")
def chat_stream(req: ChatRequest):

    # STEP 1 — Retrieve chunks from vector DB
    retrieved = retrieve_topk(req.query, top_k=req.k or 5)

    # STEP 2 — Build final prompt with RAG context
    prompt = build_prompt(req.query, retrieved)

    # STEP 3 — Stream generator: send retrieved context FIRST
    def event_gen():

        # This enables the frontend to populate citation drawer
        yield {
            "event": "retrieved",
            "data": json.dumps(retrieved)
        }

        # Stream model tokens
        for token in stream_llama(prompt):
            yield {"event": "token", "data": token}

        yield {"event": "done", "data": ""}

    return EventSourceResponse(event_gen())
