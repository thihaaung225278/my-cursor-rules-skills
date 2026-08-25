---
name: spfx
description: 'SharePoint Framework (SPFx) development. Use when: "create SPFx project", "new web part", "SPFx extension", "upgrade SPFx", "SPFx upgrade", "update SPFx version", "scaffold SPFx", "SPFx React", "SPFx design", "web part styling", "Fluent UI in SPFx", "PnPjs", "read SharePoint list", "call Microsoft Graph from SPFx". Covers project creation (Yeoman), upgrades (CLI for Microsoft 365), the gulp toolchain (this repo: SPFx 1.20), React web part design, and PnPjs data access. Do not use to migrate this repo to Heft.'
argument-hint: 'Describe what you need: create, upgrade, design, or data access'
---

# SPFx Development

Pick the reference(s) that match the user's intent. Load **only** what is needed and execute the steps exactly:

- **Create a project** → [create.md](./references/create.md)
- **Upgrade a project** → [upgrade.md](./references/upgrade.md)
- **Working on UI in a React SPFx project** (components, styling, layout, accessibility) → [react-design.md](./references/react-design.md). **This repo classic pages:** use `classic-visual-parity` instead of Fluent v9 / host-theme rules in that file.
- **Reading or writing SharePoint / Microsoft Graph data** → [pnpjs.md](./references/pnpjs.md)

## Global rules (apply to every SPFx task)

- **Use PnPjs by default for all SharePoint and Microsoft Graph data operations.** See [pnpjs.md](./references/pnpjs.md). Only fall back to raw `SPHttpClient`/`MSGraphClientV3` when the user explicitly requires it or a dependency cannot be added.
- **When running `npm install`, always run it synchronously with a timeout of at least 3 minutes.** SPFx projects have heavy dependency trees.

## Toolchain decision rule

SPFx switched build systems at v1.22.0. Determine the version from `.yo-rc.json` (`@microsoft/generator-sharepoint.version`) or `package.json`, then:

| Installed SPFx version | Toolchain | 
| --- | --- | 
| **v1.22.0 and newer** | **Heft** | 
| **v1.0 – v1.21.1** | **gulp** (legacy) |

**This repo:** SPFx **1.20 / gulp**. Do **not** upgrade to Heft or Fluent v9. Heft skills are not in this project — do not recreate them.
