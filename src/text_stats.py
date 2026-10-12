"""Функции подсчёта статистики текста."""
import re
from collections import Counter

WORD_RE = re.compile(r"[a-zA-Zа-яА-ЯёЁ0-9]+")


def count_lines(text: str) -> int:
    """Количество строк в тексте."""
    return len(text.splitlines())


def get_words(text: str) -> list:
    """Список слов в нижнем регистре."""
    return [w.lower() for w in WORD_RE.findall(text)]


def count_words(text: str) -> int:
    """Количество слов в тексте."""
    return len(get_words(text))


def count_chars(text: str) -> int:
    """Количество символов без учёта переводов строк."""
    return len(text.replace("\n", ""))


def top_words(text: str, n: int = 5) -> list:
    """N самых частых слов в виде списка пар (слово, количество)."""
    return Counter(get_words(text)).most_common(n)
