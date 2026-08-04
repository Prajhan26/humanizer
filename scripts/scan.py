#!/usr/bin/env python3
"""Deterministic pattern scan for a draft. Run: python3 scripts/scan.py FILE

Reports catalog hits with the reference.md section that governs each one, plus
the author's mechanical fingerprint and computed counts. Does the mechanical
half of the job so judgment can start from evidence instead of impression.

Deliberately does NOT decide anything. It never scores a draft, never says
text is AI-generated, and never recommends an edit. A hit is a place to look.
Read the cited section, including its false-positive note, before touching
anything. Stdlib only, so a fresh clone runs it with no install.
"""

import pathlib
import re
import sys
import unicodedata

# (label, section, pattern). Ordered roughly by how much the catalog trusts
# them. Everything here is a signal to check, not a defect.
SIGNALS = [
    ("significance inflation", "1.1", r"\b(?:stands? as|serves? as a testament|plays? a (?:vital|crucial|pivotal) role|underscor\w+ (?:its|the) significance|reflects? broader|symboliz\w+ its enduring|setting the stage for|marks? a (?:pivotal|turning) (?:moment|point)|evolving landscape|indelible mark|deeply rooted|at its core)\b"),
    ("slop vocabulary, inflated", "1.3", r"\b(?:additionally|align(?:s|ed|ing)? with|crucial|delve|emphasizing|enduring|enhance\w*|foster(?:s|ed|ing)?|garner\w*|interplay|intricate|pivotal|showcas\w+|tapestry|testament|underscor\w+|vibrant)\b"),
    # Tested at 11/11 true positives, 0/10 false positives against the forms
    # in reference.md 1.5 plus perfect-tense and plain-enumeration decoys.
    ("contrast reframe", "1.5",
     r"(?:\b\w+n[o’']?t\s+(?:just|only|merely|simply)\b"
     r"|\b(?:not|no longer)\s+(?:just|only|merely|simply)\b"
     r"|(?<!have )(?<!has )(?<!had )\bnot\s+[^.!?;,]{1,45},\s*but\b"
     r"|\b\w+n[o’']?t\s+[^.!?;,]{1,45}[;,]\s*it\b"
     r"|\bit'?s\s+not\s+[^.!?,]{1,45},\s*it'?s\b"
     r"|\binstead of\s+\w+ing\b)"),
    ("copula avoidance", "1.6", r"\b(?:serves? as|stands? as|boasts?|represents?|features?)\b"),
    ("false range", "1.8", r"\b(?:rang(?:e|es|ing)|spanning)\s+from\b"),
    ("vague attribution", "1.10", r"\b(?:industry observers|studies (?:show|suggest)|experts (?:say|agree|note)|critics have argued|(?:it is |is )?widely (?:regarded|considered|seen)|sources suggest|research shows)\b"),
    ("editorializing aside", "1.11", r"\b(?:it'?s important to note|it is important to note|no discussion would be complete|it'?s worth noting|notably,)"),
    ("section summary", "1.12", r"(?:^|\.\s+)(?:in summary|in conclusion|overall|to sum up)\b"),
    ("generic positive close", "1.15", r"\b(?:the future looks bright|exciting times|continue to evolve|only time will tell)\b"),
    ("hedging stack", "1.16", r"\b(?:could potentially|might(?: well)? (?:have|be) some|it could be argued|in certain contexts|may(?: well)? potentially)\b"),
    ("register artifact", "Part 3", r"(?:great question|what a fascinating|i hope this helps|let me know if you|as of my last update|i hope this message finds you well|would you like me to|thank you for your time and consideration|dear editors)"),
    ("markup residue", "Part 4", r"(?:turn\d+search\d+|:contentReference|\[(?:URL of|insert |your )[^\]]*\]|^```\s*$)"),
]

# Common words with legitimate uses. reference.md 1.4 is explicit: flag only
# on density plus emptiness, never on a single hit. Reported as a count only.
UNDERSTATED = [
    "quietly", "shift", "shifts", "shifting", "matters", "shape", "shapes",
    "land", "lands", "actually", "real", "earn", "earns", "the work", "hold",
    "holds", "pull", "pulls", "compound", "compounds", "signal", "signals",
]

WEAK = """Weak signals are reported for awareness only. reference.md Part 5
lists these among the indicators that do not work: perfect grammar, poor
grammar, formal tone, a single em dash, curly quotes, any one listed word,
and non-native phrasing. Editing on them produces false positives."""


