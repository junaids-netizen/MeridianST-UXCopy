# Meridian - UX Copy

Cursor / Figma agent skill for creating and reviewing copy for Meridian projects.

## Install (PMs)

**Cursor (personal skill — all projects)**

```bash
git clone https://github.com/junaids-netizen/MeridianST-UXCopy.git ~/.cursor/skills/meridian-ux-copy
```

**Cursor (team repo)**

```bash
git clone https://github.com/junaids-netizen/MeridianST-UXCopy.git .cursor/skills/meridian-ux-copy
```

Commit `.cursor/skills/meridian-ux-copy` so everyone gets the same rules.

## Use

1. Connect Figma MCP in Cursor.
2. Prompt: **“Use the meridian-ux-copy skill”** and paste a Figma frame link or select a frame.
3. Ask to **review** or **draft** copy.

You get tables: a verdict, the copy on screen against the approved copy, then numbered findings with Zero Clutter IDs (`Fix`, `Decide`, `Suggest`, `Check`), then what to keep and do next. Any new copy comes back marked **(new, needs approval)**.

Main entry point: [SKILL.md](SKILL.md)

## Contents

| File | Role |
|------|------|
| `SKILL.md` | Agent workflow and output format |
| `zero-clutter-copy.md` | Copy checks with Zero Clutter IDs, tests and word budgets |
| `terminology.md` | Vocabulary, CB/SB/MAD, failure taxonomy |
| `pilot-screens.md` | 5 pilot frames, canonical strings, known findings |
| `examples.md` | Sample outputs |
| `scripts/check.py` | Validates skill files and Zero Clutter ID references |

## Test

```bash
python3 scripts/check.py
```

## Works with Zero Clutter

This skill checks copy only. The full [Zero Clutter](https://github.com/prithvi-zeta/zero-clutter) gate covers layout, hierarchy, motion and haptics. Both use the same check IDs, so findings line up between the two.

## Figma

- File key: the segment after `/design/` in the Vera Dev Ready link above
- Pilot section node: `24190:32359`

Pilot scope will expand when full screen rules are added to `pilot-screens.md` / `terminology.md`.
