---
name: weekly-digest
category: delivery
description: >
  A digest of everything that landed on Wepop in the last seven days (or a stated window) - emails
  ingested, decisions proposed and locked, meeting notes, resolved and new open items. Read-only.
  Good candidate for a weekly schedule. Triggers on "weekly digest", "what happened this week".
  Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: weekly-digest (Wepop)

> [you] = the caller's workspace name. Output is chat only.

## Trigger
- "weekly digest", "what happened this week", "catch me up on the week", scheduled run.

## Window
- Default last 7 days. Honor an explicit window if given.

## Pre-read
1. `comms/emails/` (in window); `comms/meeting-notes/` (in window); `shared/DECISIONS.md` (locked in window); `workspaces/[you]/proposed-decisions.md` (in window); `shared/HOTSHEET.md`; `comms/todos.md`.

## Output (chat only)
- Headline
- Emails Ingested
- Meetings
- Decisions (locked / proposed)
- Open Items (new / resolved / still blocking)
- Heads-Up for Next Week

## Never
- Create / edit / commit files; include items outside the window; em-dash; DENY.
