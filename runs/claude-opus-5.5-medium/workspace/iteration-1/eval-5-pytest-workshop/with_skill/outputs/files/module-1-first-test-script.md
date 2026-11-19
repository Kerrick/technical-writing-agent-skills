# Module 1 video script: Write and run your first test

Part of [Testing Python services with pytest](index.md). Running time: about 8 minutes.

## Production notes

- **Versions.** Record with Python 3.10 or newer and pytest 9.2.0, the version on the course page.
- **Terminal.** In the terminal blocks, `$` marks the prompt; type what follows it. Lines without `$` are output. Record at 80 columns so the `=====` banners match the blocks.
- **Output.** The terminal blocks leave out pytest's header lines (`platform …`, `rootdir: …`), because those name your machine and path. They'll appear on screen; leave them in the recording. The timings (`in 0.01s`) will differ too.
- **Changed lines.** Lines ending in `# ← changed` are the ones that change in that step. Highlight them in the editor on screen. The comment is for the script only; don't type it.
- **File labels.** A first-line comment that names a file, such as `# test_invoices.py`, is a label for the script; don't type it. The line numbers pytest prints assume it isn't there.
- **Failing samples.** Any sample meant to fail or mislead carries a `# Wrong:` comment on its first line. Do type those comments on screen, so viewers who pause and copy see the warning too.
- **Working folder.** Everything happens in one empty folder named `invoicing`.

---

## 0:00 — Opening

**On screen:** Title card: "Module 1: Write and run your first test." Then an empty editor and terminal, side by side.

**Narration:**

> In the next eight minutes, we'll install pytest, write a test, watch it pass, and then break it on purpose so we can read what pytest tells us. If you've only ever written tests with `unittest`, you'll find most of the ceremony is gone. We'll see exactly what replaces it.
>
> If anything on screen doesn't match what you see, pause the video and flag a facilitator. That's what they're here for.

---

## 0:30 — The code we're testing

**On screen:** Create `invoices.py` in the `invoicing` folder.

```python
# invoices.py
from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def invoice_total(line_items, tax_rate):
    """Return the total due, tax included, rounded to the cent.

    line_items is a list of (unit_price, quantity) pairs.
    unit_price and tax_rate are Decimals; quantity is an int.
    """
    subtotal = sum(
        (unit_price * quantity for unit_price, quantity in line_items),
        Decimal("0"),
    )
    total = subtotal * (1 + tax_rate)
    return total.quantize(CENT, rounding=ROUND_HALF_UP)
```

**Narration:**

> Here's the code we'll test all day: one function from an invoicing service. It takes a list of line items, each one a unit price and a quantity, adds them up, applies tax, and rounds to the cent.
>
> We're using `Decimal` from Python's standard library, not floats, because this is money and floats can't represent most cent amounts exactly. That's also why every price is written as a string, `Decimal("19.99")`: a string gives us exactly 19.99.
>
> One shortcut to be upfront about: this function doesn't validate anything. A negative quantity sails right through. Production code would reject it, and in module 4 we'll test exactly that.

---

## 1:15 — Install pytest

**On screen:** Terminal, in the `invoicing` folder.

```console
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install "pytest==9.2.0"
```

**Narration:**

> First, a virtual environment, so pytest lives with this project and not in your system Python. On macOS and Linux, you activate it with `source`. On Windows, the command is different; the course page links to the Python docs that have it.
>
> Then we install pytest. We're pinning version 9.2.0 so your output matches mine.
>
> If you see "command not found: pytest" in a minute, the usual cause is that the virtual environment isn't active in that terminal. Run the `source` line again. Nearly everyone hits this at least once.

---

## 2:00 — The unittest version you already know

**On screen:** A slide, not a saved file. Show this code:

```python
import unittest
from decimal import Decimal

from invoices import invoice_total


class InvoiceTotalTests(unittest.TestCase):
    def test_invoice_total_adds_tax(self):
        line_items = [(Decimal("19.99"), 2), (Decimal("5.00"), 1)]
        self.assertEqual(
            invoice_total(line_items, tax_rate=Decimal("0.08")),
            Decimal("48.58"),
        )
```

**Narration:**

