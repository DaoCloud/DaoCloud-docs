---
hide:
  - toc
---

# Multicloud Management

Multicloud Management (Kairship) is an application-centric, out-of-the-box orchestration platform
for multicloud applications. It enables centralized management of multicloud and hybrid-cloud
environments, providing cross-cloud application deployment, release, and operations capabilities.
It supports application autoscaling based on cluster resources to achieve global load balancing,
and offers failover capabilities that thoroughly address disaster recovery for multicloud applications.
Developers can use multiple clouds as if they were a single Kubernetes cluster: it is compatible
with native Kubernetes APIs, upgrades from single-cluster to multi-cluster with zero modification,
and seamlessly integrates with the existing single-cluster toolchain ecosystem.

![From single cloud to multicloud](../images/what.svg)

## Key Capabilities

<div class="grid cards" markdown>

- :material-cloud-plus-outline:{ .lg .middle } __Multicloud Application Deployment__

    ---

    Define multi-cluster scheduling requirements with the PropagationPolicy deployment policy, supporting 1:N policy mapping and default policies to distribute workloads across clouds.

    [:arrow_forward: Configure deployment policies](../policy/propagation.md)

- :material-swap-horizontal:{ .lg .middle } __One-Click Conversion__

    ---

    Convert single-cloud workloads to multicloud workloads with one click, migrating existing applications with zero modification.

    [:arrow_forward: One-click conversion](../workload/promote.md)

- :material-tune:{ .lg .middle } __Differentiated Configuration__

    ---

    Automatically generate differentiated configurations for different clusters with OverridePolicy, such as adapting image registry addresses by region or storage classes by cloud vendor.

    [:arrow_forward: Configure override policies](../policy/override.md)

- :material-chart-line:{ .lg .middle } __Global Autoscaling__

    ---

    Scale applications based on cluster resources, with cross-cluster FHPA autoscaling support for global load balancing.

    [:arrow_forward: Cross-cluster autoscaling](../best-practice/fhpa.md)

- :material-cloud-sync-outline:{ .lg .middle } __Failure Recovery__

    ---

    Built-in policy sets for multiple scenarios — two cities and three centers, dual-active within a city, and cross-region disaster recovery — with failover to solve multicloud application disaster recovery.

    [:arrow_forward: Failover](../failover/failover.md)

- :material-cube-outline:{ .lg .middle } __Multicloud Resource Management__

    ---

    Centrally manage multicloud workloads and resources such as ConfigMap, Secret, Service, and Ingress, with support for multicloud custom resources (CRDs).

    [:arrow_forward: Create multicloud workloads](../workload/deployment.md)

</div>

## Workflow

Using multicloud management typically involves two phases, **environment preparation** and **application governance**: administrators first create a multicloud instance and integrate worker clusters, then business users create multicloud workloads, configure scheduling policies, and keep applications running stably with autoscaling and failover.

```mermaid
flowchart LR
    A["① Create a multicloud instance<br/>Management entry point"] --> B["② Integrate worker clusters<br/>Manage existing Kubernetes clusters"]
    B --> C["③ Create multicloud workloads<br/>Forms · YAML · one-click conversion"]
    C --> D["④ Configure scheduling policies<br/>PropagationPolicy · OverridePolicy"]
    D --> E["⑤ Autoscaling & failover<br/>FHPA · disaster recovery"]

    click A href "../instance/add/"
    click B href "../cluster/"
    click C href "../workload/deployment/"
    click D href "../policy/propagation/"
    click E href "../failover/failover/"
```

| Step | Role | Description |
| --- | --- | --- |
| ① [Create a multicloud instance](../instance/add.md) | Platform administrator | Create a multicloud instance as the management entry point for multicloud resources and policies |
| ② [Manage worker clusters](../cluster.md) | Platform administrator | Integrate or register member clusters for unified multicloud scheduling |
| ③ [Create multicloud workloads](../workload/deployment.md) | Business user | Create multicloud Deployments via forms or YAML, or [convert](../workload/promote.md) single-cloud applications with one click |
| ④ Configure [deployment policies](../policy/propagation.md) and [override policies](../policy/override.md) | Business user | Define multi-cluster scheduling requirements and generate differentiated configurations per cluster as needed |
| ⑤ [Failover](../failover/failover.md) and [cross-cluster autoscaling](../best-practice/fhpa.md) | Platform administrator | Configure FHPA to handle load fluctuations and use failover to ensure business continuity |

## Basic Concepts

