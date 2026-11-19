# Testing Python services with pytest

A one-day, hands-on workshop for backend developers. You write tests for a small invoicing module, run them with pytest, and grow them into a suite you could hand to your team. Each module builds on the last: same running example, one new idea at a time.

You don't need any pytest experience. If you've written tests with `unittest`, you'll connect each pytest idea to the `unittest` habit it replaces. If you've never written a fixture, module 2 starts from zero.

## Where to start

| If you… | Start at |
| --- | --- |
| have only used `unittest`, or have never written a Python test | Module 1, then work through in order |
| have run pytest before but never written a fixture | Skim module 1's closing checkpoint, then start module 2 |
| use fixtures and `parametrize` already | Module 4 |

Modules after the first build on the code from earlier ones. Each one begins by showing the code it starts from, so you can catch up if you skip ahead or fall behind.

## Modules

1. **[Write and run your first test](module-1-first-test-script.md)**
   Install pytest, write a test as a plain function with a plain `assert`, and read what pytest prints when it fails. Also covers the naming rule that decides which tests pytest runs, and why your existing `unittest` tests keep working. About 8 minutes of video, then a short exercise.

2. **Fixtures: shared setup without `setUp`**
   Build the test data that several tests need, once, and let pytest pass it in. Covers fixtures that clean up after themselves with `yield`, sharing fixtures through `conftest.py`, and how fixture scope trades speed for isolation. Assumes no fixture experience.

3. **Parametrize: one test, many cases**
   Replace copy-pasted tests with one test and a table of inputs and expected results, and read which case failed when one does.

4. **Testing the error paths**
   Check that bad input raises the right exception with `pytest.raises`, and that the message is the one your callers depend on.

5. **Replacing the outside world**
   Keep tests fast and repeatable when the code reads environment variables, writes files, or calls other services. Covers `monkeypatch`, `tmp_path`, and when to reach for `unittest.mock`.

6. **Organizing and running a service's suite**
   Move tests into their own directory, put pytest settings in `pyproject.toml`, select tests by name and marker, and run the suite in CI.

## Before the workshop

You need Python 3.10 or newer and a terminal. The workshop was written and tested against **pytest 9.2.0**; install that version so your output matches the videos:

```console
$ python -m pip install "pytest==9.2.0"
```

Install it inside a virtual environment, so it doesn't touch your system Python. Module 1 walks through this on macOS and Linux. On Windows, the activation command is different; see [Creating virtual environments](https://docs.python.org/3/library/venv.html) in the Python documentation.

## Getting help

During the workshop, flag a facilitator in the room first.

If you find a mistake in the course material, tell a facilitator so it gets fixed for the next group.
