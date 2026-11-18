# Zero Clutter checks for copy

The copy subset of [Zero Clutter](https://github.com/prithvi-zeta/zero-clutter)
(v0.4.3), the quality gate built on Bhavin's Design for Delight principles.
IDs and severities are Zero Clutter's, so a copy review here and a full
Zero Clutter gate name the same problem the same way. The wording below is
shortened for copy; when in doubt, Zero Clutter's
`references/checklist-items.md` is the source.

Checks that need a device, a recording or code (haptics, sound, timing, hit
areas, contrast) are out of scope here. Leave them to a full `zero-clutter` run.

Severity: **blocking** (can't ship), **major** (fix before review), **minor** (fix or note).
Principle order is priority order: when two checks conflict, the earlier one wins.

## Tests used by the checks

- **Removal test** (CLUT-01): for each string, name the question it answers or
  the action it enables. If removing it breaks nothing the user needs at that
  moment, remove it. "Context", "reassurance", "branding" and "looks empty"
  don't count as reasons.
- **Read-alone test** (WORD-02): read a label with nothing around it. Money
  labels carry their noun ("$32 statement balance", not "$32"). Commit labels
  name the action ("Pay $32", not "Confirm"). Status labels say whose state it is.
- **Scan-layer test** (WORD-03): read only the large or bold text, numbers and
  the CTA. You should still know what the screen is for, the key value and
  what to do. Every line leads with its key word.
- **Purpose test** (PROG-01): "This screen lets you ___" in 5 words or fewer,
  without "and". The nav title should be close to that answer.
- **Word budget** (WORD-01): Zero Clutter asks for the shortest version that
  passes the read-alone test. Meridian's default budgets until the full rules
  arrive:

  | Slot | Budget |
  |------|--------|
  | Nav title | 3 words |
  | Button (CTA) | 1–3 words |
  | Field label | 3 words |
  | Banner / supporting line | 6 words |
  | Error or success title | 4 words |
  | Error or success body | 1 sentence, 12 words |

## Zero Cognitive Load: first use

| ID | Severity | Copy check |
|----|----------|------------|
| ZCL-01 | blocking | No instruction text, tooltip, coachmark or "Tap/Swipe to…" hint on the primary path. |
| ZCL-04 | major | Every tappable's label predicts what happens when it's tapped. |
| ZCL-05 | blocking | No System 2 triggers in copy: mental arithmetic; recalling a value from an earlier screen; decoding a term; more than 1 sentence or 2 lines of body text above the decision control; a negation or double negative in a label, toggle or option; not being able to tell whether the last action worked. |

## 1. Zero clutter

| ID | Severity | Copy check |
|----|----------|------------|
| CLUT-01 | major | Every string passes the removal test, in every state (empty, error, success, loading), including below the fold. |
| CLUT-02 | blocking | Every fact the user needs for this screen's decision is on this screen. Nothing to guess, go back for or remember. |
| CLUT-03 | major | Rows: a title plus at most one secondary line, with at most 2 facts on that line. |
| CLUT-05 | major | One visible control per outcome. No two buttons that do the same thing. |

## 2. Fewer words

| ID | Severity | Copy check |
|----|----------|------------|
| WORD-01 | major | Every new or changed string is the shortest version that passes the read-alone test, within its word budget, with no filler. |
| WORD-02 | major | Money, status and commit labels pass the read-alone test. |
| WORD-03 | major | The screen passes the scan-layer test; every line leads with its key word. |
| WORD-04 | major | Nothing said twice on a screen: no content word echoed between title and subtitle, or a row title and its secondary line. |
| WORD-05 | minor | Everyday words only: no internal terms or abbreviations (CB, SB, MAD, Tabapay, response code), one term per concept across app, web and native. |
| WORD-06 | major | Each claim or confirmation is said once per flow: not restated on a later step, no toast repeating a change already visible, no push, inbox row and toast all announcing one event. |

## 3–5. Defaults, one context, hierarchy

| ID | Severity | Copy check |
|----|----------|------------|
| DEF-01 | major | No copy asking for something the product already knows ("Enter your phone number" when it's on file). Flag as a product call. |
| PROG-01 | major | The screen passes the purpose test. |
| PROG-04 | major | A footnote or qualifier appears with the thing it qualifies, never before it. |
| HIER-01 | major | The screen's hero is a value or a state ("$32", "Paid"), not a label. |
| HIER-07 | minor | Copy follows the order the user decides: what, how much, from/to, when/cost, act. The CTA comes after every fact it commits to. |

## 6–9. Feedback, consistency, familiar, choices

| ID | Severity | Copy check |
|----|----------|------------|
| FB-04 | major | Invalid input gets a caption at the field, at the moment it's wrong. |
| FB-06 | minor | A toast only when nothing can change in place. |
| CONS-03 | major | A fact on two consecutive screens keeps its wording. |
| CONS-07 | blocking | Every fact (rate, fee, limit, time) and term has one value and one wording on every surface. |
| MENT-03 | major | Dates, money and numbers in the user's native locale format, from one shared formatter. |
| CHOICE-02 | major | An option the user can't use right now shows a 1–2 word reason. |
| CHOICE-05 | minor | A dialog can be answered from its buttons alone: verbs that name the outcome, the safe option primary, the downside stated plainly. |
| CHOICE-06 | minor | Optional setup or upsell has a one-tap skip that leads to no second decision. |

## Engage the Senses

| ID | Severity | Copy check |
|----|----------|------------|
| SENSE-11 | major | Delight comes from motion, haptics and sound, not extra words. Success copy stays short. |

## The Science behind Delight: money, errors, trust

| ID | Severity | Copy check |
|----|----------|------------|
| SCI-01 | major | A completion makes the concrete outcome the hero, plus at most one true fact that's better than promised. |
| SCI-02 | blocking | Every cost, net amount and delay is stated before the commit control; limits are stated when they'll bite. |
| SCI-03 | major | Every pending, processing or scheduled state says when it completes and what happens next. |
| SCI-06 | minor | Use the user's own context where known: card last 4, their name, their bank's name. |
| SCI-07 | major | No guilt, threats or vague loss framing. A downside is stated once, as a plain, specific fact. |
| SCI-08 | major | Gains and savings are stated as numbers, not feature sentences. |
| SCI-11 | blocking | At a commit control, the amount, source, fee and arrival are readable above it without scrolling, with a reassurance line where the user may fear harm. |
| SCI-12 | blocking | A money failure says where the money is now and offers a one-tap recovery. |
| SCI-13 | major | An error says what happened and offers one next step as a tappable action, inline, in calm words with no blame. |
| SCI-14 | major | Alarm wording only for states that need action. A lockout warns first and states the reset time. |
| SCI-18 | blocking | A validation caption names the limit that actually bound, with the amount left. |
| SURF-01 | major | Push notifications, widgets and lock-screen copy are held to the same checks. |

## Copy integrity

These decide what the agent is allowed to change.

| ID | Severity | Rule |
|----|----------|------|
| HR-04 / PROC-08 | blocking | Approved copy (from the Figma Dev Ready file, a ticket or a spec) is used word for word, including capitals. A typo goes to the copy owner as a question, not a silent fix. |
| HR-05 / PROC-08 | blocking | Nothing invented. Every new string is marked **(new, needs approval)** until the approver signs it off. No placeholder copy, footnotes or disclaimers. Legal text stays intact. |
| PROC-07 | blocking | When approved copy breaks a check, don't change it. Report it as a **Decide** row with a proposal. |
| HR-06 | major | A story, pitch, onboarding or success screen says one thing: one statement under one visual. |

The approver is whoever owns the flow's copy. Zero Clutter's default approver is Bhavin.
