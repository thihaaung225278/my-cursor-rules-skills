---
name: spfx-release-and-package-quality
description: Packaging and release quality controls for enterprise SPFx delivery.
---

# SPFx Release and Package Quality

## Use for

1. Pre-release packaging validation.
2. SKU/package profile checks and App Catalog readiness.
3. Compliance between shipped features and release metadata.

## Do not use for

1. Feature implementation details.
2. UI-only tasks not tied to release quality.

## Trigger conditions

1. `package-solution` workflow changes.
2. Release checklist execution or app packaging requests.

## Enterprise guardrails

1. Ensure package outputs are deterministic.
2. Validate solution metadata before release.
3. Catch regressions before tenant deployment.

## Output expectations

1. Release-ready package artifacts.
2. Reduced deployment and rollback risk.

## Typical target paths (any SPFx project)

1. `config/package-solution*.json`
2. `docs/publishing/**`
3. `docs/implementation/**`

