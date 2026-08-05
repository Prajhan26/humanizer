# Pattern reference

Loaded on demand from `SKILL.md`. Organized along the source guide's own
taxonomy: language and tone, style, communication intended for the user, and
markup and citations. A final section covers indicators that do not work.

Every pattern here carries a false-positive note where one applies. Read it
before editing.

---

# Part 1: Language and tone

## 1.1 Significance inflation

Importance asserted about facts that do not carry it, usually by tying the
fact to a broader trend.

Watch: stands as, serves as a testament to, plays a vital / crucial / pivotal
role, underscores its significance, reflects broader, symbolizing its
enduring, setting the stage for, marks a turning point, evolving landscape,
indelible mark, deeply rooted, at its core.

**Before**
> The Statistical Institute of Catalonia was officially established in 1989,
> marking a pivotal moment in the evolution of regional statistics in Spain.

**After**
> The Statistical Institute of Catalonia was established in 1989 to publish
> regional statistics separately from Spain's national office.

The source notes a specific sub-case: when writing about anything framed as
cultural heritage, models repeatedly remind the reader of its importance.

## 1.2 Promotional register

People and companies written up like press releases. Places written up like
tourism copy. The tell is intensity applied to ordinary facts.

Also noted in the source: older models produced more blatantly positive text,
while newer ones are more subtly positive and tend to avoid openly
superlative words like "the best." Expect the modern version to be quieter
and therefore harder to spot.

**Before**
> Known for its reliability and performance, the truck remains a beloved
> icon among enthusiasts.

**After**
> The truck was produced from 1963 to 1985. Owners' clubs still maintain
> several hundred of them.

## 1.3 Slop vocabulary, inflated layer

Watch: additionally, align with, boasts, bolstered, crucial, delve,
emphasizing, enduring, enhance, fostering, garner, highlight (verb),
interplay, intricate, key (adjective), landscape (abstract),
meticulous/meticulously, pivotal, robust, showcase, tapestry, testament,
underscore (verb), valuable, vibrant.

These rose sharply in text produced after 2022 and cluster together: where
one appears, others usually do.

The set turns over as models change, which is why a hit dates a draft as much
as it flags it. The source's rough eras:

- **2023 to mid-2024 (GPT-4)** — additionally, boasts, bolstered, crucial,
  delve, emphasizing, enduring, garner, intricate, interplay, key, landscape,
  meticulous, pivotal, underscore, tapestry, testament, valuable, vibrant.
- **Mid-2024 to mid-2025 (GPT-4o)** — align with, bolstered, crucial,
  emphasizing, enhance, enduring, fostering, highlighting, pivotal,
  showcasing, underscore, vibrant.
- **Mid-2025 on (GPT-5)** — emphasizing, enhance, highlighting, showcasing,
  plus the understated layer in 1.4. Note how short this list is: the current
  generation is caught less by vocabulary than by the patterns in 1.1 and
  1.5.

"Delve" is the clearest case — famously overused in 2023, less frequent
through 2024, largely gone by 2025. Checking for it now mostly finds old
text.

**Before**
> Additionally, an enduring testament to Italian colonial influence is the
> widespread adoption of pasta in the local culinary landscape, showcasing
> how these dishes integrated into the traditional diet.

**After**
> Pasta, introduced during Italian colonization, is still common in the
> south.

## 1.4 Slop vocabulary, understated layer

The more recent set. Ordinary words doing no work: quietly, shift, matters,
shape, land, actually, real, earn, the work, hold, pull, compound, signal,
built different.

Harder to catch precisely because nothing sounds inflated. "The shift quietly
reshaping how teams actually work" contains no claim at all.

**False-positive note:** these are common English words with legitimate uses.
Flag only on density plus emptiness: several clustered in a passage that
makes no specific assertion.

## 1.5 Contrast reframe

The dominant tell in current output. Sets up an opposition and resolves it,
producing the shape of insight without the content.