def paragraphs(text):
    return [b for b in re.split(r"\n\s*\n", text.strip()) if b.strip()]


def fingerprint(text):
    """Mechanical habits. Consistent idiosyncrasy is evidence a person typed
    it, so these are things to PRESERVE, not normalize. See SKILL.md rule 2."""
    paras = paragraphs(text)
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    return {
        "words": len(text.split()),
        "paragraphs": len(paras),
        "sentences": len(sentences),
        "single sentence paragraphs": sum(
            1 for p in paras if len(re.findall(r"[.!?]", p)) <= 1),
        "em dashes": text.count("—"),
        "en dashes": text.count("–"),
        "spaced hyphens ' - '": text.count(" - "),
        "curly apostrophes": text.count("’"),
        "straight apostrophes": text.count("'"),
        "curly double quotes": text.count("“") + text.count("”"),
        "straight double quotes": text.count('"'),
        "bold runs": len(re.findall(r"\*\*[^*]+\*\*", text)),
        "bold-colon headers": len(re.findall(r"\*\*[^*]+:\*\*", text)),
        "emoji": sum(1 for c in text if unicodedata.category(c) == "So"),
    }


def scan(text):
    lines = text.splitlines()
    hits = []
    for label, section, pattern in SIGNALS:
        rx = re.compile(pattern, re.I | re.M)
        for n, line in enumerate(lines, 1):
            for m in rx.finditer(line):
                if m.group().strip():
                    hits.append((label, section, n, m.group().strip()))
    return hits


def understated_density(text):
    low = text.lower()
    found = {}
    for word in UNDERSTATED:
        n = len(re.findall(rf"\b{re.escape(word)}\b", low))
        if n:
            found[word] = n
    return found


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/scan.py FILE")
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        sys.exit(f"no such file: {path}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        sys.exit(f"{path} is empty")

    print(f"scan: {path}\n")

    print("FINGERPRINT  (habits to preserve, not normalize)")
    fp = fingerprint(text)
    for k, v in fp.items():
        print(f"  {k:<28} {v}")

    dash_note = None
    if fp["spaced hyphens ' - '"] >= 3 and fp["em dashes"] == 0:
        dash_note = ("Author uses spaced hyphens consistently and no em "
                     "dashes. That is a signature. Do not convert it.")
    elif fp["em dashes"] >= 3 and fp["spaced hyphens ' - '"] == 0:
        dash_note = ("Author uses em dashes consistently. Check density per "
                     "reference.md 2.1; do not enforce zero.")
    if dash_note:
        print(f"\n  NOTE: {dash_note}")

    if fp["paragraphs"] and fp["single sentence paragraphs"] / fp["paragraphs"] > 0.6:
        print(f"\n  NOTE: {fp['single sentence paragraphs']} of "
              f"{fp['paragraphs']} paragraphs are a single sentence. Cadence "
              f"is NOT in the catalog (see SOURCES.md, Known gap). Native to "
              f"some platforms. Any call here is yours, not the source's.")

    hits = scan(text)
    print(f"\n\nSIGNALS  ({len(hits)} hits)")
    if not hits:
        print("  none")
    else:
        by_label = {}
        for label, section, n, txt in hits:
            by_label.setdefault((label, section), []).append((n, txt))
        for (label, section), items in sorted(
                by_label.items(), key=lambda kv: -len(kv[1])):
            print(f"\n  {label}  [reference.md {section}]  x{len(items)}")
            for n, txt in items[:8]:
                print(f"    line {n}: {txt}")
            if len(items) > 8:
                print(f"    ... {len(items) - 8} more")

    dens = understated_density(text)
    total = sum(dens.values())
    print(f"\n\nUNDERSTATED LAYER  [reference.md 1.4]  {total} occurrences")
    if dens:
        print("  " + ", ".join(f"{w} x{n}" for w, n in
                               sorted(dens.items(), key=lambda kv: -kv[1])))
    per100 = (total / fp["words"] * 100) if fp["words"] else 0
    print(f"  density: {per100:.1f} per 100 words")
    print("  Flag only on density PLUS emptiness: several clustered in a "
          "passage that makes no specific assertion. These are ordinary "
          "English words. Never flag a single hit.")

    print(f"\n\nWEAK SIGNALS\n{WEAK}")
    print("\nThis scan reports locations, not verdicts. It cannot tell you "
          "whether a draft was written by AI, and neither can anything else. "
          "Read each cited section, including its false-positive note, before "
          "editing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
