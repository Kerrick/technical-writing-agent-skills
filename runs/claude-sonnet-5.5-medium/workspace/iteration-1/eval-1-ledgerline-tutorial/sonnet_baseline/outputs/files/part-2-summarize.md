# Part 2: Get per-account totals with `summarize()`

In Part 1 you created a `Ledger` and added entries for rent and salary. In this part you add more entries and use `summarize()` to get one total for each account. It takes about 15 minutes.

By the end, you will have a script that prints this:

```text
groceries: -107.60
rent: -2400.00
salary: 7000.00
```

This part is written for ledgerline 2.1.0, and you need Python 3 installed (the code was run on Python 3.15). You need `ledgerline.py` (the library file) in the same folder as the script you write here.

## Start a fresh script

Part 1 left you with a ledger that held a few entries. So that your numbers match the ones in this tutorial, you rebuild the ledger in a new file.

1. In the folder that contains `ledgerline.py`, create a file named `part2.py`.
2. Paste this into `part2.py` and save it:

   ```python
   from ledgerline import Ledger

   ledger = Ledger()
   ledger.add("rent", "-1200.00", "March rent")
   ledger.add("salary", "3500.00", "March paycheck")
   ```

Each call to `add()` records one **entry**: an account name, an amount, and an optional memo. In this tutorial, money you spend is negative and money you earn is positive. ledgerline does not enforce this; it is a convention we use so that totals are meaningful.

The amounts are strings, such as `"-1200.00"`, because ledgerline stores amounts as `Decimal` values, which are exact. `add()` accepts a `Decimal`, an `int`, or a `str`. You will see what it does with a `float` later in this part.

## Add more entries

A total is only interesting when an account has more than one entry. Add the next month's rent and paycheck, plus two grocery purchases.

1. Add these lines to the end of `part2.py` and save it:

   ```python
   ledger.add("groceries", "-84.50", "Market")
   ledger.add("groceries", "-23.10", "Corner store")
   ledger.add("rent", "-1200.00", "April rent")
   ledger.add("salary", "3500.00", "April paycheck")
   ```

The ledger now holds six entries across three accounts: `groceries`, `rent`, and `salary`.

## Print the totals

`summarize()` adds up the entries in each account and returns the results as a dictionary. The keys are account names and the values are the totals.

1. Add this line to the end of `part2.py`:

   ```python
   print(ledger.summarize())
   ```

2. In a terminal, in the same folder, run the script:

   ```bash
   python part2.py
   ```

   If your system uses `python3` as the command name, run `python3 part2.py` instead.

You should see one line:

```text
{'groceries': Decimal('-107.60'), 'rent': Decimal('-2400.00'), 'salary': Decimal('7000.00')}
```

Rent is `-1200.00` twice, so `-2400.00`. Groceries are `-84.50` and `-23.10`, so `-107.60`. The accounts appear in alphabetical order, whatever order you added them in.

**If you get `ModuleNotFoundError: No module named 'ledgerline'`:** Python cannot find the library. Make sure `ledgerline.py` is in the folder where you ran the command.

## Print the totals as a readable report

The `Decimal('...')` wrappers are noise when you read the output. The dictionary behaves like any other, so loop over it with `.items()` and format each line.

1. Add this loop to the end of `part2.py`:

   ```python
   for account, total in ledger.summarize().items():
       print(f"{account}: {total}")
   ```

2. Run the script again:

   ```bash
   python part2.py
   ```

The first line is the same as before. The three lines after it are new:

```text
groceries: -107.60
rent: -2400.00
salary: 7000.00
```

Printing a `Decimal` with `f"{total}"` shows the number without the wrapper, and keeps both decimal places.

## Total only some accounts

You can pass `summarize()` a list of account names to get totals for just those accounts.

1. Add this line to the end of `part2.py`:

   ```python
   print(ledger.summarize(["groceries", "rent"]))
   ```

2. Run the script again.

The last line of output is new:

```text
{'groceries': Decimal('-107.60'), 'rent': Decimal('-2400.00')}
```

`salary` is missing because you did not ask for it.

### Predict: what happens for an account with no entries?

You have no `savings` account. Before you run anything, decide what you think this returns:

