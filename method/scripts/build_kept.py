"""Build kept.md, the writer's only input, from merged.md.

Keeps each "Kept" entry's heading, Rule, Kind, Applies to and Without it. Drops
Sources, Conflict resolved, every citation of the baseline skill, and the
"Dropped" and "Counts" sections, so a writer who has never seen the baseline or
the sources learns nothing about either. Relabels Kind for that reader:

  missed principle        -> not commonly known
  correction              -> overrides common advice
  baseline, often broken  -> well known, often broken

Exit codes:
  0  written
  1  merged.md has no "## Kept" section, or an entry has no Kind
  2  bad arguments
"""

import argparse
import re
import sys
from pathlib import Path

FIELDS = {"Rule", "Kind", "Applies to", "Without it"}
KINDS = {
    "missed principle": "not commonly known",
    "correction": "overrides common advice",
    "baseline, often broken": "well known, often broken",
}


def relabel(line: str) -> str:
    kind = re.sub(r"^- \*\*Kind:\*\*\s*", "", line).lower()
    for old, new in KINDS.items():
        if kind.startswith(old):
            return f"- **Kind:** {new}."
    raise ValueError(f"unknown Kind: {line!r} (expected one of: {', '.join(KINDS)})")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="python3 method/scripts/build_kept.py",
        description="Build the writer's kept.md from merged.md.",
        epilog="example:\n  python3 method/scripts/build_kept.py runs/claude-opus-5.5-medium/pipeline/merged.md -o kept.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("merged", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()

    text = args.merged.read_text()
    if "## Kept" not in text:
        print(f"Error: no '## Kept' section in {args.merged}", file=sys.stderr)
        return 1
    kept = text.split("## Kept", 1)[1].split("## Dropped", 1)[0]

    out = [
        "# Rules to write into the skill",
        "",
        "Each rule below has a heading, the rule itself, its kind, where it applies, and what an agent does wrong without it.",
    ]
    field = None
    try:
        for line in kept.splitlines():
            if line.startswith("### "):
                field = None
                out += ["", line]
                continue
            match = re.match(r"- \*\*([^*]+):\*\*", line)
            if match:
                field = match.group(1)
            if field in FIELDS:
                out.append(relabel(line) if field == "Kind" and match else line)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    args.output.write_text("\n".join(out).strip() + "\n")
    print(f"Wrote {sum(1 for l in out if l.startswith('### '))} rules to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
