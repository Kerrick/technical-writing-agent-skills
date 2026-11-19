I wrote Part 2 and saved it as `outputs/part-2-summarizing-your-ledger.md`. I ran every code snippet against ledgerline 2.1.0, and the output shown in the tutorial is what the code actually prints.

**How it's organized:** readers set up a `budget.py` file, call `summarize()`, turn the result into a readable report with a net total, filter it with `accounts=[...]`, and see what happens with accounts that have no entries. It ends with the complete script and a short recap.

**How it fits your copy button:**
- Every code block runs as written. Nothing uses `>>>` prompts, and no output is mixed into the code.
- Output goes in its own separate `text` blocks, so copying a code block never picks up output.
- The complete script at the end can be copied and run by itself.

**Library behaviour the tutorial covers:**
- **Sorted by name:** results come back sorted by account name, not in the order entries were added.
- **`Decimal` totals:** totals print as `Decimal('...')`. The tutorial shows that an f-string prints the plain number.
- **Missing accounts:** an account named in `accounts` with no entries is left out of the result, not shown as zero, so the tutorial suggests `.get()` with a default.
- **Pass a list:** I tell readers to always pass a list to `accounts`. A bare string like `summarize(accounts="rent")` appears to work, but the library checks names with `in`, which matches substrings. I confirmed that an account named `"ent"` gets included. You may want to fix this in the library itself, for example by rejecting a bare string.

**Things to check:**
- **Part 1's example data:** I haven't seen Part 1, so I guessed at it. Step 1 assumes `from ledgerline import Ledger`, account names `"rent"` and `"salary"`, string amounts, and negative numbers for expenses. It then adds a second month and a `groceries` account. If Part 1 used different names or signs, change Step 1 to match.
- **Link to Part 1:** the link is a placeholder (`part-1.md`). Point it at the real page.
- **Test files:** my test scripts and a copy of the library are in `scratch/`. They aren't part of the tutorial, and you can delete them.