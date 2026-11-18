---
name: meridian-ux-copy
description: >-
  Meridian - UX Copy: creates and reviews in-product copy for Vera (payments)
  against the Vera Dev Ready Figma source of truth and the Zero Clutter copy
  checks (Design for Delight). Use when a PM asks to write, draft, review, or
  align UI copy on payment flows, add-card flows, or payment failure states in
  Figma or specs; when they mention Meridian UX copy, Vera copy, payment copy,
  zero clutter copy, CB/SB/MAD, or link the Vera Figma file
  (RTp68wPIXZDjWelVBqfTPi).
metadata:
  version: "0.2.0"
---

# Meridian - UX Copy

## Source of truth

| Item | Value |
|------|--------|
| Figma file | [Vera — Dev Ready ✅](https://www.figma.com/design/RTp68wPIXZDjWelVBqfTPi/Vera---Dev-Ready-%E2%9C%85) |
| File key | See Figma URL path (Vera Dev Ready) |
| Pilot section | `24190:32359` (Section 1 — payments) |
| Copy checks | [zero-clutter-copy.md](zero-clutter-copy.md) — Zero Clutter v0.4.3 IDs |

**How the file encodes use cases**

- **Full UI frames** (`payments`, white/`#FAFAFA` background): canonical strings for dev and review.
- **Dark label frames** (`#121212` background, large white Geist Bold text): scenario metadata only — flow name + variant (e.g. `Payment failure reattempt` / `Insufficient balance`). Do not treat label text as user-facing UI copy unless a full UI frame for that variant exists.
- **Hidden layer** `First time experience`: audience flag for copy variants (FnF vs returning). Respect `OUT OF SCOPE for FnF` annotations on label frames.

When the user selects a frame in Figma, read that node with `get_design_context` (`excludeScreenshot: true` is fine for copy-only work). Match the scenario to [pilot-screens.md](pilot-screens.md) or the expanded catalog when provided.

This skill covers copy only. For layout, hierarchy, motion and haptics, run the full `zero-clutter` skill if it's installed; both use the same check IDs.

## Modes

Determine mode from the user message:

| Mode | User intent | Agent behavior |
|------|-------------|----------------|
| **Review** | “Check copy”, “does this match Vera”, QA before handoff | Inventory all user-visible strings → compare to reference → run the copy checks → report |
| **Create** | “Write copy for…”, new scenario, empty/error state | Ask for scenario + audience (FnF if relevant) → draft strings that pass the checks → map to slots |
| **Update** | “Change CTA to…”, iterate on one string | Change only requested slots; re-run the checks on what changed |

If mode is unclear, default to **Review** when a Figma node or link is provided; otherwise **Create**. Ask at most one question, and only when the screen's job or audience is unknown.

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
10. Errors, modals, empty states, toasts, push notifications (if present)

Ignore: status bar time, keyboard keys, masked card digits (`•••• 8361`), placeholder amounts in mocks unless reviewing formatting rules.

### 3. Apply Meridian copy rules

Load [terminology.md](terminology.md) for vocabulary and formatting, [pilot-screens.md](pilot-screens.md) for reference strings, and [zero-clutter-copy.md](zero-clutter-copy.md) for the checks.

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

**Zero Clutter copy check** (every Review and Create; full checks with IDs and severities in [zero-clutter-copy.md](zero-clutter-copy.md))

- [ ] Clutter: every string passes the removal test, in every state (CLUT-01, CLUT-02)
- [ ] Words: shortest version within budget; money and commit labels pass the read-alone test; key word first; nothing said twice (WORD-01–06)
- [ ] First use: no instructions on the primary path; no copy System 2 triggers such as arithmetic, negations, or more than one sentence above the CTA (ZCL-01, ZCL-05)
- [ ] One context: the screen passes the purpose test (PROG-01)
- [ ] Consistency: every fact and term has one wording everywhere; dates and money in native format (CONS-07, MENT-03)
- [ ] Choices: dialogs answer from their buttons alone (CHOICE-05)
- [ ] Money and errors: costs and limits stated before commit; failures say where the money is plus one recovery action; limit captions name the limit (SCI-02, SCI-12, SCI-13, SCI-18)
- [ ] Integrity: approved copy is word for word; every new string marked **(new, needs approval)** (HR-04, HR-05)

**What you may change**

- **Approved copy** (pilot reference strings, Dev Ready frames, the spec) is never rewritten silently. When it fails a check, keep it and add a **Decide** row with a proposal (PROC-07). Known cases are listed under "Known findings" in [pilot-screens.md](pilot-screens.md).
- **New copy** (Create, Update, or a proposal in a Decide row) must pass every check and is marked **(new, needs approval)**.

### 4. Deliver output

Answer in Markdown tables, in this order. No preamble, no recap of the principles.

```markdown
| Mode | Screen | Verdict | Blocking | Major | Minor | Decide |
| --- | --- | --- | --- | --- | --- | --- |
| review | {screen name} ({nodeId}) | PASS / FAIL (create: READY / OPEN) | n | n | n | n |

| Slot | Current | Reference | Status |
| --- | --- | --- | --- |
| {slot} | {string on screen} | {pilot string, or —} | ✅ / ⚠️ / ❌ |

| # | Kind | ID | Severity | What's wrong | Slot | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Fix | WORD-02 | major | {what's wrong} | {slot} | {the fix} |
| 2 | Decide | MENT-03 | minor | {approved copy that fails a check} | {slot} | {proposal} (new, needs approval) |

| | |
| --- | --- |
| Keep | {1–3 things that work, separated by ·} |
| Next | {the one thing to do now} |
```

- **Verdict:** Review is `PASS` or `FAIL`; Create and Update are `READY` or `OPEN`. `PASS` / `READY` only with 0 blocking findings and no Check row pending on a blocking item. Decide rows on approved copy don't block the verdict.
- **Counts:** Blocking, Major and Minor count Fix and Suggest rows; Decide rows are counted only in the Decide column.
- **Status** in the inventory: ✅ matches reference; ⚠️ minor drift (punctuation, spacing, wrapping); ❌ wrong term or missing slot.
- **Kind:** `Fix` (the team fixes it), `Decide` (only the approver can: approved copy that fails a check, a taste call, a missing fact), `Suggest` (optional; nobody asked), `Check` (needs a fact or a full UI frame).
- **Order:** Fix, Decide, Suggest, Check; within each, blocking → major → minor. Number Fix, Decide and Suggest rows in `#`. At most 10 rows, then `+n more — say "details"`.
- Leave out the findings table on a clean pass.
- **Create / Update mode:** replace the inventory table with a draft table, and run the findings table on the draft:

```markdown
| Slot | Copy | Source | Words |
| --- | --- | --- | --- |
| {slot} | {string} | {pilot ID, or (new, needs approval)} | n |
```

### 5. Figma updates (only when asked)

If the user asks to apply copy in Figma: load `/figma-use` skill, then update text nodes via `use_figma`. Do not change layout, colors, or components during copy-only tasks. Never write a string marked **(new, needs approval)** into Figma until the approver has signed it off.

## Pilot scope

This skill ships with **5 pilot screens** in [pilot-screens.md](pilot-screens.md). When the user provides the full screen list and rules, replace or extend that file — keep SKILL.md workflow unchanged.

## PM prompts (examples)

**Review:** “Use meridian-ux-copy — review copy on this frame.” (with Figma link or selection)

**Create:** “Use meridian-ux-copy — draft copy for payment failure — insufficient balance, first-time user. Slots: title, body, primary CTA, secondary CTA.”

**Compare:** “Use meridian-ux-copy — does this CTA match the choose-payment-method screen in Vera?”

## Additional resources

- [zero-clutter-copy.md](zero-clutter-copy.md) — copy checks with Zero Clutter IDs, tests and word budgets
- [terminology.md](terminology.md) — vocabulary, abbreviations, failure-flow taxonomy
- [pilot-screens.md](pilot-screens.md) — five pilot frames, canonical strings, known findings
- [examples.md](examples.md) — sample outputs
