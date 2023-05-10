# cluster status

The container management module supports the management of two types of clusters: access clusters and self-built clusters.
For more information about cluster management types, see [Cluster Role](cluster-role.md).

The status of these two clusters is described below.

## access cluster

| Status | Description |
| ---------------------- | -------------------------- ------------------------------------- |
| Joining | The cluster is joining |
| Removing | The cluster is being removed |
| Running | The cluster is running normally |
| Unknown (Unknown) | The cluster has been disconnected. The data displayed by the system is the cached data before the disconnection, which does not represent real data. At the same time, any operations performed in the disconnected state will not take effect. Please check the cluster network connectivity or host status. |

## Self-built cluster

| Status | Description |
| --------------------------------------------- | ------ -------------------------------------------------- ---- |
| Creating | Cluster is being created |
| Updating | Updating the Kubernetes version of the cluster |
| Deleting | The cluster is being deleted |
| Running | The cluster is running normally |
| Unknown (Unknown) | The cluster has been disconnected. The data displayed by the system is the cached data before the disconnection, which does not represent real data. At the same time, any operations performed in the disconnected state will not take effect. Please check the cluster network connectivity or host status. |
| Creation failed (Failed) | Cluster creation failed, please check the log for detailed failure reasons |