> If you've used `unittest`, this is familiar. Import the module, write a class that inherits from `TestCase`, write a method, and call `self.assertEqual`. It works. But look at how much of it is there to satisfy the framework: the class, the `self`, and remembering which of the `assert` methods you want.
>
> Two line items: two at 19.99 and one at 5.00. That's 44.98, plus 8% tax, so 48.58.
>
> Let's write the same test the pytest way.

---

## 2:30 — Write the first pytest test

**On screen:** Create `test_invoices.py` next to `invoices.py`.

```python
# test_invoices.py
from decimal import Decimal

from invoices import invoice_total


def test_invoice_total_adds_tax():
    line_items = [(Decimal("19.99"), 2), (Decimal("5.00"), 1)]
    total = invoice_total(line_items, tax_rate=Decimal("0.08"))
    expected = Decimal("48.58")
    assert total == expected
```

**Narration:**

> No class, and no import from pytest at all. A pytest test is a plain function whose name starts with `test`, in a file whose name starts with `test_`. Inside, we use Python's own `assert` statement, the one built into the language. If the expression is true, the test passes. If it's false, the test fails.
>
> `Decimal` comes from the standard library's `decimal` module, and `invoice_total` comes from our `invoices.py`. Nothing here is pytest-specific yet. That's the point.
>
> Now we run it.

**On screen:**

```console
$ pytest
============================= test session starts ==============================
collected 1 item

test_invoices.py .                                                       [100%]

============================== 1 passed in 0.01s ===============================
```

**Narration:**

> We just typed `pytest`, with no arguments. pytest searched this folder for files named `test_` something, found ours, and collected one test. Each dot after the file name is one passing test. One dot, one passed. That's our first green test.

---

## 3:45 — Break it on purpose

**On screen:** Change the tax rate in the test from `0.08` to `0.10`. Leave the expected value alone.

```python
# test_invoices.py
from decimal import Decimal

from invoices import invoice_total


def test_invoice_total_adds_tax():
    # Wrong: tax rate changed without updating the expected total; this test fails on purpose
    line_items = [(Decimal("19.99"), 2), (Decimal("5.00"), 1)]
    total = invoice_total(line_items, tax_rate=Decimal("0.10"))  # ← changed
    expected = Decimal("48.58")
    assert total == expected
```

**Narration:**

> A test that has never failed hasn't proven much, so let's make this one fail. I'm changing the tax rate to 10% and leaving the expected total at 48.58.
>
> Before I run it, pause the video and make a prediction. With `unittest`, `assertEqual` tells you both values. But we used a plain `assert`, and normally a failed `assert` in Python just says `AssertionError` and nothing else. So what do you think pytest will print?

**On screen:** Hold for three seconds, then run:

```console
$ pytest
============================= test session starts ==============================
collected 1 item

test_invoices.py F                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_invoice_total_adds_tax __________________________

    def test_invoice_total_adds_tax():
        # Wrong: tax rate changed without updating the expected total; this test fails on purpose
        line_items = [(Decimal("19.99"), 2), (Decimal("5.00"), 1)]
        total = invoice_total(line_items, tax_rate=Decimal("0.10"))
        expected = Decimal("48.58")
>       assert total == expected
E       AssertionError: assert Decimal('49.48') == Decimal('48.58')

test_invoices.py:11: AssertionError
=========================== short test summary info ============================
FAILED test_invoices.py::test_invoice_total_adds_tax - AssertionError: assert Decimal('49.48') == Decimal('48.58')
============================== 1 failed in 0.03s ===============================
```

**Narration:**

> Let's read this from the top. Where the dot was, there's now an `F`, for failed.
>
> Under `FAILURES`, pytest prints the test's source. The arrow marks the line that failed. And the line starting with `E` shows the comparison with the real values filled in: we got 49.48, and we expected 48.58. pytest rewrites your `assert` statements as it loads test files, so that it can show you those values. That's why a plain `assert` is enough, and why you don't need a family of `assertEqual`-style methods.
>
> Below that is the file and line number, and at the very bottom, a one-line summary per failing test. When a suite has fifty failures, that summary is where you start.
>
> Put the tax rate back to `0.08`, delete the `Wrong` comment, and run `pytest` again. You should be back to one dot and `1 passed`.

---

## 5:15 — The test that never runs

**On screen:** Add a second function to the end of `test_invoices.py`. Show the anchored excerpt:

