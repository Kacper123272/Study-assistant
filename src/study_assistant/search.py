from study_assistant.loader import Chunk


def keyword_search(query: str, chunks: list[Chunk], top_k: int = 3) -> list[Chunk]:
    query_words = set(query.lower().split())
    scored = []
    for chunk in chunks:
        chunk_words = chunk.text.lower().split()
        score = sum(1 for word in chunk_words if word in query_words)
        if score > 0:
            scored.append((score, chunk))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [chunk for _, chunk in scored[:top_k]]
