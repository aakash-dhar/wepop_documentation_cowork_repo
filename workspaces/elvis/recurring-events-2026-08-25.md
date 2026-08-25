# Recurring events, scoping (TASK-012 family, phase-1.5 build target)

> Elvis workspace working file, started 2026-08-25. Spun out of `conflict-review-2026-08-19.md`
> item 9's follow-up: series pages were given a phase-1.5 build target with no design behind them,
> and series pages cannot exist without recurring events existing as a concept first. This file
> scopes both, even though the build itself lands in phase 1.5, per Elvis's request.
>
> **Renamed 2026-08-25, later the same day.** Originally called the linking concept below "series"
> and its display "series pages." That collides with a real, separate product concept introduced
> right after this file was written: Event Series, a master hub page with its own cover, title,
> description, and tags that a host builds up by attaching events over time (see
> `event-series-2026-08-25.md`). A recurring event has no master hub, per Elvis 2026-08-25, so it
> should never have shared the word "series" with a concept that does. Renamed throughout to
> **recurring group**, everywhere this file previously said "series." No design decision changed,
> only the name.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Nothing in the project (the 2026-08-17 walkthrough, DEC-001 through DEC-009, either draft) considered
an event that repeats. "Event" today is a single self-contained thing: one RSVP list, one waitlist,
one check-in flow, one set of moments, one rating. A recurring event (a weekly club meetup, most
concretely) needs to reuse that machinery without a host manually recreating the event every week.

## Architecture, RESOLVED 2026-08-25: separate linked Event instances, not a multi-date Event object

Two ways to model this were weighed. Each occurrence stays a fully separate Event row, linked by a
shared recurring-group ID, versus one Event object holding multiple date instances internally. The
separate-instances model wins clearly, not a close call: every decision made so far (item 1's ratings,
item 9's QR check-in and public org track-record count, the org tier's media caps, DEC-006's
anti-stalking pre-join model) is written "per event." Under separate instances, none of that needs to
change. Under one multi-date object, RSVP, check-in, and no-show tracking would all need to become
per-instance anyway, meaning a new sub-entity gets built regardless, with no real complexity savings
and a more tangled schema. It also collides with DEC-008 (salvage and build on the existing codebase):
every screen and backend flow already built around "an Event" would need to be taught that an Event
can now mean several simultaneous things. A ten-week recurring event becomes ten ordinary Event rows
sharing one group pointer, generated in bulk by a host-facing tool rather than created one at a time.

## Interaction model, RESOLVED 2026-08-25: Google Calendar-style, applied uniformly

One consistent pattern governs edit, delete, and join/interest, rather than separate rules per action.
From any single instance, a user can see and click into the full list of other instances in that
recurring group. A host can manually override an individual instance's time, location, or description
without detaching it from the group, an overridden instance still appears in the group's list, just
with the overridden fields, matching how a moved Google Calendar event still shows in its recurring
series.

- **Delete.** Asks whether to delete just this occurrence, or this and all following occurrences.
- **Edit.** Asks whether the change applies to just this occurrence, or this and all following
  occurrences. "Following" is relative to the occurrence being edited, not to today's date, matching
  standard behavior across Google/Outlook/Apple Calendar. Past or already-checked-into occurrences are
  never rewritten by a forward-looking edit.
- **Join / interested.** Asks whether to join just this occurrence, or this and all occurrences that
  exist in the group at that moment. A past occurrence is never joinable, ordinary RSVP logic that
  already applies to any event, recurring or not, so this never becomes a real edge case in practice.

