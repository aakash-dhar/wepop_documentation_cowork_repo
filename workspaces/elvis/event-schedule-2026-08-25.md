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

---

# Update, 2026-08-30: multi-day dependency resolved, three new resolutions

> Item #8 of the phase-1/1.5 review list, revisited 2026-08-30 against the
> `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx` intake. The single open dependency from
> 2026-08-25 is closed and three questions the handoff newly opened are resolved. Original text above
> kept unchanged, per this repo's convention of recording changes rather than overwriting them.

## Multi-day dependency, RESOLVED 2026-08-30: the Event model does support a date range

The 2026-08-25 flag for Deepak asked whether the core Event model supports a start and end date that can
differ, since nothing in DEC-001 through DEC-009 had ever established it and every description read as
singular ("a concrete activity at a place and time"). Two independent confirmations:

- **Data model.** The handoff's §14 schema deltas ship `scheduled_end` on the Event row, alongside
  `ended_at` and `live_extension_count`, marked "ship now." §3.4 states outright that multi-day events are
  covered by the explicit-end-time branch of the live-grace rules.
- **Creation flow, confirmed by Elvis 2026-08-30.** A host can pick an end date on a different day. The
  input is a calendar picker in the Airbnb style, where a single day or a range are the same interaction.
  Elvis has the design done and will upload it; this file should be revisited against it when it lands.

So the multi-day schedule design from 2026-08-25 (single-day stops carry time only, multi-day stops each
carry their own date and time) has its prerequisite and is unblocked. The scope matrix note "multi-day
depends on Event date-range (Deepak to confirm)" can be cleared.

**Recommendation to Deepak, not yet confirmed by Elvis.** Store an explicit date on every stop, including
single-day events, and derive the display rather than the storage. The motivating case is §3.4's live
extension: a host may extend a Live event at any time, and an extension crossing midnight retroactively
turns a single-day event into a two-day one. If stops carry time-only and infer the date from the parent,
that extension silently corrupts every stop's meaning. One extra column removes the entire class.

## Schedule on an unresolved event, RESOLVED 2026-08-30: allowed, host's call

The handoff's new status machine defines `planning` as logistics unresolved, with date, time, and/or
location still under poll. That collides with the 2026-08-25 design, where a single-day event's stops carry
time only and inherit the event's date, because a planning event has no confirmed date to inherit.

**Elvis's decision:** a host may build a schedule before the date or time is resolved. It is up to the
host. Stops carry their times and bind to the date when the event is confirmed.

Reasoning: sketching the shape of a day is exactly what a host does while rallying people, and it tells
prospective attendees what they are signing up for. Blocking the itinerary until a date poll resolves would
make Plan Mode feel half-built for no protective benefit, since nothing about an unresolved date makes a
9am first stop meaningless.

## Changes to a schedule are announced, RESOLVED 2026-08-30

"Moving a stop" means editing an existing stop after people have seen it: changing its time, changing its
location, or reordering, deleting, or inserting stops. The failure mode is specific and worth stating
plainly, because it is why this needs a rule at all: someone who read the itinerary yesterday and is
standing at Hongdae Station Exit 3 at 09:00 does not have the event page open. A silent change strands them
with information that was correct when they read it.

**Elvis's decision, and it is broader than schedule changes:** all changes to an event or idea generate
notifications, and event changes additionally post into the event's chat. This includes moving a stop. One
notification per save, not one per field, so a host correcting three stops in one edit fires one
notification rather than three.

This rides on existing machinery rather than adding any. §11 already establishes that poll resolution
"writes the value into the parent and posts an announcement. It is never silent," and §7.2's chat is
announcement-only by default until it auto-opens at T-24h, which is precisely the mode system change notices
belong in. It also satisfies I-14 (consequential actions are never silent).

**Audience, RESOLVED 2026-08-30: all three stakeholder groups**, not just joined attendees. Joined
attendees, waitlisted users (DEC-024), and users with a pending apply-to-join application (DEC-033). The
waitlisted case is the one that would have been missed by an attendees-only rule: auto-promote can pull
someone into an event whose date moved while they were waiting, and they would arrive never having been
told. Followers and passive viewers are not notified.

**Completed events are not editable, RESOLVED 2026-08-30.** Elvis: once an event is done there is no need
to edit any details. This closes the edge case raised earlier about change notices posting into a chat room
archived after 30 days idle, since no detail edits can occur that late.

**Completed events cannot be deleted or left by their host either, RESOLVED 2026-08-30.** This came out of
questioning why a host would ever delete a finished event, and the honest answer is that they should not be
able to. See the dedicated section below; the schedule design simply inherits it.

## Recurring events, RESOLVED 2026-08-30: copied at generation, propagates on "this and following"

