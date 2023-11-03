# Sending Trace Data to Insight

This document describes how customers can send trace data to Insight on their own. It mainly includes the following two scenarios:

1. Customer apps report traces to Insight through OTEL Agent/SDK
2. Forwarding traces to Insight through Opentelemetry Collector (OTEL COL)

In each cluster where Insight Agent is installed, there is an `insight-agent-otel-col` component
that is used to receive trace data from that cluster. Therefore, this component serves as the
entry point for user access and needs to obtain its address first. You can get the address of
the Opentelemetry Collector in the cluster through the DCE 5.0 interface, such as
`insight-agent-opentelemetry-collector.insight-system.svc.cluster.local:4317`:

In addition, there are some slight differences for different reporting methods:

## Customer apps report traces to Insight through OTEL Agent/SDK

To successfully report trace data to Insight and display it properly, it is recommended to provide
the required metadata (Resource Attributes) for OTLP through the following environment variables.
There are two ways to achieve this:

- Manually add them to the deployment YAML file, for example:

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

- Use the automatic injection capability of Insight Agent to inject the metadata (Resource Attributes)

    Ensure that Insight Agent is working properly and after [installing the Instrumentation CR](./operator.md#instrumentation-cr),
    you only need to add the following annotation to the Pod:

    `instrumentation.opentelemetry.io/inject-sdk: "insight-system/insight-opentelemetry-autoinstrumentation" `

    For example:

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

## Forwarding traces to Insight through Opentelemetry Collector

After ensuring that the application has added the metadata mentioned above, you only need to add
an OTLP Exporter in your customer's Opentelemetry Collector to forward the trace data to
Insight Agent Opentelemetry Collector. Below is an example Opentelemetry Collector configuration file:

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

## References

- [Enhancing Applications Non-intrusively with the Operator](./operator.md)
- [Achieving Observability with OTel](./otel.md)
