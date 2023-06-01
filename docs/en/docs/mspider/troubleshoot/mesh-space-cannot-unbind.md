# Unable to unbind mesh space

## Problems

- Mesh type: Hosted mesh
- Istio version: 0.16.1-mspider

After renaming the workspace managed by Global Management, the mesh space cannot be unbound properly;
Similarly, after unbinding the space in Global Management, the service mesh still shows binding and cannot be unbound. The space deleted by Global Management cannot be unbound in the mesh space.

## Analysis

The service mesh has cached the workspace and needs to clean up dirty data from the cache.

## Solution

1. Enter $ClusterName where the proper mesh instance is deployed and find the mesh-hosted-apiserver.

    ```text
    /kpanda/clusters/$ClusterName/namespaces/istio-system/pods/mesh-hosted-apiserver-0/containers
    ```

2. Use the console to enter the pod internally and adjust the kubectl command's permissions.

    ```shell
    kubeadm init phase kubeconfig admin
    alias kubectl="kubectl --kubeconfig=/etc/kubernetes/admin.conf --insurce-skip-tls-verify"
    ```

3. Use the following command to remove the annotation from the proper namespace.

    ```shell
    kubectl annotate ns $namespace controller.mspider.io/workspace-id- controller.mspider.io/workspace-name-
    ```
