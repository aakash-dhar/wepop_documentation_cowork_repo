# WEP001 - Wepop

> Front door for the Wepop documentation and delivery repo. Read this first, then CLAUDE.md.

**Project:** WEP001 - Wepop
**Client:** Elvis (embedded as client and designer)
**Team:** Aakash (principal PM, project owner, merger, financials), Elvis (client and designer), Deepak (tech lead and developer)

**About the product:** Wepop is an invite-first, location-based events and meetup app for getting
people together in the real world around shared activities. It is a meetup app, not a dating app.
See `CLAUDE.md` section 8 for the architecture and `shared/PROJECT_STRATEGY.md` for the commercial
narrative.

This is a **team documentation and delivery repo**, not a code repo. Code lives in separate
repos. Several people each run their own Cowork (or Claude Code) session against this same
GitHub repo, and share one record without stepping on each other. Three mechanisms make that
work: workspace isolation, a proposal-plus-merger model, and a shared skills toolkit. A
dual-file session log records who did what, every session.

This repo is Wepop-only and is maintained separately from any other engagement.

> **New to the repo?** Start with `GET-STARTED-ELVIS.md` for step-by-step setup (GitHub Desktop plus
> the Claude desktop app), the safety rules, and a checklist you can tick off.

## Start here

| Read | For |
|------|-----|
| `CLAUDE.md` | Project context and the mandatory session rules |
| `OWNERS.md` | Who is allowed to write where |
| `CONVENTIONS.md` | How the repo grows (naming, phases, archiving) |
| `PROPOSAL-TEMPLATES.md` | The exact formats to use when proposing a change |

## What is canonical

- `shared/` - the source of truth (merger-only: DECISIONS, HOTSHEET, PROJECT_INDEX, PROJECT_STRATEGY, PROJECT_TRACKER, TASK-BOARD, MERGE-REVIEW)
- `contracts/` - SOWs, pricing, invoices (financials owner)
- `workspaces/` - one private space per person
- `comms/` - client communications (emails, meeting notes, slack, attachments)
- `architecture/` - non-code design and planning
- `skills/` - the shared PM toolkit
- `docs/` - the client-facing pages published by GitHub Pages. The root page (`docs/index.html`) is the full five-view BetaCraft delivery board; `docs/board-public.html` is a copy kept so older links still resolve
- `research/` and `reference/` - background and grounding inputs

## What is archived

- `_legacy/` is read-only. Superseded and completed material moves here as a unit.

## Skills (the PM toolkit)

The repo ships 30 repeatable PM skills in `skills/`, each a single `SKILL.md`. Say the trigger in a
Cowork or Claude Code session with this repo open. Full trigger list in `skills/TRIGGERS.md`; the
category table in `skills/README.md`. Skills never run git and never write `shared/` directly (the
one exception is `run-merge`, run by the merger). Anything client-facing is drafted for Aakash to
review and send.

### Session and merge

| Skill | Say this | What it does |
|-------|----------|--------------|
| session-start | "start session", "good morning", "catch me up" | Reads the governing layer in order and briefs you before any work |
| session-end | "end session", "wrap up", "done for today" | Writes the dual-file session log and prepares a name-prefixed commit |
| run-merge | "run the merge", "land the proposals" | Merger-only. Previews a merge plan, lands clean proposals into shared/, parks conflicts in MERGE-REVIEW |

### Capturing what comes in

| Skill | Say this | What it does |
|-------|----------|--------------|
| archive-email | "archive this email", or paste an email | Files an incoming email by the numbered convention and extracts any decisions |
| process-transcript | "process this transcript", or paste a transcript | Saves a verbatim plus synthesized meeting record and proposes decisions / risks |
| intake-document | "intake document [file]", "client sent a document" | Files an external doc into reference/ or research/ with a notes companion |
| design-intake | "design intake", "Elvis pushed designs" | Versions a design drop, catalogs the screens, diffs it, and flags gaps |
| propose-decision | "propose this decision", "log this decision" | Files a decision as a DEC-NNN proposal for the merger to land |

### Tracking and the shared record

| Skill | Say this | What it does |
|-------|----------|--------------|
| risk-register | "add a risk", "retire risk N" | Proposes a risk-register change |
| track-open-questions | "track this question", "open questions" | Tracks questions routed to Elvis or Deepak so they are not lost |
| scope-tracker | "what's in phase 1?", "is this in scope?" | Maintains the phase / feature matrix grounded in decisions and designs |
| spec-sync | "spec sync", "refresh the product overview" | Keeps the product overview and PROJECT_INDEX in sync with DECISIONS |
| update-tracker | "project tracker", "where does the project stand?" | Regenerates the one-screen PROJECT_TRACKER status roll-up |
| task-board | "show the task board", "add a task", "start task NNN", "finish task NNN" | Tracks tasks with start / end / pushed dates and renders the six-view delivery board (shown inline; published at docs/index.html) |
| board-sync | "sync the board", "reconcile the board", "what should move?" | Reconciles the board with what has happened: auto-applies the obvious card moves and asks only on the ambiguous ones |
| update-hotsheet | "update hotsheet" | Proposes a HOTSHEET change |
| update-index | "update index" | Proposes a PROJECT_INDEX refresh |

### Checking alignment and readying build

| Skill | Say this | What it does |
|-------|----------|--------------|
| alignment-check | "alignment check", "does this match our decisions?" | Cross-checks an incoming artifact against DECISIONS and the scope matrix, reporting divergences tagged MATCH / CHANGED / ADDED / DOCS-DISAGREE / OPEN |
| compliance-watch | "compliance watch", "does this touch legal or privacy?" | Tracks legal and privacy items (age, PIPA, minors, OTP deliverability, moderation) and flags decisions or designs that touch them |
| engineering-handoff | "engineering handoff", "make dev tickets for [feature]" | Turns a decided and designed feature into a developer-ready handoff and paste-ready GitHub issue for Deepak |

### Communicating out (client-facing, drafted for Aakash to send)

| Skill | Say this | What it does |
|-------|----------|--------------|
| draft-elvis-reply | "draft a reply to Elvis", "reply to email NN" | Drafts a client reply to Elvis in Aakash's house style (chat only) |
| call-brief | "call brief", "brief me before the call" | Private pre-call rundown for the PM |
| meeting-prep | "meeting prep", "draft an agenda" | Shareable agenda for the weekly Wepop sync |
| client-release-notes | "release notes", "client changelog" | Client-facing changelog of what changed and got decided since a date or version |
| decision-signoff | "decision signoff", "get Elvis to sign off on [X]" | Packages a decision as a one-page approval brief, tracks the sign-off, routes to propose-decision on yes |
| design-critique | "design critique", "push back on this design" | Structured design pushback grounded in Wepop's invariants and decisions, for Elvis |

### Reporting and dashboard

| Skill | Say this | What it does |
|-------|----------|--------------|
| status-report | "status report", "mgmt update" | RAG status report for leadership or the client |
| weekly-digest | "weekly digest", "what happened this week" | Internal digest of the last seven days |
| build-status | "build status", "is the build green?" | Reflects code-repo build / PR / release status on the dashboard |
| dashboard-update | "update the dashboard" | Thin wrapper over the board: refreshes the delivery board that is served at docs/index.html (regenerated by team/board-render.py, never hand-edited) |

## Syncing

Sync is done by a human through **GitHub Desktop**. The agent never runs `git pull`,
`git commit`, or `git push`. Skills only suggest a name-prefixed commit message.