Forms: "It's not X, it's Y." "Not just X, but Y." "Not only X but also Y."
"No X, no Y, just Z." The reversed form is characteristic of Grok.

**Before**
> It's not just about the beat riding under the vocals; it's part of the
> aggression. This isn't merely a song, it's a statement.

**After**
> The heavy beat carries most of the aggression.

**False-positive note:** the source acknowledges negative parallelism is a
legitimate technique in sales copy. It also works when the dismissed half is
a position someone actually holds. "This isn't a pricing problem, it's a
retention problem" is a claim. "It's not a song, it's a statement" is
decoration.

**The test, in one question:** would a reader plausibly believe the dismissed
half? If yes, the sentence is correcting them and needs both halves. If the
opposition was invented on the spot so the resolution would sound like
insight, cut it.

Two that pass, from a real draft: "not fear of losing anything, but the
discomfort of waiting" denies a reading readers do bring to a resignation
story. "Instead of feeling burdened, I felt euphoria" names the reaction the
preceding sentence set the reader up to expect. Delete either half and the
surprise goes with it. Compare "the validation wasn't merely financial",
where nobody thought it was only money — that one is decoration, and the
sentence is better without it.

Deleting the dismissed half is the default fix, not an automatic one. See
`SKILL.md` rule 6.

## 1.6 Copula avoidance

Elaborate verbs standing in for "is" and "has": serves as, stands as, marks,
functions as, operates as, represents, boasts, features, maintains, offers.
Studies found the words *is* and *are* dropped over 10% in academic writing
in 2023, with no comparable change before that.

Two variants worth naming. In an opening sentence, "refers to" treats the
subject as a term rather than a thing — "Catchment area refers to the
geographic area from which..." where "is" was available. And the elaborated
career verb: "ventured into politics as a candidate" for "was a candidate",
"began his career as" for "was".

**Do not confuse this with the past perfect.** "Has been featured" is
ordinary English, not copula avoidance.

**Before**
> Gallery 825 serves as LAAA's exhibition space. It features four rooms and
> boasts over 3,000 square feet.

**After**
> Gallery 825 is LAAA's exhibition space. It has four rooms totaling 3,000
> square feet.

## 1.7 Rule of three

Triplets as a reflex, across adjectives, benefits, and takeaways alike.
"Innovative, transformative, and groundbreaking."

**False-positive note:** three is a legitimate number of things. The tell is
a third item invented to fill the slot, or triplets stacking across
consecutive sentences.

## 1.8 False ranges

"From X to Y" where X and Y are not endpoints of any real scale. Sounds
comprehensive, specifies nothing.

**Before**
> Our services range from strategic planning to implementation support.

**After**
> We write the plan and then help build it.

## 1.9 Tacked-on analysis

Participial clauses appended to plain facts to imply depth: "...highlighting
Pakistan's entry into the global pickleball community", "...improving
convenience", "...illustrating lasting influence."

Fix: state what happened. Let the reader draw the conclusion.

## 1.10 Vague attribution

Watch: industry observers note, studies show, experts say, critics have
argued, it is widely regarded, sources suggest.

The source treats this as one of the more serious problems, not a stylistic
quibble: sensationalized and vaguely attributed statements are harder to
catch and carry more risk than any formatting tic.

Fix: name the source or drop the claim.

## 1.11 Editorializing asides

"It's important to note." "No discussion would be complete without."
"Notably." The writer inserting an opinion about what matters rather than
demonstrating it.

## 1.12 Section summaries

Restating what was just explained, as if the reader could not retain it for
three paragraphs. "In summary." "Overall." "In conclusion." Used as filler
rather than to add anything.

## 1.13 Formulaic structure

"Challenges and Future Prospects." "Legacy and Impact." "Looking Ahead." A
recognizable shape the source calls out directly: "Despite its [positive
words], [subject] faces challenges..." followed by a vague positive
assessment.

Outline scaffolding that survived into the final draft. These sections
almost never contain specific information.

