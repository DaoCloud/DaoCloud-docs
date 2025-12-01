# RDMA 延时监控使用指南

## 背景介绍

### 什么是 RDMA 延时监控

RDMA 延时监控是 Unifabric 提供的一项网络性能监控功能,用于持续监控 Kubernetes 集群中 RDMA 网络的延时性能。该功能通过在集群节点间自动执行 RDMA 延时测试,帮助运维人员:

- **及时发现网络性能问题:** 持续监控延时变化,快速识别网络性能退化
- **验证网络拓扑:** 通过延时测试验证网络拓扑配置是否正确
- **定位故障节点:** 精确定位出现延时异常的节点和网卡
- **优化网络配置:** 为网络优化提供数据支持

### 工作原理

每个节点的 unifabric-agent 包含一个独立的 `rdma-latency` 容器,负责:

1. **启动 RDMA 测试服务端:** 在每个 RDMA 网卡上启动 ib_write_lat 和 ib_read_lat 服务端进程
2. **生成测试任务:** 根据配置的策略(none/topo)自动生成节点间的延时测试任务
3. **执行延时测试:** 作为客户端连接其他节点的服务端,执行 RDMA Write/Read 延时测试
4. **导出监控指标:** 将测试结果以 Prometheus 指标格式暴露,供监控系统采集

### 主要特性

- **自动化测试:** 基于 ScaleoutLeafGroup 拓扑信息自动生成测试任务
- **多种测试策略:** 支持 `none`(简单配对)和 `topo`(基于拓扑)两种策略
- **全面覆盖:** 测试组内同轨、组内跨轨、跨组同轨等多种网络路径
- **双向测试:** 同时测试 RDMA Write 和 RDMA Read 延时
- **Prometheus 集成:** 测试结果通过 Prometheus 指标暴露,便于监控告警
- **持续监控:** 定期执行测试,及时发现性能退化

## 测试方案

### 测试策略概述

RDMA 延时监控支持两种测试策略:

| 策略     | 适用场景                  | 前置条件                                           | 测试复杂度 |
| -------- | ------------------------- | -------------------------------------------------- | ---------- |
| **none** | 小规模集群,简单网络拓扑   | 无                                                 | 低         |
| **topo** | 大规模集群,需要精细化监控 | 需要依赖 RDMA 邻居发现功能(ScaleoutLeafGroup 资源) | 高         |

### None 策略(简单配对)

#### 测试逻辑

- 将所有节点按字典序排序
- 节点两两配对进行测试(0-1, 2-3, 4-5...)
- 如果节点总数为奇数:
    - 3个节点:节点0测试节点1和2
    - 大于3个节点: 第一个节点额外测试最后一个节点

#### 客户端和服务端角色

在 none 策略下,每对节点中:

- **服务端:** 字典序较大的节点(如 node-2, node-4)
- **客户端:** 字典序较小的节点(如 node-1, node-3)

#### 示例(4个节点)

```
客户端 node-1 → 服务端 node-2 (测试所有同网段的 RDMA 网卡对)
客户端 node-3 → 服务端 node-4 (测试所有同网段的 RDMA 网卡对)
```

### Topo 策略(基于拓扑)

#### 前置条件

集群中必须存在 `ScaleoutLeafGroup` 资源,该资源通过 LLDP 邻居发现自动创建,定义了节点的分组和拓扑关系。

#### 测试场景

Topo 策略包含三种测试场景,覆盖不同的网络路径:

##### 场景1: 组内同轨测试(Intra-Group Same-Rail)

**测试目标:** 验证同一 Leaf 交换机下,相同网段(轨道)的节点间延时

**轨道定义:** 具有相同 IP 网段的网卡属于同一轨道或网卡名称一致的为相同轨道

- 例如:172.17.3.0/24 网段为轨道1,172.17.4.0/24 网段为轨道2

**测试范围:** 组内所有节点两两配对,测试相同轨道的网卡

