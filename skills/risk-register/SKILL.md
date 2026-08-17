---
name: risk-register
category: maintenance
description: >
  Adds, updates, or retires a Wepop project risk in the HOTSHEET register format. Because the live
  register is merger-owned, writes the change as a proposal in workspaces/[you]/proposed-risks.md.
  Triggers on "add a risk", "log a risk", "update the risk register", "retire risk N".
  Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: risk-register (Wepop)

> [you] = the caller's workspace name.

## Trigger
- "add a risk", "log a risk", "update the risk register", "retire risk N" / "mark risk N resolved".

## Pre-read
1. `shared/HOTSHEET.md` (register table, highest risk number, exact columns).
2. `workspaces/[you]/proposed-risks.md`.
3. `shared/DECISIONS.md`.

## Format
`| # | Risk | Severity (Likelihood x Impact) | Owner | Mitigation | Status |` - lowercase x, never a
multiplication sign or em-dash. Status: ACTIVE / ACTIVE (in-flight) / RESOLVED.

## Steps
### Step 1 - Determine the action (add / update / retire).
### Step 2 - Confirm details.
### Step 3 - Append the new or updated row to `proposed-risks.md`, headed "Proposed risk register change from [you], [date] - for merger review". Retirement = restate the row as RESOLVED with a closure note.
### Step 4 - Report.

## Never
- Edit `shared/HOTSHEET.md` directly; delete a risk (retire it); reuse a number; em-dash; multiplication sign; DENY.
