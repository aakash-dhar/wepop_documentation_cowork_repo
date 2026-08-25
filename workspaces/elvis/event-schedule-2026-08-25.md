# Event schedule / itinerary, scoping (from `feature-backlog-2026-08-25.md` item 1)

> Elvis workspace working file, started 2026-08-25. Full scoping done same day, first item picked
> from the 2026-08-25 batch intake.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

A host wants to add a structured itinerary to an event, a list of stops with a time, a location, and
a note, for example "Meet at Hongdae Station at 9am." Additive to the event's own primary time and
location from DEC-003, not a replacement, this is a more detailed breakdown for events that move
through multiple stops or have real internal timing.

## Data shape, RESOLVED 2026-08-25

An ordered list of stops attached to the Event row: time, a structured location, and a free-text note
per stop. No new entity beyond that, and no RSVP-style semantics, nobody joins or leaves an individual
stop the way they would a recurring occurrence.

## Visibility, RESOLVED 2026-08-25: inherits the event's own access level exactly

The schedule does not get its own visibility rule. Whatever access level governs the event itself,
fully public and open to anyone, private and visible only to those with access, or any tier in between
the event model supports, the schedule matches it exactly. A fully public event shows its full
schedule to anyone browsing, the same way its top-level time and location already do. This was a
deliberate correction of how I first framed the question (a binary public/private choice); Elvis's
answer generalizes it correctly to however granular the event's own access model actually is, not
just two states.

## Per-stop location, RESOLVED 2026-08-25: structured map picker, same as DEC-003

Each stop's location reuses the exact map-picker component already built for the event's own location
(search plus tap a place). No new UI pattern, and attendees get a real tappable pin per stop, not a
text string they have to search for themselves.

## Multi-day support, RESOLVED 2026-08-25: tied to whether the event itself spans multiple days

A schedule supports multiple days only if the event it belongs to is itself scoped as more than one
day long. A single-day event's stops carry time only, implicitly the event's own date. A multi-day
event's stops each carry their own date and time.

**Flag for Deepak, dependency, not decided here.** This resolution assumes the core Event model
already supports a date range (a start date and an end date that can differ), not just a single date.
Nothing in DEC-001 through DEC-009 or any item resolved since has explicitly established whether
Event currently supports spanning multiple calendar days at all, everything described so far has been
"a concrete activity at a place and time," which reads as singular. If Event does not yet support a
date range, that is prerequisite scope this schedule feature depends on, not something schedule design
can resolve on its own. Needs a quick confirmation from Deepak on current data model state before
build.
