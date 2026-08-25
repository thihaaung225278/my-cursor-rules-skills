# Classic ↔ SPFx parity inventory (project-saral)

> Live SoT for route Status. Sync with repo-root `progress.md` after each wave.  
> Bulk baseline: `.cursor/skills/bulk-classic-to-spfx-baseline/SKILL.md`

Site URL: confirm at deploy — **no hardcoded tenant/site path**. Visual SoT = classic `.aspx` + `project-saral/assets/css/*`.

## Canonical

| Host | Notes |
|------|--------|
| Classic `project-saral-classic/` | Live `.aspx` + `project-saral/assets/` |
| SPFx `project-saral-SPFX/` | **One web part per live page** (no hub router) |

Each full-bleed WP: `supportsFullBleed: true` + full-width section — see `SITEASSETS.md` / skill `host-modes.md`.

## Pages

| Classic | Scripts / CSS | SPFx target | Status |
|---------|---------------|-------------|--------|
| `knowledge-hub.aspx` | `knowledge-hub.js`, `knowledge-hub.css` | **KnowledgeHub** | wired / baseline — visual QA pending |
| `the-clearing-house.aspx` | `script-kcomms*.js`, `k-comms.css`, `kiasu.css`, `individual.css` | **ClearingHouse** | wired / baseline — overview table hover + Submitted Ideas list; quote-bubble type (17/20px, Bold+700) cloned from ASPX/`k-comms.css`; live visual QA pending |
| `the-clearing-house-repository.aspx` | `script-clearing-house-respository.js` | **ClearingHouseRepository** | wired / baseline — listing + `?itemId=` detail (same WP; Site Pages reserved `?id=` avoided); votes list 404 no longer blocks detail (classic parity); **Submit Feedback** opens shared Direct2RC modal in-place (CH modal extracted; `gulp test` PASS); card lines + paginationBox sprite ported; listing hover overlay covers `.spacer` (`z-index: 2`); **detail Verdict/Details:** OpenSans-Bold + host `h3` border reset + classic `50vw` splitter + `col-md-10` wrap (`gulp test` PASS); live visual QA pending (not PASS); **detail Back/Title/Like + white-box:** STEP 3 heart sprite + `#4e74ff` values (`gulp test` PASS); live visual QA pending (not PASS); **detail title size:** UIKit h1 35.7px / 42px @960 + host `h1` reset (`gulp test` PASS); **detail title width:** Bootstrap `col-md-10` wrap (`gulp test` PASS); live visual QA pending (not PASS); **filter pills + lookup Titles:** STEP 3 `pill-x.webp` close icon + `ClusterId`/`ProductId`/`DepartmentId`/`OwnerId` Title join on cards/detail (`gulp test` PASS); live QA pending (not PASS) |
| `export-import.aspx` | Export JSON / Import stub | **ExportImport** | cut — re-scaffold in bulk Wave 1 |
| `splists/sp-import.aspx` | splists JS | **SpImport** | defer |
| `splists/sp-export.aspx` | splists JS | **SpExport** | defer |
| `*-backup.aspx` / `project-saral-backup/` | — | — | cut |

## Chrome

Classic chrome = inline per ASPX (`project-saral/components/navigation.html`, `footer.html`, `hamburger-menu.html`).  
Site Pages `ShowHeader` / `ShowFooter` gate **custom** SaralChrome AC — see `SITE_CHROME.md`.  
Shared SPFx chrome: **Application Customizer** `SaralChromeApplicationCustomizer` (primary when site CustomAction active) + **in-WP `PageChrome` fallback** on KnowledgeHub / ClearingHouse / ClearingHouseRepository (defers when AC active). See `SITE_CHROME.md`.

## Immutable contracts

- Classic class semantics + visual token rows (`classic-visual-parity`, `uikit-to-spfx-visual-parity`)
- No hardcoded site path — use `pageContext`
- OpenSans weights from classic CSS must load on SPFx
- Data = `SPHttpClient`; `@pnp/sp` ask-first
- Lists: Clearing House Repository, SComms Votes, Users, Clusters, Categories, Themes, Products, Departments, Owners — do not invent beyond script proof

## Visual PASS checklist (Wave 4 only)

font-size · **font-weight** · font color · BG · spacing · gap · margin · padding · break-line · letter-spacing · line-height · hover · animation · `@media` (classic px)

| Status | Meaning |
|--------|---------|
| inventory only | Docs only; no WP |
| wired / baseline | Loads; func stub OK; **visual may FAIL** |
| parity PASS | Func + Visual checklist PASS |

## Cutover

Classic stays live until SPFx route exists **and** Status = **parity PASS** for that route.