## 1.14 Synonym cycling

Repetition-penalty artifact. The same referent renamed every sentence:
protagonist, main character, central figure, hero.

## 1.15 Generic positive conclusions

"The future looks bright." "Exciting times lie ahead." "This space will
continue to evolve."

Fix: end on the most specific thing in the piece.

## 1.16 Hedging stacks

**Before**
> While specific details are limited, it could potentially be argued that
> these tools might have some positive effect in certain contexts.

**After**
> The evidence is thin. Two small studies found a speedup on simple tasks
> and nothing on complex ones.

## 1.17 Model-specific vocabulary

Grok overuses superficially scientific words: causal, empirical, correlate,
substantiate. It also overuses the underscore and the reversed contrast
reframe.

The source cautions that a word being overused by AI does not imply its
synonyms are, and that context matters. Do not generalize a listed word to
its neighbors.

## 1.18 Litotes

Affirming by negating the opposite. "Not unlike." "Not without merit." "No
small feat." "Not uncommon." The construction sounds considered while
committing to nothing, and it stacks: a paragraph with three of them has an
author who will not say a plain thing plainly.

**Before**
> The result was not without merit, and the approach is not uncommon among
> teams of this size.

**After**
> The result was worth something. Teams this size do it all the time.

**False-positive note:** litotes is a real rhetorical figure with real uses,
and the negation sometimes carries the meaning — "not unhappy" is genuinely
not "happy." Flag on density, or where the positive form would say the same
thing in fewer words.

## 1.19 Announcement register

"We're thrilled to announce." "We're excited to share." "Today marks an
important milestone for us." Manufactured enthusiasm standing in for a
reason the reader should care.

**Before**
> We're thrilled to announce our latest integration, designed to empower
> teams to do their best work.

**After**
> The integration ships today. It cuts the export step, which was the thing
> people complained about most.

Fix: lead with what changed for the reader. Enthusiasm, if it survives, goes
after the fact rather than in front of it.

## 1.20 Corporate vagueness

"Leveraging our ecosystem's synergies." "Holistic, end-to-end solutions."
"Unlocking value across the stack." Abstraction stacked high enough that no
specific claim is being made, and therefore nothing can be checked.

The test: ask what would be different if the sentence were false. If nothing,
the sentence is not saying anything.

**Before**
> We leverage best-in-class infrastructure to deliver scalable solutions.

**After**
> We run it on Postgres. It handles about 40,000 writes a minute.

---

# Part 2: Style

## 2.1 Em dashes

The real observation is narrow: LLM output uses em dashes more often than
nonprofessional human writing of the same genre, and puts them where a human
would more likely use a comma, parenthesis, colon, or a misused hyphen.

The source states directly that this is not a ban, and that no one is
claiming only AI uses em dashes.

**Approach:** count them. Several in one paragraph, or a rate well above the
author's usual, means substitute some. Zero is not the target. A blanket ban
produces comma splices, which is its own tell.

## 2.2 Curly quotes

Handle carefully. This one is frequently reported backwards.

Curly quotation marks and apostrophes are standard in professionally typeset
work such as major newspapers. Grammar tools like LanguageTool can insert
them. Citation tools reproduce them from source titles. And several models,
including Gemini and Claude, typically do not produce them at all.

Curly quotes are close to useless as a signal outside Wikipedia's specific
style context. Do not edit on this basis.

## 2.3 Boldface and emoji

Boldface scattered through paragraphs for emphasis. Emoji bullets.
Bold-colon list headers where prose belongs: "**Speed:** things are fast."

These are strong signals and have no legitimate use in finished prose. Cut.

## 2.4 Title Case Headings

Capitalizing every noun in a heading rather than sentence case.

**False-positive note:** title case is standard in many publications outside
Wikipedia. Strong signal in a Wikipedia context, weak elsewhere. Match the
publication.

## 2.5 Heading level quirks

