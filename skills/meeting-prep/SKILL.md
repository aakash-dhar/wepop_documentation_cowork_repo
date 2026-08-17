---
name: meeting-prep
category: delivery
description: >
  Drafts a shareable agenda to send round before the recurring Wepop meeting (the weekly Wepop sync),
  the outbound sibling of call-brief. Pulls carry-overs, decisions to confirm, blockers, open
  questions. Read-only, drafts in chat, writes no files. Triggers on "meeting prep", "draft an
  agenda", "prep the weekly sync". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: meeting-prep (Wepop)

> [you] = the caller's workspace name. Output is chat only.

## Trigger
- "meeting prep", "draft an agenda", "prep the weekly Wepop sync", "agenda for [meeting]".

## Pre-read
1. The latest meeting-note summary (action items, carried-forward).
2. `comms/todos.md`; `shared/HOTSHEET.md`; `shared/MERGE-REVIEW.md`.
3. `workspaces/[you]/proposed-decisions.md` + `workspaces/[you]/open-questions.md`.
4. `shared/DECISIONS.md` (recent locks).

## Output (chat only)
- Carry-overs from last meeting
- Decisions to confirm
- Open items / blockers to discuss
- Open questions needing an owner's answer
- Heads-up / upcoming
- Optional time-box

Keep it tight and decision-oriented. Surface scope items in the weekly Wepop sync rather than email.

## Never
- Create / edit / commit files; em-dash; DENY.
