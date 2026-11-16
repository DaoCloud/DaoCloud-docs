---
hide:
  - toc
---

# 服务网格

服务网格是基于 Istio 开源技术构建的面向云原生应用的下一代服务网格，
通过提供完整的非侵入式微服务治理方案，统一治理多云多集群的复杂环境，
以基础设施的方式为用户提供服务流量治理、安全性治理、服务流量监控以及传统微服务（SpringCloud、Dubbo）功能。

服务网格兼容社区原生 Istio 开源服务网格，提供原生 Istio 接入管理能力。
在较高的层次上，服务网格有助于降低服务治理的复杂性，减轻开发运维团队的压力。
服务网格无缝对接[容器管理](../../kpanda/intro/index.md)平台，并作为基础设施为[微服务引擎](../../skoala/intro/index.md)提供容器微服务治理支持，方便用户通过单一平台对各类微服务系统做统一管理。

## 核心能力

<div class="grid cards" markdown>

- :material-lan:{ .lg .middle } __网格创建与管理__

    ---

    支持托管网格、专有网格、外接网格三种模式，覆盖网格创建、删除与容量管理，提供免运维的托管控制面。

    [:arrow_forward: 创建网格](../user-guide/service-mesh/index.md)

- :material-swap-horizontal:{ .lg .middle } __流量治理__

    ---

    通过虚拟服务、目标规则、网关规则配置权重、内容、TCP/IP 等路由策略，实现动态智能路由与弹性流量管理。

    [:arrow_forward: 流量治理](../user-guide/traffic-governance/README.md)

- :material-chart-line:{ .lg .middle } __流量监控__

    ---

    可视化展现链路信息、服务异常响应、超长响应时延等指标，结合流量拓扑快速定位问题。

    [:arrow_forward: 流量监控](../user-guide/traffic-monitor/README.md)

- :material-shield-check:{ .lg .middle } __安全治理__

    ---

    提供对等身份认证、请求身份认证与授权策略，通过 mTLS 保障服务间通信安全。

    [:arrow_forward: 安全治理](../user-guide/security/README.md)

- :material-car-outline:{ .lg .middle } __边车管理__

    ---

    按命名空间或工作负载注入边车，支持边车资源优化、流量透传与日志级别调整。

    [:arrow_forward: 边车管理](../user-guide/sidecar-management/ns-sidecar.md)

- :material-gate:{ .lg .middle } __网格网关__

    ---

    创建并管理网格网关实例，为网格内服务提供统一的南北向流量入口。

    [:arrow_forward: 创建网关实例](../user-guide/gateway-instance/create.md)

</div>

## 使用流程

使用服务网格通常分为 **部署接入** 与 **治理观测** 两个阶段：管理员先安装模块、创建网格并纳管集群，业务用户随后注入边车，即可使用流量治理、安全治理与流量监控等治理能力。

```mermaid
flowchart LR
    A["① 安装部署<br/>部署服务网格模块"] --> B["② 创建网格<br/>托管 · 专有 · 外接"]
    B --> C["③ 纳管集群<br/>集群接入网格"]
    C --> D["④ 注入边车<br/>命名空间 · 工作负载"]
    D --> E["⑤ 治理与观测<br/>流量 · 安全 · 监控"]

    click A href "../install/install/"
    click B href "../user-guide/service-mesh/"
    click C href "../user-guide/cluster-management/join-clus/"
    click D href "../user-guide/sidecar-management/ns-sidecar/"
    click E href "../user-guide/traffic-governance/"
```

| 步骤 | 角色 | 说明 |
| --- | --- | --- |
| ① [安装部署](../install/install.md) | 平台管理员 | 在集群中部署服务网格模块 |
| ② [创建网格](../user-guide/service-mesh/index.md) | 平台管理员 | 创建托管、专有或外接模式的网格 |
| ③ [纳管集群](../user-guide/cluster-management/join-clus.md) | 平台管理员 | 将一个或多个集群接入网格统一管理 |
| ④ [注入边车](../user-guide/sidecar-management/ns-sidecar.md) | 业务用户 | 按命名空间或工作负载注入边车代理 |
| ⑤ [流量治理](../user-guide/traffic-governance/README.md)与[流量监控](../user-guide/traffic-monitor/README.md) | 业务用户 | 配置路由与安全策略，实时监控服务运行状态 |

## 产品优势

服务网格相比其他产品具备以下优势：

