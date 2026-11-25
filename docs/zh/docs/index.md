---
hide:
  - navigation
  - toc
---

# DaoCloud 文档中心

*[DCE]: DaoCloud Enterprise 的简称
*[d.run]: DaoCloud Runs Intelligence

<div class="tf-hero" markdown>

DaoCloud 是全球 AI 领域的开源先锋，致力于通过云原生技术加速企业 AI 智能化转型。
本站覆盖从算力调度、模型训练和推理，到智能应用构建和多智能体治理的 AI 全栈能力。

<div class="tf-hero-badges">
<a class="tf-hero-badge tf-hero-badge--tf" href="tf/">d.run Token 工厂效能平台</a>
<a class="tf-hero-badge tf-hero-badge--drun" href="drun/">d.run AI 操作系统</a>
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
/* 首页：三款 DaoCloud 产品关系图 */
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
/* 暗色模式：深色实底 + 高饱和品牌色描边 + 亮色文字 */
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

/* tf-hero 流光边框 */
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

=== ":material-factory: d.run Token 工厂效能平台"

    这是专为智算中心打造的高效能 AI Token 生产及经营系统，致力于将传统算力中心升级为高效、可盈利的 Token 工厂。
    平台统一纳管英伟达及国产异构算力，通过智能调度与推理优化，将分散的 GPU 算力转化为低成本、高稳定、可交易的标准化 Token 服务。
    依托 Token 工厂管家与统一运营体系，平台实现资源、生产、成本和供需的全局管理，服务终端用户、管理者、运营者与运维者，
    推动智算中心从 "提供算力" 升级为 "生产和运营 Token"。
    [查阅 Token 工厂彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/tf.pdf){ .md-button }

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">云原生 AI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="tf/hydra/intro/">
            <span class="tf-arch-card-title">大模型服务平台</span>
            <span class="tf-arch-card-tip">模型部署与运维管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/dak/">
            <span class="tf-arch-card-title">AI 应用</span>
            <span class="tf-arch-card-tip">智能问答等应用能力</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/inferx/">
            <span class="tf-arch-card-title">推理加速</span>
            <span class="tf-arch-card-tip">推理加速与引擎管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="tf/zestu/">
            <span class="tf-arch-card-title">算力云</span>
            <span class="tf-arch-card-tip">异构算力纳管与调度</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">云原生底座</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="tf/kpanda/intro/">
            <span class="tf-arch-card-title">容器管理</span>
            <span class="tf-arch-card-tip">集群与工作负载管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="tf/kangaroo/intro/">
            <span class="tf-arch-card-title">镜像仓库</span>
            <span class="tf-arch-card-tip">镜像托管与集成</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="tf/topohub/intro/">
            <span class="tf-arch-card-title">设备管理</span>
            <span class="tf-arch-card-tip">硬件设备统一纳管</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="tf/network/intro/">
            <span class="tf-arch-card-title">云原生网络</span>
            <span class="tf-arch-card-tip">多 CNI 融合网络</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="tf/storage/">
            <span class="tf-arch-card-title">云原生存储</span>
            <span class="tf-arch-card-tip">容器化存储与 CSI</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">运营管理</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="tf/copilot/">
            <span class="tf-arch-card-title">Copilot</span>
            <span class="tf-arch-card-tip">智能运维助手</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="tf/crane/intro/">
            <span class="tf-arch-card-title">驾驶舱</span>
            <span class="tf-arch-card-tip">运营数据可视化</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="tf/leopard/">
            <span class="tf-arch-card-title">费用中心</span>
            <span class="tf-arch-card-tip">计费与账单分析</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">运维管理</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="tf/insight/intro/">
            <span class="tf-arch-card-title">可观测性</span>
            <span class="tf-arch-card-tip">指标日志链路观测</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="tf/ghippo/intro/">
            <span class="tf-arch-card-title">全局管理</span>
            <span class="tf-arch-card-tip">用户权限与平台设置</span>
          </a>
        </div>
      </div>
    </div>

