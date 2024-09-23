---
hide:
  - toc
---

# Kubernetes Cluster Compatibility Test

✅: Test passed; ❌: Test failed; No Value: Test not conducted. 

## Kubernetes Compatibility Testing for Insight Server

| Scenario | Testing Method | K8s 1.31 | K8s 1.30 | K8s 1.29 | K8s 1.28 | K8s 1.27 | K8s 1.26 | k8s 1.25.0 | k8s 1.24 | k8s 1.23 | k8s 1.22 |
| ------------ | ---------------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |--------- |
| Baseline Scenario  | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Metrics Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Logs Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Traces Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Alert Center  | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Topology Query  | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Kubernetes Compatibility Testing for Insight-agent

| Scenario | Testing Method | K8s 1.31 | K8s 1.30 | K8s 1.29 | K8s 1.28 | K8s 1.27 | K8s 1.26 | k8s 1.25 | k8s 1.24 | k8s 1.23 | k8s 1.22 | k8s 1.21 | k8s 1.20 | k8s 1.19 | k8s 1.18 | k8s 1.17 | k8s 1.16 |
| ------------ | ------------------------ | ---------------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |--------- |--------- |--------- |--------- |--------- |--------- |
| Baseline Scenario | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Metrics Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Logs Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Traces Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Alert Center | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Topology Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |

!!! note

    **Insight-agent Version Compatibility History:**

    1. Insight Agent is not compatible with k8s v1.16.15 starting from v0.16.x.
    2. Insight Agent v0.20.0 is compatible with k8s v1.18.20.
    3. Insight Agent v0.19.2/v0.18.2/v0.17.x is not compatible with k8s v1.18.20.
    4. Insight Agent v0.30.1 is compatible with k8s v1.18.x and below versions.

