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
    <div class="tf-arch-layer-label">开箱即用的功能模块</div>
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

## 客户成功故事

<style>
/* 客户成功故事卡片 */
.md-typeset .story-marquee{display:grid;margin:1.2rem 0 2rem;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}
.md-typeset .story-track{display:flex;width:max-content;animation:story-move 70s linear infinite}
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

<div class="story-marquee" aria-label="客户成功故事">
  <div class="story-track">
    <div class="story-group">
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">AI 质量分析</span><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">东方电气</p><p class="story-card-desc">全球最大的能源装备制造企业集团之一，打造发电装备质量智能分析 AI 中台</p><div class="story-card-metrics"><span><b>10 倍</b>生产效率提升</span><span><b>30%</b>缺陷检测准确率</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">微服务平台</span><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">京东方</p><p class="story-card-desc">全球面板市场出货量第一，构建开放的数字化生态体系，29 套业务系统接入微服务平台</p><div class="story-card-metrics"><span><b>秒级</b>故障定位</span><span><b>70%</b>故障率降低</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">工业互联网</span><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">海尔集团</p><p class="story-card-desc">综合家电巨头，共建工业互联网平台 COSMOPlat，打造工业应用软件开发基础底座</p><div class="story-card-metrics"><span><b>30,000+</b>入驻企业</span><span><b>1,000+</b>上线应用</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">双态 IT</span><span class="story-card-ind">汽车</span></div>
        <div class="story-card-body"><p class="story-card-name">广汽丰田</p><p class="story-card-desc">世界 500 强车企子公司，应用上云实现双态 IT，生产计划与物流系统弹性部署</p><div class="story-card-metrics"><span><b>敏捷</b>应用高效迭代</span><span><b>深化</b>数字化转型</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">车联网平台</span><span class="story-card-ind">汽车</span></div>
        <div class="story-card-body"><p class="story-card-name">东风汽车</p><p class="story-card-desc">汽车行业“国家队”代表，打造满足新能源汽车监管和监控需求的平台</p><div class="story-card-metrics"><span><b>实时</b>海量车辆数据处理</span><span><b>加速</b>汽车数字化进程</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">容器集群上云</span><span class="story-card-ind">金融</span></div>
        <div class="story-card-body"><p class="story-card-name">华泰证券</p><p class="story-card-desc">中国领先的综合性证券集团，大规模标准容器集群上云</p><div class="story-card-metrics"><span><b>50%</b>运维效率提升</span><span><b>60%</b>部署效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">云原生支付</span><span class="story-card-ind">金融</span></div>
        <div class="story-card-body"><p class="story-card-name">浦发银行</p><p class="story-card-desc">全球银行前 20 强，中国首个支持大规模支付业务的云原生平台</p><div class="story-card-metrics"><span><b>10,000</b>支付峰值 TPS</span><span><b>99.99%</b>SLA</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">O+O 零售</span><span class="story-card-ind">消费</span></div>
        <div class="story-card-body"><p class="story-card-name">屈臣氏集团</p><p class="story-card-desc">全球最大的保健及美容产品零售商，端到端赋能 O+O 业务</p><div class="story-card-metrics"><span><b>99.99%</b>核心业务 SLA</span><span><b>70%+</b>发布耗时缩短</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">AI 代码审核</span><span class="story-card-ind">海外</span></div>
        <div class="story-card-body"><p class="story-card-name">汽车零部件系统供应商</p><p class="story-card-desc">全球领先的汽车与摩托车零部件系统供应商，以 d.run 打造 AI 智能代码审核应用</p><div class="story-card-metrics"><span><b>90%</b>人力投入削减</span><span><b>10 倍</b>审核效率提升</span></div></div>
      </div>
    </div>
    <div class="story-group" aria-hidden="true">
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">AI 质量分析</span><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">东方电气</p><p class="story-card-desc">全球最大的能源装备制造企业集团之一，打造发电装备质量智能分析 AI 中台</p><div class="story-card-metrics"><span><b>10 倍</b>生产效率提升</span><span><b>30%</b>缺陷检测准确率</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">微服务平台</span><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">京东方</p><p class="story-card-desc">全球面板市场出货量第一，构建开放的数字化生态体系，29 套业务系统接入微服务平台</p><div class="story-card-metrics"><span><b>秒级</b>故障定位</span><span><b>70%</b>故障率降低</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">工业互联网</span><span class="story-card-ind">制造</span></div>
        <div class="story-card-body"><p class="story-card-name">海尔集团</p><p class="story-card-desc">综合家电巨头，共建工业互联网平台 COSMOPlat，打造工业应用软件开发基础底座</p><div class="story-card-metrics"><span><b>30,000+</b>入驻企业</span><span><b>1,000+</b>上线应用</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">双态 IT</span><span class="story-card-ind">汽车</span></div>
        <div class="story-card-body"><p class="story-card-name">广汽丰田</p><p class="story-card-desc">世界 500 强车企子公司，应用上云实现双态 IT，生产计划与物流系统弹性部署</p><div class="story-card-metrics"><span><b>敏捷</b>应用高效迭代</span><span><b>深化</b>数字化转型</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">车联网平台</span><span class="story-card-ind">汽车</span></div>
        <div class="story-card-body"><p class="story-card-name">东风汽车</p><p class="story-card-desc">汽车行业“国家队”代表，打造满足新能源汽车监管和监控需求的平台</p><div class="story-card-metrics"><span><b>实时</b>海量车辆数据处理</span><span><b>加速</b>汽车数字化进程</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">容器集群上云</span><span class="story-card-ind">金融</span></div>
        <div class="story-card-body"><p class="story-card-name">华泰证券</p><p class="story-card-desc">中国领先的综合性证券集团，大规模标准容器集群上云</p><div class="story-card-metrics"><span><b>50%</b>运维效率提升</span><span><b>60%</b>部署效率提升</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">云原生支付</span><span class="story-card-ind">金融</span></div>
        <div class="story-card-body"><p class="story-card-name">浦发银行</p><p class="story-card-desc">全球银行前 20 强，中国首个支持大规模支付业务的云原生平台</p><div class="story-card-metrics"><span><b>10,000</b>支付峰值 TPS</span><span><b>99.99%</b>SLA</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">O+O 零售</span><span class="story-card-ind">消费</span></div>
        <div class="story-card-body"><p class="story-card-name">屈臣氏集团</p><p class="story-card-desc">全球最大的保健及美容产品零售商，端到端赋能 O+O 业务</p><div class="story-card-metrics"><span><b>99.99%</b>核心业务 SLA</span><span><b>70%+</b>发布耗时缩短</span></div></div>
      </div>
      <div class="story-card" style="--s1:#1B66F5;--s2:#5B8CFF">
        <div class="story-card-top"><span class="story-card-high">AI 代码审核</span><span class="story-card-ind">海外</span></div>
        <div class="story-card-body"><p class="story-card-name">汽车零部件系统供应商</p><p class="story-card-desc">全球领先的汽车与摩托车零部件系统供应商，以 d.run 打造 AI 智能代码审核应用</p><div class="story-card-metrics"><span><b>90%</b>人力投入削减</span><span><b>10 倍</b>审核效率提升</span></div></div>
      </div>
    </div>
  </div>