**Join is a snapshot, not a standing subscription, RESOLVED 2026-08-25.** Choosing "this and all
future" only enrolls the occurrences that exist in the recurring group at the moment of joining. If a
host later extends the group (generates another batch of occurrences), existing members are notified
and choose whether to join the new batch, they are not silently auto-enrolled. This was an explicit
override of my own initial recommendation (I'd suggested a standing subscription); the snapshot model
is the better call, it respects consent on an ongoing basis rather than assuming an open-ended
commitment a member never actually agreed to, and it reuses the notification system already in scope
for the app rather than adding a new one.

## Recurrence generation, RESOLVED 2026-08-25: batch-generated, not a rule engine

A host sets a pattern (for example weekly, biweekly, or monthly) plus either an end date or an
occurrence count, and the system generates that batch of ordinary Event rows immediately, all linked
by the recurring-group ID, essentially meal-prepping the group. To extend past the batch, the host
re-runs generation for another batch, which is the same moment that triggers the opt-in notification
to existing members described above. This was chosen over a flexible open-ended recurrence-rule engine
(indefinite recurrence, complex patterns like "first Monday of the month," on-the-fly occurrence
computation similar to iCalendar RRULE) because the batch approach covers the real case this needs to
serve, a semester-long club meetup, using nothing beyond what the architecture above already requires,
an ordinary Event row plus a recurring-group ID. The rule-engine approach is real, separate scope that
isn't justified for a feature that isn't blocking phase 1 in the first place.

## Series pages, RESOLVED 2026-08-25: falls out of the design above, not a separate feature

"Series pages (event lineage)" was listed as its own undiscussed surface in the original review aid,
alongside recurring events, and read at the time as belonging to recurring events specifically. Once
recurring events are designed the way they are above, clicking into any instance and seeing the linked
list of other instances in its recurring group already is that item, in substance. No standalone hub
page is being built for a recurring group under this scoping; the instance-embedded list is the whole
of it, and a recurring group intentionally has no master page, unlike the separate Event Series concept
(see `event-series-2026-08-25.md`), confirmed by Elvis 2026-08-25 as a real, deliberate difference
between the two, not an oversight.

## Who can create a recurring event, RESOLVED 2026-08-25: both individual and org hosts

No restriction to org accounts. A recurring weekly hangout between friends is a normal individual use
case, not just a club mechanic, and the build already has to support the underlying mechanic for org
hosts regardless, so there is no real scope savings in restricting it.

## Consistency with existing decisions, no special-casing needed

Because every occurrence is an ordinary Event row, everything already resolved elsewhere applies
per-instance with zero changes: item 9's waitlist auto-promote and claim window, QR check-in, the org
tier's 50-item media cap, DEC-006's anti-stalking pre-join visibility model, item 1's ratings and
reviews, and item 9's public org track-record module (each occurrence counts as one real event run,
which is also the honest way to represent a club's actual track record).

## Flags for Deepak, implementation, not decided here

- Event schema needs a nullable `recurring_group_id` field (null for a standalone event, and distinct
  from whatever field ends up representing Event Series membership, see that file) plus enough
  ordering information (an occurrence index or date-within-group) to resolve "this and following"
  relative to the edited occurrence, not to today's date.
- A batch-generation tool: host sets a pattern, a count or end date, and the system creates that batch
  of linked Event rows in one action. The same tool, re-run, extends an existing group.
- A notification hook fires when a recurring group is extended, to every user who chose "join this and
  all future" on an earlier occurrence in that group, offering them the new batch rather than
  auto-enrolling them.
- The "this one / this and following" choice needs to appear consistently across the delete, edit, and
  join/interest flows, ideally as one shared UI pattern rather than three separately built ones, since
  the underlying logic is the same shape in all three places.
- An event can belong to a recurring group and, separately, to an Event Series (see that file), these
  are two different relationships and an Event row will likely need two different nullable foreign
  keys, not one shared field. Worth Deepak confirming this doesn't tangle in the schema before build.

## Not yet decided, deliberately parked

- Exact pattern options exposed in the host UI (weekly / biweekly / monthly at minimum; whether to
  support anything finer, like a specific day-of-week picker for biweekly, is an implementation detail
  for Deepak and Elvis to settle when this is actually built, not blocking the scoping above).
