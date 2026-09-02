# Kubernetes DRA 进阶指南：六大特性让异构资源管理更灵活

## 写在前面

如果你用过 Kubernetes 管理 GPU、网卡这类硬件设备，一定听说过 DRA（动态资源分配）。简单来说，DRA 就是 Kubernetes 里的"硬件资源管家"——以前 Pod 申请 GPU 只能"整块拿走"，现在 DRA 让这件事变得更精细、更灵活。

这篇文章不讲 DRA 入门概念，而是聚焦六个**进阶特性**。它们解决的都是实际生产中会碰到的问题：

- 一块 GPU 能不能拆成多份给不同 Pod 用？
- 怎么避免把"打架"的设备模式分配到一起？
- 网络带宽能不能像 CPU 内存一样按需共享？
- 安全上能不能做到"谁在哪个节点上改什么"都管得住？
- 纯控制平面的资源，能不能不在每个节点上都装驱动？
- 容器里的应用怎么知道自己拿到了什么设备？

读完这篇文章，你会对 DRA 的能力边界有更清晰的认识，也能更好地判断哪些特性能用在你的场景里。

> 文中每个特性都会标注对应的特性门控（Feature Gate），方便你在集群中按需开启。

## 一、可分区设备：把一块硬件拆成多份来用

### 它解决什么问题

想象一下，你有一张 8GB 显存的 GPU，但你的应用每次只用 2GB。如果只能整块分配，显存利用率就很低。能不能像切蛋糕一样，把一块物理设备切成多个逻辑设备，按需分配给不同的 Pod？

**可分区设备**（Partitionable Devices）就是干这个的。它允许 DRA 驱动把底层物理设备的资源（比如 GPU 显存、计算单元）拆成多份，以"逻辑设备"的形式对外提供。

### 核心概念：CounterSet（计数器集）

在 DRA 里，物理设备的可消耗资源用 **CounterSet** 来记录。你可以把它理解成一个"资源账本"：

- **CounterSet** 是一组命名计数器，比如 `gpu-memory` 表示 GPU 显存总量
- 每个逻辑设备声明自己要"消耗"多少计数器（就像在账本上记一笔支出）
- 调度器负责算账，确保所有逻辑设备加起来不超过物理总量

打个比方：CounterSet 就像一张公交卡的余额，每个逻辑设备就是一次乘车扣费，调度器保证余额不会被扣成负数。

> CounterSet 和设备必须定义在不同的 ResourceSlice 里，但它们必须属于同一个资源池（pool），设备才能"花"那个 CounterSet 里的资源。

### 来看个例子

下面的 YAML 展示了一张 8Gi 显存的 GPU，被拆成两个各占 6Gi 的逻辑设备。因为 6 + 6 > 8，所以同一时间只能分配其中一个——调度器会自动处理这个互斥关系，上层的 ResourceClaim 完全感知不到。

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: resourceslice-with-countersets
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 2
  driver: dra.example.com
  sharedCounters:
  - name: gpu-1-counters
    counters:
      memory:
        value: 8Gi
---
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: resourceslice-with-devices
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 2
  driver: dra.example.com
  devices:
  - name: device-1
    consumesCounters:
    - counterSet: gpu-1-counters
      counters:
        memory:
          value: 6Gi
  - name: device-2
    consumesCounters:
    - counterSet: gpu-1-counters
      counters:
        memory:
          value: 6Gi
