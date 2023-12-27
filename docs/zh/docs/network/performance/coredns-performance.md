# coreDns 性能测试报告

## 测试背景

- coredns 在标准环境下的延时数据。

## Benchmark

本文基于 DCE 5.0 安装的环境，其中一组环境只安装了 coreDns，另一组安装了 coreDns 与 nodelocaldns，其余参数为默认配置。

### 物理机

| Name        | CPU                                       |  CPU  | MEM  | Interface    |
|:------------|:------------------------------------------|:------|:-----|:-------------|
| Node 1      | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz |  56C  | 128G | 10G Mellanox |
| Node 2      | Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz |  56C  | 128G | 10G Mellanox |

以下是我们使用物理服务器压测的数据

- 有 nodelocaldns

|        case        |      nslookup 耗时    |     总耗时     |
| :-----------------:|:-------------------: | :-----------: |
| Same node Pod      |       0.001250       |    0.001867   |
| Cross-node Pod     |       0.001319       |    0.002238   |
| extelnal website   |       0.002954       |    0.019675   |

- 无 nodelocaldns

|        case        |      nslookup 耗时    |     总耗时     |
| :-----------------:|:-------------------: | :-----------: |
| Same node Pod      |       0.001495       |    0.002200   |
| Cross-node Pod     |       0.001563       |    0.002700   |
| extelnal website   |       0.007863       |    0.027283   |

### 虚拟机

| Name        | CPU                                       |  CPU  | MEM  |
|:------------|:------------------------------------------|:------|:-----|
| Node 1      | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz  |  16C  | 16G  |
| Node 2      | Intel(R) Xeon(R) Gold 5118 CPU @ 2.30GHz  |  16C  | 16G  |

以下是我们使用虚拟服务器压测的数据。

- 有 nodelocaldns

|        case        |      nslookup 耗时    |     总耗时     |
| :-----------------:|:-------------------: | :-----------: |
| Same node Pod      |       0.001765       |    0.003267   |
| Cross-node Pod     |       0.002251       |    0.003593   |
| extelnal website   |       0.003656       |    0.064317   |

- 无 nodelocaldns

|        case        |      nslookup 耗时    |     总耗时     |
| :-----------------:|:-------------------: | :-----------: |
| Same node Pod      |       0.002059       |    0.003544   |
| Cross-node Pod     |       0.002246       |    0.003788   |
| extelnal website   |       0.010509       |    0.072507   |
