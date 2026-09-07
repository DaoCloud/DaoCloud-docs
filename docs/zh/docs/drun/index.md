---
hide:
  - toc
---

# d.run AI 操作系统

d.run 依托全球前三的 Kubernetes 调度技术与 vLLM 等主流开源推理引擎核心贡献积淀，统一纳管多元异构算力，
实现颗粒化调度、全栈推理优化与全链路 Token 治理，算力利用率超 80%，将算力高效转化为可管可控的 Token 化 AI 生产力；
平台汇聚全球主流大模型生态，配备可视化运营驾驶舱与 d.run Copilot 智能助手，面向企业全部门输出稳定高效的 AI 服务，
全方位支撑业务智能化长期升级。

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

<div class="tf-arch tf-arch--compact">
  <div class="tf-arch-layer tf-arch-layer--model">
    <div class="tf-arch-layer-label">云原生 AI</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="../clawos/intro/">
        <span class="tf-arch-card-title">ClawOS</span>
        <span class="tf-arch-card-tip">多智能体运行与治理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../hydra/">
        <span class="tf-arch-card-title">大模型服务平台</span>
        <span class="tf-arch-card-tip">模型部署与运维管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../baize/intro/">
        <span class="tf-arch-card-title">AI Lab</span>
        <span class="tf-arch-card-tip">云原生训推一体化</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../inferx/">
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
      <a class="tf-arch-card tf-arch-card--compute" href="../kpanda/intro/">
        <span class="tf-arch-card-title">容器管理</span>
        <span class="tf-arch-card-tip">集群与工作负载管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../topohub/intro/">
        <span class="tf-arch-card-title">设备管理</span>
        <span class="tf-arch-card-tip">硬件设备统一纳管</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kangaroo/intro/">
        <span class="tf-arch-card-title">镜像仓库</span>
        <span class="tf-arch-card-tip">镜像托管与集成</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../network/intro/">
        <span class="tf-arch-card-title">云原生网络</span>
        <span class="tf-arch-card-tip">多 CNI 融合网络</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../storage/">
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
      <a class="tf-arch-card tf-arch-card--ops" href="../insight/intro/">
        <span class="tf-arch-card-title">可观测性</span>
        <span class="tf-arch-card-tip">指标日志链路观测</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="../ghippo/intro/">
        <span class="tf-arch-card-title">全局管理</span>
        <span class="tf-arch-card-tip">用户权限与平台设置</span>
      </a>
    </div>
  </div>
</div>

作为面向企业输出的 AI 操作系统，d.run 将算力调度、大模型推理与运营治理融为一体。
平台统一纳管英伟达及国产异构算力，依靠颗粒化调度与全栈推理优化，把分散 GPU 算力转化为低成本、高稳定的 Token 服务；
配备可视化运营驾驶舱，实时呈现算力消耗、模型调用与 Token 产出全链路数据；
内置 d.run Copilot 智能助手，降低企业全部门使用 AI 的门槛，推动业务智能化长期升级。
