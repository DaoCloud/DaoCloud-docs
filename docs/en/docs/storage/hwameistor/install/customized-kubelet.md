---
hide:
   - toc
---

# Customize the Kubelet Root Directory

!!! warning

    The default `kubelet` directory is `/var/lib/kubelet`. If your Kubernetes distribution uses a different `kubelet` directory, you must set the parameter `kubeletRootDir`.

For example, if using [Canonical's MicroK8s](https://microk8s.io/), the `kubelet` directory is `/var/snap/microk8s/common/var/lib/kubelet/`.

1. To modify the `kubeletRootDir` parameter through the interface operation, go to `Global Settings` -> `Kubelet Root Dir`, and set the parameter to `/var/snap/microk8s/common/var/lib/kubelet/`. For details, refer to the [Create via UI](deploy-ui.md) documentation.

2. If deploying with Helm, run the following installation command.

    ```console
    helm install hwameistor ./hwameistor \
        -n hwameistor --create-namespace \
        --set kubeletRootDir=/var/snap/microk8s/common/var/lib/kubelet/
    ```
