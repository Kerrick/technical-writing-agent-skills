# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check PLACEMENT.md against kept.md and the skill.

Every rule in kept.md must have exactly one row, and every file:line a row
cites must exist and not be blank. Read a few cited lines yourself as well:
this checks that the line exists, not that it states the rule.

Exit codes:
  0  every rule placed, every citation valid
  1  missing rules or bad citations (listed on stdout)
  2  bad arguments
"""

import argparse
import re
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="uv run method/scripts/check_placement.py",
        description="Check that every kept rule is placed in the skill.",
        epilog=(
            "exit codes: 0 all placed, 1 problems found, 2 bad arguments\n\n"
            "example:\n"
            "  uv run method/scripts/check_placement.py runs/claude-opus-5.5-medium/PLACEMENT.md \\\n"
            "    runs/claude-opus-5.5-medium/pipeline/kept.md skills"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("placement", type=Path)
    parser.add_argument("kept", type=Path)
    parser.add_argument("root", type=Path, help="the directory cited paths are relative to")
    args = parser.parse_args()

    expected = {int(n) for n in re.findall(r"^### (\d+)\.", args.kept.read_text(), re.M)}
    rows = [l for l in args.placement.read_text().splitlines() if re.match(r"\|\s*\d+\s*\|", l)]
    problems = []
    seen = []
    for row in rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        number = int(cells[0])
        seen.append(number)
        cites = re.findall(r"([\w./-]+\.md):(\d+)", cells[-1])
        if not cites:
            problems.append(f"rule {number}: no file:line citation")
        for path, line in cites:
            target = args.root / path
            if not target.exists():
                problems.append(f"rule {number}: {path} doesn't exist")
                continue
            lines = target.read_text().splitlines()
            if int(line) > len(lines) or not lines[int(line) - 1].strip():
                problems.append(f"rule {number}: {path}:{line} is missing or blank")

    for number in sorted(expected - set(seen)):
        problems.append(f"rule {number}: no row")
    for number in sorted({n for n in seen if seen.count(n) > 1}):
        problems.append(f"rule {number}: more than one row")

    for problem in problems:
        print(problem)
    if not problems:
        print(f"All {len(expected)} rules placed; every citation exists.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
