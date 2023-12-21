# 故障转移功能介绍

当某个集群发生故障时，该集群内的 Pod 副本会被自动迁移到其他可用集群，以保证服务稳定性。

**前提条件**

多云工作负载的调度策略只能选择聚合模式或者动态权重模式，此时故障转移功能才能生效。

## 开启故障转移

1. 进入多云编排模块，点击 __系统设置__ -> __高级配置__ ，故障转移可实现多个集群之间的副本调度，默认关闭，如有需要请开启。

    ![开启故障转移](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/failover01.png)

2. 以下参数均针对集群，点击开启故障转移并保存。

    | 参数                               | 定义                           | 描述                                                                                    | 字段名 EN                                            | 字段名 ZH                | 默认值 |
    | ---------------------------------- | ------------------------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------ | ------ |
    | ClusterMonitorPeriod               | 检查周期间隔                   | 检查集群状态的时间间隔                                                                  | Check Internal                                       | 检查时间间隔             | 60s    |
    | ClusterMonitorGracePeriod          | 运行中标记集群不健康检查时长   | 集群运行中，超过此配置时间未获取集群健康状态信息，将集群标记为不健康                    | The runtime marks the duration of an unhealthy check | 运行时标记不健康检查时长 | 40s    |
    | ClusterStartupGracePeriod          | 启动时标记集群不健康的检查时长 | 集群启动时，超过此配置时间未获取集群健康状态信息，将集群标记为不健康                    | Mark health check duration at startup                | 启动时标记健康检查时长   | 600s   |
    | FailoverEvictionTimeout            | 驱逐容忍时长                   | 集群被标记为不健康后，超过此时长会给集群打上污点，并进入驱逐状态 （集群会增加驱逐污点） | Eviction tolerance time                              | 驱逐容忍时长             | 30s    |
    | ClusterTaintEvictionRetryFrequency | 优雅驱逐超时时长               | 进入优雅驱逐队列后，最长等待时长，超时后会立即删除                                      | Graceful ejection timeout duration                   | 优雅驱逐超时时长         | 5s     |

## 验证故障转移

1. 创建一个多云无状态负载，选择部署在多个集群上，调度策略选择聚合/动态权重模式.

    ![创建一个多云无状态负载](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/failover02.png)

2. 若此时一个集群不健康并且在指定的时间范围内并未恢复，则将会为此集群打上污点，进入驱逐状态（此文档将手动为某一集群打上污点）

    ![为集群打污点](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/failover03.png)

3. 此时无状态负载的 Pod 将会根据剩余集群的资源等情况进行迁移。最终不健康（被打上污点）的集群内将不存在任何 Pod。

    ![pod迁移](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/failover04.png)