=== ":material-robot-happy: d.run AI 操作系统"

    d.run 依托全球前三的 Kubernetes 调度技术与 vLLM 等主流开源推理引擎核心贡献积淀，统一纳管多元异构算力，
    实现颗粒化调度、全栈推理优化与全链路 Token 治理，算力利用率超 80%，将算力高效转化为可管可控的 Token 化 AI 生产力；
    平台汇聚全球主流大模型生态，配备可视化运营驾驶舱与 d.run Copilot 智能助手，面向企业全部门输出稳定高效的 AI 服务，
    全方位支撑业务智能化长期升级。
    [查阅 d.run AI 操作系统彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/drun.pdf){ .md-button }

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">云原生 AI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="drun/hydra/intro/">
            <span class="tf-arch-card-title">大模型服务平台</span>
            <span class="tf-arch-card-tip">模型部署与运维管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/baize/intro/">
            <span class="tf-arch-card-title">AI Lab</span>
            <span class="tf-arch-card-tip">云原生训推一体化</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/inferx/">
            <span class="tf-arch-card-title">推理加速</span>
            <span class="tf-arch-card-tip">推理加速与引擎管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="drun/clawos/intro/">
            <span class="tf-arch-card-title">ClawOS</span>
            <span class="tf-arch-card-tip">多智能体运行与治理</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">云原生底座</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="drun/kpanda/intro/">
            <span class="tf-arch-card-title">容器管理</span>
            <span class="tf-arch-card-tip">集群与工作负载管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/kangaroo/intro/">
            <span class="tf-arch-card-title">镜像仓库</span>
            <span class="tf-arch-card-tip">镜像托管与集成</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/topohub/intro/">
            <span class="tf-arch-card-title">设备管理</span>
            <span class="tf-arch-card-tip">硬件设备统一纳管</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/network/intro/">
            <span class="tf-arch-card-title">云原生网络</span>
            <span class="tf-arch-card-tip">多 CNI 融合网络</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="drun/storage/">
            <span class="tf-arch-card-title">云原生存储</span>
            <span class="tf-arch-card-tip">容器化存储与 CSI</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">运营管理</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="drun/copilot/">
            <span class="tf-arch-card-title">Copilot</span>
            <span class="tf-arch-card-tip">智能运维助手</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="drun/crane/intro/">
            <span class="tf-arch-card-title">驾驶舱</span>
            <span class="tf-arch-card-tip">运营数据可视化</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">运维管理</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="drun/insight/intro/">
            <span class="tf-arch-card-title">可观测性</span>
            <span class="tf-arch-card-tip">指标日志链路观测</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="drun/ghippo/intro/">
            <span class="tf-arch-card-title">全局管理</span>
            <span class="tf-arch-card-tip">用户权限与平台设置</span>
          </a>
        </div>
      </div>
    </div>

