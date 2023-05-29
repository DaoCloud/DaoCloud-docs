# Features

Multicloud Management module has the following features:

- Unified Management Interface: a unified interface for managing multiple multicloud instances.
- Multiple Instances: create multiple multicloud instances that work in isolation and do not affect each other.
- One-click Import of Clusters: add existing clusters from Container Management module into a multicloud instance, sync the latest cluster information at real time.
- Native APIs: Supports all Kubernetes native APIs.
- Multicloud Application Deployment: flexible deployment policies and override policies for multicloud applications.
- Failover: deploy applications to another healthy cluster when the original cluster is failed.
- Observability: Rich audit rules and metrics to improve observability.
- Practical Permissions: Manage user access based on [workspaces](../../ghippo/user-guide/workspace/workspace.md).

## Multicloud Instances

- Add multicloud instances: you can create an empty multicloud instance, and add clusters later as needed.

- Check the instance list and search by instance name.

    You can view all multicloud instances visible to the current user accnout, including CPU and memory usage, cluster status, versions, creation time, etc.

- One-click import: you can easily add clusters into a multicloud instance by just selecting from a list and clicking "OK".

- Safe Delete: multicloud instances cannot be deleted when there are still some clusters in it. This is to avoid unintentional delete and ensure data security.

## Cluster Management

- Add Cluster

    After a multicloud instance is created, you can dynamically (no need to restart) add clusters into it and manage other resources across these clsuters. Adding a clsuter is quite easy. Just select your expected clusters from the list and then click "OK".

- View Clusters

    You can view all clusters added into a multicloud instance, and further check the details of these clusters, including providers, versions, regions, CPU/Memory usage, service IP range, status, etc.

- Remove Cluster

    You can dynamically remove a cluster from the current multi-cloud instance.

    Removal Verification: to ensure data security, a cluster cannot be removed when there are still resources (deployments, namespaces, secrets, etc.) deploiyed in this cluster under the current multicloud instance.

- kubectl CLI

    You can use kubectl commands in the cloud shell to get the `kubeconfig` information so that users can manage the multi-cloud instance locally.

## Multicloud Workloads

- Create Multicloud Deployment

    Image Creation: Create a deployment through a graphical interface and set deployment or override policies.

    YAML Creation: Create a workload quickly with YAML files.

    YAML Syntax Check: Check the syntax of these YAML files and provides prompts for incorrect syntax.

- Multicloud Workload Details

    You can check the all deployments created, the number of Pods deployed, active cluster information, Pod logs, service monitoring information, etc. 

- Update Multicloud Workload

    Visualized Update: edit the workload through the graphical interface.

    YAML Update: change configuration of the multi-cloud workload by editing its YAML file.

- Delete Multicloud Workload

    Visualized Deletion: delete multicloud workloads as well as resources therein through the graphical interface.

    You can also delete it in cloudshell and terminals.

## Resource Management

- Multicloud Namespaces

    You can create or delete a namespace in multiple clusters, and view the detailed information of these namespaces.

- Multicloud Secrets

    You can create or delete a Secret in multiple clusters, view, and update the detailed information of these Secrets.

- Multicloud ConfigMaps

    You can create or delete a ConfigMap in multiple clusters, view, and update the detailed information of these ConfigMaps.

- Multicloud Services

    You can create or delete a Kubernetes Service in multiple clusters, view, and update the detailed information of these Services.

## Policy Center

- Deployment Policy

    Deployment Policy means how to deploy a multicloud resource across clusters. For example, whether deploy a same number of replicas in each cluster, or deploy more replicas in the clusters with higher weight, or leave it automatically and dynamically scheduled according to available resources in each cluster

    You can create or delete a deployment policy in multiple clusters, view, and update the detailed information of these policies.

- Override Policy

    Override Policy means you can deploy the same deployment with slight differences in each cluster, such as using different image tas, secrets, etc.
    
    You can create or delete a override policy in multiple clusters, view, and update the detailed information of these policies.
