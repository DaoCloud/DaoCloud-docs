---
hide:
  - toc
---

# cluster management

The cluster management page of the service mesh provides users with cluster access and removal features.

**Cluster access is the first step for a cluster to join the mesh management boundary**.

The connected cluster will appear in the cluster list managed by the sidecar, and then the user can enable sidecar injection for the namespace and workload of the cluster to achieve aggregated management and control of the cluster.

This feature is only valid in the __hosted mesh__ , and it is not available in the __proprietary mesh__ and __external mesh__ modes. For details, see [Service Mesh Classification](../service-mesh/README.md).
The hosting mesh adopts a single control plane multicluster approach to achieve uniform acquisition of service registration information and issue governance policies for multiple clusters. The control plane components of each hosting cluster are only responsible for accepting and forwarding policies from the control plane of the only management cluster, and do not run any policies. Policies created locally.