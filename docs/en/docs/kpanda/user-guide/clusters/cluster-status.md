---
MTPE: ModetaNiu
date: 2024-06-06
---

# Cluster Status

DCE 5.0 Container Management module can manage two types of clusters: integrated clusters and created clusters.

- Integrated clusters: clusters created in other platforms and now integrated into DCE 5.0.
- Created clusters: clusters created in DCE 5.0.

For more information about cluster types, see [Cluster Role](cluster-role.md).

We designed several status for these two clusters.

## Integrated Clusters

| Status | Description |
| ---------------------- | -------------------------- ------------------------------------- |
| Integrating | The cluster is being integrated into DCE 5.0. |
| Removing | The cluster is being removed from DCE 5.0. |
| Running | The cluster is running as expected. |
| Unknown | The cluster is lost. Data displayed in the DCE 5.0 UI is the cached data before the disconnection, which does not represent real-time data. Any operation during this status will not take effect. You should check cluster network connectivity or host status. |

## Created Clusters

| Status | Description |
| --------------------------------------------- | ------ -------------------------------------------------- ---- |
| Creating | The cluster is being created. |
| Updating | The Kubernetes version of the cluster is being operating. |
| Deleting | The cluster is being deleted. |
| Running | The cluster is running as expected. |
| Unknown | The cluster is lost. Data displayed in the DCE 5.0 UI is the cached data before the disconnection, which does not represent real-time data. Any operation during this status will not take effect. You should check cluster network connectivity or host status. |
| Failed | The cluster creation is failed. You should check the logs for detailed reasons. |
