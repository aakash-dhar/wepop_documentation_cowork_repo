---
name: call-brief
category: delivery
description: >
  A private pre-call rundown for the Wepop PM - status, what changed since the last call, open items,
  conflicts awaiting the merger, risks, talking points, outstanding action items. Read-only, creates
  and commits nothing. Triggers on "call brief", "brief me before the call", "what do I need to know
  for today's call?". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: call-brief (Wepop)

> [you] = the caller's workspace name. Output is chat only.

## Trigger
- "call brief", "prepare call brief", "brief me before the call", "what do I need to know for today's call?".

## Pre-read
1. `shared/PROJECT_INDEX.md`; `shared/HOTSHEET.md`; `shared/DECISIONS.md` (last 5); `shared/MERGE-REVIEW.md`; `workspaces/[you]/proposed-decisions.md`; `comms/summary.md`; the latest meeting-note summary; recent emails since the last call; `comms/todos.md`.

## Output (chat only)
- Status (RAG + reason, phase, last DEC)
- Since Last Call
- Open Items to Discuss
- In-Flight Proposals
- Conflicts Awaiting Merge Review
- Risks to Flag
- Suggested Talking Points
- Outstanding Action Items (table)
- Context Notes (sentiment / sensitivities)

## Never
- Create / edit / commit files; run git; em-dash; DENY.
