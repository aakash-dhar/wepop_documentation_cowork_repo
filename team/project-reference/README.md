# Project reference - how it is built and updated

The Wepop project reference (the BetaCraft-styled, module-by-module page with the detail drawer) is
generated, not hand-edited.

- `template.html` - the page shell: styling, sidebar, sections, drawer, rendering script. Contains one
  marker, `/*__DATA__*/`, where the data is inlined at build time.
- `data.js` - all authored content: `META` (as-of date, last DEC), `M` (the 24 decided modules), `ELVIS`
  (sourced detail per module under `modules`, and the Elvis-designed modules under `new`), `PLAIN`
  (plain-language explainers keyed by module id), `FLOWS` (flow-diagram specs keyed by module id plus
  `overview` and `governance`; rendered as inline SVG by the template, no external library), plus
  `RISKS`, `OPEN`, `LEGAL`, `GOV`, `PRINCIPLES`, `DATAMODEL`, `GLOSS`. Every ELVIS item carries a `src` naming the file and section it came from.
- The decision index and the full decision records (`DECS`, `DECFULL`) are NOT in data.js: `build.py`
  parses `shared/DECISIONS.md` on every build, so the page's decisions can never drift from the source
  of truth. Clicking a decision card or any DEC chip opens the verbatim record in the drawer.
- `build.py` - assembles the page and runs checks (no em-dashes, every ELVIS item has a src). Writes the
  internal copy to `team/wepop-project-reference.html`; with `--lock --user --password` also publishes
  `docs/project-reference.html` and re-gates the board pages with ONE shared salt, so unlocking the
  dashboard once unlocks the reference too.

Outputs: `team/wepop-project-reference.html` (internal, not published), `docs/project-reference.html`
(client, behind the login gate, linked from the dashboard header), and
`architecture/phase-plan/wepop-project-reference.md` (the Markdown rendition of the same data, with the
diagrams as Mermaid so GitHub renders them). All three are overwritten on every build; never hand-edit.

To update as Elvis's documents change, use the **project-reference** skill (`skills/project-reference/`).
It reads what is new in `shared/DECISIONS.md` and `workspaces/elvis/`, updates `data.js` with sources,
runs the validation passes, rebuilds, re-gates, and suggests the commit. Never edit the built HTML
files directly; they are overwritten on the next build. Never commit or push from the skill; the human
does that in GitHub Desktop.

Ground rule carried from the record: `shared/DECISIONS.md` wins over everything here. Anything from an
Elvis document that has not landed as a DEC is shown as "Elvis design", and anything that contradicts a
landed decision is flagged in red, never silently treated as scope. No em-dashes anywhere.
