# Wepop compliance register - legal, privacy, and compliance exposure

> Owner: Aakash (phase-plan). Others suggest via `suggestions/`. This tracks exposure; it is not legal
> advice. Unresolved legal questions route to counsel (DLG Law) and are marked pending-counsel.
> Grounded only in a decision, a design, or a law reference, never invented. Created 2026-08-26.
> Area: age / privacy / consent / deliverability / minors / moderation / data-retention / payments.
> Status: open / mitigated / pending-counsel / closed. No em-dashes.

| Item | Area | Requirement | Linked DEC / LC | Status | Owner |
|------|------|-------------|-----------------|--------|-------|
| Cross-jurisdiction age gate | age | Self-declared birthdate against a per-country legal-age config; block under-age with a country-named message. Country set once via store-region cascade, no forced GPS. Exact logic (signal conflict, travel jurisdiction) needs counsel before lock. | DEC-012 (was DEC-002), R1 | pending-counsel | Aakash / DLG Law |
| Minors handling | minors | If the age gate lets an under-age user through, the app must block them; under-age accounts must not be created or retained. No feature should surface minors to adults. | DEC-012, DEC-006, DEC-017 | pending-counsel | Aakash / DLG Law |
| OTP / SMS deliverability by region | deliverability | Phone verification can be blocked by geography without an in-region registered business. Email magic-link now covers account recovery. Check regional messaging-provider rules before a new market. | DEC-011 (was DEC-004), R3 | mitigated | Aakash |
| Personal data collection (PIPA / privacy) | privacy | Onboarding collects phone, birthdate, city, gender, university, tags. Needs a privacy policy and lawful basis; Korea PIPA applies in a focus market. | DEC-011, DEC-012, DEC-016, DEC-005 | open | Aakash / DLG Law |
| Behavioral inference disclosure | privacy | The recommender infers interest keywords and hidden internal tags on users and content. This typically needs general privacy-policy disclosure ("we infer interests from usage"), even without exposing the tags. | DEC-020, todos #4 | open | Aakash / DLG Law |
| Anti-stalking pre-join visibility | privacy | Pre-join, show only mutuals plus aggregates; gender aggregate-only; attendee photos only between mutual (bidirectional) follows. Enforce follow-state bidirectionally server-side. | DEC-006, DEC-017 | mitigated | Deepak |
| Free Now real-time location | privacy | Real-time availability plus location-tied rooms is the highest-exposure surface. Rounded location, aggregate-first, reciprocal join, room-creation gating, and report/block/rate-limit moderation are required baselines, enforced server-side. | DEC-025 | open | Elvis / Deepak |
| Photos and media of identifiable people | consent | Moments and live stories carry user photos/video of attendees. Visibility rules (most-restrictive-wins, poster-chosen audience) plus moderation and takedown. Minors in photos raise added exposure. | DEC-015, DEC-025 | open | Elvis / Deepak |
| Calendar data minimization | privacy | Calendar read grants full access (titles, locations, attendees); the app must extract only start/end times and discard the rest. Request contextually, not at onboarding. | DEC-013 | mitigated | Deepak |
| Content moderation (launch blocker) | moderation | Day-one moderation across anonymous host-rating comments, public moment comments, DM/group chat, and Free Now rooms. Needs a named owner and an SLA (Moments OQ-9). | DEC-013, DEC-014, DEC-015, DEC-025 | open | Aakash |
| Media data retention | data-retention | Full-resolution attendee media retained 12 months, then archived (mechanism TBD). Document the retention policy in the privacy policy. | DEC-018 | open | Aakash |
| Attendee contact export excluded | consent | Org tier deliberately excludes attendee contact export; if ever added it needs its own opt-in consent flow, not a quiet bundle. | DEC-018 | mitigated | Aakash |
| Payments: host payouts, KYC, tax | payments | Ticketing (phase 1.5) needs payment-splitting (Stripe Connect style), host identity verification before payout, refund/chargeback handling, and host tax-reporting obligations. Not built in phase 1 (provisions only). | DEC-010, DEC-018 | open | Aakash / DLG Law |
| Reimbursement invoicing (org tier) | payments | Org subscription receipts must read as real invoices (issuer legal name/address, billed party, sequential number, period, amount). Standard business invoicing. | DEC-018 | mitigated | Aakash |

## Open and pending-counsel summary

- **pending-counsel (route to DLG Law via TASK-013):** age gate mechanism, minors handling, PIPA/personal-data basis, payments KYC/tax.
- **open (design/ops action needed):** behavioral-inference disclosure, Free Now safety details, media-of-people moderation, the moderation launch blocker, media retention policy.
- **mitigated (design decision covers it, verify in build):** OTP/email recovery, anti-stalking visibility, calendar minimization, contact-export exclusion, reimbursement invoicing.

## Notes

- No new project risk beyond R1-R3 is raised by this pass; the moderation launch blocker is tracked on
  the HOTSHEET as Blocking rather than as a numbered risk. If Aakash wants it as a formal risk (R4),
  route it via `risk-register`.
- DLG Law and the ~$100K legal/ops budget line appear in Elvis's draft Moments doc and are pending the
  financials-owner escalation (conflict-review item 10); not asserted as engaged here.
