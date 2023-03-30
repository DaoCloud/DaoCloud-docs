# 应用接入 Sentinel 规范

为了正常使用 DCE 5.0 微服务引擎提供的 [Sentinel 流量治理](../plugins/sentinel.md)和查看 [Sentinel 数据监控](../monitor/components.md)，需要将应用接入 Sentinel 控制台，并且传递应用参数时需要满足一定规范。

## project.name 参数

project.name 参数的格式应为：`{{nacos_namespace_id}}@@{{nacos_group}}@@{{appName}}`。

**需要注意的是**：

- 符合此规范时，Sentinel 的治理规则会被推送到对应命名空间下，对应配置分组下的配置中心。

- 如果不符合此规范，比如只有 `appName` 或者 `{{nacos_group}}@@{{appName}}`，则所有治理规则都会被推送到 `public` 命名空间下的 `SENTINEL_GROUP` 配置中心。

- 第一部分 `{{nacos_namespace_id}}` 指的是 Nacos 命名空间的 **ID**，而非命名空间的名称。

- Nacos 的 `public` 命名空间对应的 ID 是空字符 “”。

- 如果想把应用接入 `public` 命名空间，必须使用空字符串，例如 `@@A@@appA`。

!!! note

    为了正常显示 Sentinel 监控数据，应使用 Sentinel 官方 SDK v1.8.6 **以上** 的版本。

??? note "如何获取 Sentinel 控制台"

    - 从 [release](https://github.com/alibaba/Sentinel/releases)页面下载最新版本的控制台 jar 包，或者

    - 从最新版本的源码自行构建 Sentinel 控制台

        1. 下载[控制台](https://github.com/alibaba/Sentinel/tree/master/sentinel-dashboard)工程
        2. 使用以下命令将代码打包成一个 fat jar: `mvn clean package`

    具体可参考官方文档：[启动控制台](https://sentinelguard.io/zh-cn/docs/dashboard.html)
