# vmstorage 磁盘容量规划

vmstorage 是负责存储可观测性多集群指标。
为保证 vmstorage 的稳定性，需要根据集群数量及集群规模调整 vmstorage 的磁盘容量。
更多资料请参考：[vmstorage 保留期与磁盘空间](https://docs.victoriametrics.com/guides/understand-your-setup-size.html?highlight=datapoint#retention-perioddisk-space)。

## 测试结果

经过 14 天对不同规模的集群的 vmstorage 的磁盘观测，
我们发现 vmstorage 的磁盘用量与其存储的指标量和单个数据点占用磁盘正相关。

1. 瞬时存储的指标量 __increase(vm_rows{ type != "indexdb"}[30s])__ 以获取 30s 内增加的指标量
2. 单个数据点 (datapoint) 的占用磁盘： __sum(vm_data_size_bytes{type!="indexdb"}) / sum(vm_rows{type != "indexdb"})__ 

## 计算方法

**磁盘用量** = 瞬时指标量 x 2 x 单个数据点的占用磁盘 x 60 x 24 x 存储时间 (天)

**参数说明：**

1. 磁盘用量单位为 __Byte__ 。
2. __存储时长(天) x 60 x 24__ 将时间(天)换算成分钟以便计算磁盘用量。
3. Insight Agent 中 Prometheus 默认采集时间为 30s ，故在 1 分钟内产生两倍的指标量。
4. vmstorage 中默认存储时长为 1 个月，修改配置请参考[修改系统配置](../../user-guide/system-config/modify-config.md)。

!!! warning

    该公式为通用方案，建议在计算结果上预留冗余磁盘容量以保证 vmstorage 的正常运行。

## 参考容量

表格中数据是根据默认存储时间为一个月 (30 天)，单个数据点 (datapoint) 的占用磁盘取 0.9 计算所得结果。
多集群场景下，Pod 数量表示多集群 Pod 数量的总和。

### 当未开启服务网格时

| 集群规模 (Pod 数) | 指标量 | 磁盘容量 |
| ----------------- | ------ | -------- |
| 100               | 8w     | 6 GiB    |
| 200               | 16w    | 12 GiB   |
| 300               | 24w    | 18 GiB   |
| 400               | 32w    | 24 GiB   |
| 500               | 40w    | 30 GiB   |
| 800               | 64w    | 48 GiB   |
| 1000              | 80w    | 60 GiB   |
| 2000              | 160w   | 120 GiB  |
| 3000              | 240w   | 180 GiB  |

### 当开启服务网格时

| 集群规模 (Pod 数) | 指标量 | 磁盘容量 |
| ----------------- | ------ | -------- |
| 100               | 15w    | 12 GiB   |
| 200               | 31w    | 24 GiB   |
| 300               | 46w    | 36 GiB   |
| 400               | 62w    | 48 GiB   |
| 500               | 78w    | 60 GiB   |
| 800               | 125w   | 94 GiB   |
| 1000              | 156w   | 120 GiB  |
| 2000              | 312w   | 235 GiB  |
| 3000              | 468w   | 350 GiB  |

### 举例说明

DCE 5.0 平台中有两个集群，其中全局管理集群(开启服务网格)中运行 500 个 Pod，工作集群(未开启服务网格)运行了 1000 个 Pod，预期指标存 30 天。

- 全局管理集群中指标量为 800x500 + 768x500 = 784000
- 工作集群指标量为 800x1000 = 800000

则当前 vmstorage 磁盘用量应设置为 (784000+80000)x2x0.9x60x24x31 = 124384896000 byte = 116 GiB

!!! note

    集群中指标量与 Pod 数量的关系可参考[Prometheus 资源规划](./prometheus-res.md)。
