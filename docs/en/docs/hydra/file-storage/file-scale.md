# File Storage Expansion

The platform provides 500Gi space for each cluster file storage by default. This article introduces how to expand the storage capacity of file storage.

!!! note

    "Storage capacity" in K8s is a logical unit, not a physical unit. It is only used in K8s to apply for PVs larger than the specified capacity. File storage expansion requires the CSI plugin corresponding to StorageClass and underlying storage support.

## Default Storage Capacity Expansion

The platform provides two ways to modify the default storage capacity.

!!! note

    The following modification methods only take effect for newly created file storage. For already created file storage, refer to the next section "Expand Created File Storage".

- Method 1: When installing Global component, modify the hydra product settings values.yaml in the manifests.yaml file

    ```yaml
    hydra:
      ...
      variables:
        # StorageClass used by PVC dynamic PV creation for storage service
        global.config.file_storage.storage_class_name: hydra-file-storage
        # Namespace where PVC is created for storage service
        global.config.file_storage.pvc_namespace: hydra-system
        # Storage capacity applied when PVC is created for storage service
        global.config.file_storage.capacity: 500Gi
    ```

- Method 2: If the product is already installed, go to **Global Service Cluster** -> **ConfigMaps and Secrets** -> **ConfigMaps**,
  and find the ConfigMap named **hydra** in the **hydra-system** namespace. The configuration fields are the same as those in Method 1.

    ```yaml
    file_storage:
      storage_class_name: "hydra-file-storage"
      pvc_namespace: "hydra-system"
      capacity: "500Gi"
    ```

    ![Modify the ConfigMap](../images/file-scale01.png)

## Expand an Existing File Storage

To expand an already created file storage, follow the steps below.

!!! note

    Whether online expansion is supported (the Pod is already mounted and running) depends on the underlying
    storage. Otherwise, the Pod must be stopped before the expansion.

1. Go to **Container Management** -> **Global Service Cluster Details** -> **Custom Resources**, and find the
   **filesstorages.storage.hydra.io** resource.

    ![Custom Resource](../images/file-scale02.png)

2. Click the custom resource name to enter the details page. Based on the **workspace ID** and the **cluster name**,
   find the CR instance of the target cluster, and click **Edit YAML**.

    CR instance naming rule: ws-{workspace ID}-{cluster name}-{random string}

    ![File Storage CR Instance](../images/file-scale03.png)

3. In the YAML file, modify the **spec.capacity** parameter to complete the storage capacity expansion.

    ![Modify the Storage Capacity](../images/file-scale04.png)
