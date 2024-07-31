# Longhorn Storage Solution

DCE 5.0 supports many third-party storage solutions. We have conducted detailed tests on Longhorn and finally integrated it into the app store as an Addon.
The following is a brief research and evaluation report on Longhorn.

Longhorn is a lightweight cloud native Kubernetes distributed storage platform that can run on any infrastructure.
Longhorn and DCE can be used together to deploy high-availability persistent block storage.

1. Design and Architecture

    - Control Plane: Longhorn Manager deployed with DaemonSet.
    - Data Plane: Longhorn Engine is a storage controller that can have multiple replicas.

2. Longhorn Storage Volumes

    - Supports thin provisioning of storage volumes.
    - Storage volume maintenance mode is used for snapshot reverting operations.
    - Each volume replica contains multiple snapshots.
    - The default number of replicas for a storage volume can be set in the settings. The number of replicas can be changed through the UI after the storage volume is mounted.
    - Longhorn is a crash-consistent block storage solution that automatically synchronizes the sync command before creating a snapshot.

3. Data Backup and External Secondary Storage

    - NFS/S3-compatible external secondary storage for backups is independent of the Kubernetes cluster. Data remains available even if the Kubernetes cluster is unavailable.
    - Longhorn will also synchronize the storage volume to the secondary storage of the disaster recovery (DR) cluster for disaster data recovery.
    - A backup is a flattened collection of multiple snapshot data.
    - Supports continuous and repeated snapshots and backups.
    - Supports cloning of CSI storage volumes.

4. High Availability

    - Supports replica automatic balance setting.
    - Supports data locality setting: there is at least one replica copy on the node running the pod using the storage volume.
    - Supports displaying node storage space usage.
    - Supports Kubernetes Cluster Autoscaler (Experimental).
    - Supports automatic recovery after storage volumes are accidentally unmounted.
    - Supports automatic recovery of storage volumes after cluster node failure.

5. Monitoring

    - Supports Prometheus and Grafana to monitor Longhorn.
    - Longhorn metrics can be integrated into the DCE monitoring system.
    - Supports kubelet metrics monitoring.
    - Supports Longhorn alert strategy.

6. Advanced Features

    - Supports backing images.
    - Supports orphaned replica directories.
    - Supports DCE cluster recovery: recovery of all storage volumes in the cluster.
    - Supports multiple write operations for ReadWriteMany (RWX) workloads (NFSv4).
    - Supports using Longhorn Volume as an iSCSI target.
