# Testing Python services with pytest

A one-day workshop for backend developers. You start by writing and running one test. You finish by testing a small HTTP service, including the parts that call a database or another service.

This workshop teaches pytest. It is not a general course on test-driven development or on Python itself. If you want to learn how to design code around tests, read a TDD book alongside it.

## Who this is for

- You write Python backend code and can read a function, a class and an import without help.
- You may have written tests with `unittest`, or you may never have written a test. Both are fine. Module 1 starts from an empty folder and never assumes `unittest` knowledge.
- You may never have written a fixture. Module 3 introduces them from scratch.

This workshop is not for people who are new to Python. Learn the basics first, for example with the [Python tutorial](https://docs.python.org/3/tutorial/), and then come back.

## What you need

- Python 3 and a terminal.
- A text editor.
- A folder you can create files in. Module 1 creates a virtual environment there and installs pytest into it.

## The six modules

The modules build on each other. Modules 1 to 3 use one small pricing example. Modules 4 to 6 use a small HTTP service.

| # | Module | You will be able to |
|---|--------|---------------------|
| 1 | [Your first test](#module-1) | Install pytest, write a test function, and run it. |
| 2 | [Assertions, failures and exceptions](#module-2) | Read a failing test, and check that code raises the right error. |
| 3 | [Fixtures](#module-3) | Share setup between tests and clean up after them. |
| 4 | [Parametrized tests](#module-4) | Run one test body against many inputs and name each case. |
| 5 | [Replacing dependencies](#module-5) | Swap out a database, a clock or a remote service with `monkeypatch` and test doubles. |
| 6 | [Testing an HTTP service](#module-6) | Test endpoints end to end and keep the tests fast and independent. |

### Module 1: Your first test {#module-1}

Create a virtual environment, install pytest, write a test for one function, run it, and watch it pass and then fail. The module has a video of about 8 minutes and a hands-on exercise.

### Module 2: Assertions, failures and exceptions {#module-2}

Use plain `assert`, read pytest's failure report, and check error cases with `pytest.raises`. If you use `unittest`, you will see how plain `assert` replaces the `assertEqual` family of methods.

### Module 3: Fixtures {#module-3}

Write your first fixture. Learn how pytest finds a fixture by the name of a test's parameter, how to put shared fixtures in `conftest.py`, and how to clean up with `yield`.

### Module 4: Parametrized tests {#module-4}

Replace copy-pasted tests with `@pytest.mark.parametrize`. Give each case an id so a failure tells you which input broke.

### Module 5: Replacing dependencies {#module-5}

Keep tests fast and repeatable by replacing the slow or unpredictable parts of a service: a database, the current time, a remote API. You use the `monkeypatch` fixture and `unittest.mock`, and you learn when a test double hides a real bug.

### Module 6: Testing an HTTP service {#module-6}

Put the modules together. Call the service's endpoints from tests, build a fresh database for each test with a fixture, and organise a growing test suite.

## How to use this workshop

- **Following the day in order:** do the modules 1 to 6. Each module builds on the one before it.
- **Already writing pytest tests:** skim module 1, then start at module 3. Module 3 introduces fixtures, and every later module uses them.
- **Coming from `unittest`:** do module 1 and module 2 in full. They show how each `unittest` habit maps to pytest.
- **Falling behind:** finishing a module's exercise matters more than finishing the day. Finish the module you are on, then continue with the next one after the workshop.

On a first pass you do not need to understand every line. Each module says which parts you may skip.

## Start

[Go to module 1: Your first test](#module-1)
