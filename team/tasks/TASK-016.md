# TASK-016 - Build the event location map picker

## Overview
The event-create and idea-create flows need a location picker modeled on Google Maps: the host
searches for a place, taps to select a named place (not just raw coordinates), can adjust the
address, and can add a per-event note about the spot.

The same picker is reused by location polls, where attendees suggest and vote on where to meet.
This is a Phase 1 item grounded in DEC-003.

## Sources
- decision | DEC-003 | shared/DECISIONS.md | Event location picker uses a Google-Maps-style select
- design | Phase 1 place-picker screens | architecture/elvis/ | Map-picker frames from the 2026-08-17 walkthrough
- proposal | Elvis, 2026-08-18 | workspaces/elvis/proposed-tasks.md | Raised by Elvis for the dev team; landed as TASK-016

## Activity
- 2026-08-18 | Proposed by Elvis and landed as TASK-016, owner Deepak.

## Definition of done
- [ ] Place search returns named places (Google-style), not just coordinates
- [ ] Tap-to-select drops a pin and captures the named place
- [ ] Address field is editable and a per-event note is supported
- [ ] Wired into event create, idea create, and location polls

## Blockers
- Final map-picker interaction detail is still open; needs Elvis (tracked under TASK-014).
