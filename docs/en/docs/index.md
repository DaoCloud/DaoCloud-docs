---
hide:
  - navigation
  - toc
---

# DaoCloud Docs Hub

<div class="tf-hero" markdown>

DaoCloud is an open-source pioneer in the global AI space, dedicated to accelerating enterprise intelligent transformation through cloud native technology.
This site provides documentation for three product lines, covering full-stack capabilities from infrastructure and compute scheduling to model inference and application building.

<div class="tf-hero-badges">
<a class="tf-hero-badge tf-hero-badge--tf" href="tf/">d.run Token Factory</a>
<a class="tf-hero-badge tf-hero-badge--drun" href="drun/">d.run AI OS</a>
<a class="tf-hero-badge tf-hero-badge--dce" href="dce/">DaoCloud Enterprise</a>
</div>

</div>

<style>
.tf-arch-card{min-width:calc(25% - 6px) !important}
.tf-arch{overflow:visible !important}
.tf-arch-card{overflow:visible !important}
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

=== ":material-factory: d.run Token Factory"

    This is a high-efficiency AI Token production and management system designed for intelligent computing centers, dedicated to upgrading traditional computing centers into efficient, profitable Token factories.
    The platform unifiedly manages NVIDIA and domestic heterogeneous computing power, transforming distributed GPU compute into low-cost, highly stable, and tradable standardized Token services through intelligent scheduling and inference optimization.
    Built on the Token Factory manager and unified operations system, the platform enables global management of resources, production, costs, and supply-demand, serving end users, administrators, operators, and O&M teams,
    driving intelligent computing centers to evolve from "providing compute" to "producing and operating Tokens".

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">CNAI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="tf/clawos/intro/">
            <span class="tf-arch-card-title">ClawOS</span>
            <span class="tf-arch-card-tip">Multi-agent runtime and governance</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/dak/">
            <span class="tf-arch-card-title">AI Apps</span>
            <span class="tf-arch-card-tip">Intelligent Q&A and application capabilities</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/hydra/">
            <span class="tf-arch-card-title">LLM Studio</span>
            <span class="tf-arch-card-tip">Model serving and O&M management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/inferx/">
            <span class="tf-arch-card-title">InferX Inference</span>
            <span class="tf-arch-card-tip">Inference acceleration and engine management</span>
          </a>
          <div class="tf-arch-card tf-arch-card--model">
            <span class="tf-arch-card-title">redhare Distributed Cache</span>
            <span class="tf-arch-card-tip">Distributed cache acceleration service</span>
          </div>
          <a class="tf-arch-card tf-arch-card--model" href="tf/zestu/">
            <span class="tf-arch-card-title">Compute Cloud</span>
            <span class="tf-arch-card-tip">Heterogeneous compute management and scheduling</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">CN Infra</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="tf/kpanda/intro/">
            <span class="tf-arch-card-title">Container Management</span>
            <span class="tf-arch-card-tip">Cluster and workload management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="tf/kangaroo/intro/">
            <span class="tf-arch-card-title">Container Registry</span>
            <span class="tf-arch-card-tip">Image hosting and integration</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="tf/topohub/intro/">
            <span class="tf-arch-card-title">Device Management</span>
            <span class="tf-arch-card-tip">Unified hardware device management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="tf/network/intro/">
            <span class="tf-arch-card-title">Cloud Native Network</span>
            <span class="tf-arch-card-tip">Multi-CNI fused network</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="tf/storage/">
            <span class="tf-arch-card-title">Cloud Native Storage</span>
            <span class="tf-arch-card-tip">Containerized storage and CSI</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">Ops</div>
        <div class="tf-arch-cards">
          <div class="tf-arch-card tf-arch-card--ops">
            <span class="tf-arch-card-title">Copilot</span>
            <span class="tf-arch-card-tip">Intelligent O&M assistant</span>
          </div>
          <div class="tf-arch-card tf-arch-card--ops">
            <span class="tf-arch-card-title">Dashboard</span>
            <span class="tf-arch-card-tip">Operations data visualization</span>
          </div>
          <a class="tf-arch-card tf-arch-card--ops" href="tf/leopard/">
            <span class="tf-arch-card-title">Billing Center</span>
            <span class="tf-arch-card-tip">Billing and invoice analysis</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">OAM</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="tf/insight/intro/">
            <span class="tf-arch-card-title">Insight</span>
            <span class="tf-arch-card-tip">Metrics, logs, and tracing</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="tf/ghippo/intro/">
            <span class="tf-arch-card-title">Global Management</span>
            <span class="tf-arch-card-tip">User permissions and platform settings</span>
          </a>
        </div>
      </div>
    </div>

