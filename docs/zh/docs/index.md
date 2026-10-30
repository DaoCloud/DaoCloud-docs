---
hide:
  - navigation
  - toc
---

# DaoCloud 文档中心

*[DCE]: DaoCloud Enterprise 的简称

<div class="tf-hero" markdown>

DaoCloud 是全球 AI 领域的开源先锋，致力于通过云原生技术加速企业智能化转型。
本站提供三大产品线的文档内容，覆盖从基础设施、算力调度到模型推理和应用构建的全栈能力。

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
.tf-relation{box-sizing:border-box;margin:1.5rem 0 2rem;background:var(--md-default-bg-color,#fff);color:var(--md-default-fg-color,#0F1D33);font-family:'PingFang SC','Hiragino Sans GB','Microsoft YaHei',system-ui,sans-serif;padding:18px 14px;line-height:1.6;text-align:center;border:1px solid var(--md-default-fg-color--lightest);box-shadow:0 2px 12px rgba(0,0,0,0.06)}
.tf-relation-kicker{font-size:12px;letter-spacing:2px;color:#5A6A85;font-weight:600;margin-bottom:10px}
.tf-relation-box{border-radius:12px;padding:12px 14px;border:1.5px solid transparent}
.tf-relation-box--tf{background:#FDF0E1;border-color:#E8720C}
.tf-relation-box--drun{background:#E8F7EE;border-color:#00C853}
.tf-relation-box--dce{background:#EAF1FE;border-color:#1B66F5}
.tf-relation-box-title{font-size:14.5px;font-weight:800}
.tf-relation-box-sub{font-size:12.5px;color:#5A6A85;margin-top:2px}
.tf-relation-box-detail{font-size:11.5px;color:#0F1D33;margin-top:5px}
.tf-relation-arrow{text-align:center;color:#8A98B0;font-size:15px;line-height:1.1;padding:3px 0}
.tf-relation-foot{font-size:12px;color:#8A98B0;margin-top:10px}
[data-md-color-scheme="slate"] .tf-relation{background:var(--md-default-fg-color--lightest)}
[data-md-color-scheme="slate"] .tf-relation-box--tf{background:rgba(232,114,12,0.12);border-color:rgba(232,114,12,0.4)}
[data-md-color-scheme="slate"] .tf-relation-box--drun{background:rgba(0,200,83,0.12);border-color:rgba(0,200,83,0.4)}
[data-md-color-scheme="slate"] .tf-relation-box--dce{background:rgba(27,102,245,0.14);border-color:rgba(27,102,245,0.45)}
</style>

=== ":material-factory: d.run Token 工厂效能平台"

    这是专为智算中心打造的高效能 AI Token 生产及经营系统，致力于将传统算力中心升级为高效、可盈利的 Token 工厂。
    平台统一纳管英伟达及国产异构算力，通过智能调度与推理优化，将分散的 GPU 算力转化为低成本、高稳定、可交易的标准化 Token 服务。
    依托 Token 工厂管家与统一运营体系，平台实现资源、生产、成本和供需的全局管理，服务终端用户、管理者、运营者与运维者，
    推动智算中心从 "提供算力" 升级为 "生产和运营 Token"。
    [查看/下载 Token 工厂彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/tf.pdf){ .md-button }

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">云原生 AI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="tf/hydra/">
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
      <div class="tf-arch-arrow">▼</div>
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
      <div class="tf-arch-arrow">▼</div>
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
      <div class="tf-arch-arrow">▼</div>
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
    [查看/下载 d.run AI 操作系统彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/drun.pdf){ .md-button }

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">云原生 AI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="drun/hydra/">
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
      <div class="tf-arch-arrow">▼</div>
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
      <div class="tf-arch-arrow">▼</div>
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
      <div class="tf-arch-arrow">▼</div>
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
    [查看/下载 DaoCloud Enterprise 彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/dce.pdf){ .md-button }

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">云原生底座</div>
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
      <div class="tf-arch-arrow">▼</div>
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

<div class="tf-relation">

  <div class="tf-relation-kicker">DaoCloud 产品族 ·「道生三，三生万物」</div>

  <div class="tf-relation-box tf-relation-box--tf">
    <div class="tf-relation-box-title">Token 工厂 · 面向智算中心的 Token 生产与经营系统</div>
    <div class="tf-relation-box-sub">用户/管理员双视图 · 把算力转化为可计量、可交易、可运营的 Token 产能</div>
    <div class="tf-relation-box-detail">大模型服务平台 · AI 应用 (RAG) · 推理加速 InferX · 算力云 · Copilot/驾驶舱/费用中心</div>
  </div>

  <div class="tf-relation-arrow">▲</div>

  <div class="tf-relation-box tf-relation-box--drun">
    <div class="tf-relation-box-title">d.run AI 操作系统 · 面向企业的 AI 操作系统</div>
    <div class="tf-relation-box-sub">异构算力调度 + 模型推理 + 运营治理一体 · 面向企业全部门输出 AI 服务</div>
    <div class="tf-relation-box-detail">云原生 AI（Hydra/AI Lab/ClawOS/InferX）· 云原生底座 · 运营与运维管理</div>
  </div>

  <div class="tf-relation-arrow">▲</div>

  <div class="tf-relation-box tf-relation-box--dce">
    <div class="tf-relation-box-title">DCE · 企业级云原生操作系统（底座）</div>
    <div class="tf-relation-box-sub">乐高式模块化搭建 · 容器/网络/存储/中间件/可观测/全局管理等基础能力</div>
  </div>

  <div class="tf-relation-foot">三者同属 DaoCloud 产品族，共享云原生底座与 AI 组件，差异在“服务对象”与“经营目标”</div>

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

- :material-database:{ .lg .middle } __数据服务__

    ---

    - [中间件](middleware/)

- :material-cloud-outline:{ .lg .middle } __边缘计算__

    ---

    - [云边协同](kant/intro/)

- :material-cog-outline:{ .lg .middle } __管理__

    ---

    - [全局管理](ghippo/intro/)
    - [设备管理](topohub/intro/)

</div>

<div class="tf-cta" markdown>

[申请 DCE 社区免费体验](./dce/license0.md){ .md-button .md-button--primary }
[了解 d.run](drun/index.md){ .md-button .md-button--primary }
[Token 工厂概览](tf/index.md){ .md-button .md-button--primary }

</div>
