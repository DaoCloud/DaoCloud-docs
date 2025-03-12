---
hide:
  - toc
---

# 容器日志黑名单

> 注意：目前仅支持 Deployment、 Statefulset、 Daemonset、 Pod 级别的黑名单，不支持 Namespace 级别。

具体配置方式如下：

1. 对于任意一个不需要采集容器日志的 Pod, 在 Pod 的 annotation 中添加 `insight.opentelemetry.io/log-ignore: "true"` 来指定不需要采集的容器日志，例如：

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
            insight.opentelemetry.io/log-ignore: "true"
        spec:
          containers:
            - name: nginx
              image: banzaicloud/log-generator:0.3.2
    ```

2. 重启 Pod，等待 Pod 恢复运行状态之后，Fluenbit 将不再采集这个 Pod 内的容器的日志。
