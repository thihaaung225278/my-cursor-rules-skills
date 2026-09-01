# Site assets (DBS-FFW)

No hardcoded site path. Classic vs SPFx trees differ. Visual SoT year = **2025**.

## Classic

```
DBS-FFW-classicsite/
  2025/                  current live year (SoT)
    index.aspx
    past-events.aspx
    back-door.aspx
    style.css
    events.json / events-current.json / post-event.json
    participants.json / winnerlists.json
    sass/                style.sass, _home, _fonts
    public/
      css/vendor/        uikit.min.css, swiper*.css
      css/               hamburgers.min.css
      js/controller/     indexController.js, indexControllerPastEvent.js, winnerController.js
      js/lib/            common-lib.js, lib.js
      js/spbase/         sprestlib-php.js, config.js, jquery.SPServices.min.js
      js/vendor/         uikit, swiper, jquery, fullcalendar, lottie, anime, ical, papaparse, moment
      Fonts/opensans-condensed/
      images/
  2024/ · 2023/          prior-year copies — do not migrate unless user names them
```

## SPFx

- Page UI → `*.module.scss` (clone classic values; do not embed full `uikit.min.css` or Swiper CSS)
- Small thumbs → WP `assets/` when already bundled
- Optional SiteAssets: `{web.serverRelativeUrl}/SiteAssets/...` via `pageContext` + `assetsBaseUrl`

### Ffw2023 (`2023/index.aspx`) — bundled images + SiteAssets iCal

Images, fonts, JSON, and Lottie ship inside the **Ffw2023** sppkg. Schedule **.ics** downloads are served from **Site Assets** (not bundled — keeps sppkg small).

```
src/webparts/ffw2023/assets/
  img/**/*.webp          ← resized WebP (q78; gallery/gameshow max 1600px)
  fonts/opensans/*.woff2
  data/*.json
  lottie/**
  ffw2023AssetMap.ts     ← images + lottie only
src/webparts/ffw2023/utils/ffw2023SiteAssetUrls.ts
```

One-time iCal upload (after `npm run prepare:ffw2023-assets`):

```
sharepoint/siteassets-staging/FFW2023/iCal-invites/**  →  Site Assets library /FFW2023/iCal-invites/
```

Default download URL: `{web}/SiteAssets/FFW2023/iCal-invites/...` (override in web part property pane).

Regenerate after classic asset changes:

```bash
cd DBS-FFW-SPFX
npm run prepare:ffw2023-assets
gulp bundle
```

Property pane: `galleryDownloadUrl` only (external SharePoint folder for Download All).

Detail: `.cursor/skills/classic-to-spfx-migration/references/host-modes.md` · `siteassets-gotchas.md`.
