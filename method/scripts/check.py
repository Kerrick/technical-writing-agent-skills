# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Run every check the repo has, for the default skill and every run.

For every skill in skills/ and each runs/<run>/skill/developer-docs: the
agent-skills validator. For the skills the method made: the leak check. For each run with a
PLACEMENT.md: the placement check, and the leak check on the files clean-room
steps read. Then REUSE compliance for the whole repo.

Exit codes:
  0  every check passed
  1  some check failed (each failure is shown)
  2  bad arguments
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "method" / "scripts"
VALIDATE = ROOT / "method" / "vendor" / "agent-skills" / "scripts" / "validate.py"
REUSE = "reuse@6.2.0"
CLEAN_ROOM_FILES = ("pipeline/abstracted-full.md", "pipeline/for-the-writer.md", "pipeline/kept.md")


def run(label: str, command: list[str]) -> bool:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    status = "ok  " if result.returncode == 0 else "FAIL"
    print(f"{status} {label}")
    if result.returncode:
        print((result.stdout + result.stderr).strip(), "\n")
    return result.returncode == 0


def skill_files(skill: Path) -> list[str]:
    return [str(p) for p in [skill / "SKILL.md", *sorted((skill / "references").glob("*.md"))] if p.exists()]


def main() -> int:
    argparse.ArgumentParser(
        prog="uv run method/scripts/check.py",
        description="Run every check for the default skill, every run, and REUSE.",
        epilog="exit codes: 0 all passed, 1 some check failed, 2 bad arguments",
    ).parse_args()

    results = []
    for skill in sorted(ROOT.glob("skills/*/")):
        results.append(run(f"validate {skill.relative_to(ROOT)}", ["uv", "run", "-q", str(VALIDATE), str(skill)]))

    # Skills made by the method must carry no source wording.
    made = [ROOT / "skills" / "developer-docs", *sorted(ROOT.glob("runs/*/skill/developer-docs"))]
    for skill in made:
        name = skill.relative_to(ROOT)
        if skill.parent.name == "skill":
            results.append(run(f"validate {name}", ["uv", "run", "-q", str(VALIDATE), str(skill)]))
        results.append(run(f"leak check {name}", ["uv", "run", "-q", str(SCRIPTS / "leak_check.py"), *skill_files(skill)]))

    for run_dir in sorted(ROOT.glob("runs/*/")):
        name = run_dir.relative_to(ROOT)
        files = [str(run_dir / f) for f in CLEAN_ROOM_FILES if (run_dir / f).exists()]
        if files:
            results.append(run(f"leak check {name} pipeline", ["uv", "run", "-q", str(SCRIPTS / "leak_check.py"), *files]))
        if (run_dir / "PLACEMENT.md").exists():
            # A run's own skill, or the default if this run's skill is the default.
            skill_root = run_dir / "skill" if (run_dir / "skill").exists() else ROOT / "skills"
            results.append(run(f"placement {name}", [
                "uv", "run", "-q", str(SCRIPTS / "check_placement.py"),
                str(run_dir / "PLACEMENT.md"), str(run_dir / "pipeline" / "kept.md"), str(skill_root),
            ]))

    results.append(run("REUSE compliance", ["uvx", "-q", REUSE, "lint"]))

    failed = results.count(False)
    print(f"\n{len(results) - failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
