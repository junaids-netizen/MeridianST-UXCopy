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

**Limit scenario (spec only until full UI provided):** max 5 cards — customer-facing error/toast copy TBD in full rules pass.

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

**Create-mode placeholder structure** (do not ship without compliance review):

| Slot | Draft pattern |
|------|----------------|
| error_title | Payment failed |
| error_body | Not enough balance on this card. |
| primary_cta | Use another card |
| secondary_cta | Change amount |

Replace with approved strings when design adds the full frame.

---

## Pilot checklist (agent self-test)

After editing [pilot-screens.md](pilot-screens.md) or global rules, re-run review on nodes: `726:9747`, `726:27155`, `5231:32513`, `726:21014`, `5149:35157`.
