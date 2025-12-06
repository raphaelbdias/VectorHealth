def build_prompt(query: str, retrieved: list[dict]):
    """
    Build a strict RAG prompt that forces the model to use ONLY retrieved chunks.
    """

    context_blocks = []

    for item in retrieved:
        meta = item.get("metadata", {})
        appendix = meta.get("appendix_code") or "Unknown Appendix"
        chapter = meta.get("chapter") or "General"
        source = meta.get("file_name") or ""
        page = (
            meta.get("page_start")
            or meta.get("page")
            or meta.get("page_end")
            or "?"
        )
        chunk_id = item.get("id") or "chunk"

        block = (
            f"### Source: {source}\n"
            f"Citation: [{chunk_id} | Appendix {appendix}, Page {page}]\n"
            f"Chapter: {chapter}\n"
            f"{item['document']}"
        )
        context_blocks.append(block)

    context_text = "\n\n".join(context_blocks)

    return f"""
You are the **Ontario Health Reporting Assistant**.

You answer using ONLY the retrieved documents below.
You must NOT hallucinate or invent any rules.
If information is not found in the retrieved context, say:
"I cannot find this rule in the ingested Ontario Health appendices."

Format your answer in clear Markdown with:
- Short intro line
- Headings for sections
- Bulleted lists for codes/rules
- Bold for key terms
- Preserve spacing needed for Markdown
Always include citations and copy the exact citation labels provided in the context,
using the format:
[<chunk_id> | Appendix <appendix_code>, Page <page_number>]

---

### Retrieved Context
{context_text}

---

### User Question
{query}

### Final Answer (well formatted, with citations):
"""
