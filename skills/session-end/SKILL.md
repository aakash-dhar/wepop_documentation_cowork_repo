---
name: session-end
category: session
description: >
  Mandatory closing routine for the Wepop docs repo. Records the session as a dual-file workspace
  log, checks for unlogged decisions and unfiled proposals, and prepares a name-prefixed commit.
  Writes only inside the caller's workspace. Triggers on "end session", "done for today", "wrap up".
  Enforces BLOCK-not-DENY and no em-dashes. Never writes shared/ directly.
---

# Skill: session-end (Wepop)

> Closing routine. [you] = the caller's workspace name.

## Trigger
- "end session", "done for today", "wrap up", "closing", "sign off".

## Pre-read
1. What changed this session (files touched, proposals written).

## Steps
### Step 1 - Review what changed this session.
### Step 2 - Flag any decision not yet filed as a proposal, and wait for confirmation before filing.
### Step 3 - Write `workspaces/[you]/session_log_YYYY-MM-DD.md` (add `_sessionN` for multiples): Objective, Work done (with file paths), Decisions proposed, Flags / open items.
### Step 4 - Prepend a short summary block to `workspaces/[you]/SESSION-LOG.md` (newest at top), ending with a link to the detail file.
### Step 5 - Prepare (do not run) a `[you] ...` commit message. Final report.

## Never
- Skip the dual-file log; edit `shared/` or another workspace; write a decision straight to DECISIONS.md; auto-push; em-dash; DENY.
