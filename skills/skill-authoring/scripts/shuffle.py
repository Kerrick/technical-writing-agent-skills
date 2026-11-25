# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Shuffle rule cards so no step downstream inherits the source's order.

Cards are Markdown blocks headed `### C-<source ids>`, e.g. `### C-R12+A18`.

  shuffle  CARDS OUT MAP   Write the cards to OUT in random order with fresh
                           ids (K100-K999), dropping the source ids; save the
                           K -> source-id map to MAP (keep it away from every
                           step that writes or sorts).
  common   MAP_A MAP_B CARDS_A OUTDIR FILE_A... -- FILE_B...
                           Translate two independent sorts (each made from its
                           own shuffle) to one shared set of fresh ids (C100-C999):
                           writes OUTDIR/cards.md and each FILE as OUTDIR/a-<name>
                           or OUTDIR/b-<name>, plus OUTDIR/../map-common.json.

Exit codes: 0 ok, 1 coverage check failed, 2 bad arguments.
"""
import argparse, json, random, re, sys
from pathlib import Path

HEAD = re.compile(r"(?m)^### C-(.+)$")


def parse_cards(text):
    parts = re.split(r"(?m)^(?=### C-)", text)
    return [(HEAD.match(p).group(1).strip(), p.split("\n", 1)[1].strip()) for p in parts if p.startswith("### C-")]


def expected_ids(spec):
    ids = set()
    for part in spec.split(","):
        m = re.fullmatch(r"([A-Za-z]+)(\d+)-\1?(\d+)", part.strip())
        if not m:
            raise SystemExit(f"--expect: can't read {part!r}; use ranges like R1-R116,A1-A25")
        ids |= {f"{m.group(1)}{i}" for i in range(int(m.group(2)), int(m.group(3)) + 1)}
    return ids


def main() -> int:
    ap = argparse.ArgumentParser(prog="uv run scripts/shuffle.py", description=__doc__.split("\n\n")[0],
                                 epilog=__doc__.split("\n\n", 1)[1], formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("shuffle"); s.add_argument("cards", type=Path); s.add_argument("out", type=Path); s.add_argument("map", type=Path)
    s.add_argument("--expect", help="source ids that must each appear exactly once, e.g. R1-R116,A1-A25")
    c = sub.add_parser("common"); c.add_argument("map_a", type=Path); c.add_argument("map_b", type=Path)
    c.add_argument("cards_a", type=Path); c.add_argument("outdir", type=Path); c.add_argument("files", nargs="+")
    a = ap.parse_args(); rng = random.SystemRandom()
    if a.cmd == "shuffle":
        cards = parse_cards(a.cards.read_text())
        if not cards:
            ap.error(f"no '### C-<ids>' cards in {a.cards}")
        if a.expect:
            ids = re.findall(r"[A-Za-z]+\d+", " ".join(h for h, _ in cards)); want = expected_ids(a.expect)
            missing, dup = sorted(want - set(ids)), sorted({i for i in ids if ids.count(i) > 1})
            if missing or dup:
                print(f"coverage failed: missing {missing}, duplicated {dup}", file=sys.stderr); return 1
        rng.shuffle(cards); keys = rng.sample(range(100, 1000), len(cards))
        a.out.write_text("# Rule cards (unordered)\n\n" + "".join(f"### K{k}\n{body}\n\n" for k, (_, body) in zip(keys, cards)))
        a.map.write_text(json.dumps({f"K{k}": h for k, (h, _) in zip(keys, cards)}, indent=0))
        print(f"{len(cards)} cards shuffled to {a.out}; map in {a.map}"); return 0
    if "--" not in a.files:
        ap.error("common: separate sort A's files from sort B's with --")
    i = a.files.index("--"); fa, fb = a.files[:i], a.files[i + 1:]
    ma, mb = json.loads(a.map_a.read_text()), json.loads(a.map_b.read_text())
    if set(ma.values()) != set(mb.values()):
        ap.error("the two maps don't cover the same cards")
    heads = sorted(set(ma.values())); common = dict(zip(heads, (f"C{n}" for n in rng.sample(range(100, 1000), len(heads)))))
    A = {k: common[h] for k, h in ma.items()}; B = {k: common[h] for k, h in mb.items()}
    tr = lambda text, m: re.sub(r"\bK\d{3}\b", lambda x: m.get(x.group(), x.group()), text)
    a.outdir.mkdir(parents=True, exist_ok=True)
    for files, m, tag in ((fa, A, "a"), (fb, B, "b")):
        for f in files:
            (a.outdir / f"{tag}-{Path(f).name}").write_text(tr(Path(f).read_text(), m))
    blocks = re.split(r"(?m)^(?=### K\d{3})", a.cards_a.read_text())[1:]
    blocks.sort(key=lambda b: A[b[4:8]])
    (a.outdir / "cards.md").write_text("# Rule cards\n\n" + "".join(tr(b, A) for b in blocks))
    (a.outdir.parent / "map-common.json").write_text(json.dumps(common, indent=0))
    print(f"{len(heads)} cards on shared ids in {a.outdir}"); return 0


if __name__ == "__main__":
    sys.exit(main())
