from study_assistant.loader import Chunk, chunk_text
from study_assistant.search import keyword_search


def test_chunk_text_splits_by_word_count():
    chunks = chunk_text("one two three four five", "a.txt", chunk_size=2)
    assert [c.text for c in chunks] == ["one two", "three four", "five"]
    assert chunks[2].position == 2


def test_search_ranks_best_match_first():
    chunks = [
        Chunk("cats and dogs", "a.txt", 0),
        Chunk("binary tree binary search", "a.txt", 1),
    ]
    results = keyword_search("binary tree", chunks)
    assert results[0].position == 1


def test_search_is_case_insensitive():
    chunks = [Chunk("Binary TREE", "a.txt", 0)]
    assert len(keyword_search("binary tree", chunks)) == 1


def test_search_skips_chunks_with_no_matches():
    chunks = [Chunk("cats and dogs", "a.txt", 0)]
    assert keyword_search("binary tree", chunks) == []
