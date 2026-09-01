# Classic ↔ SPFx parity inventory (DBS-FFW)

Site URL: confirm at deploy (no hardcoded tenant/site path). Visual SoT = classic `.aspx` + `DBS-FFW-classicsite/2025/style.css`. Cutover only when Status = **parity PASS**.

## Canonical

| Host | Notes |
|------|--------|
| Classic `DBS-FFW-classicsite/` | year folders `2023/` `2024/` `2025/`; live SoT = `2025/` |
| SPFx `DBS-FFW-SPFX/` | one WP per live page; **Ffw** already scaffolded |

## Pages

| Classic | SPFx target | Status |
|---------|-------------|--------|
| `2025/index.aspx` | Ffw | todo |
| `2025/past-events.aspx` | PastEvents | todo |
| `2025/back-door.aspx` | BackDoor | defer |
| `2024/*` / `2023/*` | — | cut / defer unless user names that year |
| `2024/index-old.aspx` / `2023/clickr-test.aspx` | — | cut |

## Chrome

Classic chrome = **inline** `header.page-banner` per ASPX. Site Pages `ShowHeader` / `ShowFooter` / `ShowBanner` only if the user asks to hide modern SP chrome — see `references/site-chrome.md`.

## Immutable contracts

- Classic class semantics + visual token rows (`classic-visual-parity`)
- No hardcoded site path
- OpenSans-Condensed weights used by classic CSS must load on SPFx
- Data = year JSON (`events.json`, `participants.json`, `winnerlists.json`) via `SPHttpClient` / fetch; `@pnp/sp` ask-first
- Do not invent SharePoint lists unless the slice’s script proves them

## Visual PASS checklist

font-size · **font-weight** · font color · BG · spacing · gap · margin · padding · break-line · letter-spacing · line-height · hover · animation · `@media` (classic px)

| Status | Meaning |
|--------|---------|
| inventory only | Docs only |
| wired / baseline | Func OK; visual may FAIL |
| parity PASS | Func + Visual |

Fill live status in `docs/migration/PARITY.md` (repo SoT) — keep in sync with `progress.md`. This file is the skill template copy.
