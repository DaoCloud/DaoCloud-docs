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
      <a class="tf-arch-card tf-arch-card--model" href="hydra/intro/">
        <span class="tf-arch-card-title">LLM Studio</span>
        <span class="tf-arch-card-tip">Model serving and O&M management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="dak/">
        <span class="tf-arch-card-title">AI Apps</span>
        <span class="tf-arch-card-tip">Intelligent Q&A and other application capabilities</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="inferx/">
        <span class="tf-arch-card-title">InferX Suite</span>
        <span class="tf-arch-card-tip">Inference acceleration and engine management</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="zestu/">
        <span class="tf-arch-card-title">Compute Cloud</span>
        <span class="tf-arch-card-tip">Heterogeneous compute management and scheduling</span>
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
      <a class="tf-arch-card tf-arch-card--ops" href="leopard/">
        <span class="tf-arch-card-title">Billing Center</span>
        <span class="tf-arch-card-tip">Billing and invoice analysis</span>
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

As a high-efficiency AI Token production and management system built for intelligent computing centers, Token Factory helps traditional computing centers upgrade to an efficient, profitable Token production and operations model. The platform uniformly manages NVIDIA and domestic heterogeneous computing power, relying on intelligent scheduling and inference optimization to transform distributed GPU resources into low-cost, highly stable, tradable standardized token services. Through the Token Factory manager and unified operations system, it achieves global management of resources, production, costs, and supply-demand, providing capabilities to end users, administrators, operators, and O&M personnel, and driving the intelligent computing center's business positioning to upgrade from "providing compute power" to "producing and operating tokens."

![The d.run Token Factory at a glance](images/tf-modules.svg)

## Customer success stories

