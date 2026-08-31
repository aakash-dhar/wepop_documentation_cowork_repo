---
name: project-reference
category: maintenance
description: >
  Keeps the Wepop client project reference page (docs/project-reference.html, the BetaCraft-styled
  module-by-module page with detail drawers) current as Elvis's documents and shared/DECISIONS.md
  change. Updates team/project-reference/data.js with a source on every line, runs two validation
  subagents (claim check and citation spot-check), rebuilds with build.py, and publishes behind the
  login gate shared with the dashboard (one salt, one login). Triggers on "update the project
  reference", "refresh the project reference", "Elvis updated his docs, update the reference",
  "publish the reference". Aakash-only for writes; others get a suggestion. Never invents, never
  stores the password, never runs git. Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: project-reference (Wepop)

> Keeps the Wepop project reference (the BetaCraft-styled, module-by-module page with the detail
> drawer) current as Elvis's documents and the decision log change. The page is generated from
> `team/project-reference/data.js` + `template.html` by `build.py`; this skill updates the data,
> validates it, rebuilds, and publishes behind the login gate. `[you]` = the caller's workspace name.
> `team/` and `docs/` are Aakash-owned: only Aakash writes them. Anyone else gets a suggestion file.

## Trigger
- "update the project reference", "refresh the project reference", "rebuild the reference",
  "Elvis updated his docs, update the reference", "publish the reference", "add [module/decision] to
  the reference". Also a good step right after **run-merge** lands new decisions or **design-intake**
  processes a new Elvis document.

## Guard (check first)
- If `[you]` is not aakash: do everything up to Step 4 as analysis only and write the proposed
  `data.js` changes to `workspaces/[you]/suggestions/suggestion-project-reference-YYYY-MM-DD.md`.
  Do not write `team/` or `docs/`.

## Pre-read (mandatory)
1. `team/project-reference/README.md` - how the pipeline works.
2. `team/project-reference/data.js` - read `META` (`asOf`, `lastDec`) to learn the last build point,
   then skim `M`, `ELVIS.modules`, `ELVIS.new`, `PLAIN`, `FLOWS`, `RISKS`, `OPEN`, `LEGAL` (the decision index and
   records are generated from `shared/DECISIONS.md` at build time, not kept here).
3. `shared/DECISIONS.md` - every `DEC-NNN` above `META.lastDec`, and any change-history note dated
   after `META.asOf`.
4. What Elvis changed since the last build: `git log --date=short --name-only --since=<META.asOf> --
   workspaces/elvis comms/attachments` (read-only), plus any file under `workspaces/elvis/` with a
   date in its name after `META.asOf`. Read each changed file fully.
5. `shared/HOTSHEET.md` (risks, blockers) and `shared/TASK-BOARD.md` (task ids) so risk and task
   references stay exact.

## Steps

### Step 1 - Detect what changed
List: new decisions (id, title, what they amend or supersede); Elvis files added or changed since
`META.asOf`; risks added or retired; open items resolved or added. If nothing changed, say so and stop.

### Step 2 - Map each change to the data
For every change decide where it lands in `data.js`, and nowhere else:
- A landed decision that changes a module's behaviour -> update that module's `M` entry (`flow`,
  `rules`, `build`, `open`, `decs`; add the DEC to `decs`, mark a superseded one `DEC-nnn:sup`).
  Keep `sub` and `sum` one-liners current.
- Detail in an Elvis document -> add items to `ELVIS.modules[Mnn]` as `{tag, text, src}`. `tag` is
  exactly one of `DECIDED DEC-nnn`, `ELVIS DESIGN`, or `SUPERSEDED by DEC-nnn`. `src` is
  `<file> > "<section heading>"`. Skip anything already on the page.
- A new Elvis-designed topic with no module -> add to `ELVIS.new` (`title`, `status`, `phase`, `sub`,
  `summary`, and `flow` / `rules` / `build` / `open` as `{text, src}` lists). The page numbers it
  automatically after M24. If it contradicts a landed decision, put the words "conflicts with DEC-nnn"
  in `status` so the page flags it red.
