---
name: classic-to-spfx-migration
description: >-
  Migrate SharePoint Classic (ASPX/CEWP/JSOM/jQuery) sites to SPFx web parts and
  extensions with pixel-level visual parity from classic CSS. Use when the user
  mentions classic site migration, ASPX to SPFx, CEWP/SEWP replacement, JSOM to
  PnPjs, Style Library scripts, project-saral-classic pages (Knowledge Hub,
  Clearing House, repository), mapping classic scripts to React web parts,
  bulk scaffold / all pages at once / baseline wave, or classic look (font,
  color, spacing, hover, animation, responsive @media) not matching SPFx.
---

# Classic Site → SPFx Migration

Project-specific playbook for **project-saral** classic → SPFx.

## Repo layout (do not invent paths)

| Role | Path |
|------|------|
| Classic source | `project-saral-classic/` (`.aspx`, `project-saral/assets/css/*`, `project-saral/assets/js/*`, `project-saral/components/*`) |
| SPFx target | `project-saral-SPFX/` (empty until scaffolded) |

## Project pins (always respect)

Read `project-saral-SPFX/package.json` before scaffolding or suggesting upgrades.

| Concern | This repo |
|---------|-----------|
| SPFx | **1.20.x** |
| Toolchain | **gulp** (`gulp bundle` / `gulp serve` / `gulp test`) — not Heft |
| React | **17** |
| UI | **Fluent UI v8** (`@fluentui/react`) — not Fluent v9 unless user upgrades |
| Node | engines in package.json (`>=18.17.1 <19.0.0`) |

When loading the `spfx` skill: use **gulp** path and do **not** push Heft/Fluent v9 by default.

**Load order (this repo):** this file (including appendix) → `classic-visual-parity` → `uikit-to-spfx-visual-parity` → `spfx`/`pnpjs.md` if data → a11y skill for names only. Do **not** start from `spfx-enterprise-ux-hub`. Do **not** add glassmorphism or Heft skills.

**Bulk baseline (all pages / scaffold together):** load `bulk-classic-to-spfx-baseline` **first** + `docs/migration/PARITY.md`. Wave 1–3 = wired/baseline only; return here for Wave 4 parity slices.

Related skills (load only what the task needs):

0. `bulk-classic-to-spfx-baseline` — **when user asks bulk / all WPs at once** (wired/baseline; no parity PASS)
1. `classic-visual-parity` — **required on every UI migrate / visual tweak** (classic CSS is SoT)
2. `uikit-to-spfx-visual-parity` — **required on UI migrate** so UIKit/Bootstrap gap/padding/margin/font-size/animation are not left behind (`shared.css` alone is not enough)
3. `spfx` — scaffold / toolchain (do **not** follow `react-design.md` Fluent v9 / host-theme for page look)
4. `spfx-accessibility-and-content-quality` — keyboard/focus/names only; do not restyle to Fluent
5. Project rules: `.cursor/rules/04-sharepoint-standards.mdc` · `17-classic-host-and-assets.mdc`

This skill’s references (load only what the task needs):

- Full-width / SPA / 450px clip → [host-modes.md](./references/host-modes.md)
- Site Pages chrome hide (only if user asks) → [site-chrome.md](./references/site-chrome.md)
- Images / CSP / remount → [siteassets-gotchas.md](./references/siteassets-gotchas.md)
- Segoe inherit / font-weight → [visual-typography.md](./references/visual-typography.md)
- Inventory templates → [templates/](./templates/)
- Live inventory SoT → [docs/migration/PARITY.md](../../../docs/migration/PARITY.md) (sync with `progress.md`)

Do **not** apply a glassmorphism look or treat Fluent density / theme slots as the visual target. Do **not** load a second playbook named `classic-spfx-migration`.

## Workflow

### 0) Migration waves (overview)

| Wave | Skill | Status |
|------|-------|--------|
| PREP + bulk scaffold + baseline + host | `bulk-classic-to-spfx-baseline` | wired / baseline |
| Parity per slice | this file + `classic-visual-parity` | parity PASS |

One PR for Wave 0–3 is OK when user explicitly requests bulk baseline. **Parity PASS** stays feature-by-feature.

### 1) Inventory classic surface

Scan `project-saral-classic/` and sync [docs/migration/PARITY.md](../../../docs/migration/PARITY.md):

