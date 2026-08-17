---
name: build-status
category: delivery
description: >
  Bridges the separate Wepop code repos into this docs repo by reflecting current build / PR / release
  status on the client dashboard (docs/index.html, content-only) and, when a build blocks delivery, on
  the HOTSHEET. Reports only status it can verify (from the code repo or supplied by the tech lead);
  never assumes green. Does no git. Triggers on "build status", "update build status", "sync the build
  status", "is the build green?". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: build-status (Wepop)

> [you] = the caller's workspace name. Code lives in separate repos, not here. `docs/` is Aakash-owned (content-only).

## Trigger
- "build status", "update build status", "sync the build status", "is the build green?", "reflect the latest build on the dashboard".

## Pre-read
1. `docs/index.html` (the build-status section and structure); `shared/PROJECT_INDEX.md` (RAG / phase); `shared/HOTSHEET.md`.
2. Any code-repo references in `shared/PROJECT_INDEX.md` or `research/`.

## Steps
### Step 1 - Gather build status from a verifiable source: the code repo (branch, last PR, CI result, release tag) if reachable, or a status explicitly supplied by Deepak. If it cannot be verified, record it as `Unknown (as of [date])`, never as green.
### Step 2 - Update the `docs/index.html` build-status content in place (theme, branding, and structure unchanged), or hand the content to dashboard-update. Show branch, last build result, last deploy, and date.
### Step 3 - If a build failure or blocker affects delivery, route a `proposed-hotsheet.md` entry (Blocking / Needs Attention) rather than editing HOTSHEET directly. Do not silently absorb a red build.
### Step 4 - Snapshot via `cd docs && bash dashboard-versions/snapshot.sh`. Report (source used, verified vs unknown), flag for Aakash's review, and suggest a commit.

## Never
- Report a build state you did not verify or assume green; run git commit / push; put code in this repo; restyle or restructure the dashboard (content-only); edit `shared/` directly; em-dash; DENY.
