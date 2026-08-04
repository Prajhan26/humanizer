---
name: humanizer
description: Rewrites AI-sounding drafts so they read like a person wrote them. Catches slop vocabulary, significance inflation, contrast reframes, rule-of-three padding, vague attribution, and leftover chatbot register, then puts voice back in. Use on any draft that reads as machine-generated.
when_to_use: Trigger on "humanize this", "make this sound human", "this reads like AI", "de-slop this", "rewrite this in my voice", or when the user shares a draft and asks whether it sounds machine-written.
allowed-tools: Read, Grep, Glob
---

# Humanizer

Rewrite AI-sounding text into prose a person would plausibly have written.
Removing patterns is half the job. Voiceless writing is its own tell.

## Read this before editing anything

The pattern catalog is descriptive, not prescriptive. It is a record of what
LLM output tends to do, not a list of banned words. Humans use em dashes.
Humans list three things. Humans write clean grammar.

So: a matched pattern is a reason to look closer, never an automatic edit.
Ask whether removing it makes the sentence better. If not, leave it.
Over-application produces stilted, comma-spliced prose that reads as
machine-processed in a different way.

Density is the real signal. One "crucial" is nothing. Four abstract
intensifiers in a paragraph with no concrete claim underneath is the finding.

## Process

1. Read the draft. Note its register and who it is for.
2. Scan the pattern families below. Load `reference.md` for the full catalog,
   examples, and the false-positive notes on any pattern needing judgment.
3. Rewrite. Preserve meaning and register. Remove the machine's habits, not
   the author's.
4. Audit: what still reads as generated? Two or three bullets.
5. Revise once more from that audit. Output the final version.

## Pattern families

Full catalog with examples and caveats: `reference.md`

**Puffery and significance inflation.** Importance asserted rather than
shown. stands as, serves as a testament, plays a vital role, marks a pivotal
moment, underscores the significance, evolving landscape, indelible mark.
Related: promotional register, where a person or company gets written up like
a press release, and a place gets written up like a tourism board wrote it.

**Slop vocabulary, two vintages.** Older, inflated layer: delve, tapestry,
intricate, foster, garner, showcase, vibrant, crucial, interplay, testament,
underscore, align with. Newer, understated layer common in recent output:
quietly, shift, matters, shape, land, actually, real, earn, the work, hold,
pull, compound, signal. The second set is harder to catch because the words
are plain. They read as restrained while claiming nothing.

**Contrast reframe and negative parallelism.** "It's not X, it's Y." "Not
just X, but Y." "No X, no Y, just Z." Manufactures insight by inventing an
opposition. Fix: delete the dismissed half. Note the reverse construction is
common in Grok output.

**Structural padding.** Rule of three. False ranges ("from X to Y" with no
scale between them). Synonym cycling driven by repetition penalty. Section
summaries restating what was just said. Formulaic "Challenges and Future
Prospects" scaffolding.

**Copula avoidance.** serves as, stands as, boasts, features, represents,
where "is" or "has" is the honest verb.

**Vague attribution.** Industry observers note, studies show, experts say,
widely regarded. Name the source or cut the claim.

**Tacked-on analysis.** Participial tails that gesture at meaning without
supplying it: "...highlighting the shift", "...illustrating lasting
influence", "...improving convenience."

**Editorializing asides.** "It's important to note." "No discussion would be
complete without." The writer telling the reader what matters instead of
showing it.

**Register artifacts.** Cut unconditionally. Sycophantic openers ("Great
question!"), closers ("Let me know if you'd like me to expand"),
knowledge-cutoff disclaimers, letter framing dropped into non-letter content
("I hope this message finds you well"), emoji bullets, bold-colon list
headers, leftover code fences, prompt text left in the output.

**Hedging stacks.** "It could potentially be argued that this might have some
effect in certain contexts." Hedge once when uncertain. Stacked hedges say
nothing carefully.

## Weak signals: check, do not act on alone

Listed so you recognize them, not so you edit them. See `reference.md`.

Perfect grammar. Any single em dash. Curly quotes, which are standard in
professional typesetting and which several models avoid anyway. Formal tone.
Long sentences. Non-native phrasing. Acting on these produces false positives
and, in editing, damage.

## Putting voice back

Removal leaves a hole. Unfilled, the result reads as sterile, which is
detectable in its own right.

- Take a position. Reacting to a fact beats reporting it.
- Vary rhythm. Short sentence. Then a longer one that earns its length by
  carrying a clause worth carrying.
- Allow mixed feelings. "Impressive and slightly unnerving" is a person.
- First person where the format permits.
- Concrete over abstract, especially for feeling. Not "concerning" but the
  specific thing that caused the concern.
- Leave some mess. A tangent, an unresolved qualification.

## Format notes

- **Short post.** First line is the post. One idea. No "hot take:" prefix.
- **Thread.** Hook first, each entry advances the argument, last one lands.
- **Long-form.** Open on tension. Subheadings describe, not perform.
- **Newsletter.** Subject line states a fact or creates real curiosity.

## Output

1. Draft rewrite
2. Remaining tells, 2-3 bullets
3. Final rewrite
4. Change summary only if asked

## Scope

This skill improves writing. It is not a detector-evasion tool, and the
source material it draws on was written by people trying to catch AI text,
not help it pass. See `SOURCES.md`.
