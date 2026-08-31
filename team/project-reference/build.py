#!/usr/bin/env python3
"""Build the Wepop project reference page from template.html + data.js.

  python3 team/project-reference/build.py
      -> writes team/wepop-project-reference.html (internal, plaintext)
         and architecture/phase-plan/wepop-project-reference.md (the Markdown rendition, Mermaid diagrams)

  python3 team/project-reference/build.py --lock --user U --password 'P' [--salt HEX]
      -> also publishes the client copies behind ONE login gate (same salt for all):
         docs/project-reference.html          (from the built reference)
         docs/index.html, docs/board-public.html (from team/board.html, the rendered board)
      Run team/board-render.py first if the board data changed. Never commits; the human pushes.

DECS and DECFULL (the decision index and the full records) are generated from shared/DECISIONS.md on every build.
Checks before writing: no em-dashes anywhere; every ELVIS item carries a src; module counts printed.
"""
import argparse, importlib.util, json, os, re, secrets, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TEMPLATE = os.path.join(HERE, "template.html")
DATA = os.path.join(HERE, "data.js")
OUT_INTERNAL = os.path.join(ROOT, "team", "wepop-project-reference.html")
OUT_CLIENT = os.path.join(ROOT, "docs", "project-reference.html")
BOARD_SRC = os.path.join(ROOT, "team", "board.html")
BOARD_OUTS = [os.path.join(ROOT, "docs", "index.html"), os.path.join(ROOT, "docs", "board-public.html")]
LOCK = os.path.join(ROOT, "team", "board-lock.py")
DECISIONS = os.path.join(ROOT, "shared", "DECISIONS.md")

def parse_decisions():
    """Verbatim decision records from shared/DECISIONS.md (the source of truth). Never hand-maintained."""
    src = open(DECISIONS, encoding="utf-8").read()
    body = src.split("\n## Decisions\n", 1)[1]
    decs = {}
    for e in re.split(r"\n(?=### DEC-\d{3}: )", body):
        m = re.match(r"### (DEC-\d{3}): (.+)\n", e)
        if not m: continue
        did, title = m.group(1), m.group(2).strip()
        blocks = re.findall(r"^\*\*([^*]+?):\*\*\s*(.*?)(?=\n\*\*[^*]+?:\*\*|\Z)", e[m.end():], flags=re.S | re.M)
        fields = [[lab.strip(), " ".join(txt.split())] for lab, txt in blocks]
        d = {"id": did, "title": title, "fields": fields}
        for lab, txt in fields:
            if lab == "Date": d["date"] = txt
            if lab == "Status": d["status"] = txt
            if lab == "Participants": d["participants"] = txt
            if lab == "Decision" and "decision" not in d: d["decision"] = txt
        if "decision" not in d or "status" not in d: fail(f"{did} in DECISIONS.md has no Decision or Status field")
        decs[did] = d
    if not decs: fail("no decisions parsed from shared/DECISIONS.md")
    index = [[k, v["title"]] + (["sup"] if "SUPERSEDED" in v["status"].upper() else []) for k, v in sorted(decs.items())]
    return decs, index

def fail(msg):
    print("BUILD FAILED:", msg); sys.exit(1)

def load_data(data_js):
    """Every constant in data.js is a JSON literal on one line: const NAME = {...};"""
    out = {}
    for m in re.finditer(r"^const ([A-Z]+) = (.*);$", data_js, flags=re.M):
        try: out[m.group(1)] = json.loads(m.group(2))
        except json.JSONDecodeError as e: fail(f"data.js constant {m.group(1)} is not valid JSON: {e}")
    for k in ("META","M","ELVIS","PLAIN","FLOWS","RISKS","OPEN","LEGAL","GOV","PRINCIPLES","DATAMODEL","GLOSS"):
        if k not in out: fail(f"data.js is missing const {k}")
    return out

