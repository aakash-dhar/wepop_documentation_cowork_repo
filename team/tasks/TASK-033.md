# TASK-033 - Design general user-blocking + attendee feedback mechanism

## Overview
Design the general user-blocking feature and the attendee-level feedback mechanism that DEC-023's
group-dynamics avoid signal depended on. Both were flagged undesigned prerequisites.

Resolved at the design level by the 2026-08-31 merge. DEC-037 fully designs general user blocking as a
phase-1 safety baseline (bidirectional and total across every surface, scope stated at block time,
checked at retrieval time). DEC-036 resolves the feedback half, but by dropping the thumbs up/down
mechanism this task named and replacing it with a single positive-only tap (DEC-034), which feeds a
positive-affinity ranking signal. The avoid signal itself becomes block-only. So the design is
delivered, with a deliberate scope shift away from a negative peer-rating mechanism.

Build of both is tracked as phase-1 rows on the scope matrix (general user-blocking; attendee
positive-only tap), not on this design card.

## Sources
- decision | DEC-037 | shared/DECISIONS.md | general user blocking, phase-1 baseline
- decision | DEC-036 | shared/DECISIONS.md | avoid signal block-only; positive affinity added
- decision | DEC-034 | shared/DECISIONS.md | thumbs replaced by positive-only tap
- decision | DEC-023 | shared/DECISIONS.md | the group-dynamics signal these unblock

## Activity
- 2026-08-31 | Created and closed by board-sync. Design delivered via DEC-036 + DEC-037; thumbs mechanism dropped in favor of a positive-only tap (scope shift). Marked Done.

## Definition of done
- [x] General user-blocking feature designed (DEC-037)
- [x] Attendee-level feedback mechanism resolved (DEC-036, positive-only tap)
- [x] DEC-023 avoid-signal prerequisites closed

## Blockers
(none - resolved)
