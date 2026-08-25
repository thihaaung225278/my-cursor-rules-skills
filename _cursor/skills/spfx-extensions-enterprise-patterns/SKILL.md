---
name: spfx-extensions-enterprise-patterns
description: Enterprise patterns for SPFx extensions including dialogs, commands, and host-safe UX.
---

# SPFx Extensions Enterprise Patterns

## Use for

1. Application Customizer, Field Customizer, and ListView Command Set work.
2. Custom dialog patterns within SPFx extensions.
3. Command interaction and discoverability quality.

## Do not use for

1. Web-part-only behavior not involving extensions.
2. Toolchain-only issues.

## Trigger conditions

1. Extension feature implementation or refactor.
2. Command surface, dialog, or host-page integration updates.

## Enterprise guardrails

1. Respect host context and avoid disruptive overlays.
2. Keep command behavior predictable and reversible.
3. Ensure accessibility in dialogs and command flows.

## Output expectations

1. Safe and polished extension user experience.
2. Minimal host-page side effects.

## Typical target paths (any SPFx project)

1. `src/extensions/**`
2. `src/shared/**`

