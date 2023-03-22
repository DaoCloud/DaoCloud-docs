---
hide:
  - toc
---

# 自定义 Kubelet 根目录

!!! warning

    默认的 `kubelet` 目录为 `/var/lib/kubelet`。
    如果您的 Kubernetes 发行版使用不同的 `kubelet` 目录，必须设置参数 `kubeletRootDir`。

例如，在将 `/var/snap/microk8s/common/var/lib/kubelet/` 用作 `kubelet` 目录的 [Canonical 的 MicroK8s](https://microk8s.io/) 上。

1. 通过界面操作，HwameiStor 需要需要此修改参数界面中 `Global Setting` —> `Kubelet Root Dir`参数，并将参数设置为 `/var/snap/microk8s/common/var/lib/kubelet/` 。详情参考：[通过界面创建](deploy-ui.md)

2. 如果通过 Helm 创建，请执行如下安装命令。

   ```console
   helm install hwameistor ./hwameistor \
       -n hwameistor --create-namespace \
       --set kubeletRootDir=/var/snap/microk8s/common/var/lib/kubelet/
   ```

   