def validate(data_js):
    if "\u2014" in data_js: fail("em-dash found in data.js (house rule: hyphens only)")
    d = load_data(data_js)
    elvis = d["ELVIS"]
    missing = [(mod, i) for mod, items in elvis["modules"].items() for i, it in enumerate(items) if not it.get("src")]
    for n in elvis.get("new", []):
        for k in ("flow", "rules", "build", "open"):
            for i, it in enumerate(n.get(k, [])):
                if not it.get("src"): missing.append((n.get("title", "?") + "/" + k, i))
    if missing: fail("ELVIS items without a src: " + ", ".join(f"{a}[{b}]" for a, b in missing[:20]))
    sourced = sum(len(v) for v in elvis["modules"].values())
    print(f"data.js ok: {len(d['M'])} decided modules, {len(elvis.get('new', []))} Elvis-designed modules, {sourced} sourced items, all with src, {len(d['FLOWS'])} diagrams")
    return d


OUT_MD = os.path.join(ROOT, "architecture", "phase-plan", "wepop-project-reference.md")

def mermaid(key, spec):
    """FLOWS spec -> Mermaid flowchart (GitHub renders it). Node shapes by type."""
    shape = {"start": ("([", "])"), "end": ("([", "])"), "decision": ("{{", "}}"), "system": ("[[", "]]"), "warn": ("[/", "/]"), "muted": ("[", "]"), "box": ("[", "]")}
    q = lambda s: s.replace('"', "'")
    lines = ["flowchart LR"]
    for ci, col in enumerate(spec["cols"]):
        lane = col.get("lane")
        if lane: lines.append(f'  subgraph {key}L{ci}["{q(lane)}"]'); lines.append("    direction TB")
        for n in col["nodes"]:
            l, r = shape.get(n.get("type", "box"), shape["box"])
            lines.append(f'  {"  " if lane else ""}{key}_{n["id"]}{l}"{q(n["label"])}"{r}')
        if lane: lines.append("  end")
    for e in spec.get("edges", []):
        arrow = "-.->" if (len(e) > 3 and e[3] == "dashed") else "-->"
        lbl = f'|"{q(e[2])}"|' if len(e) > 2 and e[2] else ""
        lines.append(f'  {key}_{e[0]} {arrow}{lbl} {key}_{e[1]}')
    # light BetaCraft styling
    lines.append("  classDef start fill:#fef2f2,stroke:#E63946,color:#17181d;")
    lines.append("  classDef fin fill:#e8f6ee,stroke:#1f9d55,color:#0f3d24;")
    lines.append("  classDef decision fill:#fdf3df,stroke:#d9a441,color:#4a3a10;")
    lines.append("  classDef system fill:#eef2fd,stroke:#7f9fe6,color:#1e3f8f;")
    lines.append("  classDef warn fill:#fff5f5,stroke:#C42E3A,color:#7a1f28;")
    lines.append("  classDef muted fill:#f2f2f4,stroke:#d5d6db,color:#6b6b70;")
    for col in spec["cols"]:
        for n in col["nodes"]:
            t = n.get("type", "box")
            if t != "box": lines.append(f'  class {key}_{n["id"]} {"fin" if t=="end" else t};')
    out = "```mermaid\n" + "\n".join(lines) + "\n```"
    if spec.get("note"): out += f"\n\n_{spec['note']}_"
    return out

