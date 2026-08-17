#!/usr/bin/env bash
# snapshot.sh - archive a dated copy of the Wepop delivery dashboard and rebuild the history index.
# Run from the docs/ folder:  cd docs && bash dashboard-versions/snapshot.sh
# This script does NOT run git. The human syncs via GitHub Desktop.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS="$(cd "$HERE/.." && pwd)"
SRC="$DOCS/index.html"
STAMP="$(date +%Y-%m-%d_%H%M)"
DEST="$HERE/index_${STAMP}.html"

if [ ! -f "$SRC" ]; then
  echo "error: $SRC not found" >&2
  exit 1
fi

cp "$SRC" "$DEST"
echo "snapshot archived: dashboard-versions/index_${STAMP}.html"

# Rebuild the history index page listing every snapshot, newest first.
INDEX="$HERE/history.html"
{
  echo "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
  echo "<title>Wepop dashboard - version history</title>"
  echo "<style>body{font:15px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;max-width:1320px;margin:0 auto;padding:32px 24px;background:#0f1420;color:#e6ebf4}a{color:#5b8cff}h1{font-size:20px}li{margin:6px 0}</style>"
  echo "</head><body><h1>Wepop dashboard - version history</h1><ul>"
  ls -1 "$HERE"/index_*.html 2>/dev/null | sort -r | while read -r f; do
    b="$(basename "$f")"
    echo "<li><a href=\"$b\">$b</a></li>"
  done
  echo "</ul></body></html>"
} > "$INDEX"
echo "history rebuilt: dashboard-versions/history.html"
