# 网格漏洞修复标准与计划

此方案旨在技术实现、检测及修复方面的设计，企业项目的实际情况可能会有差异，请以具体的对接人员和合同内容为准进行确认。

## 扫描方案

在 DCE 5.0 中默认使用 `trivy` 作为镜像漏洞扫描工具，所有模块在发版时都会进行进行扫描。

- 什么是 trivy？参阅 <https://trivy.dev/>
- 为什么选择 trivy？
    - 全面的漏洞数据库：Trivy 使用广泛的漏洞数据库，包括 NVD（National Vulnerability Database）、Red Hat Security Advisory、Alpine SecDB 等，能够覆盖大量的已知漏洞。
    - 应用程序依赖关系的扫描：除了操作系统层面的漏洞，Trivy 还能扫描各种语言和框架的应用程序依赖关系，例如 Ruby、Python、JavaScript 等。
    - 实时更新：Trivy 定期更新其漏洞数据库，确保能够检测到最新公开的安全漏洞。
    - Trivy 在容器安全领域中被广泛使用

使用方式参考：

扫描的代码如下，参考网格：

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

## 漏洞修复政策

### 漏洞不予修复的情况

1. **不在扫描范围内的漏洞** :

    - 使用 `trivy image --ignore-unfixed --db-repository=ghcr.io/aquasecurity/trivy-db` 进行扫描时，已知但未修复的漏洞将不会被扫描。
    - trivy 官方定期更新公开的漏洞及其修复状态。
    - 如 trivy-db 中未标记为已修复，则漏洞所在的上游组件尚未提供修复版本。

1. **扫描工具的差异** :

    若其他扫描工具发现的漏洞与 trivy 扫描结果不一致，优先采用 trivy 的结果。

1. **明确无法修复的漏洞** :
    
    特定模块（如 DCE5）中明确标记为无法修复的漏洞不会被处理。详细列表请参见[漏洞修复政策](#_3)。

1. **低风险漏洞** :

    风险级别低于 CRITICAL 的漏洞，默认不进行修复。

1. **不再维护的模块版本**:

    对于已经超出维护周期的模块版本，不进行漏洞修复，请升级至新版本。

### 漏洞修复计划

1. **CRITICAL 级别漏洞** :

    - 在 CI/CD 流程中，一旦检测到 CRITICAL 级别的漏洞，将立即进行修复。
    - 保证每个模块发布版本时，已知的所有 CRITICAL 级别漏洞都已修复，否则不发布新版本。

1. **版本发布后的持续扫描** :

    发布新版本后，将在下一版本的开发过程中继续使用 trivy 扫描，确保 CRITICAL 级别漏洞不会重复出现。

1. **HIGH 级别漏洞** :

    - 对于 HIGH 级别的漏洞，需要提交修复支持申请，研发团队将进行评估并给出决策：
        - **可修复的漏洞** ：预计在 1-2 个迭代周期内完成修复，通常在两个月内。
        - **无法修复的漏洞** ：将被添加到无法修复的清单中，并提供详细说明。

## 标记无法修复清单

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
