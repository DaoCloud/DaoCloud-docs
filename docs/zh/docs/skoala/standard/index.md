---
hide:
  - toc
---

# 服务对接规范

本节介绍传统微服务接入微服务引擎托管注册中心时需要遵循的对接规范。应用只有满足相应规范，才能正常使用微服务引擎提供的流量治理、数据监控等能力。

## 接入规范

<div class="grid cards" markdown>

- :material-account-group:{ .lg .middle } __服务接入 Nacos SDK__

    ---

    介绍不同框架的传统微服务如何接入 Nacos 的原生 SDK，实现服务注册与发现。

    [:octicons-arrow-right-24: 开始使用](nacos.md)

- :material-format-list-bulleted:{ .lg .middle } __服务接入 Sentinel 规范__

    ---

    介绍应用接入 Sentinel 控制台时需要满足的参数规范，以正常使用 Sentinel 流量治理和数据监控能力。

    [:octicons-arrow-right-24: 开始使用](sentinel.md)

- :material-hub:{ .lg .middle } __服务接入 Sentinel 监控__

    ---

    介绍传统微服务接入 Sentinel 监控功能的方法，涵盖依赖项、javaagent 参数和 Kubernetes Service 配置。

    [:octicons-arrow-right-24: 开始使用](monitor.md)

- :material-swap-horizontal:{ .lg .middle } __服务接入 Sentinel 集群流控__

    ---

    介绍服务接入 Sentinel 集群流控时服务器和客户端两方面的配置调整方法。

    [:octicons-arrow-right-24: 开始使用](flow-control.md)

</div>
