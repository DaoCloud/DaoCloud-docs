# GPU 监控指标

本页列出一些常用的 GPU 监控指标。

## 集群维度

| 指标名称 | 描述 |
| ------- | ------ |
| GPU 卡数 | 集群下所有的 GPU 卡数量 |
| GPU 平均使用率 | 集群下所有 GPU 卡的平均算力使用率 |
| GPU 平均显存使用率 | 集群下所有 GPU 卡的平均显存使用率 |
| GPU 卡功率 | 集群下所有 GPU 卡的功率 |
| GPU 卡温度 | 集群下所有 GPU 卡的温度 |
| GPU 算力使用率细节 | 24 小时内，集群下所有 GPU 卡的使用率细节（包含 max、avg、current） |
| GPU 显存使用量细节 | 24 小时内，集群下所有 GPU 卡的显存使用量细节（包含 min、max、avg、current） |
| GPU 显存带宽使用率 | 表示内存带宽利用率。以 Nvidia GPU V100 为例，其最大内存带宽为 900 GB/sec，如果当前的内存带宽为 450 GB/sec，则内存带宽利用率为 50% |

## 节点维度

| 指标名称 | 描述 |
| ------- | --- |
| GPU 模式 | 节点上 GPU 卡的使用模式，包含整卡模式、MIG 模式、vGPU 模式 |
| GPU 物理卡数 | 节点上所有的 GPU 卡数量 |
| GPU 虚拟卡数 | 节点上已经被创建出来的 vGPU 设备数量 |
| GPU MIG 实例数 | 节点上已经被创建出来的 MIG 实例数 |
| GPU 显存分配率 | 节点上所有 GPU 卡的显存分配率 |
| GPU 算力平均使用率 | 节点上所有 GPU 卡的算力平均使用率 |
| GPU 显存平均使用率 | 节点上所有 GPU 卡的平均显存使用率 |
| GPU 驱动版本 | 节点上 GPU 卡驱动的版本信息 |
| GPU 算力使用率细节 | 24 小时内，节点上每张 GPU 卡的算力使用率细节（包含 max、avg、current） |
| GPU 显存使用量 | 24 小时内，节点上每张 GPU 卡的显存使用量细节（包含 min、max、avg、current） |

**根据 XID 状态排查 GPU 相关问题**

