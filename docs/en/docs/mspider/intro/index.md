---
MTPE: windsonsea
date: 2024-01-10
hide:
  - toc
---

# Service Mesh

Service mesh is the next generation service mesh for cloud native applications, built on
the open-source technology of Istio. It provides a complete non-intrusive microservices
governance solution to unify the governance of complex multicloud and multicluster
environments, offering service traffic governance, security governance, service traffic
monitoring, and traditional microservices (SpringCloud, Dubbo) capabilities as infrastructure.

DCE's service mesh is compatible with the native Istio open-source service mesh and provides
native Istio access management capabilities. At a higher level, a service mesh helps reduce the
complexity of service governance and alleviate the pressure on development and operations teams.
The service mesh seamlessly integrates with the [container management](../../kpanda/intro/index.md)
platform and serves as infrastructure support for the [microservice engine](../../skoala/intro/index.md),
enabling unified management of various microservice systems through a single platform.

## Key Capabilities

<div class="grid cards" markdown>

- :material-lan:{ .lg .middle } __Mesh Creation and Management__

    ---

    Supports hosted, dedicated, and external mesh modes, covering mesh creation, deletion, and capacity management, with an operations-free managed control plane.

    [:arrow_forward: Create a mesh](../user-guide/service-mesh/index.md)

- :material-swap-horizontal:{ .lg .middle } __Traffic Governance__

    ---

    Configure weighted, content-based, and TCP/IP routing policies with virtual services, destination rules, and gateway rules for dynamic intelligent routing and elastic traffic management.

    [:arrow_forward: Traffic governance](../user-guide/traffic-governance/README.md)

- :material-chart-line:{ .lg .middle } __Traffic Monitoring__

    ---

    Visually displays link information, abnormal service responses, and excessively long response latency, with traffic topology for faster problem localization.

    [:arrow_forward: Traffic monitoring](../user-guide/traffic-monitor/README.md)

- :material-shield-check:{ .lg .middle } __Security Governance__

    ---

    Provides peer authentication, request authentication, and authorization policies to secure service-to-service communication with mTLS.

    [:arrow_forward: Security governance](../user-guide/security/README.md)

- :material-car-outline:{ .lg .middle } __Sidecar Management__

    ---

    Inject sidecars by namespace or workload, with sidecar resource optimization, traffic passthrough, and log level adjustment.

    [:arrow_forward: Sidecar management](../user-guide/sidecar-management/ns-sidecar.md)

- :material-gate:{ .lg .middle } __Mesh Gateway__

    ---

    Create and manage mesh gateway instances to provide a unified north-south traffic entry for services in the mesh.

    [:arrow_forward: Create a gateway instance](../user-guide/gateway-instance/create.md)

</div>

## Workflow

Using the service mesh typically involves two phases, **deployment and integration** followed by **governance and observation**: administrators deploy the module, create a mesh, and integrate clusters; business users then inject sidecars and start using traffic governance, security governance, and traffic monitoring capabilities.

```mermaid
flowchart LR
    A["① Install and deploy<br/>Deploy the service mesh module"] --> B["② Create a mesh<br/>Hosted · dedicated · external"]
    B --> C["③ Integrate clusters<br/>Clusters join the mesh"]
    C --> D["④ Inject sidecars<br/>Namespace · workload"]
    D --> E["⑤ Govern and observe<br/>Traffic · security · monitoring"]

    click A href "../install/install/"
    click B href "../user-guide/service-mesh/"
    click C href "../user-guide/cluster-management/join-clus/"
    click D href "../user-guide/sidecar-management/ns-sidecar/"
    click E href "../user-guide/traffic-governance/"
```

| Step | Role | Description |
| --- | --- | --- |
| ① [Install and deploy](../install/install.md) | Platform administrator | Deploy the service mesh module in the DCE cluster |
| ② [Create a mesh](../user-guide/service-mesh/index.md) | Platform administrator | Create a mesh in hosted, dedicated, or external mode |
| ③ [Integrate clusters](../user-guide/cluster-management/join-clus.md) | Platform administrator | Add one or more clusters to the mesh for unified management |
| ④ [Inject sidecars](../user-guide/sidecar-management/ns-sidecar.md) | Business user | Inject sidecar proxies by namespace or workload |
| ⑤ [Traffic governance](../user-guide/traffic-governance/README.md) and [traffic monitoring](../user-guide/traffic-monitor/README.md) | Business user | Configure routing and security policies, and monitor service status in real time |

