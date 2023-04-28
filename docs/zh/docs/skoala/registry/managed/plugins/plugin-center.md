# 插件中心

插件中心提供 Sentinel 治理和 Mesh 治理两种插件，支持通过用户界面实现可视化配置。安装插件后可以扩展微服务治理能力，满足不同场景下的业务诉求。

!!! info

    同一个注册中心实例不能同时开启这两种插件，但可以根据不同的场景进行切换。

![插件中心](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/managed/plugins/imgs/plugincenter01.png)

## Sentinel 治理

Sentinel 插件主要适用于传统微服务的治理场景，支持流控规则、熔断规则、热点规则、系统规则、授权规则等多种治理规则。

开启 Sentinel 治理插件后会创建一个 Sentinel 实例，需要为其设置资源配额、选择部署模式（单节点/高可用）和访问方式。

## Mesh 治理

Mesh 插件主要适用于云原生微服务的治理场景，提供虚拟服务、目标规则、网关规则、对等认证、请求身份认证、授权策略等治理规则。

开启 Mesh 治理插件需绑定一个网格实例，将微服务加入到网格中，并根据服务网格的要求配置边车等资源。