=== ":material-robot-happy: d.run AI OS"

    Leveraging top-three globally ranked Kubernetes scheduling technology and core contributions to mainstream open-source inference engines like vLLM, d.run unifiedly manages diverse heterogeneous computing power,
    achieving granular scheduling, full-stack inference optimization, and end-to-end Token governance. With compute utilization exceeding 80%, it efficiently transforms compute into manageable, controllable Token-based AI productivity.
    The platform aggregates global mainstream large model ecosystems, equipped with a visual operations dashboard and d.run Copilot intelligent assistant, delivering stable and efficient AI services across all enterprise departments,
    comprehensively supporting long-term business intelligent transformation.

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">CNAI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="drun/clawos/workspace/">
            <span class="tf-arch-card-title">ClawOS</span>
            <span class="tf-arch-card-tip">Multi-agent runtime and governance</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/hydra/">
            <span class="tf-arch-card-title">LLM Studio</span>
            <span class="tf-arch-card-tip">Model serving and O&M management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/baize/intro/">
            <span class="tf-arch-card-title">AI Lab</span>
            <span class="tf-arch-card-tip">Cloud-native integrated training and inference</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/inferx/">
            <span class="tf-arch-card-title">InferX Inference Suite</span>
            <span class="tf-arch-card-tip">Inference acceleration and engine management</span>
          </a>
          <div class="tf-arch-card tf-arch-card--model">
            <span class="tf-arch-card-title">redhare Distributed Cache</span>
            <span class="tf-arch-card-tip">Distributed cache acceleration service</span>
          </div>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">CN Infra</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="drun/kpanda/intro/">
            <span class="tf-arch-card-title">Container Management</span>
            <span class="tf-arch-card-tip">Cluster and workload management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/topohub/intro/">
            <span class="tf-arch-card-title">Device Management</span>
            <span class="tf-arch-card-tip">Unified hardware device management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/kangaroo/intro/">
            <span class="tf-arch-card-title">Container Registry</span>
            <span class="tf-arch-card-tip">Image hosting and integration</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/network/intro/">
            <span class="tf-arch-card-title">Cloud Native Network</span>
            <span class="tf-arch-card-tip">Multi-CNI fused network</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/storage/">
            <span class="tf-arch-card-title">Cloud Native Storage</span>
            <span class="tf-arch-card-tip">Containerized storage and CSI</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">Ops</div>
        <div class="tf-arch-cards">
          <div class="tf-arch-card tf-arch-card--ops">
            <span class="tf-arch-card-title">Copilot</span>
            <span class="tf-arch-card-tip">Intelligent O&M assistant</span>
          </div>
          <div class="tf-arch-card tf-arch-card--ops">
            <span class="tf-arch-card-title">Operations Dashboard</span>
            <span class="tf-arch-card-tip">Operations data visualization</span>
          </div>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">OAM</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="drun/insight/intro/">
            <span class="tf-arch-card-title">Insight</span>
            <span class="tf-arch-card-tip">Metrics, logs, and tracing</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="drun/ghippo/intro/">
            <span class="tf-arch-card-title">Global Management</span>
            <span class="tf-arch-card-tip">User permissions and platform settings</span>
          </a>
        </div>
      </div>
    </div>

=== ":octicons-stack-16: DaoCloud Enterprise"

    DaoCloud Enterprise (DCE) is a high-performance, scalable cloud native operating system,
    and a [CNCF-certified Kubernetes – AI Platform](./dce/kcsp.md).
    It delivers a consistent, stable experience across any infrastructure and environment, supporting heterogeneous clouds, edge clouds, and multicloud orchestration.

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">CN Infra</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="middleware/">
            <span class="tf-arch-card-title">Middleware</span>
            <span class="tf-arch-card-tip">Databases and message queues</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kairship/intro/">
            <span class="tf-arch-card-title">Multicloud Orchestration</span>
            <span class="tf-arch-card-tip">Multicloud and hybrid cloud orchestration</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kangaroo/intro/">
            <span class="tf-arch-card-title">Container Registry</span>
            <span class="tf-arch-card-tip">Image hosting and integration</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="mspider/intro/">
            <span class="tf-arch-card-title">Service Mesh</span>
            <span class="tf-arch-card-tip">Non-intrusive service governance</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="skoala/intro/">
            <span class="tf-arch-card-title">Microservice Engine</span>
            <span class="tf-arch-card-tip">Microservice governance and gateway</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="amamba/intro/">
            <span class="tf-arch-card-title">Workbench</span>
            <span class="tf-arch-card-tip">CI/CD and application delivery</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kpanda/intro/">
            <span class="tf-arch-card-title">Container Management</span>
            <span class="tf-arch-card-tip">Cluster and workload management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="virtnest/intro/">
            <span class="tf-arch-card-title">Virtual Machine</span>
            <span class="tf-arch-card-tip">KubeVirt virtual machine management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="topohub/intro/">
            <span class="tf-arch-card-title">Device Management</span>
            <span class="tf-arch-card-tip">Unified hardware device management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kant/intro/">
            <span class="tf-arch-card-title">Cloud Edge Collaboration</span>
            <span class="tf-arch-card-tip">Edge node management and collaboration</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="network/intro/">
            <span class="tf-arch-card-title">Cloud Native Network</span>
            <span class="tf-arch-card-tip">Multi-CNI fused network</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="storage/">
            <span class="tf-arch-card-title">Cloud Native Storage</span>
            <span class="tf-arch-card-tip">Containerized storage and CSI</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">OAM</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="insight/intro/">
            <span class="tf-arch-card-title">Insight</span>
            <span class="tf-arch-card-tip">Metrics, logs, and tracing</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="ghippo/intro/">
            <span class="tf-arch-card-title">Global Management</span>
            <span class="tf-arch-card-tip">User permissions and platform settings</span>
          </a>
        </div>
      </div>
    </div>

<div class="tf-cta" markdown>

[Apply for DCE Community Free Trial](./dce/license0.md){ .md-button .md-button--primary }
[Learn about d.run](drun/index.md){ .md-button .md-button--primary }
[Token Factory Overview](tf/index.md){ .md-button .md-button--primary }

</div>
