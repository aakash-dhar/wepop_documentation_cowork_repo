# Personality tags catalog, initial seed, 2026-08-27

> Elvis workspace working file. The initial seed content for onboarding's personality-tags step
> (`onboarding-flow-2026-08-26.md` step 10), the picker DEC-005 first scoped as "an extensible list of
> tags... show the top 10-20 common tags, make them searchable, and let users add their own." This
> organizes that list into named sections for the first time, MBTI plus two more chosen from a short
> review of what earns its place against the actual use case (`group-dynamics-2026-08-25.md`'s
> group-composition compatibility signal and `icebreakers-2026-08-25.md`'s MBTI-based matching game).
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Onboarding needs real seed content for the personality-tags picker, not just the concept of one. DEC-005
described a flat, searchable, user-extensible list with MBTI values mixed in. Structuring it into named
sections makes the picker scannable rather than one long undifferentiated list, but it also means the
"10-20 tags" figure from DEC-005 needs revisiting, MBTI alone is 16 values. Two more sections were chosen
from four candidates (zodiac, social energy, general vibe, Enneagram): social energy and general
vibe/self-descriptors. Zodiac and Enneagram are not included in this initial catalog, not ruled out.

## Section 1: MBTI, closed set, 16 values

The four-letter type, not a fixed pick-one-of-16 quiz result inferred by WePop, this is a self-reported
tag exactly as DEC-005 specified. Common nickname included alongside the code for recognizability, since
not every user remembers their type by letters alone.

- INTJ, the Architect
- INTP, the Logician
- ENTJ, the Commander
- ENTP, the Debater
- INFJ, the Advocate
- INFP, the Mediator
- ENFJ, the Protagonist
- ENFP, the Campaigner
- ISTJ, the Logistician
- ISFJ, the Defender
- ESTJ, the Executive
- ESFJ, the Consul
- ISTP, the Virtuoso
- ISFP, the Adventurer
- ESTP, the Entrepreneur
- ESFP, the Entertainer

## Section 2: Social energy, closed set, 3 values

Chosen specifically because it's Elvis's own driving example for the group-composition compatibility
signal, an extrovert-skewed group being a difficult fit for one introvert. MBTI's first letter already
carries this, but not every user knows their MBTI type, this gives the same signal directly and simply.

- Extrovert
- Introvert
- Ambivert

## Section 3: General vibe and self-descriptors, open, extensible, initial seed of 18

The section DEC-005's original design maps to most directly, searchable, and users can add their own if
theirs isn't listed. Kept to disposition and social style rather than activities or hobbies, that's what
the separate categories-and-subcategories step (`onboarding-flow-2026-08-26.md` step 11) already covers,
overlap between the two would be confusing rather than additive.

- Adventurous
- Chill / laid-back
- Planner
- Spontaneous
- Night owl
- Early bird
- Homebody
- Big-group energy
- Small-group energy
- Deep talker
- Curious
- Creative
- Analytical
- Empathetic
- Competitive
- Easygoing
- Optimist
- Realist

## Not yet decided, deliberately parked

- Whether MBTI and social energy are single-select (a person has one type, one energy level) while general
  vibe stays multi-select, or all three sections allow multiple selections uniformly. The onboarding-flow
  doc's step 10 says "multiple entries allowed" at the step level, written before this catalog had
  sections, this section-level distinction wasn't addressed there and needs a direct call.
- DEC-005's "top 10-20 common tags" figure, written for one flat list. This catalog's three sections total
  37 tags before any user-added ones. Worth a quick confirmation that this is the intended evolution of
  that guidance rather than something to trim back, especially since MBTI and social energy are both fixed,
  complete sets that can't be shortened without dropping real values.
- Whether zodiac or Enneagram get added in a later pass, both were considered and set aside for this
  initial catalog, not rejected outright.
- Exact display order within each section (alphabetical, most-common-first, or something else) and whether
  MBTI nicknames are the right call for launch copy or just a placeholder, a UX-copy pass, not decided here.

## Flags for Deepak, implementation, not decided here

- MBTI and social energy are closed, fixed tag sets, no "add your own" affordance should appear on those
  two sections, unlike the general-vibe section, which needs the full searchable, user-extensible behavior
  DEC-005 specified. The data model needs to distinguish closed-taxonomy tags from open, user-extensible
  ones, this is the first place that distinction actually matters.
- General-vibe tags a user adds that aren't in this seed list need the same moderation/review consideration
  any user-generated tag would, not designed here, likely the same mechanism DEC-005's original "let users
  add their own" already implied needing.
- All three sections feed the same personality-mix compatibility signal
  (`group-dynamics-2026-08-25.md`) and the MBTI-based icebreaker matching game
  (`icebreakers-2026-08-25.md`), MBTI specifically should stay queryable as its own field, not just a tag
  among 37, since the icebreaker game needs to match specifically on MBTI type.
