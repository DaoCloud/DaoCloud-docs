---
hide:
  - toc
---

# Token 工厂

Token 工厂是 DaoCloud 面向 AI 智算场景打造的一体化平台，围绕大模型推理、算力调度和集群运维提供端到端能力支撑。
平台采用 **用户** 与 **管理员** 双视图架构：用户视图面向终端用户，提供大模型服务调用、费用管理和智能应用接入能力；管理员视图面向运维管理团队，提供模型托管、推理引擎、基础设施和全局运营的统一管控。
[查看/下载 Token 工厂彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/tf.pdf){ .md-button }

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
    <div class="tf-arch-layer-label">云原生 AI</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="hydra/">
        <span class="tf-arch-card-title">大模型服务平台</span>
        <span class="tf-arch-card-tip">模型部署与运维管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="dak/">
        <span class="tf-arch-card-title">AI 应用</span>
        <span class="tf-arch-card-tip">智能问答等应用能力</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="inferx/">
        <span class="tf-arch-card-title">推理加速服务</span>
        <span class="tf-arch-card-tip">推理加速与引擎管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="zestu/">
        <span class="tf-arch-card-title">算力云</span>
        <span class="tf-arch-card-tip">异构算力纳管与调度</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
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
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">运营管理</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="copilot/">
        <span class="tf-arch-card-title">Copilot</span>
        <span class="tf-arch-card-tip">智能运维助手</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="crane/intro/">
        <span class="tf-arch-card-title">驾驶舱</span>
        <span class="tf-arch-card-tip">运营数据可视化</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="leopard/">
        <span class="tf-arch-card-title">费用中心</span>
        <span class="tf-arch-card-tip">计费与账单分析</span>
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

作为面向智算中心打造的高效能 AI Token 生产及经营系统，Token 工厂助力传统算力中心向高效、可盈利的 Token 生产运营模式升级。
平台统一纳管英伟达及国产异构算力，依靠智能调度与推理优化，把分散 GPU 算力转化为低成本、高稳定、可交易的标准化 Token 服务；
依托 Token 工厂管家与统一运营体系，完成资源、生产、成本、供需的全局管控，面向终端用户、管理员、运营者、运维者提供能力，
推动智算中心业务定位从 "提供算力" 升级为 "生产和运营 Token"。

![d.run Token 工厂效能平台全景图](images/tf-modules.svg)

## 学习路径

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
    <span class="tf-path-title">部署平台</span>
    <span class="tf-path-desc">离线安装 Token 工厂，完成初始化与授权</span>
    <span class="tf-path-go">前往 →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#00acc1" href="kpanda/intro/">
    <span class="tf-path-num">2</span>
    <span class="tf-path-title">纳管算力</span>
    <span class="tf-path-desc">接入 GPU 节点，创建工作集群</span>
    <span class="tf-path-go">前往 →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#43a047" href="hydra/">
    <span class="tf-path-num">3</span>
    <span class="tf-path-title">部署模型</span>
    <span class="tf-path-desc">模型广场选型，一键部署推理服务</span>
    <span class="tf-path-go">前往 →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#fb8c00" href="dak/">
    <span class="tf-path-num">4</span>
    <span class="tf-path-title">构建应用</span>
    <span class="tf-path-desc">搭建语料库与智能问答应用</span>
    <span class="tf-path-go">前往 →</span>
  </a>
  <a class="tf-path-step" style="--path-c:#8e24aa" href="crane/intro/">
    <span class="tf-path-num">5</span>
    <span class="tf-path-title">运营结算</span>
    <span class="tf-path-desc">驾驶舱看运营，费用中心管计费</span>
    <span class="tf-path-go">前往 →</span>
  </a>
</div>

[下载 Token 工厂离线包](https://docs.daocloud.io/download/tf/){ .md-button }
[安装 Token 工厂](install/index.md){ .md-button }
[查看/下载 Token 工厂彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/tf.pdf){ .md-button }
{: .tf-footer-cta }
