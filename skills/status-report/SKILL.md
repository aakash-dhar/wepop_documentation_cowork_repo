---
name: status-report
category: delivery
description: >
  A RAG-focused status report for Wepop leadership or the client - overall status, summary, decisions
  since last report, open risks, next milestones. Read-only, concise, no operational noise. Triggers
  on "status report", "mgmt update", "executive summary". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: status-report (Wepop)

> [you] = the caller's workspace name. Output is chat only.

## Trigger
- "status report", "mgmt update" / "management update", "executive summary", "generate status report".

## Pre-read
1. `shared/PROJECT_INDEX.md`; `shared/HOTSHEET.md` (open items + risk snapshot); `shared/DECISIONS.md` (since last report); `shared/MERGE-REVIEW.md`; recent meeting-notes / emails; `comms/todos.md`.

## Output (chat only)
- Overall Status (RAG + one sentence)
- Summary
- Decisions Since Last Report (table)
- Open Risks, top 3-5 (table)
- Next Milestones (table)
- Needs a Decision

## Never
- Create / edit / commit files; fabricate a SOW baseline or delivery numbers not in the repo; em-dash; DENY.
