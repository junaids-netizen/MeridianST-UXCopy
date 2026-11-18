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

Top-level bucket is usually **Payment failure reattempt**. Each variant's customer copy must pass the checks listed (IDs in [zero-clutter-copy.md](zero-clutter-copy.md)):

| Variant (spec label) | Copy must… | Checks |
|----------------------|------------|--------|
| Retry with another payment method | Say the payment failed, that nothing was charged, and offer the other method as the primary CTA | SCI-12, SCI-13 |
| Insufficient balance (+ optional **Change Amount**) | Name the card (last 4), say nothing was charged, offer one recovery as the primary CTA | SCI-06, SCI-12, SCI-13 |
| Tabapay category 1 / 2 or 3 response code | Plain-language reason only; never the processor name or code | WORD-05, SCI-13 |
| Try adding the same card again | Say what to do differently, or that the card can't be added; no blame | SCI-13, SCI-07 |
| CVC limit exhausted (Saved payments, Adding payment method, …) | Warn before the last attempt; when locked, state when it resets | SCI-14, SCI-18 |
| Payment Limit exhausted (Adding payment method → Selecting Debit card) | Name the limit that bound and what's left | SCI-18, SCI-02 |
| Max no. of cards (5) | State the limit ("up to 5 cards") and offer the recovery (remove a card) | SCI-18, SCI-13 |

"Nothing was charged" is a fact to confirm with engineering for each variant before it ships; until then it's a **Check** row.

For **Review** mode: map the user's frame to this taxonomy, then check whether a **full UI** frame exists in file. Label-only frames define scenario identity, not final error strings.

## Voice & tone (inferred from Dev Ready UI)

- **Clear and neutral** — state facts (amounts, due dates, limits); no blame, guilt or threats (SCI-07, SCI-13).
- **Concise** — within the word budgets in [zero-clutter-copy.md](zero-clutter-copy.md) (WORD-01).
- **Consistent action verbs** — Pay now, Next, Schedule, Enter custom amount, Add new. Never mix "Pay now" / "Make payment" / "Pay" (CONS-07).
- **Financial precision** — currency with `$` prefix; amounts in mocks are placeholders.
- **No jargon** — processor names (Tabapay) stay in spec labels, not in customer copy unless compliance requires (WORD-05).
- **Completion moments** (payment made, card added): the outcome is the hero; motion and haptics carry the delight, so copy stays short (SCI-01, SENSE-11).
- **Custom interactions** (e.g. the payment slider): novel UI still uses familiar words.

## Formatting

- **Due date:** `Due by {Mon} {d} {yyyy}` (approved; see known findings in pilot-screens.md for the MENT-03 comma question)
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
