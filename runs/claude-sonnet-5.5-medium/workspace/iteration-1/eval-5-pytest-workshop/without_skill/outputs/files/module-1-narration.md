# Module 1: Your first test — video narration script

**Target length:** about 8 minutes
**Format:** screen recording of a terminal and editor, with narration over it.
**Conventions:** Text in *[brackets]* is a screen direction and is not read aloud. Code blocks show what appears on screen.

---

## 1. Opening (0:00–0:50)

*[Screen: title card, "Module 1: Your first test"]*

Welcome to the workshop. In this first module, you're going to write a test, run it, watch it fail, and fix it. That's the whole loop, and it's the loop you'll repeat all day.

If you've used unittest, you already know why we test. What you'll notice here is how little you have to type. No classes, no special assertion methods. Just a function and an assert.

If you've never written a test, that's fine. We're starting from an empty folder.

*[Screen: empty terminal in a new folder called `shop`]*

---

## 2. Setup (0:50–1:50)

We need Python 3.10 or newer, and a virtual environment so we don't touch your system Python. Create one, activate it, and install pytest.

*[Type and run:]*

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install pytest
pytest --version
```

If that last command prints a version number, you're set. Anything recent will behave the same for today.

*[Pause on the version output for two seconds.]*

---

## 3. The code we'll test (1:50–2:50)

Tests need something to test. We'll use a tiny piece of a pretend online shop: a function that applies a percentage discount to a price.

Create a file called `pricing.py`.

*[Create `pricing.py` and type:]*

```python
def apply_discount(price: float, percent: float) -> float:
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)
```

It takes a price and a percentage. If the percentage makes no sense, it raises an error. Otherwise it returns the discounted price, rounded to cents.

Small, but it has two behaviors worth checking: the normal case and the bad input. We'll cover both.

---

## 4. Writing the first test (2:50–4:20)

Now create a second file in the same folder, called `test_pricing.py`.

That name matters. pytest finds tests by looking for files that start with `test_`, and functions that start with `test`. Follow that pattern and you never have to register or list your tests anywhere.

*[Create `test_pricing.py` and type:]*

```python
from pricing import apply_discount


def test_apply_discount_takes_percent_off_price():
    assert apply_discount(100, 20) == 80
```

That's the entire test. A function whose name starts with `test`, and one `assert`.

Look at what's missing compared to unittest. There's no import of a test framework. No class inheriting from TestCase. And no `assertEqual`. We use Python's own `assert` statement, with the normal double-equals operator.

And notice the function name. It's long on purpose. When this fails at two in the morning in CI, the name is the first thing you'll read, so make it say what should be true.

---

## 5. Running it (4:20–5:00)

*[Switch to terminal.]*

Run it. Just type `pytest`.

*[Run:]*

```bash
pytest
```

*[Screen output shows `test_pricing.py .` and `1 passed`.]*

pytest found our file, found our function, ran it, and printed one dot. A dot is a pass. At the bottom, the summary: one passed.

For a bit more detail, add `-v`, for verbose.

*[Run `pytest -v`.]*

Now you see each test by name with the word PASSED next to it. I use plain `pytest` while working and `-v` when I want to see exactly what ran.

---

## 6. Watching it fail (5:00–6:30)

A test that has never failed hasn't proven much. So let's break it on purpose.

*[In `test_pricing.py`, change `80` to `85`. Save. Run `pytest`.]*

```python
    assert apply_discount(100, 20) == 85
```

*[Screen shows the failure output. Highlight the `assert 80.0 == 85` line.]*

Here's the failure. Read it from the bottom up. The summary says one failed. Above it is the line that failed, marked with an arrow, and the actual values: eighty point zero does not equal eighty-five. pytest also shows which call produced that 80.0.

This is the payoff for using plain `assert`. pytest rewrites your assertions behind the scenes so that when they fail, it shows you the values on both sides. You didn't write a failure message. You got a useful one anyway.

Now fix the test. Change 85 back to 80.

*[Edit, save, run `pytest`. It passes.]*

Green again.

---

## 7. Testing the error case (6:30–7:30)

One more test. Our function promises to raise an error for a bad percentage, so let's check that it does.

*[Add to `test_pricing.py`:]*

```python
import pytest
from pricing import apply_discount


def test_apply_discount_takes_percent_off_price():
    assert apply_discount(100, 20) == 80


def test_apply_discount_rejects_percent_over_100():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
```

We import `pytest` at the top, and use `pytest.raises` as a context manager. The test passes only if the code inside the `with` block raises a ValueError. If no error is raised, or a different one, the test fails.

*[Run `pytest -v`. Two tests pass.]*

Two tests, both passing.

---

## 8. Recap and what's next (7:30–8:10)

*[Screen: three-line summary appears, one line at a time.]*

Let's recap. A test is a function whose name starts with `test`, in a file whose name starts with `test_`. You check behavior with a plain `assert`. You check errors with `pytest.raises`. And you run everything with the `pytest` command.

Now it's your turn. The exercise for this module asks you to add tests for the edge cases: zero percent, exactly 100 percent, and a negative percent. Try to predict what each should do before you run it.

In Module 2, we'll look at fixtures, which is where pytest starts to really differ from unittest. See you there.

*[End card.]*

---

## Production notes

- **Pacing:** typing on screen fills the gaps between spoken sections, so don't rush the reading to fit.
- **Failure section:** record the real pytest output for the `85` case rather than a mock-up, so learners see exactly what they'll see. Confirm the `assert 80.0 == 85` line is legible at video resolution.
- **Exercise link:** the recap refers to a Module 1 exercise. It doesn't exist yet, so create it before publishing.
