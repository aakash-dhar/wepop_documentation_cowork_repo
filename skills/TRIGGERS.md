# TRIGGERS.md - Wepop skills quick reference

Say this -> what it does. Skills are read as a plain `skills/` folder; confirm a skill by its name.

## Session bookkeeping
- "start session" / "good morning" / "catch me up" -> **session-start** (reads the governing layer, briefs you)
- "end session" / "done for today" / "wrap up" -> **session-end** (dual-file log, prepares a commit)

## Capturing what comes in
- "archive this email" / pasted email -> **archive-email** (files it by number, extracts decisions)
- "process this transcript" / pasted transcript -> **process-transcript** (dual-file meeting record)
- "intake document [file]" / "client sent a document" -> **intake-document** (files to reference/ or research/)

## Tracking and decisions
- "propose this decision" / "log this decision" -> **propose-decision** (DEC-NNN proposal)
- "add a risk" / "retire risk N" -> **risk-register** (proposed risk change)
- "track this question" / "open questions" -> **track-open-questions** (routed-question tracker)

## Communicating out
- "draft a reply to Elvis" / "reply to email NN" -> **draft-elvis-reply** (chat-only client reply)
- "call brief" / "brief me before the call" -> **call-brief** (private pre-call rundown)
- "meeting prep" / "draft an agenda" -> **meeting-prep** (agenda for the weekly Wepop sync)

## Reporting
- "status report" / "mgmt update" -> **status-report** (RAG report)
- "weekly digest" / "what happened this week" -> **weekly-digest** (last 7 days)

## Maintaining the shared record
- "update hotsheet" -> **update-hotsheet** (proposed HOTSHEET change)
- "update index" -> **update-index** (proposed PROJECT_INDEX refresh)
- "update the dashboard" -> **dashboard-update** (refresh + snapshot docs/index.html)

## Two reminders
1. Skills that touch the record go through **proposals** - the merger (Aakash) lands them.
2. **Nothing auto-pushes.** The human syncs via GitHub Desktop.
