---
name: intake-document
category: ingestion
description: >
  Formally incorporates an external document (spec, framework, resume, paper) into the Wepop project
  record. Files it to reference/ or research/, date-stamps, assesses authority, writes a companion
  _NOTES.md, and flags conflicts with locked decisions. Decisions are proposed, never written to
  shared/. Triggers on "intake document", "file this document", "client sent a document".
  Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: intake-document (Wepop)

> [you] = the caller's workspace name.

## Trigger
- "intake document [filename]", "file this document", "client sent a document", a file dropped in `comms/attachments/`.

## Pre-read
1. `shared/PROJECT_INDEX.md`; `shared/DECISIONS.md` (conflict check); `reference/` and `research/` (naming style).

## Where it goes
- `reference/` for authoritative / grounding docs the team will cite; `research/` for background / external material. If unsure, ask.

## Steps
### Step 1 - Save with a clear dated name in the right folder.
### Step 2 - Assess: type, what it relates to, supersession, conflicts.
### Step 3 - Write `[same-path]_NOTES.md`: summary, why it matters, PM-relevant points, flags.
### Step 4 - Present the assessment. Handle any implied decision via propose-decision and any conflict via a flag to the merger.
### Step 5 - Suggest a commit.

## Never
- Treat a shared doc as governing until deliberately filed; write decisions to `shared/` directly; silently resolve a conflict; delete a superseded doc (note it superseded); em-dash; DENY.
