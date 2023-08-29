# Supported Kubernetes Versions

In the DCE 5.0 platform, the [integrated clusters and self-built clusters](cluster-status.md) have different version support mechanisms.

This page introduces the version support mechanism for self-built clusters.

The Kubernetes community supports three version ranges: 1.24, 1.25, and 1.26. When a new version is released by the community, the supported version range will increment. For example, if the latest version released by the community is 1.27, then the supported version range by the community will be 1.25, 1.26, and 1.27.

To ensure the security and stability of the clusters, when creating clusters using the interface in DCE 5.0, the supported version range will always be one version lower than the community's version.

For instance, if the community supports version range 1.25, 1.26, and 1.27, then the version range for creating working clusters using the interface in DCE 5.0 will be 1.24, 1.25, and 1.26. Additionally, a stable version, such as 1.24.7, will be recommended to users.

Furthermore, the version range for creating working clusters using the interface in DCE 5.0 will remain highly synchronized with the community. When the community version increases incrementally, the version range for creating working clusters using the interface in DCE 5.0 will also increase by one version.

Kubernetes Version Release Notes

| Kubernetes Community Version Range | Self-built Working Cluster Version Range | Recommended Version for Self-built Working Cluster | DCE 5.0 Version | Release Date |
| ---------------------------------- | ---------------------------------------- | ------------------------------------------------- | -------------- | ------------ |
| 1.25<br>1.26<br>1.27               | 1.24<br>1.25<br>1.26                    | **1.26.5**                                        | V0.7.0         | 2023.05.09   |
