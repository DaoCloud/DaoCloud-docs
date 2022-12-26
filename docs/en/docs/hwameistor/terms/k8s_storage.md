# Kubernetes storage

Kubernetes provides several enhancements for container platforms (or cluster administrators) and application developers to support running stateful workloads. These features ensure that whenever scheduling containers (including volume provisioning/creation, attaching, mounting, unmounting, splitting, and deleting), storage capacity management (container ephemeral storage usage, volume scaling, etc.), can be used Different types of file and block storage (ephemeral or persistent, local or remote), which affect storage-based container scheduling (data gravity, availability, etc.) and general storage operations like snapshots.

When using HwameiStor to run stateful workloads, you need to understand several abstract concepts of Kubernetes storage:

- [Kubernetes-storage](#kubernetes-storage)
  - [Container Storage Interface](#Container Storage Interface)
  - [Storage classes and dynamic provisioning](#Storage classes and dynamic provisioning)
  - [PersistentVolume Claim](#PersistentVolumeStatement)
  - [PersistentVolume](#PersistentVolume)
  - [stateful and stateless](#stateful and stateless)

## Container storage interface

The Container Storage Interface (CSI) is a standard for exposing arbitrary file storage and block storage systems to containerized workloads on a container orchestration architecture such as Kubernetes. With CSI, third-party storage providers like HwameiStor can write and deploy new storage volume plugins, such as HwameiStor LocalDisk and LocalVolumeReplica, without modifying the Kubernetes core code.

When the cluster administrator installs HwameiStor, the required HwameiStor CSI driver components are also installed into the Kubernetes cluster.

```csharp
// Before CSI, Kubernetes supported adding new storage providers using out-of-tree resource provisioners (also known as external resource provisioners). Kubernetes in-tree volumes predate external resource provisioners. And the Kubernetes community is also working on using CSI-based volumes as an alternative to tree volumes. )
```

## Storage classes and dynamic resource provisioning

StorageClass provides a way for administrators to describe "classes" of storage. Different categories may map to quality of service levels, backup policies, or arbitrary policies determined by the cluster administrator. In some storage systems, the concept of a StorageClass is called a "profile".

With the dynamic resource allocation function, the cluster administrator does not need to allocate storage resources in advance. It automatically provisions storage resources when requested by users. The implementation of dynamic volume resource allocation is based on the abstract concept of StorageClass. The cluster administrator can define as many StorageClass objects as needed, and each object will specify a plug-in (also known as an adjuster) for provisioning volumes, and configure a set of parameters passed to the adjuster during resource provisioning.

Cluster administrators can define and expose multiple storage types (from the same or different storage systems) within the cluster, each with customizable parameters. This design also ensures that end users don't have to worry about the complexities and nuances of storage configuration, but are still able to choose from multiple storage options.

After installing HwameiStor comes with two default storage classes that allow users to create local volumes (HwameiStor LocalVolume) or replicas (HwameiStor LocalVolumeReplica). Cluster administrators can enable the required storage engines and then create storage classes for data engines.

## Persistent volume declaration

A PersistentVolumeClaim (PVC) is a user storage request for the StorageClass service provided by the cluster administrator. Applications running on containers can request some type of storage. For example, a container can specify the required storage size or the method of accessing data (read-only, single read/write, multiple read-write, etc.).

In addition to storage size and access mode, administrators can create storage classes that provide PVs with custom attributes such as disk type (HDD and SSD), performance level, or storage tier (regular or cold).

## Persistent Volume

PersistentVolumes (PVs) are provisioned dynamically by storage providers when a user requests a PVC. A PV contains details of how a container consumes storage. Kubernetes and volume drivers use the details in the PV to attach/detach storage to the node the container is running on, and to mount/unmount storage to the container.

The HwameiStor control plane dynamically sets up HwameiStor local volumes and replicas, and helps create PV objects in the cluster.

## Stateful and stateless

Kubernetes provides several built-in stateful and stateless workload resources to let application developers define workloads to run on Kubernetes. It is possible to run stateful workloads by creating a Kubernetes stateless/stateful workload and connecting it to a PV using a PVC.

For example, a MySQL stateless workload that references a PVC can be created in YAML. MySQL PVCs referenced by stateless loads should be created with the requested size and StorageClass. Once the HwameiStor control plane provides the PV for the required StorageClass and capacity, the claim is set as satisfied. Kubernetes will then mount the PV and start the MySQL stateless load.