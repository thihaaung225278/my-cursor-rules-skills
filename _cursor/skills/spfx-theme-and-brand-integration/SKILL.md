---
name: spfx-theme-and-brand-integration
description: Theme token, semantic slot, and brand font guidance for SPFx enterprise customizations.
---

# SPFx Theme and Brand Integration

## Use for

1. Applying semantic slots and theme-aware styling.
2. Integrating Brand Center font usage safely.
3. Ensuring light/dark/high-contrast compatibility.

## Do not use for

1. Hard-coded theme color overrides — **except** this repo's classic visual clone (`classic-visual-parity`): classic hex/px from `DBS-FFW-classicsite/2025/style.css` are required.
2. Ad-hoc font imports that bypass tenant strategy — OpenSans-Condensed faces already in classic/SPFx assets are in-scope for the clone.

## Trigger conditions

1. Theme-related UI work or branding requests.
2. Cross-tenant visual consistency requirements.

## Enterprise guardrails

1. Prefer semantic tokens over fixed values — **except** this repo classic clone: use classic fixed values.
2. Validate high-contrast accessibility.
3. Keep branding extensible and tenant-aware.

## Output expectations

1. Theme-safe enterprise UI.
2. No regressions across standard SharePoint themes.

## Typical target paths (any SPFx project)

1. `src/**/**/*.module.scss`
2. `src/shared/components/**`