- Live pages: `knowledge-hub.aspx`, `the-clearing-house.aspx`, `the-clearing-house-repository.aspx`, `export-import.aspx`, `splists/sp-import.aspx`, `splists/sp-export.aspx`
- Shared chrome: `project-saral/components/navigation.html`, `footer.html`, `hamburger-menu.html`
- Visual CSS: `project-saral/assets/css/shared.css`, `components.css`, `knowledge-hub.css`, `k-comms.css`, `kiasu.css`, `individual.css` + used UIKit/Bootstrap classes
- Scripts: `project-saral/assets/js/knowledge-hub.js`, `script-kcomms.js`, `script-kcomms-overview.js`, `script-kcomms-individual.js`, `script-clearing-house-respository.js`, `controller/common-controller.js`, `apiclass/kcomms.js`, `apiclass/kcommsvotes.js`, `apiclass/common-query.js`
- SP helpers: `project-saral/assets/js/spbase/*` (sprestlib-php, user.js)
- Vendors: jQuery, UIKit (`project-saral/assets/css/uikit/uikit.css`, `project-saral/assets/js/uikit/uikit.js`), Bootstrap 4.4.1, Swiper, AOS
- Cut / defer: `*-backup.aspx`, `project-saral-backup/`, `script-kcomms-old.js`

Classify each feature as:

| Target | When |
|--------|------|
| **Web Part** | Page body / list UI / feature island |
| **Application Customizer** | Header/footer/chrome across pages |
| **Command Set / Field Customizer** | List toolbar or field render |
| **Stay list/out-of-box** | No custom code needed |
| **Defer / cut** | Dead pages (`*-old.aspx`) or unused scripts |

Do not edit Classic master pages / `_layouts` system files. Prefer Site Assets / Style Library patterns already in repo.

### 2) Map data access

Classic patterns in this repo → SPFx:

| Classic | SPFx |
|---------|------|
| jQuery / SPServices / string REST | PnPjs (`@pnp/sp`) preferred, or existing `SPHttpClient` |
| Hardcoded list URLs in controllers | Service module + configurable list titles/IDs via property pane |
| Writes without digest awareness | PnPjs handles digest; raw REST needs `X-RequestDigest` |
| CAML/SQL string concat | Typed filters / parameterized queries only |

AuthZ: check list/item permissions — AuthN success is not enough (IDOR).

XSS: never port CEWP/SEWP raw HTML into `dangerouslySetInnerHTML` without sanitize.

This site lists/fields/i18n/PHP map = **This site appendix** below — do not invent extra lists.

### 3) Map UI + visual parity (blocking)

- Port feature UI into React web part components under `project-saral-SPFX/src/webparts/...`
- Replace jQuery DOM hacks with React state; keep SharePoint chrome selectors untouched
- Empty / loading / error states required for list-driven UIs (copy classic empty copy/spacing if the classic page has them)
- **Visual SoT** = `project-saral-classic/project-saral/assets/css/shared.css` + page CSS (`knowledge-hub.css` / `k-comms.css` / `kiasu.css` / `individual.css` / `components.css`) + used UIKit/Bootstrap. Load `classic-visual-parity` **before** writing SCSS
- Style with `*.module.scss`. Fluent v8 controls only where classic had a comparable control — **do not** replace classic type/color/spacing with Fluent tokens
- Do not add Tailwind/SPA routers
- Mandatory clone (skip none): font-size, font-weight, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive `@media` (classic breakpoint px — not Fluent 480/1024)
- A slice is not migrated until those match classic at **each** classic breakpoint used by that page

### 4) Implement in SPFx target only

- New code lands in `project-saral-SPFX/` unless user asks to change classic for parity testing
- Keep web part thin; put REST/Graph in services
- Property pane for list names, page URLs, feature flags
- Packaging: preserve `config/package-solution.json` patterns; no secrets/tenant IDs hard-coded

### 5) Validate

Per Testing Gate:

```bash
cd project-saral-SPFX
gulp bundle
gulp test   # if present / meaningful
```

Manual smoke (workbench or served page):

1. Script/web part loads without console errors
2. List read succeeds for permitted user
3. Write path (if any) succeeds + fails cleanly without permission
4. Keyboard focus + control names on interactive controls
5. **Visual vs classic (blocking):** font-size, font-weight, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive `@media` (same classic widths; stack/wrap/hide)

## Anti-patterns

