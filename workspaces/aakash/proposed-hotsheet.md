# Proposed HOTSHEET changes from aakash - for merger review

> Priority order Blocking -> Needs Attention -> Watching -> Resolved. No em-dashes.

## Pending

## Proposed Hotsheet Entry
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/event-location-map-picker-2026-08-27.md
**Type:** Needs Attention
**Summary:** Korea map-provider decision (Google vs Naver/Kakao) is now a real decision, not a Watching item.
**Key Points:**
- The zoom-determines-precision picker mechanic depends on the provider's POI/reverse-geocode quality at each zoom tier, so the provider choice now affects a phase-1 feature rather than being a distant concern.
- Open question whether a non-Korean business can even open a Naver or Kakao developer account, which constrains the choice.
- Elvis researched a dual Google/Naver design (per-session provider lock, reusing the current-location signal); the decision itself is unmade.
- Elevate from the existing HOTSHEET Watching "Korean map coverage" item to Needs Attention; goes to the meeting.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Decide Korea map provider (feasibility of Naver/Kakao dev account first) | Aakash + Deepak | before location picker build |

## Landed

- 2026-08-26 (sync): Korea payments (Needs Attention, consolidated with Elvis's proposal) and Korean
  maps (Watching) landed into `shared/HOTSHEET.md`. Source: 2026-08-26 team sync. Nothing pending.
- 2026-08-26 (intake): Elvis-intake hotsheet entries landed into `shared/HOTSHEET.md`.
