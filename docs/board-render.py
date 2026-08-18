#!/usr/bin/env python3
"""
Regenerates docs/board.html (the Wepop delivery board) from shared/TASK-BOARD.md.

Run from the repo root:  python3 docs/board-render.py

Light mode only. Non-kanban: five views (Delivery digest, Timeline, Journal,
Now / Next / Later, Scope vs Built), Bootstrap-style container widths, and a
right-side detail drawer (half screen). Task rows come from
shared/TASK-BOARD.md. Milestones, the Now/Next/Later horizon, and the scope
list are maintained in this file for now; keep them in step with
shared/PROJECT_TRACKER.md and architecture/phase-plan/wepop-product-overview.md.
The HTML shell is docs/board-template.html (edit styling there). No em-dashes.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOARD = os.path.join(ROOT, "shared", "TASK-BOARD.md")
TEMPLATE = os.path.join(ROOT, "docs", "board-template.html")
OUT = os.path.join(ROOT, "docs", "board.html")

HORIZON = {"TASK-010": "next", "TASK-011": "next", "TASK-012": "next",
           "TASK-013": "later", "TASK-014": "later", "TASK-015": "later", "TASK-016": "later"}

MILESTONES = [
 {"name": "First design walkthrough", "date": "2026-08-17", "status": "done", "note": "Elvis, Aakash, Deepak"},
 {"name": "Elvis GitHub ID received", "date": "2026-08-18", "status": "done", "note": "programinator-elvis"},
 {"name": "First project docs received", "date": "2026-08-18", "status": "done", "note": "as a draft; reviewed version pending"},
 {"name": "GitHub repo + invite + setup call", "date": "waiting on reviewed docs", "status": "next", "note": "gated on the final documentation"},
 {"name": "Location-at-registration locked", "date": "open", "status": "next", "note": "optional vs required, needs Elvis"},
 {"name": "Phase-1 build kickoff", "date": "not started", "status": "later", "note": "after harness + scope lock"},
 {"name": "Phase-1 MVP", "date": "target late Aug 2026", "status": "later", "note": "per the Moments spec"},
]

SCOPE = [
 {"area": "Waitlist (non-invited signups)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Onboarding (invited flow)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Registration (OTP, age gate, map picker)", "phase": "1", "designed": "draft", "built": "no", "note": "age gate provisional, pending counsel (R1)"},
 {"area": "Login (auto-detect, biometrics)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Ideas (polls, discussion)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Events (create, discussion, media, chat)", "phase": "1", "designed": "draft", "built": "no", "note": "save-as-draft screen still to add"},
 {"area": "Explore (map, list, filters, search)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Home (recommendations)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Event / group chat (text only)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Notifications (simple set)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Profiles (user + org, moments)", "phase": "1", "designed": "partial", "built": "no", "note": "profile screens still being finished"},
 {"area": "Moments / Reflections (P0 groundwork)", "phase": "1", "designed": "draft", "built": "no", "note": "v0.9; conflicts to reconcile"},
 {"area": "Calendar (device calendar)", "phase": "later", "designed": "draft", "built": "no", "note": "deferred (DEC-009)"},
 {"area": "DMs / user-created group chats", "phase": "later", "designed": "draft", "built": "no", "note": "deferred (DEC-009)"},
 {"area": "'Close to new joiners' toggle exposed", "phase": "later", "designed": "na", "built": "no", "note": "built but hidden in phase 1"},
 {"area": "Ratings / reviews", "phase": "contested", "designed": "draft", "built": "no", "note": "drafts disagree, needs a decision"},
 {"area": "In-app AI image / video generation", "phase": "excluded", "designed": "na", "built": "na", "note": "excluded (DEC-007)"},
]


def main():
    tasks, asof = [], ""
    for line in open(BOARD, encoding="utf-8"):
        if line.startswith("**As of:**"):
            asof = line.split("**As of:**", 1)[1].strip()
        if line.startswith("| TASK-"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            tasks.append(dict(id=c[0], task=c[1], owner=c[2], status=c[3],
                              started=c[4], ended=c[5], committed=c[6], notes=c[7]))
    data = json.dumps({"tasks": tasks, "horizon": HORIZON, "milestones": MILESTONES, "scope": SCOPE})
    shell = open(TEMPLATE, encoding="utf-8").read()
    html = shell.replace("__ASOF__", asof or "").replace("__DATA__", data)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", OUT, "(%d tasks)" % len(tasks))


if __name__ == "__main__":
    main()
