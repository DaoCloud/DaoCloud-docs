---
hide:
  - toc
---

# 微服务引擎

「DaoCloud 道客」微服务引擎是面向业界主流微服务生态的一站式微服务管理平台，主要提供微服务治理中心和微服务网关两个维度的功能，
具体包括服务注册发现、配置管理、流量治理、服务级别的链路追踪、API 管理、域名管理、监控告警等，覆盖了微服务生命周期中的各种管理场景。
微服务引擎具有很强的兼容性，不仅可以无缝对接 DaoCloud 的其他组件，也可以完美兼容 Spring Cloud、Dubbo 等开源生态，
帮助您更便捷地使用开源微服务技术构建自己的微服务体系。

## 产品全景

<style>
.tf-arch-card{min-width:calc(25% - 10px) !important}
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
    <div class="tf-arch-layer-label">南北向流量 · 微服务网关</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--model" href="../gateway/">
        <span class="tf-arch-card-title">网关管理</span>
        <span class="tf-arch-card-tip">多集群网关实例全生命周期管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../gateway/api/">
        <span class="tf-arch-card-title">API 管理</span>
        <span class="tf-arch-card-tip">API 策略与安全认证</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../gateway/domain/">
        <span class="tf-arch-card-title">域名管理</span>
        <span class="tf-arch-card-tip">域名与策略配置</span>
      </a>
      <a class="tf-arch-card tf-arch-card--model" href="../gateway/alert/">
        <span class="tf-arch-card-title">监控告警</span>
        <span class="tf-arch-card-tip">资源与业务双维监控</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">东西向流量 · 云原生微服务</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="../cloud-ms/traffic-control/">
        <span class="tf-arch-card-title">服务治理</span>
        <span class="tf-arch-card-tip">Mesh 与 Istio 流量治理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../cloud-ms/lane/">
        <span class="tf-arch-card-title">流量泳道</span>
        <span class="tf-arch-card-tip">全链路灰度发布</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../standard/monitor/">
        <span class="tf-arch-card-title">Sentinel 监控</span>
        <span class="tf-arch-card-tip">流控规则效果观测</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--compute">
    <div class="tf-arch-layer-label">东西向流量 · 传统微服务</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--compute" href="../trad-ms/hosted/">
        <span class="tf-arch-card-title">注册配置中心</span>
        <span class="tf-arch-card-tip">Nacos 托管与配置管理</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../trad-ms/integrated/">
        <span class="tf-arch-card-title">接入注册中心</span>
        <span class="tf-arch-card-tip">Eureka / ZooKeeper / Nacos / Consul</span>
      </a>
      <a class="tf-arch-card tf-arch-card--compute" href="../standard/sentinel/">
        <span class="tf-arch-card-title">接入 Sentinel</span>
        <span class="tf-arch-card-tip">流控、熔断降级、热点限流</span>
      </a>
    </div>
  </div>
  <div class="tf-arch-arrow">▲</div>
  <div class="tf-arch-layer tf-arch-layer--ops">
    <div class="tf-arch-layer-label">公共支撑</div>
    <div class="tf-arch-cards">
      <a class="tf-arch-card tf-arch-card--ops" href="../plugins/intro/">
        <span class="tf-arch-card-title">插件中心</span>
        <span class="tf-arch-card-tip">Wasm 插件与一键启停</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="features/">
        <span class="tf-arch-card-title">功能特性</span>
        <span class="tf-arch-card-tip">完整功能清单</span>
      </a>
      <a class="tf-arch-card tf-arch-card--ops" href="scenarios/">
        <span class="tf-arch-card-title">适用场景</span>
        <span class="tf-arch-card-tip">典型场景与产品优势</span>
      </a>
    </div>
  </div>
</div>

## 产品架构

![微服务引擎架构](../images/archi.svg)

## 文档导航

<div class="grid cards" markdown>

-   :material-run-fast:{ .lg .middle } __快速入门__

    ---

    - [微服务引擎管理组件](../quickstart/skoala.md)
    - [微服务引擎集群初始化组件](../quickstart/skoala-init.md)
    - [选择工作空间](../quickstart/select-workspace.md)
    - [skoala-init 故障排查](../troubleshoot/auth-server.md)

