---
name: classic-visual-parity
description: >-
  Clone classic-site visual CSS into SPFx module.scss at pixel level: font-size,
  font-weight, font color, BG color, spacing, Gap, margin, padding, break line,
  letter spacing, line height, hover effect, animation effect, and responsive
  @media breakpoints. Use when migrating classic ASPX to SPFx, when the user
  says the page does not look like the classic site, or when updating styles,
  style.css, OpenSans, UIKit, Bootstrap, hover, animation, mobile, tablet, or
  responsive layout on project-saral-classic pages.
---

# Classic Visual Parity (blocking)

This repo is a **visual clone**, not a Fluent redesign.

**Visual source of truth** = classic CSS, not Fluent defaults, not SharePoint theme slots, not glassmorphism.

| Source | Path |
|--------|------|
| Primary CSS | `project-saral-classic/project-saral/assets/css/shared.css` |
| Page CSS | `knowledge-hub.css`, `k-comms.css`, `kiasu.css`, `individual.css`, `components.css` (slice only) |
| Page markup | `project-saral-classic/*.aspx` + `project-saral/components/*.html` |
| Vendor layout | `project-saral/assets/css/uikit/uikit.css` + Bootstrap 4.4.1 **only classes the page uses** — load `uikit-to-spfx-visual-parity` for `uk-*` leftover |
| Carousel / motion | Swiper + AOS on pages that use them (used rules only) |
| Fonts | `project-saral/assets/fonts/OpenSans/` |
| Target | `project-saral-SPFX/src/webparts/**/*.module.scss` and `src/shared/**` |

Do **not** guess rem / Fluent density / theme tokens. Copy classic values.

## Conflict overrides (this repo)

These lose to this skill on classic → SPFx UI:

- `spfx-enterprise-design-core` “do not rely on pixel-perfect” / 480–1024 heuristics → **pixel-perfect vs classic is required**; copy classic `@media` px
- `06-surface-quality` no-px / Fluent breakpoints → **classic `px` / hex / `@media` widths are required**
- `spfx-theme-and-brand-integration` semantic slots / no hardcoded color → **hardcode classic hex**
- `spfx/references/react-design.md` Fluent v9 / inherit host theme → **Fluent v8 only if a control is needed; visual values stay classic**
- glassmorphism / Fluent glass tokens → **do not apply** to project-saral-classic page chrome or body UI
- `07-testing-gate` gulp/list smoke → **not enough**; visual rows above are blocking

Keep: CSS modules (no global chrome leaks except documented host-gap paints), keyboard/focus names, `prefers-reduced-motion` wrapping of classic animation (do not drop the effect for users without reduced-motion).

## When (always on these tasks)

- Any classic page / web part migrate or visual tweak
- User mentions: font-size, font-weight, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive, @media, mobile, tablet, breakpoint
- “classic နဲ့ မတူ” / look & feel / spacing mismatch / mobile မတူ

## Workflow (do this before calling the page done)

### 1) CSS inventory (code before SCSS)

For the slice being edited, read classic `shared.css` + the page CSS file + ASPX classes + UIKit/Bootstrap classes actually used. Build a token table. Every row below is **mandatory** — skip none:

- font-size
- font-weight
- font color
- BG color
- spacing
- Gap
- margin
- padding
- break line
- letter spacing
- line height
- hover effect
- animation effect
- responsive / @media (every classic query that applies to the slice — copy the same `max-width` px; this repo uses 320, 500, 639, 768, 959, 990, 991, 1200, 1300, 1600)

Also capture: `font-family` (OpenSans named faces), `border` / `border-radius`, `box-shadow`, `background-image` / gradient, Bootstrap grid/util classes and UIKit `uk-*` the ASPX actually uses.

Do **not** substitute Fluent 480 / 1024 heuristics. Do **not** collapse several classic breakpoints into one.

Controller JS that toggles classes (active tab, hover class, uk-active) must keep the **same class semantics** so CSS still applies.

### 2) Port exact values

- Write into `*.module.scss`. Do not add Tailwind / SPA routers.
- Reuse existing OpenSans `@font-face` (classic `project-saral/assets/fonts/OpenSans/`). Do not invent a second font stack (`Segoe UI` only as fallback after OpenSans).
- Prefer a shared tokens partial if one already exists under `project-saral-SPFX/src/shared/`. Do **not** create a new package. Duplicate `@font-face` per web part only if no shared partial exists yet.
- `:global` host paints (`#FFFFFF` on canvas) only when classic `body`/`html` background must fill Modern chrome gaps — do not restyle suite nav / command bar.
- `br` / `white-space` / empty paragraph spacing: preserve classic break line behavior; do not collapse to Fluent Text spacing.
- Hover / animation: port `:hover`, `transition`, `@keyframes`, UIKit hover classes. Do not replace with Fluent hover-only-avoidance by removing hover.
- Responsive: port each matching `@media screen and (max-width: Npx)` (and `min-width` if classic has it) with the **same N**. Inside those queries, clone the same stack / wrap / hide / width / font-size / spacing changes. Host canvas may be narrower than classic full page — still use classic queries; do not invent extra breakpoints to “fix” Modern chrome.

### 3) Blocking gate

A migrate or visual update is **not done** if any inventory row still differs from classic (wrong value, missing hover, missing animation, Fluent gap substituted, missing/wrong `@media` width, Fluent 480px used instead of classic).

Do not say “looks close” / “Fluent-aligned is enough” / “desktop is fine, mobile later”.

## Validation (manual smoke — visual)

Side-by-side classic page vs SPFx workbench/served page, same breakpoint:

1. font-size, font-weight, font color, BG color
2. spacing, Gap, margin, padding, break line
3. letter spacing, line height
4. hover effect, animation effect
5. **Responsive (blocking):** every classic `@media` for the slice — same breakpoint px; stack / wrap / hide / width match. Spot-check at those classic widths, not only 480px.

Then still run Testing Gate (`gulp bundle` / existing tests) and keyboard/focus on controls.

## Anti-patterns

- Finishing a web part with data/React done but SCSS still Fluent defaults
- Replacing classic hex with `[theme:..., default: ...]` or CSS variables from glassmorphism
- Changing classic px to rem “for a11y” on this clone (user asked for classic match)
- Applying glassmorphism / Fluent glass tokens to these pages
- Copying all of `uikit.css` into SPFx — only the classes the page uses, inlined into the module
- Replacing classic `@media` widths with Fluent 480 / 1024 heuristics
- Shipping desktop-only SCSS and deferring mobile
