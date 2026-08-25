# Site assets (project-saral)

No hardcoded site path. Classic vs SPFx trees differ.

## Classic

```
project-saral-classic/
  knowledge-hub.aspx
  the-clearing-house.aspx
  the-clearing-house-repository.aspx
  export-import.aspx
  splists/
  project-saral/
    assets/css/          shared, components, knowledge-hub, k-comms, kiasu, individual, uikit
    assets/js/           scripts, apiclass, spbase, uikit
    assets/fonts/        OpenSans
    assets/img/
    components/          navigation.html, footer.html, hamburger-menu.html
```

## SPFx

- Page UI → `*.module.scss` (clone classic values; do not embed full `uikit.css` or Bootstrap)
- Small thumbs → WP `assets/` when already bundled
- Optional SiteAssets: `{web.serverRelativeUrl}/SiteAssets/...` via `pageContext` + `assetsBaseUrl`

Detail: `references/host-modes.md` · `references/siteassets-gotchas.md`.
