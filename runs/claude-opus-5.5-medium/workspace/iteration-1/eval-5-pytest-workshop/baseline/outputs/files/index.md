<!--
Assumptions (correct these if they're wrong):
- Reader: a backend Python developer deciding whether to sign up, or a registered attendee
  checking what to prepare. They can write Python and run commands in a terminal. Most have
  written tests with unittest; some have never used a pytest fixture. They arrive from a link
  in an invite or an internal training catalog.
- The running project is a small orders service with a FastAPI HTTP layer. If your teams
  mostly use Flask or Django, swap Module 5's framework and keep the rest.
- Version pins, the repository URL, and the schedule times are placeholders marked TODO.
-->

# Testing Python services with pytest

A one-day, hands-on workshop for backend developers. You'll spend the day adding tests to a small orders service: pricing rules first, then the HTTP endpoints. By the end of the day you'll be able to:

- Write a pytest test, run it, and use the failure report to find out what went wrong.
- Move repeated setup into fixtures and share them across test files.
- Cover many inputs, and the errors you expect, with one parametrized test.
- Replace the clock, environment variables, and outside HTTP calls so tests run fast and give the same result every time.
- Test an HTTP endpoint from request to response, including its error responses.
- Pick which tests to run, and run the whole suite in CI.

## Who this is for

This workshop is for you if you write backend services in Python, and either:

- you've written tests with `unittest` and want to know what pytest does differently, or
- you've run a pytest suite someone else wrote, but you've never written a fixture.

It isn't the right fit if you already write fixtures and parametrized tests every week. Modules 4–6 may still be useful on their own; you can join after lunch. It also isn't an introduction to Python. You should already be comfortable writing functions, classes, and imports.

## What you need to know first

- You can write and import a Python module.
- You can create a virtual environment and install packages with `pip`.
- You can run commands in a terminal and use Git to clone a repository.

You don't need any previous experience with testing. If you've used `unittest`, each module points out where pytest differs.

## Set up before the workshop

Allow 15 minutes, and do this before the day. If setup fails during the workshop, you'll lose the first module to it.

You need Python 3.12 or later. Check your version:

```shell
python3 --version
```

1. Clone the workshop repository and change into it:

   ```shell
   git clone TODO(verify): repository URL
   cd orders-service
   ```

2. Create and activate a virtual environment:

   ```shell
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   If you use Windows, run `.venv\Scripts\activate` instead of the `source` command.

3. Install the pinned dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Check out the starting point and run the setup check:

   ```shell
   git checkout module-1-start
   pytest --version
   ```

   You should see `pytest` followed by a version number. TODO(verify): the exact version string once `requirements.txt` is pinned.

If any step fails, post the full error message in TODO(verify): workshop chat channel before the workshop day. If your laptop won't cooperate on the day, use the hosted environment at TODO(verify): hosted environment URL. It has the repository and dependencies installed already.

## Schedule

Each module follows the same pattern: a short video or live demo, then a lab where you add tests to the orders service yourself, then a check-in. Every module starts from a Git tag (`module-N-start`), so if you fall behind you can check out the next tag and carry on.

TODO(verify): confirm times with the venue.

| Time | Session |
| - | - |
| 9:00 | Welcome and setup check |
| 9:15 | Module 1: Write and run your first test |
| 10:15 | Module 2: Share setup with fixtures |
| 11:30 | Break |
| 11:45 | Module 3: Test many inputs with parametrize |
| 12:45 | Lunch |
| 13:45 | Module 4: Replace slow and unpredictable dependencies |
| 15:00 | Break |
| 15:15 | Module 5: Test an HTTP endpoint |
| 16:15 | Module 6: Choose which tests to run, locally and in CI |
| 17:15 | Wrap-up and questions |

## Modules

### Module 1: Write and run your first test

You'll write a test for the service's discount function, run it, and see it pass. Then you'll write a test with the wrong expected value on purpose, so you learn to read pytest's failure report before you need to. You'll see how pytest finds tests by their file and function names, and why a plain `assert` replaces `self.assertEqual`.

**You'll be able to:** write a test function, run it with `pytest`, and use the failure report to decide whether the test or the code is wrong.

### Module 2: Share setup with fixtures

Most tests for the orders service need an order to work on. Building one in each test makes the tests long, and every one breaks when the order changes. You'll move that setup into a fixture. A fixture is a function that pytest runs for you, passing its result to any test that asks for it by name. Then you'll put fixtures in `conftest.py` so every test file can use them, and use `yield` to clean up after a test.

**You'll be able to:** write a fixture, request it from a test, share it through `conftest.py`, and add cleanup code that runs after the test.

### Module 3: Test many inputs with parametrize

The pricing rules have edge cases: zero, one hundred percent, rounding, invalid input. You'll test them all with `@pytest.mark.parametrize` instead of copying a test five times. You'll also use `pytest.raises` to check that bad input raises the error you expect.

**You'll be able to:** turn repeated tests into one parametrized test, and check for an expected exception and its message.

### Module 4: Replace slow and unpredictable dependencies

Order expiry depends on the current time. The tax lookup calls an outside HTTP service. Neither belongs in a fast, repeatable test. You'll use pytest's `monkeypatch` fixture to replace a function and set environment variables. You'll use `tmp_path` to give each test its own temporary directory. And you'll use `unittest.mock` to stand in for the tax service and check how it was called.

**You'll be able to:** isolate a test from the clock, the environment, the file system, and an outside HTTP API, and choose between `monkeypatch` and a mock for each case.

### Module 5: Test an HTTP endpoint

You'll test the service's `POST /orders` endpoint with FastAPI's test client. You'll send requests and check status codes and response bodies, including the `422` response for invalid input. You'll build the client as a fixture, reusing what you learned in Module 2.

**You'll be able to:** write tests for an endpoint's success and error responses, using a fixture that gives each test a clean app.

### Module 6: Choose which tests to run, locally and in CI

As the suite grows, you won't want to run all of it every time. You'll select tests by name with `-k`, rerun only the failures with `--lf`, and mark slow tests with a custom marker. You'll move these settings into `pyproject.toml`, see that pytest runs existing `unittest` test classes without changes, and add a CI job that runs the suite on every push.

**You'll be able to:** run a subset of the suite, configure pytest in `pyproject.toml`, run an existing `unittest` suite with pytest, and run the suite in CI.

## Conventions

- `Monospace` text is code, commands, file names, or output.
- Text such as `TODO(verify): …` marks a detail the organizers still need to fill in.
- Commands assume you're in the repository's root directory, `orders-service`, with the virtual environment activated.

## Versions

This workshop uses Python 3.12 or later and TODO(verify): pytest version pinned in `requirements.txt`. The FastAPI version for Module 5 is pinned in the same file.

## After the workshop

Every module's finished code is on a tag named `module-N-end` in the repository. You can compare it with your work, or use it as a starting point when you add pytest to your own service.
