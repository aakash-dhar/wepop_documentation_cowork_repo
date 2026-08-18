---
name: task-board
category: maintenance
description: >
  Maintains the Wepop delivery board. The data is shared/TASK-BOARD.md (per-task lifecycle: owner,
  status, started, ended, pushed, notes); the view is docs/board.html, a light-mode, non-kanban page
  with five tabs (Delivery digest, Timeline, Journal, Now / Next / Later, Scope vs Built), Bootstrap
  container widths, and a right-side detail drawer. Shown live inside Claude desktop as the
  "wepop-task-board" artifact, no file download. Adds and moves tasks (stamping Started and Ended),
  fills the Pushed date from git log, and regenerates the view with docs/board-render.py. Aakash (the
  merger) owns the board; Elvis and Deepak propose tasks via workspaces/[you]/proposed-tasks.md. Does
  no git. Triggers on "show the task board", "task board", "add a task", "start task NNN", "finish
  task NNN", "update the board", "what's in progress?". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: task-board (Wepop)

> `[you]` = the caller's workspace name. `shared/TASK-BOARD.md` and `docs/` are merger-owned; only
> Aakash writes them. Elvis and Deepak propose tasks into their own workspace. The board is always
> shown inline in Claude desktop, never as a file to download. Light mode only; never build a
> kanban or a dark theme (see the UI preferences in project memory).

## Trigger
- "show the task board", "task board", "add a task", "start task [NNN]", "finish task [NNN]" /
  "mark task [NNN] done", "block task [NNN]", "update the board", "what's in progress?".

## The pieces
- `shared/TASK-BOARD.md` - the data (the table of tasks).
- `docs/board-template.html` - the HTML shell (styling lives here).
- `docs/board-render.py` - regenerates `docs/board.html` from the data.
- `docs/board.html` - the rendered board, shown inline as the `wepop-task-board` artifact.

## Board columns
`ID | Task | Owner | Status | Started | Ended | Committed | Notes`. Status is
`To Do / In progress / Blocked / Done`.

## Showing the board (default, one step)
- Regenerate if anything changed, then render `docs/board.html` INLINE in the Cowork side panel:
  update the persisted **wepop-task-board** artifact (or send it with an inline render). Never tell
  the person to open or download the file.

## Steps (when changing the board)
### Step 1 - Identify the change: add a task, move a status, block/unblock, edit notes, or land proposed tasks.
### Step 2 - Add a task:
- **If the caller is Aakash (merger):** add a row to `shared/TASK-BOARD.md` with the next `TASK-NNN`
  (never reuse), the Owner, Status `To Do`, and a Notes line.
- **If the caller is Elvis or Deepak (not the merger):** do NOT write the board. Append a block to
  `workspaces/[you]/proposed-tasks.md` using the format in `PROPOSAL-TEMPLATES.md` (task, suggested
  owner, why / context, priority). This is how Elvis raises work for the dev team: set the suggested
  owner to Deepak and link the decision or design. Aakash lands it.
### Step 3 - Land proposed tasks (Aakash only): scan `workspaces/*/proposed-tasks.md`, assign each the next `TASK-NNN`, add rows to `shared/TASK-BOARD.md`, and replace the landed block with a dated "Landed" note so it is not re-added.
### Step 4 - Move status: `To Do -> In progress` stamps Started; `-> Done` stamps Ended; `-> Blocked` records what it waits on. Use today's date (ask if the date is not today).
### Step 5 - Reconcile Pushed: read `git log --date=short --pretty="%ad | %s"`; for any Done task whose commit message contains its `TASK-NNN`, set Committed to that date. Leave blank if not pushed. Never invent a date.
### Step 6 - Regenerate and show: run `python3 docs/board-render.py`, then refresh the inline `wepop-task-board` artifact from `docs/board.html`.
### Step 7 - Report what changed and suggest a commit. Remind that putting the `TASK-NNN` in the commit message lets the next reconcile fill the Pushed date.

## Never
- Tell the person to download or open the board file; always show it inline.
- Build a kanban or a dark theme; this board is the five-view, light-mode delivery view.
- Reuse or renumber a task id; invent a Started, Ended, or Committed date (today's, stated, or from git log only).
- Let `docs/board.html` drift from the data; always regenerate with `docs/board-render.py`.
- Write `shared/` or `docs/` when not the merger (propose via `proposed-tasks.md` instead); run git commit / push.
- Em-dash; DENY.