```python
print(ledger.summarize(["savings"]))
```

Add that line to the end of `part2.py` and run the script to check your guess.

You might expect `{'savings': Decimal('0')}`. The last line of output is actually this:

```text
{}
```

`summarize()` leaves out accounts that have no entries, even when you name them. An account whose entries cancel out still appears, with a total of zero, but a name with no entries does not. If your code looks up a total by name, use `totals.get("savings", 0)` rather than `totals["savings"]`, which raises `KeyError`.

## See the entries behind a total

When a total looks wrong, list the entries that make it up. `entries()` returns them in the order you added them, and takes an optional account name.

1. Add this line to the end of `part2.py`:

   ```python
   print(ledger.entries("groceries"))
   ```

2. Run the script again.

The last line of output is new:

```text
[Entry(account='groceries', amount=Decimal('-84.50'), memo='Market'), Entry(account='groceries', amount=Decimal('-23.10'), memo='Corner store')]
```

The two amounts add up to the `-107.60` that `summarize()` reported.

## Read an error: floats are rejected

Money values written as floats, such as `12.5`, cannot always represent cents exactly, so `add()` refuses them. Trigger the error on purpose, so you recognize it later.

1. Add this line to the end of `part2.py`:

   ```python
   ledger.add("groceries", 12.5, "Bakery")
   ```

2. Run the script again.

All the earlier output prints first, then the script stops with a traceback. The last line names the problem:

```text
TypeError: amount must be Decimal, int, or str, not float
```

Read a traceback from the bottom. The last line says what went wrong. The lines above it say where: the line in `part2.py` that you wrote, then the line inside `ledgerline.py` that raised the error.

To fix it, pass the amount as a string, `"12.50"`, or as a `Decimal`.

1. Replace the line you just added with this one:

   ```python
   ledger.add("groceries", "12.50", "Bakery")
   ```

2. Run the script again. It finishes without an error.

Because this entry is added after the `print()` calls, it does not change any output you have seen. It would change the groceries total if you called `summarize()` again.

## Check your work

Your finished `part2.py` is:

```python
from ledgerline import Ledger

ledger = Ledger()
ledger.add("rent", "-1200.00", "March rent")
ledger.add("salary", "3500.00", "March paycheck")
ledger.add("groceries", "-84.50", "Market")
ledger.add("groceries", "-23.10", "Corner store")
ledger.add("rent", "-1200.00", "April rent")
ledger.add("salary", "3500.00", "April paycheck")

print(ledger.summarize())
for account, total in ledger.summarize().items():
    print(f"{account}: {total}")
print(ledger.summarize(["groceries", "rent"]))
print(ledger.summarize(["savings"]))
print(ledger.entries("groceries"))
ledger.add("groceries", "12.50", "Bakery")
```

It prints:

```text
{'groceries': Decimal('-107.60'), 'rent': Decimal('-2400.00'), 'salary': Decimal('7000.00')}
groceries: -107.60
rent: -2400.00
salary: 7000.00
{'groceries': Decimal('-107.60'), 'rent': Decimal('-2400.00')}
{}
[Entry(account='groceries', amount=Decimal('-84.50'), memo='Market'), Entry(account='groceries', amount=Decimal('-23.10'), memo='Corner store')]
```

## Exercise

Add a `"salary"` entry of `"250.00"` with the memo `"Bonus"`, then print only the salary total. Use `summarize()` with a list that names one account.

<details>
<summary>Solution</summary>

```python
ledger.add("salary", "250.00", "Bonus")
print(ledger.summarize(["salary"]))
```

The output is `{'salary': Decimal('7250.00')}`. A common mistake is to pass a bare string, `summarize("salary")`. Python then checks whether each account name is a substring of `"salary"`, so it can match accounts you did not mean to include (an account named `"sal"` would match).

</details>

## What you built

You added entries across three accounts, used `summarize()` to total them, narrowed the result to chosen accounts, and traced a total back to its entries with `entries()`. You also met the two behaviors that surprise people: accounts with no entries are left out, and floats are rejected.

## Next steps

- The `Ledger` docstrings in `ledgerline.py` describe `add()`, `entries()`, and `summarize()` in full.
