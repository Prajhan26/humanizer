#!/usr/bin/env python3
"""Structural checks for the humanizer skill. Run: python3 scripts/validate.py"""

import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required: pip install pyyaml")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAILURES = []
WARNINGS = []

# Fields Claude Code recognizes in SKILL.md frontmatter. Anything else is
# silently ignored at runtime, which is worse than an error.
KNOWN_FIELDS = {
    "name", "description", "when_to_use", "argument-hint", "arguments",
    "disable-model-invocation", "user-invocable", "allowed-tools",
    "disallowed-tools", "model", "effort", "context", "agent", "background",
    "hooks", "paths", "shell", "license", "compatibility", "metadata",
}

LISTING_CAP = 1536   # description + when_to_use truncation point
MAX_LINES = 500      # guidance ceiling for SKILL.md


def fail(msg):
    FAILURES.append(msg)


def warn(msg):
    WARNINGS.append(msg)


def check_skill():
    path = ROOT / "SKILL.md"
    if not path.exists():
        fail("SKILL.md missing from repo root. Claude Code will not find the "
             "skill if it lives in a subdirectory.")
        return

    text = path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        fail("SKILL.md does not open with YAML frontmatter.")
        return

    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("SKILL.md frontmatter is not closed with a second ---.")
        return

    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        # This is the failure mode that bites silently: Claude Code loads the
        # body with empty metadata, so /humanizer still works while automatic
        # invocation stops.
        fail(f"SKILL.md frontmatter is not valid YAML: {exc}")
        return

    if not isinstance(fm, dict):
        fail("SKILL.md frontmatter did not parse to a mapping.")
        return

    for key in fm:
        if key not in KNOWN_FIELDS:
            warn(f"Frontmatter field '{key}' is not recognized by Claude Code "
                 f"and will be ignored.")

    # Space-separated tool lists parse as one tool name, so the skill loads
    # with an unsatisfiable allowlist and every Read silently fails.
    for field in ("allowed-tools", "disallowed-tools"):
        value = fm.get(field)
        if isinstance(value, str) and "," not in value and len(value.split()) > 1:
            fail(f"'{field}' is space-separated ({value!r}). Use a "
                 f"comma-separated string or a YAML list, or it parses as a "
                 f"single tool name.")

    if "description" not in fm:
        fail("Frontmatter has no 'description'. Claude cannot match the skill "
             "to a request without one.")
    else:
        combined = len(str(fm["description"])) + len(str(fm.get("when_to_use", "")))
        if combined > LISTING_CAP:
            fail(f"description + when_to_use is {combined} chars, over the "
                 f"{LISTING_CAP} listing cap. Trigger keywords will be cut.")
        elif combined > LISTING_CAP * 0.8:
            warn(f"description + when_to_use is {combined} chars, close to the "
                 f"{LISTING_CAP} cap.")

    lines = len(text.splitlines())
    if lines > MAX_LINES:
        fail(f"SKILL.md is {lines} lines, over the {MAX_LINES} guideline. Its "
             f"content persists in context all session. Move detail to "
             f"reference.md.")

    for ref in re.findall(r"`([a-zA-Z0-9_./-]+\.md)`", text):
        if not (ROOT / ref).exists():
            fail(f"SKILL.md references '{ref}', which does not exist.")


def check_json():
    path = ROOT / "evals" / "evals.json"
    if not path.exists():
        fail("evals/evals.json missing.")
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"evals.json is not valid JSON: {exc}")
        return

    cases = data.get("cases", [])
    if not cases:
        fail("evals.json has no cases.")
        return

    ids = [c.get("id") for c in cases]
    if len(ids) != len(set(ids)):
        fail("evals.json has duplicate case ids.")

    for case in cases:
        if not case.get("assertions"):
            fail(f"eval case '{case.get('id')}' has no assertions.")

    cats = {c.get("category") for c in cases}
    for required in ("removal", "restraint", "triggering"):
        if required not in cats:
            warn(f"No eval cases in category '{required}'. Restraint and "
                 f"no-trigger cases catch over-application, which is the "
                 f"main failure mode.")


def check_required_files():
    for name in ("README.md", "reference.md", "SOURCES.md", "LICENSE"):
        if not (ROOT / name).exists():
            fail(f"{name} missing.")


def check_nesting():
    # The original bug this repo exists to fix.
    for sub in ROOT.iterdir():
        if sub.is_dir() and sub.name not in {".git", ".github", "evals", "scripts"}:
            if (sub / "SKILL.md").exists():
                fail(f"Found a nested SKILL.md in '{sub.name}/'. Only the root "
                     f"SKILL.md is loaded. Remove or hoist it.")
        if sub.is_dir() and " " in sub.name:
            fail(f"Directory name '{sub.name}' contains a space. Skill "
                 f"directory names become command names.")


def main():
    check_skill()
    check_json()
    check_required_files()
    check_nesting()

    for w in WARNINGS:
        print(f"warn: {w}")
    for f in FAILURES:
        print(f"FAIL: {f}")

    if FAILURES:
        print(f"\n{len(FAILURES)} failure(s).")
        return 1
    print(f"\nAll structural checks passed"
          f"{f' ({len(WARNINGS)} warning(s))' if WARNINGS else ''}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
