---
hide:
  - toc
---

# 微服务管理

[接入注册中心](index.md)之后，可以通过注册中心对其中的微服务进行管理。微服务管理主要指查看注册中心下的微服务，

!!! note

    接入型注册中心仅支持基础的管理操作。对于更复杂的管理场景，建议创建[托管注册中心](../hosted/index.md)以便执行更多高级操作。

1. 在`接入注册中心列表`页面点击目标注册中心的名称。

    ![点击注册中心名称](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/service01.png)

2. 在左侧导航栏点击`微服务管理`，查看微服务列表和基本信息。

    在当前页面，可以复制微服务的名称，可以查看当前注册中心下的所有微服务，以及各个微服务的所属命名空间、实例情况、请求统计数据等。

    ![点击注册中心名称](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/service02.png)

3. 点击微服务的名称，查看微服务的实例列表、接口列表、监控信息等。

    ![点击注册中心名称](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/service03.png)

    - 实例列表：查看实例状态、IP 地址、服务端口等。

        点击实例名称，还可以进一步查看该实例的监控信息和元数据。

        ![实例详情](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/integrated/imgs/service04.png)

    - 接口列表：查看微服务已经具有的接口，或者创建新的接口。

        ![实例详情](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/integrated/imgs/service05.png)

    - 监控信息：查看微服务的监控信息，包括请求数、错误率、响应耗时、请求率等。

        支持自定义时间范围。

        ![实例详情](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/integrated/imgs/service06.png)  
