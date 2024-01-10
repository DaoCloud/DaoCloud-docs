# Unable to unbind mesh space

## Problems

- Mesh type: Hosted mesh
- Istio version: 0.16.1-mspider

After renaming the workspace managed by [Global Management](../../ghippo/intro/index.md),
the mesh space cannot be unbound properly; Similarly, after unbinding the space in
Global Management, the service mesh still shows binding and cannot be unbound.
The space deleted by Global Management cannot be unbound in the mesh space.

## Analysis

The service mesh has cached the workspace and needs to clean up dirty data from the cache.

## Solution

1. If it is a hosted mesh, go to the $ClusterName where the corresponding
   mesh instance is deployed and find mesh-hosted-apiserver.

    ```text
    /kpanda/clusters/$ClusterName/namespaces/istio-system/pods/mesh-hosted-apiserver-0/containers
    ```

    If it is a dedicated mesh, perform the operation directly in the proper cluster.

2. Use the following command to remove the annotations from the namespace:

    ```shell
    kubectl annotate ns $namespace controller.mspider.io/workspace-id- controller.mspider.io/workspace-name-
    ```
