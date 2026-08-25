---
name: spfx-enterprise-design-core
description: Core design guidance for SPFx web parts and extensions. Use for layout, hierarchy, commanding, text, empty states, and responsive behavior when building or reviewing SPFx UX.
---

# SPFx Enterprise Design Core

Use this skill whenever you are **designing or reviewing SPFx UX**, not just a specific repo. It encodes Microsoft guidance for SharePoint web parts and extensions so any AI editor can propose **consistent, accessible, performant** UX.

Key MS references (for deeper detail – read only when needed):
- Web part design overview: https://learn.microsoft.com/sharepoint/dev/design/design-guidance-overview
- Design a web part: https://learn.microsoft.com/sharepoint/dev/design/design-a-web-part
- Design considerations for web parts: https://learn.microsoft.com/sharepoint/dev/spfx/web-parts/basics/design-considerations-for-web-parts
- Web part levels, titles, descriptions, commanding, layout patterns, empty states, accessibility, examples, and icons: https://learn.microsoft.com/sharepoint/dev/design/

---

## 1. When to apply this skill

Apply this guidance for **any SPFx UI change**, including:

- New or significantly updated **web parts**
- New **SPFx extensions** that introduce UI (Application/Field Customizers, Command Sets)
- Changes to:
  - Layout, card structure, or grid behavior
  - Web part **titles, descriptions, and commands**
  - **Empty, loading, error, and placeholder** experiences
  - **Responsive behavior** across breakpoints
  - **Information architecture** (content groupings, levels, and flows)

