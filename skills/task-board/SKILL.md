---
name: task-board
category: maintenance
description: >
  Maintains the Wepop delivery board. The data is shared/TASK-BOARD.md (per-task lifecycle: owner,
  status, started, ended, pushed, notes). team/board-render.py regenerates TWO views: the INTERNAL
  full board team/board.html (five tabs: Delivery digest, Timeline, Journal, Now / Next / Later,
  Scope vs Built; Bootstrap widths; right-side detail drawer; light mode), shown inline in Claude as
  the "wepop-task-board" artifact and kept under team/ so GitHub Pages does not publish it; and the
  CLIENT-SAFE public board docs/board-public.html (Overview, Timeline, Scope only; no task list,
  owners, or internal notes), which docs/ publishes via Pages. Adds and moves tasks (stamping Started
  and Ended), fills the Pushed date from git log. Aakash (the merger) owns the board; Elvis and
  Deepak propose tasks via workspaces/[you]/proposed-tasks.md. Does no git. Triggers on "show the
  task board", "task board", "add a task", "start task NNN", "finish task NNN", "update the board",
  "what's in progress?". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: task-board (Wepop)

> `[you]` = the caller's workspace name. `shared/TASK-BOARD.md`, `team/`, and `docs/` are
> merger-owned; only Aakash writes them. Elvis and Deepak propose tasks into their own workspace.
> The internal board is shown inline in Claude, never as a file to download. Light mode only; never
> build a kanban or a dark theme (see the UI preferences in project memory).

## Trigger
- "show the task board", "task board", "add a task", "start task [NNN]", "finish task [NNN]" /
  "mark task [NNN] done", "block task [NNN]", "update the board", "what's in progress?".

## The pieces
- `shared/TASK-BOARD.md` - the data (the table of tasks).
- `team/board-template.html` - the HTML shell for the internal board (styling lives here).
- `team/board-render.py` - regenerates BOTH boards from the data.
- `team/board.html` - the INTERNAL full board (all tasks, owners, notes). Under `team/` so GitHub
  Pages does NOT publish it. Shown to the team inline as the `wepop-task-board` artifact.
- `docs/board-public.html` - the CLIENT-SAFE public board (Overview, Timeline, Scope; no task list,
  owners, or internal notes). `docs/` is what GitHub Pages publishes, so only client-safe content
  goes there. Its curated content lives in the `CLIENT_*` section of `team/board-render.py`.

## Board columns (the data)
`ID | Task | Owner | Status | Started | Ended | Committed | Notes`. Status is
`To Do / In progress / Blocked / Done`.

## Showing the board (default, one step)
- Regenerate if anything changed, then render `team/board.html` INLINE in the Cowork side panel:
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
### Step 3 - Land proposed tasks (Aakash only): scan `workspaces/*/proposed-tasks.md`, assign each the next `TASK-NNN`, add rows to `shared/TASK-BOARD.md`, and replace the landed block with a dated "Landed" note.
### Step 4 - Move status: `To Do -> In progress` stamps Started; `-> Done` stamps Ended; `-> Blocked` records what it waits on. Use today's date (ask if the date is not today).
### Step 5 - Reconcile Pushed: read `git log --date=short --pretty="%ad | %s"`; for any Done task whose commit message contains its `TASK-NNN`, set Committed to that date. Leave blank if not pushed. Never invent a date.
### Step 6 - Regenerate and show: run `python3 team/board-render.py` (it rewrites both `team/board.html` and `docs/board-public.html`), then refresh the inline `wepop-task-board` artifact from `team/board.html`. Keep `docs/board-public.html` client-safe.
### Step 7 - Report what changed and suggest a commit. Remind that putting the `TASK-NNN` in the commit message lets the next reconcile fill the Pushed date.

## Never
- Tell the person to download or open the board file; always show it inline.
- Build a kanban or a dark theme; this board is the five-view, light-mode delivery view.
- Put internal task data, names, owners, or notes into `docs/board-public.html`; it is published
  publicly, so keep it client-safe.
- Reuse or renumber a task id; invent a Started, Ended, or Committed date (today's, stated, or from git log only).
- Let the boards drift from the data; always regenerate with `team/board-render.py`.
- Write `shared/`, `team/`, or `docs/` when not the merger (propose via `proposed-tasks.md` instead); run git commit / push.
- Em-dash; DENY.
