# humanizer

A Claude Code skill that rewrites AI-sounding drafts into prose a person
would plausibly have written — and governs writing composed from scratch, so
the patterns never get generated in the first place.

Clone it, paste your draft, get a version without the machine's habits in it.

Built on [Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI Cleanup, with the false-positive guidance kept
intact. Full provenance in [SOURCES.md](SOURCES.md).

## Install

The directory name becomes the command, so clone into it directly:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Prajhan26/humanizer.git ~/.claude/skills/humanizer
```

Confirm it loaded:

```
/skills
```

`humanizer` should be listed. If it is not, run `/doctor`, or start with
`claude --debug` to surface YAML parse errors.

For one project instead of globally, clone into `.claude/skills/humanizer/`
in that repo.

## Use

Paste a draft after `/humanizer`, or describe the problem and let Claude load
the skill:

```
Humanize this: [paste text]
Does this sound like AI wrote it?
Rewrite this so it doesn't read like ChatGPT.
```

It also runs on writing that does not exist yet:

```
Write a post about [topic] — make it sound human
```

In that mode the catalog acts as a constraint on generation rather than a
cleanup pass, since models produce these patterns while composing, not only
while editing.

## Layout

```
humanizer/
├── SKILL.md      # the skill; loaded into context when invoked
├── reference.md  # full pattern catalog; loaded on demand
└── SOURCES.md    # provenance and adaptations
```

`SKILL.md` stays short deliberately. Once invoked, its content persists in
context for the rest of the session, so every line is a recurring cost. The
catalog lives in `reference.md` and loads only when a pattern needs judgment.

## What it does

Removes puffery, slop vocabulary in both its inflated and understated forms,
contrast reframes, rule-of-three padding, false ranges, vague attribution,
tacked-on analysis, formulaic scaffolding, hedging stacks, and leftover
chatbot register. Then puts voice back, because clean and voiceless is its
own tell.

Full catalog with examples: [reference.md](reference.md).

| Pattern | What it looks like | Section |
|---|---|---|
| Significance inflation | "marks a pivotal moment in the evolution of..." | 1.1 |
| Rule of three | "fast, cheap, and secure" | 1.7 |
| The -ing tack-on | "...enabling new possibilities, fostering adoption" | 1.9 |
| Vague attribution | "Industry observers note..." | 1.10 |
| Generic conclusions | "The future looks bright" | 1.15 |
| Litotes | "not unlike," "not without merit" | 1.18 |
| Announcement register | "We're thrilled to share..." | 1.19 |
| Corporate vagueness | "leveraging our ecosystem's synergies" | 1.20 |
| Listicle brain | Bullet points where prose should be | 2.6 |

## What it writes instead

The skill also encodes a position on writing, in
[reference.md](reference.md) Part 6: commit to a point of view, lead with
concrete detail, build narrative tension, close on something specific. The
recurring failure it targets is the unattached data point — a number alone is
a number, a number with "which tells you..." after it is a post.

It is format-aware. A short post's first line *is* the post. A thread puts
the hook in entry one and lands rather than summarizes. Long-form opens on
tension, not conclusion, and its subheadings describe rather than perform. A
newsletter's subject line states a fact or creates curiosity the reader
cannot resolve by guessing.

The voice principles draw on how four writers operate — Paul Graham's
abstract claim followed by a concrete example inside two sentences, Morgan
Housel's apparently unrelated opening story that snaps into focus, Lyn
Alden's willingness to show her work and say what the data means, Cobie's
refusal to soften the thing everyone is thinking. Not templates. Proof that
committing to a perspective works across very different subjects.

None of Part 6 comes from the primary sources, and the skill is required to
label edits driven by it as taste rather than source-backed. See
[SOURCES.md](SOURCES.md).

## What it deliberately does not do

**No blanket em dash ban.** The source says outright that the list is not a
ban on punctuation and that no one is claiming only AI uses em dashes. The
real observation is that models use them at higher rates than nonprofessional
human writing in the same genre. So this skill checks density instead of
enforcing zero. A hard ban produces comma splices, which reads as
machine-processed in a different way.

**No curly quote ban.** Frequently reported backwards. Curly quotes are
standard in professional typesetting, and Gemini and Claude typically do not
produce them at all.

**No treating clean grammar as suspicious.** The source lists perfect grammar
among the indicators that do not work, since plenty of people write well.

**No authorship verdicts.** Asked whether a specific person used AI, the
skill describes characteristics rather than declaring. Detection tools produce
false positives in both directions, and even trained human reviewers land
around 90%, meaning one confident judgment in ten is wrong. False accusations
have real cost.

## Scope

This is a writing tool. The material it is built on is a detection guide,
written by volunteers cleaning up AI text, and that project's own
documentation treats "humanizer" services aimed at defeating detectors as
part of the problem. Using it to improve a draft is squarely in line with why
the catalog is public. Using it to pass unassisted work off is not, and it is
also an arms race on someone else's schedule.

## Contributing

Re-verify against the primary sources at least twice a year; the vocabulary
lists go stale as models change. Preserve the false-positive notes: most
downstream summaries drop them, which is how the em dash myth spread. Keep
material from outside the primary sources in its own section in `SOURCES.md`
rather than attributing it to Wikipedia.

## License

MIT for this repository. Source material is CC BY-SA 4.0; see
[SOURCES.md](SOURCES.md).
