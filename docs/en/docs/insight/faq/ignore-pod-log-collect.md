---
hide:
  - toc
---

# Container Log Blacklist

> Note: Currently only blacklists at the Deployment, Statefulset, Daemonset, and Pod levels are supported; Namespace level is not supported.

The specific configuration method is as follows:

1. For any Pod whose container logs do not need to be collected, add `insight.opentelemetry.io/log-ignore: "true"` to the Pod's annotation to specify the container logs that do not need to be collected.

> ⚠️ Note: Starting from Insight Agent v0.37.0, the `insight.opentelemetry.io/log-ignore: "true"` annotation will be deprecated; please use `fluentbit.io/exclude: "true"` instead.

For example:

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: log-generator
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: log-generator
      replicas: 1
      template:
        metadata:
          labels:
            app.kubernetes.io/name: log-generator
          annotations:
            #insight.opentelemetry.io/log-ignore: "true" # 👈 Deprecated starting from Insight Agent v0.37.0
            fluentbit.io/exclude: "true"
        spec:
          containers:
            - name: nginx
              image: banzaicloud/log-generator:0.3.2
    ```

2. Restart the Pod. After the Pod returns to a running state, Fluent Bit will no longer collect the logs from the containers in this Pod.
