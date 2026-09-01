---
name: classic-visual-parity
description: >-
  Clone classic-site visual CSS into SPFx module.scss at pixel level: font-size,
  font-weight, font color, BG color, spacing, Gap, margin, padding, break line,
  letter spacing, line height, hover effect, animation effect, and responsive
  @media breakpoints. Use when migrating classic ASPX to SPFx, when the user
  says the page does not look like the classic site, when font-weight looks light
  or bold vs classic, menu underline mismatch, or when updating styles,
  style.css, OpenSans, UIKit, Bootstrap, hover, animation, mobile, tablet, or
  responsive layout on DBS-FFW-classicsite pages.
---

# Classic Visual Parity (blocking)

This repo is a **visual clone**, not a Fluent redesign.

**Visual source of truth** = classic CSS, not Fluent defaults, not SharePoint theme slots, not glassmorphism.

| Source | Path |
|--------|------|
| Primary CSS | `DBS-FFW-classicsite/2025/style.css` |
| SASS sources | `DBS-FFW-classicsite/2025/sass/` (`style.sass`, `_home`, `_fonts`) |
| Page markup | `DBS-FFW-classicsite/2025/*.aspx` (chrome is inline `header.page-banner`) |
| Vendor layout | `2025/public/css/vendor/uikit.min.css` + Swiper + hamburgers **only classes the page uses** — load `uikit-to-spfx-visual-parity` for `uk-*` leftover |
| Motion / carousel | Swiper → `swiper-to-spfx-carousel` (init + scoped nav); lottie, anime, FullCalendar (used rules only) |
| Fonts | `DBS-FFW-classicsite/2025/public/Fonts/opensans-condensed/` (OpenSans-Condensed-ExtraBold / Bold / Regular / Light) |
| Target | `DBS-FFW-SPFX/src/webparts/**/*.module.scss` and `src/shared/**` |

Do **not** guess rem / Fluent density / theme tokens. Copy classic values.

## Conflict overrides (this repo)

These lose to this skill on classic → SPFx UI:

- `spfx-enterprise-design-core` “do not rely on pixel-perfect” / 480–1024 heuristics → **pixel-perfect vs classic is required**; copy classic `@media` px
- `06-surface-quality` no-px / Fluent breakpoints → **classic `px` / hex / `@media` widths are required**
- `spfx-theme-and-brand-integration` semantic slots / no hardcoded color → **hardcode classic hex**
- `spfx/references/react-design.md` Fluent v9 / inherit host theme → **Fluent v8 only if a control is needed; visual values stay classic**
- glassmorphism / Fluent glass tokens → **do not apply** to DBS-FFW-classicsite page chrome or body UI
- `07-testing-gate` gulp/list smoke → **not enough**; visual rows above are blocking

Keep: CSS modules (no global chrome leaks except documented host-gap paints), keyboard/focus names, `prefers-reduced-motion` wrapping of classic animation (do not drop the effect for users without reduced-motion).

## When (always on these tasks)

- Any classic page / web part migrate or visual tweak
- User mentions: font-size, **font-weight**, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive, @media, mobile, tablet, breakpoint, **ထူ**, **ပါး**, **bold**, **underline**, OpenSans
- “classic နဲ့ မတူ” / look & feel / spacing mismatch / mobile မတူ

## Workflow (do this before calling the page done)

### 1) CSS inventory (code before SCSS)

For the slice being edited, read classic `style.css` + matching `sass/` partials + ASPX classes + UIKit/Bootstrap classes actually used. Build a token table. Every row below is **mandatory** — skip none:

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
- responsive / @media (every classic query that applies to the slice — copy the same `max-width` px; this repo uses 1200, 1024, 959, 768, 640, 480)

Also capture: `font-family` (year-correct OpenSans named faces — see [visual-typography.md](../classic-to-spfx-migration/references/visual-typography.md)), `border` / `border-radius`, `box-shadow`, `background-image` / gradient, Swiper/hamburgers and UIKit `uk-*` the ASPX actually uses.

Do **not** substitute Fluent 480 / 1024 heuristics. Do **not** collapse several classic breakpoints into one.

Controller JS that toggles classes (active tab, hover class, uk-active) must keep the **same class semantics** so CSS still applies.

### 2) Port exact values

- Write into `*.module.scss`. Do not add Tailwind / SPA routers.
- Reuse existing OpenSans-Condensed `@font-face` (classic `DBS-FFW-classicsite/2025/public/Fonts/opensans-condensed/`). Do not invent a second font stack (`Segoe UI` only as fallback after OpenSans-Condensed).
- Prefer a shared tokens partial if one already exists under `DBS-FFW-SPFX/src/shared/`. Do **not** create a new package. Duplicate `@font-face` per web part only if no shared partial exists yet.
- `:global` host paints (`#FFFFFF` on canvas) only when classic `body`/`html` background must fill Modern chrome gaps — do not restyle suite nav / command bar.
- `br` / `white-space` / empty paragraph spacing: preserve classic break line behavior; do not collapse to Fluent Text spacing.
- Hover / animation: port `:hover`, `transition`, `@keyframes`, UIKit hover classes. Do not replace with Fluent hover-only-avoidance by removing hover.
- Responsive: port each matching `@media screen and (max-width: Npx)` (and `min-width` if classic has it) with the **same N**. Inside those queries, clone the same stack / wrap / hide / width / font-size / spacing changes. Host canvas may be narrower than classic full page — still use classic queries; do not invent extra breakpoints to “fix” Modern chrome.

### 2b) Typography self-check (blocking — before parity PASS)

**Read** [visual-typography.md](../classic-to-spfx-migration/references/visual-typography.md) and run the mandatory self-check on every UI slice:

1. Grep classic `font-family` / `font-weight` / menu `text-decoration` vs `*.module.scss`
2. Apply named-face rule: `OpenSans-Bold` / SemiBold / Condensed-Bold → **`font-weight: 400`**
3. Menu/nav `<a>`: `text-decoration: none` where classic has no underline (SharePoint host)
4. Output short **Typography self-check** table (selector · family · weight · link deco · OK/FIX)

Do **not** mark parity PASS or close a visual typography task without this table.

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
- Skipping typography self-check when classic Bold/SemiBold selectors lack `font-weight: 400` in SPFx
- Copying classic CSS for menu links but leaving SharePoint host underline on `<a>`
- Replacing classic hex with `[theme:..., default: ...]` or CSS variables from glassmorphism
- Changing classic px to rem “for a11y” on this clone (user asked for classic match)
- Applying glassmorphism / Fluent glass tokens to these pages
- Copying all of `uikit.min.css` into SPFx — only the classes the page uses, inlined into the module
- Replacing classic `@media` widths with Fluent 480 / 1024 heuristics
- Shipping desktop-only SCSS and deferring mobile
