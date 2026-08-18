# TRIGGERS.md - Wepop skills quick reference

Say this -> what it does. Skills are read as a plain `skills/` folder; confirm a skill by its name.
This toolkit is Wepop-only.

## Session bookkeeping
- "start session" / "good morning" / "catch me up" -> **session-start** (reads the governing layer, briefs you)
- "end session" / "done for today" / "wrap up" -> **session-end** (dual-file log, prepares a commit)

## Merging (merger only, run as Aakash)
- "run the merge" / "merge proposals" / "land the proposals" -> **run-merge** (preview a merge plan, land clean proposals into shared/ on your OK, park conflicts, empty landed proposals; no git)

## Capturing what comes in
- "archive this email" / pasted email -> **archive-email** (files it by number, extracts decisions)
- "process this transcript" / pasted transcript -> **process-transcript** (dual-file meeting record)
- "intake document [file]" / "client sent a document" -> **intake-document** (files to reference/ or research/)
- "design intake" / "Elvis pushed designs" / design drop -> **design-intake** (version, catalog screens, diff, flag gaps)

## Tracking and decisions
- "propose this decision" / "log this decision" -> **propose-decision** (DEC-NNN proposal)
- "add a risk" / "retire risk N" -> **risk-register** (proposed risk change)
- "track this question" / "open questions" -> **track-open-questions** (routed-question tracker)
- "scope tracker" / "what's in phase 1?" / "is this in scope?" -> **scope-tracker** (phase / feature matrix)
- "spec sync" / "refresh the product overview" -> **spec-sync** (overview + PROJECT_INDEX kept in sync with DECISIONS)

## Checking alignment and readying build
- "alignment check" / "does this match our decisions?" / "review this draft against the record" -> **alignment-check** (said-vs-produced divergence report against DECISIONS)
- "compliance watch" / "does this touch legal or privacy?" / "what legal items are open?" -> **compliance-watch** (legal / privacy register + flags)
- "engineering handoff" / "make dev tickets for [feature]" / "spec [feature] for build" -> **engineering-handoff** (dev-ready handoff + GitHub issue for Deepak)

## Communicating out
- "draft a reply to Elvis" / "reply to email NN" -> **draft-elvis-reply** (chat-only client reply)
- "call brief" / "brief me before the call" -> **call-brief** (private pre-call rundown)
- "meeting prep" / "draft an agenda" -> **meeting-prep** (agenda for the weekly Wepop sync)
- "release notes" / "client changelog" / "what changed for the client" -> **client-release-notes** (client-facing changelog, for Aakash to send)
- "decision signoff" / "get Elvis to sign off on [X]" -> **decision-signoff** (one-page approval brief + sign-off tracking)
- "design critique" / "push back on this design" / "review Elvis's design" -> **design-critique** (structured pushback on Wepop's own principles, for Elvis)

## Reporting
- "status report" / "mgmt update" -> **status-report** (RAG report)
- "project tracker" / "update the tracker" / "where does the project stand?" -> **update-tracker** (regenerate the one-screen shared/PROJECT_TRACKER.md roll-up)
- "weekly digest" / "what happened this week" -> **weekly-digest** (last 7 days, internal)
- "build status" / "is the build green?" -> **build-status** (reflect code-repo build state on the dashboard)

## Maintaining the shared record
- "update hotsheet" -> **update-hotsheet** (proposed HOTSHEET change)
- "update index" -> **update-index** (proposed PROJECT_INDEX refresh)
- "update the dashboard" -> **dashboard-update** (refresh + snapshot docs/index.html)

## Two reminders
1. Skills that touch the record go through **proposals** - the merger (Aakash) lands them via **run-merge**. The only skill that writes `shared/` directly is **run-merge**, and only when run as Aakash.
2. **Nothing auto-pushes.** The human syncs via GitHub Desktop.
