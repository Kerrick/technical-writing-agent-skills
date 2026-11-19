# Testing Python services with pytest

A one-day workshop for backend developers. You will write tests for a small invoicing service, starting with a single `assert` and ending with a suite that runs the same way on your laptop and in CI.

## Who this is for

You write Python backend code and want to test it with confidence. You need to be comfortable with functions, dictionaries, and a terminal. You don't need any pytest experience.

- **You've used `unittest`.** Much of what you know carries over. Each module points out where pytest does the same job differently, and [the unittest-to-pytest map](#coming-from-unittest) below lists the pairs.
- **You've never written a fixture.** Module 2 builds one from scratch, starting with the duplicated test code that fixtures remove. You don't need to know anything about them beforehand.

## The six modules

Work through them in order. Each module builds on the invoicing service from the one before, and restates the code it starts from.

| # | Module | You will |
|---|--------|----------|
| 1 | [Your first test](module-1-video-script.md) | Write a test with a plain `assert`, run it, break it on purpose, and read the failure report. |
| 2 | Fixtures | Remove repeated setup from your tests with fixtures, and control how long each one lives. |
| 3 | Parametrized tests | Run one test against many inputs, and see which input failed. |
| 4 | Isolating external services | Replace slow or unsafe dependencies, such as a payment gateway, with `monkeypatch` and fakes. |
| 5 | Testing service boundaries | Test an HTTP endpoint and database code from the outside. |
| 6 | Organizing and running the suite | Share fixtures with `conftest.py`, group tests with markers, and run the suite in CI. |

Already comfortable with a module's topic? Skip to the next one. Module 1 is the quickest to skim if you have written pytest tests before.

## Coming from unittest

Existing `unittest.TestCase` tests run under pytest without changes, so you can adopt pytest one test at a time.

| In `unittest` | In pytest | Covered in |
|---------------|-----------|------------|
| A `TestCase` subclass holding `test_*` methods | A plain function named `test_*` | Module 1 |
| `self.assertEqual(a, b)` and the other `assert*` methods | `assert a == b` | Module 1 |
| `python -m unittest` | `pytest` | Module 1 |
| `setUp` and `tearDown` | Fixtures | Module 2 |
| `subTest` | Parametrization | Module 3 |
| `unittest.mock.patch` | `monkeypatch` (and `unittest.mock` still works) | Module 4 |

## What the workshop doesn't cover

It doesn't teach Python itself or how to design the service you're testing. It doesn't cover load testing or browser testing. You'll write tests for the sample invoicing service we provide, not your own codebase, so bring questions about your own code to the breaks.

## Getting help

Ask the instructor in the room. If a step doesn't work on your machine, say so right after you hit it. Early failures are usually setup, and they're quick to fix together. If you find a mistake in these materials, tell the instructor so it gets corrected.
