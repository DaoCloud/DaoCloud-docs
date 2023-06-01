---
status: new
---

# One-click conversion to multicloud workloads [Beta]

Multicloud Management supports one-click conversion of sub-cluster workloads to multicloud workloads through simple selection operations.

<!--screenshot-->

## Operation Guide

Click the `Try Now` button above to quickly convert the sub-cluster application to a multicloud application; this function is currently in the trial version, if you encounter any problems, you can give feedback in the button below. When a subcluster is converted, you can choose whether to convert its services synchronously. By default, it will be converted synchronously.

<!--screenshot-->

- Select the corresponding sub-cluster. Note that only the working cluster that the current workload has been connected to is displayed here. The current workload that is not connected cannot be viewed. The specific access list can be viewed on the working cluster management page
- Select an application, which supports fuzzy retrieval based on the namespace and workload name, helping you quickly locate the application
- Click `Confirm` to complete the multicloud workload

After multicloudization is completed, actions such as editing and updating can be performed according to normal multicloud workloads, which are no different from standard multicloud workloads.

!!! note

    - During conversion, the selectable workload only supports the selection of workloads in sub-clusters; multicloud workloads that have already been orchestrated and distributed by multicloud do not support re-selection.
    - When multicloud, the ConfigMap and Secret associated with the workload will be automatically converted into multicloud resources.
    - When converting to multicloud, a corresponding deployment strategy will be automatically created to manage atomic clusters.

## common problem

- Will atomic cluster workloads restart after converting multicloud workloads?

    There will be no restart, and when the multicloud workload is converted, the atomic cluster is automatically managed, and the atomic cluster workload is guaranteed to be switched without any sense.

- After converting a multicloud workload, after the atomic cluster is kicked out of the deployment policy, will the sub-cluster workload be deleted?

    Yes, once managed to Multicloud Management, the atomic cluster becomes a standard multicloud workload. When the deployment strategy changes and the sub-cluster is no longer propagated, it will be deleted according to Karmada's design principle to ensure consistency.

- What Kubernetes Resource types currently support user transitions?

    At present, the open operation portal only supports multicloud for Deployment;
    However, if the Deployment in the sub-cluster is associated with the corresponding ConfigMap and Secret, then the resource will be multicloud automatically;
    The purpose of this is that when the multicloud workload is distributed to other clusters, the resources that the workload depends on also exist synchronously, otherwise the workload may start abnormally.