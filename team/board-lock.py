#!/usr/bin/env python3
"""
board-lock.py - wrap a rendered Wepop board HTML page with a simple
username / password login gate.

This is a POST-RENDER step. board-render.py produces the plaintext board;
run this afterwards to produce the gated copies that get published to
GitHub Pages (docs/index.html, docs/board-public.html).

The credential is never stored in plaintext in the page. We store a random
salt plus the SHA-256 hash of  salt + username + ":" + password. The browser
hashes what the visitor types and compares.

Honest limits (by design, for a public repo + static host):
  - This is a deterrent, not real security. The board's data is still present
    in the page source, and the same data is readable in the public repo.
  - For true protection, make the repo private and/or encrypt the page.

Usage:
  python3 board-lock.py --in team/board.html --out docs/index.html \
      --user wepop --password 'your-shared-password'

  # gate several outputs with one credential:
  python3 board-lock.py --in team/board.html \
      --out docs/index.html --out docs/board-public.html \
      --user wepop --password 'your-shared-password'
"""
import argparse
import hashlib
import os
import re
import secrets

MARKER = "<!--wp-login-gate-->"

GATE_TEMPLATE = """{marker}
<style>
#wp-gate{{position:fixed;inset:0;z-index:999999;display:flex;align-items:center;
 justify-content:center;background:#f6f6f3;
 font:15px/1.6 "Inter",system-ui,-apple-system,"Segoe UI",sans-serif;color:#12120f}}
#wp-gate .wp-card{{width:100%;max-width:360px;margin:1rem;background:#fff;
 border:1px solid #e9e8e2;border-radius:14px;padding:28px 26px;
 box-shadow:0 8px 26px rgba(18,18,15,.10)}}
#wp-gate .wp-badge{{display:inline-block;font-weight:700;letter-spacing:.02em;
 color:#c92f3c;background:#fdecee;border-radius:8px;padding:4px 10px;font-size:13px}}
#wp-gate h1{{font:600 20px/1.3 "Space Grotesk","Inter",sans-serif;margin:16px 0 4px}}
#wp-gate p.sub{{margin:0 0 18px;color:#55534d;font-size:13.5px}}
#wp-gate label{{display:block;font-size:12.5px;font-weight:600;color:#55534d;
 margin:0 0 5px}}
#wp-gate input{{width:100%;padding:10px 12px;margin:0 0 14px;border:1px solid #e9e8e2;
 border-radius:9px;font-size:15px;background:#fff;color:#12120f}}
#wp-gate input:focus{{outline:none;border-color:#e63946;box-shadow:0 0 0 3px rgba(230,57,70,.12)}}
#wp-gate button{{width:100%;padding:11px 12px;border:0;border-radius:9px;
 background:#e63946;color:#fff;font-size:15px;font-weight:600;cursor:pointer}}
#wp-gate button:hover{{background:#c92f3c}}
#wp-gate .wp-err{{display:none;margin:0 0 12px;color:#c92f3c;font-size:13px;font-weight:600}}
#wp-gate .wp-note{{margin:16px 0 0;color:#93908a;font-size:11.5px;line-height:1.5}}
</style>
<div id="wp-gate" role="dialog" aria-modal="true" aria-label="Sign in to view the board">
  <div class="wp-card">
    <span class="wp-badge">Wepop</span>
    <h1>Delivery board</h1>
    <p class="sub">This board is private to the team. Please sign in.</p>
    <form id="wp-form" autocomplete="off">
      <div class="wp-err" id="wp-err">Wrong username or password.</div>
      <label for="wp-user">Username</label>
      <input id="wp-user" type="text" autocomplete="username" autocapitalize="none"
             spellcheck="false" required>
      <label for="wp-pass">Password</label>
      <input id="wp-pass" type="password" autocomplete="current-password" required>
      <button type="submit">Sign in</button>
    </form>
    <p class="wp-note">Shared team access. Do not circulate this link outside the team.</p>
  </div>
</div>
<script>
(function(){{
  var SALT={salt!r};
  var HASH={hash!r};
  var KEY="wp_board_auth";
  function reveal(){{
    var g=document.getElementById("wp-gate");
    if(g&&g.parentNode)g.parentNode.removeChild(g);
    document.documentElement.style.overflow="";
  }}
  try{{ if(sessionStorage.getItem(KEY)===HASH){{ reveal(); return; }} }}catch(e){{}}
  document.documentElement.style.overflow="hidden";
  function toHex(buf){{return Array.prototype.map.call(new Uint8Array(buf),
    function(b){{return("0"+b.toString(16)).slice(-2);}}).join("");}}
  function sha256(str){{
    var data=new TextEncoder().encode(str);
    return crypto.subtle.digest("SHA-256",data).then(toHex);
  }}
  function wire(){{
    var form=document.getElementById("wp-form");
    var err=document.getElementById("wp-err");
    if(!form)return;
    form.addEventListener("submit",function(e){{
      e.preventDefault();
      var u=document.getElementById("wp-user").value.trim();
      var p=document.getElementById("wp-pass").value;
      sha256(SALT+u+":"+p).then(function(got){{
        if(got===HASH){{
          try{{sessionStorage.setItem(KEY,HASH);}}catch(e){{}}
          reveal();
        }}else{{
          err.style.display="block";
          document.getElementById("wp-pass").value="";
        }}
      }});
    }});
    document.getElementById("wp-user").focus();
  }}
  if(document.readyState==="loading")
    document.addEventListener("DOMContentLoaded",wire);
  else wire();
}})();
</script>
"""


def gate_html(html: str, user: str, password: str, salt: str = None) -> str:
    if MARKER in html:
        # strip any previous gate block so re-running is idempotent
        html = re.sub(re.escape(MARKER) + r".*?</script>\s*",
                      "", html, count=1, flags=re.DOTALL)
    salt = salt or secrets.token_hex(8)
    digest = hashlib.sha256((salt + user + ":" + password).encode("utf-8")).hexdigest()
    block = GATE_TEMPLATE.format(marker=MARKER, salt=salt, hash=digest)
    m = re.search(r"<body[^>]*>", html, flags=re.IGNORECASE)
    if not m:
        raise SystemExit("No <body> tag found in input HTML.")
    idx = m.end()
    return html[:idx] + "\n" + block + html[idx:]


def main():
    ap = argparse.ArgumentParser(description="Add a simple login gate to a board HTML page.")
    ap.add_argument("--in", dest="src", required=True, help="input (plaintext) board HTML")
    ap.add_argument("--out", dest="outs", action="append", required=True,
                    help="output path (repeatable)")
    ap.add_argument("--user", required=True, help="username")
    ap.add_argument("--password", required=True, help="password (not stored in the page)")
    ap.add_argument("--salt", default=None,
                    help="optional fixed salt (16 hex chars). Use the same salt across pages so one login unlocks all of them")
    args = ap.parse_args()

    with open(args.src, "r", encoding="utf-8") as f:
        html = f.read()
    gated = gate_html(html, args.user, args.password, args.salt)
    for out in args.outs:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(gated)
        print("wrote gated page:", out)


if __name__ == "__main__":
    main()
