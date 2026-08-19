# Elvis setup call - runbook (2026-08-19)

Goal: Elvis leaves the call able to push designs and documents into the repo himself.
Time: about 15 minutes. Elvis is on a Mac. Step 1 (GitHub invite) is already accepted.

## Before the call (Aakash)
- Push your latest commit so Elvis pulls a clean repo: it must include his drop folders
  (architecture/elvis/designs, architecture/elvis/documents), the updated GET-STARTED-ELVIS.md,
  and the board changes.
- Have GET-STARTED-ELVIS.md open to walk from Part 1.

## On the call - click by click
1. Confirm the invite: Elvis is a collaborator on the repo (step 1 done).
2. Install GitHub Desktop: desktop.github.com -> Download for macOS -> open the app ->
   sign in with the GitHub account tied to programinator-elvis.
3. Clone the repo: File -> Clone repository -> GitHub.com tab -> pick
   wepop_documentation_cowork_repo -> choose a local folder (e.g. Documents/GitHub) -> Clone.
4. Tour the folder: point out architecture/elvis/designs/ and /documents/ (with their READMEs),
   and GET-STARTED-ELVIS.md. Remind him: everything he pushes stays inside architecture/elvis/.
5. Connect Claude: install the Claude desktop app, sign in, then On your computer -> Add folder ->
   pick the cloned repo folder. Have him type "start session" and confirm he gets a briefing.
6. Do a real first push together:
   - Quickest: in Claude Design, export any screen as Standalone HTML into
     architecture/elvis/designs/2026-08-19_test/ (or drop a small placeholder file there).
   - GitHub Desktop shows the change. Summary: "[elvis] first design push". Commit to main. Push origin.
7. Confirm receipt: on your machine, Fetch origin / Pull, and confirm the file arrived.
8. Recap the everyday loop: Pull -> work -> Commit with "[elvis] ..." -> Push. And say
   "design intake" when he drops designs so Claude versions and catalogs them.

## If something sticks
- Repo not in the clone list: invite not accepted yet, or he is signed into the wrong GitHub account.
- Push rejected / out of date: Fetch origin, Pull, then Push again.
- Claude cannot see the folder: re-add the folder (On your computer -> Add folder); make sure the
  desktop app is connected.
- Nothing to commit after export: the file was saved outside the repo folder; re-export into
  architecture/elvis/designs/.

## After the call - update the board
- Tick the TASK-011 definition-of-done items that got done (GitHub Desktop + clone, Claude connected,
  first push).
- If the first push landed, TASK-011 can move to Done once it is pushed with TASK-011 in the message.
