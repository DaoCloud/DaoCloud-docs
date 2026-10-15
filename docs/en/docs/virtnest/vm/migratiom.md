# Cold Migration within a Cluster

This article explains how to move a virtual machine from one node to another node within the same cluster while it is powered off.

The main characteristic of cold migration is that the virtual machine remains offline during the migration, which may affect business continuity. Therefore, when performing a cold migration, you need to carefully plan the migration time window and consider business requirements and system availability. Generally, cold migration is suitable for scenarios where the downtime requirement is not very strict.

## Prerequisites

The following prerequisites must be met before using cold migration:

- The virtual machine must be powered off before cold migration can be performed.

## Cold Migration

1. From the left navigation bar, click __Virtual Machines__ -> __Virtual Machines__ in turn to enter the list page, and click __┇__ on the right side of the list to migrate a powered-off virtual machine. When a virtual machine is powered off, you cannot view the node it resides on, so you need to plan in advance or power it on to query.

    ![Before migration](../images/cold01.png)

    ![Migration after power-off](../images/cold02.png)

    !!! note

        If you use local-path in the storage pool of the original node, cross-node migration may fail. Select with caution.

2. After you click Migrate, a message indicates that during the migration you can choose to migrate to a specified node or migrate randomly. If you need to modify the storage pool, make sure that an available storage pool exists in the target node. Also make sure that the target node has sufficient resources. The migration takes a long time, so please wait patiently.

    ![Migration prompt](../images/cold03.png)

3. The migration takes some time. Please wait patiently. After it succeeds, you need to power on the virtual machine to check whether the migration succeeded. This example has already powered on the virtual machine to show the migration result.

    ![Migration result](../images/cold04.png)
