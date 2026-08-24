# Elvis - Session detail, 2026-08-19 through 2026-08-24

One continuous session, spanning several real days of work without a restart. Covers the full
draft-vs-walkthrough conflict review (all ten items plus one escalation) and the complete freemium
business model, individual and organization tiers, fully priced.

## What got done

**Conflict review, `workspaces/elvis/conflict-review-2026-08-19.md`, all items closed except one
follow-up.**

- Items 1-6 (the six headline conflicts flagged in the 2026-08-18 review aid): ratings and reviews,
  login (Kakao/OTP/password), age gate, comments on moments, video length and photo cap, DM/group
  chat/calendar phasing. All RESOLVED 2026-08-19, each with a conflict/resolution/flags write-up
  matching the repo's decision-record style, ready to promote into `proposed-decisions.md`.
- Item 7, location at registration (open question O1): RESOLVED 2026-08-24. Split into a required
  typed city/university field at onboarding, and an optional, contextually-nudged device GPS
  permission, keeping the two signals distinct from item 3's country cascade.
- Item 8, gender and photos pre-join: RESOLVED 2026-08-24. Aggregate gender ratio shown pre-join;
  individual attendee photos withheld pre-join except between mutual follows, to close a
  one-way-follow stalking vector DEC-006 was written to prevent.
- Item 9, the ten undiscussed drafted surfaces (QR check-in, waitlist auto-promote, co-hosts,
  apply-to-join, series pages, org history/track-record, org ownership transfer, Sunday Deck,
  memories resurfacing, Wrapped): RESOLVED 2026-08-24. Phase 1 keeps waitlist auto-promote, org
  ownership transfer, and a public org track-record module; the rest move to later phase. Wrapped
  corrected from "semester" to "annual," spans both org and individual levels.
- Item 10, names/budget/legal in the Moments doc (Ratnadeep Deshmane, Joy Jeong, ~$100K budget line,
  DLG Law): ESCALATED to Aakash as financials owner, no design work attempted, commercial/legal
  content only.
- Open follow-up, not yet started: series pages were given a phase-1.5 build target, but recurring
  events themselves have never been scoped anywhere in this project, and series pages cannot exist
  without that concept first. Elvis asked for this to be defined and scoped now even though the build
  lands later. This is the next thing to pick up.

**Freemium model, `workspaces/elvis/freemium-model-2026-08-19.md`, fully priced end to end.**

- Governing principle: never gate marketplace actions, quota-gate personal expression, insight-gate
  analytics.
- Individual tier, RESOLVED: $3.99/month or $36/year (~25% annual discount). 30-second video vs 15
  free, 20 media items per moment vs 10 free, aggregate engagement analytics on the user's own
  events/ideas/moments. Ship timing held, not phase 1, pending real usage data.
- Organization tier, RESOLVED: $19.99/month or $199/year (~17% annual discount), per-organization
  billing. Free baseline covers per-event operational numbers (views, joins, waitlist, check-in,
  ratings); paid layer adds cross-event rollups, attendee composition, member activity, segment/tag
  performance with progressive-unlock thresholds, and PDF/CSV export with reimbursement-grade
  invoicing. 7-day trial, monthly/annual billing, grandfathering left open.
- Media caps, RESOLVED: 50 items per attendee per event at org-paid events (revised down from an
  initial 100 once the price was set), "most generous cap wins" precedence across free individual (10)
  / paid individual (20) / org-sponsored event (50).
- Media infrastructure cost model, added 2026-08-24: modeled against real Cloudflare R2, AWS
  S3/CloudFront, AWS MediaConvert, and Cloudflare Stream pricing. Recommends R2 over S3+CloudFront
  (free egress matters for repeatedly-viewed social content) and self-hosted transcode over Cloudflare
  Stream (roughly 10x cheaper for short single-rendition clips), flagged for Deepak. Retention window
  locked at 12 months, then archive. Extreme-tail usage (~$24.60/month cost) handled by a manual
  safety-valve flag rather than automated overage billing or defensive pricing; the $19.99 price point
  was set against a realistic-upper usage scenario (~$6.15/month cost, ~55% margin net of App
  Store/Play Store commission), not the extreme case.
- Deferred, not designed: ticketing/transaction fees (flagged as likely the largest single piece of
  technical scope in the project), ads/ad-bidding, gamification/points.
- Governance flag carried forward, unresolved: no `proposed-project-strategy.md` proposal channel
  exists in CLAUDE.md section 6 for this content to route to `PROJECT_STRATEGY.md`'s commercial
  structure section. Content stays in the workspace draft until Aakash adds the channel or says
  otherwise.

## Files touched this session

- `workspaces/elvis/conflict-review-2026-08-19.md` (created and iterated throughout)
- `workspaces/elvis/freemium-model-2026-08-19.md` (created and iterated throughout)
- No edits to any `shared/` file, CLAUDE.md, or either draft doc. Everything stayed in-workspace,
  correctly, since promotion to `shared/` is merger-only (Aakash).

## Carried forward, open

- Series pages / recurring events: needs its own scoping conversation, next thing to pick up.
- Both tiers' exact annual-discount percentages are now actually set (individual ~25%, org ~17%,
  see above); this closes an item earlier entries in this file might still show as open.
- Org tier grandfathering policy: explicitly left undecided.
- Governance gap on the `proposed-project-strategy.md` channel: unresolved, flagged for Aakash.
- Items 1-9 above are RESOLVED in this workspace file but not yet promoted into
  `workspaces/elvis/proposed-decisions.md` in `PROPOSAL-TEMPLATES.md` format. That promotion step has
  not been started yet.
- Item 10 and the Moments-doc budget/legal content have not yet actually been sent to Aakash, only
  marked ready to escalate in this file.

TASK-012 remains Blocked on TASK-010 (Elvis's reviewed documentation) on the board, unchanged this
session.
