# Proposed risk register change from elvis, 2026-08-30 - for merger review

> Two new risks surfaced by the 2026-08-29 intake of
> `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx`. Both are companions to HOTSHEET entries filed
> the same day in `workspaces/elvis/proposed-hotsheet.md`; filed here as risks because both have a real
> likelihood-times-impact shape and an owner, and neither is captured by R1 to R3.
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Proposed Risk
**Date:** 2026-08-30
**Proposed by:** Elvis
**Risk:** Single-reviewer moderation. The rota is one person (Elvis) until employees are hired, covering
eleven reportable target types across five live UGC surfaces (Discussion on every event and idea, DM and
user-created group chats, Moment comments, Moments themselves, and Free Now rooms). Three distinct failure
modes follow from the count being one rather than two, and they are not the same risk. **Coverage:** there
is no cover for sleep, travel, or illness, so an urgent report (sexual content, minors, 불법촬영, threats,
self-harm) raised overnight sits until one specific person wakes up. **Independence:** the appeal design
requires review by whoever did not make the first decision, which is structurally impossible with one
reviewer, so appeals are not independent until a second person exists. **Capacity:** launch volume should
genuinely be within one person's reach given the invite-first, single-city cold start, so the real exposure
is growth outpacing hiring rather than launch day itself.
**Likelihood:** Medium
**Impact:** High
**Mitigation:** Ship the load reducers already designed in, which are what make one reviewer viable at
launch scale at all: one generic report model feeding a single queue rather than per-surface tooling,
idempotent repeat reports so one user cannot inflate volume, auto-hide on a double condition (5+ distinct
reporters AND at least 10 percent of distinct viewers) so urgent-class content is already hidden before a
human looks, and a `brigade_suspected` flag making coordinated reporting visible. Track the four day-one
metrics (reports per 1,000 Moments, median time-to-decision, backlog depth, appeal overturn rate) and use
them as the hiring trigger rather than as compliance measures, so the ceiling is found before an incident
rather than during one. Note that auto-hide is doing unusually heavy lifting under a single-reviewer setup:
it is the only thing standing between an urgent report and a sleeping reviewer, so its thresholds should
not be loosened without revisiting this risk.
**Owner:** Elvis
**Status:** ACTIVE

## Proposed Risk
**Date:** 2026-08-30
**Proposed by:** Elvis
**Risk:** 위치정보법 registration exposure. The printed-poster check-in mode constrains scans to a
location radius, which is location-data collection and may require 위치기반서비스사업 신고 to the KCC
before it can ship in Korea, the launch market. Shipping the geofence without an answer risks operating an
unregistered location-based service; waiting on an answer with no fallback planned risks blocking P0.
**Likelihood:** Medium
**Impact:** High
**Mitigation:** Route to DLG Law before the geofence ships (companion HOTSHEET entry filed the same day,
marked BLOCKING before P0). A clean fallback already exists and should be treated as the default if
registration proves burdensome: drop the radius constraint and rely on the time window plus live-display
mode, where the QR regenerates every 60 seconds from a short-TTL signed token so a forwarded screenshot
dies within a minute. Live display is already the default check-in mode, so the fallback costs the
printed-poster path some anti-forgery strength rather than costing the feature. Residual exposure is
further limited by the pending DEC-014 amendment: once eligibility decouples from check-in, a forged
check-in unlocks a badge and nothing else.
**Owner:** Aakash
**Status:** ACTIVE
