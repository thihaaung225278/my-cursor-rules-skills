# Classic ↔ SPFx parity inventory (DBS-FFW)

> Sync with repo-root `progress.md` — update both when slice status changes.

Site URL: confirm at deploy (no hardcoded tenant/site path). **Visual SoT per slice** = that year's `.aspx` + `{year}/style.css` + `{year}/sass/`. Cutover only when Status = **parity PASS**.

**Updated:** 2026-08-31 (Ffw2025 STEP 1 Scout — `2025/index.aspx`)

## Scope

Migrate **2023 · 2024 · 2025** — all year folders under `DBS-FFW-classicsite/`. One SPFx web part per classic page (rule 17). Backup/test routes = **cut**.

## Canonical

| Host | Notes |
|------|--------|
| Classic `DBS-FFW-classicsite/` | year folders `2023/` `2024/` `2025/` — **all in scope** |
| SPFx `DBS-FFW-SPFX/` | one WP per classic page; **Ffw2025** wired for `2025/index.aspx` |

## Pages — 2025

| Classic | Scripts / notes | SPFx target | Status |
|---------|-----------------|-------------|--------|
| `2025/index.aspx` | live boot = `indexController-current.js` + `events-current.json`; live = About + 3-col Highlights + GIF gallery + Schedule; `.post-event-sec` CSS hidden | **Ffw2025** | wired / baseline — shipped **v1.0.0.9**; **parity PASS မဟုတ်** |
| `2025/past-events.aspx` | `indexControllerPastEvent.js` | **PastEvents** | todo |
| `2025/back-door.aspx` | inline admin date override | **BackDoor** | defer |

## Pages — 2024

| Classic | Scripts / notes | SPFx target | Status |
|---------|-----------------|-------------|--------|
| `2024/index.aspx` | live thank-you / video-playbacks (`indexController.js`, `common.js`); `.post-event-sec` hidden | **Ffw2024** | wired / baseline — shipped **v1.0.0.8**; **parity PASS မဟုတ်** |
| `2024/past-events.aspx` | `indexControllerPastEvent.js` | WP TBD | todo |
| `2024/back-door.aspx` | inline admin | WP TBD | defer |
| `2024/index-old.aspx` / `index-current.aspx` | backups | — | cut |

## Pages — 2023

| Classic | Scripts / notes | SPFx target | Status |
|---------|-----------------|-------------|--------|
| `2023/index.aspx` | `indexController.js`, `common.js`, `spbase/config.js` | **Ffw2023** | wired / baseline — bundled assets in sppkg; visual parity pending |
| `2023/post-event.aspx` | `indexController.js`, `common.js` (2023-only route) | **PostEvent2023** | wired / baseline — Highlights `#highlight` uk-grid row-gap + named-face CSS; **parity PASS မဟုတ်** |
| `2023/back-door.aspx` | inline admin | WP TBD | defer |
| `2023/clickr-test.aspx` | test | — | cut |

## Shared

| Item | Notes | Status |
|------|-------|--------|
| Inline `header.page-banner` | chrome per ASPX | defer AC |

## Visual & assets (per year)

Each slice ports **that year's** CSS — do not assume 2025 tokens for 2023/2024 pages.

| Year | Classic | SPFx |
|------|---------|------|
| 2025 | `style.css` + `sass/`, `uikit.min.css` | `*.module.scss` + uikit parity |
| 2024 | same pattern under `2024/` | per WP |
| 2023 | same pattern under `2023/` | per WP |

## Data (per year folder)

| Source | Classic access | SPFx target | Status |
|--------|----------------|-------------|--------|
| `events.json`, `participants.json`, `post-event.json` (2023) | `commonLib.loadJson` | bundled in **Ffw2023** `assets/data/` — also consumed by **PostEvent2023** | done (2023 index + post-event) |
| `events.json`, `participants.json`, `winnerlists.json` (2024/2025) | per year folder | **Ffw2024** `events.json`; **Ffw2025** `events-current.json` bundled | Ffw2025 events-current done; 2024/2025 participants/winners TBD |

## Suggested order

1. **Ffw2025** scaffold + wired vs `2025/index.aspx` (live pre-during only)
2. **PastEvents** ↔ `2025/past-events.aspx`
3. Wave 4 remainder **Ffw2024** / **PostEvent2023** / **Ffw2023**
4. `2024/past-events.aspx` then back-door pages (defer)