=== ":octicons-stack-16: DaoCloud Enterprise"

    DaoCloud Enterprise (DCE) 是一款高性能、可扩展的云原生操作系统，
    是[经 CNCF 认证的 Kubernetes - AI Platform](./dce/kcsp.md)。
    它能够在任何基础设施和任意环境中提供一致、稳定的体验，支持异构云、边缘云和多云编排等。
    [查阅 DaoCloud Enterprise 彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/dce.pdf){ .md-button }

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">开箱即用的功能模块</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="middleware/">
            <span class="tf-arch-card-title">中间件</span>
            <span class="tf-arch-card-tip">数据库与消息队列</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kairship/intro/">
            <span class="tf-arch-card-title">多云编排</span>
            <span class="tf-arch-card-tip">多云与混合云编排</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kangaroo/intro/">
            <span class="tf-arch-card-title">镜像仓库</span>
            <span class="tf-arch-card-tip">镜像托管与集成</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="mspider/intro/">
            <span class="tf-arch-card-title">服务网格</span>
            <span class="tf-arch-card-tip">非侵入式服务治理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="skoala/intro/">
            <span class="tf-arch-card-title">微服务引擎</span>
            <span class="tf-arch-card-tip">微服务治理与网关</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="amamba/intro/">
            <span class="tf-arch-card-title">应用工作台</span>
            <span class="tf-arch-card-tip">CI/CD 与应用交付</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kpanda/intro/">
            <span class="tf-arch-card-title">容器管理</span>
            <span class="tf-arch-card-tip">集群与工作负载管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="virtnest/intro/">
            <span class="tf-arch-card-title">虚拟机</span>
            <span class="tf-arch-card-tip">KubeVirt 虚拟机管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="topohub/intro/">
            <span class="tf-arch-card-title">设备管理</span>
            <span class="tf-arch-card-tip">硬件设备统一纳管</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kant/intro/">
            <span class="tf-arch-card-title">云边协同</span>
            <span class="tf-arch-card-tip">边缘节点纳管与协同</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="network/intro/">
            <span class="tf-arch-card-title">云原生网络</span>
            <span class="tf-arch-card-tip">多 CNI 融合网络</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="storage/">
            <span class="tf-arch-card-title">云原生存储</span>
            <span class="tf-arch-card-tip">容器化存储与 CSI</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▲</div>
      <div class="tf-arch-layer tf-arch-layer--ops">
        <div class="tf-arch-layer-label">运维管理</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--ops" href="insight/intro/">
            <span class="tf-arch-card-title">可观测性</span>
            <span class="tf-arch-card-tip">指标日志链路观测</span>
          </a>
          <a class="tf-arch-card tf-arch-card--ops" href="ghippo/intro/">
            <span class="tf-arch-card-title">全局管理</span>
            <span class="tf-arch-card-tip">用户权限与平台设置</span>
          </a>
        </div>
      </div>
    </div>

## 客户成功故事

