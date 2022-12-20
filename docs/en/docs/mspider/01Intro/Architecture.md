---
hide:
  - toc
---

# system structure

The service mesh product has the ability of multi-mesh management and multi-cluster service aggregation governance; users can connect clusters from different sources to the mesh in a multicloud environment for unified traffic management and security management.

In terms of overall architecture, service mesh products can be divided into three levels: global management module, hosted mesh module, managed cluster mesh

![System Architecture](../images/architecture1.png)

- Global management module

    It runs on the independent control plane cluster Global Service Cluster (hereinafter referred to as GSC), which is used to manage multiple service meshs in a unified manner and handle the interaction with end users.
    The main business logic such as resource configuration and security governance of the entire mesh management platform will be constructed at this layer. At the same time, it is also the main module responsible for docking with other systems, so that the adaptation cost of other modules will be reduced.
    Because it does not participate in specific service governance affairs, it does not contain Istio related components.

- Managed mesh module

    Running on the Mesh Control Plane Cluster (hereinafter referred to as MCPC), it is essentially a user working cluster and also has the role of a mesh control plane. One GSC can manage multiple MCPCs.
    Core control components such as Istio will be installed in the cluster as the core control plane of the mesh to directly manage multiple clusters in the mesh, perform unified policy control and service discovery, and actually execute and deliver various traffic policies and Security policies, and ensure that only policies written to MCPC will take effect for the entire mesh.

- hosted cluster mesh

    The actual working cluster in a mesh contains the basic components of Istio, but it will not be used as a control plane. It only provides a mode similar to a management agent, which is mainly responsible for sidecar injection, certificate forwarding, xDS forwarding and other services. Synchronize policies and service registration information from MCPC and send them to the business sidecar of the cluster.

The expansion modules that run through the overall architecture mainly include: observation module, microservice platform/application workbench

- Observation module

    Observability is completely handled by Insight. The service mesh obtains traffic indicator information to draw a topology map through interface calls, and directly calls Istio's native grafana to provide users with various indicator charts.

- Microservice Platform/Application Workbench

    The microservice platform can empower its microservices with mesh capabilities through the mesh, which is convenient for users to conduct unified management of various microservice systems through a single platform.

## Functional Architecture

![Service Mesh Features](../images/features.png)

As shown in the figure above, the service mesh provides 9 modules and 12 sub-module functions, realizing the ability of diversified cluster access and mesh management in multiple modes.