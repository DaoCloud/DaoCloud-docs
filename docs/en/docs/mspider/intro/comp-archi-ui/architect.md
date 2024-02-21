---
MTPE: windsonsea
date: 2024-02-21
hide:
  - toc
---

# Architecture of Service Mesh

The service mesh module enables multi-mesh management and multicluster service aggregation governance.
Users can connect clusters from different sources to the mesh in a multicloud environment for
unified traffic and security management.

In terms of overall architecture, service mesh products can be divided into three levels:
global mesh management, control plane, and data plane.

![architecture](../../images/architecture1.svg)

- **Global mesh management**

    This module runs on an independent control plane cluster called the Global Service Cluster (GSC).
    It manages multiple service meshes in a unified way and handles interactions with end-users.
    The entire mesh management platform's main business logic, such as resource configuration and
    security governance, is constructed at this layer. It is also the primary module responsible
    for docking with other systems, reducing the adaptation cost of other modules. As it does not
    participate in specific service governance affairs, it does not contain Istio related components.

- **Control plane**

    This module runs on the Mesh Control Plane Cluster (MCPC), which is essentially a user working cluster
    and mesh control plane. One GSC can manage multiple MCPCs. Core control components such as Istio are
    installed in the cluster as the core control plane of the mesh to directly manage multiple clusters
    in the mesh. It performs unified policy control and service discovery and executes and delivers various
    traffic policies and security policies. Only policies written to MCPC take effect for the entire mesh.

- **Data plane**

    This module contains the basic components of Istio but is not used as a control plane. It provides
    a mode similar to a management agent, responsible for sidecar injection, certificate forwarding,
    xDS forwarding, and other services. It synchronizes policies and service registration information
    from MCPC and sends them to the business sidecar of the cluster.

Extension modules that run through the overall architecture include observability, microservice governance, and Workbench.

- **Observability**

    Observability is handled by [Insight](../../../insight/intro/index.md). The service mesh obtains
    traffic metric information to draw a topology map through interface calls and directly calls
    Istio's native Grafana to provide users with various metric charts.

- **Microservice**

    The microservice platform empowers microservices with mesh capabilities through the mesh,
    enabling users to conduct unified management of various microservice systems through a single platform.

- **Workbench**

    Workbench is a core module of DCE 5.0, which is used to provide users with unified capabilities
    such as application orchestration, deployment, pipeline management, CICD, application monitoring, and log querying.

## Functional Architecture

```mermaid
graph LR

    mesh([Service Mesh]) -.- overview[Mesh Overview]
    mesh -.- service[Service Management]
    mesh -.- traffic[Traffic Management]
        traffic -.- vs[Virtual Service]
        traffic -.- dr[Destination Rule]
        traffic -.- gw[Gateway]
    mesh -.- security[Security]
        security -.- peer[Peer Authentication]
        security -.- request[Request Authentication]
        security -.- authz[Authorization]
    mesh -.- monitor[Monitor]
        monitor -.- tp[Topology]
        monitor -.- list[Monitor Metrics]
    mesh -.- sidecar[Sidecars]
        sidecar -.- ns[Namespace Sidecar]
        sidecar -.- workload[Workload Sidecar]
    mesh -.- cluster[Mesh Cluster]
    mesh -.- meshgw[Mesh Gateway]
    mesh -.- config[Mesh Config] -.- istio[Istio Resources]

click vs "https://docs.daocloud.io/en/mspider/user-guide/traffic-governance/virtual-service/"
click dr "https://docs.daocloud.io/en/mspider/user-guide/traffic-governance/destination-rules/"
click gw "https://docs.daocloud.io/en/mspider/user-guide/traffic-governance/gateway-rules/"
click peer "https://docs.daocloud.io/en/mspider/user-guide/security/peer/"
click request "https://docs.daocloud.io/en/mspider/user-guide/security/request/"
click authz "https://docs.daocloud.io/en/mspider/user-guide/security/authorize/"
click tp "https://docs.daocloud.io/en/mspider/user-guide/traffic-monitor/conn-topo/"
click list "https://docs.daocloud.io/en/mspider/user-guide/traffic-monitor/monitoring-indicators/"
click ns "https://docs.daocloud.io/en/mspider/user-guide/sidecar-management/ns-sidecar/"
click workload "https://docs.daocloud.io/en/mspider/user-guide/sidecar-management/workload-sidecar/"
click istio "https://docs.daocloud.io/en/mspider/user-guide/mesh-config/istio-resources/"

 classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
 classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
 classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;
 class mesh,overview,service,traffic,security,monitor,sidecar,cluster,meshgw,config k8s;
 class vs,dr,gw,peer,request,authz,tp,list,ns,workload,global,istio cluster;
```

As shown in the figure above, the service mesh provides nine modules and twelve sub-module features, realizing the ability of diversified cluster access and mesh management in multiple modes.