**客户端和服务端:**

- 每个节点既是客户端也是服务端
- 节点 A 作为客户端测试节点 B
- 节点 B 作为客户端测试节点 A

**网络路径:** 流量经过同一个 Leaf 交换机

**示例:**

```
ScaleoutLeafGroup: group-1 (连接到 Leaf-1)
  节点: node-1, node-2, node-3, node-4

测试对(轨道1: 172.17.3.0/24):
  客户端 node-1 (172.17.3.141) → 服务端 node-2 (172.17.3.142)
  客户端 node-3 (172.17.3.143) → 服务端 node-4 (172.17.3.144)
```

**指标标签:**  `latency_type="sameleaf_samerail"`

##### 场景2: 组内跨轨测试(Intra-Group Cross-Rail)

**测试目标:** 验证同一 Leaf 交换机下,不同网段(轨道)的节点间延时

**测试范围:** 每组选择字典序第一个和最后一个节点进行跨轨测试

**客户端和服务端:** 

- **客户端:** 第一个节点(如 node-1)
- **服务端:** 最后一个节点(如 node-4)

**网络路径:** 流量可能经过 Spine 交换机(取决于 Leaf 交换机配置)

**示例:** 

```
ScaleoutLeafGroup: group-1
  节点: node-1, node-2, node-3, node-4

测试对(跨轨道):
  客户端 node-1 (轨道1: 172.17.1.141) → 服务端 node-4 (轨道2: 172.17.2.144)
  客户端 node-1 (轨道1: 172.17.1.141) → 服务端 node-4 (轨道3: 172.17.3.144)
  客户端 node-1 (轨道1: 172.17.1.141) → 服务端 node-4 (轨道4: 172.17.4.144)
  客户端 node-1 (轨道2: 172.17.2.142) → 服务端 node-4 (轨道1: 172.17.1.144)
  客户端 node-1 (轨道2: 172.17.2.142) → 服务端 node-4 (轨道3: 172.17.3.144)
  客户端 node-1 (轨道2: 172.17.2.142) → 服务端 node-4 (轨道4: 172.17.4.144)
  ...
```

**指标标签:**  `latency_type="sameleaf_crossrail"`

##### 场景3: 跨组同轨测试(Cross-Group Same-Rail)

**测试目标:** 验证不同 Leaf 交换机之间,相同网段(轨道)的节点间延时

**前置条件:** 至少有2个 ScaleoutLeafGroup

**测试范围:** 每组选择字典序第一个节点,与其他组的字典序第一个节点进行测试

**客户端和服务端:**

- 每个组的字典序第一个节点是客户端
- 其他组的字典序第一个节点是服务端
- 组间节点相互测试

**网络路径:** 流量经过 Spine 交换机

**示例:**

```
ScaleoutLeafGroup: group-1 (连接到 Leaf-1)
  节点: node-1, node-2, node-3, node-4
  测试节点: node-1

ScaleoutLeafGroup: group-2 (连接到 Leaf-2)
  节点: node-5, node-6, node-7, node-8
  测试节点: node-5

测试对:

轨道1: 172.17.1.0/24:
  客户端 node-1 (172.17.1.141) → 服务端 node-5 (172.17.1.145)
轨道2: 172.17.2.0/24:
  客户端 node-1 (172.17.2.142) → 服务端 node-5 (172.17.2.145)
轨道3: 172.17.3.0/24:
  客户端 node-1 (172.17.3.143) → 服务端 node-5 (172.17.3.145)
轨道4: 172.17.4.0/24:
  客户端 node-1 (172.17.4.144) → 服务端 node-5 (172.17.4.145)
```

**指标标签:**  `latency_type="crossgroup_samerail"`

### 监控指标格式

所有测试结果通过 Prometheus 指标暴露:

#### 指标名称

```
unifaric_rdma_latency_us
```

#### 指标类型

**Gauge** - 表示最近一次测试的平均延时值(微秒)

