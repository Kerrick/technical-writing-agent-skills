# Testing Python services with pytest

A one-day, hands-on workshop for backend developers. You write tests for a small orders service, starting from your first test and ending with a suite that runs in CI.

**Date and place:** [DATE], [LOCATION OR VIDEO LINK]
**Instructor:** [NAME]

## Who this is for

You write Python backend code and want to test it with confidence. You can read and write Python functions, classes, and `import` statements.

- **If you have only used `unittest`:** we map each `unittest` idea to its pytest equivalent as it comes up.
- **If you have never written a fixture:** you don't need to. Module 3 introduces them from scratch.

## What you will be able to do

By the end of the day you can:

- Write and run pytest tests for a Python service.
- Read a failing test's output and find the cause.
- Share setup code between tests with fixtures.
- Replace slow or unreliable dependencies, such as a database or a payment API, in a test.
- Test an HTTP endpoint without starting a server.
- Run the suite automatically on every push.

## Before the workshop

You need:

- Python 3.10 or later. Check with `python3 --version`.
- A code editor and a terminal.
- Permission to install packages with `pip` into a virtual environment.

We send a starter repository and a setup check one week before the workshop. [CONFIRM LINK AND TIMING]

## The six modules

Every module builds on the same example: an orders service with items, discounts, and payments. Each module ends with a working test suite you can compare against the starter repository's checkpoint for that module.

| # | Module | You will | Time |
| - | - | - | - |
| 1 | [Write and run your first test](#module-1-write-and-run-your-first-test) | Write, run, and read the result of a test | [TIME] |
| 2 | [Check results and failures](#module-2-check-results-and-failures) | Write many cases with parametrization and test errors | [TIME] |
| 3 | [Share setup with fixtures](#module-3-share-setup-with-fixtures) | Build fixtures and control their scope | [TIME] |
| 4 | [Replace dependencies with fakes](#module-4-replace-dependencies-with-fakes) | Isolate code from the database and network | [TIME] |
| 5 | [Test an HTTP endpoint](#module-5-test-an-http-endpoint) | Call your service's routes from a test | [TIME] |
| 6 | [Organize the suite and run it in CI](#module-6-organize-the-suite-and-run-it-in-ci) | Group tests, select subsets, run on every push | [TIME] |

### Module 1: Write and run your first test

Install pytest, write a test for an order total, run it, and read a failure. Includes a video (about 8 minutes) and a short exercise.

### Module 2: Check results and failures

Run one test body against many inputs with `pytest.mark.parametrize`. Check that code raises the right exception with `pytest.raises`. Compare `assert` with `unittest`'s `assertEqual` family.

### Module 3: Share setup with fixtures

Define a fixture, request it by name, and put shared fixtures in `conftest.py`. Control how long a fixture lives with scope. Clean up after a test with `yield`.

### Module 4: Replace dependencies with fakes

Use `monkeypatch` and `unittest.mock` to stand in for a payment gateway and a clock. Decide when a fake helps and when it hides bugs.

### Module 5: Test an HTTP endpoint

Send requests to the orders service from a test and check status codes and JSON bodies. Combine this with fixtures and fakes from modules 3 and 4.

### Module 6: Organize the suite and run it in CI

Lay out test files, mark and select tests, and read a failing CI run. Finish with a pipeline that runs your tests on every push.

## Frequently asked questions

**I know `unittest`. Will I be bored in module 1?**
Module 1 is short. It sets up the vocabulary the other five modules use, and it shows what pytest prints that `unittest` doesn't.

**Do I need to know what a fixture is before I arrive?**
No. Module 3 starts from a test that repeats setup code and shows why a fixture helps.

**Which web framework do the modules use?**
[CONFIRM FRAMEWORK] Module 5 shows the testing pattern for it. The pytest techniques carry over to other frameworks.

## Register

[REGISTRATION LINK AND PRICE]