</div>

## 产品架构

![DCE 产品架构](images/architecture.svg)

## 安装和视频教程

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up:{ .lg .middle } __安装__

    ---

    支持[离线](../install/community/k8s/offline.md)和[在线](../install/community/k8s/online.md)两种安装方式，
    可以安装到[不同的 Linux 发行版](../install/os-install/uos-v20-install-dce5.0.md)。

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
    <span class="dce-path-desc">离线或在线安装 DCE</span>
    <span class="dce-path-go">Go →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#00acc1" href="../kpanda/intro/">
    <span class="dce-path-num">2</span>
    <span class="dce-path-title">管理集群</span>
    <span class="dce-path-desc">接入集群，统一容器编排调度</span>
    <span class="dce-path-go">Go →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#43a047" href="../amamba/intro/">
    <span class="dce-path-num">3</span>
    <span class="dce-path-title">交付应用</span>
    <span class="dce-path-desc">流水线与 GitOps 持续交付</span>
    <span class="dce-path-go">Go →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#fb8c00" href="../insight/intro/">
    <span class="dce-path-num">4</span>
    <span class="dce-path-title">观测系统</span>
    <span class="dce-path-desc">指标、日志、链路统一观测</span>
    <span class="dce-path-go">Go →</span>
  </a>
  <a class="dce-path-step" style="--path-c:#8e24aa" href="../ghippo/intro/">
    <span class="dce-path-num">5</span>
    <span class="dce-path-title">管控平台</span>
    <span class="dce-path-desc">用户权限与全局安全治理</span>
    <span class="dce-path-go">Go →</span>
  </a>
</div>

[申请社区免费体验](./license0.md){ .md-button }
[最佳实践](./bphome.md){ .md-button }
[常见问题](./faq.md){ .md-button }
[查阅 DaoCloud Enterprise 彩页](https://harbor-test2.cn-sh2.ufileos.com/docs/download/dce.pdf){ .md-button }
{: .tf-footer-cta }
