# NUMA 亲和性调度

NUMA 节点是 Non-Uniform Memory Access（非统一内存访问）架构中的一个基本组成单元，一个 Node 节点是多个 NUMA 节点的集合，
在多个 NUMA 节点之间进行内存访问时会产生延迟，开发者可以通过优化任务调度和内存分配策略，来提高内存访问效率和整体性能。

## 使用场景

Numa 亲和性调度的常见场景是那些对 CPU 参数敏感/调度延迟敏感的计算密集型作业。如科学计算、视频解码、动漫动画渲染、大数据离线处理等具体场景。

## 调度策略

Pod 调度时可以采用的 NUMA 放置策略，具体策略对应的调度行为请参见 Pod 调度行为说明。

- single-numa-node：Pod 调度时会选择拓扑管理策略已经设置为 single-numa-node 的节点池中的节点，且 CPU 需要放置在相同 NUMA 下，如果节点池中没有满足条件的节点，Pod 将无法被调度。
- restricted：Pod 调度时会选择拓扑管理策略已经设置为 restricted 节点池的节点，且 CPU 需要放置在相同的 NUMA 集合下，如果节点池中没有满足条件的节点，Pod 将无法被调度。
- best-effort：Pod 调度时会选择拓扑管理策略已经设置为 best-effort 节点池的节点，且尽量将 CPU 放置在相同 NUMA 下，如果没有节点满足这一条件，则选择最优节点进行放置。

## 调度原理

当Pod设置了拓扑策略时，Volcano 会根据 Pod 设置的拓扑策略预测匹配的节点列表。
调度过程如下：

1. 根据 Pod 设置的 Volcano 拓扑策略，筛选具有相同策略的节点。
  
2. 在设置了相同策略的节点中，筛选 CPU 拓扑满足该策略要求的节点进行调度。

| Pod 可配置的拓扑策略 | 1. 根据 Pod 设置的拓扑策略，筛选可调度的节点 | 2. 进一步筛选 CPU 拓扑满足策略的节点进行调度 |
|------------------|----------------------------------------|-----------------------------------------|
| none             | 针对配置了以下几种拓扑策略的节点，调度时均无筛选行为。none：可调度；best-effort：可调度；restricted：可调度；single-numa-node：可调度 | - |
| best-effort      | 筛选拓扑策略同样为“best-effort”的节点：none：不可调度；best-effort：可调度；restricted：不可调度；single-numa-node：不可调度 | 尽可能满足策略要求进行调度：优先调度至单 NUMA 节点，如果单 NUMA 节点无法满足 CPU 申请值，允许调度至多个 NUMA 节点。|
| restricted       | 筛选拓扑策略同样为“restricted”的节点：none：不可调度；best-effort：不可调度；restricted：可调度；single-numa-node：不可调度 | 严格限制的调度策略：单 NUMA 节点的CPU容量上限大于等于 CPU 的申请值时，仅允许调度至单 NUMA 节点。此时如果单 NUMA 节点剩余的 CPU 可使用量不足，则 Pod 无法调度。单 NUMA 节点的 CPU 容量上限小于 CPU 的申请值时，可允许调度至多个 NUMA 节点。 |
| single-numa-node | 筛选拓扑策略同样为“single-numa-node”的节点：none：不可调度；best-effort：不可调度；restricted：不可调度；single-numa-node：可调度 | 仅允许调度至单 NUMA 节点。|

## 配置 NUMA 亲和调度策略

1. 在 Job 中配置 policies

    ```yaml 
    task: 
      - replicas: 1 
        name: "test-1" 
        topologyPolicy: single-numa-node 
      - replicas: 1 
        name: "test-2" 
        topologyPolicy: best-effort 
    ```

2. 修改 kubelet 的调度策略，设置 `--topology-manager-policy` 参数，支持的策略有四种：
  
    - `none`（默认）
    - `best-effort`
    - `restricted`
    - `single-numa-node`


## 使用案例

1. 示例一：在无状态工作负载中配置 NUMA 亲和性。 <a id="eg1" />

    ```yaml  
    kind: Deployment  
    apiVersion: apps/v1  
    metadata:  
      name: numa-tset  
    spec:  
      replicas: 1  
      selector:  
        matchLabels:  
          app: numa-tset  
      template:  
        metadata:  
          labels:  
            app: numa-tset  
          annotations:  
            volcano.sh/numa-topology-policy: single-numa-node    # set the topology policy  
        spec:  
          containers:  
            - name: container-1  
              image: nginx:alpine  
              resources:  
                requests:  
                  cpu: 2           # 必须为整数，且需要与limits中一致  
                  memory: 2048Mi  
                limits:  
                  cpu: 2           # 必须为整数，且需要与requests中一致  
                  memory: 2048Mi  
          imagePullSecrets:  
          - name: default-secret
    ```

2. 示例二：创建一个 Volcano Job，并使用 NUMA 亲和性。<a id="eg2" />

    ```yaml  
    apiVersion: batch.volcano.sh/v1alpha1  
    kind: Job  
    metadata:  
      name: vj-test  
    spec:  
      schedulerName: volcano  
      minAvailable: 1  
      tasks:  
        - replicas: 1  
          name: "test"  
          topologyPolicy: best-effort   # set the topology policy for task  
          template:  
            spec:  
              containers:  
                - image: alpine  
                  command: ["/bin/sh", "-c", "sleep 1000"]  
                  imagePullPolicy: IfNotPresent  
                  name: running  
                  resources:  
                    limits:  
                      cpu: 20  
                      memory: "100Mi"  
              restartPolicy: OnFailure
    ```

### NUMA 调度分析

假设 NUMA 节点情况如下：

| 工作节点 | 节点策略拓扑管理器策略 | NUMA 节点 0 上的可分配 CPU | NUMA 节点 1 上的可分配 CPU |
|--------|------------------|---------------------|---------------------|
| node-1 | single-numa-node | 16U                 | 16U                 |
| node-2 | best-effort      | 16U                 | 16U                 |
| node-3 | best-effort      | 20U                 | 20U                 |

- [示例一](#eg1)中，Pod 的 CPU 申请值为 2U，设置拓扑策略为“single-numa-node”，因此会被调度到相同策略的 node-1。
- [示例二](#eg2)中，Pod 的 CPU 申请值为20U，设置拓扑策略为“best-effort”，它将被调度到 node-3，
  因为 node-3 可以在单个 NUMA 节点上分配 Pod 的 CPU 请求，而 node-2 需要在两个 NUMA 节点上执行此操作。

### 查看当前节点的 CPU 概况 

您可以通过 lscpu 命令查看当前节点的 CPU 概况：

```sh 
lscpu 
... 
CPU(s): 32 
NUMA node(s): 2 
NUMA node0 CPU(s): 0-15 
NUMA node1 CPU(s): 16-31
```

### 查看当前节点的 CPU 分配  
  
然后查看 NUMA 节点使用情况：

```sh
# 查看当前节点的 CPU 分配
cat /var/lib/kubelet/cpu_manager_state
{"policyName":"static","defaultCpuSet":"0,10-15,25-31","entries":{"777870b5-c64f-42f5-9296-688b9dc212ba":{"container-1":"16-24"},"fb15e10a-b6a5-4aaa-8fcd-76c1aa64e6fd":{"container-1":"1-9"}},"checksum":318470969}
```

以上示例中表示，节点上运行了两个容器，一个占用了 NUMA node0 的1-9 核，另一个占用了 NUMA node1 的 16-24 核。
