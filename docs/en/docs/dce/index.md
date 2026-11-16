---
hide:
  - toc
---

# DaoCloud Enterprise Docs

DaoCloud Enterprise (DCE) is built on Kubernetes as its foundation, providing highly scalable, powerful, and flexible production-grade features that enable enterprises to easily build and manage distributed applications.
With DCE's cloud native DNA, enterprises can fully leverage the advantages of both cloud and on-premises environments, achieve optimal resource utilization, improve the reliability and elasticity of IT systems, and greatly accelerate application delivery.

<style>
.tf-arch-card{min-width:calc(25% - 6px) !important}
.tf-arch{overflow:visible !important}
.tf-arch-card{overflow:visible !important}
.tf-arch-card::after{display:none !important}
.tf-arch-layer:first-child{border-radius:14px 14px 0 0 !important}
.tf-arch-layer:last-child{border-radius:0 0 14px 14px !important}
.tf-arch-card-tip{
  opacity:0;
  position:absolute;
  bottom:calc(100% + 8px);
  left:50%;
  transform:translateX(-50%);
  background:rgba(0,0,0,0.85);
  color:#fff;
  padding:0.35rem 0.65rem;
  border-radius:6px;
  font-size:0.72rem;
  font-weight:500;
  white-space:nowrap;
  z-index:100;
  pointer-events:none;
  box-shadow:0 4px 12px rgba(0,0,0,0.2);
  transition:opacity 0.2s ease
}
.tf-arch-card-tip::after{
  content:"";
  position:absolute;
  top:100%;
  left:50%;
  transform:translateX(-50%);
  border:5px solid transparent;
  border-top-color:rgba(0,0,0,0.85)
}
.tf-arch-card:hover .tf-arch-card-tip{
  opacity:1
}
</style>

<div class="tf-arch tf-arch--compact">
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">Cloud Native Infra</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="../middleware/">
        <span class="tf-arch-card-title">Middleware</span>
        <span class="tf-arch-card-tip">Databases and message queues</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kairship/intro/">
        <span class="tf-arch-card-title">Multicloud Management</span>
        <span class="tf-arch-card-tip">Multicloud and hybrid cloud orchestration</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kangaroo/intro/">
        <span class="tf-arch-card-title">Container Registry</span>
        <span class="tf-arch-card-tip">Image hosting and integration</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../mspider/intro/">
        <span class="tf-arch-card-title">Service Mesh</span>
        <span class="tf-arch-card-tip">Non-intrusive service governance</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../skoala/intro/">
        <span class="tf-arch-card-title">Microservice Engine</span>
        <span class="tf-arch-card-tip">Microservice governance and gateway</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../amamba/intro/">
        <span class="tf-arch-card-title">Workbench</span>
        <span class="tf-arch-card-tip">CI/CD and application delivery</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kpanda/intro/">
        <span class="tf-arch-card-title">Container Management</span>
        <span class="tf-arch-card-tip">Cluster and workload management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../virtnest/intro/">
        <span class="tf-arch-card-title">Virtual Machine</span>
        <span class="tf-arch-card-tip">KubeVirt virtual machine management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../topohub/intro/">
        <span class="tf-arch-card-title">Device Management</span>
        <span class="tf-arch-card-tip">Unified hardware device management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kant/intro/">
        <span class="tf-arch-card-title">Cloud Edge Collaboration</span>
        <span class="tf-arch-card-tip">Edge node management and collaboration</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../network/intro/">
        <span class="tf-arch-card-title">Cloud Native Network</span>
        <span class="tf-arch-card-tip">Multi-CNI fused network</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../storage/">
        <span class="tf-arch-card-title">Cloud Native Storage</span>
        <span class="tf-arch-card-tip">Containerized storage and CSI</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">OAM</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="../insight/intro/">
        <span class="tf-arch-card-title">Observability</span>
        <span class="tf-arch-card-tip">Metrics, logs, and tracing</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="../ghippo/intro/">
        <span class="tf-arch-card-title">Global Management</span>
        <span class="tf-arch-card-tip">User permissions and platform settings</span>
      </a>
    </div>
  </div>
</div>

## Product Architecture

![DCE 5.0 Product Architecture](images/architecture.svg)

## Installation and Tutorials

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up:{ .lg .middle } __Installation__

    ---

    DCE supports both [offline](../install/community/k8s/offline.md) and [online](../install/community/k8s/online.md) installation methods,
    and can be installed on [various Linux distributions](../install/os-install/uos-v20-install-dce5.0.md).

    - [Install Dependencies](../install/install-tools.md)
    - [Install Community Package](../install/community/resources.md)
    - [Install Enterprise Package](../install/commercial/deploy-requirements.md)
    - [Install on Different Linux Distributions](../install/os-install/uos-v20-install-dce5.0.md)
    - [Install on Different K8s Versions](../install/k8s-install/ocp-install-dce5.0.md)

- :material-microsoft-azure-devops:{ .lg .middle } __Video Tutorials__

    ---

    We have created many video tutorials for different modules and scenarios of DCE.

    - [Scenario-based Videos](../videos/use-cases.md)
    - [Workbench Videos](../videos/amamba.md)
    - [Container Management Videos](../videos/kpanda.md)
    - [Microservices Videos](../videos/skoala.md)
    - [Middleware Videos](../videos/mcamel.md)
    - [Global Management Videos](../videos/ghippo.md)

</div>

## Learning Path

<style>
.dce-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.dce-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.dce-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.dce-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.dce-path-step:last-child::after{display:none}
.dce-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.dce-path-title{font-weight:700;font-size:0.95rem}
.dce-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.dce-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.dce-path-step::after{display:none}}
</style>

<div class="dce-path">
  <a class="dce-path-step" style="--path-c:#2196f3" href="../install/">
    <span class="dce-path-num">1</span>
    <span class="dce-path-title">Deploy the Platform</span>
    <span class="dce-path-desc">Install DCE 5.0 online or offline</span>
    <span class="dce-path-go">Go →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#00acc1" href="../kpanda/intro/">
    <span class="dce-path-num">2</span>
    <span class="dce-path-title">Manage Clusters</span>
    <span class="dce-path-desc">Integrate clusters and orchestrate containers</span>
    <span class="dce-path-go">Go →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#43a047" href="../amamba/intro/">
    <span class="dce-path-num">3</span>
    <span class="dce-path-title">Deliver Apps</span>
    <span class="dce-path-desc">CI pipelines and GitOps delivery</span>
    <span class="dce-path-go">Go →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#fb8c00" href="../insight/intro/">
    <span class="dce-path-num">4</span>
    <span class="dce-path-title">Observe the System</span>
    <span class="dce-path-desc">Unified metrics, logs, and traces</span>
    <span class="dce-path-go">Go →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#8e24aa" href="../ghippo/intro/">
    <span class="dce-path-num">5</span>
    <span class="dce-path-title">Govern the Platform</span>
    <span class="dce-path-desc">Users, permissions, and global policies</span>
    <span class="dce-path-go">Go →</span>
  </a>
</div>

[Apply for Community Free Trial](./license0.md){ .md-button }
[Best Practices](./bphome.md){ .md-button }
[FAQs](./faq.md){ .md-button }
[Read the DaoCloud Enterprise Brochure](https://harbor-test2.cn-sh2.ufileos.com/docs/download/dce.pdf){ .md-button }
