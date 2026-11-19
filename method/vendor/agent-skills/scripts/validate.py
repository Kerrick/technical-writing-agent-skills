# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "skills-ref==0.1.1",
# ]
# ///
"""Validate Agent Skills against the specification, using the skills-ref reference library.

Checks each skill's SKILL.md frontmatter: required fields, allowed fields,
naming rules, length limits, and that `name` matches the directory name.

Exit codes:
  0  every skill is valid
  1  at least one skill has validation errors
  2  bad arguments
"""

import argparse
import json
import sys
from pathlib import Path

from skills_ref import validate


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="uv run scripts/validate.py",
        description="Validate Agent Skills against the specification (skills-ref 0.1.1).",
        epilog=(
            "exit codes: 0 all valid, 1 validation errors, 2 bad arguments\n\n"
            "examples:\n"
            "  uv run scripts/validate.py path/to/my-skill\n"
            "  uv run scripts/validate.py --json skills/*/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "skills",
        nargs="+",
        type=Path,
        metavar="SKILL_DIR",
        help="skill directory, or its SKILL.md file",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help='print one JSON array of {"skill", "valid", "errors"} to stdout',
    )
    args = parser.parse_args()

    results = []
    for path in args.skills:
        if path.is_file() and path.name.lower() == "skill.md":
            path = path.parent
        # skills-ref compares the directory's name to `name`, and "." has no name.
        errors = validate(path.resolve())
        results.append({"skill": str(path), "valid": not errors, "errors": errors})

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for result in results:
            if result["valid"]:
                print(f"Valid skill: {result['skill']}")
            else:
                print(f"Invalid skill: {result['skill']}", file=sys.stderr)
                for error in result["errors"]:
                    print(f"  - {error}", file=sys.stderr)

    return 0 if all(result["valid"] for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
