---
hide:
  - toc
---

# DCE 文档导航

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

## 下载和开源生态

<div class="grid cards" markdown>

- :material-download:{ .lg .middle } __下载中心__
    
    ---

    下载中心包含了 DCE 社区版、商业版以及各个子模块的离线安装包。

    - [下载社区版](../download/free/dce5-installer-history.md)
    - [下载商业版](../download/business/dce5-installer-history.md)
    - [下载子模块](../download/index.md#_3)

- :simple-opensourceinitiative:{ .lg .middle } __DaoCloud 开源生态__
    
    ---

    DaoCloud 秉承开源企业文化，已有多项开源技术入选 CNCF Sandbox。

    - [Clusterpedia 多集群百科全书](../community/clusterpedia.md)
    - [HwameiStor 本地化存储](../community/hwameistor.md)
    - [Merbridge 服务网格加速](../community/merbridge.md)

</div>

*[Clusterpedia]: 内置在 DCE 中的多集群资源查询插件，捐献给 CNCF 后已入选 Sandbox
*[HwameiStor]: 内置在 DCE 中的本地高可用存储方案，捐献给 CNCF 后已入选 Sandbox
*[Merbridge]: 内置在 DCE 中基于 eBPF 构建的网格加速插件，捐献给 CNCF 后已入选 Sandbox

!!! success

    ```yaml
    是什么让一个企业走向成功？
      是方向一致的梦想，
        是开源分享的喜悦，
          是日夜贡献成功构建魔法后的欣喜若狂。
    
    让我们一起，
      致敬曾经、现在和未来的努力吧！
    ```

[申请社区免费体验](./license0.md){ .md-button .md-button--primary }
[最佳实践](./bphome.md){ .md-button .md-button--primary }
[常见问题](./faq.md){ .md-button .md-button--primary }
