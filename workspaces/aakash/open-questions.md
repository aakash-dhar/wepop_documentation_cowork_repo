# Open questions - aakash workspace

> Running list of questions routed to other people so they do not get lost in session
> logs. Owner is who must answer. Update status as answers land. No em-dashes.

## Open

| # | Question | Owner | Raised | Source | Status |
|---|----------|-------|--------|--------|--------|
| Q1s | Private-account design sub-items still open: approval-queue UX, and whether declining a follow request notifies the requester. (Stranger-view and findability answered by Elvis's 2026-09-02 Moments/org proposals: non-mutuals see name, username, cover and background; mutuals see the full profile incl Moments; account stays findable by name/username.) | Elvis | 2026-09-02 | private-accounts-2026-08-26.md; moments-2026-09-02.md | Open (2 of 4 remain) |
| Q3b | Org-paid Moment video length: all attendees of a paid-org event get 30s (with a notice) vs org-members-only. | Elvis | 2026-09-02 | 2026-09-02 call; DEC-018 | Open (Elvis reconsidering, confusion risk) |
| Q4b | Ideas archiving: can an archived idea be un-archived, and can you comment on an archived idea (commenting revives it)? | Elvis | 2026-09-02 | 2026-09-02 call; DEC-040 | Open (Elvis to research with Claude) |
| Q3c-w | Media retention window: 6 vs 12 months before downgrade. | Aakash + Elvis | 2026-09-02 | 2026-09-02 call; DEC-039 | Open (decide later; free-trial defers it) |
| Q5a | Push the self-report intent flow design so it can be documented; confirm host-notify vs roster and whether "running late" carries an ETA. | Elvis | 2026-09-02 | DEC-046 doc gap; ratings-checkin-2026-08-31.md | Open (not discussed on call) |
| Q5b | What "check-in surfaces in analytics" means concretely (surface, per-event vs rollup). | Elvis | 2026-09-02 | DEC-046 open note | Open |
| Q5c | Is the "claimed but unconfirmed" attendance state visible to the attendee, or is the host nudged before auto-close? | Elvis | 2026-09-02 | DEC-046 open note | Open |
| Q5d | Edited rating: shows as "edited" or changes silently within the 7-day window? | Elvis | 2026-09-02 | DEC-047 open note | Open |
| Q6 | Explore: own manual location refresh vs shared with home feed? Can a GPS-granted user opt back to the coarser stored default? | Elvis | 2026-09-02 | DEC-031 open note | Open |
| D1 | Deliverables owed: consolidated design doc, CSAM runbook draft + moderation guideline (Elvis is reviewer). | Elvis | 2026-09-02 | Session 2026-08-31 flags; TASK-039; R4 | Open |
| D2 | Plan Mode spec (code tree, superseded by handoff v0.9): decide design-intake into architecture/elvis vs treat as superseded; Elvis confirms what still stands. | Aakash (design-intake), Elvis (confirm) | 2026-09-02 | code tree; 2026-08-31 flag correction | Open |

## Answered

| # | Question | Answered | When |
|---|----------|----------|------|
| Q1 | Private accounts phase 1 or deferred? | Phase 1, confirmed by Elvis. Design sub-items tracked as Q1s above. | 2026-09-02 call |
| Q2 | Cohort hard filter soften at density? Explore loosen? | Not a hard filter at all: cohort + network + distance as ranking signals; network events cross cohorts; location stays a hard constraint. Density de-hardening is a manual, later call, no auto logic built. | 2026-09-02 call |
| Q3a | Total video-duration cap per Moment? | No total-duration cap; the media-item count per moment (10 free) is the governing cap. Per-clip 15s free / 30s paid, uniform across moments and event covers. | 2026-09-02 call |
| Q3c | Retention past boundary: 1080p vs thumbnail? | Mid-res ~1080p (not a thumbnail); original always kept, advance-warning before downgrade. Window (6 vs 12 mo) still open, see Q3c-w. | 2026-09-02 call |
| Q4a | Detached idea regains owner? | No owner-takeover mechanism in phase 1; an ownerless idea survives (deferred). | 2026-09-02 call |
| Q4c | Archived ideas in Explore or direct-link only? | Direct-link/save only; not recommended or shown in feed; nothing deleted. | 2026-09-02 call |
| Q4d | Notify interested users on archive? | No, archived quietly (auto after ~6 mo inactivity). | 2026-09-02 call |
| Q7 | Free Now rails: standing, duration, auto-close, org rooms; live stories cap. | Individuals only, not orgs; free, no standing gate; creator sets duration with a timer; auto-close on window end and inactivity. Live stories are separate, uncapped, not counted against the org 50-item cap. (Free Now and live stories are deferred features.) | 2026-09-02 call |
