---
hide:
  - toc
---

# 微服务引擎

「DaoCloud 道客」微服务引擎是面向业界主流微服务生态的一站式微服务管理平台，主要提供微服务治理中心和微服务网关两个维度的功能，
具体包括服务注册发现、配置管理、流量治理、服务级别的链路追踪、API 管理、域名管理、监控告警等，覆盖了微服务生命周期中的各种管理场景。
微服务引擎具有很强的兼容性，不仅可以无缝对接 DCE 5.0 的其他组件，也可以完美兼容 Spring Cloud、Dubbo 等开源生态，
帮助您更便捷地使用开源微服务技术构建自己的微服务体系。

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

-   :simple-amazonapigateway:{ .lg .middle } __云原生网关__

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

![微服务引擎架构](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/archi.png)
