I wrote both files, but I couldn't run pytest here. The sandbox blocked installing it, so the pytest transcripts in the script are unverified.

- **Verified:** I ran `invoice_total` and the passing test with plain Python, and they work (the sample invoice totals 27.50).
- **Unverified:** the pass/fail/`collected 0 items` output, the `>`/`E` failure lines, and the claim that a file named `invoices_tests.py` isn't collected. Please run the module once in a clean venv before recording.

Files are in `outputs/`:
- `index.md` is the landing page. It has the six modules, who the workshop is for, a unittest-to-pytest map, what isn't covered, and where to get help.
- `module-1-video-script.md` is the narration script, with timestamps and on-screen cues. The narration is roughly 1,000 words, which should run close to 8 minutes. The module covers:
  - setup;
  - a function to test (`invoice_total`);
  - the same test in `unittest` and then in pytest;
  - a prediction pause before the first run;
  - a function renamed so it silently isn't collected;
  - a deliberate failure, read via the `>` and `E` lines;
  - the shortcuts the example takes, and a closing that points to Module 2.

Calls for you to confirm:
1. **The six modules are my invention.** You didn't give a syllabus. I chose: first test, fixtures, parametrization, isolating external services, service boundaries (HTTP and database), and organizing the suite for CI. Swap in your real list; the unittest map and the closing line of Module 1 refer to modules 2 and 3.
2. **Install isn't pinned.** I couldn't check a pytest version, so the script runs `pip install pytest` with no version. Because the workshop is written for one fixed day, you'll probably want to pin the version you rehearse with.
3. **Help channel.** I used "ask the instructor in the room", since I had no other channel. I also left out dates, venue and instructor name.
4. **Module 1 links.** Only the Module 1 entry links anywhere, to its script. The other modules don't exist yet.