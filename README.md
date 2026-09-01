# my-rules-skills-and-others

Gold-standard Cursor agent pack — synced from **DBS-FFW** (2026-08-31).

## Purpose

- **Reference** when upgrading other classic → SPFx migration projects
- **Copy source** for `.cursor/` rules, skills, hooks, MCP, and migration docs
- Includes live `active_context.md`, `progress.md`, and `docs/migration/` from DBS-FFW so you can re-read the full handoff example

## Contents

| Path | Description |
|------|-------------|
| `_cursor/rules/` | 15 active rules (+ 5 archived dead stacks) |
| `_cursor/skills/` | 17 skills (incl. `swiper-to-spfx-carousel`) |
| `_cursor/hooks/` | sessionStart + preCompact + stop handoff loop |
| `_cursor/hooks.json` | Hook event wiring |
| `_cursor/mcp.json` | Codegraph MCP (`codegraph` + `${workspaceFolder}`) |
| `active_context.md` | DBS-FFW handoff example (Goal · Pins · DONE · NEXT · paste block) |
| `progress.md` | DBS-FFW slice inventory + suggested order |
| `codegraph.json` | DBS-FFW index excludes (retarget per project) |
| `docs/migration/` | PARITY · SITEASSETS · SITE_CHROME templates |

## Pins (all classic → SPFx projects)

| Item | Value |
|------|--------|
| SPFx | 1.20.x |
| Toolchain | gulp (not Heft) |
| React | 17 |
| UI | Fluent UI v8 |
| Reject | Heft/v9, classic master, secrets in chat, Codegraph Cursor hooks |

## Deploy to a new project

1. Copy pack into project root:
   ```bash
   cp -R my-rules-skills-and-others/_cursor/ /path/to/PROJECT/.cursor/
   ```
2. **Retarget paths** in rules `06`, `07`, `15`–`19`, `12` and skills (`classic-to-spfx-migration`, `classic-visual-parity`, etc.)
3. Copy `docs/migration/` and rewrite `PARITY.md` for that site's routes
4. Create project-specific `active_context.md` + `progress.md` (use DBS-FFW files here as format reference)
5. Copy `codegraph.json` and adjust `exclude` for `{PROJECT}-classicsite/` and `{PROJECT}-SPFX/`
6. Run `codegraph init` in the project workspace root

## `_cursor` vs `.cursor`

This repo uses **`_cursor/`** so Cursor does **not** auto-load rules when the monorepo root is open.

Real migration projects use **`.cursor/`**. After deploy, `hooks.json` paths (`.cursor/hooks/...`) match the live folder name.

**Do not** open `my-rules-skills-and-others` alone as your Cursor workspace for migration work — deploy to the target project first.

## Active rules (15)

| Rule | Role |
|------|------|
| `00-core-fsm` | Mode A/B, scenarios, safety, deps gate |
| `01-react-standards` | React/TSX (glob) |
| `04-sharepoint-standards` | ASPX/master (glob) |
| `06-surface-quality` | SEO/UI/A11y + classic px exception (glob) |
| `07-testing-gate` | gulp test smoke (glob) |
| `08-chain-steps` | `..chain` STEP format (Mode B) |
| `11-active-rules-report` | Mode B chrome only |
| `12-codegraph` | Need/Skip policy (on-demand) |
| `13-context-handoff` | `active_context.md` / `progress.md` SoT |
| `14-security-appsec` | OWASP, secrets |
| `15-js-code-quality` | Classic JS (glob) |
| `16-landing-page-image-quality` | Image quality (glob) |
| `17-classic-host-and-assets` | One WP per page, no hub router |
| `18-bulk-migration-baseline` | Bulk wired/baseline wave (glob) |
| `19-migration-skill-auto-invoke` | Prompt → skill routing (always-on) |

Archived (inactive): WordPress, Laravel, FastAPI, Flutter, Express → `_cursor/rules/archive/`

## Sync source

Last synced from: `DBS-FFW/.cursor/` + root memory files + `docs/`

To refresh this pack from DBS-FFW, re-run the same rsync/cp steps or ask the agent to re-sync.
