# progress — project-saral

## Inventory / slices

| Slice | Status | Notes |
|-------|--------|-------|
| SaralChrome live ShowHeader/ShowFooter | code sure-fix · deploy pending | v`1.0.0.5`: in-WP `PageChrome` on KH/CH/Repo + site feature CustomAction (`skipFeatureDeployment: false`). Bundle ship PASS. |
| Clearing House / KH / Repository WPs | see docs/migration/PARITY.md | CH quote-bubble type cloned; live visual QA pending. Repo listing + `?itemId=` detail on same WP. **Repo filter pills + lookup Titles:** STEP 3 — `pill-x.webp` close on `.pillButton`; Cluster/Product/Department/Owner via `*Id` + list Title join (`gulp test` PASS); live filter/card/detail QA pending. **CH Submitted Ideas → Repo detail:** writers emit `itemId` (strip reserved `id`); **`env=WebView` on detail href:** STEP 3 — `withPageUrlQuery` copies `env` + CH cards force `env=WebView` (`gulp test` PASS); live click QA pending (old `?id=` bookmarks still host-404). **Repo card hover white line:** STEP 3 — `.cardOverlay` `z-index: 2` above `.spacer` (`gulp test` PASS); live hover QA pending. **Repo Submit Feedback button:** classic `.btn-red` tokens (200×47, pad 13×25, 14px/600) + header gap · gulp test PASS; live visual QA pending. **Repo Submit Feedback Direct2RC modal:** STEP 3 — shared `Direct2RcModal` (reuse CH submit); in-place on repository (`gulp test` PASS); live overlay QA pending. **Repo detail vs `SComms Votes` 404:** STEP 3 — 404 degrades to default likes; item still renders. **Submissions detail loading overlay:** STEP 3 + 0.5 backdrop / min 500ms hold · gulp test PASS. **Repo detail Verdict / Details on areas of concern:** OpenSans-Bold headings, host `h3` underline reset, classic `50vw`/`2.5px #858f97` splitter, Bootstrap `col-md-10` wrap (`gulp test` PASS); live visual QA pending. **Repo detail Back / Title / Like + Owner–Status white-box:** STEP 3 — `heart-spr.webp` on `.btnHeart` (`#ff0023` 160×47 sprite), white-box `#4e74ff` OpenSans-Bold values + host border reset, Back 16px OpenSans-Bold; no invented title icon (`gulp test` PASS); live visual QA pending. **Repo detail title size:** UIKit h1 35.7px / 42px `@media (min-width: 960px)` + host `h1.detailTitle` reset (`gulp test` PASS); **title width:** classic `col-md-10` wrap (`gulp test` PASS); live visual QA pending. Card lines + paginationBox sprite = code (live visual QA pending). KH visual QA pending |
| Raster → WebP (same px) | ship sppkg ~1.5 MB | Path: `project-saral-SPFX/sharepoint/solution/project-saral-spfx.sppkg` v`1.0.0.7` rebuilt 25 Aug 12:04 (`gulp clean` + `--ship`; includes Repo `pill-x` + lookup Titles + CH `env=WebView`/`itemId`) |
| CSV List Importer — list columns preview | STEP 3 implemented · gulp test PASS | Step 2 schema until CSV; Title + InternalName + Type + Required |
| CSV List Importer — Repo import 400 / Title | STEP 3 implemented · gulp test PASS | GUID `{}` strip + getbyid 400 retry; Title from compact title/documenttitle. Live re-import pending |
| CSV List Importer — Area of concern → Details_on_area_of_concern | retargeted · gulp test PASS | Target is ProjectSaral Clearing House Repository, not Details list / not classic |
| Page-load overlay (all WPs) | STEP 3 · gulp test PASS · live visual QA pending | Shared `PageLoading` (classic `#fff` + bounce, no logo). KH / CH / Repo listing+detail / CSV `loadingLists`. Detail 500ms hold kept. |

## Suggested order
1. App catalog upload `1.0.0.7` + Enable (`sharepoint/solution/project-saral-spfx.sppkg`; ignore Teams add error)
2. **Project Saral → Site contents → Add/update app** (required for AC; WP fallback still needs new assets)
3. Live WebView smoke (no debug) on knowledge-hub + clearing-house + repository (include CH idea → detail)
4. Optional local: `gulp serve --config the-clearing-house-repository` — card hover overlay (no white spacer line) + card lines + paginationBox sprite
5. Optional: csv-list-importer → target Clearing House Repository → Import (once) → AllItems.aspx
6. Resume parity slices per PARITY.md
