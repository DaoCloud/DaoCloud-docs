# Architecture

Multicloud Management (internal code "kairship") has two core components: `kairship apiserver` and `kairship controller-manager`

## kairship apiserver

This is the entrance of data and all APIs. `protobuf` takes priority. All APIs are defined through `proto`, and the corresponding front-end and back-end codes are generated from this. `grpw-gateway` is used to support both HTTP Restful and GRPC.

When `kairship apiserver` starts, it will get the current user's role and permissions from [Global Management](../../ghippo/intro/index.md) module for authentication.

!!! note

    Multicloud Management only verifies permissions of the Karmada instances. The `kairship apiserver` verifies whether the interface from Cat interfaces have permission to operate or access the Karmada instances.

## kairship controller-manager

This is the control plane of Multicloud Management, mainly responsible for processing control logic (each logic has a separate controller), such as syncing instance status, collecting resources, registering Karmada instances and global resources. Changes are listened by list-watch mechanism.

Under multiple deployment, there is a leader selection mechanism to ensure only one Pod is running as the controller manager. Refer to the controller-manager election mechanism of Kubernetes.

Specifically, there are five controllers:

- virtual-cluster-sync-controller

    Listen the CRUD actions of multicloud management CRDs. Once an instance is created, it will create a corresponding virtual Kubernetes cluster for resource management. The same logic also applies to instance deletion.

    It uses [Clusterpedia]( ../../community/clusterpedia.md) for resource retrieval. Clusterpedia is an open-source project contributed by DaoCloud for resource management across clusters. It is integrated into the Container Management module of DCE 5.0

    If the instance is deleted, the virtual cluster registered in the container management module will be deleted synchronously.

- resource statistics controller

    Collect statistical information (e.g., CPU, memory, nodes) of all clusters added under multicloud management instances, and write this info back to the CRD of these multicloud management instances.

- status sync controller

    Collect and Sync status of the multicloud management instances.

- instance registry controller

    Register the `Karmada` instances into [Global Management](../../ghippo/intro/index.md) module through custom resources, so as to bind the permission system of Karmada and DCE 5.0.

    After the binding, these permission mapping relationships will be synced to the Multicloud Management module.

- Ghippo webhook controller

    Bind the roles and permissions with Karmada instances in the [Global Management](../../ghippo/intro/index.md) module, notify the Multicloud Management module through SDKs for authentication.

## Data Flow Diagram

![data-flow](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/arch_kairship_instance.jpg)

Kairship Management API is the only entrance of all requests that come from UI/OpenAPI/internal call. It then distribute these requests to corresponding instances. All read requests are processed by Container Management (`kpanda` in the diagram) and all write requests are processed by Karmada instances. Separate read and write mechanisms can shorten request response time and enhance performance.

You might wonder how can `kpanda` get information of Karmada instances? The answer is, each Karmada instances has a corresponding virtual Kubernetes cluster in `kpanda` module, allowing `kpanda` to collect info as quickly as possible.
