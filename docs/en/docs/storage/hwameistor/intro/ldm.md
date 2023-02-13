# local disk manager

Local Disk Manager (LDM) is an important functional module of HwameiStor system. `LDM` is designed to simplify managing disks on nodes. It abstracts the disk into a resource that can be managed and monitored. It itself is a DaemonSet object, and each node in the cluster will run the service, through which the existing disks are detected and converted into corresponding LocalDisk resources.

![LDM Architecture Diagram](../hwameistor/img/ldm.png)

Currently LDM is still in `alpha` stage.

## Basic concept

**LocalDisk(LD)**: This is the disk resource abstracted by LDM. An `LD` represents a physical disk on the node.

**LocalDiskClaim (LDC)**: This is the way the system uses the disk, by creating an `LDC` object to request a disk from the system. Users can add some description to the disk to select the disk.

> Currently, LDC supports the following description options for disks:
>
> - NodeName
> - Capacity
> - DiskType(e.g. HDD/SSD)

## Usage

If you want to fully deploy HwameiStor, please refer to [Using Helm Chart to install and deploy](../hwameistor/install/deploy.md).

If you only want to deploy LDM separately, you can refer to the following steps to install it.

## Install local disk manager

1. Clone repo to local machine

    ```bash
    git clone https://github.com/hwameistor/local-disk-manager.git
    ```

2. Enter the directory corresponding to repo

    ```bash
    cd deploy
    ```

3. Install CRDs and run LocalDiskManager

    Install the CRD for LocalDisk and LocalDiskClaim

    ```bash
    kubectl apply -f deploy/crds/
    ```

    Install the authorized CR and LDM Operators

    ```bash
    kubectl apply -f deploy/
    ```

4. View LocalDisk information

    ```bash
    $ kubectl get localdisk
    10-6-118-11-sda 10-6-118-11 Unclaimed
    10-6-118-11-sdb 10-6-118-11 Unclaimed
    ```

    This command is used to obtain the disk resource information in the cluster. The obtained information has a total of four columns, and the meanings are as follows:

      - **NAME:** represents the name of the disk in the cluster.
      - **NODEMATCH:** Indicates the node name where the disk resides.
      - **CLAIM:** Indicates which `Claim` this disk is referenced by.
      - **PHASE:** Indicates the current state of the disk.

    View more information about a disk with `kuebctl get localdisk <name> -o yaml`.

5. Apply for an available disk

    **Create LocalDiskClaim**

    ```bash
    kubectl apply -f deploy/samples/hwameistor.io_v1alpha1_localdiskclaim_cr.yaml
    ```

    This command is used to create a disk usage request.
    In this yaml file, you can add a description of the requested disk in the description field, such as disk type, disk capacity, and so on.

    **View LocalDiskClaim information**

    ```bash
    kubectl get localdiskclaim <name>
    ```

    View the Status field information of `Claim`.
    If there is a disk available, you will see a value of `Bound` for this field.