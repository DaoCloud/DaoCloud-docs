# DCE 5.0 一体机部署

本文说明如何在一体机上部署 DCE 5.0。

## 环境准备

首先要准备好网络环境和容量规划。

### 网络要求

**硬件**

- 通常一体机插有多张网卡或一张网卡有多个网口，所以建议组 Bond，并且使端口组 LACP 的 Bond 高可用
- 暂时不建议划分多平面，共用一个数据面
- 网口需要为 trunk 模式

**预留 VLAN**

至少有 2 个 VLAN：1 个用于 BMC VLAN，1 个管理/业务 VLAN，1 个存储 VLAN（可选）。
如果需要为 Pod 分配"静态 IP"，需要先创建子接口并额外分配 VLAN。

| 名称 | 用途 |
| --- | --- |
| 管理/业务 VLAN | 用于 SSH，管理界面、 API、业务流量、负载均衡、集群内部通信 |
| BMC VLAN | 用于服务器的 BMC 管理 |
| 存储 VLAN（可选） | 用于本地和远程存储访问 |

**IP**

| 资源 | 要求 | 说明 |
| --- | --- | --- |
| istioGatewayVip | 1 个 | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 DCE 的 UI 界面和 OpenAPI 访问入口 |
| insightVip | 1 个 | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 GLobal 集群的 insight 数据收集入口使用，子集群的 insight-agent 可上报数据到这个 VIP |
| 协议 | - | 支持 IPv6。 |
| 保留 IP 地址段 | 需保留两段 | 供 Pod（默认 10.233.64.0/18） 和 Service （默认 10.233.0.0/18 使用）。如果已经在使用了，可以自定义其他网段避免 IP 地址冲突。 |
| 路由 | - | 服务器有 default 或指向 0.0.0.0 这个地址的路由。 |
| NTP 服务地址 | 1~4 个 | 确保您的数据中心有可以访问的 NTP 服务器 IP 地址。 |
| DNS 服务地址 | 1~2 个 | 如果您的应用需要 DNS 服务，请准备可以访问 DNS 服务器 IP 地址。 |

**网络端口**

[端口要求](../commercial/port-requirements.md)

### 容量规划

**CPU、内存、磁盘**

| 物理机 | CPU | 内存 | containerd、k8s 默认使用根盘 | 备注 |
| --- | --- | --- | --- | --- |
| master01 | >= 12 C | >= 20 G | 480G，SSD 硬盘，RAID1 | 作为“火种机 + 集群控制节点”，资源建议可以适当调高 |
| master02 | >= 12 C | >= 20 G | 480G，SSD 硬盘，RAID1 | |
| master03 | >= 12 C | >= 20 G | 480G，SSD 硬盘，RAID1 | |

**环境准备检查表**

| 分类 | 检查项 | 级别 | 结果 |
| --- | --- | --- | --- |
| fenlei | 机架空间足够（一台服务器需要 2U 空间） | 必选 |
| | 机架的电源功率足够，每台服务器至少额定 750W 功率 | 必选 |
| | 机架有 UPS 不间断电源保护 | 可选 |
| | 电源线有无特殊要求（默认提供 2 个 C13 标准电源线） | 必选 |
| | 网线有无特殊要求（默认提供 4 个 SFP+ 光模块或 4 个 5mLC-LC 多模光纤线缆或 3 米 Cat6 网络跳线） | 必选 |
| | 访问一体机的 Chrome 浏览器（能够连接要求的 VLAN） | 必选 |
| | 一台用于连接 BMC RJ45 端口的交换机，每台服务器需预留 1 个端口 | 必选 |
| | 两台用于连接数据流量的 SFP+ 端口的交换机，每台服务器需各预留 2 个端口，共 4 个端口 | 建议 |
| | 如果没有条件配置"两台冗余交换机"，至少需要一台 SFP+ 端口的交换机，每台服务器需预留 2 个端口 | 必选 |
| | SFP+ 端口的交换机连接的端口配置为 Trunk 并允许相应 VLAN | 必选 |
| | SFP+ 端口的交换机启用了 IPv4 和 IPv6 multicast，请确保交换机之间可以多播 | 必选 |
| | 如果您使用冗余交换机，请进行相应的堆叠配置 | 必选 |
|网络| 至少有 2 个 VLAN：1 个用于 BMC VLAN，1 个管理/业务  VLAN，1 个存储 VLAN（可选） | 必选 |
| | 如果需要为 Pod 分配"静态 IP"，需要先创建子接口并额外分配 VLAN | 可选 |
| | 有集群内可访问的 NTP 服务器 IP 地址 | 必选 | |
| | 如果您的应用需要 DNS 服务，需准备集群内可访问的 DNS 服务器 IP 地址 | 建议 |
| | 确保预留的 BMC VLAN 中有足够连续的 IP 地址每台服务器需要 1 个该 VLAN 的 IP地址 | 必选 |
| | 确保预留的管理/业务 VLAN 中有足够连续的 IP 地址每台服务器需要 1 个 IP地址，整个集群还需要额外 1 个 IP（管理界面） | 必选 |
| | 整个集群还需要额外 2 个IP（istioGatewayVip、insightVip） | 必选 |
| | 确保预留的存储 VLAN 中有足够连续的 IP 地址每台服务器需要 1 个该 VLAN 的 IP地址 | 可选 |
| | 保留 IP 地址段（供 Calico 和 Kube-Proxy 使用），默认为 clusterCIDR: 10.233.64.0/18、serviceCIDR: 10.233.0.0/18。如果已经在使用了，可以自定义其他网段避免 IP 地址冲突。 | 必选 |
| 容量规划 | 确保您做好容量规划，当前的集群容量（CPU、内存、网络、硬盘）和性能可以支持您的容器化业务 | 必选 |
| | 确保假定任意服务器宕机的情况下，剩余的集群有足够的容量支撑 | 必选 |
| | 如果您未来准备扩容，需要提前预备机架空间、交换机端口和相应 VLAN 的 IP 地址 | 建议 |

## 安装步骤（3 台物理机）

### 安装前置依赖

[安装依赖项](../install-tools.md)

### 离线安装

[开始安装](../commercial/start-install.md)

**安装前注意事项：**

- 在三台物理机中选择一台物理机作为火种机执行 DCE 5.0 的部署。其中集群配置文件 `ClusterConfig.yaml`
  中的 bootstrapNode 参数可以指定火种机器的 IP。

    ```yaml title="ClusterConfig.yaml"
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      clusterName: my-cluster # (1)!
      bootstrapNode: auto  # (2)!
      ...
    ...
    ```

    1. 火种节点的域名或 IP，默认解析为火种节点默认网关所在网卡的 IP；
       可手动填入 IP 或域名，若为域名，如果检测到无法解析，将自动建立此域名和火种节点默认 IP 的映射
    2. 默认自动解析

- 集群配置文件 ClusterConfig.yaml 中，将 3 台物理机的信息配置在 masterNodes 中即可。

    ```yaml title="ClusterConfig.yaml"
    ...
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ...
      masterNodes:
        - nodeName: "g-master1" # (1)!
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
          # ansibleSSHPort: "22"
          # ansibleExtraArgs: "" 
        - nodeName: "g-master2"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
          # ansibleSSHPort: "22"
          # ansibleExtraArgs: ""
        - nodeName: "g-master3"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
          # ansibleSSHPort: "22"
          # ansibleExtraArgs: ""
        ...
    ...
    ```

    1. 物理机 1 角色为集群的控制面节点 + 火种机节点