Chatbots tend to skip level 2 headings and start sections at level 3. In
Markdown terms: a document whose top section heading is `###` with no `##`
above it.

## 2.6 Listicle brain

Bullets where prose belongs. Three sentences of connected argument split into
three bullets loses the reasoning that made it an argument.

Fix: if the items relate logically to each other, write the paragraph.
Reserve bullets for genuinely parallel, unordered items.

---

# Part 3: Communication intended for the user

Text a careless editor left in when pasting model output. All of these are
strong signals with no legitimate use. Cut on sight.

- Sycophantic openers: "Great question!" "What a fascinating topic."
- Closers: "I hope this helps!" "Let me know if you need anything else."
  "Would you like me to expand on any section?"
- Knowledge-cutoff disclaimers: "As of my last update..."
- Letter framing in non-letter content: "I hope this message finds you well",
  "Dear Editors", "Thank you for your time and consideration."
- Direct address breaking the register: "you might wonder", "let's explore."
- The prompt itself, left above the output.
- Offers to fabricate: "Would you like me to add some references?"

---

# Part 4: Markup and citation residue

Wikipedia-specific in origin, but the general form applies anywhere output
gets pasted into a system the model does not understand.

- **Leftover code fences.** Output wrapped in a Markdown code block by the
  chatbot's own formatting, with the opening or closing fence copied along
  with it. The closing fence survives more often, being easier to miss.
- **Wrong markup dialect.** Markdown asterisks and underscores pasted into a
  system that uses different syntax.
- **Search and reference artifacts.** Placeholder codes emitted where the
  model tried to attach a link, such as `turn0search0` or
  `:contentReference[oaicite:0]`.
- **Unfilled placeholders.** `[URL of reliable source]`, `[insert date]`,
  bracketed instructions the user never replaced.
- **Comments addressed to the writer.** Notes saying an image or citation
  should be added if one becomes available.

**Citations specifically.** Fabrication is the highest-stakes failure here.
Watch for dead links, invalid DOIs, ISBNs that fail checksum, and the subtler
case: a real, verifiable source that has nothing to do with the claim it is
attached to. Fabricated references often pair real author names with
invented titles, which defeats surface-level inspection.

Note that missing citations are a weak signal now. Modern chatbots search the
web and cite routinely. The citations exist. Whether they support anything is
a separate question.

---

# Part 5: Indicators that do not work

The source guide devotes a section to this, and it is the part most
downstream summaries omit. These will produce false positives.

- **Perfect grammar.** Many writers are skilled, professionally trained, or
  use grammar tools. Flawless prose indicates nothing on its own.
- **Poor grammar.** Equally uninformative in the other direction.
- **Formal or dry tone.** A register, not a fingerprint.
- **A single em dash.** See 2.1.
- **Curly quotes.** See 2.2.
- **Any one listed word.** Density matters, individual words do not.
- **Non-native phrasing.** Detection tools disproportionately misflag
  non-native English writers. So do humans.

Two signals the source rates as more informative, both requiring context you
usually will not have when editing a draft:

- **Sudden style change.** A writer whose output shifts abruptly, especially
  against samples predating late 2022. The reverse also holds: consistent
  idiosyncrasies across old and new writing suggest the newer work is
  genuine.
- **English-variety mismatch.** A writer whose location and subject point one
  way while the spelling points another. Several models default to American
  English unless told otherwise.

**On automated detectors.** The source is blunt that they should never be
sole evidence: they produce both false positives and false negatives, their
scoring is opaque, and their algorithms change. The guide also observes that
research on trained human reviewers puts them around 90% accurate, which
means roughly one in ten confident judgments is wrong.

The editorial consequence: false accusations drive people away and poison the
atmosphere. When applying this catalog to someone else's writing, the correct
output is "this passage has these characteristics," never "this was written
by AI."

## 5.1 Signs of human writing

The source's other half, and the useful one when putting voice back. These
were observed over twenty-five years of writing to be **more** common in
human text than in model output. Restoring them is source-backed; stripping
them is the over-correction this catalog most often causes.

