"""Точка входа: python src/main.py <файл> [--top N]"""
import argparse
import sys

from text_stats import count_chars, count_lines, count_words, top_words


def main() -> int:
    parser = argparse.ArgumentParser(description="Статистика по текстовому файлу")
    parser.add_argument("file", help="путь к текстовому файлу")
    parser.add_argument("--top", type=int, default=5, help="сколько частых слов показать")
    args = parser.parse_args()

    try:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Файл не найден: {args.file}", file=sys.stderr)
        return 1

    print(f"Строк:    {count_lines(text)}")
    print(f"Слов:     {count_words(text)}")
    print(f"Символов: {count_chars(text)}")
    print(f"Топ-{args.top} слов:")
    for word, cnt in top_words(text, args.top):
        print(f"  {word} — {cnt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
