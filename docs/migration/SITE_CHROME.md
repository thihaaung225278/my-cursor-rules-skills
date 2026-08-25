# Site Pages chrome toggles (project-saral)

Classic pages use **inline** chrome (`project-saral/components/*`). On modern Site Pages, chrome comes from:

1. **Primary:** SPFx **SaralChrome Application Customizer** (Top placeholder + footer host) when the site CustomAction is active  
2. **Fallback (sure path):** in-WP `PageChrome` inside Knowledge Hub / Clearing House / Feedback Repository web parts — so live pages show header/footer even if the AC is not registered yet  

`ShowHeader` / `ShowFooter` gate both paths. If the AC is already active, in-WP chrome **skips** (no double header).

## Custom chrome gate

| Display name | Internal name | Effect when Yes | Effect when No / empty |
|--------------|---------------|-----------------|-------------------------|
| Show Header | `ShowHeader` | Show custom header | Hide custom header |
| Show Footer | `ShowFooter` | Show custom footer + GoTop | Hide custom footer |

REST miss / columns missing → **fail-open** (show custom chrome).

## Why local serve works but live did not

`gulp serve --config knowledge-hub` (and other configs) injects the AC only via `serve.json` `customActions` + debug loader. That does **not** register the AC on the live site.

## SharePoint steps after this package (`1.0.0.3`)

Do these in order:

1. From `project-saral-SPFX`:
   ```bash
   gulp bundle --ship
   gulp package-solution --ship
   ```
2. Upload `sharepoint/solution/project-saral-spfx.sppkg` to the **tenant App Catalog** → Enable.  
   - “Could not add app to Teams” = ignore.  
   - Prefer **not** relying on “available to all sites” alone for the AC.
3. Open **Project Saral** site → **Site contents** → **New** → **App** → add / update **project-saral-spfx** (or “project-saral-spfx-client-side-solution”).  
   - This activates the site feature so `elements.xml` creates the SaralChrome CustomAction.  
   - If the app is already added, remove it and add again **or** use “Get it” / update after catalog replace (version `1.0.0.3`).
4. Hard-refresh (no `debug` / `debugManifestsFile`):
   - `SitePages/knowledge-hub.aspx?env=WebView`
   - `SitePages/the-clearing-house.aspx?env=WebView`
   - `SitePages/the-clearing-house-repository.aspx?env=WebView`
5. Confirm Site Pages columns **ShowHeader** / **ShowFooter** are checked (Yes) for those pages.

### Expected after step 3–4

- Header (Home / DBS logo / Menu) + footer / GoTop appear on live WebView.  
- Even if step 3 is skipped, **in-WP PageChrome** should still show chrome on pages that host the three branded web parts (after the new sppkg assets load). Step 3 remains recommended so AC owns Top chrome site-wide.

### Fallback if still missing

Register Application Customizer CustomAction on the site (CLI / PowerShell) with component id `e7a2b3c4-5d6e-4f7a-8b9c-0d1e2f3a4b5c` and the same properties as `sharepoint/assets/elements.xml`.

## Smoke

1. Checked pages → sticky nav + footer/`#GoTopBtn`
2. Unchecked → no custom chrome
3. Missing columns → fail-open show
4. `gulp serve --config knowledge-hub` → AC via serve (in-WP defers)
5. Live WebView (no debug) after sppkg + (recommended) site Add app → chrome visible
