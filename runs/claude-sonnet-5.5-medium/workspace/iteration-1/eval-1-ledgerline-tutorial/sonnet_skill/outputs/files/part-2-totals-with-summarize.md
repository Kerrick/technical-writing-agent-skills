# Part 2: Get per-account totals with `summarize()`

In Part 1 you created a `Ledger` and added entries for rent and salary. Now you have a list of entries, and the question you actually care about is "how much did I spend on rent, and how much did I earn?" Adding that up by hand gets old fast. In this part you will ask the ledger to do it with `summarize()`.

By the end you will have a short script that prints one total for each account.

This part assumes you finished Part 1 and have Python installed with `ledgerline` importable. It covers the common path for `summarize()`. It does not cover how to store a ledger on disk, because `ledgerline` keeps entries in memory only.

## Step 1: Set up the ledger

Create a file named `part2.py`. To keep this part self-contained, it rebuilds a ledger like the one from Part 1, with two months of entries. Rent is a negative amount (money going out) and salary is positive (money coming in). This is the convention used in this tutorial. `ledgerline` itself accepts any sign.

```python
from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", "3000.00", "March pay")
ledger.add("rent", "-1200.00", "March rent")
ledger.add("salary", "3000.00", "April pay")
ledger.add("rent", "-1200.00", "April rent")
```

The amounts are strings, not floats. A `Ledger` stores amounts as `Decimal` values, and it raises `TypeError` for a float because a float cannot represent cents exactly. Pass a string, an `int` or a `Decimal`.

If your Part 1 ledger has different accounts or amounts, keep it. Every step below works the same way, and only your totals will differ.

## Step 2: Ask for the totals

Add these lines to the end of `part2.py`:

```python
totals = ledger.summarize()
print(totals)
```

Run the file:

```
python part2.py
```

You should see:

```
{'rent': Decimal('-2400.00'), 'salary': Decimal('6000.00')}
```

`summarize()` returned a dictionary with one key for each account and the sum of that account's amounts as the value. Check it by hand: two rent entries of -1200.00 add up to -2400.00, and two salary entries of 3000.00 add up to 6000.00.

Two details of the result are worth knowing:

- The accounts are sorted by name, so `rent` comes before `salary` however you added them.
- The totals are `Decimal` values. The `Decimal('...')` wrapper appears because `print` shows a dictionary's values in their `repr` form. Use `str(totals["rent"])` or an f-string when you want only the number.

## Step 3: Add another account and summarize again

A new account needs no setup. Add an entry to it and it appears in the next summary. Append this to `part2.py`:

```python
ledger.add("groceries", "-84.30", "Weekly shop")
print(ledger.summarize())
```

Run the file again. The output now has the first line from Step 2 and a second line:

```
{'rent': Decimal('-2400.00'), 'salary': Decimal('6000.00')}
{'groceries': Decimal('-84.30'), 'rent': Decimal('-2400.00'), 'salary': Decimal('6000.00')}
```

`groceries` sorts first, so it is the first key. The ledger only reads its entries when you call `summarize()`, so each call gives you the current totals.

## Step 4: Limit the summary to some accounts

Pass a list of account names to get totals for only those accounts. Append this to `part2.py`:

```python
print(ledger.summarize(["rent", "groceries"]))
```

The new line of output is:

```
{'groceries': Decimal('-84.30'), 'rent': Decimal('-2400.00')}
```

Pass a list (or a tuple or set) of names, even for one account: `ledger.summarize(["rent"])`. A bare string such as `"rent"` happens to work, but only because Python tests whether each account name is a substring of that string. `summarize("re")` would match `rent` too, so avoid it.

An account that has no entries is left out of the result, even if you name it. Asking for `["groceries_typo"]` gives `{}` and no error, so an empty result can mean a misspelled name as well as an empty ledger.

## What you built

You now have a script that records entries and reads back per-account totals:

- `ledger.summarize()` returns `{account: total}` for every account that has entries, sorted by account name.
- `ledger.summarize(["rent", "groceries"])` returns the same shape for the accounts you name.
- An empty ledger, or a list of names with no entries, gives `{}`.

## Check your work

Running `part2.py` should print three lines, matching the outputs shown above. If a `summarize()` result is missing an account, check the spelling of its name in `add()`: `"Rent"` and `"rent"` are different accounts.

## Where to go next

If you want to see the entries behind a total, `ledger.entries("rent")` returns the entries for one account in the order you added them.
