# StorageClass (SC)

A StorageClass refers to a large storage resource pool composed of many physical disks. This platform supports the creation of block StorageClass, local StorageClass, and custom StorageClass after accessing various storage vendors, and then dynamically configures data volumes for workloads.

## Create StorageClass (SC)

Currently, it supports creating StorageClass through YAML and forms. These two methods have their own advantages and disadvantages, and can meet the needs of different users.

- There are fewer steps and more efficient creation through YAML, but the threshold requirement is high, and you need to be familiar with the YAML file configuration of the StorageClass.

- It is more intuitive and easier to create through the form, just fill in the corresponding values ​​according to the prompts, but the steps are more cumbersome.

### YAML creation

1. Click the name of the target cluster in the cluster list, and then click `Container Storage`->`StorageClass (SC)`->`YAML Creation` in the left navigation bar.

    

2. Enter or paste the prepared YAML file in the pop-up box, and click `OK` at the bottom of the pop-up box.

    > Supports importing YAML files from local or downloading and saving filled files to local.

    

### Form Creation

1. Click the name of the target cluster in the cluster list, and then click `Container Storage`->`StorageClass (SC)`->`Create StorageClass (SC)` in the left navigation bar.

    

2. Fill in the basic information and click `OK` at the bottom.

    **CUSTOM STORAGE SYSTEM**

    - The StorageClass name, driver, and reclamation policy cannot be modified after creation.
    - CSI storage driver: A standard Kubernetes-based container storage interface plug-in, which must comply with the format specified by the storage manufacturer, such as `rancher.io/local-path`.

        - For how to fill in the CSI drivers provided by different vendors, please refer to the official Kubernetes document [Storage Class](https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner).
    - Recycling policy: When deleting a data volume, keep the data in the data volume or delete the data in it.
    - Snapshot/Expansion: After it is enabled, the data volume/data volume declaration based on the StorageClass can support the expansion and snapshot features, but **the premise is that the underlying storage driver supports the snapshot and expansion features**.

    **Hwameistor storage system**

    - The StorageClass name, driver, and reclamation policy cannot be modified after creation.
    - Storage system: Hwameistor storage system.
    - Storage type: support LVM, raw disk type
      - `LVM type`: Hwameistor recommended usage method, which can use highly available data volumes, and the corresponding CSI storage driver is: `lvm.hwameistor.io`.
      - `Raw disk data volume`: suitable for high availability cases, without high availability capability, the corresponding CSI driver is: `hdd.hwameistor.io`
    - High Availability Mode: Before using the high availability capability, please make sure `DRDB component` has been installed. After the high availability mode is turned on, the number of data volume copies can be set to 1 and 2. Convert data volume copy from 1 to 1 if needed
    - Recycling policy: When deleting a data volume, keep the data in the data volume or delete the data in it.
    - Snapshot/Expansion: After it is enabled, the data volume/data volume declaration based on the StorageClass can support the expansion and snapshot features, but **the premise is that the underlying storage driver supports the snapshot and expansion features**.

    

## Update StorageClass (SC)

On the StorageClass list page, find the StorageClass that needs to be updated, and select Edit under the operation bar on the right to update the StorageClass.



!!! info

    Select `View YAML` to view the YAML file of the StorageClass, but editing is not supported.

## Delete StorageClass (SC)

On the StorageClass list page, find the StorageClass to be deleted, and select Delete in the operation column on the right.

