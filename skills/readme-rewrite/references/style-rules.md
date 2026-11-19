# Style rules

## Banned patterns and how to fix them

- **Filler "own".** "The runtime's own libraries", "Rake's own tasks". Delete "own" or name the thing: "the libraries in the runtime".
- **"honest", "honestly", "frankly", "to be clear", "it's worth noting".** Delete. State the fact.
- **"The X part", "the X bit".** "The tricky part is paths." Write: "Paths are tricky because ..."
- **Agency given to non-agentic nouns.** Files, sections, lockfiles, versions, builds, and gems do not decide, ask, take, want, or know. Name the person or program that acts.
- **Em-dash asides.** Use a period, a comma, or parentheses. Two or more per page is too many.
- **"not X but Y" and "it's not just X, it's Y".** State Y.
- **Clever or abstract headings.** Use a plain noun phrase the reader would search for.
- **Triplet lists for rhythm.** Keep the items that carry meaning.
- **Vague size or speed words.** "Small", "fast", "lightweight", "a lone script". Give a number or an example.
- **Stock openers and closers.** "In today's world", "Whether you are ... or ...", "Happy shipping".
- **Your private shorthand.** Words like "deeper", "forward", "sideways", "upstream" used as metaphors for links or flow.
- **Hedge stacks.** "might possibly", "in some cases generally". Say when, or leave it out.
- **Proof hedging.** "Tested with Claude Code", "in our testing", "as far as we know", "should work". Before you qualify, shrink, or cut a sentence, name the false or unverified fact it states. If you can't, it isn't an overclaim: leave it as written. A statement of what something is for, or what it does, is not an overclaim.
- **Self-praise.** "Powerful", "seamless", "robust", "blazing". Show evidence.
- **Internal citations.** "(see decision 5)", "(ADR 10)" in a user-facing README.

## Procedure to hunt for them

After drafting, run `uv run scripts/hunt.py <README>`. It searches the prose (not code) for every pattern above and prints each hit with its line. For each hit, ask: who acts here? Fix or defend. If you add a pattern to this list, add it to the script too. Then read the headings alone, in order, as a list. They should tell the story and be plain.

## Before and after

Non-agentic noun:

> Before: The lockfile decides which versions ship, and building takes the rest from your project.
> After: The build uses the versions in your lockfile and copies the rest of your project as it is.

Stock phrasing:

> Before: The packaging part is where Foo's own tooling really shines, honestly.
> After: Foo packages your project into one archive. A build of a ten-file project takes about four seconds on an M1 MacBook Air.

Section written for the wrong reader:

> Before: What CI checks on every push. Each job builds on its own runner (ADR 7).
> After: Compatibility. Foo builds for Linux, macOS, and Windows. Its tests run on all three for every change. Foo doesn't support cross-compiling, so you'll need to package your app on each operating system you want to support.

## Other rules

- Put the reader's goal before the mechanism. Lead with what they can do.
- Do not tell readers to create what they already have. Start from where the reader is. A reader of a packaging tool has a program already, so start from "In your project folder, run ...".
- Link a proper noun on its first use in each section. Link to the project's page, not a search.
- Use one term per thing. Do not alternate synonyms.
