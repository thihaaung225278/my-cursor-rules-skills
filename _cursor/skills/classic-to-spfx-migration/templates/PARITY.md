# Classic ↔ SPFx parity inventory (project-saral)

Site URL: confirm at deploy (no hardcoded tenant/site path). Visual SoT = classic `.aspx` + `project-saral/assets/css/*`. Cutover only when Status = **parity PASS**.

## Canonical

| Host | Notes |
|------|--------|
| Classic `project-saral-classic/` | live `.aspx` + `project-saral/assets/` |
| SPFx `project-saral-SPFX/` | one WP per live page; scaffold first |

## Pages

| Classic | SPFx target | Status |
|---------|-------------|--------|
| `knowledge-hub.aspx` | KnowledgeHub | todo |
| `the-clearing-house.aspx` | ClearingHouse | todo |
| `the-clearing-house-repository.aspx` | ClearingHouseRepository | todo |
| `export-import.aspx` | ExportImport | todo |
| `splists/sp-import.aspx` | SpImport | todo |
| `splists/sp-export.aspx` | SpExport | todo |
| `*-backup.aspx` / `project-saral-backup/` | cut | cut |

## Chrome

Classic chrome = `project-saral/components/navigation.html`, `footer.html`, `hamburger-menu.html`. Site Pages `ShowHeader` / `ShowFooter` / `ShowBanner` only if the user asks to hide modern SP chrome — see `references/site-chrome.md`.

## Immutable contracts

- Classic class semantics + visual token rows (`classic-visual-parity`)
- No hardcoded site path
- OpenSans weights used by classic CSS must load on SPFx
- Data = `SPHttpClient`; `@pnp/sp` ask-first
- Do not invent lists beyond Clearing House Repository / SComms Votes / Users / Clusters / Categories / Themes / Products / Departments / Owners unless the script proves them

## Visual PASS checklist

font-size · **font-weight** · font color · BG · spacing · gap · margin · padding · break-line · letter-spacing · line-height · hover · animation · `@media` (classic px)

| Status | Meaning |
|--------|---------|
| inventory only | Docs only |
| wired / baseline | Func OK; visual may FAIL |
| parity PASS | Func + Visual |

Fill live status in `docs/migration/PARITY.md` (repo SoT) — keep in sync with `progress.md`. This file is the skill template copy.
