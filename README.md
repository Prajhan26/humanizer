# humanizer

A Claude Code skill that rewrites AI-sounding drafts into prose a person
would plausibly have written.

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

```
/humanizer
```

then paste the draft. Or describe the problem and let Claude load it:

```
Does this sound like AI wrote it?
Rewrite this so it doesn't read like ChatGPT.
```

## Layout

```
humanizer/
├── SKILL.md              # the skill; loaded into context when invoked
├── reference.md          # full pattern catalog; loaded on demand
├── SOURCES.md            # provenance and adaptations
├── evals/evals.json      # test cases
├── scripts/validate.py   # structural checks
└── .github/workflows/    # CI
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

## Testing

```bash
pip install pyyaml
python3 scripts/validate.py
```

Checks frontmatter YAML validity, unrecognized fields, the 1,536-character
description budget, the 500-line ceiling, broken file references, and nested
`SKILL.md` files. That last check exists because a buried `SKILL.md` is the
single most common reason a skill silently never loads.

For behavioral testing:

```
/plugin install skill-creator@claude-plugins-official
/reload-plugins
```

Then: `evaluate my humanizer skill with skill-creator`.

`evals/evals.json` splits into removal, restraint, and triggering categories.
The restraint cases matter most. Over-application is the dominant failure
mode for this kind of skill, and a suite that only tests removal will happily
pass a version that strips every em dash from a newsletter.

Run comparisons in a fresh session. Leftover context from editing the skill
hides gaps in the written instructions.

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
rather than attributing it to Wikipedia. Add an eval case for any failure
mode you fix, including a restraint case when the fix is "stop doing this."

## License

MIT for this repository. Source material is CC BY-SA 4.0; see
[SOURCES.md](SOURCES.md).
