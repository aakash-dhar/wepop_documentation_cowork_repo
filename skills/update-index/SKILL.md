---
name: update-index
category: maintenance
description: >
  Proposes a refreshed Wepop PROJECT_INDEX (a current map of key documents with path, area, one-line
  description) via workspaces/[you]/proposed-project-index.md. Triggers on "update index",
  "refresh project index", or after any skill that creates new files. Enforces BLOCK-not-DENY and
  no em-dashes. Never writes shared/ directly.
---

# Skill: update-index (Wepop)

> [you] = the caller's workspace name.

## Trigger
- "update index", "refresh project index", after any skill that creates new files.

## Pre-read
1. `shared/PROJECT_INDEX.md` (current structure).

## Steps
### Step 1 - Scan `comms/`, `shared/`, `architecture/`, `reference/`, `research/`, `docs/` (never descend into other people's workspaces), capturing path, area / authority, one-line description, last-modified.
### Step 2 - Write `proposed-project-index.md` reproducing the index table structure, updating "Last Updated", headed "Proposed PROJECT_INDEX refresh from [you], [date] - for merger review".
### Step 3 - Report.

## Never
- Edit `shared/PROJECT_INDEX.md` directly; index another person's workspace; em-dash; DENY.
