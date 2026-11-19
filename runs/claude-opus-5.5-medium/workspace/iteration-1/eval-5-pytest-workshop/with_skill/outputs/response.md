I've written both files, but the pytest output in the script hasn't been run. Package installs were blocked in this session, so pytest couldn't be installed. Please do one run-through of the script with pytest 9.2.0 before you record.

- `outputs/index.md` is the landing page. It has a short summary, a "where to start" table, the six modules with a line on each, setup notes, and where to get help.
- `outputs/module-1-first-test-script.md` is the module 1 video script, in timed segments with on-screen notes and narration. The narration is about 1,130 words, which is roughly 8 minutes with pauses.

**What I did and didn't run.** I ran the plain-Python parts: `invoice_total` gives 48.58 at 8% tax, 49.48 at 10%, and 0.00 for an empty invoice. The `unittest` version passes. The pytest terminal output, including the failure message and the `-v` listing, is written from pytest's standard format. In the run-through, check three things in particular:
- the failure points at line 11;
- the `E` line reads `assert Decimal('49.48') == Decimal('48.58')`;
- pytest collects the `TestCase` class next to the plain test functions.

**What module 1 covers:**
- It starts with the `unittest` test they already know, then shows the plain `assert` version.
- Learners predict what pytest will print before the deliberate failure, and before the trap.
- The trap is a test whose name doesn't start with `test`: pytest silently skips it and still reports all green.
- It ends with a full checkpoint of the test file, an exercise with a way to check it, and a pointer to module 2.

**Decisions I made that you may want to change:**
- **Module lineup:**
  1. first test
  2. fixtures, assuming no prior fixture experience
  3. `parametrize`
  4. `pytest.raises` and error paths
  5. `monkeypatch`, `tmp_path` and mocks
  6. test layout, `pyproject.toml`, markers and CI

  Only module 1 links to a page.
- **Running example:** an invoicing function that uses `Decimal`. The landing page says it carries through all six modules, and module 1 says module 4 tests input validation and module 6 moves the tests into their own directory.
- **Pinned versions:** pytest 9.2.0, since the workshop is tested against one version. The landing page also says Python 3.10 or newer, which I took from pytest 9's supported versions from memory rather than checking it here.
- **Help:** "flag a facilitator in the room" is the only help channel, and also how learners report mistakes. Add a chat channel if you have one.
- **Recording:** the script's terminal blocks leave out pytest's machine-specific header lines, and a production note says so.