# TASK-BOARD.md - Wepop task tracking

> Merger-only file. The source of truth for task-level execution tracking. It is shown **inside
> Claude desktop as the live "wepop-task-board" view** (no file download): ask Claude to "show the
> task board" and it opens in the side panel, where each task card opens its full details. Maintained
> by the **task-board** skill. Everyone else suggests task changes via
> `workspaces/[you]/suggestions/suggestion-task-*.md`; the merger (Aakash) lands them. Complements
> `comms/todos.md` (raised action items) and `shared/PROJECT_TRACKER.md` (status snapshot). No
> em-dashes. Dates are YYYY-MM-DD.

## Conventions

- **ID:** `TASK-NNN`, zero-padded, never reused, never renumbered.
- **Status:** `To Do` (not started) / `In progress` (being worked) / `Blocked` (waiting) / `Done` (finished and pushed).
- **Started:** date it moved to In progress. **Ended:** date it moved to Done.
- **Committed:** date (and short ref) the work was pushed, filled by the task-board skill from
  `git log`. Put the task id in the commit message (for example `[aakash] TASK-012 ...`) so it matches
  automatically. Blank until pushed.
- **Notes:** a short one-line summary for the row.
- **Detail:** the full side-panel content (Overview, Linked sources, Activity, Definition of done,
  Blockers) lives in `team/tasks/TASK-NNN.md`. The ingestion skills append linked sources and
  activity lines there as calls, emails, and Slack come in. See `team/tasks/_TEMPLATE.md`.

## Board

