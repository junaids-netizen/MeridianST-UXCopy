# Meridian - UX Copy — example outputs (pilot)

## Example: Review P3 — pass

**Use case:** Pay flow → choose payment method  
**Figma:** `726:27155`

| Slot | Current | Reference | Status |
|------|---------|-----------|--------|
| nav_title | Choose payment method | Choose payment method | ✅ |
| field_label_cvv | CVV | CVV | ✅ |
| list_action | Add new | Add new | ✅ |
| secondary_cta | Schedule | Schedule | ✅ |
| primary_cta | Pay now | Pay now | ✅ |

**Summary:** All pilot strings match P3. No changes required.

---

## Example: Review P1 — minor flag

| Slot | Current | Reference | Status |
|------|---------|-----------|--------|
| progress_banner | You have paid $5.00 this period | You've paid $5.00 so far this statement period | ❌ |
| primary_cta | Continue | Next | ❌ |

**Design for Delight**

| Check | Result | Note |
|-------|--------|------|
| D8 | ❌ | "Continue" — Vera uses "Next" for this step |
| D2 | ⚠️ | Reference banner is 9 words; known tension, raise with design |

**Summary:** Banner wording and CTA diverge from Vera pilot. Restore reference strings or document an approved exception.

---

## Example: Create — insufficient balance (P5)

**Use case:** Payment failure reattempt → Insufficient balance (FnF)

| Slot | Draft |
|------|--------|
| error_title | Payment failed |
| error_body | Not enough balance on this card. |
| primary_cta | Use another card |
| secondary_cta | Change amount |

**Design for Delight:** passes D1–D10. Title and body don't repeat each other (D3); the fix is the primary CTA (D10); no processor terms (D9).

**Summary:** Draft follows taxonomy in terminology.md; confirm with legal/compliance before Figma implementation.
