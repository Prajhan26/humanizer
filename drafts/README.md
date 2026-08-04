# drafts

Put your draft here as a `.md` file, then scan it and ask for the rewrite.

```bash
python3 scripts/scan.py drafts/my-post.md
```

The scan is deterministic and needs no API key or network. It reports where
catalog patterns occur, which `reference.md` section governs each one, your
draft's mechanical fingerprint, and computed counts. It does not decide
anything and it cannot tell you whether text was written by AI.

Then, in Claude Code from this directory:

```
/humanizer drafts/my-post.md
```

Claude reads the scan output as evidence, applies the false-positive notes,
and returns the rewrite with changes grouped by authority: source-backed,
copyedit, or taste. Refuse the taste ones freely.

Files here are yours. Nothing in this directory is tracked except this
README, so your drafts stay local to your clone.

## What the scan cannot see

Regex finds the contrast reframe in its written forms ("not just X, but Y",
"isn't merely", "doesn't X, it Ys"). It cannot find the same move made as
bare antithesis — "The mind negotiates; the gut declares", "Not the idea.
The inevitability." Those need reading. A low signal count is not a clean
bill of health.

It also cannot see whether an analogy closes, whether a claim has evidence
behind it, or whether the paragraph cadence fits the register. Those are
usually what actually makes a draft read machine-written, and none of them
are in the catalog.
