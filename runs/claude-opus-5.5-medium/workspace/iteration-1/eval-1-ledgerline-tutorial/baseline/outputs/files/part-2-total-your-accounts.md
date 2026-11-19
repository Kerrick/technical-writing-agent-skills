<!--
Reader: a Python developer new to ledgerline, working through the tutorial
in order, who finished Part 1 (created a Ledger, added rent and salary
entries). Some arrive from search, so the page restates its starting code.
Documented against ledgerline 2.1.0.
-->

# Part 2: Total your accounts with `summarize()`

In Part 1 you recorded rent and salary in a ledger. In this part you add two months of entries and get one total per account in a single call:

```text
groceries    -128.45
rent        -2900.00
salary       6400.00
```

## Before you begin

- You finished [Part 1: Create a ledger](TODO(verify): link to Part 1), or you're comfortable creating a `Ledger` and calling `add()`.
- You have ledgerline 2.1.0 installed. To check, run this command:

  ```shell
  python3 -c "import ledgerline; print(ledgerline.__version__)"
  ```

  The output is:

  ```text
  2.1.0
  ```

- About 15 minutes.

## Start from the Part 1 ledger

You build up one file, `budget.py`, through this whole page. Every step adds code to the end of it.

1. Open `budget.py` from Part 1. If you don't have it, create `budget.py` and paste in this code:

   ```python
   from ledgerline import Ledger

   ledger = Ledger()
   ledger.add("salary", "3200.00", memo="November paycheck")
   ledger.add("rent", "-1450.00", memo="November rent")
   ```

   Money coming in is positive, and money going out is negative. Amounts are strings so that ledgerline stores the exact cents.

2. Run the file:

   ```shell
   python3 budget.py
   ```

   It prints nothing yet. That's expected: the script only records entries.

## Get a total for every account

A ledger with one entry per account doesn't need totals. Add a second month, and then ask for the totals.

1. Add these lines to the end of `budget.py`:

   ```python
   ledger.add("groceries", "-82.15", memo="Farmers market")
   ledger.add("groceries", "-46.30", memo="Corner store")
   ledger.add("salary", "3200.00", memo="December paycheck")
   ledger.add("rent", "-1450.00", memo="December rent")

   totals = ledger.summarize()
   print(totals)
   ```

2. Run the file:

   ```shell
   python3 budget.py
   ```

   The output is:

   ```text
   {'groceries': Decimal('-128.45'), 'rent': Decimal('-2900.00'), 'salary': Decimal('6400.00')}
   ```

`summarize()` returns a dictionary with one key per account. Each value is that account's entries added together. Three details are worth noticing:

- **The values are `Decimal`s.** ledgerline converts every amount to Python's [`Decimal`](https://docs.python.org/3/library/decimal.html) type when you add it, so `-82.15 + -46.30` comes out as exactly `-128.45`, with no rounding error.
- **The keys are sorted by account name**, not by the order you added entries. `groceries` comes first even though you added `salary` first.
- **Each account appears once**, however many entries it has.

If you see `TypeError: amount must be Decimal, int, or str, not float`, one of your amounts is written as a number with a decimal point, like `-82.15`. Put quotes around it: `"-82.15"`.

## Print the totals as a table

The dictionary is what your code works with. For people, print one account per line.

1. Add these lines to the end of `budget.py`:

   ```python
   print()
   for account, total in totals.items():
       print(f"{account:<10} {total:>9}")
   ```

   `:<10` pads the account name to 10 characters, and `:>9` right-aligns the total in 9 characters, so the decimal points line up.

2. Run the file:

   ```shell
   python3 budget.py
   ```

   The output now ends with the table:

   ```text
   ...

   groceries    -128.45
   rent        -2900.00
   salary       6400.00
   ```

Because `summarize()` already sorts by account name, the table comes out in alphabetical order without any extra work.

## Check a total against its entries

Before you trust a total, check one by hand. In Part 1 you used `entries()` to list one account's entries. Use it again to add up the rent yourself.