```

**怎么开启**：可分区设备由 `kube-apiserver` 和 `kube-scheduler` 中的 [`DRAPartitionableDevices` 特性门控](https://kubernetes.io/zh-cn/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)控制。

## 二、设备兼容性组：别让不兼容的设备模式"打架"

### 它解决什么问题

设备能分区之后，又冒出了新问题：同一张 GPU 可能支持多种工作模式（比如 NVIDIA 的 MIG 模式和 vGPU 模式），这两种模式是**互斥**的——GPU 要么跑在 MIG 模式下，要么跑在 vGPU 模式下，不能同时跑两种。

如果调度器只看计数器（显存够不够），可能会把一个 MIG 设备和一个 vGPU 设备分配到同一张 GPU 上。结果呢？到了节点上真正准备设备的时候才发现不行，Pod 就启动失败了。

**设备兼容性组**（Device Compatibility Groups）就是为了提前规避这种问题。它让驱动告诉调度器："哪些设备是一伙的，哪些不能在一起"，调度器在调度阶段就把不兼容的组合过滤掉。

> 这个特性依赖[可分区设备](#一可分区设备)，因为 `compatibilityGroups` 字段就放在 `device.consumesCounters[]` 上面。两个特性门控都得开。

### 工作原理：求交集

规则其实很简单，就一句话：**从同一个计数器集拿资源的多个设备，它们的兼容性组必须有交集才能共存**。

具体来说：

- 每个设备的 `consumesCounters` 条目可以带一个 `compatibilityGroups` 列表，最多写 2 个组名
- 组名就是个标签，Kubernetes 不关心它叫什么，只看名字对不对得上
- 调度器检查所有待分配设备的组名，如果它们的交集是空集，就拒绝这个分配方案

还有几个细节要注意：

- **没分组的设备**：没有声明组的设备只能和同样没分组的设备在一起，不能和有组的设备混搭
- **跨声明也生效**：即使是两个不同的 ResourceClaim，只要它们从同一个计数器集拿设备，组的交集规则同样适用
- **按计数器集隔离**：不同 CounterSet 上的组互不影响

### 来看个例子

还是那张 8Gi 显存的 GPU，驱动发布了两个逻辑设备：一个走 MIG 模式，一个走 vGPU 模式，各占 4Gi。光看显存是够两个人分的，但模式不兼容。

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: gpu-counters
spec:
  nodeName: worker-1
  pool:
    name: gpu-pool
    generation: 1
    resourceSliceCount: 2
  driver: gpu.example.com
  sharedCounters:
  - name: gpu-0-memory
    counters:
      memory:
        value: 8Gi
---
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: gpu-devices
spec:
  nodeName: worker-1
  pool:
    name: gpu-pool
    generation: 1
    resourceSliceCount: 2
  driver: gpu.example.com
  devices:
  - name: gpu-0-mig
    consumesCounters:
    - counterSet: gpu-0-memory
      counters:
        memory:
          value: 4Gi
      compatibilityGroups:
      - mig
  - name: gpu-0-vgpu
    consumesCounters:
    - counterSet: gpu-0-memory
      counters:
        memory:
          value: 4Gi
      compatibilityGroups:
      - vgpu
```

如果一个 Pod 要申请两个设备，调度器会发现 `{"mig"} ∩ {"vgpu"} = ∅`（没有交集），直接拒绝这个组合。虽然显存够，但模式不兼容，不能放一起。

### 约束条件速查

- 每个 `consumesCounters[]` 条目最多写 **2** 个组名
- 同一个条目里的组名不能重复
- 组名只在同一个驱动的资源池内有意义
- 不同计数器集上的组互不干扰

### 版本偏差安全

如果你开启了这个特性又关掉了（alpha 阶段默认是关的），kube-apiserver 会在创建或更新 ResourceSlice 时把 `compatibilityGroups` 字段剥掉。调度器发现资源池里的设备"不完整"，就会跳过整个资源池，避免出问题。

注意 `null` 和空列表 `[]` 都等同于"没设置"，不会触发上面的跳过逻辑。

