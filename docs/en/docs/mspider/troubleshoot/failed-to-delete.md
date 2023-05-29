---
hide:
   - toc
---

# The created mesh is abnormal but cannot be deleted

## Cause Analysis

The mesh is in a failed state and the mesh instance cannot be clicked.
Because the cluster is managed, a mesh gateway instance is created, or sidecar injection is enabled in the mesh, the detection always fails when the mesh is removed, so it cannot be deleted normally.

## Solution

It is recommended to troubleshoot the cause of the failure of the specific mesh and solve it. If you want to delete it forcefully, please do the following:

1. Disable sidecar injection for managed clusters

     1. Disable namespace sidecar automatic injection.

         In `Container Management`, select the cluster -> `Namespace` -> Modify the label —> remove the `istio-injection: enabled` label, and restart all Pods under the namespace.

         

     1. Disable workload sidecar injection:

         In `Container Management`, select the cluster -> `Workload` —> `Stateless Load` —> `Labels and Annotations` —> remove `sidecar.istio.io/inject: true` label.

         

1. Delete the created mesh gateway instance.

1. Remove the cluster.

     In `Container Management`, select the global cluster, and search `globalmeshes.discovery.mspider.io` for custom resources.
     Select the mesh to remove the cluster under the mspider-system namespace, and edit the YAML:

     

1. Return to the service mesh and delete the mesh instance.