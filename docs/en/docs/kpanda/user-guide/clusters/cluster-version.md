---
MTPE: windsonsea
date: 2024-01-08
---

# Supported Kubernetes Versions

In the DCE platform, [integrated clusters](cluster-status.md) and [created clusters](cluster-status.md) use different version support mechanisms.

This page mainly introduces the version support mechanism for created clusters.

The Kubernetes community supports three version ranges, such as 1.30, 1.31, and 1.32. When a new version is released by the community, the supported version range is incremented.
For example, if the latest community version 1.32 has already been released, the version range supported by the community is 1.30, 1.31, and 1.32.
[View the latest version range supported by the Kubernetes community](https://kubernetes.io/releases/version-skew-policy/#supported-versions).

To ensure the security and stability of clusters, the version range supported when creating a cluster through the interface in DCE is consistent with the community version, but the recommended version is always **one version lower** than the Kubernetes community.

For example, if the version range supported by the community is 1.30, 1.31, and 1.32, then the version range for creating worker clusters through the interface in DCE is 1.30, 1.31, and 1.32, and a stable version such as v1.31.6 will be recommended to users.

In addition, the version range for creating worker clusters through the interface in DCE stays highly synchronized with the community. When the community version is incremented, the version range for creating worker clusters through the interface in DCE is also incremented by one version accordingly.

## Kubernetes Version Support Range

| Kubernetes Community Version Range | Created Worker Cluster Version Range | Recommended Version for Created Worker Clusters | DCE Installer | Release Date |
|------------------|------------------|------------------|--------------|--------|
| <ul><li>1.30</li><li>1.31</li><li>1.32</li></ul> | <ul><li>1.30</li><li>1.31</li><li>1.32</li></ul> | v1.31.6 | v0.28.0 | 2025/4/11 |

![Version Support Mechanism](../images/clusterversion1.png)
