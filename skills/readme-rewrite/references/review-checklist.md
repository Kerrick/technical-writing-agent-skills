# Review checklist

Derived from line-by-line maintainer feedback on a first draft, generalized. Run every item.

Audience
- [ ] Is every section for the reader who might use the project? A section on CI internals, decision records, or release gates is for maintainers. Move it to contributor docs, and keep in Compatibility only the platforms and versions the reader can use.
- [ ] Do you tell readers anywhere to create something they already have?
- [ ] Is there any internal citation (ADR, plan, decision number)? Remove it.
- [ ] Would a reader skip a section because the heading looks internal?

Truth
- [ ] Is each command one you ran? Does each claim match the code?
- [ ] Is any sentence proof narration, apologizing ("untested", "not yet through review") or boasting ("CI runs every example on every change", a test count)? Cut it or move it to contributor docs, and keep only the fact it implies for the reader.
- [ ] Is anything listed that the code does not yet do? Remove or mark it as not available.
- [ ] Does any sentence say the opposite of what the code or license says? (For example, a license that does or does not cover work built with the tool.) Verify with the license text. If it stays unclear, ask the maintainer and write nothing misleading in the meantime.
- [ ] Does any wording state a current state as a policy, or a policy as a permanent fact? Keep "not yet available", "not accepted", and "never will" apart.
- [ ] Do "first", "only", "best" claims hold? "The first app built with X" can read as "the first anyone built".
- [ ] Is any sentence misleading about who installs or does what?
- [ ] If a package registry also shows this README, do its images and links still work there?

Clarity
- [ ] Does every file, option, or tool get one line saying what it is, where it goes, and whether it is optional?
- [ ] Is every size, speed, or scale claim backed by a number or example?
- [ ] Is every sentence free of non-agentic subjects ("the lockfile decides", "the gem asks")?
- [ ] Does the draft describe what the project is, in the reader's terms?
- [ ] Are there confusing constructions that need two reads? Rewrite them in plain order: actor, action, object.
- [ ] Do readers learn whether it is for them from the first screen?
- [ ] In comparison sections, are the alternatives named and linked, and the differences stated as facts?

Structure
- [ ] Do the three purposes (marketing, onboarding, index) each have a home?
- [ ] Are caveats in the caveats section, not mixed into "who it is for"?
- [ ] Is status short and about users, with a badge instead of a version sentence?
- [ ] Is Contributing a pointer to CONTRIBUTING?
- [ ] Did everything you took out of the README, other than what you confirmed is false, land somewhere the repository already uses or beside what it describes, with a link from the README?
- [ ] Is the license section clear to someone who will build work with the project?
- [ ] Does the AI disclosure match the house pattern?

Process
- [ ] Did you keep to your mode: no reading the old README in any form before the draft was done (draft blind, from scratch), or reading every README-like file in full first (edit mode)?
- [ ] In draft blind, then reconcile: did you check everything the old README said that the draft didn't, and keep what passed?
- [ ] Did you edit the file at its real path, so the maintainer can review it where they look?
- [ ] If you used a helper, did you do the rewrite yourself with this skill in hand? Don't hand README writing to a weaker model without it. If a helper must draft, give it this skill and the audience, and review the result against this checklist.