XID 消息是 NVIDIA 驱动程序向操作系统的内核日志或事件日志打印的错误报告。XID 消息用于标识 GPU 错误事件，
提供 GPU 硬件、NVIDIA 软件或应用中的错误类型、错误位置、错误代码等信息。
如检查项 GPU 节点上的 XID 异常为空，表明无 XID 消息；如有，您可按照下表自助排查并解决问题，
或查看[更多 XID 消息](https://docs.nvidia.com/deploy/xid-errors/index.html#topic_4)。

| XID | 消息 | 说明 |
| --- | --- | --- |
| 13 | Graphics Engine Exception. | 通常是数组越界、指令错误，小概率是硬件问题。 |
| 31 | GPU memory page fault. | 通常是应用程序的非法地址访问，极小概率是驱动或者硬件问题。 |
| 32 | Invalid or corrupted push buffer stream. | 事件由 PCIE 总线上管理 NVIDIA 驱动和 GPU 之间通信的 DMA 控制器上报，通常是 PCI 质量问题导致，而非您的程序产生。 |
| 38 | Driver firmware error. | 通常是驱动固件错误而非硬件问题。 |
| 43 | GPU stopped processing. | 通常是您应用自身错误，而非硬件问题。 |
| 45 | Preemptive cleanup, due to previous errors -- Most likely to see when running multiple cuda applications and hitting a DBE. | 通常是您手动退出或者其他故障（硬件、资源限制等）导致的 GPU 应用退出，XID 45 只提供一个结果，具体原因通常需要进一步分析日志。 |
| 48 | Double Bit ECC Error (DBE). | 当 GPU 发生不可纠正的错误时，会上报此事件，该错误也会同时反馈给您的应用程序。通常需要重置 GPU 或重启节点来清除这个错误。 |
| 61 | Internal micro-controller breakpoint/warning. | GPU 内部引擎停止工作，您的业务已经受到影响。 |
| 62 | Internal micro-controller halt. | 与 XID 61 的触发场景类似。 |
| 63 | ECC page retirement or row remapping recording event. | 当应用程序遭遇到 GPU 显存硬件错误时，NVIDIA 自纠错机制会将错误的内存区域 retire 或者 remap，retirement 和 remapped 信息需记录到 infoROM 中才能永久生效。Volt 架构：成功记录 ECC page retirement 事件到 infoROM。Ampere 架构：成功记录 row remapping 事件到 infoROM。 |
| 64 | ECC page retirement or row remapper recording failure. | 与 XID 63 的触发场景类似。但 XID 63 代表 retirement 和 remapped 信息成功记录到了 infoROM，XID 64 代表该记录操作失败。 |
| 68 | NVDEC0 Exception. | 通常是硬件或驱动问题。 |
| 74 | NVLINK Error. | NVLink 硬件错误产生的 XID，表明 GPU 已经出现严重硬件故障，需要下线维修。 |
| 79 | GPU has fallen off the bus. | GPU 硬件检测到掉卡，总线上无法检测该 GPU，表明该 GPU 已经出现严重硬件故障，需要下线维修。 |
| 92 | High single-bit ECC error rate. | 硬件或驱动故障。 |
| 94 | Contained ECC error. | 当应用程序遭遇到 GPU 不可纠正的显存 ECC 错误时，NVIDIA 错误抑制机制会尝试将错误抑制在发生硬件故障的应用程序，避免该错误影响 GPU 节点上运行的其他应用程序。当抑制机制成功抑制错误时，会产生该事件，仅出现不可纠正 ECC 错误的应用程序受到影响。 |
| 95 | Uncontained ECC error. | 与 XID 94 的触发场景类似。但 XID 94 代表抑制成功，而 XID 95 代表抑制失败，表明运行在该 GPU 上的所有应用程序都已受到影响。 |

## Pod 维度

| 分类 | 指标名称 | 描述 |
| --- | ------- | ---- |
| 应用概览 GPU 卡 - 算力 & 显存 | Pod GPU 算力使用率 | 当前 Pod 所使用到的 GPU 卡的算力使用率 |
| | Pod GPU 显存使用率 | 当前 Pod 所使用到的 GPU 卡的显存使用率 |
| | Pod 显存使用量 | 当前 Pod 所使用到的 GPU 卡的显存使用量 |
| | 显存分配量 | 当前 Pod 所使用到的 GPU 卡的显存分配量 |
| | Pod GPU 显存复制使用率 | 当前 Pod 所使用到的 GPU 卡的显存显存复制比率 |
| GPU 卡 - 引擎概览 | GPU 图形引擎活动百分比 | 表示在一个监控周期内，Graphics 或 Compute 引擎处于 Active 的时间占总的时间的比例 |
| | GPU 内存带宽利用率 | 表示内存带宽利用率（Memory BW Utilization）将数据发送到设备内存或从设备内存接收数据的周期分数。该值表示时间间隔内的平均值，而不是瞬时值。较高的值表示设备内存的利用率较高。<br>该值为 1（100%）表示在整个时间间隔内的每个周期执行一条 DRAM 指令（实际上，峰值约为 0.8 (80%) 是可实现的最大值）。<br>假设该值为 0.2（20%），表示 20% 的周期在时间间隔内读取或写入设备内存。 |
| | Tensor 核心引擎使用率 | 表示在一个监控周期内，Tensor Core 管道（Pipe）处于 Active 时间占总时间的比例 |
| | FP16 引擎使用率 | 表示在一个监控周期内，FP16 管道处于 Active 的时间占总的时间的比例 |
| | FP32 引擎使用率 | 表示在一个监控周期内，FP32 管道处于 Active 的时间占总的时间的比例 |
| | FP64 引擎使用率 | 表示在一个监控周期内，FP64 管道处于 Active 的时间占总的时间的比例 |
| | GPU 解码使用率 | GPU 卡解码引擎比率 |
| | GPU 编码使用率 | GPU 卡编码引擎比率 |
| GPU 卡 - 温度 & 功耗 | GPU 卡温度 | 集群下所有 GPU 卡的温度 |
| | GPU 卡功率 | 集群下所有 GPU 卡的功率 |
| | GPU 卡 - 总耗能 | GPU 卡总共消耗的能量 |
| GPU 卡 - Clock | GPU 卡内存频率 | 内存频率 |
| | GPU 卡应用SM 时钟频率 | 应用的 SM 时钟频率 |
| | GPU 卡应用内存频率 | 应用内存频率 |
| | GPU 卡视频引擎频率 | 视频引擎频率 |
| | GPU 卡降频原因 | 降频原因 |
| GPU 卡 - 其他细节 | PCIe 传输速率 | 节点 GPU 卡通过 PCIe 总线传输的数据速率 |
| | PCIe 接收速率 | 节点 GPU 卡通过 PCIe 总线接收的数据速率 |