<div class="story-marquee" aria-label="客户成功故事">
  <div class="story-track">
    <div class="story-group">
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token 工厂效能平台</a><span class="story-card-ind">智算中心</span></div>
        <div class="story-card-body"><p class="story-card-name">润道星算</p><p class="story-card-desc">广西首个以 Token 为计量单位的智算服务平台，布局东盟跨境算力与 AI Token 出海业务的核心基石</p><div class="story-card-metrics"><span><b>1000P</b>首期算力规模</span><span><b>3000P-5000P</b>规划算力规模</span></div></div>
      </div>
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token 工厂效能平台</a><span class="story-card-ind">智算中心</span></div>
        <div class="story-card-body"><p class="story-card-name">厦门思明算力联盟</p><p class="story-card-desc">市级智能算力跨主体、跨架构、跨中心的统一调度，开放 12 大行业、60 余个 AI 场景</p><div class="story-card-metrics"><span><b>近 2000P</b>全域调度算力</span><span><b>7 倍</b>Token 输出效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token 工厂效能平台</a><span class="story-card-ind">智算中心</span></div>
        <div class="story-card-body"><p class="story-card-name">PIXEL</p><p class="story-card-desc">专注数据中心与系统创新的日本上市企业，以端到端方案从基建到运营落地智算中心，快速上线 Token 服务</p><div class="story-card-metrics"><span><b>端到端</b>基建到运营</span><span><b>快速上线</b>Token 服务</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI 操作系统</a><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">欧姆龙</p><p class="story-card-desc">全球知名的自动化控制及电子设备制造领军企业，打造工业制造与企业行政双场景 AI 知识库</p><div class="story-card-metrics"><span><b>65%</b>知识整理工时节约</span><span><b>60%</b>客服处理效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI 操作系统</a><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">液晶屏制造巨头</p><p class="story-card-desc">半导体液晶屏行业领军企业，以 AI 一体机构建高性能 GPU 集群，落地制造业场景化模型应用</p><div class="story-card-metrics"><span><b>30%</b>软件研发效率提升</span><span><b>10,000+</b>AI 智能体</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI 操作系统</a><span class="story-card-ind">港澳</span></div>
        <div class="story-card-body"><p class="story-card-name">HKGAI</p><p class="story-card-desc">联合港科大打造支撑首个港产大模型落地的高效能算力集群，全面赋能 HKGAI Studio</p><div class="story-card-metrics"><span><b>90%</b>GPU 利用率</span><span><b>60%</b>模型微调效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE 云原生操作系统</a><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">东方电气</p><p class="story-card-desc">全球最大的能源装备制造企业集团之一，打造发电装备质量智能分析 AI 中台</p><div class="story-card-metrics"><span><b>10 倍</b>生产效率提升</span><span><b>30%</b>缺陷检测准确率</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE 云原生操作系统</a><span class="story-card-ind">金融</span></div>
        <div class="story-card-body"><p class="story-card-name">浦发银行</p><p class="story-card-desc">全球银行前 20 强，中国首个支持大规模支付业务的云原生平台</p><div class="story-card-metrics"><span><b>10,000</b>支付峰值 TPS</span><span><b>99.99%</b>SLA</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE 云原生操作系统</a><span class="story-card-ind">零售</span></div>
        <div class="story-card-body"><p class="story-card-name">屈臣氏集团</p><p class="story-card-desc">全球最大的保健及美容产品零售商，端到端赋能 O+O 业务</p><div class="story-card-metrics"><span><b>99.99%</b>核心业务 SLA</span><span><b>70%+</b>发布耗时缩短</span></div></div>
      </div>
    </div>
    <div class="story-group" aria-hidden="true">
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token 工厂效能平台</a><span class="story-card-ind">智算中心</span></div>
        <div class="story-card-body"><p class="story-card-name">润道星算</p><p class="story-card-desc">广西首个以 Token 为计量单位的智算服务平台，布局东盟跨境算力与 AI Token 出海业务的核心基石</p><div class="story-card-metrics"><span><b>1000P</b>首期算力规模</span><span><b>3000P-5000P</b>规划算力规模</span></div></div>
      </div>
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token 工厂效能平台</a><span class="story-card-ind">智算中心</span></div>
        <div class="story-card-body"><p class="story-card-name">厦门思明算力联盟</p><p class="story-card-desc">市级智能算力跨主体、跨架构、跨中心的统一调度，开放 12 大行业、60 余个 AI 场景</p><div class="story-card-metrics"><span><b>近 2000P</b>全域调度算力</span><span><b>7 倍</b>Token 输出效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#16A34A;--s2:#4ADE80">
        <div class="story-card-top"><a class="story-card-prod" href="tf/">d.run Token 工厂效能平台</a><span class="story-card-ind">智算中心</span></div>
        <div class="story-card-body"><p class="story-card-name">PIXEL</p><p class="story-card-desc">专注数据中心与系统创新的日本上市企业，以端到端方案从基建到运营落地智算中心，快速上线 Token 服务</p><div class="story-card-metrics"><span><b>端到端</b>基建到运营</span><span><b>快速上线</b>Token 服务</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI 操作系统</a><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">欧姆龙</p><p class="story-card-desc">全球知名的自动化控制及电子设备制造领军企业，打造工业制造与企业行政双场景 AI 知识库</p><div class="story-card-metrics"><span><b>65%</b>知识整理工时节约</span><span><b>60%</b>客服处理效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI 操作系统</a><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">液晶屏制造巨头</p><p class="story-card-desc">半导体液晶屏行业领军企业，以 AI 一体机构建高性能 GPU 集群，落地制造业场景化模型应用</p><div class="story-card-metrics"><span><b>30%</b>软件研发效率提升</span><span><b>10,000+</b>AI 智能体</span></div></div>
      </div>
      <div class="story-card" style="--s1:#7C5CFF;--s2:#A78BFF">
        <div class="story-card-top"><a class="story-card-prod" href="drun/">d.run AI 操作系统</a><span class="story-card-ind">港澳</span></div>
        <div class="story-card-body"><p class="story-card-name">HKGAI</p><p class="story-card-desc">联合港科大打造支撑首个港产大模型落地的高效能算力集群，全面赋能 HKGAI Studio</p><div class="story-card-metrics"><span><b>90%</b>GPU 利用率</span><span><b>60%</b>模型微调效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE 云原生操作系统</a><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">东方电气</p><p class="story-card-desc">全球最大的能源装备制造企业集团之一，打造发电装备质量智能分析 AI 中台</p><div class="story-card-metrics"><span><b>10 倍</b>生产效率提升</span><span><b>30%</b>缺陷检测准确率</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE 云原生操作系统</a><span class="story-card-ind">金融</span></div>
        <div class="story-card-body"><p class="story-card-name">浦发银行</p><p class="story-card-desc">全球银行前 20 强，中国首个支持大规模支付业务的云原生平台</p><div class="story-card-metrics"><span><b>10,000</b>支付峰值 TPS</span><span><b>99.99%</b>SLA</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><a class="story-card-prod" href="dce/">DCE 云原生操作系统</a><span class="story-card-ind">零售</span></div>
        <div class="story-card-body"><p class="story-card-name">屈臣氏集团</p><p class="story-card-desc">全球最大的保健及美容产品零售商，端到端赋能 O+O 业务</p><div class="story-card-metrics"><span><b>99.99%</b>核心业务 SLA</span><span><b>70%+</b>发布耗时缩短</span></div></div>
      </div>
    </div>
  </div>
