---
name: spfx-enterprise-implementation-core
description: Core implementation standards for enterprise SPFx web parts, extensions, and shared modules.
---

# SPFx Enterprise Implementation Core

## Use for

1. Defining implementation approach for SPFx workloads.
2. Enforcing service boundaries, error handling, and typed contracts.
3. Aligning code changes with enterprise maintainability standards.

## Do not use for

1. Webpack-specific tuning.
2. Pure design/styling decisions without implementation impact.

## Trigger conditions

1. Any new feature or significant refactor in SPFx code.
2. Cross-webpart shared service/component changes.

## Enterprise guardrails

1. Keep changes scoped and reversible.
2. Preserve API contracts unless explicitly requested.
3. Require test updates for changed logic paths.

## Output expectations

1. Clear module boundaries and typed interfaces.
2. Predictable error and loading behavior.
3. No incidental runtime dependency drift.

## Typical target paths (any SPFx project)

1. `src/webparts/**`
2. `src/shared/**`

