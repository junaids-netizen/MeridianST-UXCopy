---
name: meridian-ux-copy
description: >-
  Meridian - UX Copy: creates and reviews in-product copy for Vera (payments)
  against the Vera Dev Ready Figma source of truth. Use when a PM asks to write,
  draft, review, or align UI copy on payment flows, add-card flows, or payment
  failure states in Figma or specs; when they mention Meridian UX copy, Vera
  copy, payment copy, CB/SB/MAD, or link the Vera Figma file
  (RTp68wPIXZDjWelVBqfTPi).
---

# Meridian - UX Copy

## Source of truth

| Item | Value |
|------|--------|
| Figma file | [Vera — Dev Ready ✅](https://www.figma.com/design/RTp68wPIXZDjWelVBqfTPi/Vera---Dev-Ready-%E2%9C%85) |
| File key | `RTp68wPIXZDjWelVBqfTPi` |
| Pilot section | `24190:32359` (Section 1 — payments) |

**How the file encodes use cases**

- **Full UI frames** (`payments`, white/`#FAFAFA` background): canonical strings for dev and review.
- **Dark label frames** (`#121212` background, large white Geist Bold text): scenario metadata only — flow name + variant (e.g. `Payment failure reattempt` / `Insufficient balance`). Do not treat label text as user-facing UI copy unless a full UI frame for that variant exists.
- **Hidden layer** `First time experience`: audience flag for copy variants (FnF vs returning). Respect `OUT OF SCOPE for FnF` annotations on label frames.

When the user selects a frame in Figma, read that node with `get_design_context` (`excludeScreenshot: true` is fine for copy-only work). Match the scenario to [pilot-screens.md](pilot-screens.md) or the expanded catalog when provided.

## Modes

Determine mode from the user message:

| Mode | User intent | Agent behavior |
|------|-------------|----------------|
| **Review** | “Check copy”, “does this match Vera”, QA before handoff | Inventory all user-visible strings → compare to reference → report gaps |
| **Create** | “Write copy for…”, new scenario, empty/error state | Ask for scenario + audience (FnF if relevant) → draft strings → map to components |
| **Update** | “Change CTA to…”, iterate on one string | Change only requested slots; re-check consistency with reference |

If mode is unclear, default to **Review** when a Figma node or link is provided; otherwise **Create**.

## Workflow

### 1. Classify the screen

1. Parse `fileKey` / `nodeId` from a Figma URL (`node-id=726-9747` → `726:9747`).
2. Call `get_design_context` on the selected frame.
3. Decide: **full UI** vs **label-only** frame.
4. Record **use case** from frame labels or user description (see taxonomy in [terminology.md](terminology.md)).

### 2. Extract copy inventory

For each full UI frame, list strings by **slot** (fixed order):

1. Navigation title (toolbar)
2. Supporting line (due date, subheads)
3. Status / progress banner
4. Primary amount display (dynamic — note pattern, not fake numbers)
5. Slider / chart labels
6. Form field labels & helper text
7. List rows (payment methods, “Add new”)
8. Primary CTA
9. Secondary CTA(s)
10. Errors, modals, empty states (if present)

Ignore: status bar time, keyboard keys, masked card digits (`•••• 8361`), placeholder amounts in mocks unless reviewing formatting rules.

### 3. Apply Meridian copy rules

Load [terminology.md](terminology.md) for voice, terminology, and formatting. Load [pilot-screens.md](pilot-screens.md) for pilot reference strings.

**Non‑negotiables (pilot set)**

- Product terms in UI: **Current balance**, **Statement balance** (may wrap as “Statement” / “balance”), **Minimum Amount Due** — not internal abbreviations CB/SB/MAD in customer copy.
- Progress banner pattern: `You've paid {amount} so far this statement period` (curly apostrophe in design; ASCII `'` acceptable in specs if engineering constraint).
- Due date pattern: `Due by {Mon} {d} {yyyy}` (example: `Due by Jul 12 2025`).
- Primary payment actions: **Pay now**, **Next**; secondary: **Schedule**, **Enter custom amount**.
- Payment method screen title: **Choose payment method**; add card title: **Add debit card** (trailing space in component is a Figma quirk — ship without trailing space unless design system says otherwise).
- Form labels: **Debit card number**, **Name on card**, **Expiration date**, **CVV**, **Save card details**.
- List action: **Add new** (not “Add a new card” unless a future rule says so).
- Nav title on amount step: **Payment**.
- Sentence case for labels and buttons; proper nouns only where required.

### 4. Deliver output

Use this template:

```markdown
## Meridian - UX Copy — {mode}: {screen name}

**Use case:** {flow} → {variant}
**Figma:** {nodeId} | **Reference:** {pilot or catalog id}

### Copy inventory
| Slot | Current | Reference / recommendation | Status |
|------|---------|---------------------------|--------|
| … | … | … | ✅ / ⚠️ / ❌ |

### Summary
- {1–3 bullets}

### Draft copy (create/update only)
{slot-by-slot final strings ready for Figma}
```

Status legend: ✅ match; ⚠️ minor (punctuation, spacing, wrapping); ❌ wrong term, tone, or missing slot.

### 5. Figma updates (only when asked)

If the user asks to apply copy in Figma: load `/figma-use` skill, then update text nodes via `use_figma`. Do not change layout, colors, or components during copy-only tasks.

## Pilot scope

This skill ships with **5 pilot screens** in [pilot-screens.md](pilot-screens.md). When the user provides the full screen list and rules, replace or extend that file — keep SKILL.md workflow unchanged.

## PM prompts (examples)

**Review:** “Use meridian-ux-copy — review copy on this frame against pilot rules.” (with Figma link or selection)

**Create:** “Use meridian-ux-copy — draft copy for payment failure — insufficient balance, first-time user. Slots: title, body, primary CTA, secondary CTA.”

**Compare:** “Use meridian-ux-copy — does this CTA match the choose-payment-method screen in Vera?”

## Additional resources

- [terminology.md](terminology.md) — voice, abbreviations, failure-flow taxonomy
- [pilot-screens.md](pilot-screens.md) — five pilot frames + canonical strings
- [examples.md](examples.md) — sample review outputs
