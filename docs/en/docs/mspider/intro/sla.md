# Mesh Vulnerability Fix Standards and Plan

This solution aims at design in technical implementation, detection, and fix. Actual situations of enterprise projects may vary. Please confirm with the specific contact person and contract content.

## Scanning Solution

DCE 5.0 uses `trivy` as the image vulnerability scanning tool by default, and all modules are scanned when released.

- What is trivy? See <https://trivy.dev/>
- Why choose trivy?
    - Comprehensive vulnerability database: Trivy uses an extensive vulnerability database, including NVD (National Vulnerability Database), Red Hat Security Advisory, Alpine SecDB, etc., covering a large number of known vulnerabilities.
    - Application dependency scanning: In addition to operating system-level vulnerabilities, Trivy can also scan application dependencies for various languages and frameworks, such as Ruby, Python, JavaScript, etc.
    - Real-time updates: Trivy regularly updates its vulnerability database to ensure it can detect the latest publicly disclosed security vulnerabilities.
    - Trivy is widely used in container security field

Reference for usage:

The scanning code is as follows, reference mesh:

```bash
#!/usr/bin/env bash
 
set -o errexit
set -o nounset
set -o pipefail
 
# ignore VULNEEABILITY CVE-2022-1996 it will fix at k8s.io/api next release
# ignore unfixed  VULNEEABILITY
 
TRIVY_DB_REPOSITORY=${TRIVY_DB_REPOSITORY:-ghcr.io/aquasecurity/trivy-db}
```
