---
hide:
  - toc
---

# 最佳实践

本节汇集了微服务引擎的最佳实践，涵盖微服务治理、云原生网关和注册中心的典型使用场景，全部基于真实环境验证，可作为生产落地的参考。

## 微服务与注册中心

<div class="grid cards" markdown>

- :material-school:{ .lg .middle } __示例应用体验微服务治理__

    ---

    通过示例应用体验微服务治理功能，覆盖注册中心、配置中心、云原生微服务与云原生网关。

    [:octicons-arrow-right-24: 开始体验](use-skoala-01.md)

- :material-account-group:{ .lg .middle } __Nacos 对接 LDAP 进行用户管理__

    ---

    通过 Nacos（微服务引擎中名为注册中心）对接 LDAP，实现统一的用户管理。

    [:octicons-arrow-right-24: 开始使用](nacos-ldap.md)

</div>

## 云原生网关

<div class="grid cards" markdown>

- :material-gate:{ .lg .middle } __通过网关访问服务__

    ---

    演示如何将微服务接入云原生网关，并通过网关访问该服务。

    [:octicons-arrow-right-24: 开始使用](gateway01.md)

- :material-api:{ .lg .middle } __网关 API 策略__

    ---

    借助真实的微服务应用，演示负载均衡、超时重试、黑白名单等十几项 API 策略的配置方法与实际效果。

    [:octicons-arrow-right-24: 开始使用](gateway02.md)

- :material-hub:{ .lg .middle } __网关对接服务网格__

    ---

    对接云原生网关与服务网格，通过网关访问网格内服务，并可正常使用虚拟服务、目标规则等全部流量治理能力。

    [:octicons-arrow-right-24: 开始使用](gateway-mesh.md)

- :material-format-list-bulleted:{ .lg .middle } __网关请求日志添加自定义属性__

    ---

    网关底层通过 contour 向 envoy 下发请求日志字段配置，本文演示如何添加自定义属性。

    [:octicons-arrow-right-24: 开始使用](add-custom-attributes.md)

- :material-swap-horizontal:{ .lg .middle } __HTTP 转 Dubbo 协议动态路由__

    ---

    基于 Pixiu 的协议转换能力，将 HTTP 协议转换为 Dubbo 协议，实现动态路由。

    [:octicons-arrow-right-24: 开始使用](http-to-dubbo.md)

</div>
