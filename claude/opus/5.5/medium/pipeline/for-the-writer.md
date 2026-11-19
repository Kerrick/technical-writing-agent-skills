
**Rules that well-run documentation breaks by mistake.** Each of these is broken in several mature documentation sets, and each time it's an error, not a design choice. Check these hardest in every draft:

- Run every example in order from the page's starting state, and make the shown output match what the code produces.
- Check every name, version, cross-reference, and factual claim against its source, and keep facts consistent across pages.
- Don't make statements that depend on when they were written. They become false later, and readers can't tell when.

**Rules that mature documentation breaks on purpose.** Treat these as open to correction:

- **Lesson endings.** In a sequence of lessons, a fixed, brief closing on every lesson works. It can be one sentence naming what the reader should now be comfortable with and pointing to the next lesson, or a short recap of the concepts covered followed by a preview of the next one. A list of skills is one way to end, not the only way. What matters is that the closing is short, the same on every lesson, and points forward.
- **Version pinning.** When the documentation is versioned with each release, or always describes the current release, installing the newest release without a pin is a sound choice: the reader gets the version the page was written for. Add a version constraint where a minimum version is actually required.

**Rules that hold as written.** These were broken only here and there, with nothing in the sources to defend the breakage. Keep them as they are:

- Don't call a task easy or obvious.
- Don't use promotional adjectives.
- State objectives as actions the reader can perform and check.
- Open with the outcome or the answer, not an announcement of what the page will do.
- In a deprecation note, give what is deprecated, since when, its replacement, and when it will be removed.

**Correction rules whose baseline turned out not to be broken in practice.** The corrected versions of these three still stand. The breakages were scattered, so they don't justify warning that the rule is often broken:

- One primary job per page, with other material only in short, labeled sections.
- Realistic names for real use, and neutral names only for pure mechanism.
- One term per concept, with any second name declared once.

**A note on sample data.** Keeping a tutorial's setup data in a separate file that ships with the material, and telling the reader on the page where it is, doesn't break the rule to run every example. The page still has to say where the data is, and the data has to produce the output shown.
