# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Find the banned patterns from references/style-rules.md in a README draft.

Prints one line per hit, as FILE:LINE: [rule] matched text. Code blocks and
inline code are skipped. A hit is a prompt to ask "who acts here?" and then fix
or defend the sentence, not proof of a mistake.

Exit codes:
  0  no hits
  1  hits found (listed on stdout)
  2  bad arguments or unreadable file
"""

import argparse
import json
import re
import sys
from pathlib import Path

RULES = {
    "filler own": r"\bown\b",
    "announced honesty": r"\b(honest(ly)?|frankly|to be clear|it'?s worth noting)\b",
    "the X part": r"\bthe \w+ (part|bit)\b",
    "em dash": r"—",
    "not X but Y": r"\bnot\b[^.]{1,60}\bbut\b|\bnot just\b",
    "non-agentic subject": r"\b(decides|asks|takes|wants|knows|lets|allows|handles)\b",
    "private shorthand": r"\b(deeper|forward|sideways|upstream)\b",
    "vague size or speed": r"\b(small|fast|lightweight|simple|tiny|quick)\b",
    "self-praise": r"\b(powerful|seamless(ly)?|robust|blazing|best-in-class)\b",
    "stock opener or closer": r"\b(in today's|whether you('| a)re|happy \w+ing)\b",
    "hedge stack": r"\b(might|may|could) (possibly|potentially|perhaps)\b|\bin some cases,? generally\b",
    "internal citation": r"\bADR[- ]?\d+|\bdecision \d+\b",
    "proof narration": r"\buntested\b|\bnot yet (been )?(tested|tried|proven)\b|\bno one has (tried|tested|submitted)\b|\bhas (been )?run on\b|\bon every (change|push|commit)\b|\bCI (runs|builds|tests|checks)\b|\b\d[\d,]* tests\b",
    "proof hedging": r"\b(tested|verified|confirmed) (with|on|only|against)\b|\bin (our|my) testing\b|\bas far as (we|I) know\b|\bshould (just )?work\b",
}
PATTERNS = {name: re.compile(rule, re.IGNORECASE) for name, rule in RULES.items()}


def prose_lines(text: str):
    """Yield (line number, line) for lines outside fenced code, with inline code removed."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"\s*(`{3,}|~{3,})", line)
        if marker:
            fence = None if fence and marker.group(1)[0] == fence else (fence or marker.group(1)[0])
            continue
        if not fence:
            yield number, re.sub(r"`[^`]*`", "", line)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="uv run scripts/hunt.py",
        description="Find banned README patterns. Run from the skill's directory.",
        epilog=(
            "exit codes: 0 no hits, 1 hits found, 2 bad arguments\n\n"
            "examples:\n"
            "  uv run scripts/hunt.py ~/code/myproject/README.md\n"
            "  uv run scripts/hunt.py --json README.md docs/index.md"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", help="print a JSON array of hits instead of lines")
    args = parser.parse_args()

    hits = []
    for path in args.files:
        try:
            text = path.read_text()
        except OSError as error:
            print(f"Error: can't read {path}: {error.strerror}", file=sys.stderr)
            return 2
        for number, line in prose_lines(text):
            for name, pattern in PATTERNS.items():
                for match in pattern.finditer(line):
                    hits.append({"file": str(path), "line": number, "rule": name, "match": match.group()})

    if args.json:
        print(json.dumps(hits, indent=2))
    else:
        for hit in hits:
            print(f"{hit['file']}:{hit['line']}: [{hit['rule']}] {hit['match']}")
        dashes = sum(1 for h in hits if h["rule"] == "em dash")
        if dashes >= 2:
            print(f"{dashes} em dashes: two or more per page is too many", file=sys.stderr)
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
