#!/usr/bin/env python3
"""
Regenerates BOTH Wepop boards from shared/TASK-BOARD.md. Run from the repo root:

    python3 team/board-render.py

Outputs:
  team/board.html         - INTERNAL full board (five views, all tasks and notes).
                            Lives under team/ so it is NOT published by GitHub Pages.
                            Shown to the team inline in Cowork as the wepop-task-board artifact.
  docs/board-public.html  - CLIENT-SAFE public board (Overview, Timeline, Scope only; no internal
                            task list, owners, or internal notes). docs/ is what GitHub Pages
                            publishes, so only client-safe content goes there.

Keep the CLIENT_* content below client-appropriate. Light mode only. No em-dashes.
"""
import json, os

SELF = os.path.dirname(os.path.abspath(__file__))          # team/
ROOT = os.path.dirname(SELF)                               # repo root
BOARD = os.path.join(ROOT, "shared", "TASK-BOARD.md")
INT_TEMPLATE = os.path.join(SELF, "board-template.html")
INT_OUT = os.path.join(SELF, "board.html")
PUB_OUT = os.path.join(ROOT, "docs", "board-public.html")

# ---- internal-only view data (full board) ----
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

# ---- client-safe view data (public board). Curated; keep it client-appropriate. ----
CLIENT_HEALTH = ("On track", "Design direction agreed, core product decisions locked, and coordination set up. No blockers.")
CLIENT_MILESTONES = [
 {"name": "Project kickoff and full design walkthrough", "date": "2026-08-17", "status": "done", "note": ""},
 {"name": "Core product decisions locked", "date": "2026-08-17", "status": "done", "note": "nine decisions"},
 {"name": "Shared coordination repo and workflow", "date": "2026-08-18", "status": "done", "note": ""},
 {"name": "Project documentation", "date": "2026-08-18", "status": "now", "note": "first version received, in review"},
 {"name": "Phase-1 scope confirmed", "date": "in progress", "status": "next", "note": ""},
 {"name": "Phase-1 build kickoff", "date": "upcoming", "status": "later", "note": ""},
 {"name": "Phase-1 MVP", "date": "target late Aug 2026", "status": "later", "note": ""},
]
CLIENT_UPDATES = [
 "Completed the full design walkthrough and agreed the product direction.",
 "Locked nine core product decisions covering sign-up, age gating, location, privacy, and phase-1 scope.",
 "Set up a shared coordination repo and workflow so status stays in one place.",
 "Received the first project documentation; it is in review.",
]
CLIENT_SCOPE = [
 {"area": "Waitlist (non-invited signups)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Onboarding (invited flow)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Registration and sign-up (phone verification, age check)", "phase": "1", "designed": "draft", "built": "no", "note": "age check pending legal review"},
 {"area": "Login", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Ideas (polls, discussion)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Events (create, discussion, media, chat)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Explore (map, list, filters, search)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Home (recommendations)", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Event and group chat", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Notifications", "phase": "1", "designed": "draft", "built": "no", "note": ""},
 {"area": "Profiles (user and organization, moments)", "phase": "1", "designed": "partial", "built": "no", "note": "screens in progress"},
 {"area": "Moments and reflections", "phase": "1", "designed": "draft", "built": "no", "note": "in review"},
 {"area": "Calendar", "phase": "later", "designed": "draft", "built": "no", "note": "planned for a later phase"},
 {"area": "Direct messages and user-created group chats", "phase": "later", "designed": "draft", "built": "no", "note": "planned for a later phase"},
 {"area": "Ratings and reviews", "phase": "contested", "designed": "draft", "built": "no", "note": "under review"},
 {"area": "In-app AI image or video generation", "phase": "excluded", "designed": "na", "built": "na", "note": "not planned"},
]


def parse_board(path):
    tasks, asof = [], ""
    for line in open(path, encoding="utf-8"):
        if line.startswith("**As of:**"):
            asof = line.split("**As of:**", 1)[1].strip()
        if line.startswith("| TASK-"):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            tasks.append(dict(id=c[0], task=c[1], owner=c[2], status=c[3],
                              started=c[4], ended=c[5], committed=c[6], notes=c[7]))
    return tasks, asof


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_internal(tasks, asof):
    data = json.dumps({"tasks": tasks, "horizon": HORIZON, "milestones": MILESTONES, "scope": SCOPE})
    shell = open(INT_TEMPLATE, encoding="utf-8").read()
    return shell.replace("__ASOF__", asof or "").replace("__DATA__", data)


def render_public(asof):
    done = sum(1 for m in CLIENT_MILESTONES if m["status"] == "done")
    total = len(CLIENT_MILESTONES)
    pct = round(done / total * 100)

    def mrow(m):
        note = (" &middot; " + esc(m["note"])) if m["note"] else ""
        return ('<div class="tlrow %s"><span class="node"></span><div class="tlname">%s</div>'
                '<div class="tlmeta"><span class="when">%s</span>%s</div></div>'
                % (m["status"], esc(m["name"]), esc(m["date"]), note))

    def srow(s):
        desL = {"draft": "Designed (draft)", "partial": "Design in progress", "done": "Designed",
                "na": "n/a", "no": "Not started"}.get(s["designed"], "Not started")
        desC = "chip des" + (" no" if s["designed"] == "no" else " done" if s["designed"] == "done" else "")
        bltL = {"no": "Not built", "na": "n/a", "done": "Built"}.get(s["built"], "In build")
        bltC = "chip blt" + (" yes" if s["built"] == "done" else "")
        note = ('<div class="sn">%s</div>' % esc(s["note"])) if s["note"] else ""
        return ('<div class="srow"><div class="sarea">%s%s</div><span class="%s">%s</span>'
                '<span class="%s">%s</span></div>' % (esc(s["area"]), note, desC, desL, bltC, bltL))

    def sgrp(label, ph):
        items = [s for s in CLIENT_SCOPE if s["phase"] == ph]
        if not items:
            return ""
        return '<div class="grp"><div class="grph">%s</div>%s</div>' % (label, "".join(srow(s) for s in items))

    overview = (
        '<div class="card">'
        '<div class="health"><span class="hbadge">%s</span><span class="hmsg">%s</span></div>'
        '<div class="prog"><div class="pbar"><div class="pfill" style="width:%d%%"></div></div>'
        '<div class="pmeta"><span>%d of %d milestones complete</span><span>%d%%</span></div></div>'
        '<div class="sect"><div class="slab">Recent updates</div>%s</div>'
        '</div>' % (esc(CLIENT_HEALTH[0]), esc(CLIENT_HEALTH[1]), pct, done, total, pct,
                    "".join('<div class="uli">%s</div>' % esc(u) for u in CLIENT_UPDATES)))
    timeline = '<div class="card tl">%s</div>' % "".join(mrow(m) for m in CLIENT_MILESTONES)
    scope = ('<div class="note">Scope reflects the agreed phase-1 boundary and the current design. '
             'Design and build status update as work progresses.</div>'
             + sgrp("Phase 1", "1") + sgrp("Later phases", "later")
             + sgrp("Under review", "contested") + sgrp("Not planned", "excluded"))

    return PUB_TEMPLATE.replace("__ASOF__", esc(asof or "")).replace(
        "__OVERVIEW__", overview).replace("__TIMELINE__", timeline).replace("__SCOPE__", scope)


def main():
    import datetime
    tasks, asof = parse_board(BOARD)
    asof = asof or datetime.date.today().isoformat()
    with open(INT_OUT, "w", encoding="utf-8") as f:
        f.write(render_internal(tasks, asof))
    with open(PUB_OUT, "w", encoding="utf-8") as f:
        f.write(render_public(asof))
    print("wrote", INT_OUT, "and", PUB_OUT)


PUB_TEMPLATE = r'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wepop - Delivery Status</title>
<style>
:root{--plane:#f7f7f4;--surface:#fff;--ink:#12120f;--ink2:#55534d;--muted:#93908a;--line:#e9e8e2;
--accent:#2a6df4;--accentbg:#eaf1fe;--done:#1f9d55;--donebg:#e7f5ec;--now:#2a6df4;--nowbg:#eaf1fe;
--next:#6b7280;--later:#93908a;--todobg:#f0f0ee;--shadow:0 1px 2px rgba(18,18,15,.05);}
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--plane);color:var(--ink);font:15px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
.container{width:100%;margin-inline:auto;padding-inline:1rem}
@media(min-width:576px){.container{max-width:540px}}@media(min-width:768px){.container{max-width:720px}}
@media(min-width:992px){.container{max-width:900px}}
.pagepad{padding-top:30px;padding-bottom:70px}
.brand{font-size:12px;font-weight:650;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.h1{font-size:24px;font-weight:680;letter-spacing:-.01em;margin:4px 0 0}
.hsub{color:var(--ink2);font-size:13.5px;margin:4px 0 0}
.tabs{display:flex;gap:5px;flex-wrap:wrap;margin:20px 0 22px;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:6px;box-shadow:var(--shadow)}
.tab{border:none;background:transparent;color:var(--ink2);font:inherit;font-size:13.5px;font-weight:560;padding:8px 16px;border-radius:8px;cursor:pointer}
.tab:hover{color:var(--ink)}.tab.on{background:var(--accentbg);color:var(--accent)}
.view{display:none}.view.on{display:block}
.card{background:var(--surface);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow)}
.health{padding:20px 24px;display:flex;align-items:center;gap:15px;border-bottom:1px solid var(--line)}
.hbadge{font-size:12.5px;font-weight:650;color:var(--done);background:var(--donebg);border-radius:999px;padding:5px 13px;white-space:nowrap}
.hmsg{color:var(--ink2);font-size:14px}
.prog{padding:18px 24px;border-bottom:1px solid var(--line)}
.pbar{height:10px;border-radius:999px;background:var(--todobg);overflow:hidden}.pfill{height:100%;background:var(--done);border-radius:999px}
.pmeta{display:flex;justify-content:space-between;margin-top:9px;font-size:13px;color:var(--ink2)}
.sect{padding:18px 24px}
.slab{font-size:12px;font-weight:660;text-transform:uppercase;letter-spacing:.05em;color:var(--ink2);margin-bottom:12px}
.uli{padding:8px 0 8px 20px;position:relative;font-size:14.5px;border-bottom:1px solid var(--line)}
.uli:last-child{border-bottom:none}.uli::before{content:"";position:absolute;left:2px;top:15px;width:7px;height:7px;border-radius:50%;background:var(--done)}
.tl{padding:10px 26px 20px}
.tlrow{position:relative;padding:15px 0 15px 28px}
.tlrow::before{content:"";position:absolute;left:6px;top:22px;bottom:-8px;width:2px;background:var(--line)}
.tlrow:last-child::before{display:none}
.node{position:absolute;left:0;top:16px;width:14px;height:14px;border-radius:50%;background:var(--surface);border:2px solid var(--line)}
.tlrow.done .node{background:var(--done);border-color:var(--done)}
.tlrow.now .node,.tlrow.next .node{background:var(--surface);border-color:var(--now);box-shadow:0 0 0 3px var(--nowbg)}
.tlname{font-size:15px;font-weight:560}.tlmeta{font-size:13px;color:var(--muted);margin-top:2px}.tlmeta .when{color:var(--ink2);font-weight:560}
.note{background:#fdf6e3;border:1px solid #f0e2b8;color:#6b5a1a;border-radius:10px;padding:13px 16px;font-size:13px;margin-bottom:18px}
.grp{margin-bottom:20px}.grph{font-size:12px;font-weight:660;text-transform:uppercase;letter-spacing:.05em;color:var(--ink2);margin:0 2px 10px}
.srow{display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:13px 16px;margin-bottom:9px;box-shadow:var(--shadow)}
.sarea{flex:1;font-size:14.5px}.sarea .sn{font-size:12px;color:var(--muted);margin-top:3px}
.chip{font-size:11px;font-weight:600;border-radius:999px;padding:3px 10px;white-space:nowrap}
.chip.des{color:var(--now);background:var(--nowbg)}.chip.des.no{color:var(--muted);background:var(--todobg)}.chip.des.done{color:var(--done);background:var(--donebg)}
.chip.blt{color:var(--muted);background:var(--todobg)}.chip.blt.yes{color:var(--done);background:var(--donebg)}
.foot{margin-top:30px;color:var(--muted);font-size:12px}
</style></head>
<body><div class="container pagepad">
<div class="brand">BetaCraft &middot; delivery status</div>
<div class="h1">Wepop</div>
<div class="hsub">WEP001 &middot; as of __ASOF__</div>
<div class="tabs" id="tabs">
<button class="tab on" data-v="ov">Overview</button>
<button class="tab" data-v="tl">Timeline</button>
<button class="tab" data-v="sc">Scope</button>
</div>
<div class="view on" id="v-ov">__OVERVIEW__</div>
<div class="view" id="v-tl">__TIMELINE__</div>
<div class="view" id="v-sc">__SCOPE__</div>
<div class="foot">Prepared by BetaCraft for Wepop. Status updates as work progresses.</div>
</div>
<script>
document.querySelectorAll(".tab").forEach(function(b){b.addEventListener("click",function(){
var v=b.getAttribute("data-v");
document.querySelectorAll(".tab").forEach(function(x){x.classList.toggle("on",x===b);});
document.querySelectorAll(".view").forEach(function(x){x.classList.toggle("on",x.id==="v-"+v);});
});});
</script></body></html>'''

if __name__ == "__main__":
    main()
