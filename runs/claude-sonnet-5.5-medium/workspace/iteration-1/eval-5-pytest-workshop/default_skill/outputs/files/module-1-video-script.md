# Module 1: Your first test (video script)

Running time: about 8 minutes. Narration is in plain text. Lines in *italics* are on-screen actions. Code blocks show exactly what appears in the editor or terminal.

Part of [Testing Python services with pytest](index.md). This is the first module, so it relies on nothing earlier. It uses the invoicing service that every later module builds on.

## 0:00 Cold open: what we'll do

*Screen: an empty folder named `invoicing` open in the editor, with a terminal beside it.*

Welcome to the workshop. In the next eight minutes we'll write one test, run it, break it on purpose, and read what pytest tells us when a test fails.

If you've used `unittest`, you'll recognize the shape of all this. If you've never written a test, that's fine too. We'll go one step at a time.

## 0:30 Setup

*Screen: terminal.*

First, a virtual environment with pytest in it. Run these three commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```

On Windows, activate with `.venv\Scripts\activate` instead. Then check that it worked:

```bash
pytest --version
```

You should see a version line that starts with `pytest`. If you see "command not found", the environment isn't active. Pause the video and fix that now; everything after this depends on it. If you're stuck, put your hand up and the instructor will come to you.

## 1:15 The code we're testing

*Screen: create `invoices.py`.*

Here's the function we'll test. It's the heart of a small invoicing service. It takes a list of line items and a tax rate, and returns the total, rounded to cents. We use `Decimal` for money, because floats can't represent amounts like ten cents exactly.

```python
# invoices.py
from decimal import ROUND_HALF_UP, Decimal


def invoice_total(line_items, tax_rate):
    """Return the invoice total with tax, rounded to cents."""
    subtotal = sum(
        (item["unit_price"] * item["quantity"] for item in line_items),
        start=Decimal("0"),
    )
    return (subtotal * (1 + tax_rate)).quantize(Decimal("0.01"), ROUND_HALF_UP)
```

Don't worry about every line. We're testing this function, not studying it.

## 2:00 The first test

*Screen: create `test_invoices.py` next to `invoices.py`.*

Before we write the pytest version, here's the `unittest` version, so you can see what pytest takes away.

```python
# The unittest form, for comparison. We won't keep this file.
import unittest
from decimal import Decimal

from invoices import invoice_total


class InvoiceTotalTests(unittest.TestCase):
    def test_invoice_total_adds_tax_to_the_subtotal(self):
        line_items = [
            {"unit_price": Decimal("10.00"), "quantity": 2},
            {"unit_price": Decimal("5.00"), "quantity": 1},
        ]

        total = invoice_total(line_items, tax_rate=Decimal("0.10"))

        self.assertEqual(total, Decimal("27.50"))
```

A class, a base class to inherit, and `self.assertEqual`. Now the pytest version. Type this into `test_invoices.py`:

```python
# test_invoices.py
from decimal import Decimal

from invoices import invoice_total


def test_invoice_total_adds_tax_to_the_subtotal():
    line_items = [
        {"unit_price": Decimal("10.00"), "quantity": 2},
        {"unit_price": Decimal("5.00"), "quantity": 1},
    ]

    total = invoice_total(line_items, tax_rate=Decimal("0.10"))

    assert total == Decimal("27.50")
```

No class. No base class. A plain function, and a plain `assert` statement. Every name here comes from somewhere you already know: `assert` is built into Python, and `invoice_total` and `Decimal` are imported at the top of the file. Nothing is imported from pytest. The only pytest-specific part is the file and function names, and we'll come back to that in a minute.

The test follows a pattern worth copying: set up the input, call the code, then check one result. Two items at ten dollars times two, plus five dollars, make twenty-five. Add ten percent tax and we expect twenty-seven fifty.

## 3:30 Run it

*Screen: terminal, in the folder that holds both files.*

Run `pytest` with no arguments.

Before you press enter, predict: what will you see? Pause here and decide. One test, and we believe the code is right.

```bash
pytest
```

You'll see a header with your Python and pytest versions, a line saying `collected 1 item`, and then `test_invoices.py .` followed by `1 passed`. The dot is one passing test. Add `-v` for the verbose form, which prints the test's name.

```bash
pytest -v
```

How did pytest find our test without being told? It searched the current folder for files named `test_*.py` or `*_test.py`, and in them ran functions whose names start with `test`. That's called collection, and it's the rule for everything in this workshop.

## 4:30 A test that doesn't run

*Screen: rename the function in the editor.*

That rule has a trap, and it fails silently. Rename the function so it no longer starts with `test`:

```python
# Wrong: pytest only collects functions whose names start with "test".
def check_invoice_total_adds_tax_to_the_subtotal():
    ...  # the body stays exactly as it was
```

Run `pytest` again. You'll see `collected 0 items` and `no tests ran`. There's no error and nothing red. If your test never seems to run, check the name first. Rename it back before we continue.

The file name matters the same way. A correctly named function in a file called `invoices_tests.py` isn't collected either, because the file doesn't match `test_*.py` or `*_test.py`.

## 5:30 Break it on purpose

*Screen: change the expected value in the last line.*

Now the part that matters most in daily work: reading a failure. We'll make one. Change the expected total to the wrong number:

```python
    assert total == Decimal("25.00")  # Wrong on purpose: tax makes the real total 27.50
```

This test is meant to fail. Run `pytest`.

```bash
pytest
```

Look at the report. A line starting with `>` marks the exact statement that failed, and lines starting with `E` explain why:

```text
>       assert total == Decimal("25.00")
E       assert Decimal('27.50') == Decimal('25.00')
```

pytest rewrote our plain `assert` so it can show both values, which is why we didn't need `assertEqual`. Read it left to right: the actual value came first, and the expected value second. The last line of the output says `1 failed`.

Read the report in this order: first the `>` line to find where, then the `E` lines to find what. If you're new to this, that reading may feel slow. That's normal. It speeds up after a handful of failures.

Change the value back to `27.50` and run again to see it pass.

## 7:00 What we left out

*Screen: the passing test.*

We took two shortcuts, and you should know them. We tested one invoice, and one invoice isn't enough: real tests would also cover an empty list, a zero tax rate, and amounts that need rounding. Module 3 does that without copying the test. We also typed the line items inside the test. Once several tests need them, you'd move that setup into a fixture, which is what Module 2 is about.

## 7:30 Close

You can now write a plain-`assert` test, run it with `pytest`, and read a failure. Next, in Module 2, we'll see what happens when five tests all need the same line items, and fix it with a fixture.
