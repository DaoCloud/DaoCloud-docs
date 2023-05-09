# Install via Helm Chart

This installation method is recommended, and any component of HwameiStor can be easily installed through Helm Charts.

## Steps

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

## Use the container registry image

!!! tip

    The default registries are `registry.k8s.io` and `ghcr.io`.
    If you can’t access it, you can try to use the image sources provided by DaoCloud: `m.daocloud.io` and `ghcr.m.daocloud.io`.

To switch the image of the registry, use `--set` to change the values ​​of these two parameters: `global.k8sImageRegistry` and `global.hwameistorImageRegistry`.

```console
helm install hwameistor ./hwameistor \
    -n hwameistor --create-namespace \
    --set global.k8sImageRegistry=m.daocloud.io/registry.k8s.io \
    --set global.hwameistorImageRegistry=ghcr.m.daocloud.io
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
helm repo add hwameistor https://hwameistor.io/hwameistor

helm repo update hwameistor

helm pull hwameistor/drbd-adapter --untar

helm install drbd-adapter ./drbd-adapter -n hwameistor --create-namespace
```

Domestic users can use the container registry `daocloud.io/daocloud` to speed up

```console
helm install drbd-adapter ./drbd-adapter \
    -n hwameistor --create-namespace \
    --set imagePullPolicy=Always \
    --set registry=daocloud.io/daocloud
```