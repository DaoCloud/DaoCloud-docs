---
hide:
  - toc
---

# 服务接入 Sentinel 规范

为了正常使用 DCE 5.0 微服务引擎提供的 [Sentinel 流量治理](../trad-ms/hosted/plugins/sentinel.md)和查看 [Sentinel 数据监控](../trad-ms/hosted/monitor/components.md)，需要将应用接入 Sentinel 控制台，并且传递应用参数时需要满足一定规范。

## 微服务中引入 Sentinel 相关 SDK

`pom.xml` 文件中加入相关引用，常见的 SDK 如下：

```
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-sentinel</artifactId>
        </dependency>

        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-datasource-nacos</artifactId>
        </dependency>

        <dependency>
            <groupId>com.alibaba.csp</groupId>
            <artifactId>sentinel-core</artifactId>
            <version>2.0.0-alpha</version>
        </dependency>
```

## bootstrap.yml 配置文件中注意如下设置

project.name 参数的格式应为：`{{nacos_namespace_id}}@@{{nacos_group}}@@{{appName}}`。

```yaml
---
project:
  # 服务注册在sentinel中的名称, 建议与nacos注册服务名相同
  name: ${spring.cloud.nacos.discovery.namespace}@@${spring.cloud.nacos.discovery.group}@@${spring.application.name}
```

**需要注意的是**：

- 符合此规范时，Sentinel 的治理规则会被推送到对应命名空间下，对应配置分组下的配置中心。

- 如果不符合此规范，比如只有 `appName` 或者 `{{nacos_group}}@@{{appName}}`，则所有治理规则都会被推送到 `public` 命名空间下的 `SENTINEL_GROUP` 配置中心。

- 第一部分 `{{nacos_namespace_id}}` 指的是 Nacos 命名空间的 **ID**，而非命名空间的名称。

- Nacos 的 `public` 命名空间对应的 ID 是空字符 “”。

- 如果想把应用接入 `public` 命名空间，必须使用空字符串，例如 `@@A@@appA`。

## Sentinel 接入配置

```yaml
---
spring:
  cloud:
    sentinel:
      enabled: false
      # 是否开启预加载, 设置为true时实例启动后自动在sentinel dashboard中展示, 设置为false, 需要实例有流量后该实例才会出现在sentinel dashboard中
      eager: true
      transport:
        # 配置sentinel dashboard地址
        dashboard: 10.6.222.24:31165
      # 以下配置为规则存放在nacos配置中心的相关参数
      datasource:
        flow:
          nacos:
            server-addr: ${spring.cloud.nacos.config.server-addr}
            dataId: ${spring.application.name}-flow-rules
            groupId: ${spring.cloud.nacos.discovery.group}
            namespace: ${spring.cloud.nacos.discovery.namespace}
            ruleType: flow
        degrade:
          nacos:
            server-addr: ${spring.cloud.nacos.config.server-addr}
            dataId: ${spring.application.name}-degrade-rules
            groupId: ${spring.cloud.nacos.discovery.group}
            namespace: ${spring.cloud.nacos.discovery.namespace}
            rule-type: degrade
        system:
          nacos:
            server-addr: ${spring.cloud.nacos.config.server-addr}
            dataId: ${spring.application.name}-system-rules
            groupId: ${spring.cloud.nacos.discovery.group}
            namespace: ${spring.cloud.nacos.discovery.namespace}
            rule-type: system
        authority:
          nacos:
            server-addr: ${spring.cloud.nacos.config.server-addr}
            dataId: ${spring.application.name}-authority-rules
            groupId: ${spring.cloud.nacos.discovery.group}
            namespace: ${spring.cloud.nacos.discovery.namespace}
            rule-type: authority
        param-flow:
          nacos:
            server-addr: ${spring.cloud.nacos.config.server-addr}
            dataId: ${spring.application.name}-param-flow-rules
            groupId: ${spring.cloud.nacos.discovery.group}
            namespace: ${spring.cloud.nacos.discovery.namespace}
            rule-type: param-flow

```

!!! note

    为了正常显示 Sentinel 监控数据，应使用 Sentinel 官方 SDK v1.8.6 **以上** 的版本。如未能显示监控数据，可查看 Sentinel 的版本是否符合要求。
