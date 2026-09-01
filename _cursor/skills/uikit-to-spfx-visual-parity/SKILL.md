---
name: uikit-to-spfx-visual-parity
description: >-
  Ports UIKit (uikit.css / uk-* classes) visual values into SPFx module.scss
  so gap, padding, margin, font-size, and animation are not left behind. Use when
  migrating DBS-FFW-classicsite UIKit classic pages to SPFx,
  when spacing or type looks wrong vs classic, or when the user mentions UIKit,
  uk-grid, uk-margin, uk-modal, uk-sticky, uk-animation, uikit.css, leftover
  gap/padding/margin/font-size/animation.
---

# UIKit → SPFx visual parity (this repo)

Classic UIKit pages are **page CSS + UIKit + Bootstrap**. Copying only `style.css` into `*.module.scss` drops everything that lived in `uikit.min.css` / `uikit.min.js` / Bootstrap.

Do **not** load the full vendor file into SPFx. Inline **only** the `uk-*` rules the page actually uses.

Load with `classic-visual-parity` (paths + mandatory token rows). This skill is the **UIKit leftover layer** those rows often miss.

| Role | Path |
|------|------|
| UIKit CSS | `DBS-FFW-classicsite/2025/public/css/vendor/uikit.min.css` |
| UIKit JS | `DBS-FFW-classicsite/2025/public/js/vendor/uikit.min.js` |
| Markup | `DBS-FFW-classicsite/2025/*.aspx` (inline `header.page-banner`) |
| Page CSS | `DBS-FFW-classicsite/2025/style.css` + `sass/` |
| Target | `DBS-FFW-SPFX/src/webparts/**/*.module.scss` and `src/shared/**` |

## Failure mode (expected)

| Left behind | Why |
|---|---|
| Gap | `uk-grid` / `uk-grid-*` is **not** CSS `gap`. It is negative `margin-left` + child `padding-left` (and row `margin-top`). Guessing `gap: Npx` usually misses container-edge alignment. |
| Padding | `.uk-modal-body`, `.uk-offcanvas-bar`, `.uk-padding-*` live in UIKit, not page CSS. |
| Margin | `.uk-margin` / `.uk-margin-*` (often 20px stack on form fields). |
| Font-size | UIKit sets `html { font-size: 16px }` and many utilities are `rem`. SPFx host root font differs → rem drifts. |
| **Line-height (headings)** | UIKit sets `h2 { line-height: 1.3 }` (and `h1` 1.2, `h3` 1.4). Page `style.css` often overrides `h2` **font-size** only — live classic title height = UIKit line-height × page font-size. SPFx root `line-height: 28px` makes titles inherit **28px** unless ported. |
| Animation | `.uk-animation-*` needs `@keyframes` + duration. UIKit JS also animates modal/offcanvas. `transition` alone is not enough. |

Also dropped unless ported: `uk-hidden@*` / `uk-visible@*` (show/hide at UIKit breakpoints), `uk-child-width-*`, `uk-flex*`, `uk-width-*`, `uk-sticky`, `uk-table`.

CSS Modules hash class names. Putting `uk-grid` on JSX does **nothing** unless the rule is in the module (or `:global`, which is usually the wrong fix).

This site uses (verify in ASPX before porting): `uk-container`, `uk-img`, `uk-grid`, `uk-flex`. Re-read the slice ASPX — do not assume InsightsBank modal/sticky classes.

## When

- Any classic → SPFx UI migrate or visual tweak on this site
- SPFx clone looks tighter, looser, or static vs classic
- User mentions leftover **gap, padding, margin, font-size, animation** / UIKit / `uk-*`

## Workflow

### 1) Inventory used `uk-*` only

From the slice’s ASPX, list every `uk-*` class and UIKit component attribute (`uk-grid`, `uk-container`, `uk-img`, `uk-flex`). For each, extract the **computed rule** from `DBS-FFW-classicsite/2025/public/css/vendor/uikit.min.css` (do not assume another UIKit version).

Mandatory token rows (skip none) — same list as `classic-visual-parity`:

- font-size / font-weight / font color / BG color
- spacing / **Gap** / **margin** / **padding** / break line
- letter-spacing / line-height
- hover / **animation** (`:hover`, `transition`, `@keyframes`)
- responsive `@media` — copy the **same px** as classic/UIKit; this repo uses 1200, 1024, 959, 768, 640, 480. Do not replace with Fluent-only 480/1024