Confirmed by Elvis 2026-08-30, and consistent with DEC-021's Google-Calendar semantics.

- Batch generation copies everything to each occurrence, including the itinerary, with dates shifted to
  each occurrence's own date.
- A host may then edit a single occurrence whose details differ, itinerary included.
- **The schedule participates in DEC-021's "this occurrence / this and following" choice.** It is not
  simply copied once at generation and left as independent rows. If a host edits an itinerary and chooses
  "this and following," the change propagates forward to every later occurrence in the recurring group.

**Flag for Deepak.** This is the part most likely to be missed, because copy-at-generation and
propagate-on-edit look like the same feature and are not. The schedule needs to be part of the same
this/following propagation path DEC-021 already requires for edit, delete, and join, rather than a
special case bolted on afterward. Build target remains phase 1.5 with the rest of recurring events; the
schedule itself is phase 1.

## Completed events: deletion and detachment, RESOLVED 2026-08-30

Raised by Elvis questioning why anyone would delete an event after it is over. Following that through found
a real hole in the handoff spec, which §3.2 leaves open by permitting `any -> deleted` for "host or admin"
without distinguishing the two.

**Host self-deletion of a completed event is not allowed.** The legitimate reasons for a completed event to
disappear are moderation removal (an event found inappropriate after it ran, the same review path Elvis
already defined for events inspired by an inappropriate idea) and legal erasure under a PIPA deletion
request (legal register L-10). Neither is host-initiated.

**Why this matters beyond tidiness.** If a host can delete a completed event, they can delete its ratings.
A host with a poor rating or a report against them could erase that event and clean their record, which
directly undermines DEC-014's host reputation and DEC-024's public org track-record module. That module
exists specifically as a cold-start trust signal, and a trust signal the subject can selectively delete is
not a trust signal. The same reasoning already governs Ideas, where a creator cannot delete once other
people have engaged, and §12.6 leans the same way for Moments: "Host takedown is a request routed to
review, never an instant delete."

**Detachment from a completed event is by request, reviewed by an admin.** Elvis's call, and it is
deliberately stricter than the Ideas equivalent, where a creator detaches directly with no review. The
asymmetry is correct: an idea creator carries no accountability record, while an event host carries
ratings, attendance, and a public track record, so self-serve detachment would reopen the same laundering
hole through a different door. Routing it through review lets an admin distinguish a legitimate request
(harassment, leaving the organization) from an attempt to escape a rating history. It reuses the §12.6
request-routed-to-review pattern rather than adding a new one.

**Ratings persist, RESOLVED 2026-08-30, and Elvis went further than the question asked.** Ratings stay
connected to the host through detachment, and they stay connected **even when a completed event carrying
that feedback is itself deleted.** Elvis's stated principle: accountability matters, and we do not want
people to find loopholes. So detachment unlinks a host from an event's public page without touching their
aggregate record, and event deletion does not launder a rating either.

**The technical consequence is load-bearing and easy to get wrong.** A host's rating aggregate cannot be
computed by joining live event rows (`select ratings where event.host_id = X`), because that formulation
makes event deletion silently destroy the ratings, which is the exact outcome this decision rejects. The
rating has to carry its own denormalized reference to the host and survive its source event. This is not a
new pattern to invent: §3.5 already does exactly this for Moments, copying `event_name`, `event_date`, and
`org_name` onto the Moment at creation so the card survives the event's deletion. Same shape, applied to
ratings. Flag for Deepak to build it once and use it for both.

**Flags for Deepak.**

- `any -> deleted` needs to split by actor. Host-initiated deletion is permitted only before completion;
  after completion the transition is admin-only. Enforce server-side, not by hiding the affordance.
- Detachment on a completed event is a request object entering the existing moderation or admin review
  queue, not an immediate state change.
- Detail edits on a completed event must be rejected server-side for the same reason.

## Remaining accountability loopholes, MOVED 2026-08-30

Three escape routes for a host with a bad record were flagged here and then outgrew this file: statutory
erasure under PIPA, account deletion and re-registration, and hosting through disposable organization
accounts. All three are researched and resolved in `host-accountability-2026-08-30.md`, along with the
reputation-versus-enforcement split that made them tractable. Nothing about the event schedule depends on
them; they are cross-referenced here only because they surfaced from this file's completed-event deletion
work.

## Still open

- The Airbnb-style calendar picker design has not landed yet. Revisit this file when Elvis uploads it,
  particularly for how a range interacts with the schedule's per-stop date entry.
- Whether stops store an explicit date always (recommended above) or only on multi-day events.
- Whether an attendee sees a "current stop" indicator during a live event. Not raised with Elvis, noted as
  a cheap affordance that falls out of having ordered stops with times, worth its own small pass later.

