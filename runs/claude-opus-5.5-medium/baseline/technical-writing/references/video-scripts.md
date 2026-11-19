# Video and screencast scripts

A tutorial video is a tutorial that the viewer can't skim, search, or copy from. Script it so each of those losses is compensated.

## Plan the series like a book

Design the series backward from end capabilities, as in [books and courses](books.md). Each episode delivers one outcome. Shorter is better: in a large study of course videos (Guo et al., 2014), engagement dropped off sharply after about six minutes. Split a long topic into episodes rather than recording one long video.

## Script format

Use a two-column script so visuals and narration are planned together:

```markdown
# Episode 3: Add authentication

Outcome: The viewer can protect a route so only signed-in users reach it.
Starting state: tag `ep02-end` of the companion repo.
Target length: 5:00 (about 650 words of narration)

| # | Visual | Narration |
| - | - | - |
| 1 | Browser: the finished app redirecting to a sign-in page | "By the end of this video, anyone who isn't signed in gets sent here." |
| 2 | Editor: `routes.rb`, zoomed to the `resources :posts` line | "Last time we built posts. Right now, anyone can delete them." |
| 3 | Terminal: run `bin/rails generate authentication`; hold on output 2s | "Rails can generate the pieces we need. Run this." |
| ... | | |
| 12 | Title card: "Next: password resets" | "Next time, we'll let users reset a forgotten password." |
```

Read the narration aloud with a timer before recording. Narration typically runs 130–160 words per minute; screencasts with typing and pauses run slower, so budget about 120–130.

## Write for the ear

- Short sentences, one idea each. No parentheticals.
- Say symbols the way a speaker would, and say each the same way every time: "the dollar-sign prompt," "dot env file."
- No visual back-references the viewer can't see: "as shown above" doesn't exist in video. Say "the command we ran a minute ago."
- Repeat key terms more than you would in print. Listeners can't re-read.

## Visuals

- **Open with the result** in the first 10–15 seconds, then say what they'll build.
- **Don't put the narration on screen.** Full sentences on screen while you say them compete for the same attention. On-screen text is for code, short labels, and keywords.
- **Point at what you're talking about.** Zoom, highlight, or move the cursor to the line being discussed, and put labels next to the thing they name.
- **Hold on results.** Leave output on screen for two seconds or more after it appears.
- **Cut decoration.** Background music under speech, animated transitions, and busy desktops cost attention and teach nothing.

## Screencast setup

- Record at 1080p or higher, with the editor and terminal font large enough to read on a phone. Zoom in further than feels natural.
- Use a clean profile: hide notifications, bookmarks, personal tabs, and shell prompts with personal paths or hostnames.
- Never type a real secret on screen. Use placeholders or load them from a file off screen.
- Keep window size and layout the same across all episodes.
- Pre-type or cut long boilerplate; type the lines that teach.
- A real mistake and its fix can teach a lot. Keep one when it's instructive; cut fumbling.

## Episode structure

1. Hook: the result.
2. One-line recap of where the last episode left off, and the starting state.
3. The work, in subgoal chunks. Each chunk ends with something visibly working.
4. Recap of what the viewer can now do.
5. What's next.

## Companion material

Publish with each episode: captions edited from the script (auto-captions mangle code), a transcript, chapter timestamps, a link to the code at that episode's start and end, and the commands shown, as copyable text.
