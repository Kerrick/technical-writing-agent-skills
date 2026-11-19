# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Run one headless Claude Code session step for the Sonnet 5.5 run and log it.

Usage:
  uv run run_session.py --step <label> --prompt-file <file> [--resume <id> [--fork]]
                        [--tools Read,Write,...] [--add-dir DIR ...] [--no-tools]

Runs `claude -p --model sonnet --effort medium --output-format json < /dev/null`
from ${WORK}, saves the raw JSON result to logs/<label>.json, and appends a row
to ${WORK}/sessions.md with the session ID, step, usage, and the context size at
the end of the session (the last assistant message's usage in the transcript).
"""

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE / "work"
LOGS = HERE / "logs"
SESSIONS = WORK / "sessions.md"
PROJECTS = Path.home() / ".claude" / "projects"


def transcript_context(session_id: str) -> tuple[int | None, str]:
    """Context size at the end of the session: last assistant usage in its transcript."""
    mangled = str(WORK).replace("/", "-")
    for candidate in [PROJECTS / mangled / f"{session_id}.jsonl", *PROJECTS.glob(f"*/{session_id}.jsonl")]:
        if candidate.exists():
            last = None
            for line in candidate.read_text().splitlines():
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if obj.get("type") == "assistant":
                    usage = obj.get("message", {}).get("usage")
                    if usage:
                        last = usage
            if last:
                total = (last.get("input_tokens", 0) + last.get("cache_read_input_tokens", 0)
                         + last.get("cache_creation_input_tokens", 0))
                return total, str(candidate)
            return None, str(candidate)
    return None, ""


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--step", required=True)
    p.add_argument("--prompt-file", required=True, type=Path)
    p.add_argument("--resume")
    p.add_argument("--fork", action="store_true")
    p.add_argument("--tools", default="")
    p.add_argument("--add-dir", action="append", default=[])
    p.add_argument("--max-turns", type=int)
    args = p.parse_args()

    LOGS.mkdir(exist_ok=True)
    WORK.mkdir(exist_ok=True)
    prompt = args.prompt_file.read_text()

    cmd = ["claude", "-p", prompt, "--model", "sonnet", "--effort", "medium", "--output-format", "json"]
    if args.resume:
        cmd += ["--resume", args.resume]
        if args.fork:
            cmd += ["--fork-session"]
    tools = [t for t in args.tools.split(",") if t]
    if tools:
        cmd += ["--allowedTools", *tools]
    for d in args.add_dir:
        cmd += ["--add-dir", d]
    if args.max_turns:
        cmd += ["--max-turns", str(args.max_turns)]

    start = time.time()
    with open("/dev/null") as devnull:
        proc = subprocess.run(cmd, cwd=WORK, stdin=devnull, capture_output=True, text=True)
    elapsed = time.time() - start

    raw = proc.stdout
    log = LOGS / f"{args.step}.json"
    log.write_text(raw + ("\n--- stderr ---\n" + proc.stderr if proc.stderr else ""))

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        print(f"FAILED to parse JSON (exit {proc.returncode}); see {log}", file=sys.stderr)
        print(raw[-3000:], file=sys.stderr)
        print(proc.stderr[-3000:], file=sys.stderr)
        return 1

    sid = result.get("session_id", "")
    usage = result.get("usage", {})
    model_usage = result.get("modelUsage", {})
    ctx_window = next((v.get("contextWindow") for v in model_usage.values() if v.get("contextWindow")), None)
    models = ", ".join(model_usage.keys())
    ctx_end, transcript = transcript_context(sid)

    row = (f"| {args.step} | `{sid}` | {'fork of ' + args.resume if args.fork else ('resume ' + args.resume if args.resume else 'new')} "
           f"| {models} | {usage.get('input_tokens', 0)} | {usage.get('cache_creation_input_tokens', 0)} | {usage.get('cache_read_input_tokens', 0)} "
           f"| {usage.get('output_tokens', 0)} | {ctx_end if ctx_end is not None else '?'} | {ctx_window or '?'} "
           f"| {result.get('num_turns')} | {int(elapsed)}s | {result.get('subtype')}{' ERROR' if result.get('is_error') else ''} |")
    if not SESSIONS.exists():
        SESSIONS.write_text(
            "# Sessions\n\nEvery headless session of this run, in order. Usage columns are the `usage` block of each "
            "`--output-format json` result (summed over the session's API calls); \"context at end\" is the last assistant "
            "message's input + cache tokens in the transcript, which is how full the context was when the session ended.\n\n"
            "| Step | Session ID | Start | Model | input | cache_creation | cache_read | output | context at end | window | turns | time | status |\n"
            "| - | - | - | - | - | - | - | - | - | - | - | - | - |\n")
    with SESSIONS.open("a") as f:
        f.write(row + "\n")

    print(f"session_id={sid}")
    print(f"status={result.get('subtype')} is_error={result.get('is_error')} turns={result.get('num_turns')} time={int(elapsed)}s")
    print(f"usage={json.dumps(usage)}")
    print(f"context_at_end={ctx_end} window={ctx_window} transcript={transcript}")
    print("--- result text ---")
    print(str(result.get("result", ""))[:6000])
    return 0 if not result.get("is_error") else 1


if __name__ == "__main__":
    sys.exit(main())
