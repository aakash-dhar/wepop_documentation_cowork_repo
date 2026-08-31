# TASK-041 - Adopt the I-N invariant registry into CLAUDE.md

## Overview
Adopt the handoff spec's I-N invariant numbering into CLAUDE.md as a maintained registry, so the IDs the
spec cites (I-6 through I-20) resolve to something a reader here can look up. CLAUDE.md section 8 currently
carries key invariants as an unnumbered bullet list, so those citations refer to nothing checkable.

One correction is required before adoption, not after: I-12 as drafted reads "no mechanic may create a
persistent peer rating of an individual that is visible to anyone," which forbids host ratings on its face
and contradicts DEC-014. Elvis confirmed 2026-08-29 that host rating and attendee rating are separate
concepts and host rating is permitted; replacement wording is in the intake note. Adopting the numbering
without that fix would land a contradiction into the registry. Also fix the known-stale CLAUDE.md section 8
line flagged 2026-08-26 (the phone-OTP invariant predating DEC-011) in the same pass.

## Sources
- doc | handoff spec v0.9 | | section 13 invariants
- decision | DEC-014 | shared/DECISIONS.md | host rating permitted, the I-12 conflict
- decision | DEC-011 | shared/DECISIONS.md | auth model, the stale phone-OTP line
- doc | intake note item A | workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md | I-12 replacement wording
- proposal | elvis proposed-tasks 2026-08-30 | | filed the task

## Activity
- 2026-08-31 | Created by the merger, landed from elvis proposed-tasks (2026-08-30).

## Definition of done
- [ ] I-N registry added to CLAUDE.md, resolving the spec's citations
- [ ] I-12 re-scoped to distinguish participant rating from host rating (no DEC-014 contradiction)
- [ ] Stale phone-OTP invariant line corrected to reflect DEC-011
- [ ] Existing section-8 bullets mapped onto the numbered scheme

## Blockers
(none)
