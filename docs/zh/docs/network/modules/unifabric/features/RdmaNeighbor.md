# RDMA 拓扑识别

## 功能概述

Unifabric 的 RDMA 网络邻居发现功能是一个专为 RDMA 网络设计的综合性网络拓扑发现系统。该功能基于 LLDP 协议进行底层邻居发现，并在此基础上提供多种上层网络管理能力。核心功能包括：

- **LLDP 邻居发现:** 基于 LLDP 协议的底层网络拓扑发现，支持所有类型的交换机设备
- **RDMA 网络专用:** 目前专门针对基于 RoCE 协议的 RDMA 网络环境
- **网卡分类管理:** 区分 GPU 算力网络（computeNics）和存储网络（storageNics）
- **rdmaNeighbor 分组:** 专门针对 GPU 算力网络的自动分组功能，用于 Scale-out 场景的节点拓扑管理
- **Kubernetes 原生:** 深度集成到 Kubernetes 环境，通过 FabricNode CRD 管理网络状态

其中，**rdmaNeighbor** 是基于 LLDP 邻居发现的上层功能，专门用于 GPU 算力网络的拓扑分组，与存储网络无关。它通过分析节点间的 GPU 算力网络连接关系，自动将具有相同网络拓扑的节点分组，为 Scale-out 计算场景提供智能的节点管理能力。

