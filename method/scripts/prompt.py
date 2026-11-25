# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Print one step's prompt with every slot filled, ready to paste into a session.

Prompts come from the first fenced block of each file in method/prompts/, and
per-source values from method/sources.toml. Slots use string.Template syntax
(${SRC}). Any slot a prompt uses must be given as an option; the script stops
and says which, rather than printing a prompt with a slot left in it.

Steps:
  recall          step 1, a new session
  baseline        step 2, the same session (the fork point)
  reading         step 3, first message to a source's reading fork   (--source)
  after-reading   extra reading some sources do before comparing     (--source)
  compare         step 4, second message to a reading fork          (--source)
  audit           step 5, a new fork
  merge           step 6, a new fork (in compose mode, with the layered-sources rules)
  check           step 7, a new fork
  apply           step 8, back to the merge fork
  write           step 9, a fresh session

Exit codes:
  0  prompt printed
  1  missing slot value, unknown source, or a source with no such message
  2  bad arguments
"""

import argparse
import re
import sys
import tomllib
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[2]
PROMPTS = ROOT / "method" / "prompts"
FILES = {
    "recall": "01-recall.md",
    "baseline": "02-baseline.md",
    "compare": "04-compare.md",
    "audit": "05-audit.md",
    "merge": "06-merge.md",
    "check": "07-check-often-broken.md",
    "apply": "08-apply-check.md",
    "write": "09-write.md",
}
PER_SOURCE = ("reading", "after-reading", "compare")
STEPS = ("recall", "baseline", *PER_SOURCE, "audit", "merge", "check", "apply", "write")


def first_block(path: Path) -> str:
    match = re.search(r"^```[^\n]*\n(.*?)^```", path.read_text(), re.M | re.S)
    if not match:
        raise SystemExit(f"Error: no fenced prompt block in {path}")
    return match.group(1).rstrip("\n")


def merge_prompt(mode: str, sources: list[dict]) -> str:
    """The merge prompt; in compose mode, with rules 2 and 3 from its "Layered sources" block."""
    text = first_block(PROMPTS / FILES["merge"])
    if mode == "corroborate":
        return text
    blocks = re.findall(r"^```[^\n]*\n(.*?)^```", (PROMPTS / FILES["merge"]).read_text(), re.M | re.S)
    if len(blocks) < 2:
        raise SystemExit(f"Error: {FILES['merge']} has no layered-sources block for compose mode")
    lines = text.split("\n")
    for rule in blocks[1].strip().split("\n"):
        number = rule.split(".", 1)[0] + ". "
        hits = [i for i, line in enumerate(lines) if line.startswith(number)]
        if len(hits) != 1:
            raise SystemExit(f"Error: can't find rule {number.strip()} to replace in the merge prompt")
        lines[hits[0]] = rule
    layers = {}
    for s in sources:
        if not s.get("layer"):
            raise SystemExit(f"Error: compose mode needs a layer for every source; {s['key']} has none")
        layers.setdefault(s["letter"], s["layer"])
    described = " ".join(f"Source {letter} owns {layer}." for letter, layer in sorted(layers.items()))
    return Template("\n".join(lines)).safe_substitute(LAYERS=described)


def compare_prompt(source: dict) -> str:
    """Fill the per-source parts of the compare template, leaving the global slots."""
    paragraphs = first_block(PROMPTS / FILES["compare"]).split("\n\n")
    if not source.get("focus"):
        paragraphs = [p for p in paragraphs if p != "${FOCUS}"]
    if source.get("first_paragraph_extra"):
        paragraphs[0] += " " + source["first_paragraph_extra"]
    if source.get("prefix"):
        paragraphs.insert(0, source["prefix"])

    plural = source.get("plural", False)
    return Template("\n\n".join(paragraphs)).safe_substitute(
        STYLE_GUIDE=source["style_guide"],
        SOURCE=source["name"],
        HOUSE=source["house"],
        FOCUS=source.get("focus", ""),
        LICENSE=source["license"],
        NAMES=source["names"],
        OUTPUT="${WORK}/" + source["output"],
        SOURCE_LINE=source["source_line"],
        does="do" if plural else "does",
        shows="show" if plural else "shows",
        falls="fall" if plural else "falls",
        confirms="confirm" if plural else "confirms",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="uv run method/scripts/prompt.py",
        description="Print one step's prompt with every slot filled.",
        epilog=(
            "exit codes: 0 printed, 1 missing value or unknown source, 2 bad arguments\n\n"
            "examples:\n"
            "  uv run method/scripts/prompt.py --list-sources\n"
            "  uv run method/scripts/prompt.py reading --source rails-1 --src ~/tw/sources\n"
            "  uv run method/scripts/prompt.py compare --source rails-1 --src ~/tw/sources --work ~/tw/work\n"
            "  uv run method/scripts/prompt.py write --work ~/tw/work --run runs/openai-astra-6.2-medium"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("step", nargs="?", choices=STEPS)
    parser.add_argument("--source", help="source key from method/sources.toml (see --list-sources)")
    parser.add_argument("--src", help="${SRC}: folder holding the source checkouts")
    parser.add_argument("--work", help="${WORK}: this run's working folder")
    parser.add_argument("--run", help="${RUN}: this run's folder, e.g. runs/openai-astra-6.2-medium")
    parser.add_argument("--agent-skills", default=str(ROOT / "method" / "vendor" / "agent-skills"),
                        help="${AGENT_SKILLS} (default: the vendored copy)")
    parser.add_argument("--lister", default="Sonnet",
                        help="${LISTER}: the cheaper sub-agent model that lists files (default: Sonnet)")
    parser.add_argument("--list-sources", action="store_true", help="list source keys and exit")
    args = parser.parse_args()

    config = tomllib.loads((ROOT / "method" / "sources.toml").read_text())
    sources, mode = config["source"], config.get("mode", "corroborate")
    if mode not in ("corroborate", "compose"):
        print(f"Error: mode in method/sources.toml must be corroborate or compose, not {mode!r}", file=sys.stderr)
        return 1
    by_key = {s["key"]: s for s in sources}

    if args.list_sources:
        for s in sources:
            print(f"{s['key']:10} {s['letter']}  {s['name']}")
        return 0
    if not args.step:
        parser.error("give a step, or --list-sources")

    source = None
    if args.step in PER_SOURCE:
        if args.source not in by_key:
            print(f"Error: --source must be one of: {', '.join(by_key)}", file=sys.stderr)
            return 1
        source = by_key[args.source]
        if args.step == "reading":
            text = source["reading"]
        elif args.step == "after-reading":
            if "after_reading" not in source:
                print(f"Error: {args.source} has no after-reading message; go straight to compare.", file=sys.stderr)
                return 1
            text = source["after_reading"]
        else:
            text = compare_prompt(source)
    elif args.step == "merge":
        text = merge_prompt(mode, sources)
    else:
        text = first_block(PROMPTS / FILES[args.step])

    given = {
        "SRC": args.src, "WORK": args.work, "RUN": args.run,
        "AGENT_SKILLS": args.agent_skills, "LISTER": args.lister,
    }
    template = Template(text)
    missing = [name for name in template.get_identifiers() if not given.get(name)]
    if missing:
        flags = ", ".join("--" + name.lower().replace("_", "-") for name in missing)
        print(f"Error: this prompt needs {flags}", file=sys.stderr)
        return 1
    print(template.substitute({k: v.rstrip("/") for k, v in given.items() if v}))

    if source and args.step == "reading" and source.get("reading_check"):
        print(f"\n(Check the list before the fork reads anything: {source['reading_check']})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
