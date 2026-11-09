---
hide:
  - toc
---

# Container Management

Container management is a containerization management module for cloud native applications
built on Kubernetes. Based on a native multi-cluster architecture,
it decouples the underlying infrastructure to achieve unified management across multiple clouds and clusters.
This greatly simplifies the process of migrating enterprise applications to the cloud and reduces
operational and manpower costs. With container management, you can easily create Kubernetes clusters
and quickly build an enterprise-grade container cloud management platform.

![Container Management Logical Architecture](../images/kpanda_architect.svg)

## Key Capabilities

<div class="grid cards" markdown>

- :material-server:{ .lg .middle } __Cluster Management__

    ---

    Supports four cluster types — global service cluster, management cluster, worker cluster, and integrated cluster — covering creation, integration, upgrade, roles and status, and runtime selection.

    [:arrow_forward: Create a cluster](../user-guide/clusters/create-cluster.md)

- :fontawesome-brands-node:{ .lg .middle } __Nodes & Namespaces__

    ---

    Node scheduling, labels and annotations, taint management, scale-out/in, and availability checks; namespace isolation, dedicated nodes, and Pod security policies.

    [:arrow_forward: Node scheduling](../user-guide/nodes/schedule.md)

- :octicons-tasklist-16:{ .lg .middle } __Workloads & Autoscaling__

    ---

    Create Deployments, StatefulSets, DaemonSets, and Jobs/CronJobs, and scale workloads automatically with HPA and VPA policies.

    [:arrow_forward: Create a Deployment](../user-guide/workloads/create-deployment.md)

- :simple-helm:{ .lg .middle } __Helm Apps__

    ---

    Hundreds of Helm charts for one-click deployment, with app and repository management to bring business applications online quickly.

    [:arrow_forward: Browse Helm charts](../user-guide/helm/README.md)

- :material-dot-net:{ .lg .middle } __Networking & Storage__

    ---

    Manage traffic and routing with Services, Ingresses, and NetworkPolicies; native CSI support for dynamic provisioning, volume snapshots, and cloning.

    [:arrow_forward: Services](../user-guide/network/create-services.md)

- :material-security:{ .lg .middle } __Security & Inspection__

    ---

    Compliance, permission, and vulnerability scans for nodes and clusters; cluster inspection checks the overall health status automatically or on demand.

    [:arrow_forward: Create an inspection](../user-guide/inspect/config.md)

</div>

## Workflow

Using container management typically involves two stages: **platform preparation** and **running applications**. Administrators first create or integrate clusters and plan namespaces; business users then deploy workloads and expose services, with autoscaling and inspection keeping applications healthy over time.

```mermaid
flowchart LR
    A["① Create/integrate cluster<br/>Global · worker clusters"] --> B["② Create a namespace<br/>Isolation · dedicated nodes"]
    B --> C["③ Deploy workloads<br/>Deployment · Helm"]
    C --> D["④ Expose services & storage<br/>Service · Ingress · PVC"]
    D --> E["⑤ Autoscaling & inspection<br/>HPA · reports"]

    click A href "../user-guide/clusters/create-cluster/"
    click B href "../user-guide/namespaces/createns/"
    click C href "../user-guide/workloads/create-deployment/"
    click D href "../user-guide/network/create-services/"
    click E href "../user-guide/scale/create-hpa/"
```

| Step | Role | Description |
| ---- | ---- | ----------- |
| ① [Create/integrate a cluster](../user-guide/clusters/create-cluster.md) | Platform Administrator | Create global service, management, and worker clusters, or integrate existing Kubernetes clusters |
| ② [Create a namespace](../user-guide/namespaces/createns.md) | Platform Administrator | Define resource isolation boundaries, with dedicated nodes and Pod security policies |
| ③ [Deploy workloads](../user-guide/workloads/create-deployment.md) | Business User | Deploy Deployments, StatefulSets, and more from images or Helm charts |
| ④ [Expose services](../user-guide/network/create-services.md) and [mount storage](../user-guide/storage/pvc.md) | Business User | Create Services / Ingresses to expose applications, and mount persistent storage through PVCs |
| ⑤ [Autoscaling & inspection](../user-guide/scale/create-hpa.md) | Platform Administrator | Configure HPA/VPA for load fluctuations, and run periodic inspections for cluster health |

## Quick Start

<style>
.kpanda-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.kpanda-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.kpanda-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.kpanda-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.kpanda-path-step:last-child::after{display:none}
.kpanda-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.kpanda-path-title{font-weight:700;font-size:0.95rem}
.kpanda-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.kpanda-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.kpanda-path-step::after{display:none}}
</style>

<div class="kpanda-path">
  <a class="kpanda-path-step" style="--path-c:#2196f3" href="../user-guide/clusters/create-cluster/">
    <span class="kpanda-path-num">1</span>
    <span class="kpanda-path-title">Create a cluster</span>
    <span class="kpanda-path-desc">Create or integrate Kubernetes clusters</span>
    <span class="kpanda-path-go">Go →</span>
  </a>
  <a class="kpanda-path-step" style="--path-c:#00acc1" href="../user-guide/namespaces/createns/">
    <span class="kpanda-path-num">2</span>
    <span class="kpanda-path-title">Create a namespace</span>
    <span class="kpanda-path-desc">Isolation · dedicated nodes</span>
    <span class="kpanda-path-go">Go →</span>
  </a>
  <a class="kpanda-path-step" style="--path-c:#43a047" href="../user-guide/workloads/create-deployment/">
    <span class="kpanda-path-num">3</span>
    <span class="kpanda-path-title">Deploy workloads</span>
    <span class="kpanda-path-desc">Deployments · Helm charts</span>
    <span class="kpanda-path-go">Go →</span>
  </a>
  <a class="kpanda-path-step" style="--path-c:#fb8c00" href="../user-guide/network/create-services/">
    <span class="kpanda-path-num">4</span>
    <span class="kpanda-path-title">Expose services</span>
    <span class="kpanda-path-desc">Services · Ingresses · PVCs</span>
    <span class="kpanda-path-go">Go →</span>
  </a>
  <a class="kpanda-path-step" style="--path-c:#8e24aa" href="../user-guide/scale/create-hpa/">
    <span class="kpanda-path-num">5</span>
    <span class="kpanda-path-title">Autoscaling</span>
    <span class="kpanda-path-desc">HPA · VPA policies</span>
    <span class="kpanda-path-go">Go →</span>
  </a>
</div>

## More Resources

<div class="grid cards" markdown>

- :material-format-list-bulleted:{ .lg .middle } __Features__

    ---

    A complete list of container management features across clusters, nodes, workloads, networking and storage, security, and inspection.

    [:arrow_forward: View features](features.md)

- :material-map-outline:{ .lg .middle } __Scenarios__

    ---

    Best practices for multi-cluster management, application delivery, hybrid cloud, and more.

    [:arrow_forward: View scenarios](scenarios.md)

- :material-chat-question-outline:{ .lg .middle } __FAQ__

    ---

    Common questions and solutions about cluster creation, workload operation, and networking and storage.

    [:arrow_forward: View the FAQ](faq.md)

</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
[View User Manual (PDF)](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/kpanda.pdf){ .md-button }
