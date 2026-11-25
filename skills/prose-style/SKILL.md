---
name: prose-style
description: >-
  Use before writing any English prose a person or agent will read: replies
  in chat, documentation, READMEs, ADRs, Agent Skills, commit messages, code
  comments, doc comments, issue and pull-request text, and error messages.
  Use it when reviewing or revising such prose, when someone asks what's wrong
  with a sentence or says it "has the problem", and whenever you are about to
  write that a file, setting, record, document, or screen acts, decides,
  wants, or speaks.
  Agents using the readme-rewrite, developer-docs, adr, or skill-authoring
  skills load this one for sentence-level work. Not for a document's
  structure, sections, or required contents; use those skills.
license: CC0-1.0
metadata:
  author: Kerrick Long
  version: "1.0.0"
---

# Prose style

You already write clear English. These rules cover the sentence-level faults you make anyway, most of all giving agency to things that can't act, and they apply to every kind of prose, chat replies included. Where a rule here conflicts with advice you would usually follow, follow the rule here.

## Every sentence

- **Name the actor.** Make a person, the reader, or a program the subject of a verb of doing, deciding, wanting, or speaking. Before you draft or review anything longer than a short reply, read [references/agency.md](references/agency.md), which covers the hard cases.
- **Write American English:** color, gray, canceled, "in favor of", the serial comma.
- **Use plain words.** Short sentences, specific nouns, concrete numbers, versions, and commands. Write "to", not "in order to"; "use", not "utilize"; "before", not "prior to". Name what happens instead of "allows you to", "enables", "provides support for", "functionality", or "capability".
- **Write "you" for the reader.** Give an instruction in the imperative ("Run `make`"), not as "you must" or "you need to". Keep "needs" for a real necessity and "requires you to" for a rule someone imposes.
- **Use the tense of the thing.** Describe what code does in the present tense, in the third person ("Calculates the total"). Describe an event that happened in the past tense ("The trial found"). Describe what a text says in the present tense ("The study finds").
- **State facts as they are now:** "X is MIT-licensed", not "X moved to MIT in 0.8.0". Leave out words that date the sentence: "new", "recently", "currently", "as of this writing".
- **Use one term per concept.** Define it on first use, and never vary it for elegance.
- **Pick neutral words for a trade-off.** With "warm" and "cold", or "clean" and "dirty", one side sounds better. Write "reuse" and "empty" when neither is better.
- **Check a word's connotations as well as its meaning.** "Lists the price" means the list price, which is wrong for a discounted item; "owner" assumes ownership, which is wrong for anyone else at the keyboard.
- **Check a metaphor's literal sense.** In "the line runs through the subject", a reader sees a strikethrough. Prefer the plain statement: "the difference is in the subject".
- **Use the complement each verb goes with.** "Says" goes with a clause ("says the price is $40"); "shows", "lists", and "gives" go with an object and "as" ("shows the price as $40").
- **Read dialect senses, and write the standard one.** In Southern American English, "wants" can mean "needs" ("the car wants washing"). Write the standard sense.
- **Make every sentence add something** the previous one didn't.
- **Headings:** a plain noun phrase the reader would search for, never a clever one.
- **Quotes:** straight quotes in source files and Markdown, never curly ones.

## What a sentence claims

- **State verified facts plainly.** Before you qualify, shrink, or cut a sentence, name the specific false or unverified fact it states. If you can't name one, it isn't an overclaim, so leave it as written. A statement of what something is for, or what it does, is not an overclaim. Never attach how narrow the proof was ("tested with", "in our testing", "as far as we know", "should work").
- **Don't narrate the proof.** A sentence about how far a project's own testing has got either apologizes ("untested", "not yet tried on Windows") or boasts ("CI runs every example on every change", a test count). Neither says what the reader can do. Cut it, and keep only the fact it implies, such as a platform or a minimum version. A measured result the reader can weigh, such as a benchmark with its numbers, is evidence, not proof narration.
- **Check "first", "only", and "best".** "The first app built with X" can read as "the first anyone built".
- **State a correction as the right rule itself,** not as "unlike the usual advice".

## Banned patterns

Each has its fix.

- **Filler "own":** "the runtime's own libraries". Delete "own", or name the thing.
- **Announced honesty:** "honestly", "frankly", "to be clear", "it's worth noting". Delete it and state the fact.
- **"The X part", "the X bit":** "the tricky part is paths" becomes "paths are tricky because …".
- **Em-dash asides:** use a period, a comma, or parentheses. Two in a page are too many.
- **"Not X but Y", "it's not just X, it's Y":** state Y.
- **Rhythm devices:** a triplet, or a run of short parallel sentences, written for its cadence. Keep only the items that carry meaning.
- **Vague size or speed words:** "small", "fast", "lightweight", "a lone script". Give a number or an example.
- **Stock openers and closers:** "In today's world", "Whether you're … or …", "Happy shipping".
- **Your private shorthand:** words from your conversation used as metaphors, such as "deeper", "forward", "sideways", "upstream".
- **Hedge stacks:** "might possibly", "in some cases generally". Say when, or leave it out.
- **Self-praise:** "powerful", "seamless", "robust", "blazing". Show evidence instead.

## Procedure

1. Read [references/agency.md](references/agency.md) before drafting or reviewing anything longer than a short reply.
2. Draft by the rules above.
3. For a file, run `uv run scripts/hunt.py FILE…` from this skill's directory (or `python3 scripts/hunt.py`, with Python 3.11 or later). It prints `FILE:LINE: [rule] match` for each candidate and exits 1 when it finds any. A hit is a question, not a verdict: fix the sentence or defend it.
4. Reread for agency the script can't see: every subject, every possessive, every "by" phrase, every noun or adjective that gives a thing a mind or an act.
5. When someone asks what's wrong with a sentence, or asks for a review, say what's wrong and why, sentence by sentence. Give a rewritten version only when asked, and change nothing unless asked.

## Gotchas

- Fixing a sentence that was right. "The section lists four options" is correct: listing describes what the section contains. Rewriting it to "Under that section are four options" makes it worse.
- Making a file the actor for what the program reading it does: "the crontab runs the backup", "the `.gitignore` excludes build output", "the MX record routes mail". Cron, Git, and the sending mail server act.
- "Wants you to" for something you can't skip. "The app wants you to update before you can log in" describes a gate; write "you have to update before you can log in".
- Hiding false agency in a relative clause, "the bedtime that the settings name", or in a possessive, "the manifest declares its dependencies" (the app has them).
- Writing "the lockfile" with nothing for "the" to point at. "`Gemfile.lock` pins Rails at 8.1" and "a lockfile can pin Rails at 8.1" are correct; "the lockfile pins Rails at 8.1" isn't.
- Trusting the idiom of a field you or the writer know well. "The style sheet hides the sidebar" feels right to someone who writes CSS; the browser hides it. Push back hardest there.
- Giving agency to words while writing about words: "'says' takes a clause", "a relative clause hides". Write "'says' goes with a clause".
- Breaking these rules in your own prose: in replies in chat, in commit messages, and in a rule written to ban the fault. "The writer's own idiom" has filler "own", and "the line runs through the subject" is a misleading metaphor.
