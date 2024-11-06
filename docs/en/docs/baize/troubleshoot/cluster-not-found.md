---
MTPE: windsonsea
Date: 2024-07-29
---

# Cluster Not Found in Drop-Down List

## Symptom

In the AI Lab Developer and Operator UI, the desired cluster cannot
be found in the drop-down list while you search for a cluster.

## Analysis

If the desired cluster is missing from the cluster drop-down list in AI Lab,
it could be due to the following reasons:

- The `baize-agent` is not installed or failed to install, causing AI Lab
  to be unable to retrieve cluster information.
- The cluster name was not configured when installing `baize-agent`, causing
  AI Lab to be unable to retrieve cluster information.
- Observable components within the worker cluster are abnormal,
  leading to the inability to collect metrics information from the cluster.

## Solution

### `baize-agent` not installed or failed to install

AI Lab requires some basic components to be installed in each worker cluster.
If the `baize-agent` is not installed in the worker cluster, you can choose to install
it via UI, which might lead to some unexpected errors.

Therefore, to ensure a good user experience, the selectable cluster range only includes
clusters where the `baize-agent` has been successfully installed.

If the issue is due to the `baize-agent` not being installed or installation failure,
use the following steps:

**Container Management** -> **Clusters** -> **Helm Apps** -> **Helm Charts** ,
find `baize-agent` and install it.

!!! note

    Quickly jump to this address: `https://<dce_host>/kpanda/clusters/<cluster_name>/helm/charts/addon/baize-agent`.
    Note to replace `<dce_host>` with the actual DCE console address, and `<cluster_name>` with the actual cluster name.

### Cluster name not configured in the process of installing `baize-agent`

When installing `baize-agent`, ensure to configure the cluster name. This name will be used
for Insight metrics collection and **is empty by default, requiring manual configuration** .

<!-- add screenshot later -->

### Insight components in the worker cluster are abnormal

If the Insight components in the cluster are abnormal, it might cause AI Lab
to be unable to retrieve cluster information. Check if the platform's Insight services
are running and configured correctly.

- Check if the insight-server component is running properly in the
  [Global Service Cluster](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster).
- Check if the insight-agent component is running properly in the
  [worker cluster](../../kpanda/user-guide/clusters/cluster-role.md#worker-cluster).
