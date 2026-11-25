---
MTPE: windsonsea
date: 2026-11-25
---

# Ipavo Release Notes

This page lists the Release Notes of the Ipavo dashboard component, so that
you can understand the evolution path and feature changes of each version.
Insight release notes are on the [Release Notes](release-notes.md) page.

## 2026-10-31

### v0.15.2

- **Added** TokenFactory mode. With `global.tokenfactory.enable=true`, the sidebar menu is not created, while the proxy and version registration stay in place and `/ipavo` remains reachable. After upgrading an existing install with this value, the previous `<release>-menus` resource is removed

## 2026-09-30

### v0.15.1

- **Improved** global-management menu, proxy, and version resource names to follow the Helm release name
- **Improved** those resources with the annotation `argocd.argoproj.io/sync-options: SkipDryRunOnMissingResource=true`, so Argo CD can skip dry-run validation before the Ghippo CRDs are available
- **Improved** UI proxy registration so it is skipped when `ui.enabled` is false
- **Fixed** the built-in MySQL DSN to use `mysql.password` and the image reference to use `mysql.image.repository`

## 2026-08-31

### v0.15.0

- **Upgraded** the server image to **v0.15.0** and the UI image to **v0.13.0**