</div>

## 探索产品模块

<div class="grid cards home-cards" markdown>

- :material-robot:{ .lg .middle } __云原生 AI__

    ---

    - [ClawOS](drun/clawos/intro/)
    - [AI Lab](drun/baize/intro/)
    - [AI 应用](tf/dak/)
    - [大模型服务平台](tf/hydra/intro/)
    - [推理加速](tf/inferx/)
    - [算力云](tf/zestu/)

- :material-server:{ .lg .middle } __容器__

    ---

    - [容器管理](kpanda/intro/)
    - [多云编排](kairship/intro/)
    - [镜像仓库](kangaroo/intro/)
    - [云原生网络](network/intro/)
    - [云原生存储](storage/)
    - [虚拟机](virtnest/intro/)

- :material-file-document-multiple-outline:{ .lg .middle } __微服务__

    ---

    - [可观测性](insight/intro/)
    - [微服务引擎](skoala/intro/)
    - [服务网格](mspider/intro/)

</div>

<div class="grid cards home-cards" markdown>

- :material-human-greeting:{ .lg .middle } __工作台__

    ---

    - [应用工作台](amamba/intro/)

- :material-cloud-outline:{ .lg .middle } __边缘计算__

    ---

    - [云边协同](kant/intro/)

- :material-database:{ .lg .middle } __数据服务和管理__

    ---

    - [中间件](middleware/)
    - [全局管理](ghippo/intro/)
    - [设备管理](topohub/intro/)
    - [Copilot](./copilot/index.md)
    - [驾驶舱](./crane/intro/index.md)
    - [费用中心](./leopard/index.md)

</div>


