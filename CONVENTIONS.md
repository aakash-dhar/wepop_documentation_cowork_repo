# CONVENTIONS.md - how the Wepop repo grows

The anti-reorg charter. This skeleton is a reusable, client-agnostic template; Wepop is one
instance of it. A future project can fork the same structure.

## The stable skeleton

Top-level folders are functional and few. New work slots into these; it does not add new top-level
folders.

```
README.md, CLAUDE.md, OWNERS.md, PROPOSAL-TEMPLATES.md, CONVENTIONS.md   <- the rulebook
shared/        source of truth, merger-only
contracts/     SOWs / pricing, phase-structured (financials owner)
comms/         client communications
architecture/  non-code design and planning
research/      background inputs (anyone can add)
reference/     authoritative / grounding docs (with _NOTES.md companions)
workspaces/    one private space per person
skills/        the shared PM toolkit
docs/          client-facing delivery dashboard (GitHub Pages - must stay named docs/)
_legacy/       archived / superseded / completed - read-only
```

## Two growth axes

- **Phase is the main growth axis.** Phase-specific material is phase-foldered
  (`contracts/phase-N/`, `architecture/phases/phase-N/`) so each phase has one home and closes as
  a unit. Decisions, comms, and the hotsheet are chronological and cross-phase - do NOT phase-folder
  them; reference the phase inside the entry.
- **Verticals grow in the data and code, not the folder tree.** New areas appear only as research
  inputs and as scope language in contracts. No top-level folder per vertical.

## Archive on completion

When a phase fully closes, move its phase folders to `_legacy/` as a unit. When a doc is superseded,
move the old version to the nearest `_archive/`. Never keep v1/v2/v3 siblings in a live folder.

## No big-bang reorgs

Restructuring is a last resort. Moving files breaks path references across `shared/`, session logs,
and the skills. Changes to the skeleton go through a proposal.

## Naming conventions

- **Emails:** `comms/emails/NN_YYYY-MM-DD_kebab-subject.md` (sequential NN, zero-padded, never
  reused, never renumbered).
- **Meeting notes:** `comms/meeting-notes/YYYY-MM-DD_short-title.md` plus `..._TRANSCRIPT.md` when a
  verbatim exists.
- **Session logs:** `workspaces/[you]/session_log_YYYY-MM-DD.md` (add `_sessionN` for multiple in one
  day), plus a rolling `SESSION-LOG.md` index (newest at top).
- **Phase docs:** `Wepop_Phase-N_Description.docx`.
- Files predating a convention are left in place; the convention applies to new files.
