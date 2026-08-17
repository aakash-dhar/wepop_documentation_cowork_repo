---
name: dashboard-update
category: delivery
description: >
  Refreshes the client-facing Wepop delivery dashboard at docs/index.html from current project state,
  then snapshots a new version. Updates content in place only (no restyle). Does no git (human syncs
  via GitHub Desktop; GitHub Pages serves from main /docs). Triggers on "update the dashboard",
  "refresh the dashboard", "snapshot the dashboard". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: dashboard-update (Wepop)

> [you] = the caller's workspace name.

## Trigger
- "update the dashboard", "refresh the dashboard", "snapshot the dashboard".

## Pre-read
1. `docs/index.html` (exact section structure).
2. `shared/PROJECT_INDEX.md` (RAG / phase).
3. `shared/HOTSHEET.md` (open / watch / blockers).
4. `shared/DECISIONS.md` (recent).
5. The latest meeting-note summary.

## Steps
### Step 1 - Gather current state.
### Step 2 - Edit the dashboard sections in place. Keep the theme, accent, branding, and HTML structure - content only. Update any "since [date]" heading.
### Step 3 - Run the existing snapshot script: `cd docs && bash dashboard-versions/snapshot.sh`.
### Step 4 - Report (refreshed / snapshot archived / history rebuilt), flag for Aakash's review, suggest a commit.

## Never
- Run git commit / push; restyle or change branding; em-dash; DENY.
