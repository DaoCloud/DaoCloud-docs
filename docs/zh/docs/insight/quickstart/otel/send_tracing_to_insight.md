# 向 Insight 发送链路数据

此文档主要描述客户应用如何自行将链路数据上报给 Insight。主要包含如下两种场景：

1. 客户应用通过 OTEL Agent/SDK 上报链路给 Insight
2. 通过 Opentelemtry Collector(简称 OTEL COL) 将链路转发给 Insight

在每个已安装 Insight Agent 的集群中都有 __insight-agent-otel-col__ 组件用于统一接收该集群的链路数据。
因此，该组件作为用户接入侧的入口，需要先获取该地址。可以通过 DCE 5.0 界面获取该集群 Opentelemtry Collector 的地址，
比如 __insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317__ ：

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/quickstart/images/get_insight_agent_otel_col_svc.png)

除此之外，针对不同上报方式，有一些细微差别：

## 客户应用通过 OTel Agent/SDK 上报链路给 Insight Agent Opentelemtry Collector

为了能够将链路数据正常上报至 Insight 并能够在 Insight 正常展示，需要并建议通过如下环境变量提供 OTLP 所需的元数据 (Resource Attribute)，有两种方式可实现：

- 在部署文件 YAML 中手动添加，例如：

    ```yaml
    ...
    - name: OTEL_EXPORTER_OTLP_ENDPOINT
      value: "http://insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317"
    - name: "OTEL_SERVICE_NAME"
      value: my-java-app-name
    - name: "OTEL_K8S_NAMESPACE"
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.namespace
    - name: OTEL_RESOURCE_ATTRIBUTES_NODE_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: spec.nodeName
    - name: OTEL_RESOURCE_ATTRIBUTES_POD_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.name
    - name: OTEL_RESOURCE_ATTRIBUTES
      value: "k8s.namespace.name=$(OTEL_K8S_NAMESPACE),k8s.node.name=$(OTEL_RESOURCE_ATTRIBUTES_NODE_NAME),k8s.pod.name=$(OTEL_RESOURCE_ATTRIBUTES_POD_NAME)"
    ```

- 利用 Insight Agent 自动注入如上元数据 (Resource Attribute) 能力

    确保 Insight Agent 正常工作并 [安装 Instrumentation CR](./operator.md#instrumentation-cr) 之后，
    只需要为 Pod 添加如下 Annotation 即可：

    `instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation" `

    举例：

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment-with-aotu-instrumentation
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: my-deployment-with-aotu-instrumentation-kuberntes
      replicas: 1
      template:
        metadata:
          labels:
            app.kubernetes.io/name: my-deployment-with-aotu-instrumentation-kuberntes
          annotations:
            sidecar.opentelemetry.io/inject: "false"
            instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation"
    ```

## 通过 Opentelemtry Collector 将链路转发给 Insight Agent Opentelemtry Collector

在保证应用添加了如上元数据之后，只需在客户 Opentelemtry Collector 里面新增一个 OTLP Exporter 将链路数据转发给
Insight Agent Opentelemtry Collector 即可，如下 Opentelemtry Collector 配置文件所示：

```yaml
...
exporters:
  otlp/insight:
    endpoint: insight-opentelemetry-collector.insight-system.svc.cluster.local:4317
service:
...
pipelines:
...
traces:
  exporters:
    - otlp/insight
```

## 参考

- [通过 Operator 实现应用程序无侵入增强](./operator.md)
- [使用 OTel 赋予应用可观测性](./otel.md)
