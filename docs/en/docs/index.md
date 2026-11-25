---
hide:
  - navigation
  - toc
---

# DaoCloud Docs Hub

<div class="tf-hero" markdown>

DaoCloud is a global open-source pioneer in AI, accelerating enterprise AI transformation with cloud native technology. Explore the AI full stack here — from compute scheduling, model training, and inference to building AI apps and governing multi-agent systems.

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
/* Homepage: three-product relationship diagram */
.tf-relation{box-sizing:border-box;margin:1.5rem 0 2rem;background:#F4F7FB;color:#0F1D33;font-family:'PingFang SC','Hiragino Sans GB','Microsoft YaHei',system-ui,sans-serif;padding:20px 18px;line-height:1.65;text-align:center;border-radius:12px}
.tf-relation-kicker{font-size:13px;letter-spacing:2px;color:#5A6A85;font-weight:600;margin-bottom:12px}
.tf-relation-box{border-radius:12px;padding:14px 16px;border:1.5px solid transparent}
.tf-relation-box--tf{background:#FDF0E1;border-color:#E8720C}
.tf-relation-box--drun{background:#E3F6F5;border-color:#0E9F9F}
.tf-relation-box--dce{background:#EAF1FE;border-color:#1B66F5}
.tf-relation-box-title{font-size:17px;font-weight:800}
.tf-relation-box-sub{font-size:13.5px;color:#5A6A85;margin-top:4px}
.tf-relation-box-detail{font-size:12.5px;color:#0F1D33;margin-top:6px}
.tf-relation-arrow{text-align:center;color:#8A98B0;font-size:17px;line-height:1.1;padding:3px 0}
.tf-relation-foot{font-size:13px;color:#8A98B0;margin-top:12px}
.tf-relation-box-title a.tf-relation-box-link{color:inherit;text-decoration:none;cursor:pointer}
.tf-relation-box-title a.tf-relation-box-link:hover{text-decoration:underline;text-underline-offset:3px}
/* Dark mode: dark surfaces + saturated brand borders + light text */
[data-md-color-scheme="slate"] .tf-relation{background:rgba(255,255,255,0.05);color:#e6eaf2}
[data-md-color-scheme="slate"] .tf-relation-kicker{color:#94a3b8}
[data-md-color-scheme="slate"] .tf-relation-box--tf{background:#3a2a17;border-color:#ff9800}
[data-md-color-scheme="slate"] .tf-relation-box--drun{background:#14351f;border-color:#00c853}
[data-md-color-scheme="slate"] .tf-relation-box--dce{background:#182742;border-color:#42a5f5}
[data-md-color-scheme="slate"] .tf-relation-box-title{color:#ffffff}
[data-md-color-scheme="slate"] .tf-relation-box-sub{color:#c3cede}
[data-md-color-scheme="slate"] .tf-relation-box-detail{color:#dae3f0}
[data-md-color-scheme="slate"] .tf-relation-arrow{color:#7d8ba3}
[data-md-color-scheme="slate"] .tf-relation-foot{color:#94a3b8}
/* 首页产品跑马灯 */
.md-typeset .doc-marquee{display:grid;gap:.7rem;margin:2rem 0 1.2rem;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent);mask-image:linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent)}
.md-typeset .doc-marquee__track{display:flex;width:max-content;animation:doc-marquee-move 60s linear infinite}
.md-typeset .doc-marquee__track--rev{animation-direction:reverse}
.md-typeset .doc-marquee:hover .doc-marquee__track{animation-play-state:paused}
.md-typeset .doc-marquee__group{--m-accent:#1B66F5;--m-glow:rgba(27,102,245,.16);--m-bg:#EAF1FE;--m-border:#B9CEF7;--m-hover:#D8E5FC;display:flex;gap:.7rem;padding-right:.7rem}
.md-typeset .doc-marquee__group--ai{--m-accent:#0E9F9F;--m-glow:rgba(14,159,159,.16);--m-bg:#E3F6F5;--m-border:#A8DBD9;--m-hover:#D3EFEE}
.md-typeset .doc-marquee__chip{display:inline-flex;align-items:center;gap:.5rem;padding:.36rem .9rem;border-radius:999px;font-size:.78rem;font-weight:500;line-height:1.4;white-space:nowrap;background:var(--m-bg);border:1px solid var(--m-border);color:#0F1D33 !important;text-decoration:none !important;transition:transform .2s ease,border-color .2s ease,background .2s ease}
.md-typeset .doc-marquee__chip:hover{transform:translateY(-2px);border-color:var(--m-accent);background:var(--m-hover);color:#0F1D33 !important}
.md-typeset .doc-marquee__dot{flex:none;width:7px;height:7px;border-radius:50%;background:var(--m-accent);box-shadow:0 0 0 3px var(--m-glow)}
@keyframes doc-marquee-move{from{transform:translateX(0)}to{transform:translateX(-50%)}}
[data-md-color-scheme="slate"] .md-typeset .doc-marquee__group{--m-glow:rgba(27,102,245,.2);--m-bg:rgba(27,102,245,.1);--m-border:rgba(27,102,245,.35);--m-hover:rgba(27,102,245,.22)}
[data-md-color-scheme="slate"] .md-typeset .doc-marquee__group--ai{--m-glow:rgba(14,159,159,.2);--m-bg:rgba(14,159,159,.1);--m-border:rgba(14,159,159,.35);--m-hover:rgba(14,159,159,.24)}
[data-md-color-scheme="slate"] .md-typeset .doc-marquee__chip{color:#d5dce8 !important}
@media (prefers-reduced-motion: reduce){.md-typeset .doc-marquee{-webkit-mask-image:none;mask-image:none}.md-typeset .doc-marquee__track{animation:none;width:auto;flex-wrap:wrap}.md-typeset .doc-marquee__group[aria-hidden="true"]{display:none}}

/* tf-hero shimmer border */
@property --tf-hero-angle{syntax:"<angle>";inherits:false;initial-value:0deg}
.md-typeset .tf-hero{position:relative}
.md-typeset .tf-hero::before{content:"";position:absolute;inset:-1px;border-radius:inherit;padding:1.5px;background:conic-gradient(from var(--tf-hero-angle),rgba(33,150,243,0) 0deg,#2196f3 30deg,#0e9f9f 55deg,rgba(33,150,243,0) 95deg,rgba(33,150,243,0) 175deg,#7c5cff 205deg,rgba(33,150,243,0) 250deg,rgba(33,150,243,0) 360deg);-webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);mask-composite:exclude;pointer-events:none;animation:tf-hero-spin 6s linear infinite}
@keyframes tf-hero-spin{to{--tf-hero-angle:360deg}}
@media (prefers-reduced-motion: reduce){.md-typeset .tf-hero::before{animation:none}}

/* 客户成功故事卡片 */
.md-typeset .story-marquee{display:grid;margin:1.2rem 0 2rem;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}
.md-typeset .story-track{display:flex;width:max-content;animation:story-move 70s linear infinite}
.md-typeset .story-marquee:hover .story-track{animation-play-state:paused}
.md-typeset .story-group{display:flex;gap:1rem;padding-right:1rem;align-items:stretch}
.md-typeset .story-card{width:330px;flex:none;display:flex;flex-direction:column;border-radius:12px;overflow:hidden;border:1px solid var(--md-default-fg-color--lightest);background:var(--md-default-bg-color);transition:transform .2s ease,border-color .2s ease}
.md-typeset .story-card:hover{transform:translateY(-3px);border-color:var(--s1)}
.md-typeset .story-card-top{display:flex;align-items:center;justify-content:space-between;gap:.5rem;height:62px;padding:0 .9rem;background:linear-gradient(120deg,var(--s1),var(--s2))}
.md-typeset .story-card-prod{font-size:.78rem;font-weight:600;color:rgba(255,255,255,.95);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-decoration:none}
.md-typeset .story-card-prod:hover{color:#fff;text-decoration:underline;text-underline-offset:3px}
.md-typeset .story-card-ind{font-size:.62rem;color:rgba(255,255,255,.92);background:rgba(255,255,255,.18);padding:.14rem .55rem;border-radius:999px;white-space:nowrap;flex:none}
.md-typeset .story-card-body{display:flex;flex-direction:column;flex:1;padding:.7rem .9rem .85rem}
.md-typeset .story-card-name{font-weight:700;font-size:.95rem;margin:0}
.md-typeset .story-card-desc{font-size:.75rem;line-height:1.55;color:var(--md-default-fg-color--light);margin:.3rem 0 .7rem}
.md-typeset .story-card-metrics{display:flex;gap:1rem;margin-top:auto;flex-wrap:wrap}
.md-typeset .story-card-metrics span{font-size:.62rem;color:var(--md-default-fg-color--light)}
.md-typeset .story-card-metrics b{display:block;font-size:1rem;font-weight:700;color:var(--s1)}
@keyframes story-move{from{transform:translateX(0)}to{transform:translateX(-50%)}}
[data-md-color-scheme="slate"] .md-typeset .story-card{border-color:rgba(148,163,184,.18);background:rgba(148,163,184,.06)}
[data-md-color-scheme="slate"] .md-typeset .story-card-metrics b{color:var(--s2)}
@media (prefers-reduced-motion: reduce){.md-typeset .story-marquee{overflow-x:auto;-webkit-mask-image:none;mask-image:none}.md-typeset .story-track{animation:none;width:auto}.md-typeset .story-group[aria-hidden="true"]{display:none}}
</style>

=== ":material-factory: d.run Token Factory"

    This is a high-efficiency AI Token production and management system designed for AI centers, dedicated to upgrading traditional computing centers into efficient, profitable Token factories.
    The platform unifiedly manages NVIDIA and domestic heterogeneous computing power, transforming distributed GPU compute into low-cost, highly stable, and tradable standardized Token services through intelligent scheduling and inference optimization.
    Built on the Token Factory manager and unified operations system, the platform enables global management of resources, production, costs, and supply-demand, serving end users, administrators, operators, and O&M teams,
    driving AI centers to evolve from "providing compute" to "producing and operating Tokens".

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">CNAI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="tf/hydra/intro/">
            <span class="tf-arch-card-title">LLM Studio</span>
            <span class="tf-arch-card-tip">Model serving and O&M management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/dak/">
            <span class="tf-arch-card-title">AI Apps</span>
            <span class="tf-arch-card-tip">Intelligent Q&A and application capabilities</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/inferx/">
            <span class="tf-arch-card-title">Turbo Inference</span>
            <span class="tf-arch-card-tip">Inference acceleration and engine management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/zestu/">
            <span class="tf-arch-card-title">Compute Cloud</span>
            <span class="tf-arch-card-tip">Heterogeneous compute management and scheduling</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
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
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">Ops</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="tf/copilot/">
            <span class="tf-arch-card-title">Copilot</span>
            <span class="tf-arch-card-tip">Intelligent O&M assistant</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="tf/crane/intro/">
            <span class="tf-arch-card-title">Cockpit</span>
            <span class="tf-arch-card-tip">Operations data visualization</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="tf/leopard/">
            <span class="tf-arch-card-title">Billing Center</span>
            <span class="tf-arch-card-tip">Billing and invoice analysis</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
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
    The platform aggregates global mainstream large model ecosystems, equipped with a visual cockpit and d.run Copilot intelligent assistant, delivering stable and efficient AI services across all enterprise departments,
    comprehensively supporting long-term business intelligent transformation.

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">CNAI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="drun/hydra/intro/">
            <span class="tf-arch-card-title">LLM Studio</span>
            <span class="tf-arch-card-tip">Model serving and O&M management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/baize/intro/">
            <span class="tf-arch-card-title">AI Lab</span>
            <span class="tf-arch-card-tip">Cloud-native integrated training and inference</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/inferx/">
            <span class="tf-arch-card-title">Turbo Inference</span>
            <span class="tf-arch-card-tip">Inference acceleration and engine management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/clawos/intro/">
            <span class="tf-arch-card-title">ClawOS</span>
            <span class="tf-arch-card-tip">Multi-agent runtime and governance</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">CN Infra</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="drun/kpanda/intro/">
            <span class="tf-arch-card-title">Container Management</span>
            <span class="tf-arch-card-tip">Cluster and workload management</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/kangaroo/intro/">
            <span class="tf-arch-card-title">Container Registry</span>
            <span class="tf-arch-card-tip">Image hosting and integration</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/topohub/intro/">
            <span class="tf-arch-card-title">Device Management</span>
            <span class="tf-arch-card-tip">Unified hardware device management</span>
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
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">Ops</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="drun/copilot/">
            <span class="tf-arch-card-title">Copilot</span>
            <span class="tf-arch-card-tip">Intelligent O&M assistant</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="drun/crane/intro/">
            <span class="tf-arch-card-title">Cockpit</span>
            <span class="tf-arch-card-tip">Operations data visualization</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
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
        <div class="tf-arch-layer-label">Out-of-box Function Modules</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="middleware/">
            <span class="tf-arch-card-title">Middleware</span>
            <span class="tf-arch-card-tip">Databases and message queues</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kairship/intro/">
            <span class="tf-arch-card-title">Multicloud Manageent</span>
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


## Customer Success Stories

<div class="story-marquee" aria-label="Customer success stories">
  <div class="story-track">
    <div class="story-group">
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token Factory</a><span class="story-card-ind">AI Center</span></div>
        <div class="story-card-body"><p class="story-card-name">Rundao Xingsuan</p><p class="story-card-desc">Guangxi's first Token-metered AI computing platform and the cornerstone for ASEAN cross-border compute expansion</p><div class="story-card-metrics"><span><b>1000P</b>initial compute scale</span><span><b>3000-5000P</b>planned compute scale</span></div></div>
      </div>
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token Factory</a><span class="story-card-ind">AI Center</span></div>
        <div class="story-card-body"><p class="story-card-name">Xiamen Computing Alliance</p><p class="story-card-desc">City-level compute scheduling across entities, architectures, and data centers, with 60+ AI scenarios in 12 industries</p><div class="story-card-metrics"><span><b>~2000P</b>compute under unified scheduling</span><span><b>7x</b>Token output efficiency</span></div></div>
      </div>
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token Factory</a><span class="story-card-ind">AI Center</span></div>
        <div class="story-card-body"><p class="story-card-name">PIXEL</p><p class="story-card-desc">Japanese listed company focused on data center and system innovation, taking a smart computing center from build to operations and launching Token services fast</p><div class="story-card-metrics"><span><b>End-to-end</b>build to operations</span><span><b>Fast go-live</b>Token services</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI OS</a><span class="story-card-ind">Manufacturing</span></div>
        <div class="story-card-body"><p class="story-card-name">OMRON</p><p class="story-card-desc">Global automation and electronics leader with an enterprise AI knowledge base for manufacturing and administration</p><div class="story-card-metrics"><span><b>65%</b>curation time saved</span><span><b>60%</b>support efficiency</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI OS</a><span class="story-card-ind">Manufacturing</span></div>
        <div class="story-card-body"><p class="story-card-name">Panel maker</p><p class="story-card-desc">Leading LCD panel manufacturer running high-performance GPU clusters on AI appliances for scenario-based model applications</p><div class="story-card-metrics"><span><b>30%</b>R&D efficiency</span><span><b>10,000+</b>AI agents</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI OS</a><span class="story-card-ind">Global</span></div>
        <div class="story-card-body"><p class="story-card-name">HKGAI</p><p class="story-card-desc">High-efficiency compute cluster powering Hong Kong's first LLM and the HKGAI Studio platform</p><div class="story-card-metrics"><span><b>90%</b>GPU utilization</span><span><b>60%</b>faster fine-tuning</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE Cloud Native OS</a><span class="story-card-ind">Manufacturing</span></div>
        <div class="story-card-body"><p class="story-card-name">Dongfang Electric</p><p class="story-card-desc">One of the world's largest energy equipment makers, running an AI platform for power-equipment quality analysis</p><div class="story-card-metrics"><span><b>10x</b>production efficiency</span><span><b>30%</b>detection accuracy</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE Cloud Native OS</a><span class="story-card-ind">Finance</span></div>
        <div class="story-card-body"><p class="story-card-name">SPD Bank</p><p class="story-card-desc">Global top-20 bank; China's first cloud-native platform for large-scale payment services</p><div class="story-card-metrics"><span><b>10,000</b>peak TPS</span><span><b>99.99%</b>SLA</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE Cloud Native OS</a><span class="story-card-ind">Retail</span></div>
        <div class="story-card-body"><p class="story-card-name">Watsons Group</p><p class="story-card-desc">World's largest health and beauty retailer, powering its O+O business end to end</p><div class="story-card-metrics"><span><b>99.99%</b>core business SLA</span><span><b>70%+</b>faster releases</span></div></div>
      </div>
    </div>
    <div class="story-group" aria-hidden="true">
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token Factory</a><span class="story-card-ind">AI Center</span></div>
        <div class="story-card-body"><p class="story-card-name">Rundao Xingsuan</p><p class="story-card-desc">Guangxi's first Token-metered AI computing platform and the cornerstone for ASEAN cross-border compute expansion</p><div class="story-card-metrics"><span><b>1000P</b>initial compute scale</span><span><b>3000-5000P</b>planned compute scale</span></div></div>
      </div>
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token Factory</a><span class="story-card-ind">AI Center</span></div>
        <div class="story-card-body"><p class="story-card-name">Xiamen Computing Alliance</p><p class="story-card-desc">City-level compute scheduling across entities, architectures, and data centers, with 60+ AI scenarios in 12 industries</p><div class="story-card-metrics"><span><b>~2000P</b>compute under unified scheduling</span><span><b>7x</b>Token output efficiency</span></div></div>
      </div>
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token Factory</a><span class="story-card-ind">AI Center</span></div>
        <div class="story-card-body"><p class="story-card-name">PIXEL</p><p class="story-card-desc">Japanese listed company focused on data center and system innovation, taking a smart computing center from build to operations and launching Token services fast</p><div class="story-card-metrics"><span><b>End-to-end</b>build to operations</span><span><b>Fast go-live</b>Token services</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI OS</a><span class="story-card-ind">Manufacturing</span></div>
        <div class="story-card-body"><p class="story-card-name">OMRON</p><p class="story-card-desc">Global automation and electronics leader with an enterprise AI knowledge base for manufacturing and administration</p><div class="story-card-metrics"><span><b>65%</b>curation time saved</span><span><b>60%</b>support efficiency</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI OS</a><span class="story-card-ind">Manufacturing</span></div>
        <div class="story-card-body"><p class="story-card-name">Panel maker</p><p class="story-card-desc">Leading LCD panel manufacturer running high-performance GPU clusters on AI appliances for scenario-based model applications</p><div class="story-card-metrics"><span><b>30%</b>R&D efficiency</span><span><b>10,000+</b>AI agents</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI OS</a><span class="story-card-ind">Global</span></div>
        <div class="story-card-body"><p class="story-card-name">HKGAI</p><p class="story-card-desc">High-efficiency compute cluster powering Hong Kong's first LLM and the HKGAI Studio platform</p><div class="story-card-metrics"><span><b>90%</b>GPU utilization</span><span><b>60%</b>faster fine-tuning</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE Cloud Native OS</a><span class="story-card-ind">Manufacturing</span></div>
        <div class="story-card-body"><p class="story-card-name">Dongfang Electric</p><p class="story-card-desc">One of the world's largest energy equipment makers, running an AI platform for power-equipment quality analysis</p><div class="story-card-metrics"><span><b>10x</b>production efficiency</span><span><b>30%</b>detection accuracy</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE Cloud Native OS</a><span class="story-card-ind">Finance</span></div>
        <div class="story-card-body"><p class="story-card-name">SPD Bank</p><p class="story-card-desc">Global top-20 bank; China's first cloud-native platform for large-scale payment services</p><div class="story-card-metrics"><span><b>10,000</b>peak TPS</span><span><b>99.99%</b>SLA</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE Cloud Native OS</a><span class="story-card-ind">Retail</span></div>
        <div class="story-card-body"><p class="story-card-name">Watsons Group</p><p class="story-card-desc">World's largest health and beauty retailer, powering its O+O business end to end</p><div class="story-card-metrics"><span><b>99.99%</b>core business SLA</span><span><b>70%+</b>faster releases</span></div></div>
      </div>
    </div>
  </div>
</div>

## Explore Product Modules

<div class="grid cards home-cards" markdown>

- :material-robot:{ .lg .middle } __Cloud Native AI__

    ---

    - [ClawOS](drun/clawos/intro/)
    - [AI Lab](drun/baize/intro/)
    - [AI Apps](tf/dak/)
    - [LLM Studio](tf/hydra/intro/)
    - [Turbo Inference](tf/inferx/)
    - [Compute Cloud](tf/zestu/)

- :material-server:{ .lg .middle } __Containers__

    ---

    - [Container Management](kpanda/intro/)
    - [Multicloud Management](kairship/intro/)
    - [Container Registry](kangaroo/intro/)
    - [Cloud Native Network](network/intro/)
    - [Cloud Native Storage](storage/)
    - [Virtual Machine](virtnest/intro/)

- :material-file-document-multiple-outline:{ .lg .middle } __Microservices__

    ---

    - [Observability](insight/intro/)
    - [Microservice Engine](skoala/intro/)
    - [Service Mesh](mspider/intro/)

</div>

<div class="grid cards home-cards" markdown>

- :material-human-greeting:{ .lg .middle } __Workbench__

    ---

    - [Workbench](amamba/intro/)

- :material-cloud-outline:{ .lg .middle } __Edge Computing__

    ---

    - [Cloud Edge Collaboration](kant/intro/)

- :material-database:{ .lg .middle } __Data Services and Management__

    ---

    - [Middleware](middleware/)
    - [Global Management](ghippo/intro/)
    - [Device Management](topohub/intro/)

</div>

<div class="doc-marquee" aria-label="Product module quick view">
  <div class="doc-marquee__track doc-marquee__track--rev">
    <div class="doc-marquee__group doc-marquee__group--ai">
      <a class="doc-marquee__chip" href="drun/clawos/intro/"><span class="doc-marquee__dot"></span>ClawOS</a>
      <a class="doc-marquee__chip" href="drun/baize/intro/"><span class="doc-marquee__dot"></span>AI Lab</a>
      <a class="doc-marquee__chip" href="tf/dak/"><span class="doc-marquee__dot"></span>AI Apps</a>
      <a class="doc-marquee__chip" href="tf/hydra/intro/"><span class="doc-marquee__dot"></span>LLM Studio</a>
      <a class="doc-marquee__chip" href="tf/inferx/"><span class="doc-marquee__dot"></span>Turbo Inference</a>
      <a class="doc-marquee__chip" href="tf/zestu/"><span class="doc-marquee__dot"></span>Compute Cloud</a>
      <a class="doc-marquee__chip" href="kpanda/intro/"><span class="doc-marquee__dot"></span>Container Management</a>
      <a class="doc-marquee__chip" href="kairship/intro/"><span class="doc-marquee__dot"></span>Multicloud Management</a>
      <a class="doc-marquee__chip" href="kangaroo/intro/"><span class="doc-marquee__dot"></span>Container Registry</a>
      <a class="doc-marquee__chip" href="network/intro/"><span class="doc-marquee__dot"></span>Cloud Native Network</a>
      <a class="doc-marquee__chip" href="storage/"><span class="doc-marquee__dot"></span>Cloud Native Storage</a>
      <a class="doc-marquee__chip" href="virtnest/intro/"><span class="doc-marquee__dot"></span>Virtual Machine</a>
    </div>
    <div class="doc-marquee__group doc-marquee__group--ai" aria-hidden="true">
      <a class="doc-marquee__chip" href="drun/clawos/intro/"><span class="doc-marquee__dot"></span>ClawOS</a>
      <a class="doc-marquee__chip" href="drun/baize/intro/"><span class="doc-marquee__dot"></span>AI Lab</a>
      <a class="doc-marquee__chip" href="tf/dak/"><span class="doc-marquee__dot"></span>AI Apps</a>
      <a class="doc-marquee__chip" href="tf/hydra/intro/"><span class="doc-marquee__dot"></span>LLM Studio</a>
      <a class="doc-marquee__chip" href="tf/inferx/"><span class="doc-marquee__dot"></span>Turbo Inference</a>
      <a class="doc-marquee__chip" href="tf/zestu/"><span class="doc-marquee__dot"></span>Compute Cloud</a>
      <a class="doc-marquee__chip" href="kpanda/intro/"><span class="doc-marquee__dot"></span>Container Management</a>
      <a class="doc-marquee__chip" href="kairship/intro/"><span class="doc-marquee__dot"></span>Multicloud Management</a>
      <a class="doc-marquee__chip" href="kangaroo/intro/"><span class="doc-marquee__dot"></span>Container Registry</a>
      <a class="doc-marquee__chip" href="network/intro/"><span class="doc-marquee__dot"></span>Cloud Native Network</a>
      <a class="doc-marquee__chip" href="storage/"><span class="doc-marquee__dot"></span>Cloud Native Storage</a>
      <a class="doc-marquee__chip" href="virtnest/intro/"><span class="doc-marquee__dot"></span>Virtual Machine</a>
    </div>
  </div>
  <div class="doc-marquee__track">
    <div class="doc-marquee__group">
      <a class="doc-marquee__chip" href="insight/intro/"><span class="doc-marquee__dot"></span>Observability</a>
      <a class="doc-marquee__chip" href="skoala/intro/"><span class="doc-marquee__dot"></span>Microservice Engine</a>
      <a class="doc-marquee__chip" href="mspider/intro/"><span class="doc-marquee__dot"></span>Service Mesh</a>
      <a class="doc-marquee__chip" href="amamba/intro/"><span class="doc-marquee__dot"></span>Workbench</a>
      <a class="doc-marquee__chip" href="kant/intro/"><span class="doc-marquee__dot"></span>Cloud Edge Collaboration</a>
      <a class="doc-marquee__chip" href="middleware/"><span class="doc-marquee__dot"></span>Middleware</a>
      <a class="doc-marquee__chip" href="ghippo/intro/"><span class="doc-marquee__dot"></span>Global Management</a>
      <a class="doc-marquee__chip" href="topohub/intro/"><span class="doc-marquee__dot"></span>Device Management</a>
      <a class="doc-marquee__chip" href="copilot/"><span class="doc-marquee__dot"></span>Copilot</a>
      <a class="doc-marquee__chip" href="crane/intro/"><span class="doc-marquee__dot"></span>Cockpit</a>
      <a class="doc-marquee__chip" href="leopard/"><span class="doc-marquee__dot"></span>Billing Center</a>
    </div>
    <div class="doc-marquee__group" aria-hidden="true">
      <a class="doc-marquee__chip" href="insight/intro/"><span class="doc-marquee__dot"></span>Observability</a>
      <a class="doc-marquee__chip" href="skoala/intro/"><span class="doc-marquee__dot"></span>Microservice Engine</a>
      <a class="doc-marquee__chip" href="mspider/intro/"><span class="doc-marquee__dot"></span>Service Mesh</a>
      <a class="doc-marquee__chip" href="amamba/intro/"><span class="doc-marquee__dot"></span>Workbench</a>
      <a class="doc-marquee__chip" href="kant/intro/"><span class="doc-marquee__dot"></span>Cloud Edge Collaboration</a>
      <a class="doc-marquee__chip" href="middleware/"><span class="doc-marquee__dot"></span>Middleware</a>
      <a class="doc-marquee__chip" href="ghippo/intro/"><span class="doc-marquee__dot"></span>Global Management</a>
      <a class="doc-marquee__chip" href="topohub/intro/"><span class="doc-marquee__dot"></span>Device Management</a>
      <a class="doc-marquee__chip" href="copilot/"><span class="doc-marquee__dot"></span>Copilot</a>
      <a class="doc-marquee__chip" href="crane/intro/"><span class="doc-marquee__dot"></span>Cockpit</a>
      <a class="doc-marquee__chip" href="leopard/"><span class="doc-marquee__dot"></span>Billing Center</a>
    </div>
  </div>
</div>

<div class="tf-relation">

  <div class="tf-relation-kicker">DaoCloud Product Family · How the Three Fit Together</div>

  <div class="tf-relation-box tf-relation-box--tf">
    <div class="tf-relation-box-title"><a class="tf-relation-box-link" href="tf/">d.run Token Factory · Token production &amp; operations for AI compute centers</a></div>
    <div class="tf-relation-box-sub">Dual user/admin views · Turns compute into measurable, tradable, revenue-ready Token capacity</div>
    <div class="tf-relation-box-detail">LLM Studio · AI Apps (RAG) · Inference (InferX) · Compute Cloud · Copilot / Cockpit / Billing Center</div>
  </div>

  <div class="tf-relation-arrow">▲</div>

  <div class="tf-relation-box tf-relation-box--drun">
    <div class="tf-relation-box-title"><a class="tf-relation-box-link" href="drun/">d.run AI OS · Enterprise AI operating system</a></div>
    <div class="tf-relation-box-sub">Unified scheduling of heterogeneous compute, inference &amp; governance · AI for every team</div>
    <div class="tf-relation-box-detail">Cloud-native AI (LLM Studio, AI Lab, ClawOS, InferX) · Cloud native base · Ops &amp; management</div>
  </div>

  <div class="tf-relation-arrow">▲</div>

  <div class="tf-relation-box tf-relation-box--dce">
    <div class="tf-relation-box-title"><a class="tf-relation-box-link" href="dce/">DCE · Enterprise cloud native operating system (foundation)</a></div>
    <div class="tf-relation-box-sub">Lego-style modular assembly · Core capabilities in containers, networking, storage, middleware, observability &amp; more</div>
  </div>

  <div class="tf-relation-foot">All three are DaoCloud products sharing one cloud native foundation and AI stack — differing in who they serve and why.</div>

</div>

<div class="tf-cta" markdown>

[Apply for DCE Community Free Trial](./dce/license0.md){ .md-button }
[Learn about d.run](drun/index.md){ .md-button }
[Token Factory Overview](tf/index.md){ .md-button }

</div>
