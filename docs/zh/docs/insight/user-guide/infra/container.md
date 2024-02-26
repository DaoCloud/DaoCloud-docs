---
hide:
  - toc
---

# 容器监控

容器监控是对集群管理中工作负载的监控，在列表中可查看工作负载的基本信息和状态。在工作负载详情页，可查看正在告警的数量以及 CPU、内存等资源消耗的变化趋势。

## 前提条件

集群已安装 Insight Agent，且所有的容器组处于 __运行中__ 状态。

- 安装 Insight Agent 请参考：[在线安装 insight-agent](../../quickstart/install/install-agent.md) 或[离线升级 insight-agent](../../quickstart/install/offline-install.md)。

## 操作步骤

请按照以下步骤查看服务监控指标：

1. 进入 __可观测性__ 产品模块。
  
2. 在左边导航栏选择 __基础设施__ -> __容器__ 。

3. 切换顶部 Tab，查看不同类型工作负载的数据。

    ![容器监控](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/workload00.png){ width="1000"}

4. 点击目标工作负载名称查看详情。

    1. 故障：在故障卡片中统计该工作负载当前正在告警的总数。
    2. 资源消耗：在该卡片可查看工作负载的 CPU、内存、网络的使用情况。
    3. 监控指标：可查看工作负载默认 1 小时的 CPU、内存、网络和磁盘的变化趋势。

    ![容器监控](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/workload01.png){ width="1000"}

### 指标说明

| 指标名称 | 说明 |
| -- | -- |
| CPU 使用量 |工作负载下容器组的 CPU 使用量之和。|
| CPU 请求量 | 工作负载下容器组的 CPU 请求量之和。|
| CPU 限制量 | 工作负载下容器组的 CPU 限制量之和。|
| 内存使用量 | 工作负载下容器组的内存使用量之和。|
| 内存请求量 | 工作负载下容器组的内存使用量之和。|
| 内存限制量 | 工作负载下容器组的内存限制量之和。|
| 磁盘读写速率 | 指定时间范围内磁盘每秒连续读取和写入的总和，表示磁盘每秒读取和写入操作数的性能度量。|
| 网络发送接收速率 | 指定时间范围内，按工作负载统计的网络流量的流入、流出速率。|
