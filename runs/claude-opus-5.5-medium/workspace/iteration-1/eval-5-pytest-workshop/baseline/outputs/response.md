I've written both files. One limit up front: I couldn't run pytest. It isn't installed on this machine, and I didn't get approval to install it. The discount function's results are checked with plain Python: `apply_discount(5000, 10)` returns 4500 and `apply_discount(1999, 15)` returns 1699. But every block of pytest output in the script is my best guess at what pytest prints, and each one is marked `TODO(verify)`.

**`outputs/index.md`, the landing page**
- **Running project:** you add tests to a small orders service all day. Each module starts from a Git tag (`module-N-start`), so anyone who falls behind can check out the next tag and carry on.
- **Six modules:**
  1. Write and run your first test
  2. Share setup with fixtures
  3. Test many inputs with parametrize
  4. Replace slow and unpredictable dependencies
  5. Test an HTTP endpoint
  6. Choose which tests to run, locally and in CI
- **Module entries:** each one has a short description and a "You'll be able to…" line describing something attendees can do afterwards.
- **For `unittest` users:** the page says where pytest differs from `unittest`. Module 6 shows that pytest runs existing `unittest` test classes unchanged.
- **Other sections:** who it's for and who it isn't, prerequisites, setup to do before the day (with a hosted fallback), a schedule and conventions.

**`outputs/module-1-video-script.md`, the module 1 video**
- **Format:** a two-column table of what's on screen and what's said, plus production notes, the full code and output listings, and a list of material to publish alongside the video.
- **Flow:**
  - Opens on the finished, passing tests.
  - Shows the `unittest` version of the same test next to the pytest one.
  - Explains how pytest finds tests by their names.
  - Has viewers write a test with a wrong expected value on purpose (1700 instead of 1699). They read the failure report and decide whether the test or the code is wrong.
  - Ends with a prediction exercise for the lab, with the answer in a note for the lab facilitator.
- **Length:** about 7:15, not 8:00. The narration is about 730 words. I didn't pad it, because viewers stop watching in large numbers after about six minutes. The extra time can go to the lab.

**What you need to fill in or decide:**
- **Real output:** before recording, run each command from `module-1-start` and paste the real output in place of the guessed output.
- **One unconfirmed detail:** I believe the starter's `pyproject.toml` needs `pythonpath = ["."]`, or `import orders` fails with `ModuleNotFoundError`. That's unconfirmed and marked in the script.
- **Placeholders:** the repository URL, the pinned pytest version, the chat channel, the hosted environment URL, and the schedule times.
- **Companion repository:** the `orders-service` repo and its tags don't exist yet, and both files assume them.
- **Framework:** Module 5 assumes FastAPI. If your teams mostly use Flask or Django, swap the framework there.