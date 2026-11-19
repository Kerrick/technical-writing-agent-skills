I wrote Part 2 and saved it as `outputs/part-2-summarizing-your-ledger.md`. I ran the tutorial's code against `ledgerline.py` and checked that every output block matches what the code prints. The tutorial itself I haven't run as a reader would, from a `part2.py` file with the package installed.

It follows this order:
1. It rebuilds the Part 1 ledger, with rent and salary entries.
2. It adds groceries and a second month of rent and salary.
3. It shows `entries("groceries")`.
4. It introduces `summarize()`, then a loop that prints a tidy report.
5. It shows `summarize(accounts=[...])`, including the quirk that accounts with no entries are omitted.
6. It ends with the full script in one block and a short recap.

I wrote the code blocks with your copy button in mind. Each block holds only code, with no `>>>` prompts or output mixed in. Output appears in separate `text` blocks, so a copy never picks up output lines.

Please check these before publishing:
- **Part 1 isn't in the repo.** I couldn't see what Part 1 actually used, so Part 2 rebuilds the ledger from scratch. I guessed rent as `-1200.00` and salary as `3500.00`. If Part 1 used different values or memos, update the "Before you start" block and the printed outputs.
- **Sign convention.** I used negative amounts for money going out and positive for money coming in. The library doesn't enforce this, and the tutorial says so.
- **Placeholders.** The link `part-1.md` and the closing line "In Part 3, you'll ..." are placeholders for you to fill in.
- **Version check.** The command that prints the version assumes the package imports as `ledgerline`. That's my guess from `from ledgerline import Ledger`, and I didn't run the command.