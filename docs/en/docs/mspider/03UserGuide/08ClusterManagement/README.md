---
hide:
  - toc
---

# cluster management

The cluster management page of the service grid provides users with cluster access and removal functions.

**Cluster access is the first step for a cluster to join the grid management boundary**.

The connected cluster will appear in the cluster list managed by the sidecar, and then the user can enable sidecar injection for the namespace and workload of the cluster to achieve aggregated management and control of the cluster.

This function is only valid in the `managed grid`, and it is not available in the `proprietary grid` and `external grid` modes. For details, see [Service Mesh Classification](../servicemesh/README.md).
The hosting grid adopts a single control plane multi-cluster approach to achieve uniform acquisition of service registration information and issue governance policies for multiple clusters. The control plane components of each hosting cluster are only responsible for accepting and forwarding policies from the control plane of the only management cluster, and do not execute any policies. Policies created locally.