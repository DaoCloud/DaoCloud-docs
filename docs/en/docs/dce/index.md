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
        <span class="tf-arch-card-title">Multicloud Orchestration</span>
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
  <div class="tf-arch-arrow">▼</div>
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

## Download and Ecosystem

<div class="grid cards" markdown>

- :material-download:{ .lg .middle } __Download Center__

    ---

    The Download Center contains offline installation packages for the DCE Community Package, Enterprise Package, and sub-modules.

    - [Download Community Package](../download/free/dce5-installer-history.md)
    - [Download Enterprise Package](../download/business/dce5-installer-history.md)
    - [Download Sub-Modules](../download/index.md#_3)

- :simple-opensourceinitiative:{ .lg .middle } __DaoCloud Open Source Ecosystem__

    ---

    DaoCloud adheres to an open source enterprise culture, with multiple open source technologies included in the CNCF Sandbox.

    - [Clusterpedia: Multi-Cluster Encyclopedia](../community/clusterpedia.md)
    - [HwameiStor: Local Storage](../community/hwameistor.md)
    - [Merbridge: Service Mesh Acceleration](../community/merbridge.md)

</div>

*[Clusterpedia]: A multi-cluster resource query plugin built into DCE, donated to CNCF and accepted into Sandbox
*[HwameiStor]: A local highly available storage solution built into DCE, donated to CNCF and accepted into Sandbox
*[Merbridge]: A mesh acceleration plugin built into DCE based on eBPF, donated to CNCF and accepted into Sandbox

!!! success

    ```yaml
    What leads to a company's success?
      It's the shared dream, a unified vision,
        The joy of open source, collaborative decision.
          Thriving on the thrill, working day and night,
            Building magical things that shine so bright.

    Together, let us now unite,
      Honoring efforts past, present, future with delight.
    ```

[Apply for Community Free Trial](./license0.md){ .md-button .md-button--primary }
[Best Practices](./bphome.md){ .md-button .md-button--primary }
[FAQs](./faq.md){ .md-button .md-button--primary }
