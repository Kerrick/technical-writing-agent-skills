# Part 2: Totals per account with `summarize()`

In [Part 1](part-1.md) we created a `Ledger` and recorded entries for rent and salary. In this part we total those entries by account, first the laborious way and then with `Ledger.summarize()`.

This part is written against ledgerline 2.1.0. To check which version you have, run `python -c "import ledgerline; print(ledgerline.__version__)"`.

By the end you will be able to:

- get the total for every account in a ledger with one call;
- limit the totals to the accounts you name;
- predict which accounts `summarize()` leaves out.

## Where we're starting

Here is the ledger from Part 1. If you still have your Part 1 file, keep it. The amounts below are the ones this part's output uses, so if yours differ, your totals will differ too. Everything we add today goes below these lines.

```python
from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", "3200.00", "March paycheck")
ledger.add("rent", "-1500.00", "March rent")
ledger.add("salary", "3200.00", "April paycheck")
ledger.add("rent", "-1500.00", "April rent")
```

`Ledger` comes from the `ledgerline` module. If you need to look something up later, search for `ledgerline Ledger`.

Each amount is a string, and money coming in is positive while money going out is negative. ledgerline doesn't enforce a sign convention. A total is just the sum of the amounts, so the signs you choose are the signs you get back.

## The laborious way: add them up yourself

How much have we spent on rent so far? `ledger.entries()` gives us every entry, so we can loop over them and keep a running total per account.

```python
totals = {}
for entry in ledger.entries():
    totals[entry.account] = totals.get(entry.account, 0) + entry.amount

print(totals)
```

Each `Entry` has `account`, `amount` and `memo` attributes. The `amount` is a `Decimal`, so adding it to the starting `0` stays exact. Running the file prints:

```text
{'salary': Decimal('6400.00'), 'rent': Decimal('-3000.00')}
```

That works, but look at what we had to do. We wrote a loop, we chose a starting value for accounts we hadn't seen yet, and the accounts come out in whatever order they were first used. We would write the same loop in every script that wants totals. That's the job `summarize()` does for us.

## The shortcut: `summarize()`

`summarize()` is the loop we just wrote, with one difference: it returns the accounts sorted by name. It starts every total at `Decimal("0")`, adds up each account's entries, and returns a dictionary of `{account: total}`.

Before you run it, predict two things. Which account comes first in the result, `salary` or `rent`? And will the totals be the same as the ones from our loop?

```python
print(ledger.summarize())
```

```text
{'rent': Decimal('-3000.00'), 'salary': Decimal('6400.00')}
```

`rent` comes first because the result is sorted alphabetically by account name, not by when you first used each account. The totals match our loop's. Each total is a `Decimal`, which is why the dictionary prints `Decimal('-3000.00')` instead of a bare number.

The two are equivalent for the totals. They differ in order (our loop kept first-use order) and in the starting value (`summarize()` starts from `Decimal("0")`, not the integer `0`, which makes no difference to the totals).

### Printing the totals

The dictionary form is good for code, but readable output needs one more step. Since each total is a `Decimal`, an f-string prints it as a plain number.

```python
for account, total in ledger.summarize().items():
    print(f"{account}: {total}")
```

```text
rent: -3000.00
salary: 6400.00
```

## Limiting the totals to some accounts

Pass `accounts` to get totals for only the accounts you name. Give it a list.

```python
print(ledger.summarize(["rent"]))
```

```text
{'rent': Decimal('-3000.00')}
```

### Accounts with no entries are left out

Now ask for an account we haven't used. What do you expect to get back, a total of `0` or nothing?

```python
print(ledger.summarize(["groceries"]))
```

```text
{}
```

`summarize()` omits accounts with no entries, even when you name them. The empty dictionary means "no entries", and it doesn't raise an error. Code that reads `totals["groceries"]` will raise a `KeyError`, so use `totals.get("groceries", Decimal("0"))` when an account might be missing. `Decimal` comes from Python's standard `decimal` module.

An empty ledger gives the same result: `Ledger().summarize()` returns `{}`.

## Entries must use exact amounts

The totals are exact because every amount is a `Decimal`. That is also why `add()` refuses floats. The next block is meant to fail, so don't paste it into your real file.

```python
# Wrong: a float amount raises TypeError.
ledger.add("groceries", 84.17, "Weekly shop")
```

```text
TypeError: amount must be Decimal, int, or str, not float
```

A float can't hold 84.17 exactly, and that error is raised on purpose so inexact cents never reach your totals. Pass a string instead, as we did for rent and salary:

```python
ledger.add("groceries", "-84.17", "Weekly shop")
print(ledger.summarize())
```

```text
{'groceries': Decimal('-84.17'), 'rent': Decimal('-3000.00'), 'salary': Decimal('6400.00')}
```

`groceries` now appears in the totals because it has an entry, and it sorts first.

## Check your work

Your file should now be the Part 1 setup followed by the `groceries` entry. Run it and confirm that `ledger.summarize()` prints three accounts in the order `groceries`, `rent`, `salary`, with the totals shown above. If you see a `TypeError`, an amount is a float. Quote it as a string.

Try this: add a second `groceries` entry of `"-40.00"` and predict the new groceries total before you run it. It should be `-124.17`.

## What's not covered

`summarize()` totals what's in memory. A `Ledger` lives only as long as your program, and this part doesn't save it anywhere. It also doesn't group by month or filter by memo. Filtering by one account's entries is `ledger.entries("rent")`.

You can now total a ledger by account, and you know which accounts `summarize()` leaves out. Continue to [Part 3](part-3.md).
