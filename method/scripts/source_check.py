# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check a skill against the sources it was built from, for wording and arrangement.

For each source in method/sources.toml, runs skill-authoring's scripts/overlap.py
(lines sharing a run of eight or more words) and scripts/structure.py (paraphrase,
and paragraphs that follow a source page's order) on every Markdown file of the
skill, against that source's pinned paths in the checkout folder. Needs the
sources fetched first: mise run fetch -- SRC.

The skill's CC0 dedication holds only if this finds nothing: copied text from a
CC BY source needs credit, from a share-alike source makes the skill
share-alike, and from an MIT, BSD, or PostgreSQL source carries its notice.
A structure failure is a list of lines to read, not a verdict.

Exit codes:
  0  no source shares wording or arrangement with the skill
  1  some source does (each finding is shown)
  2  bad arguments, or a source not fetched
"""

import argparse
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "skills" / "skill-authoring" / "scripts"


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="uv run method/scripts/source_check.py",
        description="Check a skill against its sources for shared wording and arrangement.",
        epilog=(
            "exit codes: 0 clean, 1 findings, 2 bad arguments or sources not fetched\n\n"
            "examples:\n"
            "  uv run method/scripts/source_check.py ~/tw/sources\n"
            "  uv run method/scripts/source_check.py ~/tw/sources --skill runs/claude-sonnet-5.5-medium/skill/developer-docs"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("src", type=Path, help="the folder mise run fetch cloned the sources into")
    parser.add_argument("--skill", type=Path, default=ROOT / "skills" / "developer-docs",
                        help="the skill folder to check (default: skills/developer-docs)")
    args = parser.parse_args()

    files = sorted(str(p) for p in args.skill.rglob("*.md"))
    if not files:
        parser.error(f"no Markdown files under {args.skill}")
    sources = tomllib.loads((ROOT / "method" / "sources.toml").read_text())["source"]
    found = False
    for source in sources:
        paths = [args.src / source["dir"] / p for p in source["paths"]]
        missing = [p for p in paths if not p.exists()]
        if missing:
            print(f"Error: {missing[0]} not found; run: mise run fetch -- {args.src}", file=sys.stderr)
            return 2
        print(f"== {source['key']} ({source['name']})", flush=True)
        overlap = [sys.executable, str(SCRIPTS / "overlap.py")]
        for p in paths:
            overlap += ["--source", str(p)]
        found |= subprocess.run(overlap + files).returncode == 1
        for p in paths:
            found |= subprocess.run([sys.executable, str(SCRIPTS / "structure.py"), "--source", str(p), *files]).returncode == 1
    print("findings above" if found else "no shared wording or arrangement found")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