-   :material-connection:{ .lg .middle } __服务对接规范__

    ---

    - [接入 Sentinel](../standard/sentinel.md)
    - [接入 Nacos SDK](../standard/nacos.md)
    - [接入 Sentinel 监控](../standard/monitor.md)
    - [接入 Sentinel 集群流控](../standard/flow-control.md)

-   :fontawesome-solid-cubes-stacked:{ .lg .middle } __最佳实践__

    ---

    - [示例应用体验微服务治理](../best-practice/use-skoala-01.md)
    - [在云原生微服务中使用 JWT 插件](../best-practice/plugins/jwt.md)
    - [微服务网关接入认证服务器](../best-practice/auth-server.md)
    - [网关 API 策略](../best-practice/gateway02.md)

-   :material-engine:{ .lg .middle } __云原生微服务__

    ---

    - [导入/移除服务](../cloud-ms/traffic-control.md)
    - [服务治理](../cloud-ms/traffic-control.md)
    - [Nacos 压力测试报告](../tests/nacos-stress-test.md)

-   :material-gate:{ .lg .middle } __云原生网关__

    ---

    - [网关管理](../gateway/index.md)
    - [API 管理](../gateway/api/index.md)
    - [服务接入](../gateway/service/manual-integrate.md)
    - [监控告警](../gateway/alert.md)
    - [域名管理](../gateway/domain/index.md)
    - [网关压力测试报告](../tests/gateway-stress-test.md)

-   :simple-legacygames:{ .lg .middle } __传统微服务__

    ---

    - [注册配置中心](../trad-ms/hosted/index.md)
        - [微服务列表](../trad-ms/hosted/services/index.md)
        - [微服务配置管理](../trad-ms/hosted/configs.md)
        - [微服务监控](../trad-ms/hosted/monitor/microservices.md)
    - [接入注册中心](../trad-ms/integrated/index.md)
        - [微服务管理](../trad-ms/integrated/manage-service.md)
        - [链路追踪](../trad-ms/integrated/trace.md)

</div>

## 学习路径

<style>
.skoala-path{display:flex;gap:0.75rem;margin:1.25rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.skoala-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.skoala-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.skoala-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.skoala-path-step:last-child::after{display:none}
.skoala-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.skoala-path-title{font-weight:700;font-size:0.95rem}
.skoala-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.skoala-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.skoala-path-step::after{display:none}}
</style>

<div class="skoala-path">
  <a class="skoala-path-step" style="--path-c:#2196f3" href="../quickstart/skoala/">
    <span class="skoala-path-num">1</span>
    <span class="skoala-path-title">部署引擎组件</span>
    <span class="skoala-path-desc">安装微服务引擎管理组件</span>
    <span class="skoala-path-go">前往 →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#00acc1" href="../quickstart/skoala-init/">
    <span class="skoala-path-num">2</span>
    <span class="skoala-path-title">初始化托管组件</span>
    <span class="skoala-path-desc">安装集群初始化组件 skoala-init</span>
    <span class="skoala-path-go">前往 →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#43a047" href="../quickstart/select-workspace/">
    <span class="skoala-path-num">3</span>
    <span class="skoala-path-title">选择工作空间</span>
    <span class="skoala-path-desc">为微服务和网关划定管理边界</span>
    <span class="skoala-path-go">前往 →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#fb8c00" href="../trad-ms/integrated/">
    <span class="skoala-path-num">4</span>
    <span class="skoala-path-title">接入微服务</span>
    <span class="skoala-path-desc">接入注册中心，纳管传统与云原生微服务</span>
    <span class="skoala-path-go">前往 →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#8e24aa" href="../cloud-ms/traffic-control/">
    <span class="skoala-path-num">5</span>
    <span class="skoala-path-title">治理流量</span>
    <span class="skoala-path-desc">Sentinel / Mesh 治理东西向流量</span>
    <span class="skoala-path-go">前往 →</span>
  </a>
  <a class="skoala-path-step" style="--path-c:#e53935" href="../gateway/">
    <span class="skoala-path-num">6</span>
    <span class="skoala-path-title">配置网关</span>
    <span class="skoala-path-desc">创建网关实例，管理南北向 API</span>
    <span class="skoala-path-go">前往 →</span>
  </a>
</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
[查阅《微服务引擎用户手册》PDF](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/skoala.pdf){ .md-button }