| 优势 | 说明 |
| ---- | ---- |
| 简单易用 | 无需修改任何业务代码，也无需手动安装代理，开启服务网格功能即可体验无侵入服务治理 |
| 策略化的智能路由与弹性流量管理 | 权重、内容、TCP/IP 等路由规则；HTTP 会话保持；限流与离群检测；网络长连接管理；服务安全认证、鉴权、审计 |
| 图形化应用全景拓扑 | 链路信息、服务异常响应、超长响应时延等可视化监控，结合调用链信息更快定位问题 |
| 性能增强、可靠性增强 | 控制面和数据面基于社区版本进行加固和性能优化 |
| 多云多集群、多基础设施 | 免运维托管控制面，全局统一服务治理、安全与监控；统一服务发现和管理容器与虚拟机（VM）等多种基础设施 |
| 协议扩展 | 支持 Dubbo 协议 |
| 传统 SDK 集成 | Spring Cloud、Dubbo 等传统微服务 SDK 业务无需大量代码改造即可迁移到云原生网格环境运行 |

## 快速上手

<style>
.mspider-path{display:flex;gap:0.75rem;margin:1rem 0 1.75rem;align-items:stretch;flex-wrap:wrap}
.mspider-path-step{flex:1 1 165px;min-width:160px;display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem 0.9rem;border:1px solid var(--md-default-fg-color--lightest);border-top:3px solid var(--path-c,#2196f3);border-radius:12px;background:linear-gradient(180deg,rgba(33,150,243,0.04),transparent);color:inherit!important;text-decoration:none!important;position:relative;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
.mspider-path-step:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(0,0,0,0.10);border-color:var(--path-c,#2196f3)}
.mspider-path-step::after{content:"›";position:absolute;right:-0.65rem;top:50%;transform:translateY(-50%);font-size:1.35rem;font-weight:700;color:var(--md-default-fg-color--light);z-index:1}
.mspider-path-step:last-child::after{display:none}
.mspider-path-num{width:1.55rem;height:1.55rem;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.78rem;font-weight:700;color:#fff;background:var(--path-c,#2196f3)}
.mspider-path-title{font-weight:700;font-size:0.95rem}
.mspider-path-desc{font-size:0.78rem;color:var(--md-default-fg-color--light);line-height:1.5}
.mspider-path-go{margin-top:auto;font-size:0.75rem;font-weight:600;color:var(--path-c,#2196f3)}
@media screen and (max-width: 768px){.mspider-path-step::after{display:none}}
</style>

<div class="mspider-path">
  <a class="mspider-path-step" style="--path-c:#2196f3" href="../install/install/">
    <span class="mspider-path-num">1</span>
    <span class="mspider-path-title">安装部署</span>
    <span class="mspider-path-desc">部署服务网格模块</span>
    <span class="mspider-path-go">Go →</span>
  </a>
  <a class="mspider-path-step" style="--path-c:#00acc1" href="../user-guide/service-mesh/">
    <span class="mspider-path-num">2</span>
    <span class="mspider-path-title">创建网格</span>
    <span class="mspider-path-desc">托管 · 专有 · 外接</span>
    <span class="mspider-path-go">Go →</span>
  </a>
  <a class="mspider-path-step" style="--path-c:#43a047" href="../user-guide/cluster-management/join-clus/">
    <span class="mspider-path-num">3</span>
    <span class="mspider-path-title">纳管集群</span>
    <span class="mspider-path-desc">集群接入网格</span>
    <span class="mspider-path-go">Go →</span>
  </a>
  <a class="mspider-path-step" style="--path-c:#fb8c00" href="../user-guide/sidecar-management/ns-sidecar/">
    <span class="mspider-path-num">4</span>
    <span class="mspider-path-title">注入边车</span>
    <span class="mspider-path-desc">命名空间 · 工作负载</span>
    <span class="mspider-path-go">Go →</span>
  </a>
  <a class="mspider-path-step" style="--path-c:#8e24aa" href="../user-guide/traffic-governance/">
    <span class="mspider-path-num">5</span>
    <span class="mspider-path-title">治理与观测</span>
    <span class="mspider-path-desc">流量 · 安全 · 监控</span>
    <span class="mspider-path-go">Go →</span>
  </a>
</div>

## 更多资源

<div class="grid cards" markdown>

- :material-map-outline:{ .lg .middle } __产品架构__

    ---

    了解服务网格的整体架构、控制面组件与系统命名空间。

    [:arrow_forward: 查看产品架构](comp-archi-ui/index.md)

- :material-chat-question-outline:{ .lg .middle } __常见问题__

    ---

    服务网格使用过程中的常见问题与解决办法。

    [:arrow_forward: 查看常见问题](faq.md)

- :material-bug-outline:{ .lg .middle } __故障排查__

    ---

    持续更新的排障手册，覆盖创建网格、纳管集群、边车等常见故障案例。

    [:arrow_forward: 查看故障排查](../troubleshoot/index.md)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
[查阅《服务网格用户手册》PDF](https://harbor-test2.cn-sh2.ufileos.com/docs/download/docs/mspider.pdf){ .md-button }
