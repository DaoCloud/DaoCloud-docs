---
hide:
  -toc
---

# 创建集群流控规则

[流控规则](flow-control.md)、[熔断规则](circuit-breaker.md)、[授权规则](auth.md)、[热点规则](hotspot.md)和[系统规则](system.md)只能统计本地的资源调用信息，使用于单机应用。但是在如今的云原生时代下，很多应用都是部署在集群中，可能分布在不同的机器上。在分布式场景下，上述规则存在一些缺点。例如，路由到集群中每台机器的流量不均衡，可能尚未达到整个集群的阈值总和时，某一台机器就因此超出阈值而停止服务。

集群流控模式正是为了解决这种问题而设计的。在集群流控模式下，需要理解两个概念：

- TokenServer: 统计集群中所有实例的 QPS 并进行加总求和，将总值与集群整体阈值（单机阈值✖️机器数量）进行比较。如果尚未达到集群整体的阈值，则向客户端发送 Token。
- TokenClient：即应用分布在不同机器上的各个实例。客户端会向 TokenServer 请求 Token。如果能成功获得 Token，说明尚未达到整体阈值，该实例可以继续处理请求。如果不能获得 Token，表示已经达到了整体的阈值，对该实例的请求会直接失败。

!!! note

    - TokenSever 需要配置在 Nacos 的 `public` 命名空间，分组（Group）应为 `SENTINEL_GROUP`。
    - TokenSever 是单点的，一旦 TokenSever 宕机，集群流控模式就会退化成单机限流模式。

创建集群流控规则的方式如下：

1. 点击目标托管注册中心的名称，然后在左侧导航栏点击 __微服务列表__ ，在最右侧点击更多按钮选择 __治理__ 。

    > 注意需要治理的微服务在 __是否可以治理__ 一栏应该显示为`是`，才能进行后续步骤。

    ![微服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gov00.png)

2. 选择 __集群流控__ ，然后在右侧点击 __创建集群流控__ 。

    ![微服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gov17.png)

3. 参考下列说明填写规则配置，并在右下角点击 __确定__ 。

    - 服务器名称：Token 服务器的名称
    - TokenServer IP：Token 服务器的 IP 地址
    - TokenServer 端口：Token 服务器的端口号
    - Client 选择：集群流控客户端，用于向所属 TokenServer 通信请求 Token。

        ![微服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gov18.png)

4. 创建完成后可以在系统规则列表中查看新建的规则。在右侧点击更多按钮可以更新规则或者删除该规则。

    ![流控规则列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/gov19.png)
