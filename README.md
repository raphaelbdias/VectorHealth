# VectorHealth - OHRS Assistant

Local Retrieval-Augmented Generation (RAG) assistant for Ontario Healthcare Reporting Standards (OHRS).

Quick links
- Backend entry: [`app.main.ChatRequest`](backend/app/main.py) / [`app.main.chat_json`](backend/app/main.py) / [`app.main.chat_stream`](backend/app/main.py) — [backend/app/main.py](backend/app/main.py)
- Ingest scripts: [backend/app/rag/ingest.py](backend/app/rag/ingest.py), [backend/app/rag/ingest_ontario_health.py](backend/app/rag/ingest_ontario_health.py)
- Frontend: [frontend/package.json](frontend/package.json) and docs [frontend/README.md](frontend/README.md)
- Corpus folder: /corpus
- Vector DB: /backend/db/vector

Repository setup
- Create a new repository on GitHub (e.g., https://github.com/<your-org>/<repo-name>).
- From the project root, push the current code to the new repo:
  - git init
  - git add .
  - git commit -m "Initial commit"
  - git branch -M main
  - git remote add origin https://github.com/<your-org>/<repo-name>.git
  - git push -u origin main

Prerequisites
- Python 3.10+ (for backend)
- Node 18+ / npm (for frontend)

Backend — run locally
1. From repo root:
   - cd backend
   - python -m venv .venv
   - .venv\Scripts\activate (Windows) or source .venv/bin/activate (Linux/macOS)
   - pip install -r [backend/requirements.txt](backend/requirements.txt)
2. Start server:
   - uvicorn app.main:app --reload
3. Useful endpoints:
   - GET /health (health check) — implemented in [backend/app/main.py](backend/app/main.py)
   - POST /chat — JSON chat (see [`app.main.chat_json`](backend/app/main.py))
   - POST /chat_stream — streaming SSE endpoint (see [`app.main.chat_stream`](backend/app/main.py))

Frontend — run locally
1. cd frontend
2. Install deps:
   - npm install
3. Start dev server:
   - npm run dev
4. Default: http://localhost:3000 (Next will pick another port if 3000 is busy). See [frontend/package.json](frontend/package.json) and [frontend/README.md](frontend/README.md).

Corpus & ingestion
- Source PDFs and files live in /corpus (see [backend/app/rag/ingest.py](backend/app/rag/ingest.py) and [backend/app/rag/ingest_ontario_health.py](backend/app/rag/ingest_ontario_health.py)).
- Run the ingest scripts to generate JSON chunks used to build the vector store.

Troubleshooting
- If Next warns about lockfiles/root directory, see [frontend/next.config.js](frontend/next.config.js) for turbopack settings.
- If the frontend or backend needs additional optional Python packages, check the top of [backend/app/rag/ingest_ontario_health.py](backend/app/rag/ingest_ontario_health.py) (imports are guarded with try/except).

License / notes
- This README is a minimal local-dev guide. See individual module files for implementation details.
