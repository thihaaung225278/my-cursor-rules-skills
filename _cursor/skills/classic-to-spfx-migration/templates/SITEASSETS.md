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

Detail: `references/host-modes.md` · `references/siteassets-gotchas.md`.
