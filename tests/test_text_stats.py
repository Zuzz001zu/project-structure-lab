import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from text_stats import count_chars, count_lines, count_words, top_words  # noqa: E402

SAMPLE = "Привет мир\nпривет Git"


def test_count_lines():
    assert count_lines(SAMPLE) == 2


def test_count_words():
    assert count_words(SAMPLE) == 4


def test_count_chars():
    assert count_chars(SAMPLE) == 20


def test_top_words():
    assert top_words(SAMPLE, 1) == [("привет", 2)]


def test_empty_text():
    assert count_words("") == 0
    assert top_words("") == []
