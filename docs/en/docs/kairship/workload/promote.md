---
status: new
toc: hide
---

# One-Click Conversion to MultiCloud Workload

With the MultiCloud Orchestration module, you can easily convert a single-cloud workload into a multicloud workload with just one click. This operation greatly improves operational efficiency in multicloud environments.
Refer to [video tutorials](../../videos/use-cases.md)。

Here are the specific steps:

1. Click the name of the multicloud instance, then click __Multicloud Workloads__ on the left side and select __Convert Now__ for the new feature.

    ![Workloads](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/promote01.png)

2. Choose which application you want to convert.

    - You can filter applications by cluster and namespace or search directly by name.
    - When converting, choose whether to convert its associated configmaps and secrets. By default, they will be converted.
    - Only workloads in the clusters that have been added to the current multicloud instance will be displayed here. If there is no your target application, add the cluster where the target is deployed to the current multicloud instance and then try again.
    - Resources that have already been converted to multicloud applications cannot be converted again and will not appear in the list.
    - During the conversion, the system will automatically create corresponding deployment policies and manage the original sub-clusters.

    ![Convert Application](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/promote02.png)

3. Click __OK__ in the lower-right corner of the dialog box to complete the conversion.

    After the application is converted into a multicloud application, it supports editing, updating, and other operations, just like native multicloud workloads.

## FAQs

- Will the workload be restarted after a successful conversion?

    No, there won't be a restart. The conversion is workload-unaware.

- After a successful conversion, if the original cluster is removed from the deployment policy, will the workload replica in that cluster be deleted as well?

    Yes, it will be deleted. Once the conversion is successful, the workload becomes a standard multicloud workload. If the deployment policy changes and the workload is no longer propagated to the original cluster, according to Karmada's design principle, the workload replica in that cluster will also be deleted to maintain consistency.

- Which Kubernetes resources can be converted?

    Currently, only Deployments can be explicitly converted into multicloud resources. If the Deployment is associated with configmaps and secrets, users can choose whether to convert them together. By default, they will be converted. This is to ensure that when the new multicloud workload is distributed to other clusters, its dependent resources are also in place; otherwise, it may cause startup issues for the workload.
