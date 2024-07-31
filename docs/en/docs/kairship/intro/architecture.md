---
MTPE: ModetaNiu
DATE: 2024-07-18
---

# Product Architecture

The management interface of MultiCloud Management is primarily responsible for the following functionalities:

- Lifecycle management (LCM) of multicloud instances (based on Karmada)
- Serving as a unified entry point for multicloud products (OpenAPI, Kairship UI, internal module GRPC calls)
- Proxying API requests for multicloud instances (in the native Karmada style)
- Aggregating cluster information (monitoring, management, control) within multicloud instances
- Management and monitoring of multicloud workloads and other resources
- Potential future permission operations

## Core Components

MultiCloud Management mainly consists of two core components: __kairship-apiserver__ and __kairship controller-manager__ .

## Kairship-apiserver

The __kairship-apiserver__ primarily serves as the entry point for all traffic in MultiCloud Management,
including OpenAPI and GRPC. It acts as a unified entry point for all APIs. The APIs are defined using
 __protobuf__ , which generates corresponding frontend and backend code. It supports both HTTP Restful
and GRPC through __grpc-gateway__ .

During startup, it retrieves identity information of the operator from the [Global Management Module](../../ghippo/intro/index.md) for subsequent security verification during AuthZ.

<!-- Stateless service, specific interfaces to be supplemented (currently simple) -->

### Kairship-controller-manager

This is the controller for MultiCloud Management, responsible for instance status synchronization,
resource collection, Karmada instance registration, and global resource registration.

In a multi-replica propagation, it utilizes the leader mechanism to maintain a single working pod
at any given time (similar to Kubernetes' controller-manager election mechanism).

This component handles a series of control logic for MultiCloud Management, with each logic
represented as a separate controller. It listens for changes in specific objects through the
list-watch mechanism and processes corresponding events. The main controllers include:

- Virtual Cluster Sync Controller:
    - Listens for CRUD events of MultiCloud Management instance CRDs. When a MultiCloud Management
      instance is created, it synchronizes the creation of corresponding virtual cluster management resources.
    - Retrieval of all resources for the MultiCloud Management instance (Multicloud Workloads, PP, OP)
      is accomplished through the acceleration mechanism within the Container Management Module
      (leveraging Clusterpedia), enabling read-write separation and improved performance.
    - When an instance is deleted, the virtual cluster registered in the Container Management Module is synchronously deleted.

- Resource Statistics Controller:
    - Collects statistical information for all clusters joined by MultiCloud Management instances
      and writes it back to the MultiCloud Management instance CRD (e.g., total CPU, memory,
      and node count in the clusters managed by the instance).

- Status Sync Controller:
    - Handles status synchronization and statistics for MultiCloud Management instances.

- Instance Registry Controller:
    - MultiCloud Management registers all __Karmada__ instances in the platform to the
      Global Management Module using custom resources. This allows for the binding of roles and
      Karmada instances in global management. Ultimately, these bindings are synchronized to
      the MultiCloud Management module.

- Ghippo Webhook Controller:
    - After the binding of roles and Karmada instances is completed in the Global Management Module,
      the MultiCloud Management module is informed via SDK to perform authorization actions.

## Data Flow Diagram

![Data Flow Diagram](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/arch_kairship_instance.jpg)

It is important to note that multicloud instances are not aware of each other and are isolated from one another.

MultiCloud Management:

- Retrieves distribution policies and application status information related to Karmada.
- Retrieves cluster and node statistics, monitoring information, and management and
  control information for multicloud instances.
- Edits, updates, and deletes information related to multicloud applications in Karmada instances
  (mainly focused on Karmada workloads and PP, OP).

All request data flows directly to the multicloud instances located in the Global Services Cluster.

Next, all access requests are routed to the corresponding instances after passing through the
MultiCloud Management. All read requests such as get/list access the Container Management Module,
while write requests access Karmada instances, achieving read-write separation and improving response time.

You may wonder how the Container Management Module retrieves resource information for multicloud instances.
The solution is to add the instance itself as a virtual cluster to the Container Management Module
(not displayed in the Container Management). This allows for complete utilization of the Container Management
Module's capabilities (accelerated retrieval of resources, CRDs, etc.). When querying resources
(Deployments, propagation policies, override policies, etc.) for a specific multicloud instance
in the interface, it can be directly retrieved through the Container Management Module.
