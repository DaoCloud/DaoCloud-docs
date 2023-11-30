# 查看微服务详情

在服务列表页面点击微服务名称可以查看服务详情，进一步查看实例列表、订阅者、监控、接口列表、元数据、服务治理等信息。

## 实例列表

首先需要进入目标注册中心，在左侧导航栏点击`微服务列表`，点击目标微服务的名称，进入微服务详情页面后方可执行后续操作。

![进入微服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail01.png)

- 服务流量权重的调整

    提供流量权重控制的能力，同时开放服务流量的阈值保护，帮助用户更好的地保护服务服务提供者集群不被意外打垮。可以点击实例的编辑按钮，修改实例的权重。如果想增加实例的流量，可以将权重调大，如果不想实例接收流量，则可以将权重设为 0。

    ![调整权重](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail02.png)

- 实例上下线

    提供服务实例的上下线操作，在实例列表的操作列，可以点击实例的`上线`或者`下线`按钮。实例下线后状态会变为离线且不会被服务发现。

    ![上下线](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail03.png)

- 实例详情

    点击实例名称，可进入实例详情，查看实例的监控和元数据。

    ![实例详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail04.png)

    - 实例监控

        实例监控功能用于监控服务实例的状态，例如服务实例的请求数，错误率、响应耗时、请求率、CPU 指标、内存指标、读写速率、接收发送速率等指标的时序曲线。

        > 响应耗时中 p95 代表线上 95% 的请求耗时都小于某个时间。

        ![实例监控](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail05.png)

    - 实例元数据

        ![实例元数据](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail06.png)

## 订阅者

进入订阅者列表页面，可查看到订阅者的信息，包括 IP 和端口、客户端版本和应用名。

![订阅者](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail07.png)

## 服务监控

服务监控用于查看特定时间范围内，某个命名空间下微服务的运行状态，并且根据微服务的监控指标（请求数、错误率、响应耗时、请求率）初步判断是否出现异常。

> 在监控图表的右上角可以更改监控数据的时间范围。

![监控](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail08.png)

## 微服务元数据

提供多个维度的服务元数据，帮助用户存储自定义的信息。这些信息都是以 Key-Value 的数据结构存储，在控制台上会以 k1=v1,k2=v2 这样的格式展示。

在右侧点击`编辑`可以修改元数据。

![元数据](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail09.png)

## 微服务治理

开启微服务治理插件后，可以通过 YAML 文件或页面表单为服务创建虚拟服务、目标规则、网关规则等三种治理规则。有关微服务治理的更多说明，可参考[流量治理](../../../../mspider/user-guide/traffic-governance/README.md)。

![微服务治理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail10.png)

## 接口文档

接口文档显示服务对外暴露的 API 列表。点击右侧的`导入接口文档`可以手动录入 API，有地址导入和手工导入两种方式导入方式。

![接口文档](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/detail11.png)