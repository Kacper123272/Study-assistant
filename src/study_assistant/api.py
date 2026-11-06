from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel

from study_assistant.loader import Chunk, chunk_text, load_text_files
from study_assistant.search import keyword_search

NOTES_DIR = Path("notes")


def load_all_chunks(folder: Path) -> list[Chunk]:
    files = load_text_files(folder)
    return [chunk for name, text in files.items() for chunk in chunk_text(text, name)]


app = FastAPI(title="Study Assistant")
chunks: list[Chunk] = load_all_chunks(NOTES_DIR)


class SearchResult(BaseModel):
    source_file: str
    position: int
    text: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/search")
def search(q: str, top_k: Annotated[int, Query(ge=1, le=20)] = 3) -> list[SearchResult]:
    results = keyword_search(q, chunks, top_k)
    return [
        SearchResult(source_file=c.source_file, position=c.position, text=c.text)
        for c in results
    ]