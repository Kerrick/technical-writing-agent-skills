# Testing Python Services with pytest

**A one-day hands-on workshop for backend developers**

You ship Python services. You want to change them without holding your breath. This workshop takes you from your first `assert` to a fast, trustworthy test suite that runs on every pull request.

You don't need any pytest experience. If you've written tests with `unittest`, you'll see how much of that ceremony you can drop. If you've never written a fixture, you'll write several by lunchtime.

## Who this is for

- Backend developers who write Python services (HTTP APIs, workers, data pipelines).
- People who have used `unittest`, or have never written automated tests.
- Anyone who has inherited a test suite that is slow, flaky, or hard to read.

## Before you start

You'll need:

- Python 3.10 or newer
- A terminal and a code editor
- Comfort writing Python functions, classes, and imports

You do not need to know pytest, `unittest`, or any mocking library. We install everything in Module 1.

## What you'll learn

By the end of the day you will be able to:

- Write, run, and read the output of pytest tests
- Share setup code cleanly with fixtures
- Cover many cases with one test using parametrization
- Isolate your code from the network, the clock, and other services
- Test an HTTP API and a database-backed service end to end
- Run your suite in CI with coverage, markers, and a sensible speed budget

## The six modules

### Module 1: Your first test
Install pytest, write a test for a small function, run it, and learn to read a failure. Plain `assert` instead of `self.assertEqual`, test discovery, and `pytest.raises`.

### Module 2: Fixtures
Replace `setUp` and `tearDown` with fixtures. Fixture scope, setup and teardown with `yield`, built-in fixtures such as `tmp_path`, and sharing fixtures through `conftest.py`.

### Module 3: Parametrization and test organization
Turn copy-pasted tests into one table of cases with `@pytest.mark.parametrize`. Lay out a test directory, name tests so failures explain themselves, and use `-k` to run just what you need.

### Module 4: Isolating your code with mocks and monkeypatch
Keep tests off the network and away from the real clock. `monkeypatch`, `unittest.mock`, and when to use a fake instead of a mock.

### Module 5: Testing APIs and databases
Test a web endpoint through a test client. Build a database fixture that gives every test a clean state, and decide what to test against a real database versus a fake.

### Module 6: Running your suite in CI
Coverage, custom markers to separate fast tests from slow ones, finding the slowest tests, and a CI configuration that fails the build when it should.

## How the day works

Each module has a short video and a hands-on exercise. Watch the video, then write the code yourself in the exercise. The first video is about 8 minutes. Most of the day is you at the keyboard.

You'll build tests for one small example service across all six modules, so each module builds on the last.

## Start here

Begin with [Module 1: Your first test](module-1-narration.md).
