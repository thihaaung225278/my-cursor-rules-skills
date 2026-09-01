# Classic Swiper configs (DBS-FFW)

Source: `public/js/common.js` (2023 / 2024 / 2025 — identical for main sliders).

## `.winner-slider`

```js
new Swiper(".winner-slider", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
```

- Default `slidesPerView: 1`
- No `spaceBetween`, no `loop`, no autoplay
- Markup: team photos in `.swiper-slide` > `.team-photo` (background-image)
- Dynamic slides: some controllers replace `.winner-slider .swiper-wrapper` children when country changes — SPFx must re-render slides + call `swiper.update()` or remount

## `.gallery-slider`

```js
new Swiper(".gallery-slider", {
  slidesPerView: 1,
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    640: { slidesPerView: 2 },
    768: { slidesPerView: 3 },
  },
});
```

- Container classes: `swiper gallery-wrap gallery-slider`
- Slide content: `.gallery` div with `background-image` (height ~220px in CSS)
- Gallery hover: `transform: scale(1.03)` — lives in page CSS, not Swiper

## `.mySwiper1` (inline ASPX — not winner/gallery)

Some pages init separately in ASPX foot script — inventory per slice; often past-events / team carousel only.

## React `Swiper` prop mapping

| Classic | `swiper/react` |
|---------|----------------|
| `slidesPerView: 1` | `slidesPerView={1}` |
| `spaceBetween: 10` | `spaceBetween={10}` |
| `breakpoints` | same object on `Swiper` |
| `navigation` | `modules={[Navigation]}` + `navigation` prop or default generated buttons |
| `modules` | import from `swiper/modules` |

## SPFx scoped navigation example

When two sliders exist on one page, **do not** use classic global selectors:

```tsx
<Swiper modules={[Navigation]} navigation className="swiper winner-slider">
  {slides.map(...)}
  {/* React Swiper creates prev/next when navigation=true */}
</Swiper>
```

Or nest buttons and bind refs — each instance isolated.

## CSS selectors to port (check year `style.css`)

- `.winner-slider .team-photo`, `.gallery-slider .team-photo` — `height: 500px`, cover center
- `.winner-slider .swiper-button-prev`, `.gallery-slider .swiper-button-prev` — `left: 0`
- `.winner-slider .swiper-button-next`, `.gallery-slider .swiper-button-next` — `right: 0`
- Shared nav — `background-color: rgba(0,0,0,0.5)`, `color: #fff`, `padding: 32px`
- Hover — `background: #fff`, `color: #707070`, `transition: .3s ease-out`
- `:after` — `font-size: 35px`
- `.gallery-wrap .swiper-slide` — `overflow: hidden`
- Mobile `@media` — optional `scroll-snap` flex fallback on `.swiper-wrapper` (see Ffw2023.module.scss)

## Vendor version note

Classic ships `swiper-bundle.min.js` (bundled modules). SPFx should import only `Navigation` module + minimal CSS. Match **behavior**, not vendor file shape.

## Security / deps

- Do not commit vulnerable Swiper 8.x — user-approved `swiper@12+` if adding dep
- No user-controlled slide HTML without sanitize — winner prizes may use HTML from JSON; existing `dangerouslySetInnerHTML` paths stay separate from slide images
