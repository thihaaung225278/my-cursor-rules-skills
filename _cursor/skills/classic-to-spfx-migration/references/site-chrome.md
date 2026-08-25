# Site Pages chrome On/Off

This PJ’s classic chrome is **inline per `.aspx`** (no separate header/footer ASPX, no `ui-loader.js`). Do **not** copy dbs-mtj PortalShell Application Customizer or `__OMT_*` globals unless the user asks.

Use Site Pages Yes/No columns only when a **modern host page** must hide SharePoint chrome (header/footer/banner) around a full-bleed or SPA web part.

## Columns (Site Pages library) — only if user asks

| Display | Internal name (exact) | Default |
|---------|----------------------|---------|
| Show Header | `ShowHeader` | Yes |
| Show Footer | `ShowFooter` | Yes |
| Show Banner | `ShowBanner` | Yes |

- Add as **Yes/No**. Confirm internal names (no spaces).
- Omit a column if that surface does not exist.

## Semantics (fail-open)

| Value | Effect |
|-------|--------|
| Yes / blank / column missing / REST fail / timeout | **Show** that chrome |
| Explicit `false` / No only | **Hide** |

## Runtime (if columns exist)

1. Web part `onInit` → fetch via **`SPHttpClient`** (host Site Pages item)
2. Apply hide/show before paint. Fail-open if seed/REST missing
3. Columns apply to the **host Site Page** item, not in-WP routes

Do not invent list columns without an explicit user ask.

## Smoke (only after columns exist)

1. Defaults Yes → SP chrome visible
2. `ShowHeader=No` → suite/page header hidden as designed
3. Missing column → chrome still shows (fail-open)
