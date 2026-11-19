I wrote both files and saved them in `outputs/`.

**1. `outputs/course-landing-page.md`**
- It says who the course is for, and speaks directly to people coming from `unittest` and people who have never written a fixture. It also tells them their existing `unittest` tests will still run under pytest.
- It lists the six modules, each with what they'll do and what they'll leave with:
  1. Your first test
  2. Assertions that tell you what went wrong
  3. Fixtures
  4. Parametrize
  5. Isolating outside dependencies
  6. Testing the service end to end
- A "Before the workshop" section covers setup: Python 3.10 or newer, an editor, a terminal, and the cloned repo.

**2. `outputs/module-1-narration-script.md`**
- The script has eight timed sections, each with **ON SCREEN** cues and **NARRATION** to read aloud. There are about 1,150 spoken words, which comes to roughly 8 minutes with pauses for typing.
- The story: install pytest in a virtual environment, then test a small `apply_discount(price_cents, percent)` function. Viewers see the same test written in pytest and in `unittest` side by side, run it, and learn how pytest finds tests. Then the presenter deletes the subtraction to introduce a realistic bug, and walks through the failure output line by line.
- It ends with a recap and an exercise (test 0% and 100% discounts) that leads into Module 2. Production notes at the end include the exercise answers for instructors.

**Things to check:**
- **I couldn't run pytest here**, so the terminal output in the script comes from what I know of pytest's format, not from a real run. The script asks the presenter to rehearse and use their real output. Version numbers and timings will be different.
- **I didn't make up any logistics.** The landing page has no date, location, price, instructor names, or repo URL; it only says the repo link comes in the welcome email. Add those details.
- **Modules 5 and 6 assume things about the workshop project.** They assume it calls an outside HTTP API and has a database. Module 6 says "the framework's test client" without naming FastAPI or Flask. Adjust these to match your actual project.