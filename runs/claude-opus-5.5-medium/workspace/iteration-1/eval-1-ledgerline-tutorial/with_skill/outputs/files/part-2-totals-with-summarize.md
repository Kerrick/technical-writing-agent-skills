# Part 2: Per-account totals with `summarize()`

In [Part 1](part-1.md) we created a `Ledger` and recorded a paycheck and a rent payment. A ledger full of entries is only half the job, though. The question you actually want answered is "how much went where?" In this part we'll answer it twice: first by hand, so you can see exactly what the work involves, and then with `Ledger.summarize()`, which does the same work in one call.

By the end of this part you'll have a script that prints a total for every account, and you'll know how to ask for totals for only some accounts without getting caught by the two mistakes people most often make there.

This part uses ledgerline 2.1.0.

## Where we left off

Part 1 ended with a script that looks like this. If you're arriving from a search, or your copy has drifted, save this as `budget.py` and we'll build on it:

```python
from decimal import Decimal

from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", Decimal("4200.00"), memo="October paycheck")
ledger.add("rent", Decimal("-1500.00"), memo="October rent")
```

Two names here come from different places, which is worth knowing when you search for help:

- `Decimal` comes from Python's standard-library `decimal` module.
- `Ledger` comes from `ledgerline`.

We're recording money coming in as a positive amount and money going out as a negative one. ledgerline doesn't enforce that convention or know which accounts are income and which are expenses; it adds up whatever amounts you give it. Keeping the sign consistent is up to you.

Before going further, confirm which version of ledgerline Python is importing. Run this from the folder that holds `budget.py`:

```
python -c "import ledgerline; print(ledgerline.__version__)"
```

You should see:

```
2.1.0
```

## Step 1: Record another month

Totals aren't very interesting with one entry per account, so let's give the ledger a second month, including two trips to the grocery store. Add these lines to the end of `budget.py`:

```python
ledger.add("groceries", Decimal("-84.20"), memo="Market Street Grocer")
ledger.add("groceries", Decimal("-61.35"), memo="Corner market")
ledger.add("salary", Decimal("4200.00"), memo="November paycheck")
ledger.add("rent", Decimal("-1500.00"), memo="November rent")
```

> **Warning: a bare decimal number raises `TypeError`.**
> It's tempting to write `-84.20` without the `Decimal("...")` wrapper. ledgerline refuses floats, because a float can't hold most cent amounts exactly:
>
> ```python
> # Wrong: -84.20 is a float. This line raises TypeError.
> ledger.add("groceries", -84.20, memo="Market Street Grocer")
> ```
>
> Python stops with a traceback that ends in:
>
> ```
> TypeError: amount must be Decimal, int, or str, not float
> ```
>
> Wrap the amount in `Decimal` and pass it as a string, as in the Step 1 sample. ledgerline also accepts a plain string such as `"-84.20"` or an `int`, but we'll stick with `Decimal` throughout so every amount looks the same.

## Step 2: Total one account by hand

Before we reach for `summarize()`, let's work out a total ourselves. `ledger.entries()` (from Part 1) takes an optional account name and returns only that account's entries, in the order you added them. Each entry has an `amount`, so summing them gives the account's total.

Add this to the end of `budget.py`:

```python
rent_total = sum(entry.amount for entry in ledger.entries("rent"))
print(rent_total)
```

Run the script:

```
python budget.py
```

You should see:

```
-3000.00
```

That's two months of rent at $1,500.00 each, still exact to the cent because every amount is a `Decimal`.

## Step 3: Total every account by hand

One account was easy. Now try all of them. Writing one `sum(...)` line per account works, but you'd have to know every account name in advance, and the day you add an account and forget to add its line, your report silently leaves it out.

Instead, let's walk every entry once and keep a running total per account in a dictionary. Replace the two lines you added in Step 2 with these:

```python
totals = {}
for entry in ledger.entries():
    totals[entry.account] = totals.get(entry.account, Decimal("0")) + entry.amount

print(totals)
```

Calling `ledger.entries()` with no argument returns every entry. For each one we look up the account's total so far, starting from zero the first time we see the account, and add the entry's amount.

Run `python budget.py` again. You should see:

```
{'salary': Decimal('8400.00'), 'rent': Decimal('-3000.00'), 'groceries': Decimal('-145.55')}
```

This is correct, and it picks up new accounts automatically. But look at what it took: an empty dictionary, a loop, a `.get()` with a default, and a starting `Decimal("0")`. The accounts also come out in whatever order they first appeared, so if you print this report every month, the rows can move around. That's a lot of bookkeeping to write again in every script that needs totals.

## Step 4: Let `summarize()` do it

`Ledger.summarize()` does exactly what our Step 3 loop does, and then sorts the result by account name. Add these lines to the end of `budget.py`, keeping the Step 3 loop for now so we can compare the two:

```python
summary = ledger.summarize()
print(summary)
print(summary == totals)
```

Before you run it, make a prediction. The two dictionaries list their accounts in different orders. Will `summary == totals` print `True` or `False`?

Run `python budget.py`. You should see:

```
{'salary': Decimal('8400.00'), 'rent': Decimal('-3000.00'), 'groceries': Decimal('-145.55')}
{'groceries': Decimal('-145.55'), 'rent': Decimal('-3000.00'), 'salary': Decimal('8400.00')}
True
```

