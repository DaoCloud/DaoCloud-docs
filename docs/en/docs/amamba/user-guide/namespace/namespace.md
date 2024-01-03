# Namespace Management

A namespace is an abstraction used in Kubernetes to isolate resources.

## Prerequisites

- The current workspace already has cluster resources. Refer to [Binding Resources](../../../ghippo/user-guide/workspace/quota.md) for more information.
- The current user is authorized with the __Workspace Admin__ role. Refer to [Workspace Best Practices](../../../ghippo/user-guide/workspace/ws-best-practice.md) for details.

## Create a Namespace

!!! note

    Only __Workspace Admin__ has the privilege to create namespaces and set namespace quotas. Other roles do not support this operation.

1. Click __Namespaces__ in the left navigation pane of your Workbench, then click __Create__ in the upper right corner.

    ![namespace-listpng](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/create00.png)

2. On the __Create Namespace__ page, configure the basic information for the namespace.

    ![namespace-create01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/create01.png)

    - Name: Set the name of the namespace.
    - Cluster: Select a cluster from all the clusters bound under the current workspace.
    - Label: Set labels for the namespace.

3. After configuring the basic information, you also need to set resource quotas for the namespace.

    !!! note

        - If any resource quotas are set for the current cluster in the workspace, you must set these quotas for the namespace when creating it.
        - The resource quotas for the namespace cannot exceed the resource usage limits set for the current cluster in the workspace.
        - Leaving the request or limit fields empty means no quota is set for the current namespace.

    The currently supported resource quotas in the workspace include CPU requests, CPU limits, memory requests, memory limits, total storage requests, and storage volume claims. The limit values for CPU and memory resources must be greater than the request values.

    ![namespace-create02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/create02.png)

4. Click __OK__ to complete the resource creation. A message will appear indicating the successful creation, and you will be returned to the namespace list page.

    ![namespace-list01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/create03.png)

5. Click the __︙__ on the right side of the list to perform operations such as __Resource Quotas__ , __Update Label__ , and __Delete__ from the pop-up menu.

    !!! warning

        Deleting a namespace will delete all the resources under that namespace. Please proceed with caution.

## Namespace Quotas

In addition to CPU requests, CPU limits, memory requests, memory limits, total storage requests, and storage volume claims resource quotas required when creating a namespace, other resource quotas can also be set in the namespace quota management. For example, resources such as container groups, stateless loads, stateful loads, ordinary tasks, and scheduled tasks under the namespace.

1. On the namespace list page, select a namespace and click __Resource Quotas__ .

    ![namespace-quota](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/ns-quota01.png)

2. In the popped-up __Resource Quotas__ dialog box, you can see the current resource quota information for the namespace. Click __Add__ under __Apply Resources__ , select a resource, and set the quota. Refer to [Kubernetes Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) for details.

    ![namespace-quota01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/ns-quota02.png)

3. Click __OK__ to complete the quota settings.
