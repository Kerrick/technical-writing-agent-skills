# Module 1 video: Write and run your first test

**Viewer:** a backend Python developer at the start of the workshop. They've used `unittest` or no test framework, and they've never written a pytest test. They're watching in order, with the workshop repository open beside the video.

**Outcome:** The viewer can write a test function, run it with `pytest`, and use the failure report to decide whether the test or the code is wrong.

**Starting state:** tag `module-1-start` of the `orders-service` repository, virtual environment activated, dependencies installed as described on the workshop page. The tag contains:

- `orders/__init__.py` (empty)
- `orders/pricing.py`, with the `apply_discount` function shown in row 3
- `pyproject.toml`, with the pytest settings shown in row 9
- an empty `tests/` directory

**Ending state:** tag `module-1-end`, which adds `tests/test_pricing.py` with two passing tests.

**Target length:** about 7:15, inside the 8-minute slot. The narration is about 730 words, roughly 6 minutes of speech. Live typing, the prediction pause in row 12, and the holds on output add the rest. Don't pad it to fill 8 minutes. Viewers stop watching in large numbers after about six minutes, so finishing under the slot is better. Read the script aloud with a timer before recording, and adjust the section timings below.

**Production notes:**

- Editor and terminal at a font size readable on a phone. Same window layout as the other modules.
- Clean shell prompt: `orders-service $` with no username, hostname, or home path.
- Type the test code live. Don't paste it. The typing is the lesson.
- Hold every pytest result on screen for at least two seconds before speaking over it.
- No music under narration.
- **TODO(verify):** pytest wasn't available when this script was written, so none of the pytest output below has been run. Before recording, run each command from `module-1-start` and replace the expected output in rows 1, 8, 13, and 17 with the real output. Version numbers, timings, and the spacing of the separator lines will differ.

## Script

### Hook (0:00–0:25)

| # | Visual | Narration |
| - | - | - |
| 1 | Terminal, full screen: the result of `pytest -v` from the end of this video, two `PASSED` lines and `2 passed` (see row 17). Hold. | "This is two passing tests for a real piece of business logic. By the end of this video you'll have written both of them. You'll also have watched one of them fail, and you'll know how to read the failure." |
| 2 | Title card: "Module 1: Write and run your first test". | "This is module one: write and run your first test." |

### The code under test (0:25–1:05)

| # | Visual | Narration |
| - | - | - |
| 3 | Editor: `orders/pricing.py`, full file (listing A). Cursor on the `def` line. | "We're working in the orders service. You should be on the tag module-1-start. Open the file orders slash pricing dot py. It has one function: apply discount." |
| 4 | Highlight the parameters `subtotal_cents` and `percent`. | "It takes a subtotal in cents and a discount percentage. It returns the new subtotal, also in cents." |
| 5 | Highlight the docstring, then the `//` operator. | "The docstring says the result is rounded down to the cent. That's what the double slash does. It's integer division, so any fraction of a cent is dropped. Remember that. It matters in a few minutes." |

### Write the first test (1:05–2:30)

| # | Visual | Narration |
| - | - | - |
| 6 | Editor: create `tests/test_pricing.py`. Type the import line, then the test (listing B). Type slowly. | "Now create a file in the tests folder called test underscore pricing dot py. Import apply discount from orders dot pricing. Then write a function called test underscore ten underscore percent off. Inside it, one line: assert that apply discount of five thousand and ten equals forty-five hundred. Five thousand cents is fifty dollars, and ten percent off leaves forty-five." |
| 7 | Split screen: listing B on the left, the `unittest` version (listing C) on the right, dimmed slightly. Highlight `class`, `self`, and `assertEqual` on the right, then `assert` on the left. | "If you've used unittest, here's the same test written that way. You'd need a class that inherits from TestCase, a method that takes self, and self dot assert equal. In pytest, a test is a plain function, and you check things with Python's own assert statement. No class. No special assert methods." |

### Run it (2:30–3:45)