## Product Advantages

DCE's service mesh has the following advantages compared to other products:

| Advantage | Description |
| --------- | ----------- |
| Simple and easy to use | No need to modify any business code or manually install proxies — just enable the service mesh feature to experience non-intrusive service governance |
| Policy-based intelligent routing and elastic traffic management | Weighted, content-based, and TCP/IP routing rules; HTTP session persistence; rate limiting and outlier detection; network connection management; service authentication, authorization, and auditing |
| Graphical application panoramic topology | Visualized monitoring of link information, abnormal service responses, and long response latency, with invocation chain information for faster problem localization |
| Enhanced performance and reliability | Control plane and data plane are hardened and performance-optimized on top of the community version |
| Multi-cloud, multi-cluster, and multi-infrastructure | Operations-free managed control plane with unified governance, security, and monitoring; unified service discovery and management for containers, VMs, and other infrastructures |
| Protocol extension | Supports the Dubbo protocol |
| Traditional SDK integration | Applications built with Spring Cloud, Dubbo, and other traditional microservice SDKs can be migrated to the cloud native mesh environment without extensive code modification |

## Quick Start

<style>
.mspider-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.mspider-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.mspider-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.mspider-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.mspider-path-step:last-child::after{display:none}
.mspider-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.mspider-path-title{font-weight:700;font-size:0.95rem}
.mspider-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.mspider-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.mspider-path-step::after{display:none}}
</style>

<div class="mspider-path">
  <a class="mspider-path-step" style="--path-c:#2196f3" href="../install/install/">
    <span class="mspider-path-num">1</span>
    <span class="mspider-path-title">Install and deploy</span>
    <span class="mspider-path-desc">Deploy the service mesh module</span>
    <span class="mspider-path-go">Go →</span>
  </a>
  <a class="mspider-path-step" style="--path-c:#00acc1" href="../user-guide/service-mesh/">
    <span class="mspider-path-num">2</span>
    <span class="mspider-path-title">Create a mesh</span>
    <span class="mspider-path-desc">Hosted · dedicated · external</span>
    <span class="mspider-path-go">Go →</span>
  </a>
  <a class="mspider-path-step" style="--path-c:#43a047" href="../user-guide/cluster-management/join-clus/">
    <span class="mspider-path-num">3</span>
    <span class="mspider-path-title">Integrate clusters</span>
    <span class="mspider-path-desc">Clusters join the mesh</span>
    <span class="mspider-path-go">Go →</span>
  </a>
  <a class="mspider-path-step" style="--path-c:#fb8c00" href="../user-guide/sidecar-management/ns-sidecar/">
    <span class="mspider-path-num">4</span>
    <span class="mspider-path-title">Inject sidecars</span>
    <span class="mspider-path-desc">Namespace · workload</span>
    <span class="mspider-path-go">Go →</span>
  </a>
  <a class="mspider-path-step" style="--path-c:#8e24aa" href="../user-guide/traffic-governance/">
    <span class="mspider-path-num">5</span>
    <span class="mspider-path-title">Govern and observe</span>
    <span class="mspider-path-desc">Traffic · security · monitoring</span>
    <span class="mspider-path-go">Go →</span>
  </a>
</div>

## More Resources

<div class="grid cards" markdown>

- :material-format-list-bulleted:{ .lg .middle } __Features__

    ---

    A complete list of service mesh capabilities, from mesh management and traffic governance to security and monitoring.

    [:arrow_forward: View features](features.md)

- :material-map-outline:{ .lg .middle } __Architecture__

    ---

    Understand the overall architecture of the service mesh, its control plane components, and system namespaces.

    [:arrow_forward: View architecture](comp-archi-ui/index.md)

- :material-chat-question-outline:{ .lg .middle } __FAQ__

    ---

    Common questions and solutions related to service mesh usage.

    [:arrow_forward: View FAQ](faq.md)

- :material-bug-outline:{ .lg .middle } __Troubleshooting__

    ---

    A continuously updated troubleshooting handbook covering mesh creation, cluster integration, sidecar issues, and more.

    [:arrow_forward: View troubleshooting](../troubleshoot/index.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
[View the Service Mesh User Guide (PDF)](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/mspider.pdf){ .md-button }
