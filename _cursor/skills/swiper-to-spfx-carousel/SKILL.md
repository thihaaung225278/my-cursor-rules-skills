---
name: swiper-to-spfx-carousel
description: >-
  Wires classic Swiper carousels (winner-slider, gallery-slider) into SPFx React
  17 with classic config parity, scoped navigation, and module.scss nav styles —
  not vendor CSS bundles. Use when the user mentions Swiper, carousel, slider,
  gallery slider, winner-slider, swiper-button, slidesPerView, or gallery/winner
  section does not swipe on SPFx.
---

# Swiper → SPFx carousel (DBS-FFW)

Classic pages use **Swiper bundle** (`swiper-bundle.min.js` + CSS) with init in `public/js/common.js`. SPFx must **not** ship the vendor bundle — wire `swiper` npm (user-approved) + clone nav/slide CSS from year `style.css` into `*.module.scss`.

Load with `classic-visual-parity` (nav button / slide visuals) and `uikit-to-spfx-visual-parity` when gallery grid spacing drifts.

| Role | Path |
|------|------|
| Init configs | `DBS-FFW-classicsite/{year}/public/js/common.js` |
| Nav / slide CSS | `DBS-FFW-classicsite/{year}/style.css` (+ `sass/_home.sass`) |
| Markup | slice ASPX — `.winner-slider`, `.gallery-wrap.gallery-slider` |
| Vendor (reference only) | `{year}/public/css/vendor/swiper-bundle.min.css` — **do not import into SPFx** |
| Target | `DBS-FFW-SPFX/src/webparts/**` |

Classic configs (all years — verify slice before copy): see [classic-configs.md](./references/classic-configs.md).

## When

- Gallery or game-show winner section shows static slides on SPFx
- User mentions Swiper, carousel, slider, `swiper-button`, `slidesPerView`
- Wave 4 parity on sections with `.winner-slider` / `.gallery-slider`

## Reject

- `swiper-bundle.min.js` / `swiper-bundle.min.css` in sppkg
- `import 'swiper/css/bundle'` (pulls all module CSS — bloat + fights classic overrides)
- Global `navigation.nextEl: '.swiper-button-next'` when multiple sliders exist on one page (classic pattern — **scope per instance** in SPFx)
- Fluent carousel / `@fluentui/react` replacements for visual clone slices
- `npm i swiper` without user approval (`00` Dependencies)
- Parity PASS while slides do not swipe or breakpoints differ from classic

## Workflow

### 1) Inventory slice

From ASPX + `common.js`:

- Which sliders? (`.winner-slider`, `.gallery-slider`, `.mySwiper1`, …)
- Init options per selector (navigation, `slidesPerView`, `spaceBetween`, `breakpoints`, `loop`, …)
- Nav buttons present in markup? (`swiper-button-prev` / `swiper-button-next` inside container)
- Dynamic slide injection? (e.g. `testController.js` mutates `.winner-slider .swiper-wrapper` — mirror in React state)

SPFx stubs today (verify): `GallerySection.tsx`, `GameShowWinnersSection.tsx` — markup only, **no init**, **no nav buttons**.

### 2) Dependency (ask-first)

If approved:

```bash
cd DBS-FFW-SPFX
npm i swiper
```

- Prefer current stable `swiper` (12.x) — avoid known vulnerable 8.x transitive pins
- React 17 + SPFx 1.20: use `swiper/react` (`Swiper`, `SwiperSlide`), not Swiper Element web components unless user requests
- Import **only** needed module CSS, e.g. `swiper/css` + `swiper/css/navigation` — not bundle

### 3) Shared component pattern

Create one reusable wrapper per web part (or `src/shared/` if multiple WPs need it):

```tsx
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';
import type { SwiperOptions } from 'swiper/types';
import 'swiper/css';
import 'swiper/css/navigation';

// modules={[Navigation]} navigation onSwiper destroy on unmount (useEffect cleanup)
```

**SPFx / bundle size** (MS Learn dynamic loading): optional `import()` of swiper only when the section mounts — same pattern as heavy vendors; do not block baseline on it.

**Scoped navigation** (required when 2+ sliders on page):

- Put `swiper-button-prev` / `swiper-button-next` **inside** each `Swiper` (React creates elements)
- Or `navigation={{ nextEl: nextRef.current, prevEl: prevRef.current }}` with refs on that instance's buttons
- Do **not** reuse classic global selectors across instances

**Lifecycle:**

- `onSwiper` store instance; `useEffect` return → `swiper.destroy(true, true)` on unmount
- Re-init when slide list length changes (country change repopulating winner slides)

**A11y** (swiper docs + enterprise):

- `modules={[Navigation, A11y]}` when approved — keyboard + slide labels
- Informative slide images: `alt` on `<img>`; background-only slides: `aria-label` on slide or decorative `aria-hidden` on purely visual tiles
- `prefers-reduced-motion`: do not autoplay; classic has no autoplay on these sliders

### 4) Port classic options

| Selector | Classic (`common.js`) |
|----------|------------------------|
| `.winner-slider` | `navigation` only (default `slidesPerView: 1`) |
| `.gallery-slider` | `slidesPerView: 1`, `spaceBetween: 10`, `breakpoints: { 640: { slidesPerView: 2 }, 768: { slidesPerView: 3 } }` |

Pass as `Swiper` props / `breakpoints` object — numeric keys must match classic (640, 768), not Fluent 480.

### 5) CSS (visual parity — not vendor file)

Clone from year `style.css` into the web part module (already partially done in `Ffw2023.module.scss`):

- `.winner-slider .team-photo` / `.gallery-slider` heights (500px winner, 220px gallery tile)
- Nav: `background-color`, hover flip to white/`#707070`, `padding: 32px`, `:after { font-size: 35px }`, `left: 0` / `right: 0`
- `.gallery-wrap .swiper-slide { overflow: hidden }`, gallery hover `transform: scale(1.03)`

**Mobile fallback:** some modules include `@media` rules that set `.swiper-wrapper { display:flex; overflow-x:auto; scroll-snap-type:x mandatory }` — keep if classic year CSS has it; Swiper init should still run when JS loads.

Do **not** rely on Swiper default arrow colors — classic overrides them in page CSS.

### 6) Markup parity

Match classic structure so ported CSS applies:

```html
<div class="swiper winner-slider">
  <div class="swiper-wrapper">…</div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
</div>
```

Gallery: `swiper gallery-wrap gallery-slider` (both classes).

### 7) Validation (blocking before parity PASS on slider sections)

Manual smoke vs classic at same breakpoint:

- [ ] Prev/next visible and styled (dark overlay → white hover)
- [ ] Winner: one slide per view; swipe / arrows work
- [ ] Gallery: 1 / 2 / 3 columns at mobile / 640+ / 768+ with ~10px gap
- [ ] No horizontal page jitter; destroy clean on WP unmount (no duplicate listeners)
- [ ] `gulp bundle` passes after adding dep

## Cross-skill

| Need | Skill |
|------|--------|
| Nav colors, hover, slide heights | `classic-visual-parity` |
| Gallery grid edge alignment | `uikit-to-spfx-visual-parity` |
| Bundle / dynamic import | `spfx-enterprise-code-and-performance` |
| Image paths | `classic-to-spfx-migration` + asset map pattern |

## Anti-patterns

- Markup-only `swiper-slide` divs without Swiper init (current Ffw2023 state)
- Missing nav buttons in JSX while CSS targets `.swiper-button-prev`
- Copying inline `<script>new Swiper(...)</script>` from ASPX into SPFx
- jQuery post-init DOM hacks for slides — use React props/state