| ID | Task | Owner | Status | Started | Ended | Committed | Notes |
|----|------|-------|--------|---------|-------|-----------|-------|
| TASK-037 | Resolve the commercial-structure proposal channel and update PROJECT_STRATEGY.md with the freemium model | Aakash | To Do | | | | Governance gap: no proposed-project-strategy channel. DEC-018. Financials owner. |
| TASK-036 | Scope the payments/ticketing build (Stripe Connect style splitting, host KYC, refunds, tax) and decide whether it is phase 1 | Aakash | To Do | | | | DEC-010, DEC-018. Flagged largest technical scope in the project; own dedicated conversation. |
| TASK-035 | Confirm the cohort softening transition and who owns the manual per-city density call, with Elvis | Aakash | To Do | | | | DEC-019, DEC-020. Two mechanism transitions assumed but unconfirmed. |
| TASK-034 | Stand up content moderation (owner, SLA, tooling) across rating comments, moment comments, chat, and Free Now (LAUNCH BLOCKER) | Aakash | To Do | | | | HOTSHEET Blocking. Answers Moments OQ-9. Report/block/rate-limit baseline required. |
| TASK-033 | Design a general user-blocking feature and an attendee-level (thumbs) feedback mechanism | Elvis (+ Deepak) | To Do | | | | DEC-023 prerequisites, both undesigned. Blocking for group-dynamics recommendations. |
| TASK-032 | Build recurring events, Event Series, and co-hosts (phase 1.5) | Deepak (+ Elvis) | To Do | | | | DEC-021, DEC-022. Linked instances + recurring_group_id; series many-to-many; co-hosts permission. |
| TASK-031 | Build Free Now (real-time availability + location-pinned rooms) with safety baselines | Deepak (+ Elvis) | To Do | | | | DEC-025, highest safety flag. Rounded location, aggregate-first, reciprocal join, room-creation gating, moderation baseline. Open details to confirm with Elvis. |
| TASK-030 | Build live stories (ephemeral 24h, RSVP to post, poster-chosen 4-tier audience) | Deepak (+ Elvis) | To Do | | | | DEC-025. Media-cap interaction vs org tier open. |
| TASK-029 | Build the contained phase-1 features: event schedule, icebreakers (host question game), tips/guides | Deepak (+ Elvis) | To Do | | | | DEC-025. Schedule multi-day depends on Event date-range (TASK-028 confirm). |
| TASK-028 | Confirm the Event data model (multi-day date range) and other schema prerequisites with Deepak | Deepak | To Do | | | | DEC-025, DEC-021, DEC-022. recurring_group_id, series join table, cohort/keyword storage, follow-state bidirectional check. |
| TASK-027 | Build the org analytics tier, billing/invoicing, and gated (not live) payment provisions | Deepak (+ Aakash) | To Do | | | | DEC-018, DEC-010. Free/paid analytics split, per-org billing, 7-day trial, R2 storage + self-hosted transcode. |
| TASK-026 | Build community cohorts and the two-stage recommendation algorithm with day-one logging | Deepak | To Do | | | | DEC-019, DEC-020, DEC-023. Retrieval hard filter + weighted ranking; Explore map/list split; new-host boost. |
| TASK-025 | Build calendar busy-time ingestion (times only) and manual add-to-calendar | Deepak | To Do | | | | DEC-013. Full in-app calendar deferred to phase 1.5. |
| TASK-024 | Build DM and user-created group chats (text only) plus event/group chat | Deepak | To Do | | | | DEC-013. Live messaging infra: delivery, presence, push. Third moderation surface. |
| TASK-023 | Build moments (one per user per event, visibility model, video 720p/H.264/15s, server-side transcode) | Deepak | To Do | | | | DEC-015. React/comment/share; most-restrictive-wins; 10-item cap. |
| TASK-022 | Build ratings and the three-step post-event feedback flow with required QR check-in | Deepak | To Do | | | | DEC-014. Check-in gates ratings, reputation, recommendations, moments. Attendee thumbs internal-only. |
| TASK-021 | Build anti-stalking pre-join visibility (gender aggregate, photos to mutual follows only) | Deepak | To Do | | | | DEC-006, DEC-017. Enforce bidirectional follow-state server-side. |
| TASK-020 | Build the age gate and country cascade (self-declared birthdate, store-region cascade, per-country config) | Deepak | To Do | | | | DEC-012. Provisional pending counsel (TASK-013). No forced GPS prompt. |
| TASK-019 | Build auth: social login (Kakao/Apple/Google) + always-required phone, OTP fallback, email magic-link recovery, biometrics | Deepak | To Do | | | | DEC-011 (superseded DEC-004). Password deferred. Kakao verified-phone skip Korea-only. |
| TASK-018 | Add a chat assistant to the client delivery board so status can be asked in natural language | Aakash | To Do | | | | Later-phase enhancement from the 2026-08-19 Elvis setup call. Board already serves status visually. |
| TASK-017 | Build Elvis's client-specific input skill so he feeds info in the structure the dev harness expects | Aakash | In progress | 2026-08-19 | | | From the 2026-08-19 Elvis setup call. In progress on Aakash's side. |
| TASK-016 | Build the event location map picker (Google-style search and tap a named place, address field, per-event note) from the Phase 1 designs | Deepak | To Do | | | | Proposed by Elvis 2026-08-18. Grounded in DEC-003 and the Phase 1 place-picker screens; needed for event / idea create and location polls. Candidate for engineering-handoff. |
| TASK-015 | Investigate pushing design output (HTML) from Cowork desktop to the repo | Aakash | Done | 2026-08-19 | 2026-08-19 | | Ref todos #5. Finding: no direct Claude Design -> repo push and the GitHub connect is read-only; Elvis exports Standalone HTML then pushes via GitHub Desktop. Drop folders + onboarding set up. |
| TASK-014 | Finish the profile screens; add the draft-save and profile-description screens; finalize the map-picker detail | Elvis (+ Deepak) | To Do | | | | Ref todos #6-#9, DEC-003. Elvis design backlog from the 2026-08-17 walkthrough. |
| TASK-013 | Consult a lawyer on the age/location logic | Aakash | To Do | | | | Ref todos #4, risk R1, DEC-002. Keep the age/location logic provisional until counsel. |
| TASK-012 | Reconcile the walkthrough-vs-draft conflicts once Elvis's reviewed docs land | Elvis + Aakash | Done | 2026-08-19 | 2026-08-26 | | Ref todos #11. Resolved via the 2026-08-26 Elvis intake: all conflicts landed as decisions (DEC-011 auth, DEC-012 age, DEC-013 chat/calendar, DEC-014 ratings, DEC-015 moments/video, DEC-017 gender/photos, DEC-024 undiscussed surfaces). |
| TASK-011 | Create the Wepop GitHub repo, invite Elvis, run the Cowork setup call | Aakash | Done | 2026-08-18 | 2026-08-19 | | Ref todos #3. Repo live; Elvis invited and accepted. Setup call held 2026-08-19 (14 min): walked commit/push, start/end session, merge model, design/doc drop folders, and the board. |
| TASK-010 | Elvis sends the reviewed project documentation | Elvis | To Do | | | | Ref todos #1. Reviewed final of Phase 1 Brief v2 + Moments v0.9. |
| TASK-009 | Send Elvis the review aid, the how-to note, and the Slack message | Aakash | Done | 2026-08-18 | 2026-08-19 | | Ref todos #10. Confirmed sent by Aakash. |
| TASK-008 | Set up the task board (source + skill + inline client view) | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | Setup shipped and pushed (commit references TASK-008). Later brand / chart / board-sync work is separate. |
| TASK-007 | Write the Elvis onboarding guide (GET-STARTED-ELVIS) + PDF | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | Linked from the README. |
| TASK-006 | Add 6 PM skills, the README catalogs, and scrub Sapey from the blueprint | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | Toolkit reached 28 here; repo now Wepop-only. |
| TASK-005 | File Elvis's draft docs and produce the validated review aid | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | comms/attachments/2026-08-18_elvis-draft-docs/. Review aid independently validated. |
| TASK-004 | Log Elvis's GitHub ID and update the harness gate | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | Ref todos #2. programinator-elvis. |
| TASK-003 | Add run-merge and update-tracker skills and seed PROJECT_TRACKER | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | The merger routine and the status roll-up. |
| TASK-002 | Ingest the 2026-08-17 walkthrough; land DEC-001 to DEC-009 and risks R1-R3 | Aakash | Done | 2026-08-17 | 2026-08-17 | 2026-08-17 | Source of truth seeded from the design walkthrough. |
| TASK-001 | Stand up the Wepop docs repo and the PM skills toolkit | Aakash | Done | 2026-08-17 | 2026-08-17 | 2026-08-17 | Repo scaffold, rulebook, workspaces, toolkit, dashboard. |

## Next id

Next task id: **TASK-038** (never reuse a number).
