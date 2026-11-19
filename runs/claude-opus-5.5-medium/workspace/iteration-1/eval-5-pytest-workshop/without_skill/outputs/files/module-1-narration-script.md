# Module 1 video: Your first test

**Narration script** · Target length: about 8 minutes (about 1,150 spoken words at a relaxed pace)

**Format:** Screen recording of an editor and a terminal side by side, with the presenter's voice-over. **ON SCREEN** lines describe what viewers see. **NARRATION** is read aloud. Code and terminal output appear exactly as shown. Before recording, rehearse each command once and use your real terminal output. Version numbers and timings in the header lines will differ from the examples here.

**What viewers will have by the end:** pytest installed, one passing test, one failing test they know how to read, and a clear idea of how pytest finds tests.

---

## 1. Opening (0:00–0:45)

**ON SCREEN:** Title card: "Module 1: Your first test." Then an empty project folder in the editor.

**NARRATION:**

> Welcome to the workshop. In this first module we're going to do one thing: write a test, run it, and watch it pass. Then we'll break it on purpose so you can see what a failure looks like.
>
> If you've only used `unittest`, some of this will feel almost too simple. That's the point. pytest removes most of the ceremony. You don't need a test class, you don't need to inherit from anything, and you don't need to remember `assertEqual` versus `assertIn` versus `assertTrue`.
>
> And if you've never written a test at all, you're starting at the right place.
>
> Let's set up.

---

## 2. Install pytest (0:45–1:45)

**ON SCREEN:** Terminal in the project folder. Type each command as it's mentioned.

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python -m pip install pytest
$ pytest --version
```

**NARRATION:**

> First we'll create a virtual environment so pytest is installed for this project only and not for your whole machine. That's `python3 -m venv .venv`, then activate it.
>
> On Windows, activation is a little different: it's `.venv\Scripts\activate`. The command is in the exercise notes too.
>
> Now install pytest with `python -m pip install pytest`.
>
> To check that it worked, run `pytest --version`. You should see a version number. If you get "command not found" instead, the virtual environment probably isn't activated. Run the activate command again and retry.

---

## 3. The code we're going to test (1:45–2:30)

**ON SCREEN:** Create `pricing.py` in the editor and type:

```python
def apply_discount(price_cents, percent):
    return price_cents - price_cents * percent // 100
```

**NARRATION:**

> We need some code to test. Here's a small function you might find in an order service. It's called `apply_discount`. It takes a price in cents and a discount percentage, and returns the discounted price.
>
> We use cents, as whole numbers, so we don't run into floating-point rounding with money. A thousand cents is ten dollars.
>
> So if something costs ten dollars and we take ten percent off, we expect nine dollars back, which is nine hundred cents. Let's write a test that says exactly that.

---

## 4. Write the test (2:30–3:45)

**ON SCREEN:** Create `test_pricing.py` next to `pricing.py` and type:

```python
from pricing import apply_discount


def test_apply_discount_takes_percentage_off():
    assert apply_discount(1000, 10) == 900
```

**NARRATION:**

> Make a new file called `test_pricing.py`. The name matters, and we'll come back to why in a minute.
>
> First we import the function we're testing.
>
> Then we write a plain function whose name starts with `test_`. Name it after what it checks. "Apply discount takes percentage off" reads like a sentence, and that's on purpose. When a test fails months from now, the name should tell you what broke.
>
> Inside, there's one line: `assert apply_discount(1000, 10) == 900`.
>
> That's the whole test. It's Python's built-in `assert` statement, with no special methods.

**ON SCREEN:** Split view: the pytest test on the left, the `unittest` version on the right.

```python
import unittest

from pricing import apply_discount


class TestApplyDiscount(unittest.TestCase):
    def test_apply_discount_takes_percentage_off(self):
        self.assertEqual(apply_discount(1000, 10), 900)
```

**NARRATION:**

> If you're coming from `unittest`, here's the same test the way you'd write it there: a class that inherits from `TestCase`, a method that takes `self`, and `self.assertEqual`.
>
> Both versions check the same thing. The pytest version just has less to type and less to read.
>
> One more thing: pytest can run `unittest`-style tests too. You don't have to rewrite your existing suite to start using pytest. You can move it over one test at a time, or not at all.

---

## 5. Run it (3:45–4:45)

**ON SCREEN:** Back to the full-width terminal.

```console
$ pytest
```

```text
============================= test session starts ==============================
platform darwin -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/you/pytest-workshop
collected 1 item

test_pricing.py .                                                        [100%]