| Concept | Description |
| ------- | ----------- |
| **Resource Template** | The multicloud management software uses Kubernetes native APIs to define federated resource templates, enabling seamless integration with existing Kubernetes tooling. |
| **Deployment Policy** | The multicloud management software provides an independent `PropagationPolicy` API to define multi-cluster scheduling requirements. |
| | - Supports a **1:N policy mapping mechanism**, allowing users to avoid specifying scheduling constraints every time a federated application is created. |
| | - With the **default policy**, users can interact directly with the Kubernetes API. |
| **Differentiation Policy** | The multicloud management software provides an `OverridePolicy` API to automatically generate independent configurations for different clusters. |
| | - Automatically configures different image registry addresses based on the region of the member cluster. |
| | - Uses different storage classes according to cloud vendors of the clusters. |

## Product Advantages

Empowering developers to use **multicloud as if it were a single Kubernetes cluster**, multicloud management offers the following advantages:

| Advantage | Description |
| --------- | ----------- |
| Compatible with Kubernetes native API | Upgrade from single-cluster to multi-cluster with zero modification. |
| Seamless integration with the Kubernetes toolchain ecosystem | Freedom from vendor lock-in: multicloud platform support, automatic allocation, and flexible migration; no dependency on commercial vendor products. |
| Rich multi-cluster scheduling | Cluster affinity scheduling for high-availability multi-cluster deployments with fine granularity; supports multiple regions, availability zones, clusters, and vendors. |
| Open and neutral | Jointly initiated by organizations from internet, finance, manufacturing, telecommunications, and cloud industries; out-of-the-box built-in policy sets for multiple scenarios — dual-active across cities, two-city three-center DR, and cross-region disaster recovery. |
| Centralized management | No need to worry about cluster location; supports public cloud, private cloud, and edge clusters. |

## Quick Start

<style>
.kairship-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.kairship-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.kairship-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.kairship-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.kairship-path-step:last-child::after{display:none}
.kairship-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.kairship-path-title{font-weight:700;font-size:0.95rem}
.kairship-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.kairship-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.kairship-path-step::after{display:none}}
</style>

<div class="kairship-path">
  <a class="kairship-path-step" style="--path-c:#2196f3" href="../instance/add/">
    <span class="kairship-path-num">1</span>
    <span class="kairship-path-title">Create an instance</span>
    <span class="kairship-path-desc">Management entry point</span>
    <span class="kairship-path-go">Go →</span>
  </a>
  <a class="kairship-path-step" style="--path-c:#00acc1" href="../cluster/">
    <span class="kairship-path-num">2</span>
    <span class="kairship-path-title">Integrate clusters</span>
    <span class="kairship-path-desc">Manage existing Kubernetes clusters</span>
    <span class="kairship-path-go">Go →</span>
  </a>
  <a class="kairship-path-step" style="--path-c:#43a047" href="../workload/deployment/">
    <span class="kairship-path-num">3</span>
    <span class="kairship-path-title">Create workloads</span>
    <span class="kairship-path-desc">Forms · YAML · one-click conversion</span>
    <span class="kairship-path-go">Go →</span>
  </a>
  <a class="kairship-path-step" style="--path-c:#fb8c00" href="../policy/propagation/">
    <span class="kairship-path-num">4</span>
    <span class="kairship-path-title">Configure policies</span>
    <span class="kairship-path-desc">PropagationPolicy · OverridePolicy</span>
    <span class="kairship-path-go">Go →</span>
  </a>
  <a class="kairship-path-step" style="--path-c:#8e24aa" href="../failover/failover/">
    <span class="kairship-path-num">5</span>
    <span class="kairship-path-title">Scaling & DR</span>
    <span class="kairship-path-desc">FHPA · failover</span>
    <span class="kairship-path-go">Go →</span>
  </a>
</div>

## More Resources

<div class="grid cards" markdown>

- :material-format-list-bulleted:{ .lg .middle } __Features__

    ---

    A complete list of multicloud management capabilities, from one-click conversion and scheduling policies to global load balancing and failover.

    [:arrow_forward: View features](features.md)

- :material-play-circle-outline:{ .lg .middle } __Demo Video__

    ---

    Watch a demo of converting a single-cloud application to a multicloud application with one click.

    [:arrow_forward: Watch the demo](../../videos/use-cases.md#one-click-conversion-to-multicloud)

- :material-chat-question-outline:{ .lg .middle } __FAQ__

    ---

    Common questions and solutions related to multicloud instances, workloads, and policy configuration.

    [:arrow_forward: View FAQ](faq.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
[View the Multicloud Management User Guide (PDF)](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/kairship.pdf){ .md-button }
