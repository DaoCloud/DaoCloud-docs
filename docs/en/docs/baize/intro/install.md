# Initialize Computing Cluster

By default, when installing DCE 5.0 Enterprise, the Baize Module can be installed synchronously. Please contact the delivery support team to obtain the Enterprise installation package.

## Baize Module

Ensure that the Baize components have been installed in the global management cluster.
You can verify this by checking if the Baize module is available through the DCE 5.0 UI.

!!! info

    There is an entry for `Baize` in the primary navigation bar.

If it is not available, you can install it using the following method.
Please note that it needs to be installed in the `kpanda-global-cluster` global management cluster:

```bash
# "baize" is the development codename for the Baize component
helm repo add baize https://release.daocloud.io/chartrepo/baize
helm repo update
export VERSION=v0.1.1
helm upgrade --install baize baize/baize \
    --create-namespace \
    -n baize-system \
    --set global.imageRegistry=release.daocloud.io \
    --version=${VERSION}
```

If you are installing in an existing `DCE` environment, you can add the `helm` source to the container management and also use a graphical installation method.

## Initialize Worker Cluster

In each worker cluster with computing resources, the corresponding basic computing components need to be deployed. The main components include:

- `gpu-operator`: Initializes the GPU resources in the cluster.
  **The installation method may vary depending on the type of GPU resources.**
  For details, refer to [GPU Management](../../kpanda/user-guide/gpu/index.md).
- `insight-agent`: Observability component used to collect infrastructure information
  in the cluster, including logs, metrics, and events
- `baize-agent`: Core component of the Baize module, responsible for
  scheduling, monitoring, Pytorch, Tensorflow, and other computing components
- `nfs`: Storage service used for dataset preheating

!!! danger

    **The above components must be installed, otherwise it may cause the functionality to not work properly.**

After completing the above tasks, you can now perform task training and model development
in the Baize module. For detailed usage, you can refer to the following:

### Introduction to Preheating Components

In the data management provided by the Baize module, the preheating capability of
datasets relies on a storage service, and it is recommended to use an NFS service:

- Deploy NFS Server
    - If NFS already exists, you can skip this step
    - If it does not exist, you can refer to the best practices for
      [Deploying NFS Service](../../baize/best-practice/deploy-nfs-in-worker.md)
- Deploy `nfs-driver-csi`
- Deploy `StorageClass`

## Conclusion

After completing the above tasks, you can now experience all the functionalities of
Baize in the worker cluster. Enjoy using it!