============================== 1 passed in 0.01s ===============================
```

**NARRATION:**

> Now run `pytest` with no arguments.
>
> Let's read this from the top. The header tells you which Python and pytest versions are running, and which folder pytest treats as the project root.
>
> "collected 1 item" means pytest found one test.
>
> Next is the file name followed by a single dot. Each dot is one passing test. With a hundred tests, you'd see a row of dots filling up.
>
> At the bottom: one passed. That's your first passing test. Congratulations!
>
> If you want to see test names instead of dots, add `-v` for verbose.

**ON SCREEN:**

```console
$ pytest -v
```

```text
test_pricing.py::test_apply_discount_takes_percentage_off PASSED         [100%]
```

**NARRATION:**

> Now each test is listed by file and name, joined with a double colon. That's also how you'd run just this one test, by passing that exact path to pytest.

---

## 6. How pytest found your test (4:45–5:30)

**ON SCREEN:** Simple graphic over the file tree:

- Files named `test_*.py` or `*_test.py`
- Functions named `test_*`
- Classes named `Test*` (with no `__init__` method)

**NARRATION:**

> So how did pytest know where the test was? We never told it.
>
> pytest looks in the current folder and every folder below it. It collects files whose names start with `test_` or end with `_test`. Inside those files, it runs every function whose name starts with `test`.
>
> That's why the names matter. If you call the file `pricing_tests.py`, with an "s", or name the function `check_discount`, pytest will skip it without any warning. It'll just say it collected zero items.
>
> So if you ever see "collected 0 items" and you're sure you wrote a test, check the names first.

---

## 7. Break it on purpose (5:30–7:15)

**ON SCREEN:** In `pricing.py`, delete `price_cents - ` so the function now returns only the discount amount:

```python
def apply_discount(price_cents, percent):
    return price_cents * percent // 100
```

**NARRATION:**

> A test is only useful if it fails when the code is wrong. So let's make the code wrong.
>
> Here's a very realistic bug. I'll delete the subtraction, so the function returns the *discount amount* instead of the *discounted price*. That's the kind of mistake that slips through a quick code review.
>
> Run pytest again.

**ON SCREEN:**

```console
$ pytest
```

```text
collected 1 item

test_pricing.py F                                                        [100%]

=================================== FAILURES ===================================
___________________ test_apply_discount_takes_percentage_off ___________________

    def test_apply_discount_takes_percentage_off():
>       assert apply_discount(1000, 10) == 900
E       assert 100 == 900
E        +  where 100 = apply_discount(1000, 10)

test_pricing.py:5: AssertionError
=========================== short test summary info ============================
FAILED test_pricing.py::test_apply_discount_takes_percentage_off - assert 100 == 900
============================== 1 failed in 0.02s ===============================
```

**NARRATION:**

> The dot is now an "F," for failed. Below it, pytest explains what happened. Let's go through it slowly, because you'll read output like this a lot today.
>
> First comes the name of the failing test, between the underscores.
>
> Then the test's source code. The angle bracket on the left points to the exact line that failed.
>
> The lines starting with "E" are the error. It says: `assert 100 == 900`. We expected 900 and got 100.
>
> And the next line is the most useful part: "where 100 equals `apply_discount(1000, 10)`." pytest doesn't just tell you the comparison failed. It shows the value each part of the expression actually had. We wrote a plain `assert`, and pytest still worked out what the function returned.
>
> In `unittest`, that's why you need all those different assert methods: they're how it builds a helpful message. pytest gets the same information from a plain `assert` by rewriting it behind the scenes when it loads your test file. You write simple asserts and still get detailed failure messages.
>
> Then the file and line number, and a one-line summary at the bottom. When you have many failures, that summary is where you'll look first.
>
> Now we know exactly what's wrong: the function returns the discount instead of the price. Let's put the subtraction back.

**ON SCREEN:** Restore the original line in `pricing.py`, then run `pytest` again. Show `1 passed`.

**NARRATION:**

> Run it again, and it passes.
>
> That's the loop you'll use all day: write a test, run it, read what it tells you, fix the code, and run it again.

---

## 8. Wrap-up and handoff to the exercise (7:15–8:00)

**ON SCREEN:** Recap card:

1. A test is a function named `test_…` in a file named `test_….py`
2. Use a plain `assert`
3. Run `pytest`, or `pytest -v` to see names
4. Read failures from the `>` line down to the `E` lines

**NARRATION:**

> Let's recap. A pytest test is a plain function whose name starts with `test`, in a file whose name starts with `test`. You check things with a plain `assert`. You run everything with `pytest`. And when something fails, pytest shows you the failing line and the actual values involved.
>
> Now it's your turn. In the exercise, you'll write two more tests for `apply_discount`: one for a zero percent discount, and one for a one hundred percent discount. Before you run each one, decide what you expect to happen. Then run them and see if you were right.
>
> In Module 2, we'll go further with assertions: comparing whole dictionaries and lists, and checking that your code raises the right exception when it gets bad input.
>
> See you there.

---

## Production notes

- **Word count:** About 1,150 words of narration. At roughly 145 words per minute, plus pauses while typing, this lands close to 8 minutes. If you run long, the easiest cut is the `-v` aside at the end of section 5.
- **Type live, but not too fast.** Viewers will type along. Pause briefly after each command before you press Enter.
- **Zoom the terminal** to at least 18pt so the failure output stays readable when it's scaled down.
- **Highlight while narrating section 7.** Briefly highlight the `>` line, the `E` lines, and the `where` line as you mention each one. That's the main skill in this video.
- **Exercise answers, for instructors:** `apply_discount(1000, 0) == 1000` and `apply_discount(1000, 100) == 0`. Both pass with the correct implementation.
