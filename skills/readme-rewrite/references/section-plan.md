# Section plan

A common order for open-source projects. Drop sections that do not apply. Keep the order for those that do.

1. **Title and badges.** Name, one-line description, then badges for version, CI status, license, and docs. Use badges that update automatically instead of sentences like "the latest release is X".
2. **Introduction.** What it is, who it is for, what problem it solves, in a short paragraph. Then a few lines on how it compares with alternatives the reader already knows, with each alternative linked. Describe the project by what it is. Do not call it "a way to ship X" if it ships things made with X.
3. **A first example.** A small, real, runnable one with its output. State its size or content so the reader can judge ("a three-line script that prints a greeting").
4. **Compatibility.** Supported platforms, language versions, and requirements, in a table. State caveats here: "you need a Linux machine to build for Linux".
5. **Installation.** The commands, run and verified.
6. **Usage.** The path from first run to a release or deployment, in order. Name each file or option the first time it appears: what it is, where it goes, whether it is optional. Show an example with real options.
7. **Documentation.** Links to the API reference, guides, and changelog, each with a phrase saying what it holds.
8. **Reporting problems.** Where to open issues, and what to include. State if pull requests are not accepted.
9. **Contributing.** One or two sentences and a link to CONTRIBUTING.
10. **License.** The license, and what it means for people who use the project to build work, if that is a likely question. Verify the answer against the license text and ask the maintainer if unclear.
11. **AI disclosure.** See ai-provenance.md.

Do not include: a status log, a roadmap of internal stories, architecture records, release procedures, or test-gate descriptions.
