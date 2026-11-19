import argparse
import sys

from tallyho import count_words


def main() -> int:
    parser = argparse.ArgumentParser(prog="tallyho", description="Count the most common words in text files.")
    parser.add_argument("files", nargs="+", help="text files to read")
    parser.add_argument("--limit", type=int, default=10, help="how many words to show (default: 10)")
    args = parser.parse_args()
    text = "".join(open(path, encoding="utf-8").read() for path in args.files)
    for word, count in count_words(text, args.limit):
        print(f"{count:>6}  {word}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
