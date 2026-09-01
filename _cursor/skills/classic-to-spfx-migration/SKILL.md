---
name: classic-to-spfx-migration
description: >-
  Migrate SharePoint Classic (ASPX/CEWP/JSOM/jQuery) sites to SPFx web parts and
  extensions with pixel-level visual parity from style.css. Use when the user
  mentions classic site migration, ASPX to SPFx, CEWP/SEWP replacement, JSOM to
  PnPjs, Style Library scripts, DBS-FFW-classicsite pages (FFW / LFC home,
  past-events, back-door), mapping classic scripts to React web parts,
  bulk scaffold / all pages at once / baseline wave, or classic look
  (font, color, spacing, hover, animation, responsive @media) not matching SPFx.
---

# Classic Site → SPFx Migration

Project-specific playbook for **DBS-FFW** classic → SPFx.

## Repo layout (do not invent paths)

| Role | Path |
|------|------|
| Classic source | `DBS-FFW-classicsite/` — year folders `2023/` `2024/` `2025/` (`.aspx`, `style.css`, `sass/`, `public/`) |
| Visual SoT (current) | `DBS-FFW-classicsite/2025/` (`index.aspx`, `past-events.aspx`, `style.css`, `sass/`) |
| SPFx target | `DBS-FFW-SPFX/` (**Ffw** web part already scaffolded) |

Do **not** treat `2023/` or `2024/` as live migrate targets unless the user names that year.

## Project pins (always respect)

Read `DBS-FFW-SPFX/package.json` before scaffolding or suggesting upgrades.

| Concern | This repo |
|---------|-----------|
| SPFx | **1.20.x** |
| Toolchain | **gulp** (`gulp bundle` / `gulp serve` / `gulp test`) — not Heft |
| React | **17** |
| UI | **Fluent UI v8** (`@fluentui/react`) — not Fluent v9 unless user upgrades |
| Node | engines in package.json (`>=18.17.1 <19.0.0`) |

When loading the `spfx` skill: use **gulp** path and do **not** push Heft/Fluent v9 by default.

**Load order (this repo):** this file (including appendix) → `classic-visual-parity` → **[visual-typography.md](./references/visual-typography.md) (required on UI migrate — typography self-check)** → `uikit-to-spfx-visual-parity` → `spfx`/`pnpjs.md` if data → a11y skill for names only. Do **not** start from `spfx-enterprise-ux-hub`. Do **not** add glassmorphism or Heft skills.

**Bulk baseline (all pages / scaffold together):** load `bulk-classic-to-spfx-baseline` **first** + `docs/migration/PARITY.md`. Wave 1–3 = wired/baseline only; return here for Wave 4 parity slices.

Related skills (load only what the task needs):

0. `bulk-classic-to-spfx-baseline` — **when user asks bulk / all WPs at once** (wired/baseline; no parity PASS)
1. `classic-visual-parity` — **required on every UI migrate / visual tweak** (classic CSS is SoT)
2. **[visual-typography.md](./references/visual-typography.md)** — **required on every UI migrate** — named-face `font-weight: 400`, menu link underline, typography self-check table (blocking before parity PASS)
3. `uikit-to-spfx-visual-parity` — **required on UI migrate** so UIKit/Swiper gap/padding/margin/font-size/animation are not left behind (`style.css` alone is not enough)
4. `swiper-to-spfx-carousel` — when slice has `.winner-slider` / `.gallery-slider` (wire init + scoped nav; not vendor bundle)
5. `spfx` — scaffold / toolchain (do **not** follow `react-design.md` Fluent v9 / host-theme for page look)
6. `spfx-accessibility-and-content-quality` — keyboard/focus/names only; do not restyle to Fluent
7. Project rules: `.cursor/rules/04-sharepoint-standards.mdc` · `17-classic-host-and-assets.mdc`

This skill’s references (load with UI migrate — typography is not optional):

- Segoe inherit / font-weight / link underline self-check → [visual-typography.md](./references/visual-typography.md) **(required)**
- Full-width / SPA / 450px clip → [host-modes.md](./references/host-modes.md)
- Site Pages chrome hide (only if user asks) → [site-chrome.md](./references/site-chrome.md)
- Images / CSP / remount → [siteassets-gotchas.md](./references/siteassets-gotchas.md)
- Inventory templates → [templates/](./templates/)
- Live inventory SoT → [docs/migration/PARITY.md](../../../docs/migration/PARITY.md) (sync with `progress.md`)

Do **not** apply a glassmorphism look or treat Fluent density / theme slots as the visual target. Do **not** load a second playbook named `classic-spfx-migration`.

## Workflow

### 0) Migration waves (overview)

