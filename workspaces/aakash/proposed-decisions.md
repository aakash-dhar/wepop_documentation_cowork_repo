# Proposed decisions from aakash - for merger review

> Source: Wepop progress walkthrough, 2026-08-17 (comms/meeting-notes/2026-08-17_wepop-progress-walkthrough.md).
> DECISIONS.md is empty, so none of these conflict with a locked decision. The merger assigns the
> real DEC-NNN IDs when landing. No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** Central GitHub repo as source of truth plus Cowork PM harness
**Type:** Operational
**Decision:** Wepop coordination runs off one central GitHub repo as the single source of truth, with a Cowork PM harness on top; Elvis shares his GitHub ID and Aakash creates the repo, sends the invite, and runs a short setup call.
**Reasoning:** Removes back-and-forth document sharing and gives both sides a common, versioned source of truth.
**Impact:** Elvis pushes design and doc updates to the repo; Aakash pulls and maintains the PM record and status there.
**Relates to / Supersedes:** none
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** Age gating tied to country legal age
**Type:** Technical
**Decision:** Age eligibility is tied to the user's country legal age; if the entered age is under a threshold (around 19), the app triggers location permission early, checks the country's legal age, and blocks under-age users with a message that names the country.
**Reasoning:** Legal age differs by country (US 18, Korea 19, Germany 16); checking against the country avoids letting through under-age users while keeping the block early rather than after a long flow. Focus markets are Korea and the US.
**Impact:** Registration gains an early conditional location and age check. Depends on legal counsel (see risk R1) before the logic is locked; passive vs active location capture and travel-jurisdiction handling are still open.
**Relates to / Supersedes:** none
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** Event location picker uses Google-Maps-style select
**Type:** Technical
**Decision:** The map picker uses a Google-Maps-style model (search plus tap a place, showing the place name) rather than the Uber-style fixed center-pin, with zoom, a free-text address field, and an optional per-event note for the exact unit. Profile location captures only the general city.
**Reasoning:** Events need a human-readable named place, not raw latitude/longitude; the center-pin model suits precise pickup points (Uber) but reads poorly for "let's meet at this park". Profiles do not need a home's exact coordinates.
**Impact:** One map interaction pattern across the app for places; text-address plus note covers exact-unit cases. One picker interaction detail is still to be finalized by Elvis and Deepak.
**Relates to / Supersedes:** none
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** Auth - OTP required, optional password, biometrics if feasible
**Type:** Technical
**Decision:** Phone OTP verification is required to verify every user; an optional password is also offered, and biometric login is added if feasible.
**Reasoning:** OTP alone cannot cover a lost/blocked phone or a reset; a password is a fallback where SMS/OTP is regionally blocked (for example when the sending business is not registered in that region) and enables password reset.
**Impact:** Signup always verifies the phone via OTP; users may additionally set a password; biometric login is a nice-to-have.
**Relates to / Supersedes:** none
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** Replace MBTI with an extensible tag list
**Type:** Strategic
**Decision:** The personality field is an extensible list of tags (MBTI values included as tags) rather than an MBTI selector; show the top 10-20 common tags, make them searchable, and let users add their own.
**Reasoning:** A growing tag database is richer for the recommendation and event-matching algorithm than a fixed MBTI type.
**Impact:** Onboarding shows a searchable, user-extendable tag picker feeding matching.
**Relates to / Supersedes:** none
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** Anti-stalking visibility model
**Type:** Strategic
**Decision:** Before a user joins an event or idea, show only mutual friends' attendance plus aggregate signals (people near your age, area, and interests), not the full attendee list; lock fuller info until the user joins or marks interested; show mutuals' profile pics only.
**Reasoning:** Keeps Wepop a meetup app rather than a stalking or dating app, reduces liability, and pushes users toward the activity rather than judging attendees by looks. Whether to show gender and photos at all is still under debate.
**Impact:** Event/idea detail views gate the attendee list and richer info behind joining; only mutuals' pictures appear pre-join.
**Relates to / Supersedes:** none
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** No in-app AI image or video generation for now
**Type:** Strategic
**Decision:** The app does not generate AI images or video for users; the only AI the user interacts with is text prompt-to-create for an idea or event.
**Reasoning:** Current AI images read as low-quality and off-brand for a real-world meetup app, and skipping generation saves on token cost.
**Impact:** Users upload their own photos; no in-app image/video generation is built for this phase.
**Relates to / Supersedes:** none
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** Salvage and build on the existing Wepop code
**Type:** Strategic
**Decision:** Reuse and salvage the existing Wepop codebase and build on top of it with AI rather than rebuilding from scratch.
**Reasoning:** Reduces the timeline and gets features sorted faster.
**Impact:** Design decisions should account for what the legacy code already supports; how much is reused vs rebuilt is still being assessed.
**Relates to / Supersedes:** none
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-17
**Proposed by:** aakash
**Source:** meeting (2026-08-17 Wepop progress walkthrough)
**Topic:** Phase-1 scope boundaries
**Type:** Operational
**Decision:** For phase 1: build the idea "close to new joiners" toggle but do not expose it; defer the calendar view and device calendar (Google / iCal) integration to a later phase; ship event/group chat first, with DM and user-created group chats later if they cannot be done one-shot with AI, and no audio or video chat (text only); no media upload on ideas (photos go in the discussion board).
**Reasoning:** A new app needs more joiners not fewer, so a "close" toggle is premature to expose; the deferred items are lower priority than core flows and reduce phase-1 build scope.
**Impact:** Sets a clear phase-1 line; the merger may prefer to split this into separate decisions per area.
**Relates to / Supersedes:** none
**Status:** Awaiting merger
