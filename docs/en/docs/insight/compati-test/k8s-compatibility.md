---
hide:
  - toc
---

# Kubernetes Cluster Compatibility Test

✅: Test passed; ❌: Test failed; No Value: Test not conducted. 

## Kubernetes Compatibility Testing for Insight Server

| Scenario | Testing Method | K8s 1.36.1 | K8s 1.35.0 | K8s 1.34.0 | K8s 1.33.0 | K8s 1.32.0 | K8s 1.31.0 | K8s 1.30.0 | K8s 1.29.2 | K8s 1.28.0 | K8s 1.27.1 | K8s 1.26.0 | K8s 1.25.3 | K8s 1.24.7 | K8s 1.23.13 |
| --------- | ------------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| Baseline Scenario | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Metrics Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Logs Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Traces Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Alert Center | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Topology Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Kubernetes Compatibility Testing for Insight-agent

| Scenario | Testing Method | K8s 1.36.1 | K8s 1.35.0 | K8s 1.34.0 | K8s 1.33.0 | K8s 1.32.0 | K8s 1.31.0 | K8s 1.30.0 | K8s 1.29.2 | K8s 1.28.0 | K8s 1.27.1 | K8s 1.26.0 | K8s 1.25.3 | K8s 1.24.7 | K8s 1.23.13 |
| --------- | ------------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| Baseline Scenario | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Metrics Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Logs Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Traces Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Alert Center | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Topology Query | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

!!! note

    **Insight-agent Version Compatibility History:**

    1. Insight Agent is not compatible with k8s v1.16.15 starting from v0.16.x.
    2. Insight Agent v0.20.0 is compatible with k8s v1.18.20.
    3. Insight Agent v0.19.2/v0.18.2/v0.17.x is not compatible with k8s v1.18.20.
    4. Insight Agent is not compatible with k8s v1.22.x and below versions from v0.30.x.
    5. Insight Agent v0.38.0 supports Kubernetes v1.18.20 for metric scenarios.
    6. When Insight Agent v0.43.x uses Prometheus Operator v0.83.0, metric scenarios are compatible with Kubernetes v1.18.20.
