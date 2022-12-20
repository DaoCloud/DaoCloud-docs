# basic concept

The basic concepts related to container management are as follows.

#### Cluster Cluster

A cluster refers to the combination of cloud resources required for container operation, and is associated with several cloud server nodes. You can run your application in a cluster. Based on the container management platform, several clusters can be created or connected to several Kubernetes standard clusters.

#### Node Node

Each node corresponds to a virtual machine/physical server, and all container applications run on the nodes of the cluster. The system components on the container platform run on the controller node by default, and are used to manage the container instances running on the node. The number of nodes in the cluster can be expanded and reduced, and the node types are divided into: controller node (Controller) and worker node (Worker).

#### Container Group Pods

A container group is the smallest basic unit for Kubernetes to deploy applications or services. A container group can encapsulate one or more application containers, storage resources, and an independent network IP. These containers are relatively tightly coupled together.

#### Container Container

A container is an instance that is deployed and run through a container image. The container decouples the application from the underlying host facility, so it is easier to deploy the application in different cloud or OS environments.

#### Workload Workload

Workloads are applications running on Kubernetes.

Whether a workload is a single component or composed of multiple components, in Kubernetes it is possible to run these workloads in a set of [Pods](https://kubernetes.io/en/docs/concepts/workloads/pods).

Several built-in workload resources are provided in Kubernetes:

- **Stateless service** (Deployment): The container groups are completely independent, have the same functions, and have features such as elastic scaling and rolling upgrades. It is often used to deploy stateless applications to achieve rapid scaling. Compared with stateful services, the number of instances can be flexibly scaled. For example Nginx, WordPress. Please refer to [Create Stateless Service](../07UserGuide/Workloads/CreateDeploymentByImage.md).

- **Stateful Service** (StatefulSet): Container groups are not completely independent, with stable persistent storage and network marking, and orderly deployment, scaling, and deletion. Because the container can be migrated between different hosts, the data will not be saved on the host. By mounting the storage volume on the container, the data persistence of the stateful set service (such as mysql-HA, etcd) can be realized. Please refer to [Creating a Stateful Service](../07UserGuide/Workloads/CreateStatefulSetByImage.md).

- **Daemon Service** (DaemonSet): The container groups are completely independent, ensuring that background tasks are continuously executed in the assigned nodes without user intervention. The DaemonSet service creates a Pod per node, and you can choose a specific node for deployment. Examples of daemons include log collectors and monitoring services like [Fluentd](https://www.fluentd.org/). Please refer to [Create a daemon service](../07UserGuide/Workloads/CreateDaemonSetByImage.md).

- **Normal task** (Job): A common task is a one-time short task that can be executed after the deployment is completed. The usage scenario is to perform common tasks and upload the image to the mirror warehouse before creating the workload. Please refer to [Create common tasks](../07UserGuide/Workloads/CreateJobByImage.md).

- **CronJob** (CronJob): A cron job is a short task that runs according to a specified time period. The usage scenario is to synchronize time for all running nodes at a fixed point in time. Please refer to [Create CronJobByImage](../07UserGuide/Workloads/CreateCronJobByImage.md).

**Relationship between service and container**

A service consists of one or more container groups (Pods). A container group consists of one or more containers, and each container corresponds to a container image. For stateless workloads, container groups are all identical.

#### Apply Templates

Unified resource management and scheduling of standard templates, and related function extensions. You can manage and deploy community-standard application templates based on application templates, as well as custom business application templates.

#### Mirror Image

A container image is a template in a standard format for container application packaging, used to create containers.
A Docker image is a special file system. In addition to providing the programs, libraries, resources, configuration and other files required for the container to run, it also contains some configuration parameters prepared for the run (such as anonymous volumes, environment variables, users, etc.) .
Images do not contain any dynamic data, and their contents are not changed after they are built.

For example: a mirror can contain a complete Ubuntu operating system environment, which only installs Apache or other applications required by the user.

#### Namespace Namespace

A namespace is an abstract collection of a set of resources and objects. Different namespaces can be created in the same cluster, and the data in different namespaces are isolated from each other. So that they can share the services of the same cluster without interfering with each other. E.g:

- The business of the development environment and the test environment can be placed in different namespaces.

- Common Pods, Services, Replication Controllers, and Deployments all belong to a certain namespace (the default is Default), while Node, PersistentVolume, etc. do not belong to any namespace.

#### Service Service

A Service is an abstraction for exposing an application running on a set of Pods as a network service.

With Kubernetes, you can use unfamiliar service discovery mechanisms without modifying your application. Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load balance among them.

Kubernetes allows specifying a required type of Service, the value and behavior of this type are as follows:

- ClusterIP: Intra-cluster access. The service is exposed through the internal IP of the cluster. If this value is selected, the service can only be accessed within the cluster. This is also the default ServiceType.

- NodePort: Node access. Expose services via IP and static port (NodePort) on each Node. The NodePort service will be routed to the ClusterIP service, which will be created automatically. A NodePort service can be accessed from outside the cluster by requesting `<NodeIP>:<NodePort>`.

- LoadBalancer: load balancing. Using a cloud provider's load balancer, services can be exposed externally. External load balancers can route to NodePort services and ClusterIP services.

#### Layer 7 load balancing Ingress

Ingress is a collection of routing rules for requests entering the cluster. It can provide services with URLs accessed outside the cluster, load balancing, SSL termination, HTTP routing, etc.

#### Network Policy NetworkPolicy

NetworkPolicy provides policy-based network controls for isolating applications and reducing the attack surface. It emulates a traditional segmented network using label selectors and controls the traffic between them and from the outside through policies.

#### Configuration item ConfigMap

ConfigMap is used to save configuration non-confidential data into key-value pairs. When used, the container group can use it as an environment variable, a command-line argument, or a configuration file in a storage volume.

ConfigMap decouples your environment configuration information from container images, making it easy to modify application configurations.

#### Key Secret

Secret is similar to Configmap, but it is used to save configuration information of confidential data (such as passwords, tokens, keys, etc.). Secret decouples sensitive information from container images, and does not need to include confidential data in application code.

#### Label Label

A label is actually a pair of key/value, which is associated with an object, such as a Pod. The use of tags tends to be able to mark the characteristics of the object and is meaningful to the user, but the tag has no direct meaning to the kernel system. Labels can be specified when the object is created, or after the object is created.

#### selector LabelSelector

Label Selector is the core grouping mechanism of Kubernetes, through which clients/users can identify a group of resource objects with common characteristics or attributes.

#### Annotation

Annotation can associate Kubernetes resource objects with arbitrary non-identifying metadata, which can be retrieved through annotations.

Annotation is similar to Label, and is also defined in the form of Key/Value key-value pairs.

#### Storage Volume PersistentVolume

PersistentVolume (PV) and PersistentVolumeClaim (PVC) provide convenient persistent volumes: PV provides network storage resources, while PVC claims storage resources.

#### Storage Claim PersistentVolumeClaim

A PV is a storage resource, and a PersistentVolumeClaim (PVC) is a claim request for a PV. PVCs are similar to Pods: Pods consume Node resources, while PVCs consume PV resources; Pods can request CPU and memory resources, while PVCs request data volumes of a specific size and access mode.

#### Elastic Scaling HPA

Horizontal Pod Autoscaling, or HPA for short, is a function in Kubernetes that realizes horizontal automatic scaling of pods. The Kubernetes cluster can expand or shrink services through the scaling mechanism of the Replication Controller to achieve scalable services.

#### Affinity and anti-affinity

Affinity and anti-affinity expand the types of constraints you can define. Some benefits of using affinity and anti-affinity are:

- The performance of affinity and anti-affinity is stronger. `nodeSelector` can only select nodes that have all the specified labels. Affinity, anti-affinity give you greater control over selection logic.

- You can mark a rule as "soft demand" or "preference", so that the scheduler will still schedule the Pod if no matching node can be found.

- You can use the labels of other Pods running on the node (or in other topological domains) to enforce scheduling constraints, instead of only using the labels of the node itself. This capability allows you to define rules which allow Pods to be placed together.

Before the application was containerized, multiple components would be installed on a virtual machine, and there would be communication between processes. However, when doing container splitting, the container is often split directly by process, such as a container for business processes, monitoring log processing or local data in another container, and has an independent life cycle.
At this time, if they are distributed in two distant nodes in the network, the request will be forwarded many times, and its performance will be poor.

- Affinity: Nearby deployment can be realized, network capabilities can be enhanced to realize nearby routing in communication, and network loss can be reduced. For example, application A and application B frequently interact with each other, so it is necessary to use affinity to make the two applications as close as possible, even on one node, to reduce the performance loss caused by network communication.

- Anti-affinity: Mainly for the sake of high reliability, try to disperse instances as much as possible. When a node fails, the impact on the application is only N/N or only one instance. For example, when an application is deployed with multiple copies, it is necessary to use anti-affinity to distribute each application instance on each node to improve the HA capability.

#### Node affinity NodeAffinity

By selecting labels, you can restrict container groups to be scheduled on specific nodes.

#### Node Anti-Affinity NodeAntiAffinity

By selecting labels, you can restrict container groups from being scheduled on specific nodes.

#### Container Group Load Affinity PodAffinity

Specifies that workloads are deployed on the same node. Users can deploy workloads nearby according to business needs, and the communication between containers can be routed nearby to reduce network consumption.

#### Container Group Anti-Affinity PodAntiAffinity

Specifies that workloads are deployed on different nodes. Anti-affinity deployment of multiple instances of the same workload reduces the impact of downtime; anti-affinity deployment of mutually interfering applications avoids interference.

#### Resource Quota Resource Quota

Resource Quota (Resource Quota) is a mechanism used to limit user resource usage.

#### Resource Limit Limit Range

By default, all containers in Kubernetes do not have any CPU and memory constraints. Limit Rangee is used to add a resource limit to the namespace, including minimum, maximum and default resources. When the container group is created, resource allocation using the limits parameter is enforced.

#### Environment variables

An environment variable refers to a variable set in the container running environment. You can set no more than 30 environment variables when creating a container template. Environment variables can be modified after the workload is deployed, providing great flexibility for the workload.