1. Add these lines to the end of `budget.py`:

   ```python
   rent_entries = ledger.entries("rent")
   print()
   print(len(rent_entries), "rent entries")
   print(sum(entry.amount for entry in rent_entries))
   ```

2. Run the file:

   ```shell
   python3 budget.py
   ```

   The output now ends with:

   ```text
   ...

   2 rent entries
   -2900.00
   ```

`-2900.00` matches the `rent` total from `summarize()`. A total is the same sum you just computed, done for every account at once.

## Total only the accounts you ask for

To see what you spent, leave `salary` out. Pass the account names you want as `accounts`.

1. Add these lines to the end of `budget.py`:

   ```python
   spending = ledger.summarize(accounts=["rent", "groceries", "utilities"])
   print()
   print(spending)
   print(spending.get("utilities", 0))
   ```

2. Run the file:

   ```shell
   python3 budget.py
   ```

   The output now ends with:

   ```text
   ...

   {'groceries': Decimal('-128.45'), 'rent': Decimal('-2900.00')}
   0
   ```

`salary` is gone, as you asked. But `utilities` is missing too, even though you named it. **`summarize()` leaves out any account that has no entries**, including accounts you list in `accounts`. Asking for `spending["utilities"]` would raise a `KeyError`.

When an account might have no entries yet, read it with `.get()` and a default, as the last line does: `spending.get("utilities", 0)` returns `0` instead of raising an error.

Pass `accounts` as a list, even for one account: `accounts=["rent"]`, not `accounts="rent"`.

## Try it: predict the output

Your electric bill arrives. Add these lines to the end of `budget.py`. They record the bill and print the spending totals again:

```python
ledger.add("utilities", "-64.20", memo="Electric bill")
print()
print(ledger.summarize(accounts=["rent", "groceries", "utilities"]))
```

Before you run the file, write down what you expect the last line of output to be. Which keys appear, and in what order?

Then run it:

```shell
python3 budget.py
```

<details>
<summary>Show the answer</summary>

```text
{'groceries': Decimal('-128.45'), 'rent': Decimal('-2900.00'), 'utilities': Decimal('-64.20')}
```

`utilities` now has an entry, so it appears. It comes last because the keys are sorted by name, not by the order you listed them in `accounts`. The earlier `spending` dictionary hasn't changed: `summarize()` returns a new dictionary each time you call it, from the entries in the ledger at that moment.

</details>

## Your finished `budget.py`

If something doesn't match, compare your file with this one:

```python
from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", "3200.00", memo="November paycheck")
ledger.add("rent", "-1450.00", memo="November rent")

ledger.add("groceries", "-82.15", memo="Farmers market")
ledger.add("groceries", "-46.30", memo="Corner store")
ledger.add("salary", "3200.00", memo="December paycheck")
ledger.add("rent", "-1450.00", memo="December rent")

totals = ledger.summarize()
print(totals)

print()
for account, total in totals.items():
    print(f"{account:<10} {total:>9}")

rent_entries = ledger.entries("rent")
print()
print(len(rent_entries), "rent entries")
print(sum(entry.amount for entry in rent_entries))

spending = ledger.summarize(accounts=["rent", "groceries", "utilities"])
print()
print(spending)
print(spending.get("utilities", 0))

ledger.add("utilities", "-64.20", memo="Electric bill")
print()
print(ledger.summarize(accounts=["rent", "groceries", "utilities"]))
```

## What you learned

- Get one total per account with `ledger.summarize()`.
- Read the result as a dictionary of `Decimal` totals, sorted by account name.
- Print the totals as an aligned table.
- Check a total against the account's entries with `entries()`.
- Total only selected accounts with `summarize(accounts=[...])`, and read accounts that might have no entries with `.get()`.

## Next steps

- TODO(verify): link to Part 3 once it exists.
- TODO(verify): link to the `Ledger.summarize()` API reference, if the docs have one.
