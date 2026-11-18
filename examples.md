# Meridian - UX Copy — example outputs (pilot)

## Example: Review P3 (approved copy, one known finding)

| Mode | Screen | Verdict | Blocking | Major | Minor | Decide |
| --- | --- | --- | --- | --- | --- | --- |
| review | Choose payment method (726:27155) | PASS | 0 | 0 | 0 | 1 |

| Slot | Current | Reference | Status |
| --- | --- | --- | --- |
| nav_title | Choose payment method | Choose payment method | ✅ |
| field_label_cvv | CVV | CVV | ✅ |
| list_action | Add new | Add new | ✅ |
| secondary_cta | Schedule | Schedule | ✅ |
| primary_cta | Pay now | Pay now | ✅ |

| # | Kind | ID | Severity | What's wrong | Slot | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Decide | WORD-02 | major | "Add new" doesn't say what's added when read alone | list_action | Add card (new, needs approval) |

| | |
| --- | --- |
| Keep | Every string matches P3 · one primary CTA · no instructions |
| Next | Send 1 to the approver |

---

## Example: Review P1 (drifted copy)

| Mode | Screen | Verdict | Blocking | Major | Minor | Decide |
| --- | --- | --- | --- | --- | --- | --- |
| review | Payment amount (726:9747) | FAIL | 2 | 0 | 0 | 1 |

| Slot | Current | Reference | Status |
| --- | --- | --- | --- |
| progress_banner | You have paid $5.00 this period | You've paid $5.00 so far this statement period | ❌ |
| primary_cta | Continue | Next | ❌ |

| # | Kind | ID | Severity | What's wrong | Slot | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Fix | HR-04 | blocking | Banner reworded without approval | progress_banner | Restore the approved string |
| 2 | Fix | CONS-07 | blocking | "Continue" where Vera uses "Next" for this step | primary_cta | Next |
| 3 | Decide | WORD-01 | major | The approved banner is 9 words, over budget | progress_banner | $5.00 paid this statement period (new, needs approval) |

| | |
| --- | --- |
| Keep | Current balance / Statement balance / Minimum Amount Due wording · Enter custom amount |
| Next | Fix 1 and 2, then send 3 to the approver |

---

## Example: Create — insufficient balance (P5)

| Mode | Screen | Verdict | Blocking | Major | Minor | Decide |
| --- | --- | --- | --- | --- | --- | --- |
| create | Payment failure → Insufficient balance | OPEN | 0 | 0 | 0 | 0 |

| Slot | Copy | Source | Words |
| --- | --- | --- | --- |
| error_title | Payment failed | (new, needs approval) | 2 |
| error_body | Not enough balance on •••• 7531, so nothing was charged. | (new, needs approval) | 9 |
| primary_cta | Use another card | (new, needs approval) | 3 |
| secondary_cta | Change amount | (new, needs approval) | 2 |

| # | Kind | ID | Severity | What's wrong | Slot | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| | Check | SCI-12 | blocking | "Nothing was charged" is unconfirmed | error_body | Engineering confirms a failed payment never takes money |

| | |
| --- | --- |
| Keep | One sentence above the CTAs · names the card · recovery is the primary CTA |
| Next | Confirm the Check row, then send the draft to the approver and compliance |
