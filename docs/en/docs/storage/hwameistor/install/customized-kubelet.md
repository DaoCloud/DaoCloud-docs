---
hide:
   - toc
---

# Customize the Kubelet root directory

!!! warning

     The default `kubelet` directory is `/var/lib/kubelet`.
     If your Kubernetes distribution uses a different `kubelet` directory, the parameter `kubeletRootDir` must be set.

For example, on [Canonical's MicroK8s](https://microk8s.io/) using `/var/snap/microk8s/common/var/lib/kubelet/` as the `kubelet` directory.

1. Through the interface operation, HwameiStor needs to modify `Global Setting` —> `Kubelet Root Dir` parameter in the parameter interface, and set the parameter to
    `/var/snap/microk8s/common/var/lib/kubelet/`. For details, please refer to [Create via UI](deploy-ui.md)

2. If created by Helm, execute the following installation command.

     ```console
     helm install hwameistor ./hwameistor \
         -n hwameistor --create-namespace \
         --set kubeletRootDir=/var/snap/microk8s/common/var/lib/kubelet/
     ```