#### 指标标签

| 标签名               | 说明                           | 示例值                                                             |
| -------------------- | ------------------------------ | ------------------------------------------------------------------ |
| `source_node`        | 源节点(客户端)名称             | `node-1`                                                           |
| `source_rdma_device` | 源节点 RDMA 设备名             | `mlx5_0`                                                           |
| `source_ifname`      | 源节点网卡接口名               | `ens841np0`                                                        |
| `source_ip`          | 源节点 IP 地址                 | `172.17.3.141`                                                     |
| `target_node`        | 目标节点(服务端)名称           | `node-2`                                                           |
| `target_rdma_device` | 目标节点 RDMA 设备名           | `mlx5_0`                                                           |
| `target_ifname`      | 目标节点网卡接口名             | `ens841np0`                                                        |
| `target_ip`          | 目标节点 IP 地址               | `172.17.3.142`                                                     |
| `source_group`       | 源节点所属 ScaleoutLeafGroup   | `group-1`                                                          |
| `target_group`       | 目标节点所属 ScaleoutLeafGroup | `group-1`                                                          |
| `latency_type`       | 延时测试类型                   | `sameleaf_samerail` / `sameleaf_crossrail` / `crossgroup_samerail` |
| `test_strategy`      | 测试策略                       | `pairwise` / `topo`                                                |
| `state`              | 测试状态                       | `success` / `failed`                                               |
| `error_msg`          | 错误信息(仅失败时)             | `connection timeout`                                               |

#### 指标示例

**成功的同轨测试:**

```prometheus
unifaric_rdma_latency_us{
  source_node="node-1",
  source_rdma_device="mlx5_0",
  source_ifname="ens841np0",
  source_ip="172.17.3.141",
  target_node="node-2",
  target_rdma_device="mlx5_0",
  target_ifname="ens841np0",
  target_ip="172.17.3.142",
  source_group="group-1",
  target_group="group-1",
  latency_type="sameleaf_samerail",
  test_strategy="topo",
  state="success",
  error_msg=""
} 2.45
```

**失败的跨轨测试:**

```prometheus
unifaric_rdma_latency_us{
  source_node="node-3",
  source_rdma_device="mlx5_0",
  source_ifname="ens841np0",
  source_ip="172.17.3.143",
  target_node="node-4",
  target_rdma_device="mlx5_1",
  target_ifname="ens842np0",
  target_ip="172.17.4.144",
  source_group="group-1",
  target_group="group-1",
  latency_type="sameleaf_crossrail",
  test_strategy="topo",
  state="failed",
  error_msg="connection timeout"
} 0
```

## 配置和安装

### 配置示例

#### 小规模集群(none 策略)

```yaml
features:
  rdmaLatencyDetection:
    interval: 3m
    workers: 3
    gpuNetwork:
      enabled: true
      strategy: pairwise
    testServerPorts: "20000-20017"
```

#### 大规模集群(topo 策略)

```yaml
features:
  rdmaNeighbor:
    enabled: true
    enableScaleOutLeafGroup: true
    gpuRdmaNicFilter: "interface=ens*"

  rdmaLatencyDetection:
    interval: 5m
    workers: 10
    gpuNetwork:
      enabled: true
      strategy: topo
    testServerPorts: "20000-20017"
```

Helm 配置参数说明:

| 参数                     | 类型   | 默认值          | 说明                                                     |
| ------------------------ | ------ | --------------- | -------------------------------------------------------- |
| `interval`               | string | `"5m"`          | 测试间隔,支持 s/m/h 单位                                 |
| `workers`                | int    | `5`             | 并发执行测试的 worker 数量                               |
| `gpuNetwork.enabled`     | bool   | `true`          | 是否启用 GPU RDMA 网络延时检测                           |
| `gpuNetwork.strategy`    | string | `"topo"`        | GPU 网络测试策略:`pairwise`(两两配对)或 `topo`(基于拓扑) |
| `storageNetwork.enabled` | bool   | `true`          | 是否启用存储 RDMA 网络延时检测                           |
| `testServerPorts`        | string | `"20000-20010"` | RDMA 测试服务端端口范围                                  |
| `metrics.port`           | int    | `5027`          | Prometheus 指标暴露端口                                  |

