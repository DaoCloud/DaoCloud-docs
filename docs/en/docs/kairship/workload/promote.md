---
status: new
---

# One-click conversion to multi-cloud workloads [Beta]

Multi-cloud orchestration supports one-click conversion of sub-cluster workloads to multi-cloud workloads through simple selection operations.

<!--screenshot-->

## Operation Guide

Click the `Try Now` button above to quickly convert the sub-cluster application to a multi-cloud application; this function is currently in the trial version, if you encounter any problems, you can give feedback in the button below. When a subcluster is converted, you can choose whether to convert its services synchronously. By default, it will be converted synchronously.

<!--screenshot-->

- Select the corresponding sub-cluster. Note that only the working cluster that the current workload has been connected to is displayed here. The current workload that is not connected cannot be viewed. The specific access list can be viewed on the working cluster management page
- Select an application, which supports fuzzy retrieval based on the namespace and workload name, helping you quickly locate the application
- Click `Confirm` to complete the multi-cloud workload

After multi-cloudization is completed, actions such as editing and updating can be performed according to normal multi-cloud workloads, which are no different from standard multi-cloud workloads.

!!! note

    - During conversion, the selectable workload only supports the selection of workloads in sub-clusters; multi-cloud workloads that have already been orchestrated and distributed by multi-cloud do not support re-selection.
    - When multi-cloud, the ConfigMap and Secret associated with the workload will be automatically converted into multi-cloud resources.
    - When converting to multi-cloud, a corresponding deployment strategy will be automatically created to manage atomic clusters.

## common problem

- Will atomic cluster workloads restart after converting multi-cloud workloads?

    There will be no restart, and when the multi-cloud workload is converted, the atomic cluster is automatically managed, and the atomic cluster workload is guaranteed to be switched without any sense.

- After converting a multi-cloud workload, after the atomic cluster is kicked out of the deployment policy, will the sub-cluster workload be deleted?

    Yes, once managed to multi-cloud orchestration, the atomic cluster becomes a standard multi-cloud workload. When the deployment strategy changes and the sub-cluster is no longer propagated, it will be deleted according to Karmada's design principle to ensure consistency.

- What Kubernetes Resource types currently support user transitions?

    At present, the open operation portal only supports multi-cloud for Deployment;
    However, if the Deployment in the sub-cluster is associated with the corresponding ConfigMap and Secret, then the resource will be multi-cloud automatically;
    The purpose of this is that when the multi-cloud workload is distributed to other clusters, the resources that the workload depends on also exist synchronously, otherwise the workload may start abnormally.