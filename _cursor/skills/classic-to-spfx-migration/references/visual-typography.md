# Visual typography — font-weight, links & host inherit (self-check)

**Companion to** `classic-visual-parity` — run this **mandatory self-check** on every UI migrate / visual parity slice **before** claiming parity PASS or closing a typography fix.

Fluent tokens do **not** win before Visual PASS.

## Per-year font SoT (do not mix years)

| Year folder | Named `@font-face` families | Classic font path |
|-------------|----------------------------|-------------------|
| `2023/` · `2024/` | `OpenSans-Bold`, `OpenSans-SemiBold`, `OpenSans-Medium`, `OpenSans-Regular`, `OpenSans-Light` | `{year}/public/fonts/opensans/` · `{year}/sass/_fonts.sass` |
| `2025/` | `OpenSans-Condensed-ExtraBold`, `OpenSans-Condensed-Bold`, `OpenSans-Condensed-Regular`, `OpenSans-Condensed-Light` | `2025/public/Fonts/opensans-condensed/` |

Visual SoT = **that slice’s year** `style.css` + `sass/_fonts.sass` — not 2025-only when migrating `2023/index.aspx`.

## Why SPFx looks “a bit light” vs classic

1. **SP canvas inherit** — ancestors force **Segoe UI**; classic named faces never apply on the WP root.
2. **Named face + missing weight** — classic uses separate families (`OpenSans-Bold`) not `font-weight: 700`. SPFx must set **`font-weight: 400`** on every selector using a named Bold/SemiBold face or the face renders soft / wrong.
3. **Root baseline missing** — `.ffw2023Root` (or slice root) sets `font-family: OpenSans-Regular` but omits `font-weight: 400` on headings/menu/links using Bold faces.
4. **Font files not loaded** — `@font-face` missing or wrong path vs classic bundled fonts.
5. **Selector loses to host** — SharePoint / Fluent link rules override cloned classes (especially `<a>`).
6. **Link underline (not in classic CSS)** — host adds `text-decoration: underline` on `<a>`; classic pill nav has **no** underline visually.
7. **Remount** — computed weight drifts after canvas inject.

## Named-face rule table (blocking)

When classic CSS has `font-family: 'OpenSans-Bold'` (or SemiBold / Condensed-Bold / etc.):

| Classic | SPFx module.scss (same selector) |
|---------|----------------------------------|
| `font-family: 'OpenSans-Bold'` | Same family + **`font-weight: 400`** |
| `font-family: 'OpenSans-SemiBold'` | Same + **`font-weight: 400`** |
| `font-family: 'OpenSans-Regular'` | Same + **`font-weight: 400`** on WP root and `p` (UIKit `html` default) — host may lighten body copy vs classic |
| `h2` + Bold face | Classic often has `font-weight: 400` explicitly — port it |
| Nav / menu `<a>` with Bold face | **`font-weight: 400`** + see link rule below |

Do **not** substitute `font-weight: 700` + Segoe for named Bold faces.

## Link / menu rule (SharePoint host)

Classic desktop menu often omits `text-decoration: none` on base state (no host underline). SPFx **must** add on nav/menu anchors:

```scss
.menu ul li a,
.page-menu li a {
  text-decoration: none;
  border-bottom: none;
}
/* + :hover, :focus, :visited as needed */
```

Scope to menu/nav selectors only — do not strip underline from `.sub-description a` and other intentional content links.

## Mandatory self-check (agent — every UI slice)

Run **before** parity PASS, after SCSS port, or when user says font “ပါး” / “ထူ” / “light”:

### Step 1 — Grep classic vs SPFx

For the slice, grep classic `{year}/style.css` for `font-family`, `font-weight`, `text-decoration` on selectors you ported. Diff against `*.module.scss`. Flag any classic `OpenSans-*Bold*` / `SemiBold` without matching `font-weight: 400` in SPFx.

### Step 2 — Apply rule table

Fix every named Bold/SemiBold selector. Add menu/link `text-decoration: none` where classic shows no underline.

### Step 3 — Output checklist (in chat or handoff)

Short table required — do not skip:

| Selector / surface | Classic family | SPFx family | SPFx weight | Link deco | Status |
|--------------------|----------------|-------------|-------------|-----------|--------|
| e.g. `.menu ul li a` | OpenSans-Bold | OpenSans-Bold | 400 | none | OK / FIX |

Surfaces to always include when present: **root**, **`p` / card-wrap body copy**, **h2/main-title**, **page-banner date/description**, **post-event menu**, **mobile `.page-menu`**, **buttons/CTAs** using Bold face.

### Step 3b — UIKit heading line-height (blocking when slice uses `uk-container` + `h2`)

