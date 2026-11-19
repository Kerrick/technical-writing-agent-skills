# Testing Python Services with pytest

**A one-day, hands-on workshop for backend developers.**

You'll spend the day writing tests for a small Python web service: real code with a database, an outside API, and the edge cases that tend to break in production. By the end of the day you'll have a test suite you understand line by line, and you'll know how to start one for your own services.

---

## Who this is for

You write backend Python and want tests you can trust. You might be:

- **Coming from `unittest`.** You know `TestCase`, `setUp`, and `self.assertEqual`, and you want to know what pytest does differently. (Your existing `unittest` tests keep working. pytest runs them as they are.)
- **New to fixtures.** You've heard the word but never written one. We cover them from scratch in Module 3.
- **Testing without much structure.** You have a few tests, but they're slow, flaky, or hard to change.

You don't need any pytest experience.

## What you'll be able to do by the end

- Write and run pytest tests, and read the output when one fails
- Replace `setUp`/`tearDown` with fixtures you can reuse across files
- Run one test against many inputs without copying it
- Keep tests away from real networks, clocks, and environment variables
- Test a running service's HTTP endpoints against a real, disposable database
- Organize a test suite so it stays fast and readable as it grows

---

## The six modules

Each module starts with a short video, followed by guided exercises on the workshop project. Every module builds on the one before it.

### Module 1: Your first test

Install pytest, write a test as a plain function with a plain `assert`, and run it. Then break the code on purpose so you can see what a failure looks like and how pytest explains it. You'll also learn how pytest finds tests, and how that compares with `unittest`.

**You'll leave with:** a passing test, a failing test you know how to read, and a project set up for the rest of the day.

### Module 2: Assertions that tell you what went wrong

Get more out of `assert`: compare dicts, lists, and strings and read pytest's diff of what changed. Check that code raises the right exception with `pytest.raises`, compare floats with `pytest.approx`, and choose which output you want with `-v`, `-x`, `-k`, and `--lf`.

**You'll leave with:** tests for the service's validation logic, including the error paths.

### Module 3: Fixtures

Fixtures are how pytest handles setup and teardown. Write your first fixture, then use `yield` to clean up after a test. You'll learn fixture scope (function, module, session) and use `conftest.py` to share fixtures across files. We map each idea to the `unittest` version you may already know.

**You'll leave with:** reusable fixtures for test data and a temporary database.

### Module 4: Parametrize: one test, many cases

Use `@pytest.mark.parametrize` to run one test against a table of inputs and expected results. Give each case a readable ID so a failure tells you exactly which input broke, and parametrize fixtures to run a whole set of tests against several configurations.

**You'll leave with:** edge-case coverage for the service's business rules, without copy-paste.

### Module 5: Isolating outside dependencies

Your tests shouldn't call a real payment API or depend on today's date. Use the built-in `monkeypatch` fixture for environment variables and attributes, and `unittest.mock` when you need to check how a dependency was called. You'll also learn when *not* to mock.

**You'll leave with:** tests for code that calls an external HTTP API, with no network access needed.

### Module 6: Testing the service end to end

Put it all together. Test HTTP endpoints with the framework's test client, run each test against a clean database, and use markers to separate fast unit tests from slower integration tests. We finish with a suite layout that grows well, and with running the suite in CI.

**You'll leave with:** a complete, organized test suite for the workshop service, and a checklist for starting one in your own codebase.

---

## Before the workshop

Please set this up ahead of time so we can start writing tests in the first few minutes:

- **Python 3.10 or newer.** Check with `python3 --version`.
- **A code editor** you're comfortable with.
- **A terminal** where you can create and activate a virtual environment.
- **The workshop repository**, cloned to your machine. You'll get the link in your welcome email.

You don't need to install pytest beforehand. We do that together in Module 1.
