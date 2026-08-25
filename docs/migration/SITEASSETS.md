# Site assets + host modes (project-saral)

No hardcoded site path. Classic vs SPFx asset strategy differs — bulk baseline wires structure first; asset parity is Wave 4.

## Classic tree

```
project-saral-classic/
  *.aspx
  project-saral/
    assets/css/     shared, components, knowledge-hub, k-comms, kiasu, individual, uikit
    assets/js/      page scripts, apiclass, spbase, uikit
    assets/fonts/   OpenSans
    assets/img/
    components/     navigation.html, footer.html, hamburger-menu.html
```

Relative paths under `project-saral/` are classic SoT.

## SPFx policy (this repo)

| Asset type | Location |
|------------|----------|
| Page UI tokens | `*.module.scss` + `src/shared/styles/classicGlobal.scss` — clone values, do not embed full vendor CSS |
| Small bundled images | `src/webparts/<Wp>/assets/` |
| Large / shared images | `{web.serverRelativeUrl}/SiteAssets/...` via `pageContext` |
| Vendor libs | Prefer Fluent v8 / built-ins — **ask** before copying jQuery/UIKit min bundles |

**In sppkg:** React components, module SCSS, small assets.  
**Not in sppkg by default:** full `uikit.css`, Bootstrap, jQuery min.

## Host modes (per web part)

This repo = **one WP per classic page**, not one hub router.

### A — Single Web Part (Site Page)

1. Place WP in **full-width** section on modern page.
2. Manifest: `"supportedHosts": ["SharePointWebPart", "SharePointFullPage"]`, `"supportsFullBleed": true`.
3. Runtime: unlock canvas ancestors (width + height/overflow) if `.ms-SPLegacyFabricBlock` clips (~450px).
4. `ResizeObserver` → sync host `minHeight`; clear on dispose.

### B — Single-page app (Full Page)

1. Site page → Single-page app → one WP per route (separate WPs, not one router).
2. `SharePointFullPage` host — unlock optional fallback if canvas still clips.

Detail: `.cursor/skills/classic-to-spfx-migration/references/host-modes.md`

## Resolvers

- Web-relative URLs from `this.context.pageContext.web.serverRelativeUrl`
- No hardcoded `/sites/.../project-saral`
- Image rewrite helpers must use pageContext, not classic `config.baseSpUrl`

## Bulk baseline smoke

- [ ] Each WP in PARITY table has manifest + bundle entry + serve config
- [ ] `gulp bundle` pass
- [ ] Served page loads without console errors
- [ ] Full-width section tested on at least one route
- Visual parity **not** required for baseline sign-off

Classic `.aspx` stays production until PARITY Status = **parity PASS** for that route.
