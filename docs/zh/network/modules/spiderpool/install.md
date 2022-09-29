# 安装

本章节，介绍如何进行产品化安装spiderpool组件

## 安装步骤

1. 拥有一个 DCE 集群，登录 global 集群的 WEBUI 管理界面，在导航的"容器管理"->"集群列表"中，登录希望安装 spiderpool 的集群


2. 在"helm应用"->"helm模板"中，选择"system"仓库和"网络"组件，点击安装"spiderpool"

    ![spiderpool helm](../../images/spiderpool-helm.png)


3. 在"版本选择"中选择希望安装的版本，点击"安装"


4. 在安装参数界面，进行如下信息的填写

    ![spiderpool instal1](../../images/spiderpool-install1.png)
    在如上界面中，填写"安装名称"，"命名空间"，"版本"

    ![spiderpool instal2](../../images/spiderpool-install2.png)

    在如上界面中:

    * "global image Registry"：设置所有镜像的仓库地址，默认已经填写了可用的在线仓库，如果是私有化环境，可修改为私有仓库地址

    * "Spiderpool Agent Image repository"：设置镜像名，保持默认即可

    * "Spiderpool Agent Prometheus -> Enable Metrics"：如果打开，Spiderpool Agent组件会收集指标信息，以供外部采集

    * "Spiderpool Agent ServiceMonitor -> Install"：是否安装 Spiderpool Agent 的 ServiceMonitor 对象，这要求集群内安装好了 promethues，否则创建失败

    * "Spiderpool Agent PrometheusRule -> Install": 是否安装 Spiderpool Agent 的 promethuesRule 对象，这要求集群内安装好了 promethues，否则创建失败

    ![spiderpool instal3](../../images/spiderpool-install3.png)

    在如上界面中:
  
    * "Spiderpool Controller Setting -> replicas number"：设置Spiderpool Controller的副本数，该主要负责spiderpool的控制器逻辑，注意，该pod是hostnetwork模式，并且pod之间设置了反亲和性，
    所以，一个node上最多部署一个pod。因此，如果要部署大于 1 的副本数量，确保集群的节点数要充足，否则导致部分pod无法得到调度

    * "Spiderpool Controller Image -> repository": 设置镜像名，保持默认即可

    * "Spiderpool Controller Prometheus -> Enable Metrics"：如果打开，Spiderpool Controller 组件会收集指标信息，以供外部采集

    * "Spiderpool Controller ServiceMonitor -> Install"：是否安装 Spiderpool Controller 的 ServiceMonitor 对象，这要求集群内安装好了 promethues，否则创建失败

    * "Spiderpool Controller PrometheusRule -> Install": 是否安装 Spiderpool Controller 的 promethuesRule 对象，这要求集群内安装好了 promethues，否则创建失败

    * "IP Family Setting -> enable IPv4": 是否开启 IPv4 支持。注意，若开启，给 pod 分配 IP 时，务必会尝试分配 IPv4 地址，否分会导致 pod 启动失败
    所以，务必打开后续的 "Cluster Default Ippool Installation -> install IPv4 ippool"，以创建集群的缺省 IPv4 池

    * "IP Family Setting -> enable IPv6": 是否开启 IPv6 支持。注意，若开启，给 pod 分配 IP 时，务必会尝试分配 IPv6 地址，否分会导致 pod 启动失败
     所以，务必打开后续的 "Cluster Default Ippool Installation -> install IPv6 ippool"，以创建集群的缺省 IPv6 池

    ![spiderpool instal4](../../images/spiderpool-install4.png)

    在如上界面中:

    * "install IPv4 ippool"：是否安装 IPv4 IP 池

    * "install IPv6 ippool"：是否安装 IPv6 IP 池

    * "IPv4 subnet name"：IPv4 subnet的名字。如果未开启"install IPv4 ippool"，忽略本设置
    
    * "IPv4 ippool name"：IPv4 ippool 的名字。如果未开启"install IPv4 ippool"，忽略本设置
    
    * "IPv6 subnet name"：IPv6 subnet的名字。如果未开启"install IPv6 ippool"，忽略本设置
    
    * "IPv6 ippool name"：IPv6 ippool 的名字。如果未开启"install IPv6 ippool"，忽略本设置
    
    * "IPv4 ippool subnet"：设置默认池中的 IPv4 子网号，例如"192.168.0.0/16"。如果未开启"install IPv4 ippool"，忽略本设置

    * "IPv6 ippool subnet"：设置默认池中的 IPv6 子网号，例如"fd00::/112"。如果未开启"install IPv6 ippool"，忽略本设置

    * "IPv4 ippool gateway"：设置 IPv4 网关，例如"192.168.0.1"，该 IP 地址务必属于"IPv4 ippool subnet"。如果未开启"install IPv4 ippool"，忽略本设置

    * "IPv6 ippool gateway"：设置 IPv6 网关，例如"fd00::1"，该 IP 地址务必属于"IPv6 ippool subnet"。如果未开启"install IPv6 ippool"，忽略本设置

    * "IP Ranges for default IPv4 ippool"：设置哪些 IP 地址可分配给 pod，可设置多个成员，每个成员只支持 2 种输入格式的字符串，一种是诸如 "192.168.0.10-192.168.0.100" 设置一段连续的IP，一种是诸如 "192.168.0.200" 设置单个IP地址。注意，并不支持输入CIDR格式。
      这些 IP 地址务必属于"IPv4 ippool subnet"。如果未开启"install IPv4 ippool"，忽略本设置

    * "IP Ranges for default IPv6 ippool"：设置哪些 IP 地址可分配给 pod，可设置多个成员，每个成员只支持 2 种输入格式的字符串，一种是诸如 "fd00::10-fd00::100" 设置一段连续的IP，一种是诸如 "fd00::200" 设置单个IP地址。注意，并不支持输入CIDR格式。
     这些 IP 地址务必属于"IPv6 ippool subnet"。如果未开启"install IPv6 ippool"，忽略本设置


5. 最终点击"安装"


## 说明

1. 在安装流程中，能够完成单个subnet和ippool的创建，在完成安装后，能够在使用界面中完成更多的subnet和ippool的创建
