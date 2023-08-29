# Container Concepts

This page lists some basic concepts related to container management.

## Cluster

A cluster is the combination of cloud resources required for container operation, which are associated with several cloud server nodes. You can run your application in a cluster. Based on the container management module, you can create several clusters or access several Kubernetes standard clusters.

## Node

Each node corresponds to a virtual machine/physical server, and all container applications run on the nodes of the cluster. The system components on the container platform run on the controller node by default and are used to manage the container instances running on the node. The number of nodes in the cluster can be scaled. Node types are divided into Controller nodes and Worker nodes.

## Pod

A pod is the smallest and basic unit in which Kubernetes deploys an application or service. A pod can encapsulate one or more application containers, storage resources, and an independent network IP. These containers are relatively tightly coupled together.

## Container

Containers are instances that run through container image deployment. Containers decouple applications from the underlying hosting facility, making it easier to deploy applications in different cloud or OS environments.

## Workload

Workloads refer to applications running on Kubernetes. Whether the workload is a single component or consists of multiple components, it is possible to run these workloads in a group pod in Kubernetes.

There are several workload resources built into Kubernetes:

- **Stateless service** (Deployment): pods are completely independent and have the same features, with features such as flexible expansion and rolling upgrade. It is often used to deploy stateless applications to achieve rapid scaling. Compared with stateful services, the number of instances can be flexibly scaled. For example, Nginx, WordPress. Please refer to [create deployment](../user-guide/workloads/create-deployment.md).

- **Stateful service** (StatefulSet): pods are not completely independent. They have stable persistent storage and network identification, as well as orderly deployment, scaling and deletion. Because the container can be migrated between different hosts, the data is not saved on the host. By mounting the storage volume on the container, the data persistence of stateful set services, such as mysql-HA and etcd, is realized. Please refer to [create statefulset](../user-guide/workloads/create-statefulset.md).