!!! note

    - 如果 strategy 设置为 topo,则需要确保 features.rdmaNeighbor.enableScaleOutLeafGroup 设置为 true
    - 为正常启动 RDMA 延时测试 Server，需要确保 testServerPorts 配置足够的端口范围，并避免端口冲突。至少为每个 RDMA 网卡准备两个端口，一个用于 ib_write_lat，一个用于 ib_read_lat。比如 RDMA 网卡数量为 9，那么至少需要 18 个端口。

### 安装步骤

#### 安装或更新 Helm Chart

```bash
# 或更新现有安装
helm upgrade unifabric ./chart \
  --namespace unifabric-system \
  -f values.yaml
```

> 默认情况下，RDMA 延时检测基于 topo 策略，需要确保 features.rdmaNeighbor.enableScaleOutLeafGroup 设置为 true。

## 验证

### 容器架构

unifabric-agent Pod 包含 **3个容器:**

```
unifabric-agent Pod
├── lldpd (容器)          # LLDP 邻居发现服务
├── agent (容器)          # 主业务逻辑,管理 FabricNode 等资源
└── rdma-latency (容器)  # RDMA 延时检测服务(独立容器)
```

**rdma-latency 容器职责:**

- 启动 RDMA 测试服务端(ib_write_lat, ib_read_lat)
- 执行延时测试任务
- 暴露 Prometheus 指标(5027端口)

### 检查 Pod 状态

```bash
# 检查 Pod 状态
kubectl get pods -n unifabric-system -l app=unifabric-agent

# 预期输出:
NAME                      READY   STATUS    RESTARTS   AGE
unifabric-agent-xxxxx     3/3     Running   0          5m
```

**注意:**  `READY` 列应显示 `3/3`，表示所有 3 个容器都已就绪。

### 检查 ScaleoutLeafGroup CRD 是否正常，一个 ScaleoutLeafGroup 对象代表一组具有相同 GPU 网络拓扑的节点。

```bash
~# kubectl get scaleoutleafgroups.unifabric.io
NAME              healthyNodes   totalNodes   healthy   AGE
409bf491f7136a8a  4              4            true      6h1m
```

检查 scaleoutleafgroups 的 healthy 是否为 true, 这表明 Unifabric 已经正确收集到所有节点的 GPU 网络拓扑信息。

### 查看指标

#### 方法1: 通过 Port-Forward 查看

```bash
# 转发指标端口
kubectl port-forward -n unifabric-system <pod-name> 5027:5027

# 在另一个终端查看指标
curl http://localhost:5027/metrics | grep unifaric_rdma_latency_us
...
unifabric_rdma_latency_us{error_msg="",latency_type="sameleaf_samerail",source_group="409bf491f7136a8a",source_ifname="ens834np0",source_ip="172.17.1.141",source_node="sh-cube-master-1",source_rdma_device="mlx5_4",state="success",target_group="409bf491f7136a8a",target_ifname="ens834np0",target_ip="172.17.1.142",target_node="sh-cube-master-2",target_rdma_device="mlx5_4",test_strategy="topo"} 2.994644
unifabric_rdma_latency_us{error_msg="",latency_type="sameleaf_samerail",source_group="409bf491f7136a8a",source_ifname="ens834np0",source_ip="172.17.1.142",source_node="sh-cube-master-2",source_rdma_device="mlx5_4",state="success",target_group="409bf491f7136a8a",target_ifname="ens834np0",target_ip="172.17.1.141",target_node="sh-cube-master-1",target_rdma_device="mlx5_4",test_strategy="topo"} 5.515484
...
```

