# 组件监控

!!! note

    集群中需要[安装 insight-agent 组件](../../../../insight/quickstart/install/install-agent.md)后才能使用监控功能。


微服务引擎通过内置 Grafana 提供全方位的监控功能，覆盖各个微服务、系统组件、以及服务调用链路等监控对象。其中，组件监控功能可以提供对 Nacos 和 Sentinel 的监控信息，包括节点数、服务数、CPU/内存用量、JVM 线程数、http 请求总耗时等多个维度的信息。

查看组件监控的步骤如下：

1. 进入微服务引擎模块，点击目标注册中心的名称。

    ![点击名称](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/managed/monitor/imgs/monitor01.png)

2. 在左侧导航栏点击`监控`->`组件监控`。

    ![导航栏](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/managed/monitor/imgs/monitor02.png)

3. 点击 `Naocs 实例`页签即可查看 Nacos 实例的监控信息。

    > 下拉页面可查看请求耗时、请求次数等统计详情。在页面右上角可切换统计时间窗口和刷新周期。

    ![查看信息](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/managed/monitor/imgs/monitor03.png)
