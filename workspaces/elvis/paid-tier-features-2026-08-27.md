# Paid-tier feature ideas, 2026-08-27

> Elvis workspace working file. Raised while reviewing item #4 of the phase-1/1.5 list (home location),
> Elvis pivoted to a broader question: what belongs in the paid tier without gating core functionality.
> Restates and applies DEC-018's existing three-bucket rule (never gate marketplace actions, quota-gate
> personal expression, insight-gate analytics) to several concrete candidates, resolves one, clarifies two,
> and answers a request for concrete examples on a fourth.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Apply-to-join screening questions, RESOLVED 2026-08-27 (confirmed by Elvis): 3 free, 10 paid

Hosts using apply-to-join (proposed for phase 1.5, still awaiting merger itself per
`session_log_2026-08-26_session2.md`, not yet in `shared/DECISIONS.md`) can write up to 3 screening
questions for free, individual premium raises that to 10. Quota-based, not a full block for free hosts,
matching the shape DEC-018 already uses for Moments (10 free / 20 individual-paid / 50 org-paid media
items). Filed to `proposed-decisions.md`, extending DEC-018, awaiting merger.

## Two clarified, not yet decided: where the same quota mechanic could attach next

These aren't proposals yet, they're pointing at places the docs already show a gap, worth spelling out
concretely since the shorthand version in chat wasn't clear.

**Live stories.** `live-stories-2026-08-25.md` already has this written down as an open question, verbatim:
"Interaction with the org tier's 50-item media cap. Real open question, not decided. The org tier's media
cap and its whole cost model were built around Moments specifically, persistent content." Live stories are
a separate, ephemeral (24-hour) content type from Moments, and nobody has actually decided what media cap
applies to them at all, for anyone, free or paid. Concretely, this could resolve the same way Moments did:
a flat free cap (say, matching whatever the eventual phase-1 default turns out to be) with individual
premium raising it, the same 10/20/50-shaped pattern already in place elsewhere. This isn't "add a new paid
feature," it's "this feature has no cap decided yet at all, and when someone decides it, reusing the
existing tiered-cap pattern is the obvious choice" rather than inventing a flat-forever cap the way Moments
had before DEC-018 existed.

**Icebreakers.** `icebreakers-2026-08-25.md` resolved "host writes up to 3 questions when creating the
event" as a flat cap, for every host, free or paid, no tier distinction exists in that decision at all.
Concretely: if you want another paid lever, this could become 3 free / some higher paid number, the exact
same mechanic (a question count capped by tier) apply-to-join just got above. Practically, once the
quota-by-tier component exists for apply-to-join, extending it to icebreakers is mostly reusing that same
piece for a second feature, not building a new one.

Neither is decided. Flagging both since they're genuinely low-effort next candidates if more paid levers
are wanted later, not because either is being proposed right now.

## Explore filters, REVISED 2026-08-27 (corrected by Elvis): standard free functionality, not a paid tier

Originally floated as premium candidates. Elvis's correction, and the right call: multi-category
combination filtering, a host-quality threshold, and a finer date/time range picker aren't power-user
extras, they're how a normal free user actually finds something worth attending in a real-world discovery
app. Gating basic search/filter capability would have crossed DEC-018's own "never gate marketplace
actions" line, filtering is discovery, and discovery is the marketplace, not an add-on to it. All three
become ordinary Explore functionality, free for everyone, no tier distinction:

- **Multi-category combination filtering.** WePop's taxonomy (`categories-taxonomy-2026-08-27.md`) has 9
  categories and 85 subcategories; Explore should let a user combine more than one at once (for example,
  events tagged both `hiking_trekking` and `photography`), not just filter by a single tag.
- **Host-quality filter.** A minimum-rating or minimum-track-record threshold, drawing on data DEC-014's
  post-event ratings and DEC-024's public org track-record module already generate. New-host visibility
  itself (DEC-020's new-host boost) is untouched, this only lets a user narrow their own view.
- **Finer date/time range picker,** beyond simple presets (today, this week, this weekend), for planning
  further ahead.

**Saved filter presets, PARKED 2026-08-27 (Elvis's call): not built for anyone right now, free or paid.**
Not needed at this stage for either tier. Worth revisiting later, not scoped further here.

## Dropped, may revisit later: "see who viewed your profile"

Raised as a possible insight-gated premium feature, and set aside by Elvis's explicit call. The specific
concern: this app's design leans heavily on anti-stalking protections (DEC-006, DEC-017), and
viewer-visibility features are a common vector for exactly the kind of unwanted attention those decisions
exist to prevent. Not ruled out permanently, flagged here so the reasoning for shelving it isn't lost if it
comes back up.
