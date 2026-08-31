# Wepop phase-1 effort estimate (AI-assisted build)

> Owner: Aakash (phase-plan). Others suggest via `suggestions/`. Derived, grounded only in a landed
> decision or a design note; never invented scope. When this disagrees with `shared/DECISIONS.md`,
> DECISIONS wins. Generated 2026-08-28 against the phase-1 line in `wepop-scope-matrix.md` and
> DEC-001 to DEC-033. No em-dashes.

## What this is, and how to read it

A build-effort estimate for the phase-1 feature set, sized in **AI-accelerated dev-days**: focused
engineering days for one developer (Deepak) pairing with Claude for the build. The AI speedup is
already baked into every number here; a traditional hand-coded estimate would run materially higher.

Each line is a low-to-high range, not a single point, because most features still carry open design
or integration questions. "Dev-days" means productive engineering days, not calendar days. See
**Calendar translation** at the end for the difference, which is large.

**AI leverage** column tells you how much the Claude-pairing speedup actually helps that item:

- **High** - mostly schema, CRUD, UI from existing designs, standard app plumbing. Claude accelerates
  this the most.
- **Medium** - real logic, careful state, or a well-documented integration. Claude helps, but the
  developer drives the design and verifies hard.
- **Low** - novel algorithm design, a third-party integration with real-world credentials and edge
  cases, media/realtime infrastructure, or anything safety-, privacy-, or money-critical where the
  bottleneck is human judgment, testing, and review, not typing. AI helps least here.

The lower an item's AI leverage, the less its estimate would shrink from adding more AI, and the more
it depends on the developer's own throughput.

## Foundations (built once, most of phase 1 sits on these)

| Work | AI leverage | Dev-days | Grounding / notes |
|------|-------------|----------|-------------------|
| Codebase assessment + scaffolding + CI/envs | Medium | 3-6 | Salvage-and-extend the existing Wepop code (DEC-008); assess what is reusable before building on it. |
| Core data model + backend (users, events, ideas, orgs, follows, tags) | High | 5-9 | The schema most features hang off. Follows are bidirectional (DEC-017). |
| Design system + component library from Elvis's screens | High | 4-7 | Reuse across every surface; depends on final screens (todos #14, still open). |
| i18n architecture (externalized strings, Korean locale, profile language field, notification hookup) | Medium | 4-7 | DEC-029/DEC-027. Ground-floor, day-1; painful to retrofit. Full bilingual coverage of WePop copy. |
| Auth foundation: social login + phone always required | Low | 5-9 | DEC-011. Kakao/Apple/Google plus phone OTP (Twilio-style); real third-party credentials and flows. |
| Age gate + country cascade | High | 2-4 | DEC-012. Config table plus cascade logic; provisional pending counsel (TASK-013), so expect rework. |
| Map picker + reverse-geocode to neighborhood + fallback chain | Medium | 4-7 | DEC-003 picker reused; DEC-031 adds neighborhood-level reverse-geocode, discard-precise-coordinate, and a neighborhood/postal/city fallback chain for markets without a clean tier. |
| Notifications infra (push, SMS, email), language-aware | Low | 4-6 | DEC-029 requires the pipeline to read the profile language field; three delivery channels, each an integration. |

Foundations subtotal: **31 to 55 dev-days.**

## Feature build (phase-1 line)

| Feature | AI leverage | Dev-days | Linked DEC / notes |
|---------|-------------|----------|--------------------|
| Invite-first onboarding + waitlist + auto-promote/claim | High | 3-5 | DEC-024. |
| Location-at-registration UI | High | 2-3 | DEC-016/DEC-031; mostly rides on the map-picker foundation. |
| Personality/interest tags (extensible) | High | 2-4 | DEC-005; bilingual tag labels under one canonical ID (DEC-029). |
| Events + Ideas core flows (create/edit/view) | High | 4-7 | walkthrough, DEC-009. |
| Event schedule / itinerary | High | 2-4 | DEC-025; ordered stops reuse the picker; multi-day date range still to confirm. |
| QR check-in (required) | Medium | 3-5 | DEC-014; generation, scan, and the gating other features depend on. |
| Ratings + 3-step post-event feedback | High | 3-5 | DEC-014; skippable, check-in gated. |
| Moments (photo + 720p video, caps, visibility) | Low | 6-10 | DEC-015; the self-hosted 720p transcode pipeline (DEC-018 infra note) is the hard, low-AI-leverage part. |
| Live stories (ephemeral 24h) | Medium | 4-6 | DEC-025; separate content type; expiry and audience tiers. |
| Anti-stalking pre-join visibility | Medium | 3-5 | DEC-006/DEC-017; bidirectional follow checks, gender-as-ratio, aggregate rendering. Correctness-critical. |
| DM + user-created group chats (text) | Low | 6-9 | DEC-013; realtime messaging infrastructure. |
| Event/group chat (photos, replies, reactions) | Medium | 3-5 | DEC-009/DEC-013; extends the chat core. |
| Calendar: busy-time ingestion + add-to-calendar | Low | 3-5 | DEC-013; device-calendar platform APIs (read free/busy, discard rest). |
| Community cohorts (segmentation) | Medium | 3-5 | DEC-019, simplified by DEC-030 to a student/not binary plus the university three-signal check; per-city density review is now one global call. |
| Recommendation algorithm (two-stage, ranking, keyword extraction, logging, admin keyword view) | Medium | 10-16 | DEC-020. The single largest algorithmic build; design-heavy, AI assists but does not replace the design work. |
| Group-dynamics signals (ranking inputs) | Medium | 3-5 | DEC-023; depends on the two prerequisites below. |
| Prerequisite: general user-blocking capability | High | 2-3 | DEC-023; undesigned, likely a phase-1 safety baseline. |
| Prerequisite: attendee-level feedback (thumbs) | High | 2-3 | DEC-023; the avoid-signal data source. |
| Event icebreakers (host question game) | High | 2-3 | DEC-025; up to 3 read-only questions, check-in gated. |
| Tips/guides | High | 1-3 | DEC-025; contextual info plus static guide, copy written later. |
| Org profiles + ownership transfer | High | 3-5 | DEC-024; transfer is structural for club officer turnover. |
| Public org track-record module | High | 2-4 | DEC-024; event count and rating history. |
| Org analytics tier (paid) + org billing | Low | 6-10 | DEC-018; the one live monetization piece in phase 1. Per-org billing, 7-day trial, rollup/export split. Billing is a money-critical integration. |
| Payment provisions (gated, not live) | Medium | 2-4 | DEC-010; interfaces plus a toggle only. Full payments go-live is phase 1.5. |