| Wave | Skill | Status |
|------|-------|--------|
| PREP + bulk scaffold + baseline + host | `bulk-classic-to-spfx-baseline` | wired / baseline |
| Parity per slice | this file + `classic-visual-parity` + `visual-typography` self-check | parity PASS |

One PR for Wave 0–3 is OK when user explicitly requests bulk baseline. **Parity PASS** stays feature-by-feature.

### 1) Inventory classic surface

Scan `DBS-FFW-classicsite/2025/` and sync [docs/migration/PARITY.md](../../../docs/migration/PARITY.md):

- Live pages: `2025/index.aspx`, `2025/past-events.aspx`
- Admin / defer: `2025/back-door.aspx`
- Shared chrome: **inline** in each ASPX (`header.page-banner`) — no `components/header.aspx`
- Visual CSS: `2025/style.css` (compiled SoT), `2025/sass/` (`style.sass`, `_home`, `_fonts`), UIKit + Swiper + hamburgers classes the ASPX actually uses
- Scripts: `2025/public/js/controller/indexController.js`, `indexControllerPastEvent.js`, `winnerController.js`, `home.js`, `common.js`, `lib/common-lib.js`, `lib/lib.js`
- SP helpers: `2025/public/js/spbase/sprestlib-php.js`, `config.js`, `jquery.SPServices.min.js`
- Vendors: jQuery, UIKit (`public/css/vendor/uikit.min.css`, `public/js/vendor/uikit.min.js`), Swiper, FullCalendar (`index.global*.js`), lottie, anime, ical, papaparse, moment
- Data JSON: `events.json`, `events-current.json`, `post-event.json`, `participants.json`, `winnerlists.json`
- Cut / defer: `2024/index-old.aspx`, `2024/index-current.aspx`, `2023/clickr-test.aspx`, `*-bk.js` / `testController.js`; prior-year trees unless user names them

Classify each feature as:

| Target | When |
|--------|------|
| **Web Part** | Page body / list UI / feature island |
| **Application Customizer** | Header/footer/chrome across pages |
| **Command Set / Field Customizer** | List toolbar or field render |
| **Stay list/out-of-box** | No custom code needed |
| **Defer / cut** | Dead pages (`*-old.aspx`, test pages) or unused scripts |

Do not edit Classic master pages / `_layouts` system files. Prefer Site Assets / Style Library patterns already in repo.

### 2) Map data access

Classic patterns in this repo → SPFx:

| Classic | SPFx |
|---------|------|
| `loadJson('events.json')` / participants / winnerlists | Fetch from SiteAssets / property-pane URL, or bundle small JSON — **ask before** changing source |
| jQuery / SPServices / string REST | PnPjs (`@pnp/sp`) preferred, or existing `SPHttpClient` |
| Hardcoded list URLs in controllers | Service module + configurable list titles/IDs via property pane |
| Writes without digest awareness | PnPjs handles digest; raw REST needs `X-RequestDigest` |
| CAML/SQL string concat | Typed filters / parameterized queries only |

AuthZ: check list/item permissions — AuthN success is not enough (IDOR).

XSS: never port CEWP/SEWP raw HTML into `dangerouslySetInnerHTML` without sanitize.

This site lists/fields/i18n/PHP map = **This site appendix** below — do not invent extra lists.

### 3) Map UI + visual parity (blocking)

- Port feature UI into React web part components under `DBS-FFW-SPFX/src/webparts/...`
- Replace jQuery DOM hacks with React state; keep SharePoint chrome selectors untouched
- Empty / loading / error states required for list-driven UIs (copy classic empty copy/spacing if the classic page has them)
- **Visual SoT** = that slice’s year `style.css` (+ `sass/` + ASPX / used UIKit + Swiper). Load `classic-visual-parity` **before** writing SCSS; run [visual-typography.md](./references/visual-typography.md) **self-check before parity PASS**
- Style with `*.module.scss`. Fluent v8 controls only where classic had a comparable control — **do not** replace classic type/color/spacing with Fluent tokens
- Do not add Tailwind/SPA routers
- Mandatory clone (skip none): font-size, font-weight, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive `@media` (classic breakpoint px — not Fluent-only 480/1024)
- A slice is not migrated until those match classic at **each** classic breakpoint used by that page

### 4) Implement in SPFx target only

- New code lands in `DBS-FFW-SPFX/` unless user asks to change classic for parity testing
- Keep web part thin; put REST/Graph/JSON loaders in services
- Property pane for JSON/asset URLs, page URLs, feature flags
- Packaging: preserve `config/package-solution.json` patterns; no secrets/tenant IDs hard-coded

### 5) Validate

Per Testing Gate:

```bash
cd DBS-FFW-SPFX
gulp bundle
gulp test   # if present / meaningful
```

