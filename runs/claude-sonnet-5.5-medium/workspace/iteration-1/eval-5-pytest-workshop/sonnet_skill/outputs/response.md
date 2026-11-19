I wrote both files, but I couldn't run any of the pytest commands, so none of the script's pytest output has been checked.

pytest isn't installed here, and the sandbox blocked `pip install`. I did run the example function on its own: `order_total_cents([1000, 2500], 10)` returns 3850. The script describes the pass and fail output in words instead of pasting it. Please run the module once in a clean virtual environment before you record.

Files are in `outputs/`:
- `course-landing-page.md` has the audience, prerequisites, the six-module table with a short description of each, and routes through the day for different backgrounds.
- `module-1-video-script.md` is about 1,150 words, which should run about 8 minutes. It covers:
  - installing pytest in a virtual environment;
  - writing and running one test for a small pricing function;
  - breaking the test on purpose and reading the failure report;
  - a recap and an exercise.

Decisions I made without you:
- **Module list:** you didn't give one, so I invented it. The six modules are:
  1. first test
  2. assertions and `pytest.raises`
  3. fixtures
  4. parametrize
  5. `monkeypatch` and mocks
  6. testing an HTTP service

  Swap in your real titles if they differ. The cross-references are in both files.
- **Example domain:** the module 1 example is a pricing function that works in cents. I assumed modules 2 and 3 reuse it and modules 4 to 6 use an HTTP service.
- **Left out:** dates, venue, instructor and registration, since I had no facts for them.