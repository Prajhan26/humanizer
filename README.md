# humanizer

A Claude Code skill that rewrites AI-sounding drafts into prose a person
would plausibly have written — and governs writing composed from scratch, so
the patterns never get generated in the first place.

Clone it, paste your draft, get a version without the machine's habits in it.

Built on [Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI Cleanup, with the false-positive guidance kept
intact. Full provenance in [SOURCES.md](SOURCES.md).

## What this is

A skill built for ADITI, so drafts leave sounding like the person who wrote
them.

It is not a detector-evasion tool and it does not have a house style it
pushes everything toward. It removes what the model added and leaves what you
brought. Where it has an opinion of its own, it says so and you can refuse
it.

The hard part is restraint. A tool that strips every flagged pattern
produces prose that is clean, correct and dead, which is its own kind of
tell. Half the rules in this repo exist to stop the skill doing that.

## Before and after

**Before** — 75 words

> AI-assisted coding serves as an enduring testament to the transformative
> potential of large language models, marking a pivotal moment in the
> evolution of software development. In today's rapidly evolving
> technological landscape, these groundbreaking tools are reshaping how
> engineers ideate, iterate, and deliver, underscoring their vital role in
> modern workflows.
>
> At its core, the value proposition is clear: streamlining processes,
> enhancing collaboration, and fostering alignment. It's not just about
> autocomplete; it's about unlocking creativity at scale.

**After** — 36 words

> Large language models can write working code, and engineers now draft and
> revise with them.
>
> The claim is that this saves time and makes teams work together better.
> Autocomplete was the earlier, smaller version of it.

Nine slop words in 75. Two participial tails. Two triplets in four sentences.
One contrast reframe. `serves as` where `is` was available.

And the finding the skill reports underneath the rewrite: **the word count
fell 52% and the information did not, because there was none.** Every
sentence in that draft asserts significance. Not one is checkable. It cannot
be fixed by editing — the next line has to be something like *"our median PR
went from 3 days to 6 hours"*, and only the author knows that number. The
skill will not invent one. Rule 1 forbids it.

### The harder half

Most drafts are not that. Here is the same skill on the founder essay from
the ADITI Substack, 1,189 words, where the correct answer is mostly *leave it
alone*.

It flagged six instances of one pattern. Three were real:

> Carrying cash wasn't merely cumbersome; it was unsafe.
> → Carrying cash was unsafe.

Three were not, including this one, which the skill cut and should not have:

> Because that's what this stage really is: not fear of losing anything, but
> the discomfort of waiting for your outer reality to catch up with the inner
> truth you've already admitted to yourself.

Identical construction to the sentence above it. But readers *do* arrive at a
resignation story expecting fear of loss, so denying it is a correction, not
padding — and it sets up a distinction the essay collects on two paragraphs
later. Cutting it made the sentence say less.

That miss became [rule 6](SKILL.md): removing a pattern may not remove a
claim.

Six flagged, three edited, zero facts touched, and the author's fifteen
spaced hyphens left exactly where they were. Any tool can strip words. The
work is knowing when to stop.

## Anywhere else

[PROMPT.md](PROMPT.md) is the same thing as one paste-able block, for
ChatGPT, Claude on the web, Gemini, Codex, Cursor or Copilot. Paste it, then
paste your draft. It also drops into custom instructions, a project, or
`AGENTS.md` if you want it permanent.

## Install (Claude Code)

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
├── PROMPT.md     # paste-anywhere version for other tools
├── reference.md  # full pattern catalog; loaded on demand
└── SOURCES.md    # provenance and adaptations
```

`SKILL.md` stays short deliberately. Once invoked, its content persists in
context for the rest of the session, so every line is a recurring cost. The
catalog lives in `reference.md` and loads only when a pattern needs judgment.

## What it catches

Nine categories of AI voice killer:

| Pattern | What it looks like | Section |
|---|---|---|
| Significance inflation | "marks a pivotal moment in the evolution of..." | 1.1 |
| Rule of three | "fast, cheap, and secure" | 1.7 |
| Thrilled-to-announce energy | "We're excited to share..." | 1.19 |
| Corporate vagueness | "leveraging our ecosystem's synergies" | 1.20 |
| The -ing tack-on | "...enabling new possibilities, fostering adoption" | 1.9 |
| Litotes | "not unlike," "not without merit" | 1.18 |
| Vague attribution | "Industry observers note..." | 1.10 |
| Listicle brain | Bullet points where prose should be | 2.6 |
| Generic conclusions | "The future looks bright" | 1.15 |

Plus format-level tells: bold and emoji spam, Title Case headings,
sycophantic openers, cutoff disclaimers, and em dash *density* — not a ban,
for the reason in "What it deliberately does not do" below.

Then it puts voice back, because clean and voiceless is its own tell. Full
catalog with examples: [reference.md](reference.md).

## Format-aware

The skill adapts to what you are writing.

**Short-form posts** — the first line is the post. One idea. No "hot take:"
prefixes.

**Threads** — hook in tweet one, each post advances the idea, the last post
lands with finality rather than summarising.

**Long-form** — open on tension, not conclusion. Paragraphs develop one idea
fully. Subheadings describe, they do not perform.

**Newsletters** — subject line conveys a fact or creates genuine curiosity.
Register between a sharp blog post and a warm personal message.

## Writing influences

It also encodes a philosophy, in [reference.md](reference.md) Part 6: commit
to a point of view, lead with concrete detail, build narrative tension, close
on something specific. The recurring failure it targets is the unattached
data point — a number alone is a number, a number with "which tells you..."
after it is a post.

The voice principles draw on how four writers operate.

**Paul Graham** — abstract claim followed by a concrete example within two
sentences. Short words. Treats the reader as smart but busy.

**Morgan Housel** — opens with a small story that seems unrelated, then snaps
it into focus. Writes to learn, not to report.

**Lyn Alden** — shows her work. Uses data, forms opinions about what it
means, does not perform neutrality.

**Cobie** — says the thing people are thinking but not saying. No hedging, no
softening.

These are not templates. They are proof that committing to a perspective
works across very different subjects and styles.

None of Part 6 comes from the primary sources. The skill is required to label
edits driven by it as taste rather than source-backed, which means you can
throw any of it out. See [SOURCES.md](SOURCES.md).

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

---

Built for ADITI, with gratitude.
