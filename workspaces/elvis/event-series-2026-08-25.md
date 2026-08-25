# Event Series, scoping (new concept, introduced 2026-08-25)

> Elvis workspace working file, started 2026-08-25. A new concept, not from the original walkthrough
> or either draft: a thematic grouping of events that share a theme rather than a repeating
> time/location template, for example a concert series playing different venues around the city the
> same weekend, or a band's world tour. Distinct from recurring events (`recurring-events-2026-08-25.md`),
> which was renamed the same day specifically to free up the word "series" for this concept. See that
> file's rename note for why.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

A host wants to group events that belong together conceptually, not by a shared repeating template.
Different events in a series can have different times, locations, even different content, the only
thing they share is that they belong to the same larger thing in the host's and audience's mind. Elvis
2026-08-25: "a host may want to create an event concert series that may be events playing different
music in different locations in the city on the same weekend, or one band that is traveling the world
on a tour."

## Concept, as specified by Elvis 2026-08-25

A host creates one master Series page first: cover photo and media, title, description, and tags. That
master page is not itself an event, it cannot be joined or attended, but it can be liked, shared, and
discussed like any other content surface. After creating it, the host attaches events to it, adding as
many as they like over time. Users see an Event Series card and a detail page listing every attached
event. Each attached event still behaves like a completely normal event, RSVP, waitlist, check-in,
moments, ratings, all unchanged, it just carries a label marking it as part of a series, with a link
back to the master page. This mirrors the existing pattern where an event carries a link back to the
idea that inspired it.

## Positioning against Idea and against recurring events, RESOLVED 2026-08-25

Elvis's own framing, and the right one to build from: **a Series is closer to an Idea than to a
recurring event.** An Idea is already a hub concept the project has, something a user proposes without
hosting it, that others can spin into an event. A Series is the same shape, a hub with events attached
to it, except the add-permission is locked down: only the host and approved co-hosts can attach events
to a series, not anyone, unlike an Idea, which anyone can spin into their own event. A recurring event,
by contrast, has no master hub page at all, per the rename note in `recurring-events-2026-08-25.md`,
so it should not be confused with either Idea or Series despite sharing the word "event" and,
previously, sharing the word "series" by accident.

## Co-hosts dependency, RESOLVED 2026-08-25: pulled forward alongside Series

Series needs "approved co-host" as a real permission concept to work as specified: someone other than
the creating host, but not just anyone, needs to be able to add events to the series. Co-hosts was
previously scoped in `conflict-review-2026-08-19.md` item 9 as later-phase. Elvis's call: pull co-hosts
forward to ship in the same phase as Series, rather than shipping Series host-only first and unlocking
co-host permission once co-hosts is eventually built. **This revises item 9's earlier resolution** for
co-hosts specifically; that file needs updating to reflect co-hosts is no longer purely later-phase, it
now ships alongside Series. Not yet updated as of this writing, next step.

## Private event retroactively attached to a public series, RESOLVED 2026-08-25: most-restrictive-wins

A host can attach an already-existing event to a series after the fact, not only create new events
from inside the series flow. That raises a real visibility conflict: a private event (invite-only)
attached to a fully public series would otherwise leak that the private event exists to anyone who can
see the public series page. Resolution: the same "most restrictive setting always wins" rule already
locked for moments visibility in conflict-review item 4 applies here without modification. A private
event attached to a public series never appears in that series' public event list to anyone who
couldn't already see it through the event itself; it only appears there to people who already have
access. The series page's own public content, cover, title, description, tags, and its other public
events, is unaffected. No new privacy model needed, this reuses precedent rather than inventing a
second rule.

## Curation model, RESOLVED 2026-08-25: self-curation only

A series can only include events that the series' own host or approved co-hosts also host themselves,
not events curated in from other people's hosting. Covers both of Elvis's original examples cleanly, a
touring band hosting every stop itself, or one promoter/org running multiple venues the same weekend,
without needing a whole separate consent and notification system for attaching someone else's event to
a series they don't control. This also simplifies the private-event visibility rule above: since
attaching is always the event's own host acting on their own event, there is no scenario where a
series host exposes an event they do not themselves control. Open curation (a curator pulling in other
hosts' public events into a collection) was considered and set aside for now, a real future
enhancement if a genuine curator use case shows up later, not built into this round.

## Phase, RESOLVED 2026-08-25: phase 1.5, bundled with recurring events and co-hosts

Series shares the co-host dependency with that bundle already, and was raised as a close cousin of
recurring events in the same conversation. Grouped together for the same build push rather than
scoped as separate future work.

## Who can create a Series, RESOLVED 2026-08-25: both individual and org hosts

Consistent with recurring events' own resolution, no restriction to Organization profiles. Org
accounts will likely be the heavier users given the promoter/touring-act flavor of the examples, but
there is no real cost to also allowing individual hosts.

## Multiple series per event, RESOLVED 2026-08-25: allowed

One event can belong to more than one series at the same time. Low-risk specifically because curation
is self-only (above): the same host or org could run both a "Tuesday Talks" series and a "Founders
Series," and one event might genuinely belong to both, with no cross-consent issue since one actor
controls every series it could belong to. This means Series membership is a list, not a single link.

## Detaching an event from a series, assumed, not explicitly confirmed

Detaching only removes the link between the event and the series; it never deletes or otherwise
affects the event itself, consistent with how removing an event's link to an idea presumably already
works. Flagging this as an assumption carried forward rather than a separately confirmed decision,
since it was never asked directly, worth a quick confirmation before build if it matters.

## Flags for Deepak, implementation, not decided here

- Because an event can belong to multiple series, Series membership needs a join table (event to
  series, many-to-many), not a single nullable field on the Event row. This is separate from the
  `recurring_group_id` field scoped in `recurring-events-2026-08-25.md`, which stays a single nullable
  field since an event belongs to at most one recurring group. An event could plausibly belong to a
  recurring group, reference an idea, and belong to one or more series, all at once, three distinct
  relationships that should not be collapsed into one.
- The "part of a recurring group" label (from the other file) and "part of a series" label need to be
  visually distinct from each other in the UI, they are different concepts and a user should not read
  them as the same badge. Since an event can now belong to more than one series, the label likely needs
  to handle showing more than one series link, not just one.
- Attaching a private event to a public series needs the visibility check described above enforced at
  render time per viewer, not baked in once at attach time, since who can already see a private event
  can change after the attach happens.
- Series creation and series-add permission checks only need to verify the actor is the event's host or
  an approved co-host, given self-curation only, no separate cross-host consent flow needs building for
  this round.
