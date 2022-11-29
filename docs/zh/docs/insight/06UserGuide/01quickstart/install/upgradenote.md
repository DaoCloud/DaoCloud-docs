# 升级注意事项

## 从低版本升级到 v0.12.x

1. 从 v0.12.0 开始 ，insight-agent 中`node exporter`  Chart 开始使用 [Kubernetes 推荐的标签]([https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/).))。因此，在升级之前，请运行以下命令删除 `node exporter` 的 DaemonSet 。

    ```shell
    kubectl delete daemonset -l app=prometheus-node-exporter -n insight-system
    ```


2. 从 v0.12.0 开始 ，insight-agent 中`kube-prometheus-stack` Chart  [在 Prometheus CRD 中添加 `hostNetwork`字段](https://github.com/prometheus-community/helm-charts/pull/2693)。因此，在升级之前，请运行以下命令删除 Prometheus CRD。

    ```shell
    kubectl delete crd prometheuses.monitoring.coreos.com
    ```

!!! Note

    注意：该操作会导致 Prometheus 服务被删除直至 insight-agent 升级成功。

