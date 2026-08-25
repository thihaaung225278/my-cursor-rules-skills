# Visual typography — font-weight & host inherit

**SoT for this clone** = `classic-visual-parity` + classic `project-saral/assets/css/shared.css` (OpenSans). This file is the **Segoe inherit / weight** gotcha only — do not replace that skill’s token table.

Fluent tokens do **not** win before Visual PASS.

## Why font-weight looks “a bit light”

1. **SP canvas inherit** — parents force **Segoe UI**; classic named faces never apply on the WP root.
2. **Root baseline missing** — module SCSS sets `font-family` but omits `font-weight: 400` → semibold/bold look soft.
3. **Font files not loaded** — `@font-face` missing vs classic `project-saral/assets/fonts/OpenSans/`
4. **Selector lose** — host rules override cloned classes
5. **Remount** — computed weight drifts after inject

## Win order (this repo)

1. Inventory classic selectors (`classic-visual-parity`) — skip none
2. Port exact px/hex/weight into `*.module.scss` (do **not** “embed classic CSS and skip SCSS”)
3. Isolate on WP root: classic `font-family` **and** `font-weight: 400`
4. Reuse existing OpenSans `@font-face` (shared partial if it exists)
5. Fix fighting `style={{}}` / theme slots before adding new weight rules

## Visual PASS (typography subset)

Side-by-side vs classic `.aspx`:

- [ ] font-family (not Segoe on classic surfaces)
- [ ] **font-weight** (headings, buttons, body)
- [ ] font-size · font color · letter-spacing · line-height
- [ ] hover weight/color changes

Full visual rows (BG, spacing, gap, `@media`) stay on `classic-visual-parity`.

## QA

1. DevTools computed `font-family` + `font-weight` on heading / body (classic vs SPFx)
2. Network: font files 200
3. Do not mark parity PASS if weight is “close enough”

## Reject

- Fluent “use tokens / no hardcoded” to replace classic weights pre-PASS
- Segoe UI as the primary stack (fallback only after OpenSans)
