# WEP001 - Wepop

> Front door for the Wepop documentation and delivery repo. Read this first, then CLAUDE.md.

**Project:** WEP001 - Wepop
**Client:** Elvis (embedded as client and designer)
**Team:** Aakash (principal PM, project owner, merger, financials), Elvis (client and designer), Deepak (tech lead and developer)

This is a **team documentation and delivery repo**, not a code repo. Code lives in separate
repos. Several people each run their own Cowork (or Claude Code) session against this same
GitHub repo, and share one record without stepping on each other. Three mechanisms make that
work: workspace isolation, a proposal-plus-merger model, and a shared skills toolkit. A
dual-file session log records who did what, every session.

## Start here

| Read | For |
|------|-----|
| `CLAUDE.md` | Project context and the mandatory session rules |
| `OWNERS.md` | Who is allowed to write where |
| `CONVENTIONS.md` | How the repo grows (naming, phases, archiving) |
| `PROPOSAL-TEMPLATES.md` | The exact formats to use when proposing a change |

## What is canonical

- `shared/` - the source of truth (merger-only: DECISIONS, HOTSHEET, PROJECT_INDEX, PROJECT_STRATEGY, MERGE-REVIEW)
- `contracts/` - SOWs, pricing, invoices (financials owner)
- `workspaces/` - one private space per person
- `comms/` - client communications (emails, meeting notes, slack, attachments)
- `architecture/` - non-code design and planning
- `skills/` - the shared PM toolkit
- `docs/` - the client-facing delivery dashboard (GitHub Pages)
- `research/` and `reference/` - background and grounding inputs

## What is archived

- `_legacy/` is read-only. Superseded and completed material moves here as a unit.

## Syncing

Sync is done by a human through **GitHub Desktop**. The agent never runs `git pull`,
`git commit`, or `git push`. Skills only suggest a name-prefixed commit message.
