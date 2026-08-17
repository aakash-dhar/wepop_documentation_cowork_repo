# OWNERS.md - file ownership map (Wepop, WEP001)

Defines who can write where. Ownership model v1, 2026-08-17.

## The ownership model

- **Aakash - Principal PM and project owner (and financials owner).** Owns the project end to end:
  the client relationship, comms, proposals, the merger, decisions, the hotsheet, the dashboard,
  strategy, and final approval of client-facing material. Also owns the financials: contracts, SOWs,
  pricing, invoices, and the dollar side of scope classification (Change-Order vs absorbed fee).
- **Elvis - Client and designer.** Owns design docs and design direction, and is the client-side
  approver for client-facing material. Contributes to the shared record via proposals like everyone else.
- **Deepak - Tech lead and developer.** Owns technical design and code in the code repos. Contributes
  here via proposals, and may direct-push a shared doc when it is time-sensitive (see the exception below).

## Ownership rules

| Path | Owner | Rule |
|------|-------|------|
| `workspaces/aakash/` | Aakash | Only Aakash writes. |
| `workspaces/elvis/` | Elvis | Only Elvis writes. |
| `workspaces/deepak/` | Deepak | Only Deepak writes. |
| `shared/DECISIONS.md` | Merger (Aakash) | Everyone else proposes via `proposed-decisions.md`. |
| `shared/HOTSHEET.md` | Merger (Aakash) | Everyone else proposes via `proposed-hotsheet.md`. |
| `shared/PROJECT_INDEX.md` | Merger (Aakash) | Everyone else proposes via `proposed-project-index.md`. |
| `shared/PROJECT_STRATEGY.md` | Merger (Aakash) | Proposals only. |
| `shared/MERGE-REVIEW.md` | Merger (Aakash) | Merger-only queue. |
| `contracts/` | Financials owner (Aakash) | Others suggest via `suggestions/`. |
| `architecture/elvis/` | Elvis | Client and designer authored. Others suggest. |
| `architecture/technical/` | Deepak | Tech design docs, NO code. Others suggest. |
| `architecture/phase-plan/` | Aakash | Operational planning and effort estimates. Others suggest. |
| `comms/` | Aakash (PM) | Ingestion skills write here on behalf of the caller; PM owns the record. |
| `docs/` | Aakash (PM) | Client-facing dashboard. Content-only updates via dashboard-update. |
| `research/` | Anyone | Anyone can add background inputs. |
| `reference/` | Anyone (with `_NOTES.md` companions) | Grounding docs; add a companion notes file. |
| `_legacy/` | Read-only | Archived / superseded / completed. Do not edit in place. |

## Direct-push exception

The tech lead / developer (Deepak) may edit a shared doc directly when it is time-sensitive or
blocks implementation, committing `[deepak][review-needed] ...` and logging it. Aakash reviews at
the next session start (session-start step 6).

## How to propose changes to shared docs

Create a `proposed-*.md` in your workspace using the formats in `PROPOSAL-TEMPLATES.md`. The merger
(Aakash) lands clean proposals; conflicting proposals on the same topic go to `shared/MERGE-REVIEW.md`.
Price, contract, or scope items escalate to the financials owner (also Aakash here).

## How to suggest changes to owned folders

Create a file in `workspaces/[you]/suggestions/` named `suggestion-[topic].md`. The owner decides.
