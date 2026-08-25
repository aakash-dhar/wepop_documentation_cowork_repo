# Elvis - Session detail, 2026-08-25

Second session, picking up from the 2026-08-24 session-end log. Closed out the recurring-events
follow-up, introduced and fully scoped a new Event Series concept, and worked through a twelve-item
feature batch Elvis raised, fully scoping five of them.

## What got done

**Recurring events and series pages, `conflict-review-2026-08-19.md` item 11, and
`workspaces/elvis/recurring-events-2026-08-25.md`.** Fully scoped: each occurrence stays a separate
linked Event row (a "recurring group"), not a multi-date object, preserving every existing per-event
decision (ratings, check-in, media caps, DEC-006) with zero special-casing. Google Calendar-style "this
one / this and following" interaction across edit, delete, and join, applied uniformly. Join is a
snapshot, not a standing subscription, extending a series notifies existing members rather than
auto-enrolling them, an explicit override of my own initial recommendation and the better call. Batch-
generated occurrences (a pattern plus a count or end date), not a full recurrence-rule engine. Both
individual and org hosts can create one. Series pages turned out to fall directly out of this design,
an instance-embedded list of other occurrences, not a separate feature.

**Event Series, new concept, `conflict-review-2026-08-19.md` item 12, and
`workspaces/elvis/event-series-2026-08-25.md`.** Elvis introduced a second, different kind of series
mid-session: a thematic grouping (a concert series across venues, a band's world tour) built around a
master hub page (cover, title, description, tags, likeable/shareable/discussable), closer to the
existing Idea concept than to recurring events, except add-permission is locked to the host and
approved co-hosts. This pulled co-hosts forward from later-phase to ship alongside Series, revising
item 9's earlier resolution (recorded, not deleted, per the repo's own convention). Caught and fixed a
real naming collision before it caused confusion: I had reused the word "series" for the recurring-
events linking concept, which does not have a master hub; renamed that to "recurring group" throughout
`recurring-events-2026-08-25.md` the same day. Resolved: self-curation only (a series can only include
events its own host/co-hosts also host), phase 1.5 (bundled with recurring events and co-hosts), both
individual and org hosts can create one, and an event can belong to multiple series at once (a
many-to-many relationship, flagged for Deepak). A private event retroactively attached to a public
series stays hidden from that public list unless the viewer already had access, reusing item 4's
most-restrictive-wins precedent rather than inventing a new privacy rule.

**Feature batch intake and five items fully scoped, `workspaces/elvis/feature-backlog-2026-08-25.md`.**
Elvis raised twelve items in one batch (event schedule, live recordings, Free Now, ticketing,
gamification/virtual goods, icebreakers, tips/guides, event music, a supporters marketplace, other
business models, a web version, and a mascot/avatar system). Triaged and sized all twelve; four large
ones (ticketing, gamification/virtual-goods/avatars, ads/promoted-listings, the supporters marketplace)
logged as their own future dedicated conversations, two of which were already flagged deferred in the
freemium model doc. Web version logged as a platform roadmap note, not a design thread. Fully scoped
the five real near-term candidates, each in its own file:

- `event-schedule-2026-08-25.md`: host-added stops (time, structured DEC-003-style location, note).
  Visibility inherits the event's own access level exactly, whatever granularity that turns out to be.
  Multi-day stops only if the event itself spans multiple days, flagged as a real open dependency,
  nothing so far has established whether Event supports a date range at all.
- `live-stories-2026-08-25.md`: a separate, ephemeral (24-hour) content type from Moments. Posting
  only requires RSVP, not check-in, deliberate, to allow pre-arrival "on my way" posts. Visibility is
  poster-chosen per post across four tiers (mutuals, followers, event attendees, public), defaulting to
  the most restrictive, since the same event can have posters with opposite needs (a private user
  versus a promoter). Two items flagged, not resolved: interaction with the org tier's media cap, and
  reactions/replies.
- `free-now-2026-08-25.md`: the highest safety flag of the batch, real-time availability plus
  location-tied chatrooms. Grounded in documented failure patterns from comparable products (Snap Map,
  Yik Yak, dating-app proximity features) rather than abstract caution. Rounded/approximate location,
  not an exact pin. Aggregate-first room visibility, individual identities only on reciprocal join
  (mirrors item 8's mutual-follow rule). A new binary avatar status badge, no location attached,
  visible to followers/mutuals only. Room creation requires account standing beyond phone verification,
  exact threshold still open. Several secondary details flagged with recommendations but not confirmed
  (duration cap, the standing threshold number, room auto-archival, org-hosted rooms).
- `icebreakers-2026-08-25.md`: split across phases mid-discussion, a better answer than the options I'd
  offered. Phase 1 is a host question game only, up to 3 read-only questions, check-in gated, opt-in by
  construction via a button on the event page. Aggregate-tag matching and a card/scavenger matching
  game both moved to later phase; the scavenger game's tap/scan confirmation mechanic is already locked
  for whenever it's built.
- `tips-guides-2026-08-25.md`: a contextual "more info" icon available wherever relevant, with a "see
  all" link to a static browsable guide, opt-in by construction like phase-1 icebreakers. Targeted by
  situation and status (first-time user, first-time host), not personality or inferred traits, a
  deliberate call to avoid the app presumptively labeling someone shy. No content written yet, by
  design, structural scoping only.

## Files touched this session

- `conflict-review-2026-08-19.md` (items 11 and 12 added, item 9's co-hosts entry revised)
- `recurring-events-2026-08-25.md` (created, then renamed throughout the same day)
- `event-series-2026-08-25.md` (created)
- `feature-backlog-2026-08-25.md` (created, five items resolved within it)
- `event-schedule-2026-08-25.md` (created)
- `live-stories-2026-08-25.md` (created)
- `free-now-2026-08-25.md` (created)
- `icebreakers-2026-08-25.md` (created)
- `tips-guides-2026-08-25.md` (created)
- No `shared/` edits. Everything stayed in-workspace, correctly.

## Carried forward, open

- Seven items from the feature batch remain future dedicated conversations, not started: ticketing and
  transaction fees, gamification/virtual-goods/avatars, ads and promoted listings, the supporters
  marketplace, event music (Spotify integration), and web version (roadmap only, not a design thread).
- Several flagged sub-details within items resolved this session are still genuinely open, not silently
  assumed: the org-media-cap interaction and reactions for live stories; the account-standing threshold,
  duration cap, room auto-archival, and org-hosted rooms for Free Now; aggregate-tag matching's
  reveal-vs-alert question and later-phase opt-out for icebreakers; actual tip/guide content.
- Nothing from this session, or the prior one, has been promoted into `proposed-decisions.md` yet. This
  gap is now larger than it was at the last session-end: two full sessions of resolved design work sit
  in-workspace with nothing landed in `shared/`.
- Item 10 (Moments-doc names/budget/legal) still has not actually been sent to Aakash, still only
  marked ready to escalate.

TASK-012 remains Blocked on TASK-010 on the board, unchanged this session.