The first line is our hand-built `totals`; the second is `summary`, now in alphabetical order. They compare equal because Python's `==` on dictionaries checks keys and values and ignores order.

> **How exact is the equivalence?**
> On a ledger like ours, `ledger.summarize()` returns exactly what this code does:
>
> ```python
> dict(sorted(totals.items()))
> ```
>
> where `totals` is built by the Step 3 loop. When you pass `summarize()` a list of accounts (Step 5), it is equivalent to the same loop with `if entry.account in accounts:` guarding the addition. Like the loop, it never adds an account that has no entries, which is where it differs from the one-account `sum(...)` in Step 2.

Now that `summarize()` has been proven equal, delete the Step 3 loop and the comparison. Your script ends with only the call to `summarize()`:

```python
summary = ledger.summarize()
print(summary)
```

## Step 5: Totals for only some accounts

Sometimes you want only part of the picture, such as just your spending. `summarize()` takes an optional `accounts` argument: a list (or set) of account names to include. Every other account is left out.

Add these lines to the end of `budget.py`:

```python
spending = ledger.summarize(accounts=["groceries", "rent"])
print(spending)
```

Run `python budget.py`. The last line of output is:

```
{'groceries': Decimal('-145.55'), 'rent': Decimal('-3000.00')}
```

Salary is gone, and the remaining accounts are still sorted by name.

### Mistake 1: an account with no entries disappears

In Step 2, `sum(...)` over an account with no entries would give you `0`. `summarize()` behaves differently. Suppose you also want to report on `utilities`, which has no entries yet. Replace the two Step 5 lines with these, which add `utilities` to the list and then look up its total. This sample is meant to fail:

```python
# Wrong: "utilities" has no entries, so it is missing from the result
# and the last line raises KeyError.
spending = ledger.summarize(accounts=["groceries", "rent", "utilities"])
print(spending)
print(spending["utilities"])
```

Run `python budget.py`. The `print(spending)` line shows only two accounts:

```
{'groceries': Decimal('-145.55'), 'rent': Decimal('-3000.00')}
```

Then the next line stops the script with a traceback that ends in:

```
KeyError: 'utilities'
```

`summarize()` leaves out any account with no entries, even one you named in `accounts`. It doesn't report it as zero. An empty ledger gives you an empty dictionary, `{}`.

When you want a zero for an account with no entries, ask for it with `.get()` and a default. Replace the three lines you just added with these:

```python
spending = ledger.summarize(accounts=["groceries", "rent", "utilities"])
print(spending)
print(spending.get("utilities", Decimal("0")))
```

The last two lines of output are now:

```
{'groceries': Decimal('-145.55'), 'rent': Decimal('-3000.00')}
0
```

> **Warning: a misspelled account name returns nothing, without an error.**
> Account names are compared exactly, including case. `ledger.summarize(accounts=["Rent"])` returns `{}`, because there is no account called `Rent`, only `rent`. Nothing tells you about the typo. If a total is missing from a summary, check the spelling of the name you asked for against the account names in `ledger.summarize()`.

### Mistake 2: passing one name as a string

When you want a single account, it's natural to write the name on its own. Add this to the end of `budget.py` and run it:

```python
# Wrong: "rent" is a string, not a list of names. It happens to work here,
# but it can include accounts you didn't ask for.
print(ledger.summarize(accounts="rent"))
```

```
{'rent': Decimal('-3000.00')}
```

That output looks right, which is what makes this mistake easy to miss. `summarize()` keeps an entry when `entry.account in accounts` is true. When `accounts` is a list, `in` checks whether the name is one of the items. When `accounts` is a string, `in` checks whether the name appears *anywhere inside* the string. So `summarize(accounts="car-insurance")` would also include an account named `car`, because `"car" in "car-insurance"` is `True`.

Always wrap a single name in a list:

```python
print(ledger.summarize(accounts=["rent"]))
```

```
{'rent': Decimal('-3000.00')}
```

## Step 6: Print a readable report

The dictionary output is fine for checking our work, but it's not something you'd want to read every month. Because `summarize()` returns its accounts in sorted order, looping over it gives a report whose rows stay in the same place from month to month.

Here is the complete `budget.py` for this part. Replace your file with it:

```python
from decimal import Decimal

from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", Decimal("4200.00"), memo="October paycheck")
ledger.add("rent", Decimal("-1500.00"), memo="October rent")
ledger.add("groceries", Decimal("-84.20"), memo="Market Street Grocer")
ledger.add("groceries", Decimal("-61.35"), memo="Corner market")
ledger.add("salary", Decimal("4200.00"), memo="November paycheck")
ledger.add("rent", Decimal("-1500.00"), memo="November rent")

for account, total in ledger.summarize().items():
    print(f"{account:<12}{total:>10}")
```

The format spec `<12` pads the account name on the right to 12 characters, and `>10` pads the total on the left to 10, so the amounts line up on their decimal points.

Run `python budget.py`. You should see:

```
groceries      -145.55
rent          -3000.00
salary         8400.00
```

Try changing the November rent to `Decimal("-1550.00")` and predict the new `rent` line before you run the script. You should see `-3050.00`, and the `groceries` and `salary` lines should not change.

You should now be comfortable getting per-account totals from a ledger with `summarize()`, for every account or only the ones you name. Continue to Part 3.