以上输出说明：

- `unifaric_rdma_latency_us`：RDMA 延时指标为 2.994644 us
- `error_msg`：错误信息(仅失败时)
- `latency_type`：测试类型
- `source_group`：源节点组
- `source_ifname`：源网卡接口名称
- `source_ip`：源节点 IP
- `source_node`：源节点名称
- `source_rdma_device`：源 RDMA 设备名称
- `state`：测试状态
- `target_group`：目标节点组
- `target_ifname`：目标网卡接口名称
- `target_ip`：目标节点 IP
- `target_node`：目标节点名称
- `target_rdma_device`：目标 RDMA 设备名称
- `test_strategy`：测试策略
- `latency_type`：测试类型

#### 方法2: 通过 Prometheus 查看

在 Prometheus UI 中执行查询:

```promql
# 查看所有指标
unifaric_rdma_latency_us

# 查看成功的测试
unifaric_rdma_latency_us{state="success"}

# 查看失败的测试
unifaric_rdma_latency_us{state="failed"}
```

### 验证同轨指标

**同轨测试**指标特征:

- `latency_type="sameleaf_samerail"`
- `source_ip` 和 `target_ip` 在同一网段
- 延时值通常较低(< 5 微秒)

```promql
# 查询同轨测试
unifaric_rdma_latency_us{latency_type="sameleaf_samerail", state="success"}
```

**示例输出:** 

```
unifaric_rdma_latency_us{
  source_node="node-1",
  source_ip="172.17.3.141",
  target_node="node-2",
  target_ip="172.17.3.142",
  latency_type="sameleaf_samerail",
  state="success"
} 2.3
```

### 验证跨轨指标

**跨轨测试**指标特征:

- `latency_type="sameleaf_crossrail"`
- `source_ip` 和 `target_ip` 在不同网段
- 延时值通常较高(5-15 微秒)

```promql
# 查询跨轨测试
unifaric_rdma_latency_us{latency_type="sameleaf_crossrail", state="success"}
```

**示例输出:**

```
unifaric_rdma_latency_us{
  source_node="node-3",
  source_ip="172.17.3.143",
  target_node="node-4",
  target_ip="172.17.4.144",
  latency_type="sameleaf_crossrail",
  state="success"
} 8.7
```

## 运维故障排查

### PromQL 查询示例

1. 查看所有成功的延时测试

    ```promql
    unifaric_rdma_latency_us{state="success"}
    ```

1. 查看特定节点的延时

    ```promql
    unifaric_rdma_latency_us{source_node="node-1", state="success"}
    ```

1. 查看组内同轨延时

    ```promql
    unifaric_rdma_latency_us{latency_type="sameleaf_samerail", state="success"}
    ```

1. 查看跨轨延时(可能较高)

    ```promql
    unifaric_rdma_latency_us{latency_type="sameleaf_crossrail", state="success"}
    ```

1. 查看失败的测试

    ```promql
    unifaric_rdma_latency_us{state="failed"}
    ```

1. 计算平均延时

    ```promql
    avg(unifabric_rdma_latency_us{state="success", latency_type="sameleaf_samerail"})
    ```

1. 查找延时异常高的路径(>10微秒)

    ```promql
    unifaric_rdma_latency_us{state="success"} > 10
    ```

### 容器无法启动

#### 问题现象

```bash
kubectl get pods -n unifabric-system -l app=unifabric-agent
# 输出显示: READY 2/3 或 CrashLoopBackOff
```

#### 排查步骤

**步骤1: 检查容器状态**

```bash
# 查看 Pod 详情
kubectl describe pod -n unifabric-system <pod-name>

# 查看 rdma-latency 容器日志
kubectl logs -n unifabric-system <pod-name> -c rdmalatency --tail=100
```

**步骤2: 常见错误和解决方法**

##### 错误1: 端口冲突

**错误信息:**

```
failed to start RDMA test servers: failed to start server on mlx5_0:
address already in use
```

