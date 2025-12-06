# app/llm/ollama_client.py
import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3:latest"


def generate_full(prompt: str) -> str:
    """Non-streamed generation."""
    resp = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.0},
        },
        timeout=120,  # normal non-stream call can have a timeout
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("response", "")


def stream_llama(prompt: str):
    """Yield tokens from Ollama JSONL stream."""
    with requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": True,
            "options": {"temperature": 0.0},
        },
        stream=True,
        # ❌ timeout=0  (remove it)
        # ✅ either omit timeout or:
        # timeout=None,
    ) as r:
        r.raise_for_status()
        for line in r.iter_lines(decode_unicode=True):
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            token = obj.get("response")
            if token:
                yield token

            if obj.get("done"):
                break