```python
# test_invoices.py, after test_invoice_total_adds_tax
def check_empty_invoice_is_zero():
    # Wrong: the name doesn't start with "test", so pytest never runs this function
    total = invoice_total([], tax_rate=Decimal("0.08"))
    assert total == Decimal("1.00")
```

**Narration:**

> Now a trap that catches almost everyone. I'm adding a second test, for an empty invoice. I've called it `check_empty_invoice_is_zero`. And I've written the expected value as `1.00`, which is wrong: an empty invoice should total zero.
>
> So this test should fail. Prediction time again: how many dots will we see?

**On screen:**

```console
$ pytest
============================= test session starts ==============================
collected 1 item

test_invoices.py .                                                       [100%]

============================== 1 passed in 0.01s ===============================
```

**Narration:**

> One dot. `1 passed`. Everything's green, and our broken test never ran. pytest only collects functions whose names start with `test`, so `check_empty_invoice_is_zero` is just an ordinary function that nobody calls. No error, no warning.
>
> This is the dangerous kind of mistake: it doesn't fail, it just quietly tests less than you think. The habit that protects you is to glance at the `collected` count every time. We wrote two tests, and pytest collected one.
>
> Let's fix both problems: rename it so it starts with `test`, and correct the expected value.

**On screen:**

```python
# test_invoices.py, after test_invoice_total_adds_tax
def test_empty_invoice_is_zero():  # ← changed
    total = invoice_total([], tax_rate=Decimal("0.08"))
    assert total == Decimal("0.00")  # ← changed
```

```console
$ pytest
============================= test session starts ==============================
collected 2 items

test_invoices.py ..                                                      [100%]

============================== 2 passed in 0.01s ===============================
```

**Narration:**

> Two collected, two dots, two passed. Now the count matches what we wrote.

---

## 6:30 — Your unittest tests still run

**On screen:** Save the `unittest` version from the 2:00 slide as `test_invoices_unittest.py` in the same folder. Run with `-v`.

```console
$ pytest -v
============================= test session starts ==============================
collected 3 items

test_invoices.py::test_invoice_total_adds_tax PASSED                     [ 33%]
test_invoices.py::test_empty_invoice_is_zero PASSED                      [ 66%]
test_invoices_unittest.py::InvoiceTotalTests::test_invoice_total_adds_tax PASSED [100%]

============================== 3 passed in 0.01s ===============================
```

**Narration:**

> One more thing for those of you with an existing `unittest` suite. I've saved that `unittest` version from earlier as its own file. Running `pytest` with `-v`, for verbose, prints each test by name instead of as a dot. And there it is: pytest found and ran the `TestCase` class alongside our plain functions.
>
> So you don't have to rewrite your suite before you switch. You can start running your existing tests with pytest today, and write new tests the pytest way as you go.

---

## 7:15 — Closing

**On screen:** The complete `test_invoices.py` as a checkpoint. Then the closing card.

```python
# test_invoices.py: checkpoint at the end of module 1
from decimal import Decimal

from invoices import invoice_total


def test_invoice_total_adds_tax():
    line_items = [(Decimal("19.99"), 2), (Decimal("5.00"), 1)]
    total = invoice_total(line_items, tax_rate=Decimal("0.08"))
    expected = Decimal("48.58")
    assert total == expected


def test_empty_invoice_is_zero():
    total = invoice_total([], tax_rate=Decimal("0.08"))
    assert total == Decimal("0.00")
```

**Narration:**

> Here's the whole test file as it should look now. If yours has drifted, match it to this one. `pytest` should report `2 passed` for this file.
>
> One more shortcut to name: we've put our tests in the same folder as the code. That's fine for one module. A real service keeps tests in their own directory, and we'll set that up in module 6.
>
> Your exercise: add a test for an invoice with zero tax. Before you run it, work out the total you expect and write it in the test. You should see three dots from `test_invoices.py`. If you see fewer, check the function name first.
>
> You should now be comfortable writing a test as a plain function, running it with `pytest`, and reading a failure. Next, in module 2, we'll notice how much setup our tests are starting to repeat, and fix it with fixtures.

**On screen:** Closing card: "Next: Module 2 — Fixtures: shared setup without `setUp`."
