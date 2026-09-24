# Meridian - UX Copy — terminology & taxonomy

## Internal vs customer language

| Internal (labels on dark spec frames) | Customer-facing (UI) |
|--------------------------------------|----------------------|
| CB | Current balance |
| SB | Statement balance |
| MAD | Minimum Amount Due |

Never ship CB/SB/MAD in user-visible copy.

## Payment amount scenarios (Section 1)

Common spec labels on dark frames (not exhaustive — full catalog TBD):

- `CB: $133 SB: $32 MAD: $5` — baseline three-tier slider
- `MAD paid - Slider starts $0` — partial pay progress
- `CB = SB`, `CB = SB = MAD`, `Decimals` — slider constraint variants
- `Increments in steps of 5 (When sliding)` — interaction rule; copy unchanged unless PM adds helper text
- `Schedule` — scheduled payment entry (paired full UI elsewhere)

## Failure & limits taxonomy (spec labels)

Top-level bucket is usually **Payment failure reattempt**. Sub-variants include:

- Retry with another payment method
- Insufficient balance (+ optional **Change Amount**)
- Tabapay category 1 / 2 or 3 response code
- Try adding the same card again
- CVC limit exhausted (with context: Saved payments, Adding payment method, …)
- Payment Limit exhausted (Adding payment method → Selecting Debit card)

For **Review** mode: map the user's frame to this taxonomy, then check whether a **full UI** frame exists in file. Label-only frames define scenario identity, not final error strings.

## Voice & tone (inferred from Dev Ready UI)

- **Clear and neutral** — state facts (amounts, due dates, limits); avoid blame.
- **Concise** — short nav titles; button labels 1–3 words where possible.
- **Consistent action verbs** — Pay now, Next, Schedule, Enter custom amount, Add new.
- **Financial precision** — currency with `$` prefix; amounts in mocks are placeholders.
- **No jargon** — processor names (Tabapay) stay in spec labels, not in customer copy unless compliance requires.

## Design for Delight principles (copy)

From the CEO's Design for Delight principles. The goal is **zero cognitive load**: a first-time user never needs instructions, takes the right first action instinctively, and never switches into analytic mode. Principles are in priority order; when two conflict, the higher one wins.

| # | Principle | Copy rule |
|---|-----------|-----------|
| D1 | Zero clutter | Every string must be necessary for the outcome. Remove intro lines, restated titles, "Please note" lines, and helper text the user can succeed without. |
| D2 | Use fewer words | If one word works, don't use two. Buttons 1–3 words. Put the key fact (amount, date, action) first so the line can be scanned, not read. |
| D3 | Don't repeat | A fact appears once per screen. If the nav title says it, the body and CTA don't restate it. |
| D4 | Smart defaults | Don't ask for what the system knows or can fill. No "Enter your…" instructions for values that can be pre-filled. |
| D5 | One page, one context | Copy covers only the current step. Limits, fees and edge cases appear where they apply, not up front. |
| D6 | Hierarchy | One primary line per block; supporting detail goes in secondary text. Don't use long sentences to carry emphasis. |
| D7 | Instant feedback | Every action gets an immediate, specific result message: "Payment scheduled", not "Success!". Inline errors sit next to the field they refer to. |
| D8 | Consistency | Same word for the same thing everywhere (see terminology above). Never mix "Pay now" / "Make payment" / "Pay". |
| D9 | Familiar mental models | Use words users know from banking apps. No internal or processor terms (CB/SB/MAD, Tabapay, response code) in UI. |
| D10 | Fewer analytical choices | Options must be distinguishable from their labels alone. No near-synonym pairs ("Continue" vs "Next"). The recommended action is the primary CTA, in plain words. |

**Completion moments** (payment made, card added, milestone reached): short, warm success copy. Animation and haptics carry the delight; copy stays brief.

**Custom interactions** (e.g. the payment slider): novel UI still uses familiar vocabulary.

**Review test:** if the copy needs explaining, or a first-time user would pause to think, flag it.

### Known tensions with approved pilot copy

These canonical strings stay as reference (✅ for consistency), but reviews should add a ⚠️ D-note so design can decide:

| String | Principle | Note |
|--------|-----------|------|
| You've paid $5.00 so far this statement period | D2 | 9 words; long for a scannable banner |
| Minimum Amount Due | Sentence case rule | Title Case, unlike the rest of the UI |

## Formatting

- **Due date:** `Due by {Mon} {d} {yyyy}`
- **Statement period progress:** `You've paid {amount} so far this statement period`
- **Card mask:** `•••• {last4}` (UI); do not spell out “last four digits” in labels
- **CVV:** all caps in label

## Copy slots (component mapping)

| Slot | Typical component | Notes |
|------|-------------------|--------|
| `nav_title` | toolbar | Geist Medium 18 |
| `meta_date` | text under nav | Geist Regular 12, secondary color |
| `progress_banner` | tooltip/banner | P2 12 |
| `slider_label_*` | chart annotations | P1 14; “Statement” / “balance” may be two lines |
| `field_label_*` | input floating labels | Medium 12–14 |
| `primary_cta` | primary-button | Semibold 18 |
| `secondary_cta` | secondary-button | Semibold 18 |

## Audience flags

- **First time experience** (hidden in Figma): copy may differ for FnF; honor **OUT OF SCOPE for FnF** on spec frames.
- When audience is unknown, default to **returning user** strings from full UI frames.
