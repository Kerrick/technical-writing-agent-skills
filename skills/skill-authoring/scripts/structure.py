# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Sentence similarity and order correlation against a source: the non-literal gate.

For each file: matches every paragraph to its most similar source paragraph
(TF-IDF cosine), then measures, within each source file, whether the matched
paragraphs appear in the source's order (Kendall tau). Also lists sentences
whose best source sentence is similar above a threshold.

A file FAILS when it matches more than 3 source paragraphs AND either more than
2 similar sentences, or an in-page tau of 0.5 or more on a source file with at
least 4 matches. Before trusting the defaults on a new source, run this on a
known structural copy (it should fail) and on unrelated writing by the same
author (it should pass), and adjust --para and --sentence until it separates
them. Treat a FAIL as a list of lines to read, not a verdict:
text that shares the source's ideas will match some sentences by topic.

Exit codes: 0 all files pass, 1 a file fails, 2 bad arguments.
"""
import argparse, json, math, re, sys
from collections import Counter, defaultdict
from pathlib import Path

STOP = set("the a an and or of to in on for is are be it that this with as by at from not no your you its "
           "their they we our can may must should will would do does if then than so only any all each every one "
           "into out up when while which what who how there here been was were has have had but also more most such".split())


def tok(t):
    return [w for w in re.findall(r"[a-z][a-z0-9'-]+", t.lower()) if w not in STOP and len(w) > 2]


def paras(text):
    return [p.strip() for p in re.split(r"\n\s*\n|\n(?=[-*\d]+[.)]? )", text) if len(tok(p)) >= 6]


def sents(text):
    return [s for s in re.split(r"(?<=[.!?])\s+|\n", text) if len(tok(s)) >= 6]


def tau(xs):
    c = d = 0
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] != xs[j]:
                c, d = (c + 1, d) if xs[i] < xs[j] else (c, d + 1)
    return (c - d) / (c + d) if c + d else 0.0


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="uv run scripts/structure.py",
        description="Check FILES for paraphrase and source-ordered arrangement against SOURCE.",
        epilog="exit codes: 0 pass, 1 a file fails, 2 bad arguments\n\n"
               "example:\n  uv run scripts/structure.py --source src/ out/skill/SKILL.md out/skill/references/*.md",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, type=Path, help="source folder (one file per page)")
    ap.add_argument("--ext", default=".md,.markdown,.txt,.html,.rst")
    ap.add_argument("--para", type=float, default=0.25, help="paragraph match threshold (default 0.25)")
    ap.add_argument("--sentence", type=float, default=0.40, help="similar-sentence threshold (default 0.40)")
    ap.add_argument("--show", type=int, default=4, help="similar sentences to print per file")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("files", nargs="+", type=Path)
    a = ap.parse_args()
    if not a.source.is_dir():
        ap.error(f"--source {a.source} is not a folder")
    pages = sorted(p for p in a.source.rglob("*") if p.suffix in tuple(a.ext.split(",")))
    if not pages:
        ap.error(f"no source files with extensions {a.ext} under {a.source}")
    units, ssents = [], []
    for pi, p in enumerate(pages):
        text = p.read_text(errors="ignore")
        units += [(pi, i, tok(x)) for i, x in enumerate(paras(text))]
        ssents += [(s, tok(s)) for s in sents(text)]
    df = Counter(w for *_, t in units for w in set(t)); n = len(units)

    def vec(t):
        c = Counter(t); v = {w: k * (math.log((n + 1) / (df.get(w, 0) + 1)) + 1) for w, k in c.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        return {w: x / norm for w, x in v.items()}

    def cos(x, y):
        return sum(v * y.get(w, 0) for w, v in x.items())

    U = [(pi, i, vec(t)) for pi, i, t in units]; SS = [(s, vec(t)) for s, t in ssents]
    results, failed = [], False
    for f in a.files:
        if not f.is_file():
            ap.error(f"{f} is not a file")
        text = f.read_text(); seq = []
        for para in paras(text):
            v = vec(tok(para)); best = max(U, key=lambda u: cos(v, u[2]))
            if cos(v, best[2]) >= a.para:
                seq.append((best[0], best[1]))
        similar = []
        for s in sents(text):
            v = vec(tok(s)); b = max(SS, key=lambda u: cos(v, u[1])); sc = cos(v, b[1])
            if sc >= a.sentence:
                similar.append((round(sc, 2), s[:110], b[0][:110]))
        bypage = defaultdict(list)
        for pg, i in seq:
            bypage[pg].append(i)
        page_tau = {str(pages[pg].relative_to(a.source)): round(tau(v), 2) for pg, v in bypage.items() if len(v) >= 4}
        worst = max(page_tau.items(), key=lambda kv: kv[1]) if page_tau else ("-", 0.0)
        fail = len(seq) > 3 and (len(similar) > 2 or worst[1] >= 0.5)
        failed |= fail
        results.append({"file": str(f), "matched_paragraphs": len(seq), "worst_in_page_tau": worst[1],
                        "worst_page": worst[0], "similar_sentences": sorted(similar, reverse=True), "fail": fail})
    if a.json:
        print(json.dumps(results, indent=1))
    else:
        for r in results:
            print(f"{r['file']}: matched paragraphs {r['matched_paragraphs']}, worst in-page tau "
                  f"{r['worst_in_page_tau']:+.2f} ({r['worst_page']}), similar sentences "
                  f"{len(r['similar_sentences'])}  {'FAIL' if r['fail'] else 'ok'}")
            for sc, mine, theirs in r["similar_sentences"][:a.show]:
                print(f"   {sc:.2f}  {mine!r}\n         ~ {theirs!r}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
