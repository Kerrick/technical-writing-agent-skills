# Part 2: Summarizing your ledger

In [Part 1](part-1.md) you created a `Ledger` and added entries for rent and salary. In this part you'll add a few more entries, look at them, and then use `summarize()` to get a total for each account.

This tutorial uses ledgerline 2.1.0. To check your version, run `python -c "import ledgerline; print(ledgerline.__version__)"`.

## Before you start

You need the ledger from Part 1. To make sure everyone starts from the same place, this tutorial rebuilds it. Create a file called `part2.py` and paste this in. If you still have your Part 1 file, you can keep it and skip this step, but your numbers will differ from the ones shown here.

```python
from ledgerline import Ledger

ledger = Ledger()
ledger.add("rent", "-1200.00", "March rent")
ledger.add("salary", "3500.00", "March paycheck")
```

Two things to notice:

- Amounts are passed as strings. `add()` accepts a `Decimal`, an `int`, or a `str`. It raises `TypeError` for a `float`, because floats can't represent cents exactly. Quote your amounts and you won't hit this.
- Money going out is negative and money coming in is positive. ledgerline doesn't enforce this. It's the convention this tutorial uses, so that totals come out meaningful.

## Add more entries

One entry per account isn't much to summarize. Add the following to the end of `part2.py`:

```python
ledger.add("groceries", "-84.50", "Weekly shop")
ledger.add("groceries", "-62.25", "Weekly shop")
ledger.add("rent", "-1200.00", "April rent")
ledger.add("salary", "3500.00", "April paycheck")
```

You now have six entries across three accounts: `rent`, `salary`, and `groceries`.

## Look at the entries for one account

`entries()` returns the entries in the order you added them. Pass an account name to get only that account's entries. Add this to the end of `part2.py`:

```python
for entry in ledger.entries("groceries"):
    print(entry.memo, entry.amount)
```

Run the file with `python part2.py`. You should see:

```text
Weekly shop -84.50
Weekly shop -62.25
```

This is useful, but adding up the amounts by hand for every account would get old quickly. That's what `summarize()` is for.

## Get a total for every account

Replace the loop from the previous step with a call to `summarize()`, or add this below it:

```python
print(ledger.summarize())
```

Run the file again. The last line of output is:

```text
{'groceries': Decimal('-146.75'), 'rent': Decimal('-2400.00'), 'salary': Decimal('7000.00')}
```

`summarize()` returns a dictionary that maps each account name to its total. The totals are `Decimal` values, so they're exact, and the accounts are sorted alphabetically.

Since the result is an ordinary dictionary, you can loop over it to print a tidier report:

```python
for account, total in ledger.summarize().items():
    print(f"{account:<10} {total:>10}")
```

```text
groceries     -146.75
rent         -2400.00
salary        7000.00
```

## Summarize only some accounts

Pass `accounts` to limit the summary to the accounts you name:

```python
print(ledger.summarize(accounts=["rent", "salary"]))
```

```text
{'rent': Decimal('-2400.00'), 'salary': Decimal('7000.00')}
```

Accounts that have no entries are left out, even if you name them. This is easy to trip over: if you ask for `travel` and never added a `travel` entry, it won't appear with a zero total. It just won't be in the result.

```python
print(ledger.summarize(accounts=["rent", "travel"]))
```

```text
{'rent': Decimal('-2400.00')}
```

For the same reason, `summarize()` on an empty ledger returns `{}` rather than raising an error.

## The finished script

Here is everything from this part in one piece. Copy it into a fresh file to check that your version matches.

```python
from ledgerline import Ledger

ledger = Ledger()
ledger.add("rent", "-1200.00", "March rent")
ledger.add("salary", "3500.00", "March paycheck")
ledger.add("groceries", "-84.50", "Weekly shop")
ledger.add("groceries", "-62.25", "Weekly shop")
ledger.add("rent", "-1200.00", "April rent")
ledger.add("salary", "3500.00", "April paycheck")

for entry in ledger.entries("groceries"):
    print(entry.memo, entry.amount)

print(ledger.summarize())

for account, total in ledger.summarize().items():
    print(f"{account:<10} {total:>10}")

print(ledger.summarize(accounts=["rent", "salary"]))
```

## What you learned

- `entries()` lists entries in insertion order, optionally for a single account.
- `summarize()` returns `{account: total}` as `Decimal` values, sorted by account name.
- `summarize(accounts=[...])` restricts the result, and accounts with no entries are omitted.

In Part 3, you'll ...
