from pathlib import Path

from study_assistant.loader import chunk_text, load_text_files
from study_assistant.search import keyword_search

files = load_text_files(Path("notes"))
all_chunks = [c for name, text in files.items() for c in chunk_text(text, name)]
for chunk in keyword_search("machine learning", all_chunks):
    print(f"Source: {chunk.source_file}, Position: {chunk.position}, Text: {chunk.text[:100]}...")
