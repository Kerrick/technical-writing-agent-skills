"""Print one Markdown section's body: the lines after a heading, up to the next heading of the same or a higher level.

Used to pass clean-room agents only the parts of a file they may see, e.g. the
"## For the writer" section of often-broken-check.md.

Exit codes:
  0  section found and printed
  1  heading not found
  2  bad arguments
"""

import argparse
import re
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="python3 scripts/extract_section.py",
        description="Print the body of one Markdown section.",
        epilog=(
            "exit codes: 0 found, 1 heading not found, 2 bad arguments\n\n"
            "example:\n"
            '  python3 scripts/extract_section.py "## For the writer" often-broken-check.md > for-the-writer.md'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("heading", help='the exact heading line, e.g. "## Abstracted"')
    parser.add_argument("file", type=Path)
    args = parser.parse_args()

    level = len(re.match(r"#*", args.heading).group())
    if level == 0:
        parser.error('heading must start with "#", e.g. "## Abstracted"')

    lines = args.file.read_text().splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == args.heading.strip())
    except StopIteration:
        print(f"Error: heading {args.heading!r} not found in {args.file}", file=sys.stderr)
        return 1

    for line in lines[start + 1 :]:
        match = re.match(r"(#+) ", line)
        if match and len(match.group(1)) <= level:
            break
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
