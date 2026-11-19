I wrote Part 2 and saved it as `outputs/part-2-summarize.md`.

It's a hands-on tutorial. The reader builds `part2.py` step by step: more entries, then `summarize()`, a formatted loop, `summarize([...])` with a list of accounts, `entries()`, and a deliberate float `TypeError`. It closes with a full-file checkpoint and an exercise with a hidden solution. The checkpoint prints:

```text
groceries: -107.60
rent: -2400.00
salary: 7000.00
```

**What I ran:** I extracted the final `part2.py` from the Markdown and ran it against `ledgerline.py` on Python 3.15. I also ran the exercise solution and its substring pitfall. The shown outputs match those runs. The traceback in the float step was run on its own and trimmed to its last line in the text.

**Assumptions to check:**
- **Part 1 isn't in the folder.** I didn't know its variable names, amounts or file name, so Part 2 starts a fresh `part2.py` that rebuilds the ledger. If Part 1 used different numbers, you may want to align them.
- **Sign convention.** The doc says spending is negative and income positive. It labels this as the tutorial's own convention, since the library doesn't enforce it.
- **Prerequisite wording.** I only had Python 3.15 available. The doc says "Python 3 installed (run on 3.15)" rather than claiming a minimum version.

**How it handles copy-paste:** each code block holds exactly one action, with no output or prompts mixed in. Later steps say "add to the end of `part2.py`", and every output is in a separate `text` block.

**Not covered:** I didn't test the troubleshooting note for `ModuleNotFoundError`, and I didn't check how the site renders the `<details>` solution block. If your site doesn't render `<details>`, the solution will show as plain text.