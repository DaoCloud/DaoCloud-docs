# Data volume declaration (PVC)

A persistent volume claim (PersistentVolumeClaim, PVC) expresses a user's request for storage. PVC consumes PV resources and claims a data volume with a specific size and specific access mode. For example, the PV volume is required to be mounted in ReadWriteOnce, ReadOnlyMany or ReadWriteMany modes.

## Create data volume statement

Currently, there are two ways to create data volume declarations: YAML and form. These two ways have their own advantages and disadvantages, and can meet the needs of different users.

- There are fewer steps and more efficient creation through YAML, but the threshold requirement is high, and you need to be familiar with the YAML file configuration of the data volume declaration.

- It is more intuitive and easier to create through the form, just fill in the corresponding values ​​according to the prompts, but the steps are more cumbersome.

### YAML creation

1. Click the name of the target cluster in the cluster list, and then click __Container Storage__ -> __Data Volume Declaration (PVC)__ -> __Create with YAML__ in the left navigation bar.

    

2. Enter or paste the prepared YAML file in the pop-up box, and click __OK__ at the bottom of the pop-up box.

    > Supports importing YAML files from local or downloading and saving filled files to local.

    

### Form Creation

1. Click the name of the target cluster in the cluster list, and then click __Container Storage__ -> __Data Volume Declaration (PVC)__ -> __Create Data Volume Declaration (PVC)__ in the left navigation bar.

    

2. Fill in the basic information.

    - The name, namespace, creation method, data volume, capacity, and access mode of the data volume declaration cannot be changed after creation.
    - Creation method: dynamically create a new data volume claim in an existing StorageClass or data volume, or create a new data volume claim based on a snapshot of a data volume claim.

        > The declared capacity of the data volume cannot be modified when the snapshot is created, and can be modified after the creation is complete.

    - After selecting the creation method, select the desired StorageClass/data volume/snapshot from the drop-down list.
    - access mode:

      - ReadWriteOnce, the data volume declaration can be mounted by a node in read-write mode.
      - ReadWriteMany, the data volume declaration can be mounted by multiple nodes in read-write mode.
      - ReadOnlyMany, the data volume declaration can be mounted read-only by multiple nodes.
      - ReadWriteOncePod, the data volume declaration can be mounted by a single Pod in read-write mode.

        

## View data volume statement

Click the name of the target cluster in the cluster list, and then click __Container Storage__ -> __Data Volume Declaration (PVC)__ in the left navigation bar.

- On this page, you can view all data volume declarations in the current cluster, as well as information such as the status, capacity, and namespace of each data volume declaration.

- Supports sorting in sequential or reverse order according to the declared name, status, namespace, and creation time of the data volume.

    

- Click the name of the data volume declaration to view the basic configuration, StorageClass information, labels, comments and other information of the data volume declaration.

    

## Expansion data volume statement

1. In the left navigation bar, click __Container Storage__ -> __Data Volume Declaration (PVC)__ , and find the data volume declaration whose capacity you want to adjust.

    

2. Click the name of the data volume declaration, and then click the operation button in the upper right corner of the page and select __Expansion__ .

    

3. Enter the target capacity and click __OK__ .

    

## Clone data volume statement

By cloning a data volume claim, a new data volume claim can be recreated based on the configuration of the cloned data volume claim.

1. Enter the clone page

    - On the data volume declaration list page, find the data volume declaration that needs to be cloned, and select __Clone__ under the operation bar on the right.

        > You can also click the name of the data volume declaration, click the operation button in the upper right corner of the details page and select __Clone__ .

        

2. Use the original configuration directly, or modify it as needed, and click __OK__ at the bottom of the page.

    

## Update data volume statement

There are two ways to update data volume claims. Support for updating data volume claims via form or YAML file.

!!! note

    Only aliases, labels, and annotations for data volume claims are updated.

- On the data volume list page, find the data volume declaration that needs to be updated, select __Update__ in the operation bar on the right to update it through the form, and select __Edit YAML__ to update it through YAML.

    

- Click the name of the data volume declaration, enter the details page of the data volume declaration, select __Update__ in the upper right corner of the page to update through the form, select __Edit YAML__ to update through YAML.

    

## Delete data volume statement

On the data volume declaration list page, find the data to be deleted, and select Delete in the operation column on the right.

> You can also click the name of the data volume statement, click the operation button in the upper right corner of the details page and select __Delete__ .



## common problem

1. If there is no optional StorageClass or data volume in the list, you can [Create a StorageClass](sc.md) or [Create a data volume](pv.md).

2. If there is no optional snapshot in the list, you can enter the details page of the data volume declaration and create a snapshot in the upper right corner.

    

3. If the StorageClass (SC) used by the data volume declaration is not enabled for snapshots, snapshots cannot be made, and the page will not display the "Make Snapshot" option.
4. If the StorageClass (SC) used by the data volume declaration does not have the capacity expansion feature enabled, the data volume does not support capacity expansion, and the page will not display the capacity expansion option.

    