**原因:**  配置的端口范围与其他服务冲突

**解决方法:**

```yaml
# 修改 values.yaml,调整端口范围
features:
  rdmaLatencyDetection:
    testServerPorts: "21000-22000" # 使用不同的端口范围
```

```bash
# 更新配置
helm upgrade unifabric ./chart -n unifabric-system -f values.yaml
```

##### 错误2: RDMA 设备不存在

**错误信息:**

```
failed to start RDMA test servers: no RDMA devices found
```

**原因:**  节点没有 RDMA 网卡或网卡未正确识别

**排查方法:**

```bash
# 在节点上检查 RDMA 设备
kubectl exec -n unifabric-system <pod-name> -c rdmalatency -- ibv_devices

# 检查 FabricNode 资源
kubectl get fabricnode <node-name> -o yaml | grep -A 20 gpuNics
```

##### 错误3: 权限不足

**错误信息:**

```
failed to start RDMA test servers: permission denied
```

**原因:**  Pod 没有足够的权限访问 RDMA 设备

**解决方法:**  确保 DaemonSet 配置了 `hostNetwork: true` 和适当的 securityContext

### 调整日志级别

如需更详细的日志进行排查:

```yaml
# 修改 values.yaml
agent:
  config:
    logLevel: 7 # 0=info, 3=debug, 7=trace
```

```bash
# 更新配置
helm upgrade unifabric ./chart -n unifabric-system -f values.yaml

# 查看详细日志
kubectl logs -n unifabric-system <pod-name> -c rdma-latency -f
```

### 没有生成任何指标

**可能原因:**

1. RDMA 延时检测未启用
2. 没有找到 RDMA 网卡
3. 使用 topo 策略但没有 ScaleoutLeafGroup

**排查步骤:**

```bash
# 1. 检查配置
kubectl get cm -n unifabric-system unifabric -o yaml

# 2. 检查 FabricNode 是否有 RDMA 网卡信息
kubectl get fabricnode <node-name> -o yaml

# 3. 查看日志，检查 Metrcis Server 是否正常启动
kubectl logs -n unifabric-system daemonset/unifabric-agent -c rdmalatency
```

### 指标显示测试失败(state=failed)

#### 问题现象

```promql
unifaric_rdma_latency_us{state="failed"} > 0
```

#### 排查步骤

**步骤1: 查看错误信息**

```promql
# 查看失败指标的 error_msg 标签
unifaric_rdma_latency_us{state="failed"}
```

**常见错误信息:**

##### 错误1: connection timeout

**原因:**  目标节点的服务端未启动或网络不通

**排查方法:** 

```bash
# 1. 检查目标节点的 rdma-latency 容器状态
kubectl get pods -n unifabric-system -l app=unifabric-agent -o wide | grep <target-node>

# 2. 检查目标节点的服务端进程
kubectl exec -n unifabric-system <target-pod-name> -c rdma-latency -- \
  ps aux | grep ib_write_lat

# 3. 检查端口监听
kubectl exec -n unifabric-system <target-pod-name> -c rdma-latency -- \
  netstat -tlnp | grep 20000

# 4. 手动测试 RDMA 连接
kubectl exec -n unifabric-system <source-pod-name> -c rdma-latency -- \
  ib_write_lat -d mlx5_0 -p 20000 <target-ip>
```

##### 错误2: no route to host

**原因:**  网络不通或防火墙阻止

**排查方法:**

```bash
# 1. 测试网络连通性
kubectl exec -n unifabric-system <source-pod-name> -c rdma-latency -- \
  ping -c 3 <target-ip>

# 2. 检查防火墙规则
kubectl exec -n unifabric-system <source-pod-name> -c rdma-latency -- \
  iptables -L -n | grep 20000

# 3. 检查路由
kubectl exec -n unifabric-system <source-pod-name> -c rdma-latency -- \
  ip route get <target-ip>
```
