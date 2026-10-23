---
hide:
  - toc
---

# Compatibility

This page lists the compatibility test results between ClawOS Agent and Kubernetes clusters to help you choose an appropriate cluster version.

✅: Test passed; ❌: Test failed or not supported; Blank: Not tested.

## Kubernetes Cluster Compatibility Test

| Scenario | Testing Method | K8s 1.37.0 | K8s 1.36.1 | K8s 1.35.0 | K8s 1.33.0 | K8s 1.31.0 | K8s 1.29.4 | K8s 1.27.16 | K8s 1.25.16 | K8s 1.23.17 |
| -------- | -------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ----------- | ----------- | ----------- |
| Baseline scenario (instance creation/query/deletion) | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Instance lifecycle (stop/start/restart) | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Chat (start a chat from the quick entry) | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Model configuration (primary/fallback model) | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Skill marketplace (skill publishing and review) | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Global skill marketplace (global skill publishing) | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Network policy template management (create/enable/disable/bind/delete) | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Network policy traffic control (Ingress access control) | E2E | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |

!!! note

    **Testing notes:**

    1. Compatibility tests are based on the AgentClaw E2E suite and run against kind clusters for each Kubernetes version listed above. The scope is smoke test cases.
    2. Network policy traffic control depends on the CNI implementation of NetworkPolicy. In kind clusters running K8s 1.2x (v1.23, v1.25, v1.27, and v1.29), the default CNI (kindnet) does not support NetworkPolicy, so this scenario is not supported on these versions. Network policy template management is not affected.
    3. To use network policy traffic control in production, make sure your cluster CNI supports NetworkPolicy. K8s 1.31.0 or later is recommended.

    **Supported Kubernetes versions:** v1.23.17, v1.25.16, v1.27.16, v1.29.4, v1.31.0, v1.33.0, v1.35.0, v1.36.1, v1.37.0.
