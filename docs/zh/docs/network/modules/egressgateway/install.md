---
hide:
  - toc
---

# 安装 EgressGateway

本章节主要介绍如何安装 EgressGateway 组件。

## 前提条件

- 在 DCE 5.0 集群内使用 EgressGateway，需要结合 [Calico/Flannel/Weave/Spiderpool](../../modules/egressgateway/use-egpolicy.md)。

- 建议安装 v0.4.0 及其以上的 EgressGateway 版本，安装后可以创建出口网关实例并配合出口网关策略使用。

## 安装步骤

请确认您的集群已成功接入 __容器管理__ 平台，然后执行以下步骤安装 EgressGateway。

1. 在左侧导航栏点击 __容器管理__ —> __集群列表__ ，然后找到准备安装 EgressGateway 的集群名称。

1. 在左侧导航栏中选择 __Helm 应用__ -> __Helm 模板__ ，找到并点击 __egressgateway__ 。

    ![找到 egressgateway](../../images/egress-install-1.png)

1. 在版本选择中选择希望安装的版本，点击 __安装__ ，在安装界面，填写所需的安装参数。

    ![点击安装](../../images/egress-install-2.png)

    ![填写参数](../../images/egress-install-3.png)

    上图中的各项参数说明：

    - __命名空间__ ：部署 EgressGateway 组件的命名空间，默认为 __default__ 。可更改为其他命名空间。
    - __Feature__ —> __Enable IPv4__ ：支持开启 IPv4，默认开启。
    - __Feature__ —> __Enable IPv6__ ：支持开启 IPv6，默认关闭。若启用，Pod 网络必须是双栈才能正常使用。
    - __Feature__ -> __Tunnel IPv4 subnet__ ：设置隧道的 IPv4 子网，可使用默认值。若更改，不得与集群中的 CIDR 重复，造成网络冲突。
    - __Feature__ -> __Tunnel IPv6 subnet__ ：设置隧道的 IPv6 子网，可使用默认值。若更改，不得与集群中的 CIDR 重复，造成网络冲突。
    - __Feature__ -> __VXLAN Setting__ -> __VXLAN name__ ：设置 VXLAN 名称，可使用默认值。
    - __Feature__ -> __VXLAN Setting__ -> __VXLAN port__：设置 VXLAN 端口，可使用默认值。
    - __Feature__ -> __VXLAN Setting__ -> __VXLAN ID__ ：设置 VXLAN ID，可使用默认值。
    - __Feature__ -> __Iptables Setting__ -> __Backend mode__ ：设置 iptable 的模式，默认选择 auto 模式。
      若更改，您可以通过在集群主机上运行 “iptables –version” 来查看 iptables 的当前模式。

    ![填写参数](../../images/egress-install-4.png)

    上图中的各项参数说明：

    - __Controller Setting__ —> __Image Setting__ -> __Image registry__ ：设置镜像名，可使用默认值。
    - __Controller Setting__ —> __Debug Setting__ -> __Log level__ ：设置日志级别，可使用默认值，或者下拉选择其他级别。
    - __Controller Setting__ —>__Prometheus Setting__ —> __ServiceMonitor Setting__ -> __Log level__ -> __Install__ ：支持开启安装 Prometheus 监控，默认不安装。
    - __Agent Setting__ —> __Image Setting__ -> __Image registry__ ：设置镜像名，可使用默认值。
    - __Controller Setting__ —> __Debug Setting__ -> __Log level__ ：设置日志级别，可使用默认值，或者下拉选择其他级别。
    - __Controller Setting__ —>__Prometheus Setting__ —> __ServiceMonitor Setting__ -> __Log level__ -> __Install__ ：支持开启安装 Prometheus 监控，默认不安装。

1. 参数设置完成后点击 __确定__ 完成安装，完成后可参考创建出口网关实例和网关策略进行出口网关的使用。
