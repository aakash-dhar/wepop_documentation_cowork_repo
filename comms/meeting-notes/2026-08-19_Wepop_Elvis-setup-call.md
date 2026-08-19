# Wepop Elvis setup call - summary - 2026-08-19

> Synthesized meeting notes. Companion verbatim: `2026-08-19_Wepop_Elvis-setup-call_TRANSCRIPT.md`.
> Speakers normalized by role. Source recording:
> https://fathom.video/share/-YSFwY-JJsP51vPqdbDZMMmfHE_yF8xW (14 mins).
> Operational onboarding call. No product decisions or scope changes; nothing here conflicts with
> DEC-001 to DEC-009.

## Attendees

- Aakash - PM (project owner, merger). Ran the walkthrough.
- Elvis - client and designer. Being onboarded into the repo and Cowork harness.

## Purpose

Short setup call to onboard Elvis onto the shared Wepop repo and the Cowork PM harness: how he
works day to day, how his changes reach the shared record, where he drops designs and documents,
and the delivery board he can self-serve status from. This is the setup call called for by DEC-001
and tracked as TASK-011.

## What was covered

- Workflow and the commit/push split. Cowork (Claude) can commit but cannot push; pushing is a
  manual step in GitHub Desktop, which Aakash framed as a deliberate safety gate so both sides know
  exactly what is going out. Elvis should finish his work, commit, then push to main himself.
- Muscle-memory routine. Start every working session with "start session" (reads the repo and
  reports overall status) and close with "end session" (writes a session log into his workspace).
  Elvis can later ask Claude what he did on a given day and get the log back. Elvis summarized it as
  a checks-and-balances system.
- The merge model. Elvis's work stays in his own `workspaces/elvis/` zone; committing stages it
  there. Aakash, as PM, pulls, reviews, and runs the merger skill to land proposed changes into the
  shared directory, which is the context source of truth the harness reads from.
- The delivery board. Aakash shared the board link in the call chat. It shows what is done, in
  progress, and to do, plus a scope-versus-build view mapped to the signed SOW so Elvis can see how
  much of scope is complete without asking anyone. Aakash plans to add a chat option to the board so
  Elvis can also ask a bot for status. The board is a PM skill assigned to Aakash's side.
- Adding tasks. Elvis can tell his Cloud desktop to create a task and assign it to Aakash or Deepak;
  it lands on the board and shows in the owner's view. Goal is to reduce communication friction.
- Design and document drop. Going forward Elvis exports designs from Cloud Design into
  `architecture/elvis/designs/` and documents into `architecture/elvis/documents/` (both already
  git-tracked), then commits and pushes. Aakash pulls to keep one central, in-sync repository.
- Client-specific skill. Aakash is building an Elvis-specific input skill (still in progress) so
  Elvis feeds information to Cloud in the structure Deepak's harness expects, rather than free-form.
  Elvis offered to build planning skills from his side and push them for Aakash to trigger, and
  Aakash asked Elvis to flag any recurring task he wants turned into a skill.
- Context. Aakash noted this harness is the fix for coordination problems he hit on Weatherbox and
  Reflex, and that a working version here could be replicated to those.

## Decisions reached

None. Operational onboarding only. The contribution and merge operating model walked through here
(Claude commits, human pushes; per-person workspaces; designs to `designs/`, docs to `documents/`;
PM merges to shared) reinforces DEC-001 and could be logged as its own decision if wanted; not filed.

## Action items

- Elvis: finish reviewing the GET-STARTED onboarding questions, commit, and push to main. Owner: Elvis.
- Elvis: going forward, drop designs to `architecture/elvis/designs/` and documents to
  `architecture/elvis/documents/`, then commit and push. Owner: Elvis.
- Elvis: adopt the start-session / end-session routine as muscle memory. Owner: Elvis.
- Elvis: flag any recurring task he wants built into a client-specific skill. Owner: Elvis.
- Aakash: finish the Elvis client-specific input skill and push it. Owner: Aakash. (TASK-017.)
- Aakash: add a chat assistant option to the delivery board. Owner: Aakash. (TASK-018, later.)

## Status changes from this call

- TASK-011 (create the repo, invite Elvis, run the setup call) moves to Done, 2026-08-19. The repo
  is live, Elvis has accepted the invite, and the setup walkthrough is complete. todos #3 closed.

## Sentiment

Positive and low-friction. Elvis understood the model quickly, called it a good checks-and-balances,
and said he will trial it and raise questions as they come up.