- [LLDP 邻居发现](#lldp)
- [交换机邻居发现](#_7)
- [ScaleoutLeafGroup 自动分组](#scaleoutleafgroup)
- [存储主机邻居上报](#_6)

GPU 网络分类概念：

- **GPU 算力网络（computeNics）:** 用于 GPU 间通信、模型训练、推理计算的高速 RDMA 网络
- **GPU 存储网络（storageNics）:** 用于 GPU 与存储系统间数据传输的专用 RDMA 网络

![rdma](../images/rdma.JPEG)

### 架构设计

邻居发现功能采用分层架构设计：

```
__________________________________________________________________________________
|                                                                                  |
|                               RDMA 网络邻居发现                                  |
|__________________________________________________________________________________|
|  LLDP邻居发现          |  交换机邻居上报        |  外部存储邻居上报              |
|  (Host Neighbor)       |  (Switch Neighbor)     |  (Storage Neighbor)            |
|                        |                        |                                |
|  • GPU 算力网络        |  • 交换机拓扑          |  • 存储集群发现                |
|  • GPU 存储网络        |  • gnmi 集成           |  • 跨集群连接                  |
|  • LLDP 协议           |  • LLDP 协议           |  • 存储路径优化                |
|________________________|________________________|________________________________|

```

### LLDP 邻居发现

LLDP 邻居发现功能: Unifabric 运行 lldpd 守护进程通过 LLDP 协议自动发现 GPU 算力网络和 GPU 存储网络中的邻居设备，并同步到 FabricNode CRD 的 Status 字段中，以供 RDMA 网络中拓扑展示使用。

#### 启用 RDMA 网络邻居发现功能

注意：该功能必须确保交换机开启 LLDP 协议，否则无法发现邻居设备。

最佳实践配置已经默认配置，参考 [Install](../install.md)。以下是涉及该功能的 Helm values 详细参数说明：

```yaml
features:
  rdmaNeighbor:
    # 开启扩展邻居发现功能
    enabled: true

    # FabricNode 同步 LLDP 邻居同步时间
    timeToWaitSyncLLDPToFabricNode: 1m

    # GPU 算力网络网卡筛选规则
    # 用于筛选节点哪些 RDMA 网卡属于 computeNics
    # 支持接口名称通配（interface=）或子网（cidr=）
    # 示例：gpuRdmaNicFilter: "cidr=172.16.0.0/16"
    gpuRdmaNicFilter: "interface=ens16*"

    # GPU 存储网络网卡筛选规则
    # 用于筛选节点哪些 RDMA 网卡属于 storageNics
    storageRdmaNicFilter: "interface=ens17*"
    # 示例：storageRdmaNicFilter: "cidr=172.17.0.0/16"

    # LLDP 守护进程配置
    lldpd:
      # LLDP 报文发送间隔（秒）
      txInterval: 30

      # 管理 IP 配置模式, 默认为空，使用 Kubelet NodeIP 作为管理 IP
      # 支持：IP地址列表 | 接口名称 | 自动选择（留空）
      managementIPPattern: ""

      # LLDP 启用接口配置, 如果为空表示作用与所有 RDMA 网卡
      # 支持：具体接口 | 模式匹配 | 全部接口（留空）
      interfaces: "ens*"
```

`gpuRdmaNicFilter，storageRdmaNicFilter` 配置说明：

这些配置影响主机哪些 RDMA 物理网卡计入 FabricNode.status 的 computeNics 和 storageNics 中：

- 网卡分类优先级：优先检查 storageRdmaNicFilter，未匹配的归入 FabricNode.status 中 computeNics
- 如果 gpuRdmaNicFilter 和 storageRdmaNicFilter 同时未配置，主机所有物理网卡计入 FabricNode.status 中 computeNics
- 如果 gpuRdmaNicFilter 和 storageRdmaNicFilter 都配置，按照通配值正常筛选，分别计入 FabricNode.status 中 computeNics 和 storageNics

**推荐配置**: 优先设置 storageRdmaNicFilter，未匹配的 RDMA 网卡自动归入 FabricNode.status 中 computeNics。

`agent.config.rdmaNeighbor.lldpd.interfaces` 配置说明：

- **具体接口:**

    ```yaml
    interfaces: "eth0,eth1,eth2"
    ```

- **模式匹配:**

    ```yaml
    interfaces: "eth*" # 所有以 eth 开头的接口
    ```

- **排除模式:**

    ```yaml
    interfaces: "eth*,!eth2" # 所有 eth 接口，但排除 eth2
    ```

- **全部接口**（默认）：

    ```yaml
    interfaces: "" # 使用所有 RDMA 网卡启用 LLDP
    ```

1. 使用 Helm 部署或更新 Unifabric

    ```bash
    helm upgrade --install unifabric -n unifabric --create-namespace ./chart --values values.yaml
    ```

1. 验证 RDMA 网络邻居发现功能是否正常

- 检查 unifabric 组件（特别是 lldpd 容器）是否正常运行，lldpd 日志作为独立的 container 运行在 unifabric-agent pod 中：

    ```bash
    kubectl get po -n unifabric
    NAME                         READY   STATUS    RESTARTS      AGE
    unifabric-746d4f8d75-qbknh   1/1     Running   1             12m
    unifabric-agent-4rpbw        2/2     Running   0             12m
    unifabric-agent-fgpkc        2/2     Running   0             12m
    ```

- 检查 FabricNode CRD 中的 computeNics 和 storageNics 所有网卡的 lldpNeighbor 字段是否包含邻居信息：

注意： 由于 LLDP 邻居采集需要一定时间，默认情况下 unifabric-agent 会等待一分钟后才会将 LLDP 邻居信息同步到 FabricNode CRD 的 Status 字段中。

如果需要调整等待时间，可以修改 Helm 参数 `agent.config.rdmaNeighbor.timeToWaitSyncLLDPToFabricNode` 配置，默认为 1 分钟

```bash
~# kubectl get fabricnodes.unifabric.io sh-cube-master-3 -o yaml
apiVersion: unifabric.io/v1beta1
kind: FabricNode
metadata:
  creationTimestamp: "2025-06-19T07:02:08Z"
  generation: 1
  name: sh-cube-master-3
  resourceVersion: "48723802"
  uid: aa85f55f-d87f-4fbe-8dbc-e3c9cc089943
spec: {}
status:
  gpuNics:
  - ipv4: 172.17.3.143/24
    ipv6: ""
    lldpNeighbor:
      description: 'SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
        ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64'
      hostname: LEAF03
      mac: 70:06:92:6e:32:1c
      mgmtIP: 10.193.77.203
      port: Ethernet208
    name: ens841np0
    rdma: true
    state: up
  - ipv4: 172.17.4.143/24
    ipv6: ""
    lldpNeighbor:
      description: 'SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
        ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64'
      hostname: LEAF04
      mac: 70:06:92:6e:34:5c
      mgmtIP: 10.193.77.204
      port: Ethernet208
    name: ens842np0
    rdma: true
    state: up
  - ipv4: 172.17.2.143/24
    ipv6: ""
    lldpNeighbor:
      description: 'SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
        ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64'
      hostname: LEAF02
      mac: 70:06:92:6e:34:80
      mgmtIP: 10.193.77.202
      port: Ethernet200
    name: ens835np0
    rdma: true
    state: up
  - ipv4: 172.17.1.143/24
    ipv6: ""
    lldpNeighbor:
      description: 'SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
        ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64'
      hostname: LEAF01
      mac: 70:06:92:6e:33:18
      mgmtIP: 10.193.77.201
      port: Ethernet208
    name: ens834np0
    rdma: true
    state: up
  rdmaHealthy: true
  totalNics: 5
  storageNics:
  - ipv4: 172.16.1.143/24
    ipv6: ""
    lldpNeighbor:
      description: 'SONiC Software Version: SONiC.CuOS_4.0-0.R_X86_64_ztp - HwSku:
        ds730-32d - Distribution: 10.13 - Kernel: 4.19.0-12-2-amd64'
      hostname: StorageSW
      mac: 70:06:92:6e:32:64
      mgmtIP: 10.193.77.211
      port: Ethernet144
    name: ens1np0
    rdma: true
    state: up
```

需要检查:

- gpuNics 中是否包括主机每一个 GPU 算力网卡，并且其 IP 地址、状态等是否符合预期，并且 lldpNeighbor 是否准确包含邻居设备的详细信息。

- storageNics 中是否包括主机每一个存储网卡，并且其 IP 地址、状态等是否符合预期，并且 lldpNeighbor 是否也准确包含邻居设备的详细信息。

- rdmaHealthy 表示如果所有 RDMA 网卡都 Ready（包括网卡状态，LLDP 邻居发现都正常） ，该字段为 true，否则为 false

- totalNics 表示主机所有 RDMA 网卡的总数，包括 gpuNics 和 storageNics

## ScaleoutLeafGroup 自动分组功能

ScaleoutLeafGroup 负责基于上述 LLDP 邻居发现信息自动将具有相同 GPU 算力网络拓扑的节点分组管理， 并将分组信息同步到 ScaleoutLeafGroup CRD 的 Status 字段中，并且为属于同一个 ScaleoutLeafGroup 的节点打上一组相同的标签(默认 label key: dce.unifabric.io/scaleout-group, 可通过 Helm 参数 `features.rdmaNeighbor.nodeTopoZoneLabelKey` 自定义， value 为 group name)。 该功能为横向扩展（Scale-out）场景提供了智能的节点分组和网络拓扑管理能力。

### 工作原理

ScaleoutLeafGroup 自动分组功能依赖于 FabricNode CRD 的 Status 字段中的 LLDP 邻居发现信息，因此必须确保 FabricNode CRD 的 Status.computeNics 字段中的 LLDP 邻居发现正常上报并信息正确。默认情况下，unifabric-agent 等待一分钟后才会将 LLDP 邻居信息同步到 FabricNode CRD 的 Status 字段中。如果需要调整等待时间，可以修改 Helm 参数 `features.rdmaNeighbor.timeToWaitSyncLLDPToFabricNode` 配置，默认为 1 分钟。

![rdma_neighbor](../images/rdma-neighbor.png)

### 配置示例

在 Install.md 中已经默认开启此配置，如果您意外关闭，或者出现任何问题。可以参考一下内容重新配置：

在 Controller 组件中启用 ScaleoutLeafGroup 自动分组功能：

```yaml
features:
  rdmaNeighbor:
    # 启用 RDMA 邻居发现功能
    enabled: true
    # 开启 ScaleoutLeafGroup 自动分组功能
    enableScaleOutLeafGroup: true
    # ScaleoutLeafGroup 自动分组标签 key
    nodeTopoZoneLabelKey: dce.unifabric.io/scaleoutleaf-group
```

> 注意： 必须启用 `features.rdmaNeighbor.enabled` 才能使 `features.rdmaNeighbor.enableScaleOutLeafGroup` 生效。

执行安装：

```bash
helm upgrade --install unifabric unifabric/unifabric -n unifabric -f values.yaml
```

### 验证安装

1. 检查 unifabric 组件是否正常运行：

    ```bash
    kubectl get po -n unifabric
    NAME                         READY   STATUS    RESTARTS      AGE
    unifabric-746d4f8d75-qbknh   1/1     Running   1             12m
    unifabric-agent-4rpbw        2/2     Running   0             12m
    unifabric-agent-fgpkc        2/2     Running   0             12m
    ```

2. 检查 ScaleoutLeafGroup CRD 是否正常，一个 ScaleoutLeafGroup 对象代表一组具有相同 GPU 网络拓扑的节点。

    ```bash
    ~# kubectl get scaleoutleafgroups.unifabric.io
    NAME              healthyNodes   totalNodes   healthy   AGE
    409bf491f7136a8a  4              4            true      6h1m
    ```

    以上信息说明:

    - NAME 表示该 ScaleoutLeafGroup 的名称， 通过对该组内的所有交换机名称进行哈希算法得到
    - healthyNodes 表示该分组内健康的节点数量
    - totalNodes 表示该分组内节点的总数
    - healthy 表示该分组是否健康，如果组内有一个节点不健康，则该分组不健康
    - AGE 表示该分组的创建时间

如下是一个 ScaleoutLeafGroup CRD 示例：

```bash
~# kubectl get scaleoutleafgroups.unifabric.io 409bf491f7136a8a -o yaml
apiVersion: unifabric.io/v1beta1
kind: ScaleoutLeafGroup
metadata:
  creationTimestamp: "2025-09-18T03:37:59Z"
  generation: 1
  name: 409bf491f7136a8a
  resourceVersion: "85472900"
  uid: e8d34e3a-d73f-4587-b39a-9f80a72631c0
spec: {}
status:
  healthy: true
  nodes:
  - healthy: true
    name: sh-cube-master-1
  - healthy: true
    name: sh-cube-master-2
  - healthy: true
    name: sh-cube-master-3
  - healthy: true
    name: sh-inf-worker-1
  healthyNodes: 4
  totalNodes: 4
  switches:
  - LEAF01
  - LEAF02
  - LEAF03
  - LEAF04
```

如上 status 输出说明：

- healthy: 表示该分组是否健康，如果组内有一个节点不健康，则该分组不健康
- nodes: 表示该分组包含的节点列表，其中每个节点都有 healthy 字段表示该节点的 RDMA 链路是否正常
- healthyNodes: 表示该分组内健康的节点数量
- totalNodes: 表示该分组内节点的总数
- switches: 表示该分组包含所有节点连接的交换机列表

当节点在该分组中时，并且 RDMA 链路正常时（healthy 为 true），unifabric 会为该节点打上 dce.unifabric.io/scaleoutleaf-group 标签，value 为该分组的名称。

```bash
~# kubectl get nodes -l dce.unifabric.io/scaleoutleaf-group=409bf491f7136a8a
NAME               STATUS   ROLES                      AGE    VERSION
sh-cube-master-1   Ready    control-plane,fluent,gpu    130d   v1.30.5
sh-cube-master-2   Ready    control-plane,gpu          130d   v1.30.5
sh-cube-master-3   Ready    control-plane,gpu          130d   v1.30.5
sh-inf-worker-1    Ready    gpu                        130d   v1.30.5
```

如果节点从该分组中被移除，或者 RDMA 链路不正常时（healthy 为 false），unifabric 会移除该节点的 dce.unifabric.io/scaleoutleaf-group 标签。

## 存储主机邻居上报

存储主机邻居上报功能将通过 RDMA 链路状态监控，实现对存储主机设备的拓扑发现和状态监控，为构建完整的网络拓扑视图提供关键的基础设施层信息。

> **注意:** 此功能计划在后续版本中实现。

## 交换机邻居上报

> **注意:** 此功能计划在后续版本中实现，当前为功能规划和设计说明。

交换机邻居上报功能将通过 gnmi 协议和交换机管理接口，实现对 RDMA 交换机设备的拓扑发现和状态监控，为构建完整的网络拓扑视图提供关键的基础设施层信息。

### 故障排查

参考 [Troubleshooting](Troubleshooting.md)
