# data volume (PV)

A data volume (PersistentVolume, PV) is a piece of storage in the cluster, which can be prepared in advance by the administrator, or dynamically prepared using a storage class (Storage Class). PV is a cluster resource, but it has an independent life cycle and will not be deleted when the Pod process ends. Mounting PVs to workloads can achieve data persistence for workloads. The PV holds the data directory that can be accessed by the containers in the Pod.

## Create data volume

Currently, there are two ways to create data volumes: YAML and form. These two ways have their own advantages and disadvantages, and can meet the needs of different users.

- There are fewer steps and more efficient creation through YAML, but the threshold requirement is high, and you need to be familiar with the YAML file configuration of the data volume.

- It is more intuitive and easier to create through the form, just fill in the corresponding values ​​according to the prompts, but the steps are more cumbersome.

### YAML creation

1. Click the name of the target cluster in the cluster list, and then click __Container Storage__ -> __Data Volume (PV)__ -> __Create with YAML__ in the left navigation bar.

    

2. Enter or paste the prepared YAML file in the pop-up box, and click __OK__ at the bottom of the pop-up box.

    > Supports importing YAML files from local or downloading and saving filled files to local.

    

### Form Creation

1. Click the name of the target cluster in the cluster list, and then click __Container Storage__ -> __Data Volume (PV)__ -> __Create Data Volume (PV)__ in the left navigation bar.

    

2. Fill in the basic information.

    - The data volume name, data volume type, mount path, volume mode, and node affinity cannot be changed after creation.
    - Data volume type: For a detailed introduction to volume types, refer to the official Kubernetes document [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/).

      - Local: The local storage of the Node node is packaged into a PVC interface, and the container directly uses the PVC without paying attention to the underlying storage type. Local volumes do not support dynamic configuration of data volumes, but support configuration of node affinity, which can limit which nodes can access the data volume.
      - HostPath: Use files or directories on the file system of Node nodes as data volumes, and do not support Pod scheduling based on node affinity.

    - Mount path: mount the data volume to a specific directory in the container.
    - access mode:

        - ReadWriteOnce: The data volume can be mounted by a node in read-write mode.
        - ReadWriteMany: The data volume can be mounted by multiple nodes in read-write mode.
        - ReadOnlyMany: The data volume can be mounted read-only by multiple nodes.
        - ReadWriteOncePod: The data volume can be mounted read-write by a single Pod.

    - Recycling strategy:

        - Retain: The PV is not deleted, but its status is only changed to __released__ , which needs to be manually recycled by the user. For how to manually reclaim, refer to [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain).
        - Recycle: keep the PV but empty its data, perform a basic wipe ( __rm -rf /thevolume/*__ ).
        - Delete: When deleting a PV and its data.

    - Volume mode:

        - File system: The data volume will be mounted to a certain directory by the Pod. If the data volume is stored from a device and the device is currently empty, a file system is created on the device before the volume is mounted for the first time.
        - Block: Use the data volume as a raw block device. This type of volume is given to the Pod as a block device without any file system on it, allowing the Pod to access the data volume faster.

    - Node affinity:

        

## View data volume

Click the name of the target cluster in the cluster list, and then click __Container Storage__ -> __Data Volume (PV)__ in the left navigation bar.

- On this page, you can view all data volumes in the current cluster, as well as information such as the status, capacity, and namespace of each data volume.

- Supports sequential or reverse sorting according to the name, status, namespace, and creation time of data volumes.

    

- Click the name of a data volume to view the basic configuration, StorageClass information, labels, comments, etc. of the data volume.

    

## Clone data volume

By cloning a data volume, a new data volume can be recreated based on the configuration of the cloned data volume.

1. Enter the clone page

    - On the data volume list page, find the data volume to be cloned, and select __Clone__ under the operation bar on the right.

        > You can also click the name of the data volume, click the operation button in the upper right corner of the details page and select __Clone__ .

        

2. Use the original configuration directly, or modify it as needed, and click __OK__ at the bottom of the page.

## Update data volume

There are two ways to update data volumes. Support for updating data volumes via forms or YAML files.

!!! note

    Only updating the alias, capacity, access mode, reclamation policy, label, and comment of the data volume is supported.

- On the data volume list page, find the data volume that needs to be updated, select __Update__ under the operation bar on the right to update through the form, select __Edit YAML__ to update through YAML.

    

- Click the name of the data volume to enter the details page of the data volume, select __Update__ in the upper right corner of the page to update through the form, select __Edit YAML__ to update through YAML.

    

## Delete data volume

On the data volume list page, find the data to be deleted, and select Delete in the operation column on the right.

> You can also click the name of the data volume, click the operation button in the upper right corner of the details page and select __Delete__ .

