# active_context — project-saral

## Goal
Ship production `.sppkg` for App Catalog (includes Repo pills + lookup Titles since `1.0.0.6`).

## Pins
SPFx 1.20 gulp · React 17 · Fluent v8 · Reject Heft/v9, classic master, secrets, Codegraph Cursor hooks.

## Current slice
Release — `project-saral-spfx.sppkg` v`1.0.0.7`

## Status
sppkg built · App Catalog upload pending

## DONE
- Version bump `1.0.0.6` → `1.0.0.7` (`package-solution.json` solution + feature)
- Node 18.20.8: `gulp clean` + `gulp bundle --ship` + `gulp package-solution --ship` PASS
- Artifact: `project-saral-SPFX/sharepoint/solution/project-saral-spfx.sppkg` (~1.5 MB, 25 Aug 12:04) — AppManifest `Version="1.0.0.7"`

## PARTIAL
- Tenant App Catalog upload / site app update not done this turn
- Live visual QA still pending (not PASS)

## NEXT
Upload `1.0.0.7` to App Catalog → Enable → Project Saral Site contents update app → WebView smoke (KH / CH / Repo).

## Out of scope
Heft/v9; `@pnp/sp`; classic master; live deploy from this agent.

## Context ကုန်လို့ နောက် chat

```
Continue project-saral from active_context.md + progress.md.
DONE: sppkg v1.0.0.7 ship (~1.5 MB) at project-saral-SPFX/sharepoint/solution/project-saral-spfx.sppkg.
NEXT: App Catalog upload 1.0.0.7 + site app update + live WebView smoke.
Pins: SPFx 1.20 gulp, React 17, Fluent v8. Reject Heft/v9, classic master, secrets, Codegraph Cursor hooks.
If context thin: update active_context handoff only — no code.
Mode B: ..chain → y → y; one STEP per y.
```
