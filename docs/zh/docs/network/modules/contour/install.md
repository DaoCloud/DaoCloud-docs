---
hide:
  - toc
---

# 安装 Contour

本页介绍如何安装 Contour。

请确认您的集群已成功接入`容器管理`平台，然后执行以下步骤安装 Contour。

1. 在左侧导航栏点击`容器管理`—>`集群列表`，然后找到准备安装 Contour 的集群名称。

    ![contour-cluster](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/contour-cluster.png)

2. 在左侧导航栏中选择 `Helm 应用` -> `Helm 模板`，找到并点击 `contour`。

    ![contour-helm](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/contour-helm.png)

3. 在`版本选择`中选择希望安装的版本，点击`安装`。

    ![contour-version](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/contour-version.png)

4. 在安装界面，填写所需的安装参数。

    ![contour-install-1](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/contour-install-1.png)

    在如上界面中，填写`应用名称`、`命名空间`、`版本`等。

    ![contour-install-2](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/contour-install-2.png)

    在如上界面中，填写以下参数：

    - `contour` —> `Global Settings` —> `Global Image Registry`：统一设置镜像仓库地址。
    - `contour` —> `Contour Settings` —> `Contour Controller` —> `Manage CRDs`：创建 Contour 的 CRD。
    - `contour` —> `Contour Settings` —> `Contour Controller` —> `Controller Replica Count`：配置 Contour 控制面的副本数量。
    - `contour` —> `Contour Settings` —> `IngressClass` —> `IngressClass Name`：配置 Ingress Class 名称。如果集群部署多套 Ingress 的时候，可以使用此 Class 进行区分，这个字段会在创建 Ingres CR 的时候设置。
    - `contour` —> `Contour Settings` —> `IngressClass` —> `Default IngressClass`：设置默认 Ingress。
    - `contour` —> `Contour Settings` —> `IngressClass` —> `Enable Debug Log`：设置控制面 Debug 级别日志输出。

    ![contour-install-3](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/contour-install-3.png)

    在如上界面中，填写以下参数：

    - `contour` —> `Contour Settings` —> `Envoy Settings`  —> `Envoy Replica Count`：配置数据面 Envoy 的副本数量。
    - `contour` —> `Contour Settings` —> `Envoy Settings`  —> `Envoy Deploy Kind`：配置 Envoy 的部署类型，可以选择部署为 Deployment 或者是 DaemonSet。
    - `contour` —> `Contour Settings` —> `Envoy Settings`  —> `Enable HostNetwork`: 使用 Host 网络，默认关闭。如没有特殊需求不推荐开启此选项。
    - `contour` —> `Contour Settings` —> `Envoy Settings`  —> `Envoy Access Log Level`：配置 Envoy 访问日志等级。
    - `contour` —> `Contour Settings` —> `Envoy Settings`  —> `Envoy Service` —> `Service Type`：配置 Service 类型。
    - `contour` —> `Contour Settings` —> `Envoy Settings`  —> `Envoy Service` —> `IP Family Policy`：IP 单双栈设置，可以根据需求开启。

    ![contour-install-4](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/contour-install-4.png)

    在如上界面中，填写以下参数：

    - `contour` —> `Contour Settings` —> `Envoy Settings`  —> `Envoy Node Affinity` —> `Match Expressions`：通过软亲和性指定调度规则。
    - `contour` —> `Contour Settings` —> `Envoy Settings`  —> `Envoy Node Affinity` —> `Match Expressions` —> `Weight`：软亲和调度规则的权重。
    - `contour` —> `Contour Settings` —> `Metrics` —> `ServiceMonitor`：集群需要已部署 Prometheus Operator。
    - `contour` —> `Contour Settings` —> `Alert Configurations` —> `Prometheus Rule`：若开启，则创建包含告警规则 PrometheusRule CR。要求集群已安装 Prometheus Operator，或者部署 Insight 组件。

5. 点击 Tab 选项卡中 `YAML` 通过 YAML 方式进行高级配置。然后，点击右下角`确定`按钮即可完成创建。

    ![contour-yaml](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/contour-yaml.png)

创建完成后，创建 Ingress 路由，可通过 `平台级负载均衡` 选择 Contour 实例。详情参考： [创建路由](../../../kpanda/user-guide/network/create-ingress.md)

