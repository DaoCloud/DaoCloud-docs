# 什么是 Falco-exporter

[Falco-exporter](https://github.com/falcosecurity/falco-exporter) 是一个 Falco 输出事件的 Prometheus Metrics 导出器。

Falco-exporter 会部署为 Kubernetes 集群上的守护进程集。如果集群中已安装并运行 Prometheus，Prometheus 将自动发现 Falco-exporter 提供的指标。