<style>
/* 客户成功故事卡片 */
.md-typeset .story-marquee{display:grid;margin:1.2rem 0 2rem;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}
.md-typeset .story-track{display:flex;width:max-content;animation:story-move 23s linear infinite}
.md-typeset .story-marquee:hover .story-track{animation-play-state:paused}
.md-typeset .story-group{display:flex;gap:1rem;padding-right:1rem;align-items:stretch}
.md-typeset .story-card{width:330px;flex:none;display:flex;flex-direction:column;border-radius:12px;overflow:hidden;border:1px solid var(--md-default-fg-color--lightest);background:var(--md-default-bg-color);transition:transform .2s ease,border-color .2s ease}
.md-typeset .story-card:hover{transform:translateY(-3px);border-color:var(--s1)}
.md-typeset .story-card-top{display:flex;align-items:center;justify-content:space-between;gap:.5rem;height:62px;padding:0 .9rem;background:linear-gradient(120deg,var(--s1),var(--s2))}
.md-typeset .story-card-high{font-size:.78rem;font-weight:600;color:rgba(255,255,255,.95);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
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

<div class="story-marquee" aria-label="Customer success stories">
  <div class="story-track">
    <div class="story-group">
      <div class="story-card" style="--s1:#2EA452;--s2:#60CE6B">
        <div class="story-card-top"><span class="story-card-high">Cross-border compute</span><span class="story-card-ind">ASEAN</span></div>
        <div class="story-card-body"><p class="story-card-name">Rundao Xingsuan</p><p class="story-card-desc">Guangxi's first Token-metered AI computing platform and the cornerstone for ASEAN cross-border compute expansion</p><div class="story-card-metrics"><span><b>1000P</b>initial compute scale</span><span><b>3000-5000P</b>planned compute scale</span></div></div>
      </div>
      <div class="story-card" style="--s1:#2EA452;--s2:#60CE6B">
        <div class="story-card-top"><span class="story-card-high">Unified scheduling</span><span class="story-card-ind">AI Center</span></div>
        <div class="story-card-body"><p class="story-card-name">Xiamen Computing Alliance</p><p class="story-card-desc">City-level compute scheduling across entities, architectures, and data centers, with 60+ AI scenarios in 12 industries</p><div class="story-card-metrics"><span><b>~2000P</b>compute under unified scheduling</span><span><b>7x</b>Token output efficiency</span></div></div>
      </div>
      <div class="story-card" style="--s1:#2EA452;--s2:#60CE6B">
        <div class="story-card-top"><span class="story-card-high">End-to-end</span><span class="story-card-ind">Japan</span></div>
        <div class="story-card-body"><p class="story-card-name">PIXEL</p><p class="story-card-desc">Japanese listed company focused on data center and system innovation, taking a smart computing center from build to operations and launching Token services fast</p><div class="story-card-metrics"><span><b>End-to-end</b>build to operations</span><span><b>Fast go-live</b>Token services</span></div></div>
      </div>
    </div>
    <div class="story-group" aria-hidden="true">
      <div class="story-card" style="--s1:#2EA452;--s2:#60CE6B">
        <div class="story-card-top"><span class="story-card-high">Cross-border compute</span><span class="story-card-ind">ASEAN</span></div>
        <div class="story-card-body"><p class="story-card-name">Rundao Xingsuan</p><p class="story-card-desc">Guangxi's first Token-metered AI computing platform and the cornerstone for ASEAN cross-border compute expansion</p><div class="story-card-metrics"><span><b>1000P</b>initial compute scale</span><span><b>3000-5000P</b>planned compute scale</span></div></div>
      </div>
      <div class="story-card" style="--s1:#2EA452;--s2:#60CE6B">
        <div class="story-card-top"><span class="story-card-high">Unified scheduling</span><span class="story-card-ind">AI Center</span></div>
        <div class="story-card-body"><p class="story-card-name">Xiamen Computing Alliance</p><p class="story-card-desc">City-level compute scheduling across entities, architectures, and data centers, with 60+ AI scenarios in 12 industries</p><div class="story-card-metrics"><span><b>~2000P</b>compute under unified scheduling</span><span><b>7x</b>Token output efficiency</span></div></div>
      </div>
      <div class="story-card" style="--s1:#2EA452;--s2:#60CE6B">
        <div class="story-card-top"><span class="story-card-high">End-to-end</span><span class="story-card-ind">Japan</span></div>
        <div class="story-card-body"><p class="story-card-name">PIXEL</p><p class="story-card-desc">Japanese listed company focused on data center and system innovation, taking a smart computing center from build to operations and launching Token services fast</p><div class="story-card-metrics"><span><b>End-to-end</b>build to operations</span><span><b>Fast go-live</b>Token services</span></div></div>
      </div>
    </div>
  </div>
</div>

## Learning Path

<style>
.tf-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.tf-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.tf-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.tf-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.tf-path-step:last-child::after{display:none}
.tf-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.tf-path-title{font-weight:700;font-size:0.95rem}
.tf-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.tf-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.tf-path-step::after{display:none}}
</style>

<div class="tf-path">
  <a class="tf-path-step" style="--path-c:#2196f3" href="install/">
    <span class="tf-path-num">1</span>
    <span class="tf-path-title">Deploy the Platform</span>
    <span class="tf-path-desc">Install Token Factory offline, complete initialization and licensing</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#00acc1" href="kpanda/intro/">
    <span class="tf-path-num">2</span>
    <span class="tf-path-title">Onboard Compute</span>
    <span class="tf-path-desc">Attach GPU nodes and create worker clusters</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#43a047" href="hydra/intro/">
    <span class="tf-path-num">3</span>
    <span class="tf-path-title">Deploy Models</span>
    <span class="tf-path-desc">Pick models from the catalog and deploy inference services in one click</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#fb8c00" href="dak/">
    <span class="tf-path-num">4</span>
    <span class="tf-path-title">Build Applications</span>
    <span class="tf-path-desc">Set up corpus libraries and intelligent Q&A applications</span>
    <span class="tf-path-go">Go →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#8e24aa" href="crane/intro/">
    <span class="tf-path-num">5</span>
    <span class="tf-path-title">Operate &amp; Settle</span>
    <span class="tf-path-desc">Cockpit for operations, Billing Center for metering</span>
    <span class="tf-path-go">Go →</span>
  </a>
</div>

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
{: .tf-footer-cta }
