# 服务接入 Sentinel 监控

本文介绍如何为传统观念微服务接入 Sentinel 监控功能。

1. 添加依赖项

    `sentinel metric exporter` SDK 的版本需要 >=  [v2.0.0-alpha](https://github.com/alibaba/Sentinel/releases/tag/2.0.0-alpha)

    ```xml
    <dependency>
      <groupId>com.alibaba.csp</groupId>
      <artifactId>sentinel-metric-exporter</artifactId>
      <version>v2.0.0-alpha</version>
    </dependency>
    ```

    如需了解相关原因，可参考：https://github.com/alibaba/Sentinel/pull/2976

2. 启动服务时添加 `javaagent` 参数，且 JMX 端口固定为 `12345`

    ```
    -javaagent:/jmx_prometheus_javaagent-0.17.0.jar=12345:/prometheus-jmx-config.yaml
    ```

    有关 JMX 的详细说明，可参考[使用 JMX Exporter 暴露 JVM 监控指标](../../insight/quickstart/jvm-monitor/jmx-exporter.md)。

3. 为服务创建 Kubernetes Service。重点包括以下参数：

    - labels 字段：固定为 `skoala.io/type: sentinel`
    - ports 字段：固定为 `name: jmx-metrics`，`port: 12345`，`targetPort: 12345`

        ```yaml
        apiVersion: v1
        kind: Service
        metadata:
          labels:
            skoala.io/type: sentinel
          name: sentinel-demo
          namespace: skoala-jia
        spec:
          ports:
          - name: jmx-metrics
            port: 12345
            protocol: TCP
            targetPort: 12345
          selector:
            app.kubernetes.io/name: sentinel-demo
        ```

!!! note "如需了解相关原因，可参考 ServiceMonitor CR 的定义"

    ```yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      labels:
        release: insight-agent
        operator.insight.io/managed-by: insight
      name: sentinel-service-monitor
    spec:
      endpoints:
        - port: jmx-metrics
          scheme: http
      jobLabel: jobLabel
      namespaceSelector:
        any: true
      selector:
        matchLabels:
          skoala.io/type: sentinel
    ```
