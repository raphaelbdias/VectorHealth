# backend/app/rag/ingest_ontario_health.py

import json
import re
from pathlib import Path
from typing import Dict, List

# Optional deps – install as you go:
# pip install pypdf python-docx pandas openpyxl
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

try:
    import docx  # python-docx
except ImportError:
    docx = None

try:
    import pandas as pd
except ImportError:
    pd = None


# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------

HERE = Path(__file__).resolve()
PROJECT_ROOT = HERE.parents[3]          # .../ohrs-assistant
CORPUS_DIR = PROJECT_ROOT / "corpus"    # all your folders
OUTPUT_DIR = HERE.parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
OUT_JSON = OUTPUT_DIR / "ontario_health_chunks.json"


# -------------------------------------------------------------------
# Basic chunking utility (simple and safe)
# -------------------------------------------------------------------

def simple_chunks(text: str, max_chars: int = 1600, overlap: int = 200) -> List[str]:
    """
    Very simple character-based chunking with overlap.
    Enough for RAG; you can swap this for your existing chunker if you like.
    """
    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0
    n = len(text)

    while start < n:
        end = min(start + max_chars, n)
        # try to break on a newline or period
        chunk = text[start:end]
        last_break = max(chunk.rfind("\n"), chunk.rfind("."))
        if last_break > 200:
            end = start + last_break + 1
            chunk = text[start:end]

        chunks.append(chunk.strip())
        start = max(end - overlap, end)

    return chunks


# -------------------------------------------------------------------
# File-type specific text loaders
# -------------------------------------------------------------------

def load_pdf(path: Path) -> str:
    if PdfReader is None:
        print(f"[WARN] pypdf not installed; skipping PDF: {path}")
        return ""
    try:
        reader = PdfReader(str(path))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n\n".join(pages)
    except Exception as e:
        print(f"[ERROR] Failed to read PDF {path}: {e}")
        return ""


def load_docx(path: Path) -> str:
    if docx is None:
        print(f"[WARN] python-docx not installed; skipping DOCX: {path}")
        return ""
    try:
        d = docx.Document(str(path))
        paras = [p.text for p in d.paragraphs]
        return "\n".join(paras)
    except Exception as e:
        print(f"[ERROR] Failed to read DOCX {path}: {e}")
        return ""


def load_excel(path: Path) -> str:
    if pd is None:
        print(f"[WARN] pandas/openpyxl not installed; skipping Excel: {path}")
        return ""
    try:
        # read all sheets and flatten into text
        xls = pd.read_excel(path, sheet_name=None, dtype=str)
        parts = []
        for sheet_name, df in xls.items():
            parts.append(f"### Sheet: {sheet_name}")
            # turn each row into a ' | ' separated line
            for _, row in df.iterrows():
                row_vals = [str(v) for v in row.tolist() if pd.notna(v)]
                if row_vals:
                    parts.append(" | ".join(row_vals))
        return "\n".join(parts)
    except Exception as e:
        print(f"[ERROR] Failed to read Excel {path}: {e}")
        return ""


def load_plain_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        print(f"[ERROR] Failed to read text {path}: {e}")
        return ""


def load_file_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return load_pdf(path)
    elif suffix == ".docx":
        return load_docx(path)
    elif suffix in (".xls", ".xlsx"):
        return load_excel(path)
    elif suffix in (".txt",):
        return load_plain_text(path)
    else:
        # Older .doc files – you may want to convert them manually to PDF/DOCX.
        print(f"[WARN] Unsupported extension {suffix} – {path.name} (convert manually)")
        return ""


# -------------------------------------------------------------------
# Metadata helpers
# -------------------------------------------------------------------

SOURCE_FAMILIES = {
    "ohrs": "ohrs",
    "admin": "admin",
    "mis": "mis",
    "icd": "icd",
    "ajcc": "ajcc",
    "cco": "cco",
    "waittimes": "waittimes",
    "pathology": "pathology",
    "pet": "pet",
    "sso": "sso",
    "ndfp": "ndfp",
    "orrs": "orrs",
}

CHAPTER_HINTS = {
    "ohrs": "ALR / OHRS",
    "admin": "ALR Admin",
    "mis": "ALR Meta",
    "icd": "Coding / ICD",
    "ajcc": "AJCC Staging",
    "cco": "CCO Systemic / Guidelines",
    "waittimes": "WTIS / Wait Times",
    "pathology": "ePath",
    "pet": "PET",
    "sso": "SSOIS",
    "ndfp": "NDFP",
    "orrs": "ORRS",
}


def parse_appendix_code(filename: str) -> str | None:
    """
    Try to extract an appendix identifier from the filename.
    Works on patterns like:
      - Appendix_A_v12.docx
      - CCO_DBK_Appendix_1-18_MAY_22.xlsx
      - Appendix_13.11_20240718.xlsx
    """
    # normalize spaces/underscores
    name = filename.replace(" ", "_")
    m = re.search(r"Appendix[_A-Za-z]*_([0-9A-Za-z.\-]+)", name)
    if m:
        return m.group(1)

    # simple OHRS A/B/C/D
    m2 = re.search(r"Appendix_([A-D])[_\.]", name)
    if m2:
        return m2.group(1)

    return None


def parse_year_hint(filename: str) -> str | None:
    # Examples: _APR_21, _MAY_22, _20250718, etc.
    # We'll just grab a trailing 4-digit year if present.
    m = re.search(r"(20[0-9]{2})", filename)
    if m:
        return m.group(1)
    return None


# -------------------------------------------------------------------
# Main ingestion
# -------------------------------------------------------------------

def build_chunks() -> List[Dict]:
    all_chunks: List[Dict] = []
    chunk_counter = 0

    for subdir_name in sorted(SOURCE_FAMILIES.keys()):
        dir_path = CORPUS_DIR / subdir_name
        if not dir_path.exists():
            print(f"[WARN] Missing directory: {dir_path}")
            continue

        source_family = SOURCE_FAMILIES[subdir_name]
        chapter_hint = CHAPTER_HINTS.get(subdir_name)

        print(f"\n=== Ingesting {subdir_name} ({dir_path}) ===")

        for path in sorted(dir_path.glob("*")):
            if not path.is_file():
                continue

            text = load_file_text(path)
            if not text.strip():
                continue

            appendix_code = parse_appendix_code(path.name)
            year_hint = parse_year_hint(path.name)

            chunks = simple_chunks(text)
            print(f"  - {path.name} → {len(chunks)} chunks")

            for i, ch in enumerate(chunks):
                chunk_id = f"{source_family}:{path.stem}:{i}"

                meta = {
                    "source_family": source_family,
                    "file_name": path.name,
                    "path": str(path),
                    "appendix_code": appendix_code,
                    "chapter": chapter_hint,
                    "year_hint": year_hint,
                }

                all_chunks.append(
                    {
                        "id": chunk_id,
                        "document": ch,
                        "metadata": meta,
                    }
                )
                chunk_counter += 1

    print(f"\nTotal chunks: {chunk_counter}")
    return all_chunks


def main():
    chunks = build_chunks()
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Wrote {len(chunks)} chunks to {OUT_JSON}")


if __name__ == "__main__":
    main()
