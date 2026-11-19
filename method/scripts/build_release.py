# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Build one ZIP per skill in skills/, for attaching to a GitHub release.

Each ZIP holds the skill's folder (developer-docs/SKILL.md and so on), named
<skill>-<version>.zip from the skill's metadata.version. Every skill must have
the version you give, so a release never ships a skill with a stale one.
Builds files only; publishing is a separate `gh release create`.

Exit codes:
  0  ZIPs built (their paths printed)
  1  a skill's version doesn't match
  2  bad arguments
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP = {"__pycache__", ".DS_Store"}


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="uv run method/scripts/build_release.py",
        description="Build one ZIP per skill into dist/.",
        epilog=(
            "exit codes: 0 built, 1 version mismatch, 2 bad arguments\n\n"
            "example:\n"
            "  uv run method/scripts/build_release.py 1.0.0\n"
            "  gh release create v1.0.0 dist/*.zip --title v1.0.0 --notes-file notes.md"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("version", help="the release version, such as 1.0.0")
    args = parser.parse_args()

    skills = sorted(p.parent for p in ROOT.glob("skills/*/SKILL.md"))
    wrong = []
    for skill in skills:
        match = re.search(r'^\s+version:\s*"?([^"\n]+)"?', (skill / "SKILL.md").read_text(), re.M)
        if not match or match.group(1) != args.version:
            wrong.append(f"{skill.name} is at {match.group(1) if match else 'no version'}")
    if wrong:
        print(f"Error: every skill must be at {args.version}: " + "; ".join(wrong), file=sys.stderr)
        return 1

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for skill in skills:
        target = dist / f"{skill.name}-{args.version}.zip"
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(skill.rglob("*")):
                if path.is_file() and not SKIP & set(path.parts):
                    archive.write(path, path.relative_to(skill.parent))
        print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
