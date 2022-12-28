# Container Management Release Notes

This page lists the Release Notes of container management, so that you can understand the evolution path and feature changes of each version.

## 2022-11-29

### v0.13

#### New features

- **New** Productization of Replicatsets:
    - Support using WEB terminal (CloudTTY) to manage Replicatsets.
    - Support viewing Replicatsets monitoring, logs, Yaml, events, containers.
    - Support viewing Replicatsets details.
    - Linked with **Application Workbench**, the whole lifecycle of Replicatsets is managed by Grayscale Release.
- **New** Pod details page.
- **NEW** Namespace details page.
- **NEW** Use the WEB terminal to upload files to the container and download files from the Pod to the local.
- **New** The workload is elastically scaled based on custom indicators, which is closer to the user's actual business elastic expansion and contraction needs.

#### Optimization

- **Optimized** Deployment cluster support:
    - Deploy the cluster using cilium CNI.
    - Create a cluster with nodes with different usernames, passwords, SSH ports.
- **Optimized** The Pod list supports viewing the total number of container groups and the running number, as well as viewing the container type.
- **Optimized** Added a manual scaling window for workloads, simplifying the manual scaling process for users.
- **Optimized** The container log supports viewing init container and ephemeral container, providing a more friendly operation and maintenance experience.
- **Optimization** node details, the value of annotation vaule is not displayed correctly.
- **Optimization** Operation prompt feedback, giving users correct feedback on operations.

#### Fix

- **FIXED** The problem that creating a namespace fails due to the strong coupling between creating a namespace and binding a workspace.
- **Fix** The problem that updating the routing rules cannot modify the path prefix of the forwarding policy.
- **FIXED** The problem that creating a service while creating a workload interface does not take effect.
- **FIXED** The update service exception error problem.
- **FIXED** Unable to connect to AWS cluster.
- **FIXED** Kpanda user list is out of sync after using WS Admin user to bind resource group.
- **Fixed** the configuration details page, when PageSize=50, the ListClusterConfigMaps interface abnormally reports an error.

## 2022-10-28

### v0.10

#### new function

- **Added** NetworkPolicy policy management functions, including creating, updating, deleting NetworkPolicy policies, and displaying NetworkPolicy policy details to help users configure inbound and outbound traffic policies for Pods
- **NEW** The workload supports multi-NIC configuration and IP Pool display, which meets the user's need to configure multiple NICs separately for workload configuration
- **New** After the cluster creation fails, it supports viewing the operation log of the creation process to help users quickly locate the fault
- **NEW** Stateful workloads support the use of dynamic data volume templates
- **Add** Create cluster, create Secret, create Ingress, edit namespace quota information verification, help guide users to enter the correct configuration parameters, and reduce user experience of failure to create tasks

#### Optimization

- **Optimized** The cluster drop-down list supports displaying cluster status, and optimizes user experience when creating a cluster to select a managed cluster, creating a namespace to select a target cluster, and cluster authorization to select a target cluster
- **Optimization** Install the insight-agent plug-in in the helm application to support automatic acquisition and filling of the Insight-server related address of the global service cluster
- **optimized** default icon for Helm template icon when it is empty
- **Optimization** Select the network mode as None when creating a cluster to allow users to install the network plug-in after the cluster is created
- **Optimized** cluster operation information architecture:
    - Adjust the cluster upgrade operation on the cluster list and cluster overview pages to the cluster operation and maintenance function in the cluster details
    - When a management cluster is removed from the cluster list, the cluster created based on this management cluster will be hidden on the interface. Cluster upgrade, manage node, delete node operations

#### Fix

- **Fix** When switching resources, the selected namespace is automatically converted to all namespaces