# Site Pages chrome toggles (DBS-FFW)

Classic pages keep **inline** chrome. Use Site Pages Yes/No columns **only** when a modern host page must hide SharePoint chrome around a full-bleed / SPA web part. Not an Application Customizer. Not required for Visual PASS of the cloned body UI.

## Columns (only if user asks)

Site Pages → **+ Add column** → **Yes/No**:

| Display name | Internal name | Default |
|--------------|---------------|---------|
| Show Header | `ShowHeader` | Yes |
| Show Footer | `ShowFooter` | Yes |
| Show Banner | `ShowBanner` | Yes |

Confirm internal names after create. Omit Banner if unused.

| Value | Effect |
|-------|--------|
| Yes / blank / column missing | Show (fail-open) |
| No | Hide |

Runtime: `SPHttpClient` on the host page item. Detail: `.cursor/skills/classic-to-spfx-migration/references/site-chrome.md`.
