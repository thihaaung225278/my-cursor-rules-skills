---
name: spfx-css-and-styling-governance
description: CSS architecture and styling governance for SPFx components.
---

# SPFx CSS and Styling Governance

## Use for

1. CSS module structure and style isolation.
2. Naming consistency and maintainability in SCSS files.
3. Preventing style collisions across web parts.

## Do not use for

1. Introducing new styling frameworks by default.
2. Rewriting stable component styles without value.

## Trigger conditions

1. New style layer or major visual refresh.
2. CSS conflicts, leakage, or maintainability issues.

## Enterprise guardrails

1. Keep styling local and explicit.
2. Maintain Fluent-aligned visual language — **except** this repo classic → SPFx: match `DBS-FFW-classicsite/2025/style.css` (`classic-visual-parity`). Isolation still required.
3. No Tailwind in `spfx-solution` unless explicitly approved.

## Output expectations

1. Predictable styling behavior.
2. Easier long-term style maintenance.

## Typical target paths (any SPFx project)

1. `src/**/**/*.module.scss`
2. `src/shared/components/**`

