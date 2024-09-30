---
MTPE: windsonsea
date: 2024-05-21
---

# Initialize AI Lab Cluster

Starting from DCE 5.0 installer v0.17.0, the Enterprise package can simultaneously install the AI Lab module
**without requiring separate installation** . Please contact the delivery support team to obtain the Enterprise package.

## Install the AI Lab Module (UI)

> This module only needs to be installed in the [global service cluster](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster).

Use the link below to open the global service cluster, then find `baize`
under __Helm Apps__ -> __Helm Charts__ and follow the installation steps.

!!! note "Important Notes"

    * The namespace should be `baize-system`.
    * After replacing the environment address,
      open `<YOUR_DCE_HOST>/kpanda/clusters/kpanda-global-cluster/helm/charts/addon/baize`.
    * Note the `kpanda-global-cluster` global service cluster.

## Installing the AI Lab Module (CLI)

> The management module only needs to be installed in the global servicemanagement cluster.

Ensure that the AI Lab components are already installed in the global service cluster.
You can confirm this by checking the DCE 5.0 UI for the presence of the AI Lab module.

!!! info

    The primary navigation bar has an `AI Lab` entry.

    If it does not exist, you can install it using the following method.
    Note that it needs to be installed in the `kpanda-global-cluster`, that is, global service cluster:

    ```bash
    # baize is the codename for the AI Lab component
    helm repo add baize https://release.daocloud.io/chartrepo/baize
    helm repo update
    helm search repo baize # Get the latest version number
    export VERSION=<version> # Make sure to use the latest version
    helm upgrade --install baize baize/baize \
        --create-namespace \
        -n baize-system \
        --set global.imageRegistry=release.daocloud.io \
        --version=${VERSION}
    ```

## Initialize Worker Cluster

In each worker cluster with computing resources, the corresponding basic computing components
need to be deployed. The main components include:

- `gpu-operator`: Initializes the GPU resources in the cluster.
  **The installation method may vary depending on the type of GPU resources.**
  For details, refer to [GPU Management](../../kpanda/user-guide/gpu/index.md).
- `insight-agent`: Observability component used to collect infrastructure information
  in the cluster, including logs, metrics, and events
- `baize-agent`: Core component of the AI Lab module, responsible for
  scheduling, monitoring, Pytorch, Tensorflow, and other computing components
- Optional `nfs`: Storage service used for dataset preheating

!!! danger

    **The above components must be installed, otherwise it may cause the functionality to not work properly.**

After completing the above tasks, you can now perform task training and model development
in the AI Lab module.

### Components for preheating

In the data management provided by the AI Lab module, the preheating capability of
datasets relies on a storage service, and it is recommended to use an NFS service:

- Deploy NFS Server
    - If NFS already exists, you can skip this step
    - If it does not exist, you can refer to the best practices for
      [Deploying NFS Service](../../baize/best-practice/deploy-nfs-in-worker.md)
- Deploy `nfs-driver-csi`
- Deploy `StorageClass`

## Conclusion

After completing the above steps, you can now experience all the functionalities of
AI Lab in the worker cluster. Enjoy using it!
