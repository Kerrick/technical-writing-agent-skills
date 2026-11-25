# Moving detailed design out of an ADR

Read this when an ADR is long, holds more than one decision, reads like a specification, or no longer passes the test in step 1 of SKILL.md.

1. **List every decision in it,** and apply step 1's test to each. Often one passes, and sometimes none. The rest is detailed design.
2. **Group the detailed design by subject** into design documents, each with one purpose. Use the documents the repository already has for those subjects before making new ones. Write each as a plain specification of how things are now. Leave out the history: how the team got there, trial runs and their IDs, old version numbers. Git keeps those.
3. **Keep the ADR for the decision that passes,** under its number, shortened to that decision. Keep every option, reason, and consequence that belongs to it, in the words of the old text. Add none. Fix a title that is a topic, so that it states the decision. Write a second ADR, with the next number, only for a second decision that passes. When none passes, delete the ADR.
4. **Rewrite every citation that no longer points at the right place,** in code and docs, in the same change. A citation for how something works now has the design document's path. A citation for why keeps the ADR's number. Update the index.
5. **Map every section of the old ADR to its new home** in your report, including what you dropped and why, so a reviewer can see nothing was lost.
