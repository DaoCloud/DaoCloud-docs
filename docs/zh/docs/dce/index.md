---
hide:
  - toc
---

# DaoCloud Enterprise 文档导航

DaoCloud Enterprise (DCE) 以 K8s 作为开发底座，提供了高度可扩展、强大灵活的各项生产级功能，使得企业能够轻松构建和管理分布式应用。
借助 DCE 的云原生天赋，企业可以充分利用云上云下优势，实现资源的最优利用，提高 IT 系统的可靠性和弹性，极大地加速应用的交付速度。

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
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">云原生底座</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="../middleware/">
        <span class="tf-arch-card-title">中间件</span>
        <span class="tf-arch-card-tip">数据库与消息队列</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kairship/intro/">
        <span class="tf-arch-card-title">多云编排</span>
        <span class="tf-arch-card-tip">多云与混合云编排</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kangaroo/intro/">
        <span class="tf-arch-card-title">镜像仓库</span>
        <span class="tf-arch-card-tip">镜像托管与集成</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../mspider/intro/">
        <span class="tf-arch-card-title">服务网格</span>
        <span class="tf-arch-card-tip">非侵入式服务治理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../skoala/intro/">
        <span class="tf-arch-card-title">微服务引擎</span>
        <span class="tf-arch-card-tip">微服务治理与网关</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../amamba/intro/">
        <span class="tf-arch-card-title">应用工作台</span>
        <span class="tf-arch-card-tip">CI/CD 与应用交付</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kpanda/intro/">
        <span class="tf-arch-card-title">容器管理</span>
        <span class="tf-arch-card-tip">集群与工作负载管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../virtnest/intro/">
        <span class="tf-arch-card-title">虚拟机</span>
        <span class="tf-arch-card-tip">KubeVirt 虚拟机管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../topohub/intro/">
        <span class="tf-arch-card-title">设备管理</span>
        <span class="tf-arch-card-tip">硬件设备统一纳管</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../kant/intro/">
        <span class="tf-arch-card-title">云边协同</span>
        <span class="tf-arch-card-tip">边缘节点纳管与协同</span>
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
  <div class="tf-arch-arrow">▲</div>
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

## 产品架构

![DCE 5.0 产品架构](images/architecture.svg)

## 安装和教程

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up:{ .lg .middle } __安装__

    ---

    DCE 支持[离线](../install/community/k8s/offline.md)和[在线](../install/community/k8s/online.md)两种安装方式，
    可以安装到[不同的 Linux 发行版上](../install/os-install/uos-v20-install-dce5.0.md)。

    - [安装依赖项](../install/install-tools.md)
    - [安装社区版](../install/community/resources.md)
    - [安装商业版](../install/commercial/deploy-requirements.md)
    - [安装到各种 Linux 发行版](../install/os-install/uos-v20-install-dce5.0.md)
    - [安装到不同 K8s 版本](../install/k8s-install/ocp-install-dce5.0.md)

- :material-microsoft-azure-devops:{ .lg .middle } __视频教程__

    ---

    我们为 DCE 的各个模块和场景制作了精良的[视频教程](../videos/index.md)。

    - [场景化视频](../videos/use-cases.md)
    - [应用工作台视频](../videos/amamba.md)
    - [容器管理视频](../videos/kpanda.md)
    - [微服务视频](../videos/skoala.md)
    - [中间件视频](../videos/mcamel.md)
    - [全局管理视频](../videos/ghippo.md)

</div>

## 学习路径

<style>
.dce-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.dce-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.dce-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.dce-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.dce-path-step:last-child::after{display:none}
.dce-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.dce-path-title{font-weight:700;font-size:0.95rem}
.dce-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.dce-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.dce-path-step::after{display:none}}
</style>

<div class="dce-path">
  <a class="dce-path-step" style="--path-c:#2196f3" href="../install/">
    <span class="dce-path-num">1</span>
    <span class="dce-path-title">部署平台</span>
    <span class="dce-path-desc">离线或在线安装 DCE 5.0</span>
    <span class="dce-path-go">前往 →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#00acc1" href="../kpanda/intro/">
    <span class="dce-path-num">2</span>
    <span class="dce-path-title">管理集群</span>
    <span class="dce-path-desc">接入集群，统一容器编排调度</span>
    <span class="dce-path-go">前往 →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#43a047" href="../amamba/intro/">
    <span class="dce-path-num">3</span>
    <span class="dce-path-title">交付应用</span>
    <span class="dce-path-desc">流水线与 GitOps 持续交付</span>
    <span class="dce-path-go">前往 →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#fb8c00" href="../insight/intro/">
    <span class="dce-path-num">4</span>
    <span class="dce-path-title">观测系统</span>
    <span class="dce-path-desc">指标、日志、链路统一观测</span>
    <span class="dce-path-go">前往 →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#8e24aa" href="../ghippo/intro/">
    <span class="dce-path-num">5</span>
    <span class="dce-path-title">管控平台</span>
    <span class="dce-path-desc">用户权限与全局安全治理</span>
    <span class="dce-path-go">前往 →</span>
  </a>
</div>

[申请社区免费体验](./license0.md){ .md-button }
[最佳实践](./bphome.md){ .md-button }
[常见问题](./faq.md){ .md-button }
[查阅 DaoCloud Enterprise 彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/dce.pdf){ .md-button }
