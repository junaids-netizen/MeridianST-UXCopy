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