### 2) Port into `*.module.scss`

- Write equivalent selectors on the React/CSS-module classes (rename `uk-*` to module classes).
- Copy **exact px / hex / duration**. Do not convert to rem “for a11y”. Do not use Fluent density or theme slots as the look.
- Grid: prefer the same negative-margin + child padding model. Use CSS `gap` only after side-by-side proof that edges and gutters match.
- Animation: port `@keyframes` used by the slice. Wrap with `prefers-reduced-motion` (do not drop the effect for everyone).
- Responsive: port `uk-hidden@m` / `uk-visible@m` as the same `min-width` / `max-width` px as this UIKit file (`@m` = 960px).
- Host: SharePoint `ControlZone` padding/margin resets can eat spacing — compensate in the web part root, do not restyle suite nav.

Typical **UIKit 3** defaults in this repo’s `uikit.css` (re-read the file if it changes):

| Class / component | Value in this vendor file |
|---|---|
| `html` | `font-size: 16px`; `line-height: 1.5` |
| **`h2`, `.uk-h2`** | **`line-height: 1.3`** (page CSS may override `font-size` only — still port this) |
| `h1`, `.uk-h1` | `line-height: 1.2` |
| `h3`, `.uk-h3` | `line-height: 1.4` |
| `.uk-grid` | `display: flex; flex-wrap: wrap; margin-left: -30px` + `> * { padding-left: 30px }` |
| `.uk-grid-medium` | 30px gutter; row `margin-top: 30px` |
| `.uk-margin` | `margin-bottom: 20px`; `* + .uk-margin { margin-top: 20px }` |
| `.uk-modal-body` | `padding: 30px` |
| `.uk-modal-dialog` | `width: 600px`; open: `opacity` + `translateY(-100px)` → `0` over `.3s linear` |
| `.uk-offcanvas-bar` | `width: 270px`; `padding: 20px` |
| `[class*=uk-animation-]` | `animation-duration: .5s`; `ease-out`; `both` |
| `.uk-animation-slide-top-small` | `@keyframes` `opacity: 0` + `translateY(-10px)` |
| `@s` / `@m` / `@l` / `@xl` | 640 / 960 / 1200 / 1600 |

`uk-grid` JS also injects `uk-grid-margin` on wrapped rows. If you skip the JS, you must still reproduce row gap in SCSS. `uk-sticky` / `uk-modal` / `uk-toggle` behavior must be React state + CSS, not a copied `uikit.js`.

### 3) Blocking gate

Not done if any inventory row still differs, if `uk-*` was left as a class name with no module rule, if full `uikit.css` was bundled, or if Fluent `gap`/480px was substituted.

**UIKit section titles (`h2` / `.main-title` inside `uk-container`):** port **`line-height: 1.3`** on `h2` unless slice ASPX has no `h2` titles — see [visual-typography.md](../classic-to-spfx-migration/references/visual-typography.md) Step 3b. Do not leave WP root `line-height: 28px` on headings.

**UIKit body copy (`p` in `.card-wrap` / `uk-container`):** port **`font-weight: 400`** on WP root + `p` when classic uses `OpenSans-Regular` — see visual-typography Step 3c. Do not leave host-inherited light weight on card paragraphs.

Do not say “looks close” or “desktop is fine, mobile later”.

## Validation

Side-by-side classic vs SPFx at **each** classic/UIKit breakpoint used by the slice:

1. font-size, weight, color, BG
2. gap/gutter, margin, padding, break line
3. letter-spacing, line-height
4. hover + animation (keyframes, modal/sticky motion)
5. `uk-hidden@*` / `uk-visible@*` show-hide and child widths

Then run `gulp bundle` in `DBS-FFW-SPFX`. Visual match is blocking even if the bundle passes.

## Anti-patterns

- Copying all of `uikit.css` / `uikit.js` into SPFx
- Porting `style.css` only and treating UIKit/Bootstrap as unused vendor
- Replacing `uk-grid` with an arbitrary CSS `gap`
- Keeping `uk-*` class names under CSS Modules without porting rules
- Replacing classic/UIKit `@media` px with Fluent 480 / 1024
- Dropping `@keyframes` and shipping hover-only or no motion
- Converting UIKit `px`/`rem` to theme tokens or glassmorphism
