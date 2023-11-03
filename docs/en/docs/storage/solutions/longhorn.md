# Longhorn Storage Solution

DCE 5.0 supports many third-party storage solutions. We have conducted detailed tests on Longhorn and finally integrated it into the app store as an Addon.
The following is a brief research and evaluation report on Longhorn.

Longhorn is a lightweight cloud native Kubernetes distributed storage platform that can run on any infrastructure.
Longhorn and DCE can be used together to deploy high-availability persistent block storage.

1. Design and Architecture

    - Control plane: Longhorn Manager deployed with DaemonSet
    - Data plane: Longhorn Engine is a storage controller that can have multiple replicas

    

1. Longhorn Storage Volumes

    - Support for Thin provisioning of storage volumes
    - Storage volume maintenance mode is used for snapshot reverting operation
    - Each volume replica contains multiple snapshots.
    - The default number of replicas of the storage volume can be set in settings.
      The number of replicas can be changed through the UI after the storage volume is mounted.
    - Longhorn is a crash-consistent block storage solution that automatically synchronizes
      the sync command before creating a snapshot snapshot

    

1. Data backup and external secondary storage

    - NFS/S3 compatible external secondary storage for backups is independent of the Kubernetes cluster.
      Data remains available even if the Kubernetes cluster is unavailable
    - Longhorn will also synchronize the storage volume to the secondary storage of the
      disaster recovery cluster (DR) for disaster data recovery
    - A backup is a flattened collection of multiple snapshot data.
    - Supports continuous and repeated snapshots and backups.
    - Support Clone of CSI storage volume

    

1. High Availability

    - Support Replica automatic balance setting
    - Support data locality setting: there is at least one replica copy on the node
      running the pod using the storage volume
    - Support for displaying node storage space usage.
    - Support Kubernetes Cluster Autoscaler (Experimental)
    - Supports automatic recovery after storage volumes are accidentally unmounted
    - Supports automatic recovery of storage volumes after cluster node failure

1. Monitoring Monitoring

    - Support Prometheus and Grafana to monitor Longhorn
    - Longhorn metrics can be integrated into DCE monitoring system
    - Support Kubelete Metrics monitoring
    - Support Longhorn alert strategy

1. Advanced features

    - Support Backing Image
    - Support for Orphaned Replica Directories
    - Support DCE cluster recovery: recovery of all storage volumes in the cluster
    - Support multiple write operations ReadWriteMany (RWX) workloads (NFSv4)
    - Support Longhorn Volume as iSCSI Target
