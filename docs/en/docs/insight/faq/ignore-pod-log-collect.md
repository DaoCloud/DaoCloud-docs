---
hide:
  - toc
---

# Container Log Blacklist

To exclude container logs from being collected, follow these steps:

1. **For any Pod where log collection is not needed**, add the annotation `insight.opentelemetry.io/log-ignore: "true"` in the Pod's metadata. This prevents logs from being collected for that Pod. Example:

    ```yaml
    apiVersion: apps/v1
    kind: Pod
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
            insight.opentelemetry.io/log-ignore: "true"
        spec:
          containers:
            - name: nginx
              image: banzaicloud/log-generator:0.3.2
    ```

2. **Restart the Pod.** Once the Pod is back in a running state, Fluent Bit will no longer collect logs from the containers within that Pod.
