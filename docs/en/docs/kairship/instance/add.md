---
hide:
  - toc
---

# add instance

DaoCloud provides powerful multi-instance management capabilities of multi-cloud modules based on Karmada, and you only need to follow the steps below to perform simple operations.

When entering multi-cloud orchestration for the first time, you need to `add multi-cloud instance`. The simple operation steps are as follows:

1. In the multi-cloud instance list, click `Add Multi-Cloud Instance` in the upper right corner.

    <!--screenshot-->

2. In the `Add Multi-Cloud Instance` window, you need to fill in the name, alias, pull down to select the management plane cluster, and fill in the label annotation.

    !!! note

        When choosing to install the management plane cluster of a multi-cloud instance, all clusters accessed from the container management platform can be used as the management plane cluster. It is recommended to use a cluster that is running normally and has a storage volume statement (PVC) installed, otherwise there is a risk of installation failure.

    <!--screenshot-->

3. Return to the multi-cloud instance list, and the upper right corner of the screen will prompt that the creation is successful, and the newly created instance will be the first item in the list by default.

!!! note

    The current multi-cloud orchestration product function design, the created multi-cloud instance will be in the `global management cluster` by default, and appear in DCE 5.0 as a virtual cluster, which is transparent to you, so you don’t need to be aware of it; but some precautions require you focus on.

## Instance name prefix

Because multi-cloud instances are in the form of virtual clusters in DCE 5.0, in order to avoid name conflicts with existing clusters, our design requires adding a prefix before the cluster name to solve this problem.

## The operation of instance release

Recently, we have updated the ability to release Karmada instances synchronously when the instance is released; the purpose of this design is to give users greater resources. When the cluster is deleted, whether to synchronize the existing resources synchronously clean up.

By default, synchronous deletion is enabled. If you disable it, we will not recycle the Karmada instance after the cluster is deleted. You can recycle it yourself according to your needs.

> Note: After deleting an instance, it will be removed from the instance list of multi-cloud orchestration