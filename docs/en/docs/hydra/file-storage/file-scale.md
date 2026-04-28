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