<div class="doc-marquee" aria-label="产品模块速览">
  <div class="doc-marquee__track doc-marquee__track--rev">
    <div class="doc-marquee__group doc-marquee__group--ai">
      <a class="doc-marquee__chip" href="drun/clawos/intro/"><span class="doc-marquee__dot"></span>ClawOS</a>
      <a class="doc-marquee__chip" href="drun/baize/intro/"><span class="doc-marquee__dot"></span>AI Lab</a>
      <a class="doc-marquee__chip" href="tf/dak/"><span class="doc-marquee__dot"></span>AI 应用</a>
      <a class="doc-marquee__chip" href="tf/hydra/intro/"><span class="doc-marquee__dot"></span>大模型服务平台</a>
      <a class="doc-marquee__chip" href="tf/inferx/"><span class="doc-marquee__dot"></span>推理加速</a>
      <a class="doc-marquee__chip" href="tf/zestu/"><span class="doc-marquee__dot"></span>算力云</a>
      <a class="doc-marquee__chip" href="kpanda/intro/"><span class="doc-marquee__dot"></span>容器管理</a>
      <a class="doc-marquee__chip" href="kairship/intro/"><span class="doc-marquee__dot"></span>多云编排</a>
      <a class="doc-marquee__chip" href="kangaroo/intro/"><span class="doc-marquee__dot"></span>镜像仓库</a>
      <a class="doc-marquee__chip" href="network/intro/"><span class="doc-marquee__dot"></span>云原生网络</a>
      <a class="doc-marquee__chip" href="storage/"><span class="doc-marquee__dot"></span>云原生存储</a>
      <a class="doc-marquee__chip" href="virtnest/intro/"><span class="doc-marquee__dot"></span>虚拟机</a>
    </div>
    <div class="doc-marquee__group doc-marquee__group--ai" aria-hidden="true">
      <a class="doc-marquee__chip" href="drun/clawos/intro/"><span class="doc-marquee__dot"></span>ClawOS</a>
      <a class="doc-marquee__chip" href="drun/baize/intro/"><span class="doc-marquee__dot"></span>AI Lab</a>
      <a class="doc-marquee__chip" href="tf/dak/"><span class="doc-marquee__dot"></span>AI 应用</a>
      <a class="doc-marquee__chip" href="tf/hydra/intro/"><span class="doc-marquee__dot"></span>大模型服务平台</a>
      <a class="doc-marquee__chip" href="tf/inferx/"><span class="doc-marquee__dot"></span>推理加速</a>
      <a class="doc-marquee__chip" href="tf/zestu/"><span class="doc-marquee__dot"></span>算力云</a>
      <a class="doc-marquee__chip" href="kpanda/intro/"><span class="doc-marquee__dot"></span>容器管理</a>
      <a class="doc-marquee__chip" href="kairship/intro/"><span class="doc-marquee__dot"></span>多云编排</a>
      <a class="doc-marquee__chip" href="kangaroo/intro/"><span class="doc-marquee__dot"></span>镜像仓库</a>
      <a class="doc-marquee__chip" href="network/intro/"><span class="doc-marquee__dot"></span>云原生网络</a>
      <a class="doc-marquee__chip" href="storage/"><span class="doc-marquee__dot"></span>云原生存储</a>
      <a class="doc-marquee__chip" href="virtnest/intro/"><span class="doc-marquee__dot"></span>虚拟机</a>
    </div>
  </div>
  <div class="doc-marquee__track">
    <div class="doc-marquee__group">
      <a class="doc-marquee__chip" href="insight/intro/"><span class="doc-marquee__dot"></span>可观测性</a>
      <a class="doc-marquee__chip" href="skoala/intro/"><span class="doc-marquee__dot"></span>微服务引擎</a>
      <a class="doc-marquee__chip" href="mspider/intro/"><span class="doc-marquee__dot"></span>服务网格</a>
      <a class="doc-marquee__chip" href="amamba/intro/"><span class="doc-marquee__dot"></span>应用工作台</a>
      <a class="doc-marquee__chip" href="kant/intro/"><span class="doc-marquee__dot"></span>云边协同</a>
      <a class="doc-marquee__chip" href="middleware/"><span class="doc-marquee__dot"></span>中间件</a>
      <a class="doc-marquee__chip" href="ghippo/intro/"><span class="doc-marquee__dot"></span>全局管理</a>
      <a class="doc-marquee__chip" href="topohub/intro/"><span class="doc-marquee__dot"></span>设备管理</a>
      <a class="doc-marquee__chip" href="copilot/"><span class="doc-marquee__dot"></span>Copilot</a>
      <a class="doc-marquee__chip" href="crane/intro/"><span class="doc-marquee__dot"></span>驾驶舱</a>
      <a class="doc-marquee__chip" href="leopard/"><span class="doc-marquee__dot"></span>费用中心</a>
    </div>
    <div class="doc-marquee__group" aria-hidden="true">
      <a class="doc-marquee__chip" href="insight/intro/"><span class="doc-marquee__dot"></span>可观测性</a>
      <a class="doc-marquee__chip" href="skoala/intro/"><span class="doc-marquee__dot"></span>微服务引擎</a>
      <a class="doc-marquee__chip" href="mspider/intro/"><span class="doc-marquee__dot"></span>服务网格</a>
      <a class="doc-marquee__chip" href="amamba/intro/"><span class="doc-marquee__dot"></span>应用工作台</a>
      <a class="doc-marquee__chip" href="kant/intro/"><span class="doc-marquee__dot"></span>云边协同</a>
      <a class="doc-marquee__chip" href="middleware/"><span class="doc-marquee__dot"></span>中间件</a>
      <a class="doc-marquee__chip" href="ghippo/intro/"><span class="doc-marquee__dot"></span>全局管理</a>
      <a class="doc-marquee__chip" href="topohub/intro/"><span class="doc-marquee__dot"></span>设备管理</a>
      <a class="doc-marquee__chip" href="copilot/"><span class="doc-marquee__dot"></span>Copilot</a>
      <a class="doc-marquee__chip" href="crane/intro/"><span class="doc-marquee__dot"></span>驾驶舱</a>
      <a class="doc-marquee__chip" href="leopard/"><span class="doc-marquee__dot"></span>费用中心</a>
    </div>
  </div>
