# TASK-040 - Route the handoff legal register (L-1..L-12) to DLG Law

## Overview
Route the handoff spec's twelve-item legal register to DLG Law as a single consult. It has never been
routed anywhere. Two items are genuinely new rather than restatements of known issues.

L-3 (위치정보법: the printed-poster check-in geofence is location-data collection and may require
위치기반서비스사업 신고 to the KCC) is marked BLOCKING before P0 by the handoff itself, and is distinct
from TASK-013, which scopes the age/location logic rather than the question of collecting location data
at all. L-8 (PIPA 만 14세 미만 guardian consent) is a new angle on the age gate: TASK-013 and DEC-012
have been framed around adult-age thresholds, and the under-14 guardian-consent requirement applies
regardless of a university-student audience, so it folds into that same consult. The remaining items
(L-1 peer affinity as personal data, L-2 gender purpose limitation, L-4 EXIF/GPS stripping, L-5/L-11
정보통신망법 takedown and 임시조치, L-6/L-7 subscription and in-app payment, L-9 FSC 선불전자지급수단,
L-10 data retention and deletion) are lower priority individually but cheaper answered in one consult.

## Sources
- doc | handoff spec v0.9 | | section 16 legal register
- risk | R5 위치정보법 registration | shared/HOTSHEET.md | companion Blocking entry
- decision | DEC-044 | shared/DECISIONS.md | ban-list CI/부정이용 retention legal escalation (L-1, L-10)
- proposal | elvis proposed-tasks 2026-08-30 | | filed the task

## Activity
- 2026-08-31 | Created by the merger, landed from elvis proposed-tasks (2026-08-30).

## Definition of done
- [ ] Full L-1..L-12 register packaged and sent to DLG Law as one consult
- [ ] L-3 flagged to DLG as a P0 blocker (before the geofence ships)
- [ ] L-8 folded into the TASK-013 age/location consult
- [ ] Answers logged back against the relevant decisions and HOTSHEET entries

## Blockers
- Waits on DLG Law engagement.
