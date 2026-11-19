# Programming books and video/screencast scripts

Read this for long-form or spoken formats. Everything in SKILL.md and [teaching.md](teaching.md) still applies; this file adds what changes with length and medium.

## Programming books

### Plan the whole book first

1. **Reader promise:** one sentence: "After this book, a [specific reader] can [specific capability]." Every chapter must serve it; cut chapters that don't.
2. **Reader profile:** prior knowledge, why they're reading, how they'll read (front to back, or dip in). Write down what you will *not* assume or cover.
3. **Spine:** a running project or a progression of increasingly demanding ones. Each chapter adds capability and ends with something that works.
4. **Outline with learning objectives per chapter,** dependency-ordered. Check no chapter uses a concept before its introduction; keep a concept-introduction table (concept → chapter) and update it as you draft.
5. **Parts:** group chapters into parts with a clear arc (foundations → building → production, for example). Use appendices for setup, reference, and exercise solutions.

### Chapter shape

- Opening hook: a problem the reader cares about, shown concretely, then what they'll be able to do after the chapter.
- Body: sections of roughly equal weight, each introducing one idea with example → explanation → variation.
- Mid-chapter checkpoints and a "try it" that applies the idea.
- Closing: summary of key points (bulleted, short), common pitfalls, exercises, and a bridge to the next chapter.
- Sidebars for tangents, history, and platform notes. Use them sparingly; each interrupts the flow.

### Code in books

- **The book's code lives in a repo that CI builds and tests** against pinned versions, with one directory or tag per chapter and per checkpoint. Include code in the manuscript by *extraction from the tested files* (snippet markers or include directives) so prose and tests can't drift. Never paste untested code.
- Show only the relevant lines in the text, with `...` elisions and line-level callouts; give file path above each listing so readers know where it belongs. Consistent listing numbering lets the prose refer to them.
- Use diffs or highlighting when modifying an existing listing.
- Limit listing width to what the print or e-book column holds (about 70-80 characters) so there is no wrapping; check at actual page size.
- Pick the version policy up front: pin versions and say so, or write version-independent concepts and isolate version-specific details to marked boxes, because books outlive releases.
- Provide a "stuck? start here" path: the repo's chapter starting point and a known-good end state.

### Manuscript mechanics

- Choose a toolchain that builds from plain text (AsciiDoc, Markdown+Pandoc, LaTeX, or the publisher's system), version-controlled, with a one-command build to every target format (PDF, EPUB, HTML). Test EPUB and e-reader rendering early; code and wide tables break there.
- Maintain a style sheet: terminology, spelling, code font rules, capitalization, how commands and file names are formatted, tone, person, and tense. Keep a glossary and an index plan (mark index terms as you write).
- Cross-references use generated links, not manual chapter numbers, since chapters move.
- Keep a changelog and an errata page for readers; fix and republish.
- Draft a chapter, then run the entire code and exercises from scratch on a clean machine; then do a "cold read" for flow. Get technical review from someone at the target level, who finds confusion, and one from an expert, who finds errors.
- Permissions and licensing: track the license for every figure, dataset, and borrowed code; credit sources.

### Voice and pacing

- Pick a consistent voice (typically a friendly colleague, "we" for building together, "you" for exercises). Use humor lightly; it dates and doesn't translate.
- Variety in rhythm: alternate exposition, code, figures, and exercises; avoid more than a page of unbroken prose or listing.
- Explain the "why" before a technique's mechanics so the reader can judge when not to use it. Show wrong or naive approaches first when they teach why the better approach exists.
- Foreshadow and recall: "we'll return to this in Chapter 9" and "remember the cache from Chapter 4" build coherence and give spaced practice.

## Video and screencast scripts

A script is for the ear and the eye. People can't re-read a sentence in a video; they can only rewind.

### Plan the series

- One video = one outcome, usually 5-12 minutes. Split longer ones; a series gives each video its own title and thumbnail and clearer searchability. Make titles state the outcome or question ("Add authentication to an Express app"), the way viewers search.
- For a series, write a series outline with each episode's objective, prerequisites (episode links), and end state; carry a running project with a repo and a tag per episode.
- Hook within the first 15 seconds: the result they'll get, shown, then a one-line roadmap. Skip long intros, logos, and "welcome back to my channel" stalling.

### Script format

Use two columns (or alternating lines) so narration and screen action stay aligned:

```
| SCREEN / ACTION                                  | NARRATION                                                     |
| ------------------------------------------------ | ------------------------------------------------------------- |
| Terminal, empty dir. Type `npm init -y`.         | Start with an empty folder and create a new project.          |
| Show package.json created; highlight "name".     | That gives us a package.json. We'll add dependencies next.    |
```

Include for each segment: the exact commands and keystrokes, file and line to show, zoom or highlight cues, and any pause for output to appear. Mark timing estimates. Keep a separate list of assets (slides, diagrams, starter repo).

### Writing for the ear

- Short sentences, plain words, contractions, one idea each. Read aloud while writing; if you stumble, rewrite.
- Say what's on screen before the viewer needs to find it: "In the top right, the run button." Don't narrate every keystroke; narrate intent. Pause during typing or let the viewer watch silently for a beat when something is rendering.
- Repeat the key idea in a different form: state it, show it, restate in one line. Spoken text needs more redundancy than written text.
- Don't read code aloud symbol by symbol; describe what it does and let the visuals carry syntax. For code that matters, highlight lines in sync with narration.
- Signpost: "Two steps left." "That's the setup; now the interesting part." Recap at the end in one short list and point to the next video and the written companion.
- Spell out numbers, versions, and URLs sparingly; put long strings in the description or on-screen text and a written companion.

### Screen and recording practice

- Large font (editor 18-24pt, terminal likewise), high contrast theme, hide notifications and unrelated tabs, 1080p minimum, window sized for the recording, cursor easy to follow, zoom into small UI.
- Rehearse the full run on a clean environment; record only after the steps work. Script mistakes and re-record the section, or cut; don't leave on-camera debugging unless it's the lesson, and then choose it on purpose.
- Prefer prepared checkpoints: paste long code from a snippet file, or use a tool that types it, so the video doesn't spend minutes watching typing. Show the typing only where the typing is the teaching.
- Audio matters more than video: use a decent mic, a quiet room, consistent level; use captions or a transcript (accessibility, search, non-native viewers). Provide chapters/timestamps.
- Don't rely on color alone or on tiny text; check that important details are readable on a phone.

### Videos age fast

- Avoid showing version numbers or dated UI in thumbnails and titles unless needed; pin the version in the first seconds or description.
- Keep text companions (the repo and a written walkthrough) as the source of truth, since text can be updated and videos can't. Pinned comment or description notes correct errors and link to updates.
- Plan which segments are most likely to change and keep them modular so only they need re-recording.

## Conference talks, workshops, and live coding (brief)

- Workshop: ship a repo and setup check before the session; exercises with timed segments and checkpoints; helpers for stuck learners; slides thin, hands-on thick.
- Talk: one message, a story arc, demos pre-recorded or heavily rehearsed with a fallback, slides readable from the back of the room.
