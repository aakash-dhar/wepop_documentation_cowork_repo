# Proposed HOTSHEET changes from elvis, 2026-08-26 - for merger review

## Proposed Hotsheet Entry
**Date:** 2026-08-26
**Proposed by:** Elvis
**Source:** `workspaces/elvis/internationalization-korea-2026-08-26.md`
**Type:** Needs Attention
**Summary:** Stripe's actual support for Korea-based payments (KRW payout, Korean local payment methods) is unconfirmed and may not cover what DEC-010/DEC-018's org tier billing needs for the Korea launch market.
**Key Points:**
- DEC-010 commits to using Programination's existing Stripe account for all payments. DEC-018's org tier is proceeding now, not held, so this is not a distant-future concern.
- Checking Stripe's current documentation for Korea coverage did not confirm whether a Korea-based merchant relationship, KRW payouts, or Korean local payment methods (KakaoPay, Naver Pay, direct bank transfer/virtual account) are supported the way Korean org-tier customers would need. Korean consumers strongly prefer these local methods over card payment.
- Korea has established local payment processors built for exactly this (Toss Payments, NHN KCP, PortOne/Iamport are the standard names), worth evaluating alongside or instead of Stripe for the Korea market specifically.
- Payments/financials sit with Aakash per OWNERS.md. DEC-010 already flags a dedicated payments conversation as needed; this raises its urgency given Korea is the launch market, not a later-expansion market.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Confirm directly with Stripe whether it actually supports Korea-based merchant payouts and Korean local payment methods for the org tier; evaluate a Korea-specific processor (Toss Payments, NHN KCP, or PortOne) if it does not | Aakash | TBD |
