---
name: session-start
category: session
description: >
  Mandatory opening routine for the Wepop docs repo. Reads the governing layer in order and reports
  a concise status briefing before any work begins. Multi-person plus proposal model; reads the
  caller's own workspace log; never runs git pull. Triggers on "start session", "good morning",
  "catch me up". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: session-start (Wepop)

> Opening routine. [you] = the caller's workspace name (aakash, elvis, or deepak).

## Trigger
- "start session", "good morning", "catch me up", "what's the status?", or the first message after opening the folder.

## Pre-read (mandatory order)
1. `CLAUDE.md`
2. `OWNERS.md`
3. `shared/PROJECT_INDEX.md`
4. `shared/DECISIONS.md` (last 5)
5. `shared/HOTSHEET.md`
6. `shared/MERGE-REVIEW.md`
7. `workspaces/[you]/SESSION-LOG.md` (top entry)
8. `comms/todos.md`

## Steps
### Step 1 - Read everything in order, fully.
### Step 2 - Emit a briefing: Last Session, Status (RAG + one-line reason), Phase, Last DEC, Since Last Session, Blocking, Needs Attention, Overdue Action Items, Waiting for merge review.
### Step 3 - Then wait for instruction. Do not start work until told.

## Never
- Skip the routine; run git; assume prior context without reading; write to another workspace or `shared/`; em-dash; DENY.
