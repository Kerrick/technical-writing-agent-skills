# Module 1: Your first test (video narration script)

Running time: about 8 minutes. The narration is about 1,150 words, spoken at a calm pace.

How to read this script: text under **Narration** is spoken. Text under **On screen** is what the presenter types or shows. Command blocks hold only the command. Output is described in the narration, so the viewer reads it on screen.

The example is a small pricing function for an order service. Modules 2 and 3 reuse it.

## 1. What we build (0:00–0:40)

**On screen:** Title card "Module 1: Your first test". Then an empty terminal in an empty folder named `pricing-demo`.

**Narration:**

Welcome to module 1. In the next eight minutes you will write one test and run it. You will also make it fail on purpose, because the first failure you see should be one you caused.

I assume you can read Python. I do not assume you have used a test framework. If you have used `unittest`, keep that in mind as we go. I will point out where pytest differs.

We start with an empty folder. By the end it holds one function, one test, and a passing test run.

## 2. Install pytest (0:40–1:50)

**On screen:** Type each command and pause after it.

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
python -m pip install pytest
```

**Narration:**

First, a virtual environment. It keeps pytest inside this folder, so it cannot disturb other projects on your machine. The first command creates it. The second command activates it. On Windows, the activation command is `.venv\Scripts\activate` instead. Your prompt now shows `.venv` at the start. That tells you the environment is active.

The third command installs pytest. I run it as `python -m pip` so the install goes to the same Python that the environment uses.

You can check the install with `python -m pytest --version`. It prints the version number, so there is nothing to compare against here. If it prints a version, you are ready.

From here on, I run pytest as `python -m pytest`, not as `pytest`. Both work. The `python -m` form also puts your current folder on Python's import path, which saves you from import errors in a small project like this one.

## 3. The code under test (1:50–3:00)

**On screen:** Create `pricing.py` in the editor and type the code.

```python
def order_total_cents(item_prices_cents, tax_percent):
    subtotal = sum(item_prices_cents)
    return subtotal + subtotal * tax_percent // 100
```

**Narration:**

Now the code we want to test. Create a file named `pricing.py`.

This function takes the prices of the items in an order, in cents, and a tax rate as a whole percent. It adds the prices, then adds the tax, and returns the total in cents.

Two choices here are worth a sentence. We use cents, as integers, so there is no floating-point rounding to distract us. And the double slash is integer division, so the tax is rounded down to a whole cent.

Before we write any test, work out one answer by hand. Two items, ten dollars and twenty-five dollars, so 1000 and 2500 cents. The subtotal is 3500. Ten percent of 3500 is 350. The total is 3850.

That hand calculation is the heart of a test. You decide the right answer first, from the requirements and not from the code. Then you ask the code to agree.

## 4. Write the test (3:00–4:30)

**On screen:** Create `test_pricing.py` next to `pricing.py` and type the code.

```python
from pricing import order_total_cents


def test_order_total_adds_tax_to_the_subtotal():
    total = order_total_cents([1000, 2500], 10)

    assert total == 3850
```

**Narration:**

Create a second file, named `test_pricing.py`, in the same folder.

The file name matters. pytest looks for files whose names start with `test_`. Inside those files, it runs every function whose name starts with `test_`. That is the whole discovery rule for this module. You do not register tests anywhere.

The first line imports the function. The test function has a long name on purpose. When a test fails, the name is the first thing you read, so make it say what should be true.

The body has three parts. We call the function with the two prices and the tax rate. We store the result. Then we use a plain `assert` statement to say that the result equals 3850, the number we worked out by hand.

If you come from `unittest`, notice what is missing. There is no class, no base class that you inherit from, and no `assertEqual` method. A test is a function, and a check is a Python `assert`. In module 2 you will see how pytest still gives you a detailed failure message from a plain `assert`.

## 5. Run it (4:30–5:30)

**On screen:** Run the command. Keep the output visible for the whole section.

```bash
python -m pytest
```

**Narration:**

Now run pytest.

Look at the output from top to bottom. First, pytest prints a header with the Python version, the pytest version and your folder. Then it prints the name of the file it found, `test_pricing.py`, followed by a single green dot. One dot is one test that passed. A failing test would show an F instead.

The last line is the summary. It says one passed, and how long the run took. Green means the code did what you said it should.

A passing run proves less than it seems to, though. A test that has never failed might not be checking anything. So the next step is to break it on purpose.

## 6. Make it fail (5:30–7:00)

**On screen:** In `test_pricing.py`, change `3850` to `3851`. Save. Run `python -m pytest` again, with the output visible.

```bash
python -m pytest
```

**Narration:**

In the test file, change the expected value from 3850 to 3851. Save the file and run pytest again.

This time the dot is an F, and the summary says one failed. Between them, pytest prints a failure report. Read it in this order.

First, the name of the failing test. That is why we gave it a descriptive name.

Second, the source of the test, with an arrow pointing at the line that failed: the `assert` line.

Third, the two values it compared. You see the actual value, 3850, and the expected value, 3851. pytest took your plain `assert` and worked out the values on both sides for you. You did not write a message.

Here the mistake is in the test. When you see a failure like this in real work, there are two possible causes: the code is wrong or the test is wrong. Your hand calculation from earlier decides which. That is why we did it first.

Now change 3851 back to 3850, and run pytest once more.

```bash
python -m pytest
```

The dot is back, and the summary says one passed. You have now seen a test pass, fail and pass again, and you know what each looks like.

## 7. Recap and exercise (7:00–8:00)

**On screen:** A slide with the recap list. Then the exercise instructions from the module page.

**Narration:**

Let me recap. You created a virtual environment and installed pytest. You wrote a function and worked out one answer by hand. You wrote a test as a plain function in a file whose name starts with `test_`, and you checked the result with `assert`. You ran it with `python -m pytest`, and you saw both a pass and a failure.

In the exercise on the module page, you add two more tests to the same file. One uses an empty list of items. The other uses a tax rate of zero. Work out each answer by hand before you run anything.

This module left out some things on purpose. How pytest chooses which files to run, how to run a single test, and how to test code that should raise an error are all covered later. Error cases come in module 2.

In module 3, you will see what to do when five tests need the same setup. See you there.

## Notes for the presenter

- Record in a terminal with a font large enough to read on a phone.
- Do not skip section 6. It is the part viewers remember.
- The failure report in section 6 is described, not pasted, so that the narration matches your terminal. Read the real output aloud during the recording.
