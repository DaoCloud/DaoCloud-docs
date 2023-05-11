# Insight-agent component status description

Observability Insight is a multi-cluster observation product in DCE 5.0. In order to realize the unified collection of multi-cluster observation data, users need to install the Helm application `insight-agent`
(Installed in insight-system namespace by default). See [How to install `insight-agent`](./install-agent.md).

## Status description

In `Observability` -> `Acquisition Management` section, you can view the status of `insight-agent` installed in each cluster.

- `not installed`: `insight-agent` is not installed under the insight-system namespace in this cluster
- `Running`: `insight-agent` is successfully installed in the cluster, and all deployed components are running
- `Exception`: If insight-agent is in this state, it means that the helm deployment failed or the deployed components are not running

Can be checked by:

1. Execute the following command, if the status is `deployed`, go to the next step. If it is `failed`, since it will affect the upgrade of the application, it is recommended to reinstall after uninstalling `Container Management -> Helm Application`:

     ```bash
     helm list -n insight-system
     ```

2. Execute the following command or check the status of the components deployed in the cluster in `Observability -> Collection Management`. If there is a container group that is not in the `Running` state, please restart the abnormal container group.

     ```bash
     kubectl get pods -n insight-system
     ```

## Supplementary instructions

1. The resource consumption of the indicator collection component Prometheus in `insight-agent` is directly proportional to the number of container groups running in the cluster.
    Please adjust Prometheus resources according to the cluster size, please refer to: [Prometheus Resource Planning](../../best-practice/prometheus-res.md)

2. Since the storage capacity of the indicator storage component vmstorage in the global service cluster is directly proportional to the sum of the number of container groups in each cluster.

     - Please contact the platform administrator to adjust the disk capacity of vmstorage according to the cluster size, see [vmstorage disk capacity planning](../../best-practice/vms-res-plan.md)
     - Adjust vmstorage disk according to multi-cluster size, see [vmstorge disk expansion](../../best-practice/modify-vms-disk.md)