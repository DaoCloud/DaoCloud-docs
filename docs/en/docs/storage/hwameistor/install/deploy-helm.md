---
hide:
   - toc
---

# Install via Helm Chart

Any component of HwameiStor can be installed through Helm Chart.

## Prerequisites

- Free HDD and SSD disks have been prepared on the nodes to be used
- Completed the items in [Preparation](prereq.md)
- If you need to use highly available data volumes, please complete [DRDB installation](drbdinstall.md) in advance
- If the deployment environment is a production environment, please read [Resource Requirements for Production Environment](proresource.md) in advance
- If your Kubernetes distribution uses a different `kubelet` directory, please confirm `kubeletRootDir` in advance.
   For details, please refer to [Customize Kubelet root directory](customized-kubelet.md).

## Steps

1. Prepare the Helm tool, install the [Helm](https://helm.sh/) command-line tool, see the [Helm Documentation](https://helm.sh/docs/).

2. Download `hwameistor` Repo, download and decompress the Repo file to local:

    ```console
    helm repo add hwameistor http://hwameistor.io/hwameistor
    helm repo update hwameistor
    helm pull hwameistor/hwameistor --untar
    ```

3. Install HwameiStor, named as follows:

    ```console
    helm install hwameistor ./hwameistor \
        -n hwameistor --create-namespace
    ```


!!! tip

    The default registries are `registry.k8s.io` and `ghcr.io`.
    
    If you can't access it, you can try to use the mirror sources provided by DaoCloud: `m.daocloud.io` and `ghcr.m.daocloud.io`.

To switch the mirroring of the registry, use `--set` to change the values of these two parameters: `global.k8sImageRegistry` and `global.hwameistorImageRegistry`.

```console
helm install hwameistor ./hwameistor \
    -n hwameistor --create-namespace \
    --set global.k8sImageRegistry=m.daocloud.io/registry.k8s.io\
    --set global.hwameistorImageRegistry=ghcr.m.daocloud.io
```

!!! success

    The installation is complete! To verify the installation effect, please refer to the next chapter [Post-check](./post-check.md).

If you need to customize the Kubelet root directory, please refer to [Customize the Kubelet root directory](customized-kubelet.md).

The installation is complete! To verify the installation effect, please refer to the next chapter [Post-check](./post-check.md).