def strip_html(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")

def write_markdown(d, decs, index):
    meta, M, E, P, F = d["META"], d["M"], d["ELVIS"], d["PLAIN"], d["FLOWS"]
    L = []
    w = L.append
    w("# Wepop - Complete Project Reference (WEP001)\n")
    w(f"> Generated {meta['asOf']} by `team/project-reference/build.py` from `team/project-reference/data.js` and `shared/DECISIONS.md` (DEC-001 to {meta['lastDec']}). Do not edit by hand: it is overwritten on every build. The interactive version is `docs/project-reference.html` (client, behind the login gate) and `team/wepop-project-reference.html` (internal).")
    w("> `shared/DECISIONS.md` is the source of truth and wins wherever anything here disagrees. Items marked **Elvis design** come from Elvis's own documents and have not landed as decisions; anything that conflicts with a landed decision is flagged, never treated as scope. Every sourced item names its file and section. No em-dashes; governance values are ALLOW / BLOCK / ESCALATE.\n")
    w("## Contents\n")
    w("1. What Wepop is  \n2. Core objects  \n3. Phase plan  \n4. The modules (24 decided, then 7 Elvis-designed)  \n5. Cross-cutting principles and invariants  \n6. Data-model notes  \n7. Legal, privacy and compliance  \n8. Risk register  \n9. Open items  \n10. Governance  \n11. Decision index and records  \n12. Glossary\n")
    w("---\n\n## 1. What Wepop is\n")
    w("Wepop is an **invite-first, location-based events and meetup app**: a tool for getting people together in the real world around shared activities. It is deliberately a meetup app, **not a dating app**, and much of the product design exists to hold that line (the anti-stalking visibility model, attendee-list gating, the no-paid-boost rule). Focus launch markets are **Korea and the US**. It is being **rebuilt on top of an existing Wepop codebase**, salvaged and extended with AI-assisted build (DEC-008).\n")
    w("- **Invite-first.** New users arrive through an invitation to a specific event or host, or wait on a waitlist that auto-promotes; both a growth model and a real safety mitigation cited in the age-gate reasoning (DEC-012, DEC-024).\n- **Real-world-first.** The app pushes people toward attending, hosting and remembering real events rather than browsing people (DEC-006, DEC-020).\n")
    w(f"**Status ({meta['asOf']}).** {meta['statusLine']} Three launch blockers are open on the HOTSHEET: moderation capability, Korea 위치정보법 KCC registration for the geofenced check-in mode, and the CSAM preserve-and-report runbook.\n")
    w("### The journey, end to end\n\n" + mermaid("ov", F["overview"]) + "\n")
    w("---\n\n## 2. Core objects\n")
    w("Everything in the app hangs off five objects.\n")
    w("- **Event** - a concrete activity at a place and time, with details, a Discussion board, media and chat. Standalone, one occurrence of a recurring group, or a member of one or more Series. Has a seven-status lifecycle (handoff spec section 3) including planning, live, completed and deleted, with a 60-day expiry for a planning event that never gets a date, and becomes largely immutable once completed to protect its rating record (DEC-021, DEC-022, DEC-043). \"Plan\" is not a separate object: `planning` is the Event stage where the date or time is still under poll (Elvis's earlier documents call this Plan Mode).\n- **Idea** - something a user wants to do but is not hosting. Others rally around it (Interested, Discussion, time/place polls) and can spin a real Event out of it. No fixed date; behaves like a subreddit for a topic, with its own lifecycle (DEC-009, DEC-040). No media upload on Ideas.\n- **Event Series** - a host-created thematic hub page, not itself joinable, with events attached over time and a locked add-permission. Phase 1.5 (DEC-022).\n- **User profile** - birthdate, neighborhood, gender, languages, personality and interest tags, university, followers, created events/ideas, saved items and moments. Public in phase 1 (DEC-005, DEC-015).\n- **Business / Organization profile** - a multi-member account; university clubs first. Ownership transfers as officers turn over, and enforcement propagates from a user to the orgs they operate (DEC-024, DEC-044).\n")
    w("---\n\n## 3. Phase plan\n")
    w("**Phase 1:** core objects; waitlist auto-promote; social login + phone with the Korea PASS branch; age gate + country cascade; neighborhood home location + map picker; Events and the Ideas lifecycle; event schedule; ratings + feedback (check-in as a badge); Moments with video; live stories; DMs + group chat (text); busy-time ingestion + add-to-calendar; cohorts + recommendation; Free Now; icebreakers and tips; general user blocking; change notifications; host accountability; Korean localization; A/B testing (proposed, phase unconfirmed). Payment provisions built but gated off.\n\n**Phase 1.5:** payments go live (ticketing + fee); individual premium tier (held); full in-app calendar; recurring events; Event Series; co-hosts.\n\n**Later:** Sunday Deck; apply-to-join; annual Wrapped; memories resurfacing; private accounts (per DEC-015; see module 4.30); learned per-user weights; look-alike host affinity; gamification / ads / marketplace / web.\n")
    w("---\n\n## 4. The modules\n")
    w("Each module: a plain-language explainer, what it is, the user flow, the rules, build notes for Deepak, open items, the governing decisions, and Elvis's sourced design detail (tagged **Decided** when backed by a DEC, **Elvis design** when in his file but not yet a decision, **Superseded** for what an earlier draft said before a DEC changed it).\n")
    tagname = lambda t: t
    def module_block(m, elvis_items, raw=None):
        w(f"### {m['num']} {m['t']}\n")
        ph = {"1":"Phase 1","1.5":"Phase 1.5","later":"Later"}.get(m.get("ph",""), "Phase unstated")
        tags = ", ".join(x for x in m.get("tags",[]) if x!="elvis")
        w(f"**{ph}** · {m['area']}" + (f" · {tags}" if tags else "") + (f" · **Elvis design, no DEC yet**" if raw else "") + (" · **Conflicts with a landed DEC**" if m.get("conflict") else "") + "\n")
        if P.get(m["id"]): w(f"> **In plain terms.** {P[m['id']]}\n")
        if F.get(m["id"]): w(mermaid(m["id"], F[m["id"]]) + "\n")
        w(f"**What it is.** {m['sum']}\n")
        w("**User flow.**\n\n" + "\n".join(f"{i+1}. {x}" for i,x in enumerate(m["flow"])) + "\n")
        if m["rules"]: w("**Rules that govern it.**\n\n" + "\n".join(f"- {x}" for x in m["rules"]) + "\n")
        if m["build"]: w("**Build notes for Deepak.**\n\n" + "\n".join(f"- {x}" for x in m["build"]) + "\n")
        w("**Open items.**\n\n" + ("\n".join(f"- {x}" for x in m["open"]) if m["open"] else "- None on this module.") + "\n")
        if raw:
            w(f"**Status, in Elvis's file.** {raw['status']}" + (f" Phase, as stated: {raw['phase']}." if raw.get("phase") else "") + "\n")
            w("**Sources per line.**\n")
            for k in ("flow","rules","build","open"):
                for it in raw.get(k, []):
                    w(f"- ({k}) {it['text']}  \n  src: `{it['src']}`")
            w("")
        else:
            w("**Governing decisions.** " + ", ".join(x.split(":")[0] + (" (superseded)" if x.endswith(":sup") else "") for x in m["decs"]) + "\n")
            if elvis_items:
                w(f"**Elvis's design detail, sourced ({len(elvis_items)}).**\n")
                for it in elvis_items:
                    w(f"- **[{it['tag']}]** {it['text']}  \n  src: `{it['src']}`")
                w("")
    for m in M:
        module_block(m, E["modules"].get(m["id"], []))
    w("### Elvis-designed modules, not yet decisions\n\nThe modules below come from design documents Elvis wrote in his workspace. Each is grounded only in his file and carries its source on every line. None has landed as a DEC; where one conflicts with a landed decision it is flagged rather than treated as scope.\n")
    for i, n in enumerate(E.get("new", [])):
        mid = f"M{25+i}"
        ph = n.get("phase","") or ""
        phk = "1.5" if "1.5" in ph else ("1" if re.match(r"^1\b", ph.strip()) else ("later" if "later" in ph.lower() else ""))
        summ = n["summary"].split(" | src: ")[0]
        m = {"id":mid,"num":f"4.{25+i}","t":n["title"],"area":"Elvis design","ph":phk,"tags":[],"sum":summ,"flow":[x["text"] for x in n["flow"]],"rules":[x["text"] for x in n["rules"]],"build":[x["text"] for x in n["build"]],"open":[x["text"] for x in n["open"]],"decs":[],"conflict":"conflict" in n["status"].lower()}
        module_block(m, [], raw=n)
    w("---\n\n## 5. Cross-cutting principles and invariants\n")
    for p in d["PRINCIPLES"]: w(f"- **{p[0]}.** {p[1]} ({p[2]})")
    w("\n---\n\n## 6. Data-model notes\n")
    for x in d["DATAMODEL"]: w(f"- {strip_html(x)}")
    w("\n---\n\n## 7. Legal, privacy and compliance\n")
    for l in d["LEGAL"]: w(f"- **{l[1]}.** {l[2]}")
    w("\n---\n\n## 8. Risk register\n")
    for r in d["RISKS"]: w(f"- **{r[0]} - {r[1]}** ({r[3]}, owner {r[4]}, ACTIVE). {r[2]}")
    w("\n---\n\n## 9. Open items and decisions still pending\n")
    for x in d["OPEN"]: w(f"- {strip_html(x)}")
    w("\n---\n\n## 10. Governance: how the record works\n")
    for g in d["GOV"]: w(f"- **{g[0]}.** {g[1]}")
    w("\n### How a change travels through the record\n\n" + mermaid("gov", F["governance"]) + "\n")
    w("---\n\n## 11. Decision index and records\n")
    w("Verbatim from `shared/DECISIONS.md`. Superseded decisions are never deleted; they keep a pointer to their replacement.\n")
    for k, title, *sup in index:
        f = decs[k]
        w(f"### {k}: {title}" + (" (SUPERSEDED)" if sup else ""))
        w(f"**Date:** {f.get('date','')} · **Status:** {f.get('status','')} · **Participants:** {f.get('participants','')}\n")
        for lab, txt in f["fields"]:
            if lab in ("Date","Status","Participants"): continue
            w(f"**{lab}:** {txt}\n")
    w("---\n\n## 12. Glossary of Korean terms\n")
    for g in d["GLOSS"]: w(f"- **{g[0]}** - {g[1]}")
    w(f"\n---\n\n_Generated {meta['asOf']}. When this document and shared/DECISIONS.md disagree, DECISIONS.md wins._\n")
    text = "\n".join(L)
    if "—" in text: fail("em-dash found in generated markdown")
    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    open(OUT_MD, "w", encoding="utf-8").write(text)
    print("wrote markdown reference:", os.path.relpath(OUT_MD, ROOT), f"({len(text.splitlines())} lines)")

def build():
    tpl = open(TEMPLATE, encoding="utf-8").read()
    data = open(DATA, encoding="utf-8").read()
    d = validate(data)
    if "/*__DATA__*/" not in tpl: fail("template.html has no /*__DATA__*/ marker")
    decs, index = parse_decisions()
    gen = ("/* generated at build time from shared/DECISIONS.md */\nconst DECFULL = " + json.dumps(decs, ensure_ascii=False)
           + ";\nconst DECS = " + json.dumps(index, ensure_ascii=False) + ";\n")
    print(f"decisions: {len(decs)} parsed from shared/DECISIONS.md ({sum(1 for i in index if len(i)==3)} superseded)")
    html = tpl.replace("/*__DATA__*/", data + gen, 1)
    write_markdown(d, decs, index)
    if "—" in html: fail("em-dash found in built page")
    os.makedirs(os.path.dirname(OUT_INTERNAL), exist_ok=True)
    open(OUT_INTERNAL, "w", encoding="utf-8").write(html)
    print("wrote internal copy:", os.path.relpath(OUT_INTERNAL, ROOT))
    return html

def lock(html, user, password, salt):
    spec = importlib.util.spec_from_file_location("board_lock", LOCK)
    bl = importlib.util.module_from_spec(spec); spec.loader.exec_module(bl)
    salt = salt or secrets.token_hex(8)
    os.makedirs(os.path.dirname(OUT_CLIENT), exist_ok=True)
    open(OUT_CLIENT, "w", encoding="utf-8").write(bl.gate_html(html, user, password, salt))
    print("wrote gated client copy:", os.path.relpath(OUT_CLIENT, ROOT))
    if os.path.exists(BOARD_SRC):
        board = open(BOARD_SRC, encoding="utf-8").read()
        gated = bl.gate_html(board, user, password, salt)
        for out in BOARD_OUTS:
            open(out, "w", encoding="utf-8").write(gated)
            print("re-gated board:", os.path.relpath(out, ROOT))
    else:
        print("note: team/board.html not found, board not re-gated")
    print("salt used for all gated pages (one login unlocks all):", salt)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Build (and optionally publish behind the login gate) the Wepop project reference.")
    ap.add_argument("--lock", action="store_true", help="also write the gated client copies under docs/")
    ap.add_argument("--user"); ap.add_argument("--password"); ap.add_argument("--salt")
    a = ap.parse_args()
    html = build()
    if a.lock:
        if not (a.user and a.password): fail("--lock needs --user and --password")
        lock(html, a.user, a.password, a.salt)
    else:
        print("reminder: docs/ copies not touched. Run with --lock --user --password to publish behind the gate.")
