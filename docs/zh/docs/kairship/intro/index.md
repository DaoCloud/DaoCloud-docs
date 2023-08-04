---
hide:
  - toc
---

# 什么是多云编排

国内的云计算已经发展了近 15 年，随着技术的成熟，企业应用不单单是简单的上云，出现了更多更复杂的多云需求。云计算从单云到多云的发展历程简单示意如下。

![单云到多云](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/what.png)

企业从最初简单的只要上云就好，到如今开始选择到底上哪个云，或者上哪些云，从而构建专属于企业自身的多云环境。

经数据统计表明，目前企业选择上云时的多云配比情况如下：

| 上云方案                | 市场占比 |
| ----------------------- | -------- |
| 多个公有云 + 多个私有云 | 43%      |
| 多个公有云 + 一个私有云 | 29%      |
| 一个公有云 + 多个私有云 | 12%      |
| 一个公有云 + 一个私有云 | 9%       |
| 一个公有云/私有云       | 7%       |

从上表可以看出，多云是趋势，也是市场主流。这也是多云编排之所以诞生的原因。

多云编排 Kairship（Kubernetes Airship）是一个以应用为中心、开箱即用的多云应用编排平台。
多云编排实现了多云和混合云的集中管理，提供跨云的应用部署、发布和运维的能力；支持基于集群资源的应用弹性扩缩，实现全局负载均衡；提供了故障恢复的能力，彻底解决多云应用灾备的问题。

![workload](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/workload01.png)

[演示视频：如何将单云应用一键转换为多云应用](../../videos/use-cases.md#_2)

[下载 DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
