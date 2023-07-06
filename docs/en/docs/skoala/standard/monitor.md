# Service Integration with Sentinel Monitoring

This document describes how to integrate traditional microservices with the Sentinel monitoring feature.

1. Add Dependencies

    The version of the `sentinel metric exporter` SDK needs to be >= [v2.0.0-alpha](https://github.com/alibaba/Sentinel/releases/tag/2.0.0-alpha).

    ```xml
    <dependency>
      <groupId>com.alibaba.csp</groupId>
      <artifactId>sentinel-metric-exporter</artifactId>
      <version>v2.0.0-alpha</version>
    </dependency>
    ```

    If you want to understand the reasons behind it, you can refer to: [https://github.com/alibaba/Sentinel/pull/2976](https://github.com/alibaba/Sentinel/pull/2976)

2. When starting the service, add the `javaagent` parameter and set the JMX port to `12345`.

    ```
    -javaagent:/jmx_prometheus_javaagent-0.17.0.jar=12345:/prometheus-jmx-config.yaml
    ```
    For detailed information about JMX, you can refer to [Exposing JVM Monitoring Metrics using JMX Exporter](../../insight/quickstart/jvm-monitor/jmx-exporter.md).

3. Create a Kubernetes Service for your service. Pay attention to the following parameters:

    - `labels` field: Set it to `skoala.io/type: sentinel`.

    - `ports` field: Set it to `name: jmx-metrics`, `port: 12345`, `targetPort: 12345`.

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

!!! note
    
    If you want to understand the reasons behind it, you can refer to the definition of the ServiceMonitor CR.

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
