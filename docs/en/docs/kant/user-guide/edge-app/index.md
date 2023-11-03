# Overview of Edge Applications

The platform supports deploying container applications to edge nodes. Container applications can
directly pull images from the image repository.

The architecture of the container image must be consistent with the architecture of the edge node.

## Workloads

A workload (Deployment) is an API object that manages replicas of an application. It represents
pods without local state, where the pods are independent, functionally identical, and can be scaled up or down flexibly.

## Batch Deployments

Deploying workloads with similar configurations or minor differences to a node group is a task or batch deployment action.

- By using labels, resources of the same type can be filtered, enabling batch deployment of container applications
  for a specific category or region.
- Each node group corresponds to a batch deployment task, and a workload definition can be deployed to multiple node groups.
- To avoid task failures caused by network jitter or high-concurrency traffic control, the platform provides
  a visual deployment view that timely synchronizes the status and results of batch deployments.

## Application Fault Migration

- When an application instance in a node group experiences an exception or when a node fails, the platform's
  offline self-healing feature can quickly schedule the application instance to run on other available nodes
  in the node group, ensuring autonomous operation of the application and business continuity.
- Even when the node is offline (disconnected from the cloud), automatic scheduling can still take place.

## Configuration Items and Secrets

Configuration items and secrets are resource types used to store and manage authentication information,
certificates, keys, and other important and sensitive information required by workloads. The content is
determined by the user. After the resource is created, it can be loaded and used in the container application.

The process of creating and using configuration items and secrets in the Cloud Edge Collaboration module
is consistent with the process in the Container Management module. In the details page of the edge unit,
go to the `Configuration Items and Secrets` menu. Refer to
[Creating Configuration Items](../../../kpanda/user-guide/configmaps-secrets/create-configmap.md)
for the creation and usage process.
