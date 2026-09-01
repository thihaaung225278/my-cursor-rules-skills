# progress — DBS-FFW

> Slice ပြီးတိုင်း status ပြင်။ `active_context.md` Current slice နဲ့ sync ထား။ `docs/migration/PARITY.md` နဲ့ တိုက်ဆိုင်ထား။

**Updated:** 2026-08-31 (ship v1.0.0.10 — classic favicon)

## Legend

`todo` · `doing` · `done` · `defer` · `cut`

Status meanings (migration): **inventory only** · **wired / baseline** · **parity PASS**

## Scope (user-confirmed)

Migrate **all year folders**: `2023/` · `2024/` · `2025/`. Visual SoT **per slice** = that year's `style.css` + `sass/` (not 2025-only). Backup/test artifacts remain **cut**.

## Tooling (meta)

| Item | Status |
|------|--------|
| `.cursor/rules` + project skills | done |
| Context handoff (`13` + hooks) | done |
| `.cursorignore` / `codegraph.json` | done — all years indexed; backup `*-bk.js`, `index-old.aspx`, test files excluded |
| Unused framework rules archived | done — `.cursor/rules/archive/` |
| `active_context.md` / `progress.md` | done |
| `docs/migration/PARITY.md` sync | done — full-year inventory |
| SPFx scaffold `DBS-FFW-SPFX` | done — **Ffw2023** + **PostEvent2023** + **Ffw2024** + **Ffw2025** |
| `config/serve.json` real site URL | done — `ffw2023` → index.aspx · `postEvent2023` → post-event.aspx · `ffw2024` → index2024.aspx · `ffw2025` → index2025.aspx |
| **Ffw2023 + PostEvent2023 + Ffw2024 + Ffw2025 ship package** | done — v1.0.0.10 · `npm run ship` · ~7.7 MB (classic favicon included) |
| Codegraph index | done — 37 files · 471 nodes · 2023+2024+2025 (backups/tests excluded) |
| Codegraph auto-sync | done — MCP `serve --mcp` watcher |
| Classic favicon (all live WPs) | done (code + shipped **v1.0.0.10**) — `src/shared/host/favicon.ico` + `classicHostUnlock`; **live tab smoke after App Catalog**; **parity PASS မဟုတ်** |

## Inventory → target

| Classic surface | Scripts / notes | SPFx target | Status |
|-----------------|-----------------|-------------|--------|
| `2025/index.aspx` | live boot = `indexController-current.js` + `events-current.json`; live = About + Highlights + GIF gallery + Schedule; `.post-event-sec` CSS hidden | **Ffw2025** | wired / baseline — shipped **v1.0.0.9**; schedule `.contents` opacity 1 (classic cascade; over-specific `.check-past` 0.4 ဖြုတ်); **parity PASS မဟုတ်** |
| `2025/past-events.aspx` | `indexControllerPastEvent.js` | **PastEvents** | todo |
| `2025/back-door.aspx` | inline admin date override | **BackDoor** | defer |
| `2024/index.aspx` | `indexController.js` + `common.js` — live = thank-you / video-playbacks (`.post-event-sec` hidden) | **Ffw2024** | wired / baseline — shipped **v1.0.0.8**; Video Playbacks flatten + `.desc` a/img; `.desc a` host underline ဖြုတ်; **parity PASS မဟုတ်** |
| `2024/past-events.aspx` | `indexControllerPastEvent.js` | WP TBD | todo |
| `2024/back-door.aspx` | inline admin | WP TBD | defer |
| `2023/index.aspx` | `indexController.js`, `common.js`, `spbase/config.js` | **Ffw2023** | wired / baseline — menu hash/anchor classic 1000ms scroll + `pushState`; remainder visual/func parity pending |
| `2023/post-event.aspx` | `indexController.js`, `common.js` | **PostEvent2023** | wired / baseline — `#schedule` `renderEventList`; `#game_show_winners` no photo slider (dropdown-above-card); shipped **v1.0.0.7**; **parity PASS မဟုတ်** |
| `2023/back-door.aspx` | inline admin | WP TBD | defer |
| Inline `header.page-banner` | chrome in each ASPX | stay in-page | defer AC |
| `2024/index-old.aspx` / `2024/index-current.aspx` / `2023/clickr-test.aspx` | backups / test | — | cut |
| Per-year `style.css` + `sass/` | visual SoT per slice | `*.module.scss` via `classic-visual-parity` | todo |
| Per-year `public/css/vendor/uikit.min.css` | `uk-*` | `uikit-to-spfx-visual-parity` | todo |
| Year JSON (`events.json`, `participants.json`, `post-event.json`) | per year folder | bundled in **Ffw2023** `assets/data/` — **PostEvent2023** consumes same | done (2023 index + post-event) |

## Suggested order

1. **Ffw2025** live smoke vs classic — schedule cards opaque white + full-contrast type (`npm run serve:ffw2025` on `index2025.aspx`)
2. `2025/past-events.aspx` → **PastEvents**
3. Ffw2024 remainder visual — parked
4. Wave 4 remainder **PostEvent2023** / **Ffw2023** vs 2023 live
5. `2024/past-events.aspx` then `2024/back-door.aspx` (defer)
6. `2023/back-door.aspx` (defer)
