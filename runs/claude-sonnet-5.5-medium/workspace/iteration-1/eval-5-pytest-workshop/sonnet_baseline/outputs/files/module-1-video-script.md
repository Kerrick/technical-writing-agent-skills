# Module 1 video: Write and run your first pytest test

**Target length:** about 8 minutes (about 1,050 spoken words at a relaxed pace)
**Outcome:** the viewer writes a test, runs it, reads a failure, and fixes it.
**Assumes:** Python 3.10 or later, a terminal, an editor. Viewer knows how to write a Python function.
**Pinned versions:** [PYTEST VERSION], Python [VERSION]. State both in the video description, not in the narration.

## Assets

- Empty folder `orders-service/`, open in the editor and a terminal. Editor and terminal font at 20pt or larger. Notifications off.
- Snippet files to paste from, so the video doesn't show long typing: `orders.py`, `test_orders.py` (stages 1 to 3 below).
- On-screen text card for each command (shown while narrating it).
- Written companion in the module 1 page. It is the source of truth.

## Code used in this video

`orders.py`:

```python
def order_total(prices_cents):
    return sum(prices_cents)


def apply_discount(total_cents, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return total_cents * (100 - percent) // 100
```

Prices are integers in cents so the tests avoid floating-point rounding.

`test_orders.py`, final state:

```python
import pytest

from orders import apply_discount, order_total


def test_order_total_adds_item_prices():
    assert order_total([1250, 799]) == 2049


def test_apply_discount_takes_percent_off():
    assert apply_discount(2000, 10) == 1800


def test_apply_discount_rejects_percent_over_100():
    with pytest.raises(ValueError):
        apply_discount(2000, 150)
```

## Script

| SCREEN / ACTION | NARRATION |
| - | - |
| **0:00 to 0:25. Hook.** Terminal showing a finished run: three dots and `3 passed`. | By the end of this video you'll have written three tests for an orders service and run them. You'll also have read a failing test and fixed it. Four steps: install, write, run, break. |
| **0:25 to 1:30. Install.** Terminal, empty folder `orders-service`. Type `python3 -m venv .venv`. Then `source .venv/bin/activate`. On-screen note: "Windows: `.venv\Scripts\activate`". | Start in an empty folder. We'll make a virtual environment so pytest installs here and nowhere else. On Windows, the activate command is on screen. |
| Type `pip install pytest`. Wait for it to finish. Then `pytest --version`. Highlight the version line. | Install pytest, then ask it for its version. If you see a version number, the install worked. If you see "command not found", the virtual environment isn't active. Run the activate line again. |
| **1:30 to 2:30. The code to test.** Open `orders.py` (paste from snippet). Highlight `order_total`, then `apply_discount`. | This is the code under test. `order_total` adds up item prices. Prices are whole numbers of cents, which keeps our math exact. `apply_discount` takes a percentage off a total, and it refuses a percentage below zero or above one hundred. |
| Pause on the file for two seconds. | Two functions. That's all we need. |
| **2:30 to 4:00. Write the first test.** Create `test_orders.py`. Type the import line, then the first test. Zoom in on the code as it appears. | Now the test. Make a new file. The name starts with `test_`. This matters: pytest finds tests by looking for files named like this. |
| Highlight `def test_order_total_adds_item_prices`. | Inside, write a function whose name also starts with `test_`. Pytest runs every function it finds with that prefix. Name it for the behavior you expect. |
| Highlight the line `assert order_total([1250, 799]) == 2049`. | The body is one line. Call the function with a twelve-fifty item and a seven-ninety-nine item. Then `assert` that the result equals twenty forty-nine. |
| Hold on the `assert` line. | If you've used `unittest`, this replaces `self.assertEqual`. No class, no `self`, no special method. A plain `assert`. A test passes when the function finishes without an error. It fails when an assertion is false. |
| **4:00 to 4:50. Run it.** Terminal. Type `pytest`. Wait for output. Highlight the line `test_orders.py .` and the summary `1 passed`. | Run `pytest` with no arguments. It looks in this folder, finds our file, and runs the test. The dot means one test passed. The last line says `1 passed`. That's your first test. |
| **4:50 to 5:40. Add two more.** Paste in the other two tests. Highlight the `with pytest.raises(ValueError):` line. | Add two more. The second checks a discount of ten percent off twenty dollars. The third checks the error case. `pytest.raises` passes only if the code inside raises that exception. If no error happens, this test fails. |
| Run `pytest`. Highlight `test_orders.py ...` and `3 passed`. | Run again. Three dots, three passed. |
| **5:40 to 7:10. Read a failure.** Edit the second test: change the call to `apply_discount(1999, 10)` and leave `== 1800`. Save. | Now let's break one on purpose, so a failure looks familiar when it's real. Change the total to nineteen ninety-nine, and keep the expected result at eighteen hundred. Before you run it, what do you think pytest will report? Pause for three seconds. |
| Run `pytest`. Pause on the output, then highlight in order: the `F` in the progress line, the `>` arrow line, the `E       assert 1799 == 1800` line. | Run it. An `F` replaces the dot. Under it, pytest shows the test's code, with an arrow on the line that failed. The lines starting with `E` explain why. The function returned seventeen ninety-nine. We expected eighteen hundred. |
| Highlight the short summary line `FAILED test_orders.py::test_apply_discount_takes_percent_off`. | The last section names the failed test. Copy that name to run just this one test later. |
| Highlight `//` in `orders.py`. | So who's wrong, the test or the code? Here, the code. The `//` rounds down to a whole cent, and ten percent off nineteen ninety-nine is seventeen ninety-nine, rounded down. The test's expectation was the mistake. |
| Edit the test: change `1800` to `1799`. Run `pytest`. Show `3 passed`. | Fix the expected value, run again, and we're back to three passed. Reading the `E` lines first will answer most failures. |
| **7:10 to 8:00. Recap and next.** Split screen: the three tests on the left, the passing run on the right. | Here's what you did. You installed pytest. You wrote tests as plain functions in files starting with `test_`. You checked results with `assert`, and errors with `pytest.raises`. You ran `pytest` and read a failure from the `E` lines. |
| Show the module 1 page and the exercise link. | Next is a short exercise. You'll add a test for a discount of zero percent. Then, in module 2, we'll run one test against many inputs at once. The written steps and all code from this video are on the module page. |

## Notes for the recording

- **Output is illustrative.** The pytest output described above was not captured from a real run when this script was written. Run the whole script once on a clean machine and update the highlighted lines (the dots, `1 passed`, the `E` line, and the summary name) to match exactly what your pytest version prints.
- **Re-record candidates:** the install segment (0:25 to 1:30) changes most as tools change. Keep it as its own clip.
- **Captions:** use this narration column as the caption source, after the output check.
