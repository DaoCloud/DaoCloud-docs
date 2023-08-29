# Backup stateless workloads

This page describes how to back up data for stateless workloads through the `Application Backup` module. The workload used in this tutorial is named `dao-2048`.

## Prerequisites

Before backing up stateless workloads, the following prerequisites must be met:

- In the [Container Management](../../intro/index.md) module [Access Kubernetes Cluster](../clusters/integrate-cluster.md) or [Create Kubernetes Cluster](../clusters/create-cluster.md), and can access the cluster UI interface.

- Create a [namespace](../namespaces/createns.md) and a [user](../../../ghippo/user-guide/access-control/user.md).

- The current operating user should have [`NS Edit`](../permissions/permission-brief.md#ns-edit) or higher permissions, for details, please refer to [Namespace Authorization](../namespaces/createns.md).

- [Install velero components](install-velero.md), and velero components are working fine.

- [Create a stateless workload](../workloads/create-deployment.md) (the workload in this tutorial is named `dao-2048`), and mark the stateless workload with `app: dao-2048` Tag of.

## backup workload

Refer to the following steps to back up the stateless workload `dao-2048`.

1. Enter the container management module, click `Backup and Restore` -> `Application Backup` on the left navigation bar to enter the `Application Backup` list page.

    

2. On the `Application Backup` list page, select the cluster where the velero and `dao-2048` applications have been installed. Click "Backup Plan" in the upper right corner to create a new backup cluster.

    

3. Fill in the backup configuration by referring to the instructions below.

    - Name: Name of the newly created backup plan.
    - Source Cluster: The cluster where the application backup is scheduled to be performed.
    - Object storage location: The access path of the object storage configured when velero was installed on the source cluster.
    - Namespace: The namespace that needs to be backed up supports multiple selections.
    - Advanced configuration: Back up specific resources in the namespace such as an application based on resource tags, or not back up specific resources in the namespace based on resource tags during backup.

        

4. Refer to the instructions below to set the backup execution frequency, and then click `Next`.

    - Backup frequency: Set the time period for task execution based on minutes, hours, days, weeks, and months. Support custom Cron expressions with numbers and `*`, **after inputting the expression, the meaning of the current expression will be prompted**. For detailed expression syntax rules, please refer to [Cron Schedule Syntax](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax).
    - Retention period (days): Set the storage time of backup resources, the default is 30 days, and will be deleted after expiration.
    - Backup data volume (PV): Whether to back up the data in the data volume (PV), support direct copy and use CSI snapshot.
        - Direct copy: directly copy the data in the data volume (PV) for backup;
        - Use CSI snapshots: Use CSI snapshots to back up data volumes (PVs). Requires a CSI snapshot type available for backup in the cluster.

            

5. Click `OK`, the page will automatically return to the application backup plan list, find the newly created `dao-2048` backup plan, and perform the `backup now` operation.

    

6. At this point, the `last execution status` of the cluster will change to `backup`. After the backup is complete, you can click the name of the backup plan to view the details of the backup plan.

    