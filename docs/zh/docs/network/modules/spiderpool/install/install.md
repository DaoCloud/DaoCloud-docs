---
hide:
  - toc
---

# 安装 Spiderpool

本页介绍如何安装 Spiderpool。

## 前提条件

1. 在 DCE 5.0 集群内使用 SpiderPool，需要结合 [Calico](../../calico/index.md)/[Cillium](../../cilium/index.md)。

2. 建议使用 v0.7.0 及其以上的 Spiderpool 版本，新版 Spiderpool 支持自动安装 [Multus](../../multus-underlay/install.md)，安装后可结合 [Mulus CR 管理](../../../config/multus-cr.md)使用 Underlay CNI（[Macvlan](../../multus-underlay/macvlan.md) 或 [SR-IOV](../../multus-underlay/sriov.md)，并确认待使用的网卡接口和子网。

## 安装步骤

请确认您的集群已成功接入`容器管理`平台，然后执行以下步骤安装 Spiderpool。

1. 在左侧导航栏点击 `容器管理` —> `集群列表`，然后找到准备安装 Spiderpool 的集群名称。

2. 在左侧导航栏中选择 `Helm 应用` -> `Helm 模板`，找到并点击 `spiderpool`。

    ![spiderpool helm](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-helm.png)

3. 在`版本选择`中选择希望安装的版本，点击`安装`。

