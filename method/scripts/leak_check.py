# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check that files meant for a clean-room agent name no source and no technology.

Run it on every file a clean-room context will read (abstracted-full.md,
for-the-writer.md, kept.md) and on the finished skill. Matches whole words only,
so "trust" doesn't match "rust" and "member" doesn't match "ember".

Exit codes:
  0  no names found
  1  names found (listed on stdout as file:line: word)
  2  bad arguments
"""

import argparse
import re
import sys
from pathlib import Path

DEFAULT_NAMES = [
    "react", "jsx", "ember", "glimmer", "django", "python", "sphinx", "rails",
    "ruby", "rdoc", "rust", "cargo", "rustc", "mdn", "javascript", "ecmascript",
    "postgres", "postgresql", "psql", "sql", "diátaxis", "diataxis",
]


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="uv run method/scripts/leak_check.py",
        description="Find source or technology names in clean-room files.",
        epilog=(
            "exit codes: 0 clean, 1 names found, 2 bad arguments\n\n"
            "examples:\n"
            "  uv run method/scripts/leak_check.py runs/claude-opus-5.5-medium/pipeline/kept.md\n"
            "  uv run method/scripts/leak_check.py --names vue,nuxt pipeline/abstracted-full.md"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--names", help="comma-separated names to add to the default list")
    args = parser.parse_args()

    names = DEFAULT_NAMES + [n.strip().lower() for n in (args.names or "").split(",") if n.strip()]
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, names)) + r")\b", re.IGNORECASE)

    found = 0
    for path in args.files:
        for number, line in enumerate(path.read_text().splitlines(), 1):
            for match in pattern.finditer(line):
                print(f"{path}:{number}: {match.group()}")
                found += 1
    if found:
        print(f"{found} name(s) found", file=sys.stderr)
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
