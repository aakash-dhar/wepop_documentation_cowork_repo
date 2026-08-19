# Wepop delivery board - changelog

Version and change history for the delivery board (docs/index.html, docs/board-public.html,
team/board.html). Newest at top. Bump the version and add an entry whenever the board's design or
features change. The top version and date show in the board footer. Format: `## vX.Y - YYYY-MM-DD`.

## v1.0 - 2026-08-19
- Added a KPI hero strip (percent complete, done, in progress, blocked, to do).
- Added charts: status donut, workload by owner, design-vs-build phase progress, Journal
  activity-by-day, and a cumulative burn-up.
- Added a sixth tab, Decisions, generated from shared/DECISIONS.md (expandable per decision).
- Added a risk register card from shared/HOTSHEET.md and task aging markers.
- Added a "Changed this week" delta feed on the digest; made milestones and scope rows expand inline.
- Introduced board versioning and this changelog; the version now shows in the footer.

## v0.5 - 2026-08-19
- Hardened against content overflow across all rows; validated at four widths.

## v0.4 - 2026-08-18
- Added the per-task detail panel (overview, linked sources, activity, definition of done, blockers),
  fed from team/tasks/TASK-NNN.md and auto-updated by the ingestion skills.

## v0.3 - 2026-08-18
- Applied the BetaCraft brand: red accent, Space Grotesk and Inter, the betacraft wordmark, and the
  real logo.svg on a dark navigation bar (light content).

## v0.2 - 2026-08-18
- Made the full six-view board the GitHub Pages root (docs/index.html); retired the old dark
  narrative dashboard (archived at team/legacy-dashboard.html).

## v0.1 - 2026-08-18
- First light-mode, non-kanban delivery board with five views and a right-side detail drawer.