</div>

<div class="tf-relation">

  <div class="tf-relation-kicker">DaoCloud 产品族 ·「道生三，三生万物」</div>

  <div class="tf-relation-box tf-relation-box--tf">
    <div class="tf-relation-box-title"><a class="tf-relation-box-link" href="tf/">d.run Token 工厂效能平台 · 面向智算中心的 Token 生产与经营系统</a></div>
    <div class="tf-relation-box-sub">用户/管理员双视图 · 把算力转化为可计量、可交易、可运营的 Token 产能</div>
    <div class="tf-relation-box-detail">大模型服务平台 · AI 应用 (RAG) · 推理加速 · 算力云 · Copilot/驾驶舱/费用中心</div>
  </div>

  <div class="tf-relation-arrow">▲</div>

  <div class="tf-relation-box tf-relation-box--drun">
    <div class="tf-relation-box-title"><a class="tf-relation-box-link" href="drun/">d.run AI 操作系统 · 面向企业的 AI 操作系统</a></div>
    <div class="tf-relation-box-sub">异构算力调度 + 模型推理 + 运营治理一体 · 面向企业全部门输出 AI 服务</div>
    <div class="tf-relation-box-detail">云原生 AI（Hydra/AI Lab/ClawOS/InferY）· 云原生底座 · 运营与运维管理</div>
  </div>

  <div class="tf-relation-arrow">▲</div>

  <div class="tf-relation-box tf-relation-box--dce">
    <div class="tf-relation-box-title"><a class="tf-relation-box-link" href="dce/">DaoCloud Enterprise · 企业级云原生操作系统（底座）</a></div>
    <div class="tf-relation-box-sub">乐高式模块化搭建 · 容器/网络/存储/中间件/可观测/全局管理等基础能力</div>
  </div>

  <div class="tf-relation-foot">三者同属 DaoCloud 产品族，共享云原生底座与 AI 组件，差异在“服务对象”与“经营目标”</div>

</div>

<div class="tf-cta" markdown>

[申请 DCE 社区免费体验](./dce/license0.md){ .md-button }
[了解 d.run](drun/index.md){ .md-button }
[Token 工厂概览](tf/index.md){ .md-button }

</div>
