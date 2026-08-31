# TASK-039 - CSAM preserve-and-report runbook

## Overview
Write a one-page CSAM (child sexual abuse material) preserve-and-report runbook that any moderation
reviewer can follow unaided, and have DLG Law review it before launch. This is a hard pre-launch legal
gate, distinct from TASK-034's moderation tooling and SLA scope, because it is a written legal procedure
rather than infrastructure.

It matters specifically because the intuitive engineering and moderator response, delete it, is the
legally wrong action. The required handling is preserve, restrict access, and report to the authorities;
deleting destroys evidence. With the moderation rota at one reviewer plus a to-be-hired second, the
runbook is also what makes the procedure transferable rather than living in one person's head. It governs
what happens after the urgent lane auto-hides the content, not whether it is caught.

## Sources
- decision | DEC-034 | shared/DECISIONS.md | check-in decouple context for moderation load
- risk | moderation Blocking + R4 | shared/HOTSHEET.md | single-reviewer moderation
- doc | handoff spec v0.9 | | section 12.5, legal register L-12 (불법촬영물 under 전기통신사업법)
- proposal | elvis proposed-tasks 2026-08-30 | | filed the task

## Activity
- 2026-08-31 | Created by the merger, landed from elvis proposed-tasks (2026-08-30).

## Definition of done
- [ ] One-page runbook written, followable without calling Elvis at the moment it happens
- [ ] Procedure is preserve, restrict access, report (never delete)
- [ ] DLG Law has reviewed it
- [ ] Linked from the moderation guideline (TASK-034)

## Blockers
- Soft-depends on DLG Law engagement (see TASK-040 legal-register consult).
