# Assign the cluster to multiple workspaces (tenants)

Cluster resources are usually managed by operation and maintenance personnel. When assigning resource allocations, they need to create namespaces to isolate resources, and set resource quotas.
This method has a disadvantage. If the business volume of the enterprise is large, manual allocation of resources requires a large workload, and it is not a small difficulty to flexibly allocate resource quotas.

DCE introduces the concept of workspace for this purpose. Workspaces can provide higher-dimensional resource quota capabilities through shared resources, enabling workspaces (tenants) to self-create Kubernetes namespaces under resource quotas.

For example, if you want to have several departments share different clusters.

| | Cluster01 (common) | Cluster02 (high availability) |
| ----------------- | ----------------- | ------------- ------ |
| Department (workspace) A | 50 quota | 10 quota |
| Department (workspace) B | 100 quota | 20 quota |

You can share the cluster with multiple departments/workspaces/tenants by following the process:

```mermaid
graph TB

preparews[Prepare workspace] --> preparecs[Prepare cluster]
--> share[Share cluster with workspace]
--> judge([Judge remained quota of workspace])
judge -.More than remained quota.->modifyns[Modify namespace quota]
judge -.Less than remained quota.->createns[Create namespace]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class preparews,preparecs,share, cluster;
class judge plain
class modifyns,createns k8s

click preparews "https://docs.daocloud.io/en/ghippo/04UserGuide/02Workspace/a-cluster-to-multi-ws/#_2"
click preparecs "https://docs.daocloud.io/en/ghippo/04UserGuide/02Workspace/a-cluster-to-multi-ws/#_3"
click share "https://docs.daocloud.io/en/ghippo/04UserGuide/02Workspace/a-cluster-to-multi-ws/#_4"
click createns "https://docs.daocloud.io/en/amamba/03UserGuide/Namespace/namespace/#_3"
click modifyns "https://docs.daocloud.io/en/amamba/03UserGuide/Namespace/namespace/#_4"
```

## Prepare a workspace

In order to meet the multi-tenant usage scenarios, the workspace forms an isolated resource environment based on multiple resources such as clusters, cluster namespaces, meshs, mesh namespaces, multicloud, and multicloud namespaces.
Workspaces can be mapped to various concepts such as projects, tenants, enterprises, and suppliers.

1. Log in to the web console as a user with the admin/folder admin role, and click `Global Management` at the bottom of the left navigation bar.

    ![Global Management](../../images/ws01.png)

1. Click `Workspace and Hierarchy` in the left navigation bar, and click the `Create Workspace` button in the upper right corner.

    ![Create workspace](../../images/ws02.png)

1. After filling in the workspace name, folder and other information, click `OK` to complete the creation of the workspace.

    ![OK](../../images/ws03.png)

## Prepare a cluster

The workspace is to meet the multi-tenant usage scenarios. It forms an isolated resource environment based on multiple resources such as clusters, cluster namespaces, meshs, mesh namespaces, multiclouds, and multicloud namespaces. Workspaces can be mapped to projects and tenants. , business, supplier and many other concepts.

Follow the steps below to prepare a cluster.

1. Click `Container Management` at the bottom of the left navigation bar, and select `Cluster List`.

    ![Container Management](../../images/clusterlist01.png)

1. Click `Create Cluster`[Create a Cluster](../../../kpanda/07UserGuide/Clusters/CreateCluster.md), or click `Join Cluster`[Join a Cluster](../ ../../kpanda/07UserGuide/Clusters/JoinACluster.md).

## Add a cluster to the workspace

Return to `Global Management` to add clusters for the workspace.

1. Click `Global Management` -> `Workspace and Hierarchy` -> `Shared Resources`, click a workspace name, and click the `New Shared Resource` button.

    ![Add resource](../../images/addcluster01.png)

1. Select a cluster, fill in the resource limit, and click `OK`.

    ![Add resource](../../images/addcluster02.png)

Next step: After allocating cluster resources to multiple workspaces, users can go to `Application Workbench` under these workspaces [create namespace and deploy application](../../../amamba/03UserGuide/Namespace /namespace.md).