# Review checklist

Derived from line-by-line maintainer feedback on a first draft, generalized. Run every item.

Audience
- [ ] Is every section for the reader who might use the project? A section on CI internals, decision records, or release gates is for maintainers. Move it or retitle and recast it as user-facing (for example, Compatibility).
- [ ] Does any sentence tell readers to create something they already have?
- [ ] Is there any internal citation (ADR, plan, decision number)? Remove it.
- [ ] Would a reader skip a section because the heading looks internal?

Truth
- [ ] Is each command one you ran? Does each claim match the code?
- [ ] Is anything listed that the code does not yet do? Remove or mark it as not available.
- [ ] Does any sentence say the opposite of what the code or license says? (For example, a license that does or does not reach work built with the tool.) Verify with the license text. If it stays unclear, ask the maintainer and write nothing misleading in the meantime.
- [ ] Does any wording state a current state as a policy, or a policy as a permanent fact? Keep "not yet available", "not accepted", and "never will" apart.
- [ ] Do "first", "only", "best" claims hold? "The first app built with X" can read as "the first anyone built".
- [ ] Does any sentence mislead about who installs or does what?

Clarity
- [ ] Does every file, option, or tool get one line saying what it is, where it goes, and whether it is optional?
- [ ] Is every size, speed, or scale claim backed by a number or example?
- [ ] Is every sentence free of non-agentic subjects ("the build takes", "the gem asks")?
- [ ] Does the draft describe what the project is, in the reader's terms?
- [ ] Are there confusing constructions that need two reads? Rewrite them in plain order: actor, action, object.
- [ ] Do readers learn whether it is for them from the first screen?
- [ ] Do comparison sections name the alternatives, link them, and state the differences as facts?

Structure
- [ ] Do the three purposes (marketing, onboarding, index) each have a home?
- [ ] Are caveats in the caveats section, not mixed into "who it is for"?
- [ ] Is status short and about users, with a badge instead of a version sentence?
- [ ] Is Contributing a pointer to CONTRIBUTING?
- [ ] Is the license section clear to someone who will build work with the project?
- [ ] Does the AI disclosure follow the house pattern?

Process
- [ ] Did you read the old README fully (edit mode) or deliberately not (whole-cloth mode)?
- [ ] Did you edit the file at its real path, so the maintainer can review it where they look?
- [ ] Did you do the rewrite yourself with the full list of principles in hand, if you used a helper? Do not hand README writing to a weaker model without the principles. If a helper must draft, give it the reading list and audience, and review the result against this checklist.
