# What is Service Mesh?

Service Mesh is a next-generation, cloud native service mesh built on the open-source Istio technology.
It is a fully managed product with high performance and usability, providing a complete non-intrusive
microservice governance solution that can uniformly manage multi-cloud and multi-cluster environments.

Service Mesh offers service traffic governance, security governance, and service traffic monitoring to its users.
It allows access to traditional microservices in the form of infrastructure. The platform is seamlessly connected
to the DCE Container Management platform, providing an out-of-the-box experience to users. As an infrastructure,
it provides container microservice governance support for the microservice engine, making it easy for users to
manage all microservice systems through a single platform.

Service Mesh is compatible with the native Istio open-source service mesh, providing native Istio access management.
At a high level, Service Mesh helps reduce the complexity of service governance and decrease pressure on DevOps teams.
It streamlines microservice governance by providing an all-in-one solution that simplifies multi-cloud and multi-cluster environments.

## Product Benefits

DCE 5.0 Service Mesh offers several advantages compared to other products:

- Easy to Use: Users do not need to modify any business code or manually install agents.
  They can enable Service Mesh feature and experience rich non-intrusive service governance capabilities.

- Strategic Intelligent Routing and Elastic Traffic Management: Supports configuring load balancing, service routing,
  fault injection, circuit breaking, and other governance rules for services. Combined with a one-stop management
  system, it provides real-time, visualized micro-service traffic management that supports non-intrusive intelligent
  traffic management. It can perform dynamic intelligent routing and elastic traffic management without modifying
  the application. The following are additional features:

    - Routing rules such as weight, content, TCP/IP, etc.
    - HTTP sessions are maintained to meet the demands of business processing continuity.
    - Current limiting and fusing to achieve stable and reliable traces between services.
    - Network persistent connection management reduces resource loss and improves network throughput.
    - Service security certification: certification, authentication, audit, etc., providing the cornerstone of service security.

- Graphical Application Panorama Topology and Visualized Traffic Management: Provides visual traffic monitoring,
  including link information, service abnormal response, and long response delay, and comprehensively displays
  business operation status through charts and topologies. Service Mesh combines application operation and maintenance
  management and application performance management services to provide detailed microservice-level traffic monitoring,
  abnormal response traffic reports, and call chain information, enabling faster and more accurate location of problems.

- Enhanced Performance and Increased Reliability: The Service Mesh control plane and data plane are
  more reliable and performance-optimized based on the community version.

- Multicloud, Multicluster, Multi-infrastructure: Provides an O&M-free hosting control plane and offers multicloud
  and multicluster global unified service governance, security, and service operation monitoring capabilities.
  It also provides unified service discovery and management for multiple infrastructures such as containers
  and virtual machines (VMs).

- Protocol Extensions: Extend the support of Dubbo protocol.

- Legacy SDK Integration: Provides integrated solutions for traditional microservice SDKs such as Spring Cloud
  and Dubbo. Businesses developed by traditional microservice SDKs can be quickly migrated to cloud native mesh
  operating environments without extensive code modification.

## Learning Path

The learning path for the service mesh is as follows:

```mermaid
flowchart TD

    install([Installation and Deployment])
    install --> mesh[Create a Mesh]
        subgraph mesh[Create a Mesh]
            managed[Hosted Mesh]
            private[Dedicated Mesh]
            external[External Mesh]
            
        end

    mesh --> cluster[Cluster Management]

    cluster --> inject[Sidecar Injection]

        subgraph inject[Sidecar Injection]
            namespace[Namespace Injection]
            workload[Workload Injection]
        end

    
    inject -.-> service[Service Management]
    inject -.-> traffic[Traffic Management]
    inject -.-> security[Security]
    inject -.-> sidecar[Mesh Sidecar]
    inject -.-> watch[Traffic Monitor]
    inject -.-> gateway[Mesh Gateway]
    inject -.-> upgrade[Upgrade]
    

    service -.-> entry[Service Entry<br>One-Click Repair]
    traffic -.-> virtual[Virtual Service<br>Destination Rule<br>Gateway Rule]
    security -.-> peer[Peer Authentication<br>Request Authentication<br>Authorization Policy]
    sidecar -.-> sidecarm[Namespace Sidecar<br>Workload Sidecar<br>Traffic Passthrough]
    watch -.-> watch2[Traffic Monitor<br>Traffic Topology]
    upgrade -.-> upgrade1[Upgrade Istio<br>Upgrade Sidecar]

    classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

    class mesh plain
    class install,service,gateway,traffic,watch,upgrade,security,entry,virtual,peer,cluster,sidecar,sidecarm,watch2,managed,private,external,namespace,workload,upgrade1 cluster

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

[Download DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
[Free Trial](../../dce/license0.md){ .md-button .md-button--primary }