Classic pages load UIKit **before** page CSS. Page `style.css` often sets `h2 { font-size: … }` but **does not** set `line-height` — computed title line-height comes from UIKit:

| UIKit selector | `line-height` (this repo vendor) |
|--------------|----------------------------------|
| `h2`, `.uk-h2` | **`1.3`** |
| `h1`, `.uk-h1` | `1.2` |
| `h3`, `.uk-h3` | `1.4` |

SPFx WP root often sets `line-height: 28px` on the root/body clone. Without porting UIKit `h2 { line-height: 1.3 }`, section titles (`.main-title`) inherit **28px** instead of **1.3** → title box too tight, star pseudo-elements misaligned, title→card gap looks wrong.

**Agent rule (do not wait for user to repeat):**

1. If ASPX uses `uk-container` (or other UIKit layout) and section titles are `h2` / `.main-title`, port **`line-height: 1.3`** on `h2` (or `.main-title` if slice has no other `h2`) in `*.module.scss`.
2. Grep classic `{year}/public/css/vendor/uikit.min.css` for `h2{` / `line-height` — do not guess.
3. Add row to typography checklist:

| Selector | Classic/UIKit | SPFx | Status |
|----------|---------------|------|--------|
| `h2` / `.main-title` | `line-height: 1.3` | must match | OK / FIX |

See also `uikit-to-spfx-visual-parity` — UIKit heading defaults table.

### Step 3c — Body copy / card-wrap `p` weight (blocking when slice uses `uk-container`)

Classic `style.css` sets `p { font-family: OpenSans-Regular; font-size: 17px; line-height: 28px }` — often **no** explicit `font-weight`. Live classic = UIKit `html { font-weight: 400 }` + Regular face → body copy looks **normal weight**.

SPFx WP root may set `font-family: OpenSans-Regular` but **omit** `font-weight: 400` on root and `p`. SharePoint canvas inherit can render card copy (`section .card-wrap .card-content p`, `.main-sub-title`, highlights intro `p`) **lighter/thinner** than classic (“classicsite ထူ · SPFx ပါး”).

**Agent rule (do not wait for user to repeat):**

1. Set **`font-weight: 400`** on slice WP root (e.g. `.ffw2023Root`) and on **`:global p`** when classic uses `OpenSans-Regular` for body copy.
2. Typography checklist row:

| Selector | Classic/UIKit | SPFx | Status |
|----------|---------------|------|--------|
| WP root + `p` / `.card-wrap p` | `font-weight: 400` + OpenSans-Regular | must match | OK / FIX |

3. If still light after weight fix: Network tab — OpenSans `.woff2` → 200 (font not loaded = Segoe fallback).

### Step 4 — Manual QA (when served)

DevTools computed on SPFx vs classic same breakpoint:

- [ ] `font-family` = classic named face (not Segoe primary)
- [ ] `font-weight` = `400` on named Bold/SemiBold selectors
- [ ] Menu/nav links: no host underline
- [ ] Network: font `.woff2` / `.woff` → 200

## Win order (fix)

1. Inventory classic selectors (`classic-visual-parity`) — skip none
2. Port exact px/hex/family into `*.module.scss`
3. Apply **named-face rule table** on every Bold/SemiBold selector
4. Menu/nav link `text-decoration: none` where classic has no underline
5. WP root: classic `font-family` stack + `font-weight: 400` baseline on Bold headings if still soft
6. Reuse year-correct `@font-face` from classic fonts folder (bundled in sppkg)
7. Fix fighting `style={{}}` / theme slots before adding `!important`

## Repo examples (Ffw2023 — copy pattern)

| Issue | Classic | SPFx fix |
|-------|---------|----------|
| Menu too light | `.menu ul li a { font-family: OpenSans-Bold }` | + `font-weight: 400` |
| Menu underline | no underline visually | + `text-decoration: none; border-bottom: none` on menu `<a>` |
| Date bold soft | `.date { OpenSans-Bold }` | + `font-weight: 400` |
| h2 soft | `h2 { OpenSans-Bold; font-weight: 400 }` | port both |
| Card copy light | `p` in `#post-about` / `.card-wrap` — Regular, implicit 400 | + `font-weight: 400` on root + `p` |

Files: `Ffw2023.module.scss` · `PageBanner.tsx` menu markup.

## Reject

- Marking parity PASS without typography self-check table
- “CSS copied from classic” while named Bold selectors lack `font-weight: 400`
- Fluent tokens / Segoe as primary stack pre-PASS
- Global `a { text-decoration: none }` that breaks content underlines
- `font-weight: 700` instead of named OpenSans-Bold face
