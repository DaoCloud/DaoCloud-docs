# storage pool (SC)

A storage pool refers to a large storage resource pool composed of many physical disks. This platform supports the creation of block storage pools, local storage pools, and custom storage pools after accessing various storage vendors, and then dynamically configures data volumes for workloads.

## Create storage pool (SC)

Currently, it supports creating storage pools through YAML and forms. These two methods have their own advantages and disadvantages, and can meet the needs of different users.

- There are fewer steps and more efficient creation through YAML, but the threshold requirement is high, and you need to be familiar with the YAML file configuration of the storage pool.

- It is more intuitive and easier to create through the form, just fill in the corresponding values ​​according to the prompts, but the steps are more cumbersome.

### YAML creation

1. Click the name of the target cluster in the cluster list, and then click `Container Storage`->`Storage Pool (SC)`->`YAML Creation` in the left navigation bar.

    

2. Enter or paste the prepared YAML file in the pop-up box, and click `OK` at the bottom of the pop-up box.

    > Supports importing YAML files from local or downloading and saving filled files to local.

    

### Form Creation

1. Click the name of the target cluster in the cluster list, and then click `Container Storage`->`Storage Pool (SC)`->`Create Storage Pool (SC)` in the left navigation bar.

    

2. Fill in the basic information and click `OK` at the bottom.

    **CUSTOM STORAGE SYSTEM**

    - The storage pool name, driver, and reclamation policy cannot be modified after creation.
    - CSI storage driver: A standard Kubernetes-based container storage interface plug-in, which must comply with the format specified by the storage manufacturer, such as `rancher.io/local-path`.

        - For how to fill in the CSI drivers provided by different vendors, please refer to the official Kubernetes document [Storage Class](https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner).
    - Recycling policy: When deleting a data volume, keep the data in the data volume or delete the data in it.
    - Snapshot/Expansion: After it is enabled, the data volume/data volume declaration based on the storage pool can support the expansion and snapshot functions, but **the premise is that the underlying storage driver supports the snapshot and expansion functions**.

    **Hwameistor storage system**

    - The storage pool name, driver, and reclamation policy cannot be modified after creation.
    - Storage system: Hwameistor storage system.
    - Storage type: support LVM, raw disk type
      - `LVM type`: Hwameistor recommended usage method, which can use highly available data volumes, and the corresponding CSI storage driver is: `lvm.hwameistor.io`.
      - `Raw disk data volume`: suitable for high availability scenarios, without high availability capability, the corresponding CSI driver is: `hdd.hwameistor.io`
    - High Availability Mode: Before using the high availability capability, please make sure `DRDB component` has been installed. After the high availability mode is turned on, the number of data volume copies can be set to 1 and 2. Convert data volume copy from 1 to 1 if needed
    - Recycling policy: When deleting a data volume, keep the data in the data volume or delete the data in it.
    - Snapshot/Expansion: After it is enabled, the data volume/data volume declaration based on the storage pool can support the expansion and snapshot functions, but **the premise is that the underlying storage driver supports the snapshot and expansion functions**.

    

## Update storage pool (SC)

On the storage pool list page, find the storage pool that needs to be updated, and select Edit under the operation bar on the right to update the storage pool.



!!! info

    Select `View YAML` to view the YAML file of the storage pool, but editing is not supported.

## Delete storage pool (SC)

On the storage pool list page, find the storage pool to be deleted, and select Delete in the operation column on the right.

