---
hide:
  - toc
---

# What is a service mesh

Service mesh is a next-generation service mesh for cloud-native applications built on Istio open source technology.

Service mesh is a fully managed service mesh product with high performance and high usability. By providing a complete non-intrusive microservice governance solution, it can uniformly manage the complex environment of multicloud and multi-cluster.
Provide users with service traffic governance, security governance, service traffic monitoring, and access to traditional microservices (SpringCloud, Dubbo) in the form of infrastructure.

DCE 5.0's service mesh is compatible with the community's native Istio open source service mesh, providing native Istio access management capabilities. At a high level, a service mesh can help reduce the complexity of service governance and reduce the pressure on DevOps teams.

As a member of the DCE 5.0 product system, the service mesh is seamlessly connected to the [Container Management](../../kpanda/intro/what.md) platform, which can provide users with an out-of-the-box experience.
And as an infrastructure, it provides container microservice governance support for [microservice engine](../../skoala/intro/features.md), which is convenient for users to manage all kinds of microservice systems through a single platform.

## Product benefits

Here are the advantages of DCE 5.0 service mesh compared to other products.

- easy to use

    There is no need to modify any business code or manually install agents, just enable the service mesh function to experience rich non-intrusive service governance capabilities.

- Strategic intelligent routing and elastic traffic management

    Supports configuring load balancing, service routing, fault injection, circuit breaking and other governance rules for services. Combined with a one-stop management system; provides real-time, visualized micro-service traffic management; supports non-intrusive intelligent traffic management, and can perform dynamic intelligent routing and elastic traffic management without any modification of the application.

    - Routing rules such as weight, content, TCP/IP, etc.

    - HTTP sessions are maintained to meet the demands of business processing continuity.

    - Current limiting and fusing to achieve stable and reliable links between services.

    - Network persistent connection management reduces resource loss and improves network throughput.

    - Service security certification: certification, authentication, audit, etc., providing the cornerstone of service security.

- Graphical application panorama topology, visualized traffic management

    The service mesh provides visual traffic monitoring, including information such as link information, service abnormal response, and long response delay, and comprehensively displays business operation status through charts and topologies.

    The service mesh can combine application operation and maintenance management and application performance management services to provide detailed microservice-level traffic monitoring, abnormal response traffic reports, and call chain information, enabling faster and more accurate location of problems.

- Enhanced performance, increased reliability

    The service mesh control plane and data plane are more reliable and performance optimized based on the community version.

- Multicloud, multi-cluster, multi-infrastructure

    Provides an O&M-free hosting control plane, provides multicloud and multi-cluster global unified service governance, security, and service operation monitoring capabilities, and also provides unified service discovery and management for multiple infrastructures such as containers and virtual machines (VMs).

- Protocol extensions

    Extend the support of Dubbo protocol.

- Legacy SDK integration

    Provide integrated solutions for traditional microservice SDKs such as Spring Cloud and Dubbo. Businesses developed by traditional microservice SDKs can be quickly migrated to cloud-native mesh operating environments without extensive code modification.

## To use service mesh

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
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

    class managed,private,external,global,namespace,workload plain
    class install,service,gateway,traffic,watch,upgrade,security,entry,virtual,peer,cluster,sidecar,sidecarm,watch2 cluster

    click install "https://docs.daocloud.io/en/mspider/install/install/"
    click managed "https://docs.daocloud.io/en/mspider/user-guide/service-mesh/"
    click private "https://docs.daocloud.io/en/mspider/user-guide/service-mesh/"
    click external "https://docs.daocloud.io/en/mspider/user-guide/service-mesh/external-mesh/"
    click cluster "https://docs.daocloud.io/en/mspider/user-guide/cluster-management/join-clus/"
    click global "https://docs.daocloud.io/en/mspider/user-guide/sidecar-management/global-sidecar/"
    click namespace "https://docs.daocloud.io/en/mspider/user-guide/sidecar-management/ns-sidecar/"
    click workload "https://docs.daocloud.io/en/mspider/user-guide/sidecar-management/workload-sidecar/"
    click gateway "https://docs.daocloud.io/en/mspider/user-guide/gateway-instance/create/"
    click service "https://docs.daocloud.io/en/mspider/user-guide/service-list/"
    click traffic "https://docs.daocloud.io/en/mspider/user-guide/traffic-governance/"
    click security "https://docs.daocloud.io/en/mspider/user-guide/security/"
    click watch "https://docs.daocloud.io/en/mspider/user-guide/traffic-monitor/"
    click upgrade "https://docs.daocloud.io/en/mspider/user-guide/upgrade/istio-update/"
    click entry "https://docs.daocloud.io/en/mspider/user-guide/service-list/service-entry/"
    click virtual "https://docs.daocloud.io/en/mspider/user-guide/traffic-governance/virtual-service/"
    click peer "https://docs.daocloud.io/en/mspider/user-guide/security/peer/"
    click sidecar "https://docs.daocloud.io/en/mspider/user-guide/sidecar-management/ns-sidecar/"
    click sidecarm "https://docs.daocloud.io/en/mspider/user-guide/sidecar-management/passthrough/"
    click watch2 "https://docs.daocloud.io/en/mspider/user-guide/traffic-monitor/conn-topo/"
```

[Download DCE 5.0](../../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/intro.md){ .md-button .md-button--primary }
[Free Trial](../../dce/license0.md){ .md-button .md-button--primary }