# SiteAssets + runtime gotchas

Classic assets live under `project-saral-classic/resources/` (not `public/`). SPFx may **bundle** page CSS/JS/thumbs in the web part; keep large vendor / fonts / images on SiteAssets when they must update without rebuild.

## Typical split (this repo)

| Where | What |
|-------|------|
| sppkg / WP `assets/` | Page SCSS, React, small thumbs already bundled (e.g. Step1 `step1-second-video.jpg`) |
| Property pane URLs | Step1 videos (`video1Url`–`video3Url`) — **not** bundled |
| SiteAssets (optional) | Shared images, UIKit/fonts if not bundled; `{web.serverRelativeUrl}/SiteAssets/...` from `pageContext` only |

## Resolvers

- Base = `this.context.pageContext.web.serverRelativeUrl` — no hardcoded `/sites/…`
- `assetsBaseUrl` property pane when SiteAssets (or CDN) is used
- Do not copy classic `config.baseSpUrl`

## CSP

- Do **not** boot classic JS via `blob:` + `createObjectURL` — SP `script-src` blocks it
- Prefer webpack chunks / React in the WP

## Remount / UIKit

If a slice still uses UIKit in the WP (avoid when React covers it):

- After DOM inject, rebind hover / modal / offcanvas; dispose listeners on unmount
- UIKit `uk-*` visual values → `uikit-to-spfx-visual-parity` (do not load full `uikit.css`)

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
- [ ] Hover / video modal still work after navigation
