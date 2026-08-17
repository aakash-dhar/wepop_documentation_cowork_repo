---
name: draft-elvis-reply
category: delivery
description: >
  Drafts an outbound client reply to Elvis in the PM's house style, grounded in the latest
  DECISIONS.md and the email or topic being answered. Chat-only, writes no files. If the reply
  commits to something new it flags it and offers propose-decision but never files automatically.
  Triggers on "draft a reply to Elvis", "reply to email NN", "write Elvis back about X".
  Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: draft-elvis-reply (Wepop)

> [you] = the caller's workspace name. Output is chat only. Writes no files, commits nothing.

## Trigger
- "draft a reply to Elvis", "draft an email to Elvis", "reply to email NN", "draft a note back to the client", "write Elvis back about [X]".

## Pre-read
1. The email / topic (read `comms/emails/NN_*.md` in full if referenced).
2. `shared/DECISIONS.md` (locked positions).
3. `workspaces/[you]/proposed-decisions.md` (in-flight).
4. 1-2 recent thread emails.
5. `comms/summary.md` (sentiment).

## House style
- Greeting "Hi Elvis,"; sign-off "Best," then [you].
- Open with a one-line thanks + a short framing sentence.
- Number multi-point answers with a bold header per point.
- Plain confident prose, short paragraphs, position then reason.
- Isolate any open item in a single closing paragraph.
- Close with a light live-walkthrough offer.

## Hard rules
- End with the client-facing gate: "For Aakash to review/send."
- No em-dash; BLOCK-not-DENY; do not over-claim; do not commit to anything undecided without flagging.

## Steps
### Step 1 - Identify what is being answered (mirror a numbered email's structure).
### Step 2 - Ground each point in a locked decision or mark it an open item.
### Step 3 - Draft in chat.
### Step 4 - Flag any new commitment and offer propose-decision.
### Step 5 - Offer to revise or (on request only) save an outbound record.

## Never
- Write or commit files; auto-file a decision; invent a position on an unsettled point; em-dash; DENY.