- **Daemon service** (DaemonSet): Complete independence between pods, guaranteeing that background tasks continue to be performed in the assigned nodes without user intervention. The daemon (DaemonSet) service creates a Pod on each node, and you can select a specific node to deploy. Examples of daemons include [Fluentd](https://www.fluentd.org/) log collectors and monitoring services. Please refer to [create daemonset](../user-guide/workloads/create-daemonset.md).

- **Common tasks** (Job): a normal task is a short task that runs once and can be executed after deployment. The usage scenario is to perform a common task to upload the image to the container registry before creating the workload. Please refer to [create job](../user-guide/workloads/create-job.md).

- **Timed task** (CronJob): a timed task is a short task that runs for a specified period of time. The usage scenario is to synchronize the time of all running nodes at a fixed time point. Please refer to [create CronJob](../user-guide/workloads/create-cronjob.md).

A service consists of one or more pods. A pod consists of one or more containers, each corresponding to a container image. For stateless workloads, the pods are all identical.

## Helm charts

Helm charts enable unified resource management and scheduling of standard charts, along with expanding related features. You can manage and deploy community standard application charts based on helm charts, as well as customize business application charts.

## Image

A container image is a standard format template packaged with a container application to create a container. A Docker image is a special file system that contains some configuration parameters (such as anonymous volume, environment variables, user, etc.) prepared for the runtime in addition to providing the programs, libraries, resources, configuration, and other files required by the container runtime. The image does not contain any dynamic data, and its content is not changed after it is built.

For example, an image can contain a complete Ubuntu operating system environment with only Apache or other applications installed that the user needs.

## Namespace

A namespace is an abstract consolidation of a set of resources and objects. Different namespaces can be created within the same cluster, and the data in different namespaces is isolated from each other. This way they can share the services of the same cluster, but also do not interfere with each other.

- The business of the development environment and the test environment can be placed in different namespaces.
- Common items such as Pod, Service, Replication Controller, and Deployment all belong to a namespace (Default), while Node, Persistent Volume, and Persistent Volume Claim are not limited by namespace.

## Service

A service is a logical set of pods that serves as the access point to consume services. Kubernetes provides an abstract layer for service resources, which separates them from specific pod IP addresses and allows for service discovery mechanisms to be used.

Kubernetes has two types of services, cluster-internal services and externally accessible services. Cluster-internal services can only be accessed within the cluster while externally accessible services can be accessed from outside the cluster.

Kubernetes allows you to specify a desired type of Service with specific values and behavior:

- ClusterIP: Intracluster access. It exposes the service through the internal IP of the cluster. This value allows the service to be accessed only within the cluster. This is also the default ServiceType.

- Node Port: Node access. It exposes services through an IP and static port (NodePort) on each Node. The NodePort service routes to the ClusterIP service, which is automatically created. A NodePort service can be accessed from outside the cluster through a request `<NodeIP>:<NodePort>`.

- LoadBalancer: Load balancing. It exposes the service externally using the load balancer of the cloud provider. An external load balancer can route to the NodePort service and the Cluster IP service.

## Seven Layers of Load Balancing Ingress

Ingress is a collection of routing rules for requests entering the cluster, which can provide URLs for the Service, load balancing, SSL termination, and HTTP routing, among others. Ingress is used for external access to the cluster.

## NetworkPolicy

NetworkPolicy provides policy-based network control to isolate applications and reduce the attack surface. It uses tag selectors to simulate a traditional segmented network and controls traffic between them and from the outside through policies.

## ConfigMap

ConfigMap is used to store configuration non-confidential data into key-value pairs. When used, a pod can use it as an environment variable, a command-line argument, or a configuration file on a storage volume.

ConfigMap decouples the environment configuration information from the container image, making it easy to apply configuration changes.

## Secret

Secret is similar to ConfigMap, but it is used to hold configuration information for confidential data such as passwords, tokens, keys, etc. Secret decouples sensitive information from the container image and eliminates the need to include confidential data in the application code.

## Label

A label is a key/value pair that is attached to an object such as a Pod. The use of labels tends to identify the object's characteristics and is meaningful to the user, but labels are not directly meaningful to the kernel system. The label can be specified when creating the object or after creating it.

## LabelSelector

LabelSelector is the grouping mechanism at the core of Kubernetes. Through Label Selector, clients/users can identify a group of resource objects with common characteristics or attributes.

## Annotation

Annotations can associate metadata to non-identifying arbitrary Kubernetes resource objects that can be retrieved through annotations.

Annotations, like Labels, are defined using Key/Value pairs.

## PersistentVolume

PersistentVolume (PV) and Persistent Volume Claim (PVC) provide convenient persistent volumes: PVs provide network storage resources, and PVCs claim storage resources.

## PersistentVolumeClaim

A PV is a storage resource, and a PersistentVolumeClaim (PVC) is a claim request for a PV. PVCs are similar to Pods: Pods consume Node resources, whereas PVCs consume PV resources. Pods can request CPU and memory resources, whereas PVCs request data volumes of a specific size and access pattern.

## HPA

Horizontal Pod Autoscaling (HPA for short) is a feature in Kubernetes that enables automatic horizontal scaling of Pods. The Kubernetes cluster can complete the expansion or contraction of services through the scaling mechanism of Replication Controller to realize scalable services.

## Affinity and anti-affinity

Affinities and anti-affinities extend the types of constraints you can define. Some benefits of using affinity and anti-affinity are:

- The expression ability of affinity and anti-affinity is stronger. Only nodes that have all the specified labels can be `nodeSelector` selected. Affinity and anti-affinity give you more control over the selection logic.

- You can indicate that a rule is a “soft demand” or a “preference” so that the scheduler can still schedule the Pod if it cannot find a matching node.

- Instead of only being able to use the label of the node itself, you can use the labels of other pods running on the node (or in other topology domains) to enforce scheduling constraints. This capability enables you to define rules that allow which pods can be placed together.

  Before containerizing an application, multiple components will be installed on a virtual machine, and there will be communication between processes. However, when doing containerization splitting, containers are often split directly by process, such as a container for business processes, monitoring log processing, or local data in another container, and theyhave an independent lifecycle. At this point, if they are distributed on two distant nodes in the network, the request will be forwarded many times, and its performance will be very poor.

- Affinity: It enables nearby deployment, enhances network capability, realizes nearby routing in communication, and reduces network loss. For example, if application A and application B frequently interact with each other, it is necessary to use affinity to make the two applications as close as possible, even on one node, to reduce the performance loss caused by network communication.

- Anti-affinity: It is mainly for high reliability. The instances are scattered as much as possible so that when a node fails, the impact on the application is only one in N or only one instance. For example, when deploying an application with multiple copies, it is necessary to use anti-affinity to distribute each application instance on each node to improve the HA capability.

## NodeAffinity

By selecting the label, the pod can be restricted to be dispatched to a specific node.

## NodeAntiAffinity

By selecting the label, you can restrict the pod from being scheduled on a specific node.

## PodAffinity

It specifies that the workload is deployed on the same node. Users can deploy workloads nearby according to business needs, and communication between containers can be routed nearby to reduce network consumption.

## PodAntiAffinity

It specifies that the workload is deployed on different nodes. Multiple instances of the same workload are deployed in anti-affinity to reduce the impact of downtime. Applications that interfere with each other are deployed in anti-affinity to avoid interference.

## Resource Quotas

Resource Quota is a mechanism used to limit the amount of resources used by a user.

## Resource Limit Range

By default, all containers in Kubernetes do not have any CPU and memory limitations. Limit Range is used to add a resource limit to the namespace, including minimum, maximum, and default resources. It enforces the allocation of resources using the parameters of limits at the time of pod creation.

## Environment Variables

An environment variable is a variable set in the running environment of a container. You can set up to 30 environment variables when creating a container template. Environment variables can be modified after the workload is deployed, providing flexibility for the workload.
