# active_context — DBS-FFW

> Agent: session start မှာ ဤဖိုင် + `progress.md` ကို Read ပြီး တိုက်ဆိုင်။ Stale မထားရ။ Secrets မထည့်ရ။

**Updated:** 2026-08-31 (ship v1.0.0.10 — classic favicon)

## Goal

Classic SharePoint site (`DBS-FFW-classicsite/`) → SPFx (`DBS-FFW-SPFX/`) feature-by-feature migrate။

**Scope (user-confirmed):** **2023 + 2024 + 2025** — all year folders. Visual SoT **per slice** = that year's `style.css` + `sass/` (`classic-visual-parity`).

## Pins (do not drift)

| Item | Value |
|------|--------|
| SPFx | 1.20.x |
| Toolchain | gulp (`gulp bundle` / `gulp serve` / `gulp test`) |
| React | 17 |
| UI | Fluent UI v8 (`@fluentui/react`) |
| Node | `>=18.17.1 <19.0.0` |
| Skills entry | `classic-to-spfx-migration` → then `classic-visual-parity` / `uikit-to-spfx-visual-parity` / `spfx` |
| Rules | `.cursor/rules/04-sharepoint-standards.mdc` · `17-classic-host-and-assets.mdc` |

## Paths

| Role | Path |
|------|------|
| Classic | `DBS-FFW-classicsite/` (`2023/` · `2024/` · `2025/`) |
| SPFx | `DBS-FFW-SPFX/` |
| Skills | `.cursor/skills/` |
| Memory | `active_context.md`, `progress.md`, `docs/migration/PARITY.md` |

## Current slice

- **Focus:** Classic **favicon** on all live SPFx WPs (Ffw2023 · PostEvent2023 · Ffw2024 · Ffw2025)
- **Status:** Mode B **STEP 3 Implement done** · favicon wired · **parity PASS မဟုတ်** (tab icon live smoke = you; restart `gulp serve` so gulpfile `.ico` rule loads)
- **Classic SoT:** `<link rel="icon" href="favicon.ico" type="image/x-icon" />` on live ASPX heads; same ICO all years (MD5 `a4fb4156418cd12bf9872bed68b375fc`, 32 KB)
- **SPFx gap:** closed in code — `classicHostUnlock` sets `rel=icon` + restore on dispose; live tab smoke pending serve restart
- **Package:** `sharepoint/solution/dbs-ffw-spfx.sppkg` **v1.0.0.10** (~7.7 MB — Ffw2023 + PostEvent2023 + Ffw2024 + Ffw2025 + classic favicon)

## Handoff (files win — see `.cursor/rules/13-context-handoff.mdc`)