- A new module (decided or Elvis-designed) -> write its `PLAIN` explainer: two to four plain sentences
  that only restate what the module's own data says, for a reader with no context. Never a new fact.
- A module with a real sequence of steps -> add or update its `FLOWS[Mnn]` diagram spec (columns of
  nodes, edges with optional labels, a note). Node and edge labels may only restate that module's own
  `flow` / `rules` (or DECISIONS.md); an arrow asserts a sequence, so never draw one the record does not
  state, and never lift wording from a superseded decision. `FLOWS.overview` and `FLOWS.governance`
  are the two page-level diagrams.
- A new or changed decision -> nothing to do in `data.js`: `build.py` regenerates the decision index and
  the full decision records (`DECS`, `DECFULL`) from `shared/DECISIONS.md` on every build, so the page's
  decisions can never drift from the source of truth. Only the module `decs` chips need updating.
- Risks, open items, legal items -> `RISKS`, `OPEN`, `LEGAL`, mirroring the HOTSHEET wording.
- Finally set `META.asOf` to today and `META.lastDec` to the highest landed DEC.

### Step 3 - Edit `data.js` only
Apply the mapped changes. Quote numbers, prices, thresholds and dates exactly as the source states
them; keep the source's own qualifiers ("not confirmed", "recommendation", "parked", "provisional").
Never edit `template.html` for content, and never edit the built HTML files (they are overwritten).
No em-dashes anywhere in the data.

### Step 4 - Validate (mandatory, two passes)
Run two subagents and fix every finding before building:
1. **Claim validator** - for every `M` entry touched, every `ELVIS` item added, and every `FLOWS`
   diagram touched (each node label, edge label and note, including whether an arrow implies a sequence
   the record does not state), check the text against its cited source and against `shared/DECISIONS.md`. Report anything unsupported, wrongly
   numbered, over-claimed, or tagged with the wrong DEC, with file:line evidence.
2. **Citation spot-check** - sample at least 30 added items (all of them if fewer) and confirm each
   `src` points at a real file and section that supports the text.
Re-run until both come back clean. A finding is never silently dropped.

### Step 5 - Build
`python3 team/project-reference/build.py`. It refuses to build if any ELVIS item lacks a `src` or an
em-dash is present. It writes `team/wepop-project-reference.html` (internal copy).

### Step 6 - Publish behind the gate (Aakash only)
If the board data also changed, run `python3 team/board-render.py` first. Then:
`python3 team/project-reference/build.py --lock --user <user> --password '<password>'`
Ask Aakash for the credentials in chat if they were not given in this session. Never store them in a
file, a memory, or the page. This gates `docs/project-reference.html` and re-gates `docs/index.html`
and `docs/board-public.html` with ONE shared salt, so one login unlocks the dashboard and the reference.
Confirm: no plaintext password in any `docs/` file, the dashboard still carries the "Project reference"
link, and the three pages share the same `SALT`.

### Step 7 - Housekeeping
If a new module or file appeared, make sure `shared/PROJECT_INDEX.md` "Where everything lives" still
points at `team/project-reference/` and `docs/project-reference.html` (propose via
`proposed-project-index.md` unless you are the merger).

### Step 8 - Report and suggest a commit
Summarise: decisions folded in, modules touched, items added (with counts), new modules, any conflict
flagged red, and the validator results. Suggest
`[aakash] project reference refresh: DEC-0xx to DEC-0yy, <Elvis files>` for GitHub Desktop and
remind that nothing is live until the push.

## Never
- Invent, infer, or embellish. Every ELVIS item carries a `src`; a detail you cannot anchor to a line
  in a source stays out.
- Treat an Elvis design as scope, or resolve a conflict with a landed decision. Flag it; DECISIONS wins.
- Edit the built HTML files by hand, or edit `template.html` for content.
- Store or echo the gate password anywhere; run `git commit` or `git push`.
- Write `team/` or `docs/` as anyone but Aakash.
- Em-dash; DENY (governance values are ALLOW / BLOCK / ESCALATE).
