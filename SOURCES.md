# Sources

Provenance for every claim in `reference.md`, plus what was deliberately left
out and why.

Last verified: 2026-08-04.

## Primary

**[Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)**
Maintained by WikiProject AI Cleanup. Roughly 15,000 words. A catalog of
patterns observed across many thousands of instances of AI-generated text on
Wikipedia, with real examples drawn from articles and drafts.

Its own structure, which `reference.md` follows:

| Section | Covers | Ported here as |
|---|---|---|
| Language and tone | Puffery, vocabulary, syntax patterns | Part 1 |
| Style | Em dashes, lists, emoji, headings, boldface | Part 2 |
| Communication intended for the user | Leftover chatbot register | Part 3 |
| Markup | Wikitext the model does not understand | Part 4 |
| Citations | Fabricated and mismatched references | Part 4 |
| Ineffective indicators | What does not work as a signal | Part 5 |

**[Wikipedia:WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)**
and its **[/Guide](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide)**
subpage. The project that produced the above. The Guide supplies the material
in Part 5 on detector reliability and reviewer accuracy.

## What the source says about itself

Quoting the framing directly, because it constrains what this skill should
do:

> This list is not a ban on certain words, phrases, or punctuation. No one is
> taking your em-dashes away or claiming that only AI uses them.

And on scope:

> While some of its advice may be broadly applicable, some signs, particularly
> those involving punctuation and formatting, may not apply in a non-Wikipedia
> context.

Both are load-bearing. Any humanizer built on this material that treats the
list as a ban list is misreading it.

## Adaptations made, and why

The source targets Wikipedia editors detecting other people's text. This
skill targets a writer improving their own draft. Four consequences:

1. **Wikipedia-specific style rules were reweighted, not copied.** Sentence
   case headings and straight quotes are Wikipedia house style. Title case is
   normal in most publications; curly quotes are normal in professional
   typesetting. Marked as context-dependent in Part 2 rather than as rules.

2. **Markup signals were generalized.** Wikitext residue became "output
   pasted into a system the model does not understand," which covers the
   Markdown-code-fence and placeholder cases anywhere.

3. **Detection framing was inverted into editing framing.** "This is evidence
   of AI" became "this sentence is not doing work." Part 5 exists to stop the
   skill acting on signals the source explicitly rates as unreliable.

4. **The false-positive notes were kept.** Most downstream summaries of this
   page drop them, which is how the em dash myth spread.

## Material from outside the primary sources

Additions the Wikipedia page does not catalog as such. Some are drawn from
2025–2026 documentation of newer model output; the last two are this
project's own and are not detection claims at all.

- **The understated slop layer** (Part 1.4): quietly, shift, matters, shape,
  land, actually, real, earn, the work, hold, pull, compound, signal. Newer
  models are subtly rather than blatantly positive, which the Wikipedia page
  does note in general terms; this vocabulary set is the specific form it
  takes.
- **The contrast reframe as the dominant tell** (Part 1.5). The page covers
  negative parallelism; the promotion to first position reflects its current
  frequency, not a claim in the source.

- **Litotes** (Part 1.18), **announcement register** (1.19), and **corporate
  vagueness** (1.20). The Wikipedia page covers promotional register and
  puffery, which overlap these; splitting them out is an editorial choice
  made because each has a distinct fix. Litotes in particular is a
  long-standing rhetorical figure, and calling it an AI tell is a claim about
  frequency in model output, not about the figure.
- **The writing philosophy** (Part 6.1) and **the format guidance** (6.2).
  Neither is in the source, which catalogs what AI text does and says nothing
  about what good writing does. This is the project's own position.
- **The four writers named in Part 6.3** — Paul Graham, Morgan Housel, Lyn
  Alden, Cobie. Characterizations are this project's reading of publicly
  available work by each. None of them is affiliated with this project,
  endorses it, or has been consulted about it. They are cited as
  demonstrations that committing to a perspective works across different
  subjects, not as an authority for any rule.

All of these are flagged here rather than presented as Wikipedia's findings.
`SKILL.md` rule 4 requires the skill to label edits driven by this section as
taste rather than source-backed.

## Known gap: paragraph cadence

The primary source catalogs vocabulary, sentence patterns, markup, and
citation problems. It does not cover format rhythm — the sequence of
one-or-two-sentence paragraphs each landing on a beat, common to LLM output
and to the founder-post register it was trained on. Testing found this is
often what makes a long personal draft read machine-written even after every
catalogued pattern is cleared, and that consolidating paragraphs while
rejoining the beats with periods changes the count without changing the
rhythm.

The skill is instructed to treat calls here as its own rather than the
source's. Nothing in Wikipedia's page supports them.

## Context worth knowing

Since March 2026, Wikipedia's WP:LLM guideline has prohibited using LLMs to
generate or rewrite article content, with limited exceptions for translation
and basic copyediting.

The WikiProject's Guide also notes that many sites offer to "humanize" LLM
text specifically to defeat detection tools, and treats those tools as part
of the problem it is addressing.

Worth stating plainly: this repository borrows a detection catalog to improve
writing. Its authors would not endorse using it to pass work off as
unassisted. If your use case is "make AI text survive a detector," you are
using a source against the intent of the people who built it, and you are
also entering an arms race you will lose on a schedule set by someone else.

## Re-verification

The primary page changes frequently and its vocabulary lists go stale as
models update. Re-check at least twice a year. `scripts/validate.py` checks
structure, not currency.

When updating: preserve the false-positive notes, keep additions from outside
the primary sources in the "Material from outside" section above rather than
attributing them to Wikipedia, and update the verification date at the top.

## Licensing

Wikipedia content is CC BY-SA 4.0. This repository paraphrases and
restructures rather than copying, and attributes above. Short quotations are
marked as quotations. If you fork this and copy source text verbatim at
length, CC BY-SA applies to your fork.