- **Simple is/has phrases.** "There is a", "it has a". The plain copula is a
  human habit. See 1.6 for the avoidance pattern this is the cure for.
- **Plain words where a stiff synonym exists.** wrote not authored, moved not
  relocated, used not utilized, tried not attempted, died not passed away.
- **Superlative or definitive statements.** "One of the best", "is the only",
  "was the first". Models hedge away from commitment; people commit.
- **Hedging qualifiers and intensifiers.** very, perhaps, tends to. Note this
  is the opposite of 1.16 — a *stack* of hedges is a tell, a single "very" is
  a person. Do not cut these on sight.
- **Isolated wordy constructions.** "as a result of", "in order to", "all of
  the", "a part of", "the fact that". Tightening every one of these is how an
  edit ends up sounding machine-processed.

Two more the source lists, useful only with context you rarely have when
editing a draft: text predating 30 November 2022 cannot be AI, and a writer
who can explain why they made a specific choice is usually the writer.

---

# Part 6: Writing, not only fixing

Everything above is a repair manual. This part is what to do instead, and it
applies whether a draft already exists or the page is blank. Nothing in this
part comes from the primary sources; see `SOURCES.md`.

## 6.1 Four principles

**Commit to a point of view.** Reacting to a fact beats reporting it. A draft
that could have been written by someone who believes the opposite is not
finished.

**Lead with concrete detail.** The first sentence decides whether there is a
second one. Open on the specific thing — the number, the moment, the line
someone actually said — not on the category it belongs to.

**Build tension.** A list of facts is not writing. Facts connected by a
thread of reasoning, arriving somewhere the reader did not expect, is. If
paragraph four could be swapped with paragraph two, there is no thread.

**Close on something specific.** The last line is the one that gets quoted.
A generic close ("the future looks bright", 1.15) throws away the only
sentence the reader is guaranteed to finish on.

The recurring failure underneath all four is the unattached data point. A
number alone is a number. A number with "which tells you..." after it is a
piece of writing.

## 6.2 Format

**Short post.** The first line is the post. One idea, carried the whole way.
No "hot take:" prefix, no throat-clearing before the claim — the prefix is a
promise the post then has to keep.

**Thread.** The hook lives in the first entry, not the second. Each
subsequent entry advances the argument rather than restating it with new
adjectives. The last entry lands; it does not summarize what the reader just
read (1.12).

**Long-form.** Open on tension, not conclusion. Each paragraph develops one
idea to its end before the next one starts. Subheadings describe what is
below them; they do not perform ("The Plot Thickens").

**Newsletter.** The subject line states a fact or creates real curiosity, and
curiosity means the reader cannot guess the answer. Register sits between a
sharp blog post and a warm personal message — closer to a letter than to a
company update.

## 6.3 Writers worth stealing from

Not templates. Four demonstrations that committing to a perspective works
across very different subjects.

**Paul Graham** — abstract claim, then a concrete example within two
sentences. Short words. Treats the reader as intelligent but in a hurry.

**Morgan Housel** — opens on a small story that appears unrelated, then snaps
it into focus. Writes to work something out rather than to report a
conclusion he already had.

**Lyn Alden** — shows her work. Presents the data, then says what she thinks
it means. Does not perform neutrality.

**Cobie** — says the thing everyone is thinking and not saying. No hedging,
no softening on the way in.

What they share is the thing the catalog cannot supply: a person deciding
something is true and being willing to be wrong about it in public.

---

# Framing

The catalog exists to describe what LLM output tends to do. It is not a style
guide, not a ban list, and not proof of authorship. Surface tics are also not
the real problem: they are a cue to check for the things that matter, which
are fabricated sources, unverifiable claims, and absent original thought.

Applied to your own draft, the useful question is never "does this match a
pattern." It is "does this sentence say something, and does it say it in a
voice." Where a listed rule and a better sentence conflict, the sentence
wins.