### DONE
- **Ship v1.0.0.10** — `npm run ship`; AppManifest Version=1.0.0.10; ~7.7 MB; includes classic favicon ICO + Ffw 2025 + Ffw 2024 + Ffw 2023 + Post Event 2023. gulp serve stopped for ship.
- **Mode B STEP 3 Implement (favicon)** — Option A: copied classic ICO to `src/shared/host/favicon.ico`; gulpfile `.ico` `asset/resource` + `copyStaticAssets`; `unlockClassicHost` apply/`refresh`/`dispose` restore. ၄ WP already call unlock. No TSX/SCSS/title/AC/Yeoman/new deps. `gulp bundle` exit 0 (Ffw2023 pre-existing `no-new-null`). Live tab icon = **you** after **restart** `gulp serve` (running serve still has old gulpfile — webpack `Can't resolve './favicon.ico'` until restart).
- **Mode B STEP 2 Plan (favicon)** — Selected Path Option A: copy one classic ICO into `src/shared/host/favicon.ico`; webpack `asset/resource` for `.ico` (gulpfile — like `.ics`); apply + restore inside `unlockClassicHost`/`dispose` (၄ WP already call). No per-WP ICO copy. No AC / title / new deps / Yeoman / TSX / SCSS. Fallback = PNG `rel=icon` if webpack rejects ICO.
- **Mode B STEP 1 Scout (favicon)** — Classic live ASPX (`2023/index.aspx`, `2023/post-event.aspx`, `2024/index.aspx`, `2025/index.aspx`) all set `<link rel="icon" href="favicon.ico">`. Year ICO files identical. SPFx 4 WPs have **no** favicon/`document.head` handling. Shared hook = `classicHostUnlock` (BG only). AC မတောင်း။
- **Ffw2025 gulp serve** — `ffw2025` config = `index2025.aspx?env=WebView&loadSPFX=true`. Serve started then **user-aborted**. Re-run: `gulp serve --config=ffw2025`.
- **Ffw2025 schedule opacity** — classic compiled `.contents { opacity: 1 }` beats `.check-past { opacity: 0.4 }`. Over-specific SPFx 0.4 ဖြုတ်။ Card BG `#fff`. `gulp bundle` exit 0.
- **Ship v1.0.0.9** — `npm run ship`; AppManifest Version=1.0.0.9; ~7.4 MB; includes **Ffw 2025** + Ffw 2024 + Ffw 2023 + Post Event 2023. gulp serve stopped for ship.
- **Mode B STEP 3 Implement** — Option A **Ffw2025** WP: live About + 3-col text Highlights + GIF gallery + Schedule (`events-current.json` flatten+sort+group; Watch playback; `check-past`). Host `#284055` + BG webp. GIF keep. Condensed fonts. No Yeoman / post-event / calendar / Swiper / Lottie / FullCalendar / new deps. `Ffw2023*` / `Ffw2024*` / `PostEvent2023*` မထိ။ `gulp bundle` exit 0 (Ffw2025 lint clean; Ffw2023 pre-existing `no-new-null`).
- **Mode B STEP 2 Plan** — Selected Path Option A: new **Ffw2025** WP (copy-adapt Ffw2024 folder; **no Yeoman**). Live uncommented `2025/index.aspx` only: About + 3-col **text** Highlights + GIF gallery + `#schedule` (events-current.json flatten+sort+group; Watch playback; “What's Happening in”). Host `#284055`. No `body.video-playbacks`. No post-event / calendar / category tabs / Lottie / Swiper / FullCalendar. No new npm deps. `Ffw2023*` / `Ffw2024*` / `PostEvent2023*` မထိ။ Fallback = skip GIF convert; serve `index2025.aspx` missing → workbench note.
- **Mode B STEP 1 Scout** — `2025/index.aspx` live = `.pre-during-event-sec` (About LFC 2025 + 3 text Highlights + `MICROSITE.gif` gallery + `#schedule` country dropdown). `.post-event-sec { display: none }` (style.css:1593). Boot script = `indexController-current.js` (not `indexController.js` / `home.js` / `winnerController.js`). Data = `events-current.json` (sg/cn/hk/in/id/tw/ics). `renderEvents` (2414): after 2025-07-04 reveal → flatten+sort all events into `.tab-content` (no `#calendar` / `#category_tabs` in ASPX). Today 2026-08-31 → all events `isPast` → Watch playback. Host `#284055`. Fonts = OpenSans-Condensed-*. **Ffw2025 WP မရှိ** — clone template = Ffw2024. `Ffw2023*` / `Ffw2024*` / `PostEvent2023*` မထိရ။
- **Ffw2024 `.desc a` underline** — classic `2024/style.css` `.desc a` has color `#b12c32` only (no underline). SPFx host was painting underline on iTQ/eCards. Added `text-decoration: none` + `border-bottom: none` on `.desc a` + hover/focus/visited. TSX / `Ffw2023*` / `PostEvent2023*` မထိ။ `gulp serve --config=ffw2024` watch rebuild OK (sass+webpack; Ffw2023 pre-existing `no-new-null`).
- **Mode B STEP 3 Implement** — Option A: `Ffw2024.module.scss` `.tab-content .tab-pane` port (`padding: 30px` + `#fff` + `border-radius: 12px` + `margin-bottom: 10px` + `margin: 0 auto` + `gap: 15px`). `.contents` `30px` ထား။ TSX / `Ffw2023*` / `PostEvent2023*` မထိ။ `display: none` / dead `padding-bottom: 40px` မထည့်။ `gulp bundle` exit 0 (Ffw2024 lint clean; Ffw2023 pre-existing `no-new-null`).
- **Mode B STEP 2 Plan** — Selected Path Option A: `Ffw2024.module.scss` မှာ classic compiled `.tab-content .tab-pane` ကို verbatim port (`padding: 30px` + `#fff` + `border-radius: 12px` + `margin-bottom: 10px` + `margin: 0 auto` + `gap: 15px`). `.contents` `30px` မဖြုတ်။ TSX / `Ffw2023*` / `PostEvent2023*` မထိ။ `display: none` on pane မထည့် (cards ပျောက်မည်)။ `padding-bottom: 40px` dead rule မကူး။ Fallback = live classic ~30px သာမြင်ရင် Option C (`.contents` padding `0`)။
- **Mode B STEP 1 Scout** — Ffw2024 `#video-playbacks` card padding: `.contents` `padding: 30px` + inner tokens (`.desc` 20px, left/right `padding-top: 5px`, `.tab-content` `20px 0`, 640 `padding-top: 30px`) **match**. Classic `.tab-content .tab-pane` also has `padding: 30px` + white card chrome (`background` / `border-radius: 12px` / `margin-bottom: 10px`) — **SPFx missing** that rule. Effective classic inset ≈ **60px** (pane 30 + contents 30); SPFx ≈ **30px**. `_home.sass` still has `.tab-content` `52px 47px` + pane `display:none` — live SoT = compiled `style.css` (`20px 0`, no pane `display:none`). Markup both = `.tab-pane` > `.contents.has-video.uk-flex`. `Ffw2023*` / `PostEvent2023*` မထိ။
- **Mode B STEP 3 Implement** — Option A Ffw2024 Video Playbacks: `flattenEventsByDate` inside `groupPlaybackEvents`; `renderPlaybackContent` allowlist (`br` + https `<a>` + `see-it.png` `<img>`); PNG bundled (not WebP); `.desc a` `#b12c32` + `.desc img` `padding-top: 20px`. No `external_link` CTA. `Ffw2023*` / `PostEvent2023*` မထိ။ `gulp bundle` exit 0 (Ffw2024 lint clean after regexp fix; Ffw2023 pre-existing `no-new-null`).
- **Mode B STEP 2 Plan** — Selected Path Option A: flatten-by-date (`getEvents` uniqueDates first-seen → bucket → flat) then existing `groupPlaybackEvents`; allowlist `.desc` renderer (`br` + `https` `<a>` + `see-it.png` `<img>` via `resolveFfw2024Image`); bundle `see-it.png` (PNG copy if WebP soft); port `.desc a` `#b12c32` + `.desc img` `padding-top: 20px`. No DOMPurify. No `external_link` right-cta (classic live empty). `Ffw2023` / `PostEvent2023` မထိ။ Fallback = skip img if asset missing; sort-by-date if flatten still mismatches.
- **Mode B STEP 1 Scout** — Ffw2024 `#video-playbacks`: (1) sort ≠ classic because SPFx `groupPlaybackEvents` uses raw JSON order; classic `filterEvents` flattens `getEvents()` date buckets first (late CheckIds with earlier dates pulled back). (2) Missing screenshot block is **Staff Appreciation Week** `.desc` HTML (`<a>` iTQ/eCards + `<img src="public/images/2024/see-it.png">`), stripped by `renderBrText` (br-only). `see-it.png` not in `FFW2024_IMAGE_MAP` / `LIVE_STILLS`. `.desc a` / `.desc img` CSS not in `Ffw2024.module.scss`. Not a separate footer. `Ffw2023` / `PostEvent2023` မထိ။
- **`serve.json` ffw2024** — `pageUrl` ကို `SitePages/index2024.aspx?env=WebView&loadSPFX=true` သို့ ပြောင်း (`ffw-2024.aspx` မဟုတ်)။ `npm run serve:ffw2024` ရှိပြီး။
- **Ship v1.0.0.8** — `npm run ship`; AppManifest Version=1.0.0.8; ~6.4 MB; includes **Ffw 2024** + Ffw 2023 + Post Event 2023. gulp serve stopped for ship.
- **Mode B STEP 3 Implement** — Option A **Ffw2024** WP: live About + 3-col Highlights + GIF gallery + Video Playbacks. Host `#284055`. WebP stills q78 / highlights 1600px. GIF keep. Condensed fonts. `events.json` bundled. `Ffw2023*` / `PostEvent2023*` မထိ။ `gulp bundle` exit 0 (Ffw2024 lint clean; Ffw2023 pre-existing `no-new-null`).
- **Mode B STEP 2 Plan** — Selected Path Option A: new **Ffw2024** WP, live uncommented `2024/index.aspx` only (About + 3-col Highlights + GIF gallery + Video Playbacks). Host `#284055`. WebP stills q78 max 1600 (logo 1620 keep). GIF keep. No Swiper. No post-event-sec. `Ffw2023` / `PostEvent2023` မထိ။ Fallback = skip highlight resize if cwebp fails (copy original) / skip GIF convert.
- **Mode B STEP 1 Scout** — `2024/index.aspx` live SoT = `body.video-playbacks` + `.pre-during-event-sec` (About thank-you + 3-col Highlights + Gallery GIF + Video Playbacks). `.post-event-sec { display:none }`. Mobile/Lottie/footer commented. Fonts = OpenSans-Condensed-* (compiled CSS). Host paint `#284055` not 2023 peach. Images exist on disk (cursorignore). No Ffw2024 WP yet.
- **Ship v1.0.0.7** — `npm run ship`; AppManifest Version=1.0.0.7; ~4.9 MB; includes PostEvent `#game_show_winners` slider strip + Ffw 2023. gulp serve stopped for ship.
- **Mode B STEP 3 Implement** — Option A: `PostEventGameShowWinners` မှ `ClassicSwiper` + `DEFAULT_SLIDES` ဖြုတ်။ Dropdown-above-card + 2×2 finals + `renderPrizeTitle` + semi-final. Online Winners heading မထည့်။ `GameShowWinnersSection.tsx` / `Ffw2023.tsx` / `Ffw2023.module.scss` မထိ။ `gulp bundle` exit 0 (PostEvent lint clean; Ffw2023 pre-existing `no-new-null`).
- **Mode B STEP 2 Plan** — Selected Path Option A: `PostEventGameShowWinners` မှ `ClassicSwiper` + `DEFAULT_SLIDES` ဖြုတ် (classic slide JS commented / screenshot မှာ photo မရှိ)။ Dropdown-above-card + 2×2 finals + `renderPrizeTitle` + semi-final data ရှိရင် ထား။ Online Winners empty heading မထည့်။ `GameShowWinnersSection.tsx` / `Ffw2023.tsx` / `Ffw2023.module.scss` မထိ။ Fallback = empty `.winner-slider` wrapper (slides/nav မပါ) ပြန်ထည့်။
- **Mode B STEP 1 Scout** — PostEvent `#game_show_winners` vs classic `2023/post-event.aspx`: dropdown already above card; SPFx still injects `ClassicSwiper` + `DEFAULT_SLIDES` (classic slide JS commented — empty wrapper → no 500px photo). SoT = title + centered `#select_country` + white `card-wrap` 2×2 finals (`renderPrizeTitle` + `post-event.json`). Do not touch `GameShowWinnersSection.tsx` / `Ffw2023.tsx`. Semi-final JS still runs (keep). Online-winners JS commented (omit empty heading unless STEP 2 says otherwise).
- **Mode B STEP 3 Implement** — Option A: `PostEventSchedule` = classic `renderEventList` (`.tab-content`, all events, `.contents.check-past`, left time, title+`past` span, save-the-date via `resolveFfw2023IcalUrl`). `video_link` Watch / `.past-event-tab-content` / React `hidden` ဖြုတ်။ `PostEvent2023.tsx` `icalBaseUrl` ပို့။ `Ffw2023.tsx` / `ScheduleSection` / `VideoHighlightsSection` မထိ။ Join-live မပါ။ `gulp bundle` exit 0 (PostEvent lint clean; Ffw2023 pre-existing `no-new-null`).
- **Mode B STEP 2 Plan** — Selected Path Option A: `PostEventSchedule` ကို classic `post-event.aspx` `renderEventList` ပြန်ချိန် (`.tab-content` + all events + left time + save-the-date + `check-past`; `hidden` ဖြုတ်; `video_link` Watch မဟုတ်)။ Join-live / `getWebexLink` (ICAL) မဆွဲ။ `icalBaseUrl` ကို `PostEvent2023` → schedule ပို့။ `Ffw2023.tsx` / `ScheduleSection` / `VideoHighlightsSection` မထိ။ Fallback = `hidden` ဖြုတ် + `.tab-content` အရင်၊ Watch filter မထား။
- **Mode B STEP 1 Scout** — User မှန်: `PostEventSchedule` က index `#video_highlights` / `renderPastEvent` (`.past-event-tab-content` + `video_link` Watch) ကို `#schedule` ထဲ ထည့်ထား။ Classic `post-event.aspx` `#schedule` SoT = `renderEventList` → `ul.tabs` + `#schedule-dd` + `.tab-content` + `.contents` (left time + save-the-date / join-live)။ `renderPastEvent` က index `#video-highlight-dd` သာ။ Empty white box = `.tab-pane { display:none }` + extra React `hidden` နှင့်/သို့ parent `.tab-content` မဟုတ်။ Taiwan Day 1 JSON မှာ `video_link` ရှိ — data-empty မဟုတ်။ `Ffw2023.tsx` / `ScheduleSection.tsx` မထိရ။
- **Mode B STEP 3 Implement** — Option A: `PostEventSchedule.tsx` (`#schedule`, title Schedule, tab-menu → timezone → `.contents` + `video_link` Watch playback). `PostEvent2023.tsx` မှာ `ScheduleSection` ဖြုတ်. `ScheduleSection.tsx` / `Ffw2023.tsx` မထိ။ Named-face `font-weight: 400` on tabs / `.text-intro span` / title / playback `<a>`. `gulp bundle` exit 0 (PostEvent lint clean; Ffw2023 pre-existing `no-new-null`).
- **Mode B STEP 2 Plan** — Selected Path Option A: PostEvent-only `PostEventSchedule` (`id="schedule"`, title Schedule, tab-menu → timezone → `.contents` playback cards). `ScheduleSection` / `Ffw2023.tsx` မထိ။ Fallback = inner classes ကို `past-event-tab` သို့ ပြောင်း။
- **Mode B STEP 1 Scout** — PostEvent2023 `#schedule` reuses Ffw2023 pre-during `ScheduleSection` (save-the-date / `schedule-card` / no timezone / no Day N). Classic `post-event.aspx` keeps `#schedule` + title Schedule (nav About/Highlights/Schedule). Post-event card SoT = `indexController.renderPastEvent` (`.contents` + `video_link` + Watch playback). `Ffw2023.tsx` hides `#schedule` in post-event and shows `#video_highlights` instead — different page.
- **`.overlay::before` overlay.png** — user override: restored bundled `url('../assets/img/overlay.webp')` (classic `public/images/overlay.png`). `background-image: none` ဖြုတ်။ `gulp bundle` OK.
- **Mode B STEP 2 Plan** — Selected Path Option A: CSS-only `#highlight` nth-child + named-face weight. Overlay မပြန်တင်။ `uk-grid-margin` class မထည့်။
- **Mode B STEP 1 re-scout (color+gap)** — Gap V missing (`uk-grid-margin` / `#highlight` nth-child). Card **photo** RGB WebP≈PNG (Δ≤1). `overlay.png` = opaque `#000` 900×500 under `.bg-image`. SPFx `.overlay::before { background-image: none }` = visible-equivalent; **do not** stack overlay on top. Title/SemiBold `font-weight: 400` still missing.
- **Ship v1.0.0.6** — `npm run ship`; AppManifest Version=1.0.0.6; ~4.7 MB; includes **Post Event 2023** + **Ffw 2023**. gulp serve stopped for ship.
- **PostEvent2023 STEP 3 compose** — Option A: page-specific banner/nav (About/Highlights/Schedule), 10Jul highlights, winners dropdown-above-card, lucky-draw empty chrome; reuse Lottie/About/Schedule/Footer + Ffw2023 CSS/data. `Ffw2023.tsx` untouched. gulp serve tsc+webpack OK (PostEvent lint clean; Ffw2023 pre-existing `no-new-null` warnings)
- **PostEvent2023 STEP 1 Scout** — classic `post-event.aspx` ≠ Ffw2023 `index.aspx` post-event mode (menu 3 links; Highlights 10Jul 4 cards; About = pre-event copy; no date-gate wrappers; participants `uk-hidden`; lucky-draw JS commented; no gallery/video)
- **PostEvent2023 stub** — `PostEvent2023.tsx` region placeholders only; host unlock without `#FFE5D4`; `serve.json` `postEvent2023` → `SitePages/post-event.aspx`
- `.cursor` rules + skills + hooks
- Codegraph: **all years** indexed
- `PARITY.md` ↔ `progress.md` — full 2023/2024/2025 inventory
- **Ffw** Yeoman scaffold removed (placeholder only; 2025 → **Ffw2025** TBD when slice starts)
- **Ffw2023** functional migrate for `2023/index.aspx` (sections, country dropdowns, 2023 CSS `:global` port)
- **Ffw2023 bundled assets** — project-saral pattern: 53 WebP (q85, same px), fonts SCSS, JSON + 166 iCal in sppkg; SiteAssets not required
- **Ffw2023 ship package v1.0.0.5** — `npm run ship`; includes menu hash/anchor; AppManifest Version=1.0.0.5
- **Ffw2023 hero Lottie** — `lottie-web` + 11 bundled JSON; `LottieLayer` wired (classic `common.js` parity); `MobileNav` gated on `showPostEvent`
- **Ffw2023 hero logo + banner-text CSS** — `Ffw2023.module.scss`: UIKit `img` global, `.image img { width:100% }`, date/description `font-weight:400`
- **Ffw2023 hero layout anchor** — badge relocated into `page-banner`; removed `.ffw2023Root position:relative`; badge `max-width:none`; menu always-in-DOM + CSS hide (classic jQuery parity)
- **Ffw2023 mobile post-event navbar** — fixed overlay (no flow space); `uk-hidden@m` fix; classic menu-icon CSS; `scrollToClassicAnchor`; overlay scroll opacity
- **Typography self-check gate** — `visual-typography.md` expanded; mandatory in `classic-visual-parity` + `classic-to-spfx-migration` + rules `17`/`19` (named-face `font-weight: 400`, menu link underline, checklist table before parity PASS)
- **Ffw2023 post-event menu underline** — desktop `.menu ul li a`: `text-decoration: none` + `border-bottom: none` on base/hover/focus/visited (SharePoint link inherit fix; classic visual = no underline)
- **Ffw2023 post-event menu font-weight** — desktop `.menu ul li a` + mobile `.page-menu` / `#m-menu` links: `font-weight: 400` on OpenSans-Bold (classic parity; host inherit fix)
- **Ffw2023 section title stars** — `.main-title::before/::after` restore `star.webp`; desktop `top: 50%` + `translateY(-50%)` vertical center; mobile `::before` above title (`top: -47px`) unchanged
- **Ffw2023 UIKit h2 line-height** — `h2 { line-height: 1.3 }` (UIKit port; fixes root 28px inherit on `.main-title`); skill gate in `visual-typography.md` Step 3b + `uikit-to-spfx-visual-parity`
- **Ffw2023 body copy font-weight** — `.ffw2023Root` + `p { font-weight: 400 }` (card-wrap / post-event copy vs classic); skill gate `visual-typography.md` Step 3c
- **Ffw2023 Swiper carousels** — `swiper@14` + `ClassicSwiper`; gallery + winner wired; nav classic **swiper-icons** `:after` 35px (SVG hidden), box `content-box` 27×44 + pad 32
- **Ffw2023 game show dropdown + winners grid** — `CountryDropdown`: document mousedown outside-close + `onMouseDown` select (classic `common.js` parity); `#game_show_winners` dropdown center `display:block`, winner-listing text-align; Bold-face `font-weight:400` on `.selected-option` / `.winner-title` / `.team-name`
- **Ffw2023 game show winners UIKit grid spacing** — `.uk-grid > .uk-grid-margin` row gap; nth-child row gaps; global `@1200` gutter 40px; **`.winner-listing.uk-grid` / `.semi-final-listing.uk-grid` padding restored after UIKit `padding:0` reset** (classic cascade); typography `h3` 1.4 + prize/members line-height
- **Ffw2023 lucky draw winners** — `LuckyDrawAndFooter.tsx`: Participation (14) + Metaverse (40) blocks in one `card-content`; `LuckyDrawBlock` helper; SCSS `#lucky_draw_winner h3` `font-weight:400` + `.futureforward-week ul` list reset
- **Ffw2023 footer host-gap background** — `classicHostUnlock` optional `pageBackground`; Ffw2023WebPart paints `#FFE5D4` on canvas ancestors + `#spPageCanvasContent` + `body`/`html` (classic `body, html` parity); restore on dispose
- **Ffw2023 gallery Download All + playback icons** — `Ffw2023.module.scss`: `.download-all-btn a` + `.right-content a` SharePoint underline inherit fix; restore `::before` icons (`btn_playback`, `btn_calendar`, `btn_watch` + inactive/check-past variants); `ScheduleSection` save-date = classic `::before` only (removed duplicate `<img>`)
- **PostEvent2023** baseline for `2023/post-event.aspx`
- `config/config.json` bundles + `serve.json` serveConfigurations stubs
- **Ffw2023 side-scroll** — `.lottie-animation` + svg `pointer-events: none` (`Ffw2023.module.scss`); `position: fixed` kept; host unlock unchanged
- **Ffw2023 menu hash/anchor** — classic `common.js` 1000ms `html`+`body` rAF + overflow-parent fallback; `preventDefault` only if target exists; reduced-motion = jump

### PARTIAL
- **Classic favicon** — code + `gulp bundle` OK. Live tab vs classic = **you**. Restart `gulp serve --config=ffw2025` (gulpfile `.ico` rule). **parity PASS မဟုတ်။**
- **Ffw2025 schedule opacity** — CSS applied. Live vs classic on `index2025.aspx` (SG Marshall Goldsmith card: full-contrast title `#b12c32`, desc `#525252`, time `#8a8a8a`, solid white card) = **you** (`npm run serve:ffw2025`). **parity PASS မဟုတ်။**
- **Ffw2025** remainder visual — **not run** this turn (Browser MCP မရှိ). Create Site Page if missing.
- **Ffw2024 Staff Appreciation `.desc a` underline** — CSS applied. Live vs classic on `index2024.aspx` = **you**. **parity PASS မဟုတ်။**
- **Ffw2024 Video Playbacks card padding** — code applied (`.tab-pane` 30px + contents 30px). Live vs classic on `index2024.aspx` = **you**. If inset looks ~2× classic, Option C (`.contents` padding `0`). **parity PASS မဟုတ်။**
- **Ffw2024 Video Playbacks** — flatten + Staff Appreciation `.desc` a/img already applied. **parity PASS မဟုတ်။**
- **PostEvent2023 `#game_show_winners`** — slider ဖြုတ်ပြီး; live vs classic screenshot (SG dropdown + 2×2) = **you** (`npm run serve:postEvent2023` already running)
- **PostEvent2023 `#schedule`** — code applied (`renderEventList`); live vs classic (SG default + Taiwan Day 1 cards) = **you** (`npm run serve:postEvent2023`)
- **PostEvent2023 Highlights `#highlight`** — uk-grid gap + overlay.webp on `.overlay::before`; live vs classic = **you** (`gulp serve --config=postEvent2023`)
- **PostEvent2023** remainder visual vs classic — **not run** this turn (Browser MCP မရှိ)
- **Ffw2023** menu hash/anchor — code applied; live click smoke = **you** on `index.aspx` debug
- App Catalog upload — **user action**

### NEXT

**This chat:** App Catalog upload = **you**. After deploy, hard-refresh a WP page and check tab icon vs classic. No parity PASS.

**Do not claim parity PASS** until 640/959 visual checklist vs classic.

**Do not claim parity PASS** until 640/959 visual checklist + typography table vs classic screenshot.

Ffw2024 remainder / PostEvent / Ffw2023 = parked (not this slice).

### Out of scope
- `mk/.cursor` hub playbook
- Heft / Fluent v9
- Hidden `.post-event-sec` on `2025/index.aspx` (game-show / lucky-draw / gallery Swiper / video_highlights) — CSS `display:none`; do not port this slice
- `2025/past-events.aspx` · `2025/back-door.aspx`
- Commented `#key-programmes` · Lottie (`common.js` commented) · FullCalendar (`#calendar` not in ASPX)
- Hidden `.post-event-sec` on `2024/index.aspx` (game-show / lucky-draw / gallery Swiper) — Option A reject
- `2024/past-events.aspx` · `2024/back-door.aspx` · `index-old.aspx` / `index-current.aspx`
- `2023/back-door.aspx` (defer)
- New npm deps (swiper already in package.json; no extra install for live GIF gallery)
- Favicon slice: `document.title` · Application Customizer · apple-touch-icon · ship version bump · Yeoman

## Context ကုန်လို့ နောက် chat

```
Continue DBS-FFW from active_context.md + progress.md.
DONE: Ship v1.0.0.10 (~7.7 MB) with classic favicon. gulp serve stopped.
NEXT: App Catalog upload (you). Live tab smoke after deploy. No parity PASS.
Pins: SPFx 1.20 gulp, React 17, Fluent v8. Reject Heft/v9, classic master, secrets, Codegraph Cursor hooks.
If context thin: update active_context handoff only — no code.
Mode B: ..chain → y → y; one STEP per y.
```
