import os
import os
import pdfplumber
import json
from pathlib import Path
from .chunk import chunk_text
from .models import Chunk

# Resolve path to project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # backend/
ROOT_DIR = BASE_DIR.parent                                # ohrs-assistant/
CORPUS_DIR = ROOT_DIR / "corpus" / "ohrs_v12"

OUTPUT_FILE = BASE_DIR / "app" / "rag" / "output" / "ohrs_v12_chunks.json"


def load_pdfs():
    pdf_files = [
        f for f in CORPUS_DIR.iterdir()
        if f.suffix.lower() == ".pdf"
    ]
    return sorted(pdf_files)


def appendix_from_filename(filename: str) -> str:
    # Extract A/B/C/D from "Appendix_A_v12.pdf"
    if "Appendix_A" in filename:
        return "A"
    if "Appendix_B" in filename:
        return "B"
    if "Appendix_C" in filename:
        return "C"
    if "Appendix_D" in filename:
        return "D"
    return "?"


def ingest():
    all_chunks = []

    pdf_files = load_pdfs()
    print(f"[INGEST] Found {len(pdf_files)} PDFs")

    for pdf_path in pdf_files:
        appendix = appendix_from_filename(pdf_path.name)
        print(f"[INGEST] Processing Appendix {appendix}: {pdf_path.name}")

        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text() or ""

                if not text.strip():
                    continue

                chunks = chunk_text(text)

                for i, chunk in enumerate(chunks):
                    chunk_id = f"{appendix}_{page_num}_{i}"

                    all_chunks.append(
                        Chunk(
                            id=chunk_id,
                            appendix=appendix,
                            page_start=page_num,
                            page_end=page_num,
                            text=chunk
                        ).dict()
                    )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2)

    print(f"[INGEST] Completed. {len(all_chunks)} chunks saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    ingest()
