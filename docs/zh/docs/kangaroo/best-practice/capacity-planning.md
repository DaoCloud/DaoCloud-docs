#  镜像仓库容量资源规划

整个Harbor架构可以分为三层，分别为 Consumer、Service 和 Data Access Layer。

- Consumer：主要是 Harbor Portal、helm 工具、docker client 工具。
- Service：服务层主要是 Harbor 提供功能的核心服务，如：core、registry、jobserver。
- Data Access：主要是提供数据的持久化存储，比如镜像文件数据、镜像元数据。

![资源架构](../images/resource-architecture.png)

在容量规划上体现在服务层和存储层：

- 服务层：主要是服务运行的资源，比如 CPU、Memory
- 存储层：主要是镜像文件数据存储、元数据 DB 存储、缓存 Redis 存储。

实际场景下推荐使用估算+验证的方式来确定资源规划是否合理。

## 1.举例：如下按照存储 500Gi 的镜像数据来进行设置预估。

### 服务层
不同的资源配置能支撑的服务请求量不同，并且最少设置 2 个服务副本：


|  服务                                               | CPU | Memory |
| -------------------------------------     | -------- | -------- |
| Harbor 服务（所有服务）          | 1 核    | 2 Gi    |

### 存储层


| 类型     | 存储                                                                                            |
| -------- | ----------------------------------------------------------------------------------------------- |
| 镜像文件 | 文件系统：使用率不要超过 85% ,如实际需要 500Gi 文件，则文件系统至少配置 588Gi 的存储。  [Minio 对象存储](https://min.io/product/erasure-code-calculator)： Minio 的实际使用存储率和服务个数、纠删码配置有关。如：文件系统需要配置 588Gi 存储，使用率在 50%，则需要设置 1176Gi 的存储。 |
| DB 存储  | DB 存储： 500Gi 的镜像数据，大概申请 50Gi 的 DB空间即可。       |
| 缓存存储 | Redis缓存：500Gi 的镜像数据，大概申请 5Gi 的 缓存空间即可。 |

## 2.验证：可以通过压测工具进行验证该资源规划是否满足实际应用场景需要

若不确定当前配置是否满足实际应用场景，推荐使用如下压测工具进行验证。压测工具 [Harbor pref](https://github.com/goharbor/perf)


```
git clone https://github.com/goharbor/perf
cd perf
export HARBOR_URL=https://admin:password@harbor.domain(用户名密码和地址)
export HARBOR_VUS=100（虚拟用户数）
export HARBOR_ITERATIONS=200（每个虚拟用户数执行的次数）
export HARBOR_REPORT=true（是否生成报告）
go run mage.go
```
## 3.补充说明

每个公司的镜像情况不一样，并且层之间会复用，还要考虑镜像 GC（不启用则不需要考虑），镜像文件存储针对使用 minio 或者文件系统也不一样，需合理规划资源。

GC （Garbage Collection）是指原生 Harbor 提供的镜像清理能力，当您从 Harbor 中删除图像时，空间不会自动释放。您必须运行垃圾收集，通过从文件系统中删除清单不再引用的 blob 来释放空间。详细介绍：[Garbage Collection](https://goharbor.io/docs/edge/administration/garbage-collection/)

- 不启用 GC ：不断地往镜像仓库存储镜像，这时不光要考虑现有镜像的存储，还需要考虑增量以及增长速度。
- 定期 GC ：定期 GC 会缓解镜像仓库的存储压力，但也要根据实际情况确认是否开启，如需开启请前往原生 Harbor使用。
