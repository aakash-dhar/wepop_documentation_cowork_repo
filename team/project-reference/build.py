#!/usr/bin/env python3
"""Build the Wepop project reference page from template.html + data.js.

  python3 team/project-reference/build.py
      -> writes team/wepop-project-reference.html (internal, plaintext)

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

def validate(data_js):
    if "—" in data_js: fail("em-dash found in data.js (house rule: hyphens only)")
    m = re.search(r"^const ELVIS = (\{.*\});$", data_js, flags=re.M)
    if not m: fail("could not find the single-line 'const ELVIS = {...};' in data.js")
    elvis = json.loads(m.group(1))
    missing = [(mod, i) for mod, items in elvis["modules"].items() for i, it in enumerate(items) if not it.get("src")]
    for n in elvis.get("new", []):
        for k in ("flow", "rules", "build", "open"):
            for i, it in enumerate(n.get(k, [])):
                if not it.get("src"): missing.append((n.get("title", "?") + "/" + k, i))
    if missing: fail("ELVIS items without a src: " + ", ".join(f"{a}[{b}]" for a, b in missing[:20]))
    decided = len(re.findall(r'^\{id:"M\d\d"', data_js, flags=re.M))
    sourced = sum(len(v) for v in elvis["modules"].values())
    print(f"data.js ok: {decided} decided modules, {len(elvis.get('new', []))} Elvis-designed modules, {sourced} sourced items, all with src")

def build():
    tpl = open(TEMPLATE, encoding="utf-8").read()
    data = open(DATA, encoding="utf-8").read()
    validate(data)
    if "/*__DATA__*/" not in tpl: fail("template.html has no /*__DATA__*/ marker")
    decs, index = parse_decisions()
    gen = ("/* generated at build time from shared/DECISIONS.md */\nconst DECFULL = " + json.dumps(decs, ensure_ascii=False)
           + ";\nconst DECS = " + json.dumps(index, ensure_ascii=False) + ";\n")
    print(f"decisions: {len(decs)} parsed from shared/DECISIONS.md ({sum(1 for i in index if len(i)==3)} superseded)")
    html = tpl.replace("/*__DATA__*/", data + gen, 1)
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