Feature-build subtotal: **80 to 134 dev-days.**

## Admin, ops, and safety (cross-cutting, phase-1 required)

| Work | AI leverage | Dev-days | Grounding / notes |
|------|-------------|----------|-------------------|
| Content moderation tooling (4 surfaces, plus Korean-language) | Medium | 5-9 | HOTSHEET launch blocker: host-rating comments (DEC-014), moment comments (DEC-015), DM/group chat (DEC-013), Free Now rooms (DEC-025). Build only; staffing and SLA are a separate, unresolved decision. |
| "Give Feedback" channel + Admin Portal table | High | 2-3 | DEC-029 doc; one form, three intents, writes to an Admin Portal table. |
| Admin Portal baseline (internal keyword view, moderation queues, feedback, analytics access) | Medium | 4-7 | Assembles the surfaces above into the existing Admin Portal access model. |

Admin/ops subtotal: **11 to 19 dev-days.**

## Uplifts and contingency

| Line | Dev-days | Why |
|------|----------|-----|
| QA, integration, security and privacy hardening (~20%) | 25-42 | Claude can generate tests, but safety (anti-stalking), privacy (PIPA, DEC-029), and money (billing) paths need human review and real QA. Applied to the three subtotals above. |
| Contingency for open design + legal-driven rework (~15%) | 18-31 | Undesigned prerequisites, the provisional age/location logic (R1/TASK-013), and Korea specifics that may force rework. |

## Phase-1 total (one developer + Claude)

| Bucket | Dev-days (low to high) |
|--------|------------------------|
| Foundations | 31-55 |
| Feature build | 80-134 |
| Admin / ops / safety | 11-19 |
| QA + hardening (~20%) | 25-42 |
| Contingency (~15%) | 18-31 |
| **Phase-1 total** | **165 to 281 AI-accelerated dev-days** |

Working midpoint: roughly **220 dev-days** for phase 1, for one developer pairing with Claude.

### Excluded from the total (call out separately)

- **Korea PASS carrier verification (DEC-026): 5-10 dev-days, AI leverage Low.** A Korea-specific
  identity-verification integration explicitly flagged as possibly handled by a freelancer, and gated
  on TASK-013 legal confirmation. Kept out of the one-developer total because the owner is unsettled;
  add it back if Deepak builds it in-house.
- The **redacted-ID fallback review flow** (Korea, DEC-026 doc): flow only is confirmed, tooling and
  reviewer process undesigned. Not sized.

## Calendar translation (read before quoting a date)

Dev-days are focused engineering days, not calendar days. For a single developer, real calendar
throughput is typically 3 to 4 productive engineering-days per working week once meetings, reviews,
context-switching, client turnaround, and blocked-on-a-decision time are removed. On that basis:

- 220 dev-days at ~3.5/week is roughly **12 to 15 calendar months solo.**
- The band across the full 165 to 281 range is roughly **10 to 19 calendar months solo.**

This is a large phase 1 for one developer even with AI pairing. The honest read is that hitting a
launch inside 6 months would need either a tighter phase-1 cut (defer the recommendation algorithm's
full weighting, live stories, or org analytics), a second developer on the low-AI-leverage tracks
(auth, payments/billing, chat infra, media pipeline), or both. That is a scope and staffing call for
Aakash, not something AI throughput alone closes.

## Biggest estimate risks (where the numbers are least certain)

- **Recommendation algorithm (10-16):** design-heavy and the largest single item; real scope depends
  on how much of DEC-020's ranking and keyword layers ships at launch versus later.
- **Moments media pipeline (6-10):** self-hosted 720p transcode is genuine infrastructure, low AI
  leverage; cost and effort both hinge on the DEC-018 infra choice (R2, self-hosted transcode).
- **Auth + billing + chat (low-AI-leverage cluster):** these three do not shrink much with AI and set
  the practical floor on the timeline.
- **Provisional age/location logic (DEC-012, R1):** locked before counsel could force rework; the
  contingency line covers a moderate hit, not a redesign.

_Regenerate this estimate after a scope change, a design intake that lands new phase-1 detail, or once
Deepak has assessed the salvaged codebase (which will sharpen the Foundations and every High-leverage
line)._
