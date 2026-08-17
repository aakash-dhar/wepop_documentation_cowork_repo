---
name: update-hotsheet
category: maintenance
description: >
  Proposes changes to the Wepop HOTSHEET (blockers, risks, action items) via
  workspaces/[you]/proposed-hotsheet.md, keeping priority order and source references. Often
  auto-runs after archive-email and process-transcript. Triggers on "update hotsheet",
  "refresh hotsheet". Enforces BLOCK-not-DENY and no em-dashes. Never writes shared/ directly.
---

# Skill: update-hotsheet (Wepop)

> [you] = the caller's workspace name.

## Trigger
- "update hotsheet", "refresh hotsheet"; auto after the two ingestion skills.

## Pre-read
1. `shared/HOTSHEET.md` (structure, priority order); `workspaces/[you]/proposed-hotsheet.md`.

## Steps
### Step 1 - Identify changes from this session: Resolve / Add / Reclassify.
### Step 2 - Write `proposed-hotsheet.md` mirroring the HOTSHEET structure (priority order Blocking -> Needs Attention -> Watching -> Resolved). Every item needs a description, a "since" date, and a source reference. Resolved items move to Resolved, never deleted. Head it "Proposed HOTSHEET changes from [you], [date] - for merger review".
### Step 3 - Report.

## Never
- Edit `shared/HOTSHEET.md` directly; delete a resolved item; em-dash; DENY.
