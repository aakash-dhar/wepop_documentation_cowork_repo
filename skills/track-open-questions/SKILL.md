---
name: track-open-questions
category: maintenance
description: >
  Tracks open questions routed to other people on Wepop (Elvis, Deepak) so they do not get lost in
  session logs. Maintains a running list in workspaces/[you]/open-questions.md (own workspace, no
  proposal needed). Triggers on "track this question", "route this to [person]", "open questions",
  "what's still unanswered?". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: track-open-questions (Wepop)

> [you] = the caller's workspace name.

## Trigger
- "track this question", "route this to [person]", "open questions" / "show open questions", "what's still unanswered?", "mark question N answered".

## Tracker format
`| # | Question | Routed to | Raised | Source | Status |` with Status OPEN / ANSWERED (date).

## Modes
- **Scan / show:** list OPEN grouped by owner, oldest first, flag any older than ~7 days.
- **Add:** confirm question / owner / source, append an OPEN row.
- **Resolve:** set ANSWERED with the date + a one-line answer, never delete.

## Steps
### Step 1 - Read the tracker (+ session logs / todos for stray questions on scans).
### Step 2 - Perform the mode.
### Step 3 - Write the updated table back. Suggest a commit.

## Never
- Delete an answered question; write to another workspace or `shared/`; invent an answer; em-dash; DENY.