**怎么开启**：由 kube-apiserver 和 kube-scheduler 中的 [`DRADeviceCompatibilityGroups` 特性门控](https://kubernetes.io/zh-cn/docs/reference/command-line-tools-reference/feature-gates/#DRADeviceCompatibilityGroups)控制，同时需要启用 [`DRAPartitionableDevices` 特性门控](https://kubernetes.io/zh-cn/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)。

## 三、可消耗容量：一个设备多人共享用

### 它解决什么问题

前面说的"可分区设备"是把一块物理设备**预先切成**多个逻辑设备，每个 Pod 拿走一个完整的逻辑设备。

但有些场景不是这样的。比如一张网卡总带宽 10G，你可能想让 10 个 Pod 各用 1G——总容量是固定的，但 Pod 按需领取，领多少用多少，剩下的还能给别人用。

这就是**可消耗容量**（Consumable Capacity）要解决的问题。你可以把它理解成"设备版的 CPU/内存共享"：就像节点上的 CPU 可以按 milli 单位分给多个 Pod，设备上的带宽、算力也可以按容量分给多个 ResourceClaim。

### 核心概念

可消耗容量涉及两个关键字段：

- **`allowMultipleAllocations`**：在 ResourceSlice 的设备上设为 `true`，表示这台设备允许多个声明共享使用
- **`capacity`**：在 ResourceClaim 的请求里指定，告诉调度器你要消耗多少容量

调度器的职责就是记账——确保所有声明从一台设备上"拿走"的容量加起来，不超过设备的总容量。

驱动还可以通过 `requestPolicy` 规定容量的申请规则，比如最小申请多少、按什么步长递增。就像你去买奶茶，最小杯是中杯，大杯只能按固定规格升级。

### 来看个例子

下面是一张 10G 带宽的网卡，允许多次分配。带宽申请最少 1M，按 8 的倍数递增，默认值是 1M。

```yaml
kind: ResourceSlice
apiVersion: resource.k8s.io/v1
metadata:
  name: resourceslice
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 1
  driver: dra.example.com
  devices:
  - name: eth1
    allowMultipleAllocations: true
    attributes:
      name:
        string: "eth1"
    capacity:
      bandwidth:
        requestPolicy:
          default: "1M"
          validRange:
            min: "1M"
            step: "8"
        value: "10G"
```

用户在 ResourceClaimTemplate 里声明要 1G 带宽：

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: bandwidth-claim-template
spec:
  spec:
    devices:
      requests:
      - name: req-0
        exactly:
          deviceClassName: resource.example.com
          capacity:
            requests:
              bandwidth: 1G
```

分配成功后，结果里会告诉你实际消耗了多少容量，以及一个 `shareID` 标识这次共享分配：

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
...
status:
  allocation:
    devices:
      results:
      - consumedCapacity:
          bandwidth: 1G
        device: eth1
        shareID: "a671734a-e8e5-11e4-8fde-42010af09327"
```

有一点需要注意：如果资源池里既有"可多次分配"的设备，也有"整块分配"的设备，调度器可能选到整块的。如果你的业务必须用共享模式，可以加一条 CEL 筛选条件：`device.allowMultipleAllocations == true`。

### DistinctAttribute 约束

当你在一个 ResourceClaim 里申请多台设备时，**DistinctAttribute** 约束可以保证拿到的设备在某个属性上的值都不一样。

这有什么用呢？举两个例子：

- 你申请了 4 个可共享的 GPU 实例，不希望 4 个都落到同一张物理卡上——用 DistinctAttribute 按 `numa_node` 属性分散开
- 你申请多块网卡，希望它们来自不同的物理网卡而不是同一张的多个共享实例

简单说，这个约束就是帮你做"设备分布优化"的。

## 四、细粒度状态授权：谁能改什么，精确到节点

### 它解决什么问题

在 Kubernetes 里，RBAC 控制谁能对什么资源做什么操作。但对于 DRA 的 ResourceClaim 来说，光有"能不能改状态"这种粗粒度控制还不够。

为什么？因为更新 ResourceClaim 状态这件事，可能是调度器在做，也可能是某个节点上的 kubelet 在做。从安全角度看，理想状态是：**每个节点只能改跟自己相关的那部分状态**，而不是所有节点都有权力改所有 ResourceClaim 的状态。

从 Kubernetes v1.36 开始，DRA 引入了**细粒度状态授权**，通过合成子资源（synthetic subresources）和节点感知动词（node-aware verbs），把授权粒度做得更细。

这意味着什么呢？简单来说：

- 不是"允许/拒绝更新 ResourceClaim 状态"二选一了
- 可以精确控制"谁能更新哪些子资源"
- 还能控制"在哪些节点上才能更新"

这对多租户集群、零信任安全模型来说，是个很重要的安全加固。

**想深入了解**：包括调度器和 DRA 驱动的 RBAC 示例，可以参考官方的[加固指南 - 动态资源分配](https://kubernetes.io/zh-cn/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)。集群管理员的操作步骤在[在集群中加固动态资源分配](https://kubernetes.io/zh-cn/docs/tasks/administer-cluster/hardening-dra/)。

## 五、可选节点操作：控制平面资源不用每个节点装驱动

### 它解决什么问题

在 DRA 的标准流程里，每个节点上都要有对应的驱动插件，kubelet 通过 gRPC 调用驱动来准备/取消准备设备。这对 GPU、FPGA 这类确实需要节点本地操作的硬件来说是必要的。

但有些资源其实完全是在控制平面管理的，比如虚拟设备、云资源配额之类的。为了它们在每个节点上都部署一个"空壳驱动"，既浪费资源又增加维护成本。

**可选节点操作**（Optional Node Operations）就是来解决这个问题的。驱动可以声明"这些设备不需要节点本地操作"，kubelet 看到后就会跳过 gRPC 调用，不用去找驱动了。

### 怎么配置

在 ResourceSlice 里加一个 `skipNodeOperations` 字段，写上要跳过哪些操作：

- `"NodePrepareResources"`：跳过准备设备的 gRPC 调用（必须同时跳过 `NodeUnprepareResources`，否则 Pod 结束时可能卡住）
- `"NodeUnprepareResources"`：跳过取消准备的 gRPC 调用
- `"*"`：全部跳过

下面是一个控制平面资源的例子，所有节点操作都跳过：

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: control-plane-resources
spec:
  nodeName: worker-1
  pool:
    name: central-pool
    generation: 1
    resourceSliceCount: 1
  driver: control-plane.example.com
  skipNodeOperations:
  - "*"
  devices:
  - name: virtual-device-1
```

### 执行流程

调度器分配设备时，会把 `skipNodeOperations` 从 ResourceSlice 复制到 ResourceClaim 的分配结果里：

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
...
status:
  allocation:
    devices:
      results:
      - device: virtual-device-1
        driver: control-plane.example.com
        pool: central-pool
        skipNodeOperations:
        - "*"
```

Pod 跑起来的时候，kubelet 读一下分配结果，如果某个驱动的所有设备都跳过同一项操作，kubelet 就干脆不调用那个 gRPC 钩子了。

### 操作上的注意事项

**原地升级驱动时要小心**

因为 `skipNodeOperations` 是分配时复制过去的，已经在运行的 Pod 会保留当时的设置。如果你把驱动从"需要节点操作"改成"不需要"，老的声明还是按老规则来。

所以在做这种变更的时候（特别是要下线节点驱动 DaemonSet 时），先确认这个驱动没有活跃的声明了再动手，不然 Pod 终止时可能会因为找不到驱动而卡住。

**和节点声明特性的配合**

不是所有版本的 kubelet 都支持跳过 DRA 操作。为了防止 Pod 被调度到不支持的节点上，这个特性和[节点声明特性](https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/node-declared-features/)做了集成——调度器会先确认目标节点声明了 `DRAOptionalNodeOperations` 支持，才会把使用了跳过操作的 Pod 调度过去。

**怎么开启**：由 `kube-apiserver`、`kube-scheduler` 和 `kubelet` 中的 [`DRAOptionalNodeOperations`](https://kubernetes.io/zh-cn/docs/reference/command-line-tools-reference/feature-gates/#DRAOptionalNodeOperations) 特性门控控制。

## 六、设备元数据：容器里怎么知道拿到了什么设备

### 它解决什么问题

想象一下：你的应用跑在容器里，DRA 给你分配了一块 GPU。但应用怎么知道这块 GPU 的具体信息呢？比如 UUID 是什么、PCI 地址是多少、驱动版本是多少？

以前的做法要么是应用去调 Kubernetes API 查询，要么是自己搞个 sidecar 注入信息。前者增加了 API 服务的压力，还有权限管理的问题；后者既麻烦又不统一。

**DRA 设备元数据**（Device Metadata）提供了一个标准方案：驱动把设备信息写成 JSON 文件，挂载到容器里的固定路径。应用直接读文件就行，不用调 API，也不用关心是谁提供的。

KEP-5304 定义了这套协议的标准格式。如果你用官方的 [DRA kubelet 插件库](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin)，这些都帮你实现好了。

> 设备元数据和设备访问的规则一致：只有在容器规约里显式请求了设备的容器，才能看到对应的元数据文件。

### 协议的四条规则

**1. 文件放哪**

元数据文件统一放在容器的 `/var/run/kubernetes.io/dra-device-attributes` 目录下：

- 直接引用 ResourceClaim：`resourceclaims/<claimName>/<requestName>/<driverName>-metadata.json`
- 通过 ResourceClaimTemplate 创建：`resourceclaimtemplates/<podClaimName>/<requestName>/<driverName>-metadata.json`

路径常量定义在 [`k8s.io/dynamic-resource-allocation/api/metadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata) 包里。

**2. 文件里有什么**

每个文件是一个或多个 `DeviceMetadata` 对象的 JSON 流，带有标准的 `apiVersion` 和 `kind` 字段。同一份元数据会按支持的 API 版本各编码一次（新版本在前），应用读第一个能解析的就行。

参考 [`DeviceMetadata` API 文档](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1alpha1#DeviceMetadata)了解字段详情。

**3. 怎么判断更新了**

每次驱动更新元数据文件，都必须把 `metadata.generation` 加 1。应用通过观察这个字段就能知道数据变了。

**4. 怎么进容器**

通常是通过 CDI（Container Device Interface）绑定挂载进去的。只要文件路径正确、容器内只读，用其他方式也行。

### 它是怎么工作的

设备元数据是驱动侧的能力，不需要改动 Kubernetes API，也没有专门的特性门控。

驱动在为 Pod 准备设备的时候生成元数据文件和 CDI 挂载配置，容器启动前文件就已经在约定的位置了。如果一个请求涉及多个驱动，每个驱动写自己的元数据文件，容器枚举目录下的 `*-metadata.json` 就能发现所有设备。

如果你写 Go 应用，官方的 [`k8s.io/dynamic-resource-allocation/devicemetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata) 包提供了读取这些文件的工具函数。

### 来看个实际的 JSON 例子

下面是一个 GPU 设备的元数据文件示例，能看到设备的驱动版本、索引、型号、UUID 等信息：

```json
{
  "kind": "DeviceMetadata",
  "apiVersion": "metadata.resource.k8s.io/v1alpha1",
  "metadata": {
    "name": "pod0-gpu-2kqrd",
    "namespace": "gpu-test1",
    "uid": "c7e7b22e-239b-4498-b27c-7f1344481e14",
    "generation": 1
  },
  "podClaimName": "gpu",
  "requests": [
    {
      "name": "gpu",
      "devices": [
        {
          "driver": "gpu.example.com",
          "pool": "worker-0",
          "name": "gpu-0",
          "attributes": {
            "driverVersion": {
              "version": "1.0.0"
            },
            "index": {
              "int": 0
            },
            "model": {
              "string": "LATEST-GPU-MODEL"
            },
            "uuid": {
              "string": "gpu-18db0e85-99e9-c746-8531-ffeb86328b39"
            }
          }
        }
      ]
    }
  ]
}
```

### 两种提供方式：即时 vs 延迟

驱动有两种时机来填充元数据：

**即时模式**：在节点上准备设备的时候就把元数据写好，容器启动前文件就完整了。GPU 驱动通常是这种模式，设备信息在准备阶段就能拿到。

**延迟模式**：有些设备（比如网络设备）的信息要等 Pod 沙箱创建好之后才知道。这种情况下驱动先创建一个空文件占位，然后通过 NRI 钩子在容器启动前把真正的元数据写进去。每次更新都要递增 `metadata.generation`。这样应用永远不会读到"半截"的文件。

不管哪种模式，元数据在容器运行期间一直可用，Pod 里所有容器都退出后文件会被清理掉。

想了解应用侧怎么使用元数据，可以看[访问 DRA 设备元数据](https://kubernetes.io/zh-cn/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/)。

### 自己写驱动怎么办

如果你不用官方的 kubelet 插件库，而是自己实现 DRA 驱动，那就得自己实现这套元数据协议。要点就三个：

1. 文件路径要放对
2. 每次更新 `metadata.generation` 要加 1
3. 通过 CDI 或类似机制把文件以只读方式挂进容器

## 总结

DRA 的六个进阶特性，从不同维度完善了 Kubernetes 的异构资源管理能力。它们不是孤立的，而是层层递进、互相配合：

| 特性 | 一句话概括 | 关键 API 字段 |
|------|-----------|--------------|
| 可分区设备 | 一块物理设备拆成多个逻辑设备 | `sharedCounters`, `consumesCounters` |
| 设备兼容性组 | 防止不兼容的设备模式被分配到一起 | `compatibilityGroups` |
| 可消耗容量 | 一台设备的容量可以被多个声明共享 | `allowMultipleAllocations`, `capacity` |
| 细粒度状态授权 | 精确控制谁能在哪个节点上改 ResourceClaim 状态 | 合成子资源 + 节点感知动词 |
| 可选节点操作 | 纯控制平面资源不用在每个节点装驱动 | `skipNodeOperations` |
| 设备元数据 | 容器里直接读文件就能知道设备信息 | `DeviceMetadata` JSON |

举几个组合使用的例子：

- **设备兼容性组** 建立在 **可分区设备** 之上，没有分区就谈不上兼容组
- **DistinctAttribute** 约束是随 **可消耗容量** 一起引入的
- **可选节点操作** 和 **节点声明特性** 配合，确保调度到支持的节点

随着 Kubernetes 在 AI、高性能计算等场景的应用越来越广泛，DRA 这些特性会变得越来越重要。了解它们的能力边界，能帮助你更好地规划集群的硬件资源管理方案。
