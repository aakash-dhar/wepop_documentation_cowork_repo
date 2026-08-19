# TASK-015 - Investigate pushing design output from Cowork to the repo

## Overview
Question: can Elvis push his Claude Design work and documents straight into the shared repo from his
end? Investigated with Aakash on 2026-08-19.

Finding: not directly from Claude Design. Claude Design has no GitHub or repo integration yet
(planned but not shipped), and the GitHub "connect" option in Claude is read-only. The working path
is a quick export and push: Elvis exports Standalone HTML from Claude Design (or PDF/Word for
documents), saves it into his own area in the repo, and commits and pushes with GitHub Desktop, the
same model Aakash and code already use.

## Sources
- slack | Elvis + Aakash, 2026-08-19 | | Agreed to do the setup on the call; Elvis has the GitHub invite done
- doc | Claude Design announcement | https://www.anthropic.com/news/claude-design-anthropic-labs | Exports: Canva, PDF, PPTX, standalone HTML; no repo push yet
- doc | GitHub integration (Anthropic) | https://support.claude.com/en/articles/10167454-use-the-github-integration | The GitHub connect is read-only

## Activity
- 2026-08-19 | Investigated; confirmed the export-then-push flow is the way.
- 2026-08-19 | Set up architecture/elvis/designs + documents with READMEs; added the "Pushing designs and documents" section to GET-STARTED-ELVIS.md and wired the Slack note.

## Definition of done
- [x] Confirmed whether a direct push is possible (it is not, yet)
- [x] Documented the working flow (export Standalone HTML -> GitHub Desktop -> push)
- [x] Set up Elvis's drop folders and onboarding steps
- [x] Sent Elvis the how-to (Slack)

## Blockers