- Suggesting Heft toolchain or Fluent v9 while project is on SPFx 1.20 / Fluent v8
- Rewriting the entire classic site in one PR **for parity PASS** — use `bulk-classic-to-spfx-baseline` for scaffold/baseline only; parity stays feature-by-feature
- Copying vendor minified bundles into SPFx when Fluent/PnP covers the need (ask before new deps)
- Installing packages to `~/.cursor/skills` or user-global skills
- Mixing React (web) generic app patterns that ignore SPFx host lifecycle
- Shipping Fluent / theme-token / glassmorphism look instead of classic `project-saral/assets/css/*`
- Calling a migrate done when data works but type, color, spacing, hover, animation, or responsive `@media` still differ from classic
- Porting `project-saral-backup/` or `*-backup.aspx` as live features

## Output expectations

When asked to migrate, respond with:

1. Inventory summary (pages/scripts → target type) + CSS sources (`shared.css` / page CSS / used UIKit+Bootstrap)
2. Selected Path for this slice (one feature)
3. Visual token table (mandatory rows from `classic-visual-parity`)
4. Files to add/change under `project-saral-SPFX/`
5. Validation commands + manual smoke checklist (including visual parity rows)

## This site appendix (project-saral-classic)

Do not invent lists, fields, or languages. Do not port dead scripts or `config.js` debug dumps.

### Suggested web part map

| Classic surface | Script(s) | SPFx target |
|-----------------|-----------|-------------|
| `knowledge-hub.aspx` | `knowledge-hub.js` | Web Part **KnowledgeHub** |
| `the-clearing-house.aspx` | `script-kcomms.js`, `script-kcomms-overview.js`, `script-kcomms-individual.js` | Web Part **ClearingHouse** |
| `the-clearing-house-repository.aspx` | `script-clearing-house-respository.js` | Web Part **ClearingHouseRepository** |
| `export-import.aspx` | `splists/` | Web Part **ExportImport** (or keep as list tools) |
| `splists/sp-import.aspx` | `splists/js/*` | Web Part **SpImport** / defer |
| `splists/sp-export.aspx` | `splists/js/*` | Web Part **SpExport** / defer |
| `project-saral/components/navigation.html` + `footer.html` | — | Application Customizer (later) |

### Lists (property pane titles — defaults)

| Internal use | Classic title | Typical PnP |
|---|---|---|
| Clearing House | `Clearing House Repository` | `sp.web.lists.getByTitle("Clearing House Repository")` |
| Votes | `SComms Votes` | `sp.web.lists.getByTitle("SComms Votes")` |
| Users | `Users` | `sp.web.lists.getByTitle("Users")` |
| Clusters | `Clusters` | `tableName.Clusters` |
| Categories | `Categories` | `tableName.Categories` |
| Themes | `Themes` | `tableName.Themes` |
| Products | `Products` | `tableName.Products` |
| Departments | `Departments` | `tableName.Departments` |
| Owners | `Owners` | `tableName.Owners` |

Classic data plane is `sprLibPhp` (`project-saral/assets/js/spbase/sprestlib-php.js`) + `CommonQuery` / `KComms`. SPFx: typed object via PnPjs (`@pnp/sp`) — **ask before adding the package**. Do not call PHP `db.php`. Do not copy `config.baseSpUrl`; use `this.context.pageContext.web`.

| Classic | SPFx |
|---|---|
| `sprLibPhp.items` / `CommonQuery` | PnP `items.filter(...).orderBy(...).top(n)` — do not copy `queryLimit: 5000` as the default page size |
| `sprLibPhp.create` / `KComms.addNew` | `items.add({ ... })` |
| `User` helper (`Users` list) | `pageContext.user` (+ profile only if extra fields are required) |

Read the slice’s script before inventing columns. Do not assume change-management-learning / make-it-easy / agile-exchange field names.

### i18n

No locale folder copies (`zh/` `sc/` `id/`) in this classic tree. Port page copy via SPFx `loc/` only if a slice actually has translations.

### Do not port

- `project-saral-backup/` and `*-backup.aspx`
- `script-kcomms-old.js`
- `config.js` `console.log` / debug dumps
- Hardcoded `/sites/ClassicSite/project-saral` (use `pageContext`)
- Vendor minified jQuery / UIKit / Bootstrap / SPServices bundles as-is

`project-saral-SPFX/` is empty until Yeoman scaffold. Confirm `package.json` pins after scaffold. `config/serve.json` `initialPage` must be the real workbench/site URL before `gulp serve` against the tenant.
