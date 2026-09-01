# SiteAssets + runtime gotchas

Classic assets live under `DBS-FFW-classicsite/2025/` — compiled CSS at `style.css`, vendor/fonts under `public/`, app scripts under `public/js/`. SPFx may **bundle** page CSS/JS/thumbs in the web part; keep large vendor / fonts / images on SiteAssets when they must update without rebuild.

## Typical split (this repo)

| Where | What |
|-------|------|
| sppkg / WP `assets/` | Page SCSS, React, small thumbs already bundled |
| Property pane URLs | Optional large images / downloads — **not** bundled unless the slice requires it |
| SiteAssets (optional) | Shared images, UIKit/fonts if not bundled; `{web.serverRelativeUrl}/SiteAssets/...` from `pageContext` only |

## Resolvers

- Base = `this.context.pageContext.web.serverRelativeUrl` — no hardcoded `/sites/…`
- `assetsBaseUrl` property pane when SiteAssets (or CDN) is used
- Do not copy classic `config.baseSpUrl` (`/sites/ClassicSite/dbs-ffw`)

## CSP

- Do **not** boot classic JS via `blob:` + `createObjectURL` — SP `script-src` blocks it
- Prefer webpack chunks / React in the WP

## Remount / UIKit

If a slice still uses UIKit in the WP (avoid when React covers it):

- After DOM inject, rebind hover / modal / offcanvas; dispose listeners on unmount
- UIKit `uk-*` visual values → `uikit-to-spfx-visual-parity` (do not load full `uikit.min.css`)

## Flash / blank

| Symptom | Fix |
|---------|-----|
| Flash then empty | Host height/overflow unlock + minHeight sync (`host-modes.md`) |
| Content clipped at ~450px | `.ms-SPLegacyFabricBlock` overflow unlock |
| Mobile offcanvas dead | Unlock overflow/transform parents; portal to `body` if needed |

## Smoke (minimum)

- [ ] Images resolve (bundled, SiteAssets, or property-pane URL)
- [ ] No blob CSP errors
- [ ] Full-width section: no 450px clip
- [ ] Hover / modal still work after navigation