4. 在安装界面，填写所需的安装参数。如需要使用RDMA 资源，更多详情可参考 [RDMA 安装及使用准备](rdmapara.md)

    ![spiderpool instal1](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-install1.png)

    ![spiderpool instal2](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-install2.png)

    上图中的各项参数说明：

    - `namespace`：部署 SpiderPool 组件的命名空间，默认为 `kube-system`。如改为其他 Namespace，界面可能会不可用。

    - `Global Setting` —> `global image Registry`：设置所有镜像的仓库地址，默认已经填写了可用的在线仓库，如果是私有化环境，可修改为私有仓库地址。

    - `Spiderpool Agent Setting` —> `Spiderpool Agent Container registry`：设置镜像名，保持默认即可。

    - `Spiderpool Agent Setting` —> `Spiderpool Agent Prometheus` -> `Enable Metrics`：若启用，Spiderpool Agent 组件会收集指标信息，以供外部采集。

    - `Spiderpool Agent Setting` —> `Spiderpool Agent ServiceMonitor` -> `Install`：安装 Spiderpool Agent 的 ServiceMonitor 对象，这要求集群内已安装 Prometheus，否则会创建失败。

    ![spiderpool instal3](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-install3.png)

    上图中的各项参数说明：

    - `Spiderpool Agent Setting` —> `Spiderpool Agent PrometheusRule` -> `Install`：安装 Spiderpool Agent 的 prometheusRule 对象，这要求集群内已安装 Prometheus，否则会创建失败。

    - `Spiderpool Controller Setting` -> `replicas number`：设置 Spiderpool Controller 的副本数，主要负责 Spiderpool 的控制器逻辑。

        > 该 Pod 是 hostnetwork 模式，并且在 Pod 之间设置了反亲和性，所以一个 Node 上最多部署一个 Pod。
        如果要部署大于 1 的副本数量，请确保集群的节点数充足，否则将导致部分 Pod 调度失败。

    - `Spiderpool Controller Setting` -> `Spiderpool Controller Image` -> `repository`：设置镜像名，保持默认即可.

    - `Spiderpool Controller Setting` -> `Spiderpool Controller Prometheus` -> `Enable Metrics`：若启用，Spiderpool Controller 组件会收集指标信息，以供外部采集。

    - `Spiderpool Controller Setting` -> `Spiderpool Controller ServiceMonitor` -> `Install`：安装 Spiderpool Controller 的 ServiceMonitor 对象，这要求集群内已安装 Prometheus，否则创建失败。

    - `Spiderpool Controller Setting` -> `Spiderpool Controller PrometheusRule` -> `Install`：安装 Spiderpool Controller 的 prometheusRule 对象，这要求集群内已安装 Prometheus，否则创建失败。

    ![spiderpool instal4](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-install4.png)

    上图中的各项参数说明：

    - `Multus Setting -> MultusCNI -> Install Multus CNI`：启用 Multus 安装。如果您已经安装了 Multus，则可以将其设置为 false。默认为 true。

    - `Multus Setting -> MultusCNI -> Default CNI Name`：集群默认 CNI 名称。 默认为空，如果该值为空，Spiderpool 将根据/etc/cni/net.d/ 中已有的 CNI conf 文件自动获取默认 CNI。

    - `Multus Setting -> Multus Image -> repository`：设置 Multus 的镜像仓库地址，默认已经填写了可用的在线仓库，如果是私有化环境，可修改为私有仓库地址。

    - `IP Family Setting -> enable IPv4`：开启 IPv4 支持。若开启，在给 pod 分配 IP 时，会尝试分配 IPv4 地址，否则会导致 Pod 启动失败。所以，请开启 `Cluster Default Ippool Installation` -> `install IPv4 ippool`，以创建集群的默认 IPv4 池。

    - `IP Family Setting -> enable IPv6`：开启 IPv6 支持。若开启，在给 pod 分配 IP 时，会尝试分配 IPv6 地址，否则会导致 Pod 启动失败。所以，请开启 `Cluster Default Ippool Installation` -> `install IPv6 ippool`，以创建集群的默认 IPv6 池。

    ![spiderpool instal5](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/spiderpool-install5.png)

    上图中的各项参数说明：

    - `Cluster Default Ippool Installation` -> `install IPv4 ippool`：安装 IPv4 IP 池。

    - `Cluster Default Ippool Installation` -> `install IPv6 ippool`：安装 IPv6 IP 池。

    - `Cluster Default Ippool Installation` -> `IPv4 ippool name`：IPv4 ippool 的名字。如果未开启 `install IPv4 ippool`，请忽略本项。

    - `Cluster Default Ippool Installation` -> `IPv6 ippool name`：IPv6 ippool 的名字。如果未开启 `install IPv6 ippool`，请忽略本项。

    - `Cluster Default Ippool Installation` -> `IPv4 ippool subnet`：设置默认池中的 IPv4 子网号，请提前规划好可使用的子网及网关，例如 `192.168.0.0/16`。如果未开启 `install IPv4 ippool`，请忽略本项。

    - `Cluster Default Ippool Installation` -> `IPv6 ippool subnet`：设置默认池中的 IPv6 子网号，请提前规划好可使用的子网及网关，例如 `fd00::/112`。如果未开启 `install IPv6 ippool`，请忽略本项。

    - `Cluster Default Ippool Installation` -> `IPv4 ippool gateway`：设置 IPv4 网关，例如 `192.168.0.1`，该 IP 地址务必属于 `IPv4 ippool subnet`。如果未开启 `install IPv4 ippool`，请忽略本项。

    - `Cluster Default Ippool Installation` -> `IPv6 ippool gateway`：设置 IPv6 网关，例如 `fd00::1`，该 IP 地址应属于 `IPv6 ippool subnet`。如果未开启 `install IPv6 ippool`，请忽略本项。

    - `Cluster Default Ippool Installation` -> `IP Ranges for default IPv4 ippool`：设置哪些 IP 地址可分配给 Pod，可设置多个成员，每个成员只支持 2 种输入格式的字符串。

        1. 一种是一段连续的 IP，如 `192.168.0.10-192.168.0.100`。
        2. 一种是单个 IP 地址，如 `192.168.0.200` 。不支持输入 CIDR 格式。

        这些 IP 地址应属于 `IPv4 ippool subnet`。如果未开启 `install IPv4 ippool`，请忽略本项。

    - `Cluster Default Ippool Installation` -> `IP Ranges for default IPv6 ippool`：设置哪些 IP 地址可分配给 Pod，可设置多个成员，每个成员只支持 2 种输入格式的字符串。

        1. 一种是一段连续的 IP，如 `fd00::10-fd00::100`。
        2. 一种是单个 IP 地址，如 `fd00::200` 设置。不支持输入 CIDR 格式。

        这些 IP 地址应属于 `IPv6 ippool subnet`。如果未开启 `install IPv6 ippool`，请忽略本项。

5. 点击右下角`确定`按钮即可完成安装。完成后，可参考 [SpiderPool 的使用](../../../config/use-ippool/usage.md)进行 IP Pool 的使用。

!!! note

    在安装过程中，可创建单个 subnet 和 ippool；在安装完成后，在使用界面可创建更多的 subnet 和 ippool。
