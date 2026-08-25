# Event icebreakers, scoping (from `feature-backlog-2026-08-25.md` item 6)

> Elvis workspace working file, started 2026-08-25. Full scoping done same day, fourth item picked
> from the 2026-08-25 batch intake. Split across phases during the discussion, phase 1 fully resolved,
> two later-phase mechanics captured but deliberately not fully designed yet.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Elvis's own framing, worth keeping as the guiding principle for every phase of this feature: help
attendees get comfortable, break the ice, meet people, or have an excuse to approach and talk.
Icebreakers should not take over the whole event experience. Already locked elsewhere
(`freemium-model-2026-08-19.md`): icebreakers stay in the free tier, never gated, since they improve
the quality of every attendee's experience, not just a paying user's.

## Three distinct mechanics, one feature name

"Icebreakers" covers three genuinely different things, split across phases rather than designed as
one uniform feature:

1. A host-authored question game (phase 1, fully resolved below).
2. Aggregate-tag matching, "find someone who also likes hiking" (later phase, not designed yet).
3. A card or attribute matching/scavenger game (later phase, not designed yet, one mechanic detail
   already locked).

## Phase 1: host question game, RESOLVED 2026-08-25

- Host writes up to 3 questions when creating the event.
- Questions are read-only in-app. Nothing is typed or submitted through the app, the point is for an
  attendee to read a question on their phone and then answer or follow up in person, at the event,
  with whoever they're standing near. The app delivers the prompt, the conversation happens in the
  real world.
- Access requires check-in, not just RSVP, consistent with how Moments, ratings, and live stories'
  posting permission are gated on actual attendance where it matters for the experience being genuine.
- Surfaced via a button on the event page, visible to checked-in attendees. Because it's something a
  user chooses to tap rather than a prompt pushed at them, this is opt-in by construction. No separate
  opt-out mechanism is needed for phase 1, nobody sees a question unless they go looking for it.

## Later phase, not designed yet: aggregate-tag matching

"Find someone who also likes hiking," built from the aggregate tag data already gathered per DEC-005.
Explicitly pushed to later phase alongside the scavenger game below, confirmed 2026-08-25. One real
design question was raised but not resolved, left open for whenever this is picked up: does the app
reveal exactly who shares the tag, or only alert that someone here does and let attendees find them
organically? The latter reads truer to the "excuse to approach and talk" framing above, but this was
not locked, only flagged as the question to answer when this phase starts.

## Later phase, not designed yet: card / attribute matching, scavenger-style

Each attendee gets a virtual card, or matches on an existing attribute like MBTI, and finds their
match in person. Also pushed to later phase. One mechanic detail already locked ahead of the rest of
the design: **match confirmation happens in-app, a tap or scan, similar to the existing check-in QR
pattern**, rather than being purely honor-system. Everything else about this mechanic (how cards are
assigned, whether there's a result or reward for finding a match) is undesigned, parked for later.

## Not yet decided, deliberately parked

- Opt-out for the later-phase mechanics. Phase 1's opt-in-by-construction reasoning does not
  automatically carry over to aggregate-tag matching or the scavenger game, which may push content
  more actively (a badge, a notification) rather than sitting behind a button someone chooses to tap.
  Worth revisiting when those phases are actually designed, not assumed to inherit phase 1's answer.
- Whether aggregate-tag matching needs the same minimum-sample-threshold pattern already used
  elsewhere (org tier segment analytics, item 1's small-event rating anonymity) to avoid surfacing a
  "match" that's really just one other easily-identifiable person at a small event. Not raised yet.
