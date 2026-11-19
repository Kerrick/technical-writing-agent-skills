I wrote the landing page and the module 1 narration script, but I couldn't run pytest, so the video script's pytest output is unchecked. The sandbox needed approval to install pytest, so I never got it installed. I ran the arithmetic in `orders.py` with plain Python: `order_total([1250, 799])` gives 2049, `apply_discount(2000, 10)` gives 1800, and `apply_discount(1999, 10)` gives 1799. The pytest output the narration describes (the dots, `3 passed`, the `E assert 1799 == 1800` line, the `FAILED` summary line) is illustrative. The script's recording notes say to do a clean-machine run first and match the highlights to what your pytest version prints.

**What I assumed**
- **Reader:** backend developers who can write Python functions. Some know `unittest`, and a few have never seen a fixture.
- **Module list:** you didn't give me one, so I made it up. The six modules are:
  1. First test
  2. Parametrize and `pytest.raises`
  3. Fixtures
  4. Fakes and `monkeypatch`
  5. HTTP endpoint testing
  6. Suite organization and CI

  Please swap in your real list.
- **Running example:** a small orders service with prices in cents, used in both files.

**Placeholders you need to fill in**
- The landing page has bracketed placeholders for date, location, instructor, per-module times, registration link and price, and the pytest/Python versions.
- It also has a bracketed placeholder for the web framework in module 5. The page promises a starter repo and setup check a week ahead, so confirm that or cut it.

**The video script**
- The script is a two-column screen/narration table with timestamps and runs about 1,050 spoken words, close to 8 minutes. I didn't time it by reading it aloud.
- The learner writes three tests, runs them, and predicts then reads one deliberate failure. The failure comes from the code's `//` rounding down, so the test's expectation is what's wrong.

Files are in `outputs/`:
- `course-landing-page.md`
- `module-1-video-script.md`