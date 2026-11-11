---
MTPE: windsonsea
date: 2024-07-17
hide:
  - toc
---

# What is Cloud Edge Collaboration

The number of IoT access nodes is growing explosively, and centralized cloud computing can no longer meet the requirements for transmitting and processing massive volumes of data in real time. Cloud Edge Collaboration (Kant) extends cloud-native capabilities to the edge with an integrated device-edge-cloud architecture, moving data processing, business applications, and AI models down to the edge for execution. The cloud manages edge nodes, applications, and devices centrally; the edge keeps running autonomously on weak or offline networks; and the device side supports multi-protocol terminal access. This addresses response latency, data privacy, and maintenance convenience in industrial Internet, smart factories, smart parks, smart retail, and similar scenarios.

## Product Architecture

![Cloud Edge Collaboration Architecture](../images/kant-arch.svg)

The architecture consists of three layers, from top to bottom: cloud, edge, and devices.

| Layer | Component | Responsibility | In the diagram |
| --- | --- | --- | --- |
| **Cloud** | Management plane | Centrally manages edge nodes, delivers applications and models, manages device twins, and configures message endpoints and routes | Blue area |
| **Cloud** | Kubernetes cluster / operating system | Hosts the cloud control plane, delivers applications, configurations, and models to the edge, and receives data and status reports | Blue bars, orange dashed line |
| **Edge** | Applications / models, edge control | Runs containerized applications and models; provides resource control, edge O&M, device data collection and protocol conversion, and data channels | Green area |
| **Edge** | Container engine, operating system, infrastructure | Runs on x86, ARM, and network, compute, and storage resources; keeps workloads running on weak or offline networks | Green base |
| **Devices** | Multi-protocol terminals and smart IoT devices | Connect to edge nodes through protocols such as Modbus and the DMI standard interface; collect and report data nearby | Orange area, gray arrows |

## Key Capabilities

Cloud Edge Collaboration provides a complete set of capabilities around edge nodes, applications and models, end devices, and data collaboration:

<div class="grid cards" markdown>

-   :material-server-network:{ .lg .middle } __Edge Node Management__

    ---

    Supports onboarding a vast number of edge nodes with token- or certificate-based management, and enables unified management, monitoring, and operation of nodes and node groups from the cloud.

    [:arrow_forward: Overview of Edge Nodes](../user-guide/node/index.md)

-   :material-cube-outline:{ .lg .middle } __Edge Applications and Models__

    ---

    Packages applications or models as container images and deploys them to edge nodes quickly; provides runtime data, events, and logs, as well as CPU / GPU scheduling.

    [:arrow_forward: Overview of Edge Applications](../user-guide/edge-app/index.md)

-   :material-developer-board:{ .lg .middle } __End Device Access__

    ---

    Supports terminal access over multiple protocols such as Modbus, connects device capabilities through the standard DMI, and manages devices and device twins centrally from the cloud.

    [:arrow_forward: End Device Overview](../user-guide/device/index.md)

-   :material-transit-connection-variant:{ .lg .middle } __Edge-Cloud Message Routing__

    ---

    Configures message routing rules to forward edge messages by path to REST, EventBus, ServiceBus, and other endpoints; supports bidirectional cloud-edge transfer of unstructured data such as images and videos.

    [:arrow_forward: Edge-Cloud Messages](../user-guide/route/index.md)

-   :material-lan:{ .lg .middle } __Edge Mesh__

    ---

    Implements a closed loop of edge business traffic through service discovery and traffic proxy, solving edge-to-edge communication problems in edge scenarios.

    [:arrow_forward: Edge Mesh Overview](../user-guide/edge-network/index.md)

-   :material-shield-check-outline:{ .lg .middle } __Edge Autonomy and Security__

    ---

    Edge nodes remain self-managing on weak or offline networks; provides platform, folder, and workspace-level permissions, mutual cloud-edge TLS encryption, and audit logs.

    [:arrow_forward: Product Advantages](benefits.md)

</div>

## Learning Path

Follow these steps in order to go from creating an edge unit to enabling cloud-edge data transfer:

<style>
.kant-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.kant-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.kant-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.kant-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.kant-path-step:last-child::after{display:none}
.kant-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.kant-path-title{font-weight:700;font-size:0.95rem}
.kant-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.kant-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.kant-path-step{flex:1 1 100%}.kant-path-step::after{display:none}}
</style>

<div class="kant-path">
  <a class="kant-path-step" style="--path-c:#2196f3" href="../user-guide/edge-unit/create-internal-unit/">
    <span class="kant-path-num">1</span>
    <span class="kant-path-title">Create Edge Unit</span>
    <span class="kant-path-desc">Create an internal edge unit</span>
    <span class="kant-path-go">Go →</span>
  </a>
  <a class="kant-path-step" style="--path-c:#00acc1" href="../user-guide/node/access-guide/">
    <span class="kant-path-num">2</span>
    <span class="kant-path-title">Onboard Node</span>
    <span class="kant-path-desc">Register a node with a token or certificate</span>
    <span class="kant-path-go">Go →</span>
  </a>
  <a class="kant-path-step" style="--path-c:#43a047" href="../user-guide/edge-app/create-app/">
    <span class="kant-path-num">3</span>
    <span class="kant-path-title">Deploy App</span>
    <span class="kant-path-desc">Run an app or model on edge nodes</span>
    <span class="kant-path-go">Go →</span>
  </a>
  <a class="kant-path-step" style="--path-c:#fb8c00" href="../user-guide/device/create-device-model/">
    <span class="kant-path-num">4</span>
    <span class="kant-path-title">Connect Devices</span>
    <span class="kant-path-desc">Define device models, add devices and set routes</span>
    <span class="kant-path-go">Go →</span>
  </a>
</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
[View User Manual (PDF)](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/kant.pdf){ .md-button }
