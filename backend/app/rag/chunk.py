def chunk_text(text: str, max_tokens: int = 600, overlap: int = 100):
    """
    Very basic character-based chunker (tokenizer-free for now)
    """
    words = text.split()
    chunks = []
    
    start = 0
    end = max_tokens

    while start < len(words):
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        start = end - overlap
        end = start + max_tokens

    return chunks
