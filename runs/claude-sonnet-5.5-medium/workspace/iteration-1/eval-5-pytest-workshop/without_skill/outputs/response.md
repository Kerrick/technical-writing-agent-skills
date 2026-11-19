I wrote both files to `outputs/`. I didn't run the example code or time the narration.

- **`outputs/index.md`** is the landing page. It covers who the workshop is for, prerequisites, learning outcomes, the six modules and how the day works. It links to the Module 1 script.
- **`outputs/module-1-narration.md`** is the script for the Module 1 video. Narration is plain text, and screen directions and code are marked separately. The video builds a small `apply_discount()` function and its first test. It runs `pytest`, breaks the test on purpose to read the failure, then adds a `pytest.raises` test.

My estimate of the narration is about 900 words, which fits roughly 8 minutes once on-screen typing and pauses are added. Time a read-through before recording.

- **The six modules are my own outline.** You didn't give me a syllabus, so I made one up:
  1. First test
  2. Fixtures
  3. Parametrization and organization
  4. Mocks and monkeypatch
  5. Testing APIs and databases
  6. Running the suite in CI

  If your real syllabus differs, the landing page and the Module 2 hand-off at the end of the script need editing.
- **The landing page has no logistics.** There's no date, venue, price, instructor or registration link, because I didn't have them.
- **The Module 1 exercise doesn't exist yet.** The script's closing section sends learners to it, so you'll need to write it.
- **The failure output is untested.** The `assert 80.0 == 85` line is what I expect pytest to show, so check it when you record.