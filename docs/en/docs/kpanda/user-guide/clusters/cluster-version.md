---
MTPE: windsonsea
date: 2024-01-08
---

# Supported Kubernetes Versions

In DCE 5.0, the [integrated clusters](cluster-status.md) and [created clusters](./cluster-status.md) have different version support mechanisms.

This page focuses on the version support mechanism for created clusters.

The Kubernetes community supports three version ranges: 1.26, 1.27, and 1.28. When a new version
is released by the community, the supported version range is incremented. For example, if the
latest version released by the community is 1.27, the supported version range by the community
will be 1.27, 1.28, and 1.29.

To ensure the security and stability of the clusters, when creating clusters
in DCE 5.0, the supported version range will always be one version lower than the community's
version.

For instance, if the Kubernetes community supports v1.25, v1.26, and v1.27, then the
version range for creating worker clusters in DCE 5.0 will be
v1.24, v1.25, and v1.26. Additionally, a stable version, such as 1.24.7, will be recommended to users.

Furthermore, the version range for creating worker clusters in DCE 5.0
will remain highly synchronized with the community. When the community version increases
incrementally, the version range for creating worker clusters in
DCE 5.0 will also increase by one version.

## Supported Kubernetes Versions

<table>
  <thead>
    <tr>
      <th>Kubernetes Community Versions</th>
      <th>Created Worker Cluster Versions</th>
      <th>Recommended Versions for Created Worker Cluster</th>
      <th>DCE 5.0 Installer</th>
      <th>Release Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>1.26</li>
          <li>1.27</li>
          <li>1.28</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>1.26</li>
          <li>1.27</li>
          <li>1.28</li>
        </ul>
      </td>
      <td><strong>1.27.5</strong></td>
      <td>v0.13.0</td>
      <td>2023.11.30</td>
    </tr>
  </tbody>
</table>
