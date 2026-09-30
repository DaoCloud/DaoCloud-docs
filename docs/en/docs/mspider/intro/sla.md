# Mesh Vulnerability Fix Standards and Plan

This solution aims at design in technical implementation, detection, and fix. Actual situations of enterprise projects may vary. Please confirm with the specific contact person and contract content.

## Scanning Solution

DCE uses `trivy` as the image vulnerability scanning tool by default, and all modules are scanned when released.

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
 
# The parameters that this shell receives look like this ：
# HIGH,CRITICAL release-ci.daocloud.io/mspider/mspider:v0.8.3-47-gd3ac6536  release-ci.daocloud.io/mspider/mspider-api-server:v0.8.3-47-gd3ac6536
# so need use firtParameter parameter to skip first Parameter HIGH,CRITICAL than trivy images
firtParameter=1
for i in "$@"; do
    if (($firtParameter == 1)); then
        ((firtParameter = $firtParameter + 1))
    else
        trivy image --skip-dirs istio.io/istio --ignore-unfixed --db-repository=${TRIVY_DB_REPOSITORY} --exit-code 1 --severity $1 $i
    fi
done
```

## Vulnerability Fix Policy

### Cases Where Vulnerabilities Are Not Fixed

1. **Vulnerabilities out of the scanning scope**:

    - When scanning with `trivy image --ignore-unfixed --db-repository=ghcr.io/aquasecurity/trivy-db`, known but unfixed vulnerabilities will not be scanned.
    - trivy officially updates publicly disclosed vulnerabilities and their fix status periodically.
    - If trivy-db does not mark it as fixed, the upstream component where the vulnerability resides has not yet provided a fixed version.

2. **Differences among scanning tools**:

    If vulnerabilities found by other scanning tools are inconsistent with the trivy scanning results, the trivy results prevail.

3. **Vulnerabilities that are explicitly unfixable**:

    Vulnerabilities explicitly marked as unfixable in specific modules (such as DCE5) will not be handled. For the detailed list, see [Vulnerability Fix Policy](#vulnerability-fix-policy).

4. **Low-risk vulnerabilities**:

    Vulnerabilities with a risk level lower than CRITICAL are not fixed by default.

5. **Module versions that are no longer maintained**:

    For module versions that are beyond the maintenance cycle, vulnerabilities will not be fixed. Please upgrade to a new version.

### Vulnerability Fix Plan

1. **CRITICAL vulnerabilities**:

    - In the CI/CD process, once a CRITICAL vulnerability is detected, it will be fixed immediately.
    - It is guaranteed that all known CRITICAL vulnerabilities are fixed when each module version is released, otherwise the new version will not be released.

2. **Continuous scanning after a version release**:

    After a new version is released, trivy scanning will continue to be used during the development of the next version, ensuring that CRITICAL vulnerabilities will not reappear.

3. **HIGH vulnerabilities**:

    - For HIGH vulnerabilities, a fix support request needs to be submitted, and the R&D team will evaluate and make a decision:
        - **Fixable vulnerabilities**: The fix is expected to be completed within 1-2 iteration cycles, usually within two months.
        - **Unfixable vulnerabilities**: They will be added to the list of unfixable vulnerabilities with a detailed explanation.

## List of Vulnerabilities Marked as Unfixable

```text
CVE-2019-12900
CVE-2019-14697
CVE-2019-17571
CVE-2019-20444
CVE-2019-20445
CVE-2019-8457
CVE-2020-35527
CVE-2021-20231
CVE-2021-20232
CVE-2021-22945
CVE-2021-33574
CVE-2021-3520
CVE-2021-35942
CVE-2021-3711
CVE-2021-44906
CVE-2022-0686
CVE-2022-1292
CVE-2022-1471
CVE-2022-1664
CVE-2022-22965
CVE-2022-23218
CVE-2022-23219
CVE-2022-25845
CVE-2022-29155
CVE-2022-3515
CVE-2022-37601
CVE-2022-4116
CVE-2022-47629
CVE-2023-20873
CVE-2022-45047

# mspider ignore list, see: https://gitlab.daocloud.cn/ndx/mspider/-/blob/main/.trivyignore
# cannot ignore istio library, these vulnerabilities have been fixed after 1.14.1, so ignore
CVE-2022-31045
CVE-2019-12995
CVE-2019-14993
CVE-2021-39155
CVE-2022-23635

# insight ignore list, see: https://gitlab.daocloud.cn/ndx/engineering/insight/insight/-/blob/main/.trivyignore
## k8s.gcr.io/kube-state-metrics/kube-state-metrics:v2.6.0
CVE-2022-1996
## only use in e2e testing
## 10.5.14.30/elastic.m.daocloud.io/kibana/kibana:7.16.3
CVE-2023-46233

# ignore helm vulnerability, this vulnerability has been fixed after 3.9.2. (related to k8s)
CVE-2022-27664

# git vulnerability
CVE-2022-23521
CVE-2022-41903

CVE-2022-1586
CVE-2022-1587
CVE-2021-46848
CVE-2022-37434

## docker.m.daocloud.io/grafana/grafana:9.3.14
CVE-2023-49569

# mcamel ignore list:
CVE-2023-46233
CVE-2022-36760
CVE-2023-25690
CVE-2023-38545
CVE-2022-24963
CVE-2023-45871
```
