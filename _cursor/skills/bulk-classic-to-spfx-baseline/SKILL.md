---
name: bulk-classic-to-spfx-baseline
description: >-
  Bulk scaffold multiple classic ASPX pages into separate SPFx web parts in one
  wave — wired/baseline only, parity later. Use when the user asks to convert
  all pages at once, bulk scaffold, baseline wave, or wire multiple web parts
  together without claiming visual PASS. DBS-FFW only; no hub pageKey router.
---

# Bulk Classic → SPFx Baseline (DBS-FFW)

Fast **wire-first** wave adapted from Clickr `mk` playbook — **without** hub router or mk chat/behavior rules.

## When to load

| Load | Skip |
|------|------|
| User asks bulk / all pages / all web parts at once / baseline wave / scaffold together | Single-slice visual parity tweak only |
| Re-scaffold cut WPs (PastEvents, BackDoor) as stubs | Hub `pageKey` router (rejected in rule 17) |
| Inventory + manifest + serve.json for all live routes | Claiming parity PASS in the same wave |

**Load order:** `docs/migration/PARITY.md` → this skill → `classic-to-spfx-migration` (appendix) → `spfx`/`create.md` for Yeoman patterns → parity skills **not** required until Wave 3.

## Hard rejects (same as main migration)

- Hub web part + `pageKey` router (one WP per classic page only)
- Heft / Fluent v9 while on SPFx 1.20 / Fluent v8
- New npm packages without user approval
- Marking **parity PASS** or Visual PASS during baseline wave
- Porting `2023/clickr-test.aspx` / `*-old.aspx` / prior-year trees unless user names them
- Hardcoded tenant/site URLs
- Embedding full vendor minified jQuery/UIKit/Swiper/FullCalendar bundles in sppkg

## Wave order (do not skip)

| Wave | Goal | Status allowed |
|------|------|----------------|
| **0 PREP** | Sync `docs/migration/PARITY.md` + `progress.md` | inventory only |
| **1 SCAFFOLD** | Yeoman-style WP folders for every **live** route in PARITY table | inventory → wired |
| **2 BASELINE** | Thin React shell + shared classic SCSS hook + manifest `supportsFullBleed` + `config.json` + `serve.json` | **wired / baseline** |
| **3 HOST** | Per-WP full-width unlock if canvas clips — [host-modes.md](../classic-to-spfx-migration/references/host-modes.md) | wired / baseline |
| **4 PARITY** | **Separate slices** — `classic-visual-parity` + [visual-typography.md](../classic-to-spfx-migration/references/visual-typography.md) self-check + `uikit-to-spfx-visual-parity` | parity PASS |

Wave 1–3 may land in **one PR** when user explicitly requests bulk baseline. Wave 4 stays **feature-by-feature**.

## Architecture (this repo)

```
Classic ASPX (one page)  →  SPFx Web Part (one WP)  →  optional SPA host per page
NOT: one hub WP + pageKey router
```

| Classic | SPFx target | Notes |
|---------|-------------|-------|
| `2025/index.aspx` | **Ffw** | exists |
| `2025/past-events.aspx` | **PastEvents** | scaffold if in scope |
| `2025/back-door.aspx` | **BackDoor** | defer unless user asks |

## Wave 1 — Scaffold checklist (per WP)

Under `DBS-FFW-SPFX/src/webparts/<Name>/`:

- `<Name>WebPart.ts` + `.manifest.json` (`supportsFullBleed: true`, `SharePointWebPart` + `SharePointFullPage`)
- `components/<Name>.tsx` + `I<Name>Props.ts`
- `components/<Name>.module.scss` (host isolation only in baseline)
- `loc/en-us.js` + `mystrings.d.ts`
- Register in `config/config.json` bundles
- Add `config/serve.json` entry pointing at tenant page with `debug=true&noredir=true`

Copy patterns from the existing **Ffw** web part — do not invent new architecture.

## Wave 2 — Baseline content (minimal)

Goal: page loads without console errors; classic **look** may FAIL.

1. Root wrapper class matching classic page root (e.g. FFW home root from `2025/index.aspx`)
2. Import shared classic tokens via existing `src/shared/styles/classicGlobal.scss` (or equivalent) — do **not** paste full `uikit.min.css`
3. Placeholder structure for main regions (header area optional; body sections stubbed)
4. Data: read-only smoke only OR static placeholder — full JSON/PnP port is Wave 4
5. Property pane: JSON/asset URL defaults from `classic-to-spfx-migration` appendix (`events.json`, etc.)

## Wave 3 — Host

Per WP that needs full classic width:

- Full-width section on modern page
- Ancestor unlock (width + height/overflow) per [host-modes.md](../classic-to-spfx-migration/references/host-modes.md)
- Document host mode in `docs/migration/SITEASSETS.md`

## Validation (baseline wave)

```bash
cd DBS-FFW-SPFX
gulp bundle
gulp test   # if meaningful
```

Smoke (all WPs in scope):

1. Each WP loads on workbench or served tenant page — no console errors
2. `supportsFullBleed` manifest present
3. Root layout visible (stub OK)
4. **Do not** block on visual parity checklist

Update `docs/migration/PARITY.md` Status column and sync `progress.md`.

## Output expectations (bulk wave)

1. PARITY table diff (before → after Status)
2. List of WPs scaffolded vs already present
3. Files added under `DBS-FFW-SPFX/`
4. `gulp bundle` result
5. Explicit note: **wired/baseline only — parity PASS deferred to Wave 4 slices**

## Anti-patterns

- Using this skill to skip Wave 4 forever
- One mega React file routing all pages (hub pattern)
- Fluent redesign instead of classic SCSS hook
- Declaring migration complete after baseline
- Bulk parity PASS in one agent turn (context + quality bar — split slices)
