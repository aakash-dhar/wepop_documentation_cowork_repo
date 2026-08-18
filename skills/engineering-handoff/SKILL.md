---
name: engineering-handoff
category: delivery
description: >
  Turns a feature that is both decided (has a DEC) and designed (in a design intake) into a
  developer-ready handoff for Deepak: user story, acceptance criteria, states and edge cases,
  validation and non-functional notes, the linked DEC and design screens, and a paste-ready GitHub
  issue body for the separate code repos. Grounded only in decisions and designs, never invented
  scope. Does no git and does not open issues itself. Triggers on "engineering handoff", "handoff
  for [feature]", "make dev tickets for [feature]", "spec [feature] for build". Enforces
  BLOCK-not-DENY and no em-dashes.
---

# Skill: engineering-handoff (Wepop)

> `[you]` = the caller's workspace name. Bridges this docs repo to the separate code repos. Code
> and tech design live in `architecture/technical/` (Deepak-owned), so this skill writes there only
> if the caller is Deepak, otherwise it produces a deliverable or a suggestion.

## Trigger
- "engineering handoff", "handoff for [feature]", "make dev tickets for [feature]", "spec [feature]
  for build", "ticket this up for Deepak".

## Pre-read
1. `shared/DECISIONS.md` (the feature's DEC and any it relates to or supersedes).
2. `architecture/phase-plan/wepop-scope-matrix.md` (phase and status) and `wepop-product-overview.md`.
3. The latest design intake / screens for the feature.
4. `shared/HOTSHEET.md` (linked risks, e.g. legal provisionals).

## Gate (check first)
- A feature is handoff-ready only if it is BOTH decided (a DEC) AND designed (a screen set). If a
  decision or a design is missing, BLOCK: report exactly what is missing and stop. Do not invent the
  gap.

## Steps
### Step 1 - Confirm the gate (decided AND designed). If not, BLOCK and name what is missing.
### Step 2 - Assemble the handoff: user story ("As a ... I want ... so that ..."); acceptance criteria in Given / When / Then; screen-by-screen states (loading, empty, error, offline, permission); edge cases; data and validation notes; non-functional notes (perf, privacy, i18n where relevant); the linked DEC and design screens; open questions that block build.
### Step 3 - Format as one or more paste-ready GitHub issue bodies for the code repo (title, labels, body). The agent does not run git or gh; it produces the text for a human to paste.
### Step 4 - Place it: if the caller is Deepak, write to `architecture/technical/`; otherwise deliver it and write a `suggestions/suggestion-handoff-[feature].md`. Report and suggest a commit.

## Never
- Invent scope, an acceptance criterion, or a screen not backed by a decision or a design (BLOCK and flag the gap).
- Write `architecture/technical/` when not the owner (suggest instead); write `shared/` directly.
- Run git or gh, or claim an issue was created.
- Em-dash; DENY.
