# Meridian - UX Copy — pilot screens (5)

File: `RTp68wPIXZDjWelVBqfTPi` · Section `24190:32359`

Use these as the reference set until the full catalog is added.

---

## P1 — Payment amount (partial pay / MAD selected)

| Field | Value |
|-------|--------|
| **ID** | `P1-payment-amount-partial` |
| **Node** | `726:9747` |
| **Spec label** | (full UI — partial payment with progress banner) |
| **URL** | [Open in Figma](https://www.figma.com/design/RTp68wPIXZDjWelVBqfTPi/Vera---Dev-Ready-%E2%9C%85?node-id=726-9747) |

**Canonical copy**

| Slot | String |
|------|--------|
| nav_title | Payment |
| meta_date | Due by Jul 12 2025 |
| progress_banner | You've paid $5.00 so far this statement period |
| slider_label_top | Current balance |
| slider_label_mid | Statement / balance (two lines) |
| slider_label_bottom | Minimum Amount Due |
| secondary_cta | Enter custom amount |
| primary_cta | Next |

---

## P2 — Payment amount (baseline CB / SB / MAD)

| Field | Value |
|-------|--------|
| **ID** | `P2-payment-amount-baseline` |
| **Spec frame (label only)** | `726:21014` |
| **Reference UI** | `726:9747` or `5261:35142` (same copy set; different scenario state) |
| **Spec text** | CB: $133 / SB: $32 / MAD: $5 |

**Canonical copy:** same slot table as P1 (without progress banner if scenario has no prior payment in spec).

---

## P3 — Choose payment method

| Field | Value |
|-------|--------|
| **ID** | `P3-choose-payment-method` |
| **Node** | `726:27155` |
| **URL** | [Open in Figma](https://www.figma.com/design/RTp68wPIXZDjWelVBqfTPi/Vera---Dev-Ready-%E2%9C%85?node-id=726-27155) |

**Canonical copy**

| Slot | String |
|------|--------|
| nav_title | Choose payment method |
| field_label_cvv | CVV |
| list_action | Add new |
| secondary_cta | Schedule |
| primary_cta | Pay now |

---

## P4 — Add debit card

| Field | Value |
|-------|--------|
| **ID** | `P4-add-debit-card` |
| **Node** | `5231:32513` |
| **Spec label frame** | `5282:41557` — `add debit card` / `Max no. of cards(5)` |
| **URL** | [Open in Figma](https://www.figma.com/design/RTp68wPIXZDjWelVBqfTPi/Vera---Dev-Ready-%E2%9C%85?node-id=5231-32513) |

**Canonical copy**

| Slot | String |
|------|--------|
| nav_title | Add debit card |
| field_debit_number | Debit card number |
| field_name | Name on card |
| field_expiration | Expiration date |
| field_cvv | CVV |
| checkbox | Save card details |
| secondary_cta | Schedule |
| primary_cta | Pay now |

**Limit scenario (spec only until full UI provided):** max 5 cards. Customer-facing copy is TBD; when it's written it must state the limit and offer the recovery (SCI-18, SCI-13), e.g. "You can save up to 5 cards" + "Remove a card" (new, needs approval).

---

## P5 — Payment failure reattempt — insufficient balance

| Field | Value |
|-------|--------|
| **ID** | `P5-failure-insufficient-balance` |
| **Spec frame (label only)** | `5149:35157` |
| **Taxonomy** | Payment failure reattempt → Insufficient balance |
| **Related spec** | `5261:35135` adds **Change Amount** variant |

**Canonical UI copy:** not present on label frame. For pilot **Review**, report:

- Scenario classification ✅ against taxonomy
- User-facing error title/body/CTAs ❌ *missing — requires full UI frame or PM-supplied draft*

**Create-mode draft** (all strings new, needs approval; do not ship without compliance review):

| Slot | Draft | Words |
|------|-------|-------|
| error_title | Payment failed | 2 |
| error_body | Not enough balance on •••• {last4}, so nothing was charged. | 9 |
| primary_cta | Use another card | 3 |
| secondary_cta | Change amount | 2 |

The body names the card (SCI-06), says where the money is (SCI-12) and stays one sentence above the CTAs (ZCL-05). "Nothing was charged" must be confirmed with engineering. Replace with approved strings when design adds the full frame.

---

## Known findings on approved pilot copy

These strings stay as the reference (PROC-07). Reviews report them as **Decide** rows with the proposal below until the approver rules.

| Pilot | Slot | Approved string | ID | Finding | Proposal (new, needs approval) |
|-------|------|-----------------|----|---------|--------------------------------|
| P1 | progress_banner | You've paid $5.00 so far this statement period | WORD-01, WORD-03 | 9 words, over the 6-word banner budget; the amount isn't first | $5.00 paid this statement period |
| P1 | meta_date | Due by Jul 12 2025 | MENT-03 | US date format has a comma after the day | Due by Jul 12, 2025 |
| P1 | slider_label_bottom | Minimum Amount Due | Sentence case rule | Title Case, unlike every other label | Minimum amount due |
| P3 | list_action | Add new | WORD-02 | Read alone, "new" what? | Add card |

---

## Pilot checklist (agent self-test)

After editing [pilot-screens.md](pilot-screens.md) or global rules, re-run review on nodes: `726:9747`, `726:27155`, `5231:32513`, `726:21014`, `5149:35157`.
