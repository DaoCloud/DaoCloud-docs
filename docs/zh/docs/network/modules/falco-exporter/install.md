# 安装

本章节介绍如何安装 Falco-exporter 组件

## 安装须知
在安装使用 Falco-exporter 之前，您需要[安装](../falco/install.md)运行Falco，并启用gRPC输出（默认通过Unix套接字）。 可以在[此处](https://github.com/falcosecurity/charts/tree/master/falco#enabling-grpc) 找到在 Falco Helm Chart 中启用 gRPC 输出的说明。

## 集群安装组件步骤

1. 在浏览器打开集群的管理界面，点击侧边栏导航的 `Helm 应用`，然后点击 `Helm 模板`。

2. 在 `Helm 模板`中，点击安装 `falco-exporter`。

   ![falco-exporter_helm-1](../../images/falco-exporter-install-1.png)

3. 在`版本选择`中选择希望安装的版本，点击`安装`。

4. 在安装界面，填写所需的安装参数。

   ![falco-exporter_helm-2](../../images/falco-exporter-install-2.png)

   在如上界面中，填写`应用名称`、`命名空间`、`版本`等。

   ![falco-exporter_helm-3](../../images/falco-exporter-install-3.png)

   在如上界面中:

    - `Falco Prometheus Exporter -> Image Settings -> Registry`：设置 falco-exporter 镜像的仓库地址，默认已经填写了可用的在线仓库，如果是私有化环境，可修改为私有仓库地址。

    - `Falco Prometheus Exporter -> Prometheus ServiceMonitor Settings -> Repository`：设置 falco-exporter 镜像名。

    - `Falco Prometheus Exporter -> Prometheus ServiceMonitor Settings -> Install ServiceMonitor`：安装 Prometheus Operator 服务监视器，默认开启。
    
    - `Falco Prometheus Exporter -> Prometheus ServiceMonitor Settings -> Scrape Interval`：用户自定义的间隔；如果未指定，则使用 Prometheus 默认间隔。

    - `Falco Prometheus Exporter -> Prometheus ServiceMonitor Settings -> Scrape Timeout`：用户自定义的抓取超时时间；如果未指定，则使用 Prometheus 默认的抓取超时时间

   ![falco-exporter_helm-3](../../images/falco-exporter-install-4.png)
   ![falco-exporter_helm-3](../../images/falco-exporter-install-5.png)
   在如上界面中:

    - `Falco Prometheus Exporter -> Prometheus prometheusRules -> Install prometheusRules`：创建 PrometheusRules，对优先事件发出警报，默认开启。

    - `Falco Prometheus Exporter -> Prometheus prometheusRules -> Alerts settings`：告警设置，为不同级别的日志事件设置是否启用、告警的间隔时间、告警的阈值。

   点击右下角`确定`按钮即可完成创建。
