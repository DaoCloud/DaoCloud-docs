# Product Architecture

The management plane of multi-cloud orchestration is mainly responsible for the following functions:

- Lifecycle Management (LCM) for multi-cloud instances (based on Karmada)
- As a unified traffic entry for multi-cloud products (OpenAPI, Kairship UI, internal module GRPC calls)
- Proxy API requests for multi-cloud instances (Karmada native style)
- Aggregation of cluster information (monitoring, management, control), etc. within multi-cloud instances
- Management and monitoring of resources such as multi-cloud workloads
- Subsequent possible permission operations

## Core Components

Multi-cloud orchestration mainly includes two core components:

- kairship apiserver

     Multi-cloud orchestration data flow entrance, all API entrances (protobuf is preferred, all API interfaces are defined through proto, and the corresponding front-end and back-end codes are generated from this, and grpw-gateway is used to support both http restful and grpc).

- kairship controller-manager

     The multi-cloud orchestration controller is mainly responsible for instance state synchronization, resource collection, Karmada instance registration, global resource registration, etc.

!!! note

     Currently, the authentication function of multi-cloud orchestration only verifies the permissions of the Karmada instance. The kairship apiserver verifies whether the interface from Amao has permission to operate or access the Karmada instance.

### Kairship apiserver

The kairship apiserver is mainly responsible for the entrance of multi-cloud orchestration of all traffic (openapi, grpc, etc.). When starting up, it will obtain the identity information of the operator from [Global Management Module](../../ghippo/intro/what.md), It is used for subsequent security verification of AuthZ.

<!--Stateless service, specific interface to be added (currently relatively simple) -->

### kairship controller-manager

!!! note

     Multi-copy deployment, through the election of the leader mechanism, maintains only one working Pod at a time (refer to the controller-manager election mechanism of Kubernetes).

This component is mainly responsible for the processing of a series of control logic for multi-cloud orchestration (each logic is a separate controller), monitors the changes of specific objects through the list-watch mechanism, and then processes the corresponding events. mainly include:

- virtual-cluster-sync-controller

     The CRUD event monitoring of multi-cloud orchestration instance CRD, once the kariship instance is created, the corresponding Kpanda cluster (virtual type, container management interface does not need to be displayed) will be created synchronously.

     The retrieval of all resources of the multi-cloud orchestration instance (multi-cloud workload, pp, op) will be completed through the acceleration mechanism inside the [container management module](../../kpanda/intro/what.md) (with the aid of [Clusterpedia]( ../../community/clusterpedia.md)) to separate reads and writes and improve performance.

     If the instance is deleted, the virtual cluster registered in the container management module will be deleted synchronously.

- resource statistics controller

     It mainly collects the statistical information of all clusters joined in the multi-cloud orchestration instance, and writes it back to the CRD of the multi-cloud orchestration instance (for example, how many CPUs, memory, and number of nodes are included in the clusters managed by the instance).

- status sync controller

     The status synchronization and statistics of the multi-cloud orchestration instance itself.

- instance registry controller

     Multi-cloud orchestration needs to register all `Karmada` instances in the platform to the [global management module](../../ghippo/intro/what.md) through custom resources, so as to complete the role and Karmada instance in the global management binding relationship.
     Finally, these binding relationships will be synchronized to the multi-cloud orchestration module.

-Ghippo webhook controller

     After the [global management module](../../ghippo/intro/what.md) completes the binding relationship between the role and the Karmada instance, notify the multi-cloud orchestration through the sdk, and the multi-cloud orchestration completes the authentication action accordingly.

In the figure above `Kairship management`, there is an instance proxy component (internal component), which is mainly responsible for the communication between the multi-cloud orchestration management plane and each `Karmada` instance.
It can be understood as a collection of Kubernetes clients, get the corresponding client according to the Cluster Name, and then access the real Karmada instance.

## Data Flow Diagram

!!! note

     Multi-cloud instances are not aware of each other and are isolated from each other.

The multi-cloud orchestration management plane needs to operate each multi-cloud orchestration instance, which is mainly divided into the following scenarios:

- Obtain Karmada-related distribution policies and application status information.
- Obtain the statistics and monitoring information of the clusters and nodes in the multi-cloud orchestration instance.
- Edit, update, and delete information related to multi-cloud applications in related Karmada instances (mainly around Karmada workloads and two CRDs of pp and op).

All request traffic is passed directly to the multi-cloud orchestration instance located at [Global Service Cluster](../../kpanda/user-guide/clusters/cluster-role.md). In this way, performance may be affected when large-scale requests are made, as shown in the figure:

<!--screenshot-->

As shown in the figure above, all requests to access the multi-cloud module will be shunted after multi-cloud orchestration, and all read requests such as get/list will access [container management module](../../kpanda/intro/what. md), write requests will access the Karmada instance. This will cause a problem: After creating a multi-cloud application through multi-cloud orchestration, how can the relevant resource information be obtained through the [container management module](../../kpanda/intro/what.md)?

Friends who know Karmada know that the essence of Karmada control-plane is a complete Kubernetes control plane, but there are no nodes that carry workloads.
Therefore, when multi-cloud orchestration creates an instance, it adopts a tricky action, adding the instance itself as a hidden cluster to the [container management module](../../kpanda/intro/what.md) (not in the container management).
In this way, the capabilities of the container management module can be fully utilized (collecting and accelerating the retrieval of resources, CRD, etc. of each Kubernetes cluster), when querying the resources (deployment, pp, op, etc.) of a multi-cloud orchestration instance in the interface, they can be directly managed through the container The module can be retrieved to achieve separation of reading and writing to speed up the response time.

## Multi-cloud orchestration instance LCM

### Deployment topology

<!--screenshot-->

As shown in the figure, the entire multi-cloud orchestration consists of three components, kairship apiserver, kairship controller manager, and karmada operator are all deployed in [Global Service Cluster](../../kpanda/user-guide/clusters/cluster-role.md ).
Among them, the karmada operator fully complies with the deployment architecture of the open source community; the kairship apiserver stateless service supports horizontal expansion; the kairship controller manager has a high-availability architecture, has an internal election mechanism, and can work on a single Pod at the same time.

### Cluster import

<!--screenshot-->

As shown in the figure, all the Kubernetes clusters managed by the Karmada instance come from the `Kpanda` cluster. After the Karmada instance joins a cluster, it will automatically perform CR synchronization (Kpanda Cluster --> Karmada Cluster).
At the same time, the multi-cloud orchestration management plane has a control loop logic that monitors Kpanda Cluster changes in real time, synchronizes to the control plane immediately, and further feeds back to the Karmada Cluster corresponding to the `Karmada` instance. Currently, it mainly monitors changes in Kpanda cluster access credentials.

### Karmada instance CR

The Karmada community is working on the Karmada operator recently. Here we do not make a separate design, just refer to the latest developments in the community.
Therefore, this article does not design the LCM of the `Karmada` example. Assuming that the operator in the community is still not perfect at this stage, we can first connect the CR conversion.