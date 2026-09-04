---
hide:
  - navigation
  - toc
---

# DaoCloud 文档中心

<div class="tf-hero" markdown>

DaoCloud 是全球 AI 领域的开源先锋，致力于通过云原生技术加速企业智能化转型。
本站提供三大产品线的文档内容，覆盖从基础设施、算力调度到模型推理和应用构建的全栈能力。

<div class="tf-hero-badges">
<a class="tf-hero-badge tf-hero-badge--tf" href="tf/">Token 工厂效能平台</a>
<a class="tf-hero-badge tf-hero-badge--drun" href="drun/">d.run AI 操作系统</a>
<a class="tf-hero-badge tf-hero-badge--dce" href="dce/">DCE 云原生操作系统</a>
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

=== ":material-factory: Token 工厂效能平台"

    这是专为智算中心打造的高效能 AI Token 生产及经营系统，致力于将传统算力中心升级为高效、可盈利的 Token 工厂。
    平台统一纳管英伟达及国产异构算力，通过智能调度与推理优化，将分散的 GPU 算力转化为低成本、高稳定、可交易的标准化 Token 服务。
    依托 Token 工厂管家与统一运营体系，平台实现资源、生产、成本和供需的全局管理，服务终端用户、管理者、运营者与运维者，
    推动智算中心从 "提供算力" 升级为 "生产和运营 Token"。

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">云原生 AI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="clawos/intro/">
            <span class="tf-arch-card-title">ClawOS</span>
            <span class="tf-arch-card-tip">多智能体运行与治理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="dak/">
            <span class="tf-arch-card-title">AI 应用</span>
            <span class="tf-arch-card-tip">智能问答等应用能力</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="hydra/">
            <span class="tf-arch-card-title">大模型服务平台</span>
            <span class="tf-arch-card-tip">模型部署与运维管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="inferx/">
            <span class="tf-arch-card-title">InferX 推理</span>
            <span class="tf-arch-card-tip">推理加速与引擎管理</span>
          </a>
          <div class="tf-arch-card tf-arch-card--model">
            <span class="tf-arch-card-title">redhare 分布式缓存</span>
            <span class="tf-arch-card-tip">分布式缓存加速服务</span>
          </div>
          <a class="tf-arch-card tf-arch-card--model" href="zestu/">
            <span class="tf-arch-card-title">算力云</span>
            <span class="tf-arch-card-tip">异构算力纳管与调度</span>
          </a>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">云原生底座</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="kpanda/intro/">
            <span class="tf-arch-card-title">容器管理</span>
            <span class="tf-arch-card-tip">集群与工作负载管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kangaroo/intro/">
            <span class="tf-arch-card-title">镜像仓库</span>
            <span class="tf-arch-card-tip">镜像托管与集成</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="topohub/intro/">
            <span class="tf-arch-card-title">设备管理</span>
            <span class="tf-arch-card-tip">硬件设备统一纳管</span>
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
        <div class="tf-arch-layer-label">运营管理</div>
        <div class="tf-arch-cards">
          <div class="tf-arch-card tf-arch-card--ops">
            <span class="tf-arch-card-title">Copilot</span>
            <span class="tf-arch-card-tip">智能运维助手</span>
          </div>
          <div class="tf-arch-card tf-arch-card--ops">
            <span class="tf-arch-card-title">驾驶舱</span>
            <span class="tf-arch-card-tip">运营数据可视化</span>
          </div>
          <a class="tf-arch-card tf-arch-card--ops" href="leopard/">
            <span class="tf-arch-card-title">费用中心</span>
            <span class="tf-arch-card-tip">计费与账单分析</span>
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

=== ":material-robot-happy: d.run AI 操作系统"

    d.run 依托全球前三的 Kubernetes 调度技术与 vLLM 等主流开源推理引擎核心贡献积淀，统一纳管多元异构算力，
    实现颗粒化调度、全栈推理优化与全链路 Token 治理，算力利用率超 80%，将算力高效转化为可管可控的 Token 化 AI 生产力；
    平台汇聚全球主流大模型生态，配备可视化运营驾驶舱与 d.run Copilot 智能助手，面向企业全部门输出稳定高效的 AI 服务，
    全方位支撑业务智能化长期升级。

    <div class="tf-arch tf-arch--compact">
      <div class="tf-arch-layer tf-arch-layer--model">
        <div class="tf-arch-layer-label">云原生 AI</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--model" href="clawos/intro/">
            <span class="tf-arch-card-title">ClawOS</span>
            <span class="tf-arch-card-tip">多智能体运行与治理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="hydra/">
            <span class="tf-arch-card-title">大模型服务平台</span>
            <span class="tf-arch-card-tip">模型部署与运维管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="baize/intro/">
            <span class="tf-arch-card-title">AI Lab</span>
            <span class="tf-arch-card-tip">云原生训推一体化</span>
          </a>
          <a class="tf-arch-card tf-arch-card--model" href="inferx/">
            <span class="tf-arch-card-title">InferX 推理套件</span>
            <span class="tf-arch-card-tip">推理加速与引擎管理</span>
          </a>
          <div class="tf-arch-card tf-arch-card--model">
            <span class="tf-arch-card-title">redhare 分布式缓存</span>
            <span class="tf-arch-card-tip">分布式缓存加速服务</span>
          </div>
        </div>
      </div>
      <div class="tf-arch-arrow">▼</div>
      <div class="tf-arch-layer tf-arch-layer--compute">
        <div class="tf-arch-layer-label">云原生底座</div>
        <div class="tf-arch-cards">
          <a class="tf-arch-card tf-arch-card--compute" href="kpanda/intro/">
            <span class="tf-arch-card-title">容器管理</span>
            <span class="tf-arch-card-tip">集群与工作负载管理</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="topohub/intro/">
            <span class="tf-arch-card-title">设备管理</span>
            <span class="tf-arch-card-tip">硬件设备统一纳管</span>
          </a>
          <a class="tf-arch-card tf-arch-card--compute" href="kangaroo/intro/">
            <span class="tf-arch-card-title">镜像仓库</span>
            <span class="tf-arch-card-tip">镜像托管与集成</span>
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
        <div class="tf-arch-layer-label">运营管理</div>
        <div class="tf-arch-cards">
          <div class="tf-arch-card tf-arch-card--ops">
            <span class="tf-arch-card-title">Copilot</span>
            <span class="tf-arch-card-tip">智能运维助手</span>
          </div>
          <div class="tf-arch-card tf-arch-card--ops">
            <span class="tf-arch-card-title">运营驾驶舱</span>
            <span class="tf-arch-card-tip">运营数据可视化</span>
          </div>
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

=== ":octicons-stack-16: DCE 云原生操作系统"

    DaoCloud Enterprise (DCE) 是一款高性能、可扩展的云原生操作系统，
    是[经 CNCF 认证的 Kubernetes - AI Platform](./dce/kcsp.md)。
    它能够在任何基础设施和任意环境中提供一致、稳定的体验，支持异构云、边缘云和多云编排等。

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
          <a class="tf-arch-card tf-arch-card--compute" href="network/config/">
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

<div class="tf-cta" markdown>

[申请 DCE 社区免费体验](./dce/license0.md){ .md-button .md-button--primary }
[了解 d.run](drun/index.md){ .md-button .md-button--primary }
[Token 工厂概览](tf/index.md){ .md-button .md-button--primary }

</div>
