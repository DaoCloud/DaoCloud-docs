# Install via Helm Chart

This installation method is recommended, and any component of HwameiStor can be easily installed through Helm Charts.

## steps

1. Prepare Helm tools

    Install the [Helm](https://helm.sh/) command-line tool, see the [Helm Documentation](https://helm.sh/docs/).

2. Download `hwameistor` Repo

    Download and unzip the Repo file locally

    ```console
    helm repo add hwameistor http://hwameistor.io/hwameistor

    helm repo update hwameistor

    helm pull hwameistor/hwameistor --untar
    ```

3. Install HwameiStor

    ```console
    helm install hwameistor ./hwameistor \
        -n hwameistor --create-namespace
    ```

!!! success

    The installation is complete! To verify the installation effect, please refer to the next chapter [Post-check](./post-check.md).

## Use the mirror warehouse mirror

!!! tip

    The default registries are `quay.io` and `ghcr.io`.
    If you can’t access it, you can try to use the mirror sources provided by DaoCloud: `quay.m.daocloud.io` and `ghcr.m.daocloud.io`.

To switch the mirroring of the registry, use `--set` to change the values ​​of these two parameters: `k8sImageRegistry` and `hwameistorImageRegistry`.

```console
helm install hwameistor ./hwameistor \
    -n hwameistor --create-namespace \
    --set k8sImageRegistry=k8s-gcr.m.daocloud.io \
    --set hwameistorImageRegistry=ghcr.m.daocloud.io
```

## Customize kubelet root directory

!!! warning

    The default `kubelet` directory is `/var/lib/kubelet`.
    If your Kubernetes distribution uses a different `kubelet` directory, the parameter `kubeletRootDir` must be set.

For example, on [Canonical's MicroK8s](https://microk8s.io/) using `/var/snap/microk8s/common/var/lib/kubelet/` as the `kubelet` directory, HwameiStor needs to be configured as follows Install:

```console
helm install hwameistor ./hwameistor \
    -n hwameistor --create-namespace \
    --set kubeletRootDir=/var/snap/microk8s/common/var/lib/kubelet/
```

## Production environment installation

The production environment requires:

- Specify resource configuration
- Avoid deploying to the Master node
- Enables fast failover of controllers
  
Some recommended values ​​are provided in the `values.extra.prod.yaml` file, the specific usage is:

```console
helm install hwameistor ./hwameistor \
    -n hwameistor --create-namespace \
    -f ./hwameistor/values.yaml \
    -f ./hwameistor/values.extra.prod.yaml
```

!!! warning

    In a resource-constrained test environment, setting the above values ​​will cause the Pod to fail to start!

## (Optional) Install DRBD

If you want to enable highly available volumes, you must install DRBD

```console
helm pull hwameistor/drbd9-adapter --untar

helm install drbd9 ./drbd9-adapter \
    -n hwameistor --create-namespace
```

Domestic users can use the mirror warehouse `daocloud.io/daocloud` to speed up

```console
helm install drbd-adapter ./drbd-adapter \
    -n hwameistor --create-namespace \
    --set registry=daocloud.io/daocloud
```