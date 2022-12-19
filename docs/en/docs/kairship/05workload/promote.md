---
status: new
---

# One-click upgrade for multi-cloud workloads [Beta]

Multi-cloud orchestration supports one-click upgrade of sub-cluster workloads to multi-cloud workloads through simple selection operations.

![image](../images/promote01.jpg)

## Operation Guide

Click the `Try Now` button above to quickly upgrade the application of the sub-cluster to a multi-cloud application; this function is currently in the trial version, if you encounter any problems, you can give feedback in the button below.

![image](../images/promote02.jpg)

- Select the corresponding sub-cluster. Note that only the working cluster that the current workload has been connected to is displayed here. The current workload that is not connected cannot be viewed. The specific access list can be viewed on the working cluster management page
- Select an application, which supports fuzzy retrieval based on the namespace and workload name, helping you quickly locate the application
- Click `Confirm` to complete the multi-cloud workload

![image](../images/promote03.jpg)

After multi-cloudization is completed, actions such as editing and updating can be performed according to normal multi-cloud workloads, which are no different from standard multi-cloud workloads.

!!! note

    - When upgrading, the selectable workload only supports the selection of workloads in sub-clusters; multi-cloud workloads that have already been orchestrated and distributed by multi-cloud cannot be selected again.
    - When multi-cloud, the ConfigMap and Secret associated with the workload will be automatically upgraded to multi-cloud resources.
    - When upgrading multi-cloud, a corresponding deployment strategy will be automatically created to manage atomic clusters.

## common problem

- Will atomic cluster workloads restart after upgrading multi-cloud workloads?

    There will be no restart, and when upgrading multi-cloud workloads, atomic clusters will be managed automatically, while ensuring that atomic cluster workloads can be upgraded without any sense.

- After upgrading a multi-cloud workload, if the atomic cluster is kicked out of the deployment policy, will the sub-cluster workload be deleted?

    Yes, once managed to multi-cloud orchestration, the atomic cluster becomes a standard multi-cloud workload. When the deployment strategy changes and the sub-cluster is no longer propagated, it will be deleted according to Karmada's design principle to ensure consistency.

- What types of Kubernetes resources currently support user upgrades?

    At present, the open operation portal only supports multi-cloud for Deployment;
    However, if the Deployment in the sub-cluster is associated with the corresponding ConfigMap and Secret, then the resource will be multi-cloud automatically;
    The purpose of this is that when the multi-cloud workload is distributed to other clusters, the resources that the workload depends on also exist synchronously, otherwise the workload may start abnormally.