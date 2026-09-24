# Meridian - UX Copy

Cursor / Figma agent skill for creating and reviewing **Vera** payment-flow copy against the [Vera Dev Ready Figma file](https://www.figma.com/design/RTp68wPIXZDjWelVBqfTPi/Vera---Dev-Ready-%E2%9C%85).

## Install (PMs)

**Cursor (personal skill — all projects)**

```bash
git clone https://github.com/YOUR_ORG/meridian-ux-copy.git ~/.cursor/skills/meridian-ux-copy
```

If you clone this repo with the folder name `Meridian - UX Copy`:

```bash
git clone https://github.com/YOUR_ORG/Meridian-UX-Copy.git ~/.cursor/skills/meridian-ux-copy
```

**Cursor (team repo)**

```bash
cp -R "Meridian - UX Copy" .cursor/skills/meridian-ux-copy
```

Commit `.cursor/skills/meridian-ux-copy` so everyone gets the same rules.

## Use

1. Connect Figma MCP in Cursor.
2. Prompt: **“Use the meridian-ux-copy skill”** (Meridian - UX Copy) and paste a Figma frame link or select a frame.
3. Ask to **review** or **draft** copy.

Main entry point: [SKILL.md](SKILL.md)

## Contents

| File | Role |
|------|------|
| `SKILL.md` | Agent workflow and output template |
| `terminology.md` | Voice, CB/SB/MAD, failure taxonomy |
| `pilot-screens.md` | 5 pilot frames + canonical strings |
| `examples.md` | Sample review outputs |

## Figma

- File key: `RTp68wPIXZDjWelVBqfTPi`
- Pilot section node: `24190:32359`

Pilot scope will expand when full screen rules are added to `pilot-screens.md` / `terminology.md`.