Manual smoke (workbench or served page):

1. Script/web part loads without console errors
2. JSON / list read succeeds for permitted user
3. Write path (if any) succeeds + fails cleanly without permission
4. Keyboard focus + control names on interactive controls
5. **Visual vs classic (blocking):** font-size, font-weight, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive `@media` (same classic widths; stack/wrap/hide)

## Anti-patterns

- Suggesting Heft toolchain or Fluent v9 while project is on SPFx 1.20 / Fluent v8
- Rewriting the entire classic site in one PR **for parity PASS** — use `bulk-classic-to-spfx-baseline` for scaffold/baseline only; parity stays feature-by-feature
- Copying vendor minified bundles into SPFx when Fluent/PnP covers the need (ask before new deps)
- Installing packages to `~/.cursor/skills` or user-global skills
- Mixing React (web) generic app patterns that ignore SPFx host lifecycle
- Shipping Fluent / theme-token / glassmorphism look instead of classic `style.css`
- Calling a migrate done when data works but type, color, spacing, hover, animation, or responsive `@media` still differ from classic
- Porting `2023/clickr-test.aspx` / `*-old.aspx` / `testController.js` as live features
- Scaffolding a separate WP per year folder unless the user asks

## Output expectations

When asked to migrate, respond with:

1. Inventory summary (pages/scripts → target type) + CSS sources (`2025/style.css` / `sass/` / used UIKit+Swiper)
2. Selected Path for this slice (one feature)
3. Visual token table (mandatory rows from `classic-visual-parity`)
4. Files to add/change under `DBS-FFW-SPFX/`
5. Validation commands + manual smoke checklist (including visual parity rows)

## This site appendix (DBS-FFW-classicsite)

Do not invent lists, fields, or languages. Do not port dead scripts or `config.js` debug dumps.

### Suggested web part map

| Classic surface | Script(s) | SPFx target |
|-----------------|-----------|-------------|
| `2025/index.aspx` | `indexController.js`, `winnerController.js`, `home.js`, `common.js` | Web Part **Ffw** (exists) |
| `2025/past-events.aspx` | `indexControllerPastEvent.js` | Web Part **PastEvents** / scaffold |
| `2025/back-door.aspx` | inline admin date override | Web Part **BackDoor** / defer |
| Inline `header.page-banner` | — | stay in-page (Application Customizer later only if user asks) |
| `2024/*`, `2023/*` | prior-year copies | cut / defer unless user names that year |
| `2024/index-old.aspx`, `2023/clickr-test.aspx` | — | cut |

### Data (property pane — defaults)

Primary data plane is **year JSON next to the ASPX**, not InsightsBank-style SharePoint lists. Do not invent list titles.

| Use | Classic source |
|---|---|
| Events | `2025/events.json` / `events-current.json` |
| Post-event | `2025/post-event.json` |
| Participants | `2025/participants.json` |
| Winners | `2025/winnerlists.json` |

`sprLibPhp` (`public/js/spbase/sprestlib-php.js`) + `CommonLib` exist for optional SP list CRUD. SPFx: typed object via PnPjs (`@pnp/sp`) — **ask before adding the package**. Do not call PHP `db.php`. Do not copy `config.baseSpUrl`; use `this.context.pageContext.web`. Read the slice’s script before inventing columns or list names.

| Classic | SPFx |
|---|---|
| `commonLib.loadJson('events.json')` | `SPHttpClient` / fetch from SiteAssets or property-pane URL |
| `sprLibPhp.items` / `itemsCAML` | PnP `items.filter(...).orderBy(...).top(n)` — do not copy `queryLimit: 5000` as the default page size |
| `sprLibPhp.create` / `update` | `items.add({ ... })` / `items.getById(id).update({ ... })` |
| Current user helper | `pageContext.user` (+ profile only if extra fields are required) |

Do not assume dbs-Insights-Bank / project-saral / change-management-learning field names.

### i18n

No locale folder copies (`zh/` `sc/` `id/`) in this classic tree. Port page copy via SPFx `loc/` only if a slice actually has translations.

### Do not port

- `2023/clickr-test.aspx`, `2024/index-old.aspx`, `testController.js`, `indexController-bk.js`
- `config.js` `console.log` / `userStaticDebug` / `userStaticProfile` dumps
- Hardcoded `/sites/ClassicSite/dbs-ffw` (use `pageContext`)
- Vendor minified jQuery / UIKit / Swiper / FullCalendar / SPServices bundles as-is

`DBS-FFW-SPFX/` already has the **Ffw** web part. Confirm `package.json` pins before suggesting upgrades. `config/serve.json` `initialPage` must be the real workbench/site URL before `gulp serve` against the tenant.
