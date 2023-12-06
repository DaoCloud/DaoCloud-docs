# Difference between Resource Groups and Shared Resources

Both resource groups and shared resources support cluster binding, but they have significant differences in usage.

## Differences in Usage Scenarios

- Cluster Binding for Resource Groups: Resource groups are usually used for batch authorization. After binding a resource group to a cluster,
  the workspace administrator will be mapped as a cluster administrator and able to manage and use cluster resources.
- Cluster Binding for Shared Resources: Shared resources are usually used for resource quotas. A typical scenario is that the platform administrator assigns a cluster to a first-level supplier, who then assigns the cluster to a second-level supplier and sets resource quotas for the second-level supplier.

![diff](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/res-gp01.png)

Note: In this scenario, the platform administrator needs to impose resource restrictions on secondary suppliers.
Currently, it is not supported to limit the cluster quota of secondary suppliers by the primary supplier.

## Differences in Cluster Quota Usage

- Cluster Binding for Resource Groups: The workspace administrator is mapped as the administrator of the cluster and is equivalent to being granted the Cluster Admin role in Container Management-Permission Management. They can have unrestricted access to cluster resources, manage important content such as management nodes, and cannot be subject to resource quotas.
- Cluster Binding for Shared Resources: The workspace administrator can only use the quota in the cluster to create namespaces in the Workbench and does not have cluster management permissions. If the workspace is restricted by a quota, the workspace administrator can only create and use namespaces within the quota range.

## Differences in Resource Types

- Resource Groups: Can bind to clusters, cluster-namespaces, multi-clouds, multi-cloud namespaces, grids, and grid-namespaces.
- Shared Resources: Can only bind to clusters.

## Similarities between Resource Groups and Shared Resources

After binding to a cluster, both resource groups and shared resources can go to the Workbench to create namespaces, which will be automatically bound to the workspace.