| # | Visual | Narration |
| - | - | - |
| 8 | Terminal: type `pytest`, press Enter. Output (listing D) appears. Hold 2s. | "Go to the terminal, in the root of the project, and run pytest. That's the whole command." |
| 9 | Highlight `collected 1 item`. Then cut to `pyproject.toml` (listing E) briefly, highlighting `testpaths` and `pythonpath`. Back to terminal. | "Look at the line that says collected one item. Pytest searched the tests folder and found our test on its own. The pyproject file from the starter tells pytest to look in tests, and to let the tests import the orders package. You won't need to touch it today." |
| 10 | Highlight the single dot after `tests/test_pricing.py`, then the `1 passed` line. | "Each dot after the file name is one passing test. We have one dot. The last line says one passed." |
| 11 | Editor: highlight the file name `test_pricing.py`, then the function name `test_ten_percent_off`. | "How did pytest know this was a test? By its name. Pytest collects files whose names start with test underscore. Inside them, it runs functions whose names start with test. If you forget the prefix, pytest doesn't report an error. It skips the function without saying anything. So check the name first when a test doesn't seem to run." |

### Watch a test fail on purpose (3:45–6:15)

| # | Visual | Narration |
| - | - | - |
| 12 | Editor: below the first test, type the second test with `1700` as the expected value (listing F). Pause on the screen before running. | "Let's add a second test. Nineteen ninety-nine cents, fifteen percent off. Fifteen percent of nineteen ninety-nine is about three hundred, so I'm going to guess seventeen hundred. Before you run it, pause the video. Look back at the docstring, and predict whether this passes." |
| 13 | Terminal: run `pytest`. Failure report (listing G) appears. Hold 3s. | "Run pytest again. This time we get a capital F instead of a dot, and a failure report." |
| 14 | Highlight the line beginning with `>`. | "Read it from the top. The line with the arrow is the line that failed. Pytest shows you the actual code of the test." |
| 15 | Highlight the two `E` lines: `assert 1699 == 1700`, then `where 1699 = apply_discount(1999, 15)`. | "The lines starting with E show the values. The function returned sixteen ninety-nine. We expected seventeen hundred. The next line says where sixteen ninety-nine came from: the call to apply discount. We wrote a plain assert, and pytest still shows both sides. That's why you don't need assert equal." |
| 16 | Editor: show `pricing.py` docstring next to the test. Change `1700` to `1699` in the test (diff, listing H). | "Now the important question. Is the test wrong, or is the code wrong? The exact answer is sixteen ninety-nine point one five cents. The docstring says round down, so sixteen ninety-nine is correct. My guess was wrong, not the code. Change seventeen hundred to sixteen ninety-nine. When a test fails, always ask that question first. Don't change the test just to get it passing." |
| 17 | Terminal: run `pytest -v`. Output (listing I) appears. Hold 2s. Highlight each `PASSED`. | "Run it once more, this time with dash v, for verbose. Instead of dots, you get each test's name and its result. Both tests pass." |

### Recap and next (6:15–7:15)

| # | Visual | Narration |
| - | - | - |
| 18 | Editor: `tests/test_pricing.py`, final version (listing J). Cursor moves to the file name, then each function name, then each `assert`. | "Here's what you can now do. Write a test as a plain function in a file that starts with test. Check results with a plain assert. Run everything with pytest. And when a test fails, read the arrow line and the E lines, and decide whether the test or the code is wrong." |
| 19 | Text on screen, one line: "Predict: rename `test_ten_percent_off` to `check_ten_percent_off`. What does `pytest` print?" | "One question to try in the lab. Rename the first test so it starts with check instead of test. Before you run pytest, predict what it prints. Then run it and see." |
| 20 | Title card: "Next: Module 2: Share setup with fixtures". | "Next, in module two, we'll test whole orders. Each test will need an order to work with, and you'll use a fixture so you don't have to build it in every test." |

## Listings

These are the exact code and output for the visuals above. Publish listings B, E, and J with the video as copyable text.

### Listing A: `orders/pricing.py` (in the starter, not typed)

```python
def apply_discount(subtotal_cents: int, percent: int) -> int:
    """Return the subtotal after a percentage discount, rounded down to the cent."""
    if not 0 <= percent <= 100:
        raise ValueError(f"percent must be between 0 and 100, got {percent}")
    return subtotal_cents * (100 - percent) // 100
```

