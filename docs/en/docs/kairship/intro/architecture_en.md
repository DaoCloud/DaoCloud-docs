# Product Architecture

The management plane of multicloud orchestration is mainly responsible for the following functions:

- Lifecycle Management (LCM) for multicloud instances (based on Karmada)
- As a unified traffic entry for multicloud products (OpenAPI, Kairship UI, internal module GRPC calls)
- Proxy API requests for multicloud instances (Karmada native style)
- Aggregation of cluster information (monitoring, management, control), etc. within multicloud instances
- Management and monitoring of resources such as multicloud workloads
- Subsequent possible permission operations

## Core Components

Multicloud orchestration mainly includes two core components:

- kairship apiserver

     Multicloud orchestration data flow entrance, all API entrances (protobuf is preferred, all API interfaces are defined through proto, and the corresponding front-end and back-end codes are generated from this, and grpw-gateway is used to support both http restful and grpc).

- kairship controller-manager

     The multicloud orchestration controller is mainly responsible for instance state synchronization, resource collection, Karmada instance registration, global resource registration, etc.

!!! note

     Currently, the authentication function of multicloud orchestration only verifies the permissions of the Karmada instance. The kairship apiserver verifies whether the interface from Amao has permission to operate or access the Karmada instance.

### Kairship apiserver

The kairship apiserver is mainly responsible for the entry of all traffic in multicloud orchestration (openapi, grpc, etc.). When starting up, it will obtain the identity information of the operator from [Global Management Module](../../ghippo/intro/what.md), It is used for subsequent security verification of AuthZ.

<!--Stateless service, specific interface to be added (currently relatively simple) -->

### kairship controller-manager

!!! note

     Multi-copy deployment, through the election of the leader mechanism, maintains only one working Pod at a time (refer to the controller-manager election mechanism of Kubernetes).

This component is mainly responsible for the processing of a series of control logic for multicloud orchestration (each logic is a separate controller), monitors the changes of specific objects through the list-watch mechanism, and then processes the corresponding events. mainly include:

- virtual-cluster-sync-controller

     The CRUD event monitoring of multicloud orchestration instance CRD, once the kariship instance is created, the corresponding Kpanda cluster (virtual type, container management interface does not need to be displayed) will be created synchronously.

     The retrieval of all resources of the multicloud orchestration instance (multicloud workload, pp, op) will be completed through the internal acceleration mechanism of the [container management module](../../kpanda/intro/what.md) (with the help of [Clusterpedia](../../community/clusterpedia.md)) to separate reads and writes and improve performance.

     If the instance is deleted, the virtual cluster registered in the container management module will be deleted synchronously.

- resource statistics controller

     It mainly collects the statistical information of all clusters joined in the multicloud orchestration instance, and writes it back to the CRD of the multicloud orchestration instance (for example, how many CPUs, memory, and number of nodes are included in the clusters managed by the instance).

- status sync controller

     The status synchronization and statistics of the multicloud orchestration instance itself.

- instance registry controller

     Multicloud orchestration needs to register all `Karmada` instances in the platform to [Global Management Module](../../ghippo/intro/what.md) through custom resources, so as to complete the role and Karmada instance in the global management binding relationship.
     Finally, these binding relationships will be synchronized to the multicloud orchestration module.

-Ghippo webhook controller

     After the [Global Management Module](../../ghippo/intro/what.md) completes the binding relationship between the role and the Karmada instance, notify the multicloud orchestration through the sdk, and the multicloud orchestration completes the authentication action accordingly.

In the figure above `Kairship management`, there is an instance proxy component (internal component), which is mainly responsible for the communication between the multicloud orchestration management plane and each `Karmada` instance.
It can be understood as a collection of Kubernetes clients, get the corresponding client according to the Cluster Name, and then access the real Karmada instance.

## Data Flow Diagram

!!! note

     Multicloud instances are not aware of each other and are isolated from each other.

The multicloud orchestration management plane needs to operate each multicloud orchestration instance, which is mainly divided into the following scenarios:

- Obtain Karmada-related distribution policies and application status information.
- Obtain the statistics and monitoring information of the clusters and nodes in the multicloud orchestration instance.
- Edit, update, and delete information related to multicloud applications in related Karmada instances (mainly around Karmada workloads and two CRDs of pp and op).

All request data flows directly to the multicloud orchestration instance located at [Global Service Cluster](../../kpanda/07UserGuide/Clusters/ClusterRole.md). In this way, performance may be affected when large-scale requests are made, as shown in the figure:



As shown in the figure above, all requests to access the multicloud module will be shunted after multicloud orchestration, and all read requests such as get/list will access the [container management module](../../kpanda/intro/what. md), write requests will access the Karmada instance. This will cause a problem: After creating a multicloud application through multicloud orchestration, how can the relevant resource information be obtained through the [container management../../kpanda/intro/what.mdKPanda.md)?

Friends who know Karmada know that the essence of Karmada control-plane is a complete Kubernetes control plane, but there are no nodes that carry workloads.
Therefore, when multicloud orchestration creates an instance, it adopts a tricky action, adding the instance itself as a hidden cluster to the [container management module](../../kpanda/intro/what.md) (not in the container management).
In this way, the capabilities of the container management module can be fully utilized (collecting and accelerating the retrieval of resources, CRD, etc. of each Kubernetes cluster), when querying the resources (deployment, pp, op, etc.) of a multicloud orchestration instance in the interface, they can be directly managed through the container The module can be retrieved to achieve separation of reading and writing to speed up the response time.

## Multicloud orchestration instance LCM

### Deployment topology



As shown in the figure, the entire multicloud orchestration consists of three components, kairship apiserver, kairship controller manager, and karmada operator are all deployed in [Global Service Cluster](../../kpanda/07UserGuide/Clusters/ClusterRole.md).
Among them, the karmada operator fully complies with the deployment architecture of the open source community; the kairship apiserver stateless service supports horizontal expansion; the kairship controller manager has a high-availability architecture, has an internal election mechanism, and can work on a single Pod at the same time.

### Cluster import



As shown in the figure, all the Kubernetes clusters managed by the Karmada instance come from the `Kpanda` cluster. After the Karmada instance joins a cluster, it will automatically perform CR synchronization (Kpanda Cluster --> Karmada Cluster).
At the same time, the multicloud orchestration management plane has a control loop logic that monitors Kpanda Cluster changes in real time, synchronizes to the control plane immediately, and further feeds back to the Karmada Cluster corresponding to the `Karmada` instance. Currently, it mainly monitors changes in Kpanda cluster access credentials.

### Karmada instance CR

The Karmada community is working on the Karmada operator recently. Here we do not make a separate design, just refer to the latest developments in the community.
Therefore, This page does not design the LCM of the `Karmada` example. Assuming that the operator in the community is still not perfect at this stage, we can first connect the CR conversion.