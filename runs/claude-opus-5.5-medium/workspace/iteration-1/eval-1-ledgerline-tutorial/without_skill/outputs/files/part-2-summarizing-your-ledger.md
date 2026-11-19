# Part 2: Summarizing your ledger

In [Part 1](part-1.md), you created a `Ledger` and recorded a few entries for rent and salary. A list of entries is useful, but most of the time you want a simpler answer: *how much is in each account?*

In this part, you'll add a few more entries and then use `summarize()` to get a total for each account.

By the end, you'll be able to:

- Get the total for every account with `summarize()`
- Narrow the summary to just the accounts you care about
- Print the totals as a readable report

This tutorial uses ledgerline 2.1.0.

## Step 1: Set up your ledger

Create a file called `budget.py` and add the code below. It's the ledger from Part 1, plus a second month and a new `groceries` account so there's more to add up.

```python
from ledgerline import Ledger

ledger = Ledger()

# March
ledger.add("rent", "-1500.00", memo="March rent")
ledger.add("salary", "4200.00", memo="March paycheck")
ledger.add("groceries", "-86.40", memo="Market run")

# April
ledger.add("groceries", "-123.15", memo="Weekly shop")
ledger.add("salary", "4200.00", memo="April paycheck")
ledger.add("rent", "-1500.00", memo="April rent")
```

As in Part 1, money going out is negative and money coming in is positive. The amounts are strings, not floats. ledgerline converts them to `Decimal` so cents stay exact. If you pass a float such as `4.50`, `add()` raises a `TypeError`.

## Step 2: Get the total for each account

Add this line to the end of `budget.py`:

```python
print(ledger.summarize())
```

Run the script:

```bash
python budget.py
```

You should see:

```text
{'groceries': Decimal('-209.55'), 'rent': Decimal('-3000.00'), 'salary': Decimal('8400.00')}
```

`summarize()` returns a dictionary that maps each account name to the sum of its entries. Two things to notice:

- **The accounts are sorted by name**, not in the order you added them. `groceries` comes first even though you added `rent` first.
- **The totals are `Decimal` values.** That's why they print as `Decimal('-209.55')`. You can do math with them just like numbers.

## Step 3: Print a readable report

The raw dictionary is fine for checking your work, but you'll usually want something easier to read. Because `summarize()` returns an ordinary dictionary, you can loop over it.

Replace the `print(ledger.summarize())` line with:

```python
totals = ledger.summarize()

for account, total in totals.items():
    print(f"{account:<10} {total:>10}")
```

Run the script again. You should see:

```text
groceries     -209.55
rent         -3000.00
salary        8400.00
```

Formatting a `Decimal` with an f-string prints the number itself, without the `Decimal(...)` wrapper.

Since the totals are numbers, you can also add them up to get your net balance. Add this to the end of the file:

```python
print(f"{'net':<10} {sum(totals.values()):>10}")
```

Your report now ends with:

```text
net           5190.45
```

## Step 4: Summarize only some accounts

Sometimes you only care about a few accounts, like your fixed monthly costs and your income. Pass a list of account names to the `accounts` argument:

```python
print(ledger.summarize(accounts=["rent", "salary"]))
```

Output:

```text
{'rent': Decimal('-3000.00'), 'salary': Decimal('8400.00')}
```

`groceries` is left out because you didn't ask for it.

> **Warning:** Always pass a list, even for one account. Write `accounts=["rent"]`, not `accounts="rent"`. A plain string may seem to work, but ledgerline checks each entry with Python's `in` operator. For a string, `in` matches substrings, so an account named `"ent"` would also be included.

### Accounts with no entries are left out

If you ask for an account that has no entries, it isn't in the result. It won't show up with a total of zero:

```python
print(ledger.summarize(accounts=["rent", "utilities"]))
```

Output:

```text
{'rent': Decimal('-3000.00')}
```

The same rule covers an empty ledger: calling `summarize()` on a `Ledger` with no entries returns `{}`.

If your code needs every account you asked for to be present, use `.get()` with a default:

```python
from decimal import Decimal

totals = ledger.summarize(accounts=["rent", "utilities"])
print(totals.get("utilities", Decimal("0")))
```

Output:

```text
0
```

## The complete script

Here's the finished `budget.py`:

```python
from ledgerline import Ledger

ledger = Ledger()

# March
ledger.add("rent", "-1500.00", memo="March rent")
ledger.add("salary", "4200.00", memo="March paycheck")
ledger.add("groceries", "-86.40", memo="Market run")

# April
ledger.add("groceries", "-123.15", memo="Weekly shop")
ledger.add("salary", "4200.00", memo="April paycheck")
ledger.add("rent", "-1500.00", memo="April rent")

totals = ledger.summarize()

for account, total in totals.items():
    print(f"{account:<10} {total:>10}")

print(f"{'net':<10} {sum(totals.values()):>10}")
```

Running it prints:

```text
groceries     -209.55
rent         -3000.00
salary        8400.00
net           5190.45
```

## Recap

In this part, you learned that:

- `ledger.summarize()` returns a `{account: total}` dictionary, sorted by account name.
- Totals are `Decimal` values, so they stay exact and work with ordinary math like `sum()`.
- `summarize(accounts=[...])` limits the result to the accounts you name. Always pass a list.
- Accounts with no entries are left out of the result, so use `.get()` with a default when you need a value for every account.
