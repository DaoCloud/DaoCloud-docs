---
hide:
  - toc
---

# d.run Token Factory

d.run Token Factory is an integrated platform built by DaoCloud for AI intelligent computing scenarios, providing end-to-end capabilities around large model inference, compute scheduling, and cluster operations. The platform adopts a dual-view architecture of **User** and **Admin**: the user view serves end users, providing large model service invocation, cost management, and intelligent application access capabilities; the admin view serves operations and management teams, providing unified management of model hosting, inference engines, infrastructure, and global operations.

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
  <div class="tf-arch-layer tf-arch-layer--model">
    <div class="tf-arch-layer-label">CNAI</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="clawos/intro/">
        <span class="tf-arch-card-title">ClawOS</span>
        <span class="tf-arch-card-tip">Multi-agent runtime and governance</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="dak/">
        <span class="tf-arch-card-title">AI Apps</span>
        <span class="tf-arch-card-tip">Intelligent Q&A and other application capabilities</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="hydra/">
        <span class="tf-arch-card-title">LLM Studio</span>
        <span class="tf-arch-card-tip">Model serving and O&M management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="inferx/">
        <span class="tf-arch-card-title">InferX Inference</span>
        <span class="tf-arch-card-tip">Inference acceleration and engine management</span>
      </a>
      <div class="tf-arch-card tf-arch-card--model">
        <span class="tf-arch-card-title">redhare Distributed Cache</span>
        <span class="tf-arch-card-tip">Distributed cache acceleration service</span>
      </div>
      <a class="tf-arch-card tf-arch-card--model" href="zestu/">
        <span class="tf-arch-card-title">Compute Cloud</span>
        <span class="tf-arch-card-tip">Heterogeneous compute management and scheduling</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">CN Infra</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="kpanda/intro/">
        <span class="tf-arch-card-title">Container Management</span>
        <span class="tf-arch-card-tip">Cluster and workload management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="kangaroo/intro/">
        <span class="tf-arch-card-title">Container Registry</span>
        <span class="tf-arch-card-tip">Image hosting and integration</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="topohub/intro/">
        <span class="tf-arch-card-title">Device Management</span>
        <span class="tf-arch-card-tip">Unified hardware device management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="network/intro/">
        <span class="tf-arch-card-title">Cloud Native Network</span>
        <span class="tf-arch-card-tip">Multi-CNI converged network</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="storage/">
        <span class="tf-arch-card-title">Cloud Native Storage</span>
        <span class="tf-arch-card-tip">Container storage and CSI</span>
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
        <span class="tf-arch-card-title">Cockpit</span>
        <span class="tf-arch-card-tip">Operations data visualization</span>
      </div>
      <a class="tf-arch-card tf-arch-card--ops" href="leopard/">
        <span class="tf-arch-card-title">Billing Center</span>
        <span class="tf-arch-card-tip">Billing and invoice analysis</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▼</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">OAM</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="insight/intro/">
        <span class="tf-arch-card-title">Observability</span>
        <span class="tf-arch-card-tip">Metrics, logs, and tracing</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="ghippo/intro/">
        <span class="tf-arch-card-title">Global Management</span>
        <span class="tf-arch-card-tip">User permissions and platform settings</span>
      </a>
    </div>
  </div>
</div>

As a high-efficiency AI Token production and management system built for intelligent computing centers, Token Factory helps traditional computing centers upgrade to an efficient, profitable Token production and operations model. The platform uniformly manages NVIDIA and domestic heterogeneous computing power, relying on intelligent scheduling and inference optimization to transform distributed GPU resources into low-cost, highly stable, tradable standardized token services. Through the Token Factory manager and unified operations system, it achieves global management of resources, production, costs, and supply-demand, providing capabilities to end users, administrators, operators, and O&M personnel, and driving the intelligent computing center's business positioning to upgrade from "providing compute power" to "producing and operating tokens."
