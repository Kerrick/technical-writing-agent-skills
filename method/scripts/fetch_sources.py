# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Clone every source in method/sources.toml at its pinned commit.

Each clone is shallow (one commit) and sparse (only the paths the method reads,
plus the files at the repository root, such as licenses and contributor
guides), so even large repositories download quickly. Safe to rerun: a
checkout already at its pinned commit is left alone, and a checkout at any
other commit is reported and left alone too, never reset.

Exit codes:
  0  every source is at its pinned commit
  1  some source failed or is at another commit (listed on stderr)
  2  bad arguments
"""

import argparse
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def git(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="uv run method/scripts/fetch_sources.py",
        description="Clone the sources at their pinned commits, shallow and sparse.",
        epilog=(
            "exit codes: 0 all at their commits, 1 failures or mismatches, 2 bad arguments\n\n"
            "examples:\n"
            "  uv run method/scripts/fetch_sources.py ~/tw/sources\n"
            "  uv run method/scripts/fetch_sources.py ~/tw/sources --only react rust --dry-run"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("src", type=Path, help="${SRC}: folder to clone the sources into")
    parser.add_argument("--only", nargs="+", metavar="KEY", help="only these source keys (see prompt.py --list-sources)")
    parser.add_argument("--dry-run", action="store_true", help="say what would be cloned, and clone nothing")
    args = parser.parse_args()

    sources = tomllib.loads((ROOT / "method" / "sources.toml").read_text())["source"]
    if args.only:
        unknown = set(args.only) - {s["key"] for s in sources}
        if unknown:
            parser.error(f"unknown source key(s): {', '.join(sorted(unknown))}")
        sources = [s for s in sources if s["key"] in args.only]

    # One checkout per directory; sources that share one (the Rails halves) share its paths.
    checkouts: dict[str, dict] = {}
    for s in sources:
        c = checkouts.setdefault(s["dir"], {"repo": s["repo"], "commit": s["commit"], "paths": []})
        c["paths"] += [p for p in s["paths"] if p not in c["paths"]]

    problems = 0
    for name, c in checkouts.items():
        target = args.src.expanduser() / name
        short = c["commit"][:9]
        try:
            if target.exists():
                head = git("rev-parse", "HEAD", cwd=target)
                if head == c["commit"]:
                    print(f"ok       {name} is at {short}")
                else:
                    print(f"mismatch {name} is at {head[:9]}, not {short}; left alone", file=sys.stderr)
                    problems += 1
                continue
            if args.dry_run:
                print(f"would    clone {c['repo']} at {short} into {target}, paths: {', '.join(c['paths'])}")
                continue
            print(f"cloning  {name} at {short} ({', '.join(c['paths'])})")
            target.mkdir(parents=True)
            try:
                git("init", "-q", cwd=target)
                git("remote", "add", "origin", c["repo"], cwd=target)
                git("sparse-checkout", "set", "--cone", *c["paths"], cwd=target)
                git("fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", c["commit"], cwd=target)
                git("checkout", "-q", "FETCH_HEAD", cwd=target)
            except RuntimeError:
                shutil.rmtree(target)  # only ever a folder this run created
                raise
            print(f"ok       {name} is at {short}")
        except RuntimeError as error:
            print(f"failed   {name}: {error}", file=sys.stderr)
            problems += 1

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
