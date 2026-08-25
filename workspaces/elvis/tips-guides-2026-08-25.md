# Tips and guides for shy users and new hosts, scoping (from `feature-backlog-2026-08-25.md` item 7)

> Elvis workspace working file, started 2026-08-25. Full scoping done same day, fifth item picked
> from the 2026-08-25 batch intake. Structural scoping only, no content written yet, by design, see
> below.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Elvis's own framing: people are losing social skills, there are plenty of shy or introverted
attendees and inexperienced hosts, and WePop should offer tips and guides when someone needs them, to
help ensure a good experience on both sides, as a host and as an attendee.

## Delivery mechanism, RESOLVED 2026-08-25: a contextual info icon, plus a static guide behind "see all"

A "more info" icon, available wherever relevant, on whatever page or at whatever moment fits the
current situation. Clicking it shows tips relevant to that specific timing or context, not a generic
dump. A "see all" option from there leads to a static, browsable guide section for anyone who wants to
read more broadly rather than just what's relevant right now. Opt-in by construction, matching the
same pattern already locked for phase-1 icebreakers: nothing is pushed at the user, the icon is simply
present for whoever chooses to tap it.

## Targeting, RESOLVED 2026-08-25: situation and status-based, not personality-based

Content is shown based on the user's actual situation or status, first-time user, first-time host, and
similar concrete states, rather than any inferred or self-identified personality trait like introvert
or extrovert. Deliberate: an app deciding someone is shy and saying so risks landing as presumptuous
even when well-intentioned, whereas a first-time-user or first-time-host state is a plain fact about
where someone is in their WePop experience, not a judgment about who they are.

## Content, deliberately not written yet

No actual tip or guide copy exists at this stage. This file scopes the mechanism and where it shows
up, not what it says. Elvis's own framing: capture the structure in the backlog now, write the actual
content later. When that happens, the project's `design:ux-copy` skill is the right tool for drafting
the actual microcopy and guide text, not something to front-load into this scoping pass.

## Flags for Deepak, implementation, not decided here

- Needs a lightweight content model: tip/guide entries tagged with the situations that trigger their
  relevance (for example `first_time_host`, `before_first_checkin`, `creating_event`), so the info icon
  can query "what's relevant here" rather than every instance of the icon needing separately hardcoded
  content.
- Icon placement itself (which pages, which moments actually get one) is a design task for whenever
  this is built, not decided in this scoping pass, since it depends on which situations end up having
  written content behind them.
- No gamification or points tie-in. Gamification is its own separate, later-phase thread
  (`feature-backlog-2026-08-25.md` item 5); tips and guides should stay pure content and nudges, not
  get folded into badges or an achievement system.
