---
name: task-board
category: maintenance
description: >
  Maintains the Wepop delivery board. Data in shared/TASK-BOARD.md (per-task: owner, status, started,
  ended, pushed, notes). team/board-render.py regenerates a light-mode, non-kanban board with six
  tabs (Delivery digest, Timeline, Journal, Now / Next / Later, Scope vs Built, Decisions), KPI cards,
  charts, and a right-side detail drawer. It writes team/board.html (shown inline as the
  wepop-task-board artifact), docs/index.html (the GitHub Pages root), and docs/board-public.html.
  Going live needs a human commit and push in GitHub Desktop. Adds and moves
  tasks (stamping Started and Ended) and fills Pushed from git log. Aakash (the merger) owns the board;
  Elvis and Deepak propose tasks via workspaces/[you]/proposed-tasks.md. Does no git. Triggers on
  "show the task board", "add a task", "start task NNN", "finish task NNN", "update the board",
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

## Related
- **board-sync** decides WHAT should move (reads comms, git log, activity, decisions and reconciles).
  This skill (`task-board`) is the mechanical layer it calls to make the actual edits and re-render.

## The pieces
- `shared/TASK-BOARD.md` - the data (the table of tasks).
- `team/board-template.html` - the HTML shell for the internal board (styling lives here).
- `team/board-CHANGELOG.md` - the board's version history. When you change the board's DESIGN or
  features (not the data), add an entry at the top and bump the version; the footer shows it.
- `team/board-render.py` - regenerates all board outputs from the data. It reads tasks from
  `shared/TASK-BOARD.md`, per-task detail from `team/tasks/`, decisions from `shared/DECISIONS.md`,
  and risks from `shared/HOTSHEET.md`, and writes `docs/index.html` (Pages root),
  `docs/board-public.html`, and `team/board.html`.
- `team/tasks/TASK-NNN.md` - per-task DETAIL (Overview, Linked sources, Activity, Definition of
  done, Blockers). This is what the task side panel shows in full. Format in `team/tasks/_TEMPLATE.md`.
  The ingestion skills (archive-email, process-transcript) append Source and Activity lines here as
  calls, emails, and Slack arrive, so the panel gets richer over time. Merger writes; others propose.
- `team/board.html` - the INTERNAL full board (all tasks, owners, notes). Under `team/` so GitHub
  Pages does NOT publish it. Shown to the team inline as the `wepop-task-board` artifact.
- `docs/index.html` - the board served at the GitHub Pages ROOT url. Per Aakash's decision it is the
  FULL board (owners, notes, detail, decisions, risks), not a sanitized subset. `docs/board-public.html`
  is a copy kept so older links resolve. `docs/` is public, so this board is world-readable while the
  repo is public. If the repo goes private, switch to the sanitized `render_public` kept in
  `team/board-render.py`.

## Board columns (the data)
`ID | Task | Owner | Status | Started | Ended | Committed | Notes`. Status is
`To Do / In progress / Blocked / Done`.

## Showing the board (default, one step)
- Regenerate if anything changed, then render `team/board.html` INLINE in the Cowork side panel:
  update the persisted **wepop-task-board** artifact (or send it with an inline render). Never tell
  the person to open or download the file.

## Publishing to GitHub Pages (making an update go live)
Regenerating (Step 6) refreshes the files on disk and the inline artifact, but the PUBLIC board at the
GitHub Pages URL only changes after a human pushes. The agent never runs git. Finish an update like this:
1. Regenerate: `python3 team/board-render.py`. This rewrites `docs/index.html` (the Pages root),
   `docs/board-public.html`, and `team/board.html`.
2. Tell Aakash to open **GitHub Desktop**, review the changed files, and commit with a name-prefixed
   message. Put any finished task's `TASK-NNN` in the message so the next reconcile (Step 5) fills its
   Pushed date, for example `[aakash] TASK-016 handoff + board refresh`.
3. Push in GitHub Desktop. GitHub Pages rebuilds in a minute or two, then the live URL shows the update.
   Nothing is live until this push happens.
The Wednesday "board refresh" scheduled task runs this same hygiene and flags uncommitted changes. The
board can only be regenerated while the Claude desktop app is open with the repo folder connected.

## Steps (when changing the board)
### Step 1 - Identify the change: add a task, move a status, block/unblock, edit notes, or land proposed tasks.
### Step 2 - Add a task:
- **If the caller is Aakash (merger):** add a row to `shared/TASK-BOARD.md` with the next `TASK-NNN`
  (never reuse), the Owner, Status `To Do`, and a Notes line.
- **If the caller is Elvis or Deepak (not the merger):** do NOT write the board. Append a block to
  `workspaces/[you]/proposed-tasks.md` using the format in `PROPOSAL-TEMPLATES.md` (task, suggested
  owner, why / context, priority). This is how Elvis raises work for the dev team: set the suggested
  owner to Deepak and link the decision or design. Aakash lands it.
### Step 2b - Give a substantive task a detail file: create `team/tasks/TASK-NNN.md` from
`team/tasks/_TEMPLATE.md` and fill Overview + Definition of done at least. Sources and Activity
accrue automatically as the ingestion skills run. A task with no detail file still renders a basic
panel from its Notes, so this is optional but recommended for anything real.
### Step 3 - Land proposed tasks (Aakash only): scan `workspaces/*/proposed-tasks.md`, assign each the next `TASK-NNN`, add rows to `shared/TASK-BOARD.md`, and replace the landed block with a dated "Landed" note.
### Step 4 - Move status: `To Do -> In progress` stamps Started; `-> Done` stamps Ended; `-> Blocked` records what it waits on. Use today's date (ask if the date is not today).
### Step 5 - Reconcile Pushed: read `git log --date=short --pretty="%ad | %s"`; for any Done task whose commit message contains its `TASK-NNN`, set Committed to that date. Leave blank if not pushed. Never invent a date.
### Step 6 - Regenerate and show: run `python3 team/board-render.py` (it writes `docs/index.html` [Pages root], `docs/board-public.html`, and `team/board.html`), then refresh the inline `wepop-task-board` artifact.
### Step 7 - Report what changed and suggest a commit. Remind that putting the `TASK-NNN` in the commit message lets the next reconcile fill the Pushed date.

## Never
- Tell the person to download or open the board file; always show it inline.
- Build a kanban or a dark theme; this board is the five-view, light-mode delivery view.
- Forget that `docs/index.html` (and `docs/board-public.html`) is published publicly while the repo
  is public; that is Aakash's current choice. If the repo goes private, switch to the sanitized `render_public`.
- Reuse or renumber a task id; invent a Started, Ended, or Committed date (today's, stated, or from git log only).
- Let the boards drift from the data or the detail files; always regenerate with `team/board-render.py`.
- Put client-unsafe detail in `team/tasks/` while `docs/` is public: the full board (with detail) is
  published, so keep task detail client-appropriate (or move to a private repo, see render_public).
- Write `shared/`, `team/`, or `docs/` when not the merger (propose via `proposed-tasks.md` instead); run git commit / push.
- Em-dash; DENY.
