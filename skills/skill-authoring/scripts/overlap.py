# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Find word runs that files share with a source: the literal-copying gate.

Tokenizes to lowercase words, collects every N-word run in the source's
Markdown/text files, and reports each line of FILES that contains one.

Exit codes: 0 no shared runs, 1 shared runs found, 2 bad arguments.
"""
import argparse, json, re, sys
from pathlib import Path

TOKEN = re.compile(r"[a-z0-9']+")


def runs(words, n):
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="uv run scripts/overlap.py",
        description="Report lines of FILES that share an N-word run with SOURCE.",
        epilog="exit codes: 0 clean, 1 shared runs found, 2 bad arguments\n\n"
               "examples:\n  uv run scripts/overlap.py --source src/ out/skill/SKILL.md out/skill/references/*.md\n"
               "  uv run scripts/overlap.py --source src/ --n 6 --summary out/skill/*.md",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, type=Path, action="append",
                    help="folder or file to compare against (repeatable)")
    ap.add_argument("--n", type=int, default=8, help="run length in words (default 8; use 6 for a stricter look)")
    ap.add_argument("--ext", default=".md,.markdown,.txt,.html,.rst", help="source file extensions")
    ap.add_argument("--summary", action="store_true", help="print only per-file totals")
    ap.add_argument("--json", action="store_true", help="print findings as JSON")
    ap.add_argument("files", nargs="+", type=Path)
    a = ap.parse_args()
    exts = tuple(a.ext.split(","))
    grams = set()
    for src in a.source:
        if not src.exists():
            ap.error(f"--source {src} does not exist")
        paths = [src] if src.is_file() else [p for p in src.rglob("*") if p.suffix in exts]
        for p in paths:
            grams |= runs(TOKEN.findall(p.read_text(errors="ignore").lower()), a.n)
    findings = []
    for f in a.files:
        if not f.is_file():
            ap.error(f"{f} is not a file")
        for num, line in enumerate(f.read_text().splitlines(), 1):
            w = TOKEN.findall(line.lower())
            hit = set()
            for i in range(len(w) - a.n + 1):
                if tuple(w[i:i + a.n]) in grams:
                    hit |= set(range(i, i + a.n))
            if hit:
                findings.append({"file": str(f), "line": num, "shared_words": len(hit),
                                 "words": len(w), "run": " ".join(w[i] for i in sorted(hit))})
    if a.json:
        print(json.dumps(findings, indent=1))
    elif a.summary:
        tot = {}
        for x in findings:
            tot[x["file"]] = tot.get(x["file"], 0) + x["shared_words"]
        for f, t in tot.items():
            print(f"{f}\t{t} shared words")
    else:
        for x in findings:
            print(f"{x['file']}:{x['line']}: {x['shared_words']}/{x['words']} words: {x['run'][:200]}")
    if findings:
        print(f"{len(findings)} line(s) share a {a.n}-word run", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
