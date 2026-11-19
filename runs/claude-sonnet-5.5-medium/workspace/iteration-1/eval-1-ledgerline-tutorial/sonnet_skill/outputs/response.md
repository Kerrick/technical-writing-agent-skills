I wrote Part 2 and saved it as `outputs/part-2-totals-with-summarize.md`. I ran every snippet against `ledgerline.py` and the printed output matches what the page shows.

The page builds one `part2.py` file in four steps:
1. It sets up a ledger with salary and rent entries.
2. It calls `summarize()` and shows the output. It also shows how to check the totals by hand.
3. It adds a `groceries` account and summarizes again.
4. It filters the summary with a list of account names.

It also covers the `Decimal(...)` output, sorted account order, the float `TypeError`, and the silent `{}` for an account with no entries. The page warns about the string-argument trap in `summarize("re")`, where a bare string is matched as a substring.

Command blocks follow one convention: the code and the `python part2.py` command are in blocks with no prompt character, and the output is in separate blocks, so the copy button grabs only what runs.

Calls I made that you should check:
- **Part 1's contents:** I didn't have Part 1, so Step 1 rebuilds a similar ledger (salary 3000.00 and rent -1200.00 for March and April). It tells readers they can keep their own ledger, and only the totals will differ. If Part 1 used different accounts or amounts, update Step 1 and the outputs.
- **Sign convention:** I treated rent as negative and salary as positive. The page says this is a tutorial convention and that the library accepts any sign.
- **Links and install:** I didn't link to Part 1, Part 3 or an API reference, because I don't know their URLs. The page assumes `ledgerline` is already importable.