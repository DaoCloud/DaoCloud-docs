---
hide:
  - navigation
MTPE: windsonsea
date: 2026-06-30
---

# SeaweedFS object storage Release Notes

This page lists the Release Notes of SeaweedFS object storage, so that you can understand the evolution path and feature changes of each version.

*[mcamel-seaweedfs]: "mcamel" is the dev name for DaoCloud's middlewares, and SeaweedFS is an open-source distributed object storage middleware

## 2026-06-30

### v0.1.4

- **Added** SeaweedFS lifecycle management
- **Added** LevelDB2 support as the Filer Meta Store, with instance types returned in the Pod list
- **Added** Master, Filer, and Volume ready counts (`pod_ready_num`) to the instance Pod list
- **Added** database connectivity checks
- **Added** Japanese translations for the frontend
- **Fixed** instance status display issues
- **Fixed** Dashboard display issues
- **Fixed** API version issues in the OpenAPI documentation
- **Fixed** UI display and version issues
- **Improved** parameter validation, and simplified Filer and Master exposure and storage configurations
- **Improved** sensitive field handling by automatically filling sensitive fields before validation to avoid repeated input
- **Upgraded** SeaweedFS to 4.35, including intermediate versions 4.19, 4.20, 4.21, 4.22, and 4.25, and added e2e test cases
