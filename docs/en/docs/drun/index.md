---
hide:
  - toc
---

# d.run AI Operating System

d.run leverages the world's top-three Kubernetes scheduling technology and core contributions to mainstream open-source inference engines such as vLLM to uniformly manage diverse heterogeneous computing power. It enables granular scheduling, full-stack inference optimization, and end-to-end token governance, achieving a compute utilization rate of over 80% and efficiently transforming computing power into manageable, controllable token-based AI productivity. The platform aggregates the global mainstream large model ecosystem, equipped with a visual operations cockpit and the d.run Copilot intelligent assistant, delivering stable and efficient AI services to all departments of the enterprise and comprehensively supporting long-term business intelligence upgrades.

[View/Download the d.run AI OS brochure](https://harbor-test2.cn-sh2.ufileos.com/docs/download/drun.pdf){ .md-button }

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
      <a class="tf-arch-card tf-arch-card--model" href="hydra/">
        <span class="tf-arch-card-title">LLM Studio</span>
        <span class="tf-arch-card-tip">Model serving and O&M management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="baize/intro/">
        <span class="tf-arch-card-title">AI Lab</span>
        <span class="tf-arch-card-tip">Cloud Native integrated training and inference</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="inferx/">
        <span class="tf-arch-card-title">InferX Suite</span>
        <span class="tf-arch-card-tip">Inference acceleration and engine management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="clawos/intro/">
        <span class="tf-arch-card-title">ClawOS</span>
        <span class="tf-arch-card-tip">Multi-agent runtime and governance</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
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
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">Ops</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="copilot/">
        <span class="tf-arch-card-title">Copilot</span>
        <span class="tf-arch-card-tip">Intelligent O&M assistant</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="crane/intro/">
        <span class="tf-arch-card-title">Cockpit</span>
        <span class="tf-arch-card-tip">Operations data visualization</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
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

As an AI operating system designed for enterprises, d.run integrates compute scheduling, large model inference, and operations governance into a unified platform. The platform uniformly manages NVIDIA and domestic heterogeneous computing power, relying on granular scheduling and full-stack inference optimization to transform distributed GPU resources into low-cost, highly stable token services. It features a visual operations cockpit that presents real-time data across the entire chain of compute consumption, model invocations, and token production. The built-in d.run Copilot intelligent assistant lowers the barrier for all enterprise departments to adopt AI, driving long-term business intelligence upgrades.

![The d.run AI Operating System at a glance](images/drun-modules.svg)

## Learning Path

<style>
.drun-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.drun-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.drun-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.drun-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.drun-path-step:last-child::after{display:none}
.drun-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.drun-path-title{font-weight:700;font-size:0.95rem}
.drun-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.drun-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.drun-path-step::after{display:none}}
</style>

<div class="drun-path">
  <a class="drun-path-step" style="--path-c:#2196f3" href="install/">
    <span class="drun-path-num">1</span>
    <span class="drun-path-title">Deploy and Install</span>
    <span class="drun-path-desc">Install d.run AI Operating System offline</span>
    <span class="drun-path-go">Go →</span>
  </a>
  <a class="drun-path-step" style="--path-c:#00acc1" href="kpanda/intro/">
    <span class="drun-path-num">2</span>
    <span class="drun-path-title">Onboard Compute</span>
    <span class="drun-path-desc">Attach clusters and manage heterogeneous GPU resources</span>
    <span class="drun-path-go">Go →</span>
  </a>
  <a class="drun-path-step" style="--path-c:#43a047" href="hydra/">
    <span class="drun-path-num">3</span>
    <span class="drun-path-title">Deploy Models</span>
    <span class="drun-path-desc">Pick models from the catalog and deploy inference services in one click</span>
    <span class="drun-path-go">Go →</span>
  </a>
  <a class="drun-path-step" style="--path-c:#fb8c00" href="clawos/intro/">
    <span class="drun-path-num">4</span>
    <span class="drun-path-title">Build Agents</span>
    <span class="drun-path-desc">Orchestrate multi-agent workflows for business scenarios</span>
    <span class="drun-path-go">Go →</span>
  </a>
  <a class="drun-path-step" style="--path-c:#8e24aa" href="crane/intro/">
    <span class="drun-path-num">5</span>
    <span class="drun-path-title">Operational Insight</span>
    <span class="drun-path-desc">Monitor end-to-end token operations in the Cockpit</span>
    <span class="drun-path-go">Go →</span>
  </a>
</div>

[Download d.run AI OS Package](https://docs.daocloud.io/download/drun/){ .md-button }
[View the d.run AI OS brochure](https://harbor-test2.cn-sh2.ufileos.com/docs/download/drun.pdf){ .md-button }
[Install d.run AI Operating System](install/index.md){ .md-button }
