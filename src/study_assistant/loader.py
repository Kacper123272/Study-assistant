from dataclasses import dataclass
from pathlib import Path


@dataclass
class Chunk:
    text: str
    source_file: str
    position: int


def load_text_files(folder: Path) -> dict[str, str]:
    """Return {filename: file contents} for each text file in the folder."""
    return {path.name: path.read_text(encoding="utf-8") for path in folder.glob("*.txt")}


def chunk_text(text: str, source_file: str, chunk_size: int = 200) -> list[Chunk]:
    """Split text into chunks of a given size."""
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        piece = " ".join(words[i : i + chunk_size])
        chunks.append(Chunk(text=piece, source_file=source_file, position=i // chunk_size))
    return chunks
