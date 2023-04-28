# 微服务监控

微服务引擎通过内置 Grafana 提供全方位的监控功能，覆盖各个微服务、系统组件、以及服务调用链路等监控对象。其中，微服务监控功能可以提供对托管注册中心下各个微服务的监控信息，包括服务响应时间、并发量、异常 QPS、阻塞 QPS、通过 QPS、成功 QPS 等多个维度的信息。

!!! note

    集群中需要[安装 insight-agent 组件](../../../../insight/user-guide/quickstart/install-agent.md)后才能使用监控功能。

查看微服务监控的步骤如下：

1. 进入微服务引擎模块，点击目标注册中心的名称。

    ![点击名称](imgs/monitor01.png)

2. 在左侧导航栏点击`监控`->`微服务监控`。

    ![导航栏](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/managed/monitor/imgs/monitor04.png)

3. 选择对应的微服务命名空间即可查看该命名空间下的微服务监控数据。

    > 点击仪表盘名称可以进一步查看或分享该监控信息。在页面右上角可切换统计时间窗口和刷新周期。

    ![查看信息](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/managed/monitor/imgs/monitor05.png)