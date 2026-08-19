---
name: board-sync
category: maintenance
description: >
  The reconciliation layer for the Wepop delivery board. Reads what has happened (the board,
  comms/todos.md, recent emails and meeting notes, each task's team/tasks activity log, git log,
  DECISIONS and HOTSHEET) and works out which cards should move. Auto-applies the obvious,
  evidence-backed moves (pushed with its TASK-NNN in a commit becomes Done; work clearly started
  becomes In progress; a Blocked task whose blocker is Done gets unblocked) and only asks about
  ambiguous ones (no clear evidence, a status regression, an unclear task match, an implied new
  task). Never invents dates; never regresses a status without asking. Edits through task-board and
  regenerates. Aakash (merger) only writes; others get a report. No git. Triggers on "sync the
  board", "reconcile the board", "catch the board up", "what should move on the board?". BLOCK not
  DENY; no em-dashes.
---

# Skill: board-sync (Wepop)

> `[you]` = the caller's workspace name. This is the RECONCILE layer: it decides what should move on
> the board and applies the obvious moves. The mechanical edits and rendering are `task-board`'s job;
> this skill uses them. The board (`shared/TASK-BOARD.md`, `team/`, `docs/`) is merger-owned: only
> Aakash writes it. If the caller is not Aakash, this skill only REPORTS suggested moves.

## Trigger
- "sync the board", "reconcile the board", "catch the board up", "what should move on the board?",
  "did anything on the board change?". Also a good step after archive-email, process-transcript, a
  merge, or any working conversation that changed a task's state.

## What it reads (the signals)
1. `shared/TASK-BOARD.md` - the current cards, their status and dates.
2. `team/tasks/TASK-NNN.md` - each task's activity log and definition of done.
3. `comms/todos.md` and recent `comms/emails/` + `comms/meeting-notes/` - what was said or agreed.
4. `git log --date=short --pretty="%ad | %s"` - what actually got pushed.
5. `shared/DECISIONS.md` and `shared/HOTSHEET.md` - decisions landed, risks or blocks cleared.
6. The current conversation, if the caller just discussed status.

## The rule: auto-apply the obvious, ask on the ambiguous
Every auto move needs concrete evidence. With evidence, apply it and report it. Without evidence, or
in any of the ambiguous cases below, stop and ask.

### Auto-apply (obvious, evidence-backed)
- **Pushed:** a finished task whose `TASK-NNN` appears in a git commit message -> keep/set Done and
  fill Committed with that commit date.
- **Started:** a To Do task with clear evidence work began (a dated activity line, an email or
  transcript, or Aakash saying so) -> In progress, stamp Started.
- **Finished:** an In progress task with clear evidence it is complete (its definition of done all
  ticked, or a stated or committed completion) -> Done, stamp Ended.
- **Unblocked:** a Blocked task whose blocking `TASK-NNN` is now Done -> move to To Do (or In
  progress if work has visibly started) and drop the "waits on" note.
- Reconcile Committed dates from git log and append activity lines from ingested comms.

### Ask first (ambiguous)
- No concrete evidence for the move (a hunch, a "should be nearly done").
- A status regression (for example Done -> In progress); never automatic.
- The signal does not map cleanly to one task, or maps to several.
- It implies a NEW task, an owner change, a scope change, or a date you cannot ground.
- Two signals disagree; never resolve a conflict silently, surface it.

## Steps
### Step 1 - Read the signals. Build a candidate list: for each task, the proposed move and the exact evidence for it.
### Step 2 - Split candidates into AUTO (evidence-backed, unambiguous) and ASK (everything else).
### Step 3 - Apply the AUTO moves through task-board: edit `shared/TASK-BOARD.md` (stamp Started / Ended from today, stated, or git log only, never invented), fill Committed from git log, append activity lines to `team/tasks/TASK-NNN.md`, and drop any cleared "waits on" note.
### Step 4 - Regenerate: run `python3 team/board-render.py` and refresh the inline `wepop-task-board` artifact.
### Step 5 - Report: list what was auto-applied (task, move, evidence), then present the ASK list as a short numbered set of questions. Apply Aakash's answers the same way, then regenerate again.
### Step 6 - Suggest a name-prefixed commit. Remind that putting the `TASK-NNN` in the commit message lets the next sync fill the Committed date.

## If the caller is not Aakash (merger)
- Do NOT write the board. Produce the same AUTO + ASK analysis as a report, and offer to file the
  suggested moves as `workspaces/[you]/suggestions/suggestion-board-*.md` for Aakash to apply.

## Never
- Move a card without concrete evidence; invent a Started, Ended, or Committed date (today, stated, or git log only).
- Auto-apply a status regression or silently resolve conflicting signals; always ask.
- Write `shared/`, `team/`, or `docs/` when not the merger (report or suggest instead); run git commit / push.
- Create a new task, change an owner, or change scope on your own; propose it and ask.
- Em-dash; DENY.