Do **not** use for:
- Build/toolchain-only work (Heft/webpack, packaging)
- Pure back-end/service work with no user-facing surface
- **this repo classic visual clone** of type, color, spacing, hover, animation, or `@media` breakpoints — use `classic-visual-parity` (this skill's “no pixel-perfect” and 480/1024 rules do **not** apply there)

---

## 2. Web part structure & levels

Design SPFx web parts with **clear levels** and hierarchy:

1. **Web part level**
   - Title: clear, action- or outcome-oriented (e.g., "Permissions risk heatmap", not "PRH")
   - Description: 1–2 concise sentences answering: _What does this do?_ and _Why should I care?_
   - Optional **subtitle/context**: scope or key filter (e.g., "Current site", "Last 30 days").

2. **Section / region level**
   - Group related content into visually distinct regions (cards, panels, tabs).
   - Each region should have a **clear label** (heading) and purpose.

3. **Item level**
   - Each row/card/tile must make sense on its own: label, primary metric/state, and key action.
   - Favor **progressive disclosure**: show high-value info first; move details into drill-ins.

Implementation snippet (React):
```ts
// Example web part root structure
return (
  <section aria-label="Permissions risk heatmap" className={styles.webPartRoot}>
    <header className={styles.header}>
      <h2 className={styles.title}>Permissions risk heatmap</h2>
      <p className={styles.description}>
        Highlight sites and groups with the highest sharing and access risk.
      </p>
      {renderHeaderCommands()}
    </header>

    <main className={styles.content}>
      {renderMainContent()}
    </main>
  </section>
);
```

---

## 3. Layout & responsive design

Follow grid and responsive patterns from:
- https://learn.microsoft.com/sharepoint/dev/design/grid-and-responsive-design
- https://learn.microsoft.com/sharepoint/dev/design/layout-patterns

Core rules:

1. **Use responsive layouts, not fixed widths**
   - Prefer CSS `grid` / `flex` with min/max widths.
   - Avoid horizontal scroll for primary flows; let cards wrap.

2. **Breakpoints** (heuristics) — generic SPFx only
   - **Small (< 480px)**: single-column, stacked content; hide non-essential chrome.
   - **Medium (480–1024px)**: two-column cards, condensed table, fewer visible commands.
   - **Large (> 1024px)**: full grid/table, full command bar.
   - **Exception (this repo classic clone):** copy `@media` widths from `project-saral-classic/project-saral/assets/css/shared.css` (commonly 320 / 500 / 639 / 768 / 959 / 990 / 991 / 1200 / 1300 / 1600). Do **not** replace with 480/1024 heuristics.

3. **Do not rely on pixel-perfect design** (generic SPFx)
   - Design for **content resilience**: longer labels, translated text, variable data.
   - **Exception:** classic → SPFx in this repo **does** require pixel match vs `project-saral-classic/project-saral/assets/css/shared.css`.

CSS snippet:
```scss
.webPartRoot {
  display: flex;
  flex-direction: column;
}

.contentGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 12px;
}

@media (max-width: 480px) {
  .contentGrid {
    grid-template-columns: 1fr;
  }
}
```

---

## 4. Web part titles, descriptions & UI text

Key references:
- Titles & descriptions: https://learn.microsoft.com/sharepoint/dev/design/web-part-titles-and-descriptions
- UI text guidance: https://learn.microsoft.com/sharepoint/dev/design/ui-text-for-web-parts

Guidelines:

1. **Titles**
   - Describe **purpose and outcome**, not implementation.
   - Avoid jargon and internal project names.
   - Good: _"External sharing overview"_ vs. Bad: _"ExtShareV2"_.

2. **Descriptions**
   - 1–2 sentences, present tense, user benefit first.
   - Example: _"Track where external sharing is enabled and identify risky sites."_

3. **Labels & commands**
   - Use **verb-first** labels for actions: _"Filter", "Export", "Open details"_.
   - Avoid using the same word for both state and action (e.g., "Sharing" as both a tab and a command).

4. **Tone**
   - Professional, direct, and neutral.
   - Avoid blame in error text: focus on resolution.

---

## 5. Commanding patterns

Reference: https://learn.microsoft.com/sharepoint/dev/design/web-part-commanding

Principles:

1. **Primary vs secondary actions**
   - One **primary action** (button) per main surface (e.g., "New", "Configure", "Fix issues").
   - Group secondary actions in menus when they clutter the surface.

2. **Contextual commands**
   - Row-level actions belong near the row (action icons or contextual menu).
   - Web-part-level actions belong in a header command bar.

3. **Selection-aware behavior**
   - Disable or hide commands that are invalid for the current selection.
   - Provide clear feedback when an action requires selection.

Example command bar:
```tsx
<CommandBar
  items={[
    {
      key: 'newPolicy',
      text: 'New policy',
      iconProps: { iconName: 'Add' },
      onClick: handleNewPolicy
    },
    {
      key: 'export',
      text: 'Export',
      iconProps: { iconName: 'Download' },
      onClick: handleExport
    }
  ]}
/>
```

---

## 6. Placeholders, empty states, and fallbacks

Key refs:
- Placeholders & fallbacks: https://learn.microsoft.com/sharepoint/dev/design/placeholders-and-fallbacks
- Empty states: https://learn.microsoft.com/sharepoint/dev/design/empty-states

Design **first-run** and **no-data** experiences explicitly:

1. **First-run / not configured**
   - Show **what the web part does**, **what is missing**, and a **clear next step**.
   - Include a clear config action: _"Open configuration"_ or link to settings pane.

2. **No data (but configured)**
   - Acknowledge the valid state: _"No risky sites found in the last 30 days."_
   - Offer a meaningful next step if possible: filter changes, documentation, or alternate view.

3. **Fallback content**
   - If some data is unavailable, show **partial** content instead of blocking everything.

Example JSX:
```tsx
if (!isConfigured) {
  return (
    <Placeholder
      iconName="Settings"
      iconText="Set up this web part"
      description="Connect to a data source to see permissions risk for your sites."
      buttonLabel="Open configuration"
      onConfigure={openPropertyPane}
    />
  );
}

if (!items?.length) {
  return (
    <EmptyState
      title="No risky sites found"
      description="We didn't find any sites that match your risk filters for this period."
    />
  );
}
```

---

## 7. Accessibility basics (design side)

Reference: https://learn.microsoft.com/sharepoint/dev/design/accessibility

Design decisions must support:

1. **Keyboard and focus**
   - All interactive elements must be reachable via Tab.
   - Visual focus indicator must be clearly visible against the background.

2. **Semantics**
   - Use semantic elements: `<button>`, `<a>`, `<header>`, `<main>`, `<section>`, `<table>`.
   - Use ARIA roles/labels **only when necessary** to supplement semantics.

3. **Color & contrast**
   - Do not rely on color alone to convey meaning (use icons/text as well).
   - Respect SharePoint theme tokens and ensure WCAG AA contrast.

Example focus treatment (SCSS):
```scss
.button {
  border-radius: 2px;

  &:focus-visible {
    outline: 2px solid var(--focusBorder, #005a9e);
    outline-offset: 2px;
  }
}
```

---

## 8. Performance-aware design decisions

Design choices affect performance:

1. **Above-the-fold clarity**
   - Show primary summary metrics or table quickly; defer expensive details.

2. **Progressive rendering**
   - Consider a **lightweight summary view** for large datasets, with explicit navigation to detail pages.

3. **Config vs default behavior**
   - Pick safe, performant defaults (shorter time windows, scoped data) and allow power users to expand.

---

## 9. How to use this skill in practice

When an AI editor is asked to design or adjust SPFx UX:

1. **Identify** the surface: web part vs extension, first-run vs daily use.
2. **Apply**:
   - Section 2–3 for structure and layout.
   - Section 4–5 for titles, text, and commanding.
   - Section 6–7 for states and accessibility.
3. **Propose** concrete JSX/SCSS snippets that follow these patterns.
4. **Check**: Is the result understandable, accessible, responsive, and performant for an enterprise tenant?
