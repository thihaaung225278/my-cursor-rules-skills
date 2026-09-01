---
name: spfx-enterprise-ux-hub
description: >-
  Index of generic (non-clone) SPFx UX skills. Do not use as the first skill for
  DBS-FFW-classicsite classic → SPFx page clones — use classic-to-spfx-migration,
  classic-visual-parity, and uikit-to-spfx-visual-parity instead.
---

# SPFx Enterprise UX Hub

**This repo (DBS-FFW-classicsite):** do **not** start here for classic → SPFx. Start with `classic-to-spfx-migration` + `classic-visual-parity` + `uikit-to-spfx-visual-parity`. Gulp 1.20 only. No glassmorphism. No Heft.

This skill is a **global index** for generic (non-clone) SPFx UX. For those tasks:

1. Decide which **specialized SPFx skills** are relevant.
2. Load only those skills to keep context lean.

Use this hub for SharePoint Framework UX that is **not** a classic `style.css` clone.

---

## 1. Skill map (when to use what)

### 1.1 Design & content (top priority)

- **`spfx-enterprise-design-core`**  
  Use for: layout, information hierarchy, web part levels, titles/descriptions, commanding, placeholders, empty/loading/error states, and responsive design.

- **`spfx-accessibility-and-content-quality`**  
  Use for: keyboard/focus patterns, screen-reader semantics, empty/error text quality, recovery paths, and overall UX text tone.

### 1.2 Theme, brand, and styling

- **`spfx-theme-and-brand-integration`**  
  Use for: theme tokens, semantic slots, high-contrast and dark mode, Brand Center fonts, and tenant-safe branding.

- **`spfx-css-and-styling-governance`**  
  Use for: SCSS module structure, selector scoping, naming conventions, preventing style leakage across web parts.

- **`classic-visual-parity`**  
  Use for: **this repo** classic → SPFx page clone (font-size, color, spacing, hover, animation, `@media` / responsive). Visual SoT = `DBS-FFW-classicsite/2025/style.css`. Load this instead of theme-slot / glassmorphism / Fluent 480 defaults.

- **`uikit-to-spfx-visual-parity`**  
  Use for: UIKit leftover layer (`uk-grid` gutter, `uk-margin`, modal/offcanvas padding, rem font-size, `@keyframes`). Load with `classic-visual-parity` on every classic UI migrate.

### 1.3 Behavior & configuration

- **`spfx-property-pane-reactivity`**  
  Use for: choosing reactive vs non-reactive property pane behavior and designing property editing UX that doesn’t hurt performance.

- **`spfx-extensions-enterprise-patterns`**  
  Use for: Application Customizers, Field Customizers, and Command Sets; dialog patterns; respecting host page context.

### 1.4 Data, implementation, and performance

- **`spfx-enterprise-code-and-performance`**  
  Use for: code structure, data access patterns (REST, Graph, PnPjs), performance optimization, and recommended npm packages.

- **`spfx-enterprise-implementation-core`**  
  Use for: service boundaries, typed interfaces, error/loading handling, module structure, and maintainability.

- **`spfx-image-and-media-optimization`**  
  Use for: image sizing, lazy loading, responsive media, and performance-aware image handling.

### 1.5 Release, packaging, and toolchain

- **`spfx-release-and-package-quality`**  
  Use for: package-solution configuration, versioning, app catalog readiness, and release checklists. This repo: gulp (`gulp bundle` / `gulp serve`), not Heft.

---

## 2. How an AI editor should use this hub

When handling an SPFx task:

1. **Identify the task type**
   - Classic site visual clone (DBS-FFW-classicsite pages)? → stop; use `classic-to-spfx-migration` + `classic-visual-parity` + `uikit-to-spfx-visual-parity` (not this hub, not glassmorphism, not Fluent density, not Heft).
   - Pure UX/design (non-clone)? → `spfx-enterprise-design-core`, `spfx-accessibility-and-content-quality`.
   - Theming/visual alignment (non-clone)? → `spfx-theme-and-brand-integration`, `spfx-css-and-styling-governance`. Not glassmorphism in this repo.
   - Configuration/behavior? → `spfx-property-pane-reactivity`, `spfx-extensions-enterprise-patterns`.
   - Data & implementation? → `spfx-enterprise-implementation-core`, `spfx-image-and-media-optimization`.
   - Release/build? → `spfx-release-and-package-quality` + gulp (`gulp bundle` / `gulp serve`). Not Heft.

2. **Load only the relevant skills**  
   Do **not** load all SPFx skills at once. Pick the minimal set needed.

3. **Apply Microsoft guidance**  
   Each specialized skill encodes patterns aligned with Microsoft docs (design, theming, image helper API, etc.). Use those patterns as the default unless the user explicitly overrides them. This repo stays on gulp 1.20.

4. **Aim for enterprise-grade UX**  
   Every SPFx change should be:
   - Accessible (keyboard, screen reader, color contrast)
   - Performance-aware (no heavy blocking operations in UI or property pane)
   - Theme- and tenant-safe (semantic slots, no hard-coded brand colors) — **except** this repo classic clone: hard-code classic CSS from `DBS-FFW-classicsite/2025/style.css`
   - Classic visual clone: pixel match `style.css` before calling the page done
   - Maintainable (clear module boundaries, typed APIs, minimal toolchain hacks)

---

## 3. Quick decision checklist

For any SPFx task, quickly answer:

1. **Does this change UI or UX?**  
   - Classic clone (this repo)? → `classic-to-spfx-migration` + `classic-visual-parity` + `uikit-to-spfx-visual-parity` + a11y names only.
   - Other SPFx → `spfx-enterprise-design-core` and `spfx-accessibility-and-content-quality`.

2. **Does it affect colors, fonts, visual style, or responsive layout?**  
   - Classic clone (this repo pages) → Add `classic-visual-parity` + `uikit-to-spfx-visual-parity` (classic `@media` px, not theme slots / not glassmorphism / not Fluent 480).
   - Other SPFx → Add `spfx-theme-and-brand-integration` and `spfx-css-and-styling-governance`.

3. **Does it add or change configuration / property panes?**  
   - Yes → Add `spfx-property-pane-reactivity`.

4. **Does it introduce or change images/media?**  
   - Yes → Add `spfx-image-and-media-optimization`.

5. **Is this for release or pipeline work?**  
   - Yes → Add `spfx-release-and-package-quality`. This repo: gulp, not Heft.

For **this repo** classic migrate, do not use this hub as the first stop.
