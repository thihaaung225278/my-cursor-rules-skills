# Host modes — Full Width WP + Single-page app

This repo ships **one web part per classic page** (Home, Step1, Reporting, …), not a single hub with `pageKey`. Each WP that must match classic page width uses the same host contract.

## Manifest (already on Step1 / Reporting / Home as shipped)

```json
"supportedHosts": ["SharePointWebPart", "SharePointFullPage"],
"supportsFullBleed": true
```

Do not drop `supportsFullBleed` on a clone WP. Workbench-only width is not Visual PASS.

## A — Single Web Part (Site Page)

1. Editor: place the part in a **full-width** section (fullBleed-capable canvas).
2. Runtime: unlock canvas **ancestors** for:
   - **width** (canvas max-width / padding)
   - **height + overflow** (`.ms-SPLegacyFabricBlock` ~450px clip → flash-then-blank / clipped scroll)
3. `ResizeObserver` → sync host `minHeight` to content root height. Dispose on unmount.
4. CSS `width:100%; max-width:none` **only if** unlock found **no** ancestors — do not stack `100vw` ±50% breakout on unlock.
5. On dispose: clear unlock attributes / inline overrides.

## B — Single-page app (Full Page)

1. Site page → **Single-page app** → one WP per route (this repo: separate WPs, not one router).
2. Form factor FullPage via `SharePointFullPage`.
3. **No** parent unlock by default. Keep unlock as fallback if canvas still clips after deploy.

## Do / Don't

| Do | Don't |
|----|-------|
| Smoke full-width **section** on a modern page | Assume `supportsFullBleed` CSS alone fixes the canvas |
| Unlock height/overflow, not only width | Leave FabricBlock 450px lock |
| Smoke WP full-width **and** SPA if both are used | Claim full width after workbench-only check |

## Smoke

- Full-width section → content matches classic width; long pages scroll; no 450px clip
- SPA (if used) → no double chrome if product requires hide (`references/site-chrome.md`)
- Hard refresh after `.sppkg` update
