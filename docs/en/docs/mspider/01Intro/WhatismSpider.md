---
hide:
  - toc
---

# What is a service mesh

Service mesh is a next-generation service mesh for cloud-native applications built on Istio open source technology.

Service mesh is a fully managed service mesh product with high performance and high usability. By providing a complete non-intrusive microservice governance solution, it can uniformly manage the complex environment of multicloud and multi-cluster.
Provide users with service traffic governance, security governance, service traffic monitoring, and access to traditional microservices (SpringCloud, Dubbo) in the form of infrastructure.

DCE 5.0's service mesh is compatible with the community's native Istio open source service mesh, providing native Istio access management capabilities. At a high level, a service mesh can help reduce the complexity of service governance and reduce the pressure on DevOps teams.

As a member of the DCE 5.0 product system, the service mesh is seamlessly connected to the [Container Management](../../kpanda/03ProductBrief/WhatisKPanda.md) platform, which can provide users with an out-of-the-box experience.
And as an infrastructure, it provides container microservice governance support for [microservice engine](../../skoala/intro/features.md), which is convenient for users to manage all kinds of microservice systems through a single platform.

The service mesh learning path is as follows:

```mermaid
flowchart TD

    install([install deployment])
    install --> mesh[create mesh]
        subgraph mesh[create mesh]
            managed[managed mesh]
            private[proprietary mesh]
            external [external mesh]
            
        end

    mesh --> cluster[management cluster]

    cluster --> inject[inject sidecar]

        subgraph inject[inject sidecar]
            global [global injection]
            namespace[namespace injection]
            workload [workload injection]
        end

    
    inject -.-> service[service management]
    inject -.-> gateway [gateway]
    inject -.-> traffic[traffic management]
    inject -.-> watch[traffic monitoring]
    inject -.-> upgrade[version upgrade]
    inject -.-> security[Security Governance]

    service -.-> entry[service entry]

    traffic -.-> virtual[virtual service]
    traffic -.-> target[target rule]
    traffic -.-> gaterule[gateway rule]

    security -.-> peer [peer authentication]
    security -.-> request[request authentication]
    security -.-> authorize[authorization policy]

    classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
    classDef k8s fill: #326ce5, stroke: #fff, stroke-width: 1px, color: #fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

    class managed, private, external, global, namespace, workload plain
    class install, service, gateway, traffic, watch, upgrade, security, entry, virtual, target, gaterule, peer, request, authorize, cluster cluster

    click install "https://docs.daocloud.io/mspider/install/"
    click managed "https://docs.daocloud.io/mspider/03UserGuide/servicemesh/create-mesh/"
    click private "https://docs.daocloud.io/mspider/03UserGuide/servicemesh/create-mesh/"
    click external "https://docs.daocloud.io/mspider/03UserGuide/servicemesh/integrate-mesh/"
    click cluster "https://docs.daocloud.io/mspider/03UserGuide/08ClusterManagement/join-clus/"
    click global "https://docs.daocloud.io/mspider/03UserGuide/07SidecarManagement/GlobalSidecar/"
    click namespace "https://docs.daocloud.io/mspider/03UserGuide/07SidecarManagement/NamespaceSidecar/"
    click workload "https://docs.daocloud.io/mspider/03UserGuide/07SidecarManagement/WorkloadSidecar/"
    click gateway "https://docs.daocloud.io/mspider/03UserGuide/09GatewayInstance/create/"
    click service "https://docs.daocloud.io/mspider/03UserGuide/01ServiceList/"
    click traffic "https://docs.daocloud.io/mspider/03UserGuide/02TrafficGovernance/"
    click security "https://docs.daocloud.io/mspider/03UserGuide/05Security/"
    click watch "https://docs.daocloud.io/mspider/03UserGuide/06TrafficMonitor/"
    click upgrade "https://docs.daocloud.io/mspider/03UserGuide/upgrade/IstioUpdate/"
    click entry "https://docs.daocloud.io/mspider/03UserGuide/01ServiceList/service-entry/"
    click virtual "https://docs.daocloud.io/mspider/03UserGuide/02TrafficGovernance/VirtualService/"
    click target "https://docs.daocloud.io/mspider/03UserGuide/02TrafficGovernance/DestinationRules/"
    click gaterule "https://docs.daocloud.io/mspider/03UserGuide/02TrafficGovernance/GatewayRules/"
    click peer "https://docs.daocloud.io/mspider/03UserGuide/05Security/peer/"
    click request "https://docs.daocloud.io/mspider/03UserGuide/05Security/request/"
    click authorize "https://docs.daocloud.io/mspider/03UserGuide/05Security/authorize/"
```

[Download DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/intro.md){ .md-button .md-button--primary }
[Free Trial](../../dce/license0.md){ .md-button .md-button--primary }