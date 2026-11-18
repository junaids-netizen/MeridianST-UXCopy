#!/usr/bin/env python3
"""Validate Meridian - UX Copy against Zero Clutter checklist IDs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZC_REF = (
    Path.home()
    / "Documents/zero-clutter/skills/zero-clutter/references"
)


def load_zero_clutter_ids() -> dict[str, str]:
    items = (ZC_REF / "checklist-items.md").read_text()
    rules = (ZC_REF / "house-rules.md").read_text()
    ids = {m[0]: m[1] for m in re.findall(r"\*\*([A-Z]+-\d{2})\*\* · (\w+)", items)}
    ids.update({m: "major" for m in re.findall(r"### (HR-\d{2})", rules)})
    return ids


def ids_in_copy_checks() -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for line in (ROOT / "zero-clutter-copy.md").read_text().splitlines():
        if not line.startswith("| "):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 4 or parts[1] in ("ID", "---"):
            continue
        sev = parts[2]
        if sev not in ("blocking", "major", "minor"):
            continue
        for token in re.findall(r"[A-Z]+-\d{2}", parts[1]):
            found.append((token, sev))
    return found


def main() -> int:
    if not ZC_REF.is_dir():
        print(
            "FAIL: Zero Clutter repo not found at ~/Documents/zero-clutter",
            file=sys.stderr,
        )
        return 1

    required = [
        "SKILL.md",
        "README.md",
        "terminology.md",
        "pilot-screens.md",
        "examples.md",
        "zero-clutter-copy.md",
    ]
    for name in required:
        if not (ROOT / name).is_file():
            print(f"FAIL: missing {name}", file=sys.stderr)
            return 1

    skill = (ROOT / "SKILL.md").read_text()
    if not re.search(r"name:\s*meridian-ux-copy", skill):
        print("FAIL: SKILL.md missing meridian-ux-copy name", file=sys.stderr)
        return 1

    theirs = load_zero_clutter_ids()
    ours = ids_in_copy_checks()
    missing = sorted({i for i, _ in ours if i not in theirs})
    if missing:
        print(f"FAIL: unknown Zero Clutter IDs: {missing}", file=sys.stderr)
        return 1

    sev_bad = [
        (i, s, theirs[i])
        for i, s in ours
        if i in theirs
        and not i.startswith("HR")
        and theirs[i].replace("blocker", "blocking") != s
    ]
    if sev_bad:
        print(f"FAIL: severity mismatch vs Zero Clutter: {sev_bad}", file=sys.stderr)
        return 1

    print(
        f"Meridian copy check passed: {len(ours)} ID references, {len(required)} files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())