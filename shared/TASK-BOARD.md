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
| TASK-016 | Build the event location map picker (Google-style search and tap a named place, address field, per-event note) from the Phase 1 designs | Deepak | To Do | | | | Proposed by Elvis 2026-08-18. Grounded in DEC-003 and the Phase 1 place-picker screens; needed for event / idea create and location polls. Candidate for engineering-handoff. |
| TASK-015 | Investigate pushing design output (HTML) from Cowork desktop to the repo | Aakash | To Do | | | | Ref todos #5. Would let Elvis push designs straight to the repo. |
| TASK-014 | Finish the profile screens; add the draft-save and profile-description screens; finalize the map-picker detail | Elvis (+ Deepak) | To Do | | | | Ref todos #6-#9, DEC-003. Elvis design backlog from the 2026-08-17 walkthrough. |
| TASK-013 | Consult a lawyer on the age/location logic | Aakash | To Do | | | | Ref todos #4, risk R1, DEC-002. Keep the age/location logic provisional until counsel. |
| TASK-012 | Reconcile the walkthrough-vs-draft conflicts once Elvis's reviewed docs land | Elvis + Aakash | Blocked | | | | Ref todos #11. Waits on TASK-010. Conflicts: ratings, comments, video, age 18-vs-19, Kakao/OTP, DM/calendar phase tags. |
| TASK-011 | Create the Wepop GitHub repo, invite Elvis, run the Cowork setup call | Aakash | In progress | 2026-08-18 | | | Ref todos #3. Repo live; Elvis invited and accepted (step 1 done). Setup call scheduled 2026-08-19. Invite goes to programinator-elvis. |
| TASK-010 | Elvis sends the reviewed project documentation | Elvis | To Do | | | | Ref todos #1. Reviewed final of Phase 1 Brief v2 + Moments v0.9. |
| TASK-009 | Send Elvis the review aid, the how-to note, and the Slack message | Aakash | In progress | 2026-08-18 | | | Ref todos #10. All three are drafted and ready to send. |
| TASK-008 | Set up the task board (source + skill + inline client view) | Aakash | In progress | 2026-08-18 | | | This board. Moves to Done once pushed with TASK-008 in the commit message. |
| TASK-007 | Write the Elvis onboarding guide (GET-STARTED-ELVIS) + PDF | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | Linked from the README. |
| TASK-006 | Add 6 PM skills, the README catalogs, and scrub Sapey from the blueprint | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | Toolkit reached 28 here; repo now Wepop-only. |
| TASK-005 | File Elvis's draft docs and produce the validated review aid | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | comms/attachments/2026-08-18_elvis-draft-docs/. Review aid independently validated. |
| TASK-004 | Log Elvis's GitHub ID and update the harness gate | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | Ref todos #2. programinator-elvis. |
| TASK-003 | Add run-merge and update-tracker skills and seed PROJECT_TRACKER | Aakash | Done | 2026-08-18 | 2026-08-18 | 2026-08-18 | The merger routine and the status roll-up. |
| TASK-002 | Ingest the 2026-08-17 walkthrough; land DEC-001 to DEC-009 and risks R1-R3 | Aakash | Done | 2026-08-17 | 2026-08-17 | 2026-08-17 | Source of truth seeded from the design walkthrough. |
| TASK-001 | Stand up the Wepop docs repo and the PM skills toolkit | Aakash | Done | 2026-08-17 | 2026-08-17 | 2026-08-17 | Repo scaffold, rulebook, workspaces, toolkit, dashboard. |

## Next id

Next task id: **TASK-017** (never reuse a number).