I checked the function's results with plain Python: `apply_discount(5000, 10)` returns `4500`, and `apply_discount(1999, 15)` returns `1699`.

### Listing B: `tests/test_pricing.py`, first version

```python
from orders.pricing import apply_discount


def test_ten_percent_off():
    assert apply_discount(5000, 10) == 4500
```

### Listing C: the same test in `unittest` (shown, not typed)

```python
import unittest

from orders.pricing import apply_discount


class TestApplyDiscount(unittest.TestCase):
    def test_ten_percent_off(self):
        self.assertEqual(apply_discount(5000, 10), 4500)
```

### Listing D: first `pytest` run

```shell
pytest
```

TODO(verify): replace with real output.

```text
============================= test session starts ==============================
platform darwin -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /orders-service
configfile: pyproject.toml
testpaths: tests
collected 1 item

tests/test_pricing.py .                                                  [100%]

============================== 1 passed in 0.01s ===============================
```

### Listing E: pytest settings in `pyproject.toml` (in the starter)

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
```

Without `pythonpath = ["."]`, running `pytest` from the project root can fail with `ModuleNotFoundError: No module named 'orders'`, because `tests/` has no `__init__.py`. TODO(verify): confirm by removing the line and running `pytest`. If that's the case, add this error and its fix to the lab's troubleshooting notes.

### Listing F: second test added, with the wrong expected value

```python
def test_ten_percent_off():
    assert apply_discount(5000, 10) == 4500


def test_fifteen_percent_off_rounds_down():
    assert apply_discount(1999, 15) == 1700
```

### Listing G: failing run

```shell
pytest
```

TODO(verify): replace with real output.

```text
============================= test session starts ==============================
...
collected 2 items

tests/test_pricing.py .F                                                 [100%]

=================================== FAILURES ===================================
_____________________ test_fifteen_percent_off_rounds_down _____________________

    def test_fifteen_percent_off_rounds_down():
>       assert apply_discount(1999, 15) == 1700
E       assert 1699 == 1700
E        +  where 1699 = apply_discount(1999, 15)

tests/test_pricing.py:9: AssertionError
=========================== short test summary info ============================
FAILED tests/test_pricing.py::test_fifteen_percent_off_rounds_down - assert 1699 == 1700
========================= 1 failed, 1 passed in 0.02s ==========================
```

### Listing H: the fix

```diff
 def test_fifteen_percent_off_rounds_down():
-    assert apply_discount(1999, 15) == 1700
+    assert apply_discount(1999, 15) == 1699
```

### Listing I: verbose run

```shell
pytest -v
```

TODO(verify): replace with real output.

```text
============================= test session starts ==============================
...
collected 2 items

tests/test_pricing.py::test_ten_percent_off PASSED                       [ 50%]
tests/test_pricing.py::test_fifteen_percent_off_rounds_down PASSED       [100%]

============================== 2 passed in 0.01s ===============================
```

### Listing J: `tests/test_pricing.py`, final version (tag `module-1-end`)

```python
from orders.pricing import apply_discount


def test_ten_percent_off():
    assert apply_discount(5000, 10) == 4500


def test_fifteen_percent_off_rounds_down():
    assert apply_discount(1999, 15) == 1699
```

## Answer to the prediction question (for the lab facilitator, not the video)

Pytest collects one item instead of two. `check_ten_percent_off` doesn't start with `test`, so pytest ignores it and reports nothing about it. The output shows `1 passed`. That's the trap: the suite stays green while a test silently stops running. TODO(verify): confirm the output.

## Companion material to publish with the video

- Captions edited from this script. Auto-captions mangle code names such as `apply_discount`.
- Chapter timestamps: 0:00 Hook, 0:25 The code under test, 1:05 Write the first test, 2:30 Run it, 3:45 Watch a test fail, 6:15 Recap. Update these from the final cut.
- Links to tags `module-1-start` and `module-1-end`.
- The commands as copyable text: `pytest`, `pytest -v`.
