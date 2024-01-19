# 创建网格实例时，集群列表存在未知的集群

造成这种问题的情况有几种：

## 情况 1

未知集群卸载不久，集群信息同步任务还未触发。可能是未知集群的网格实例还处于卸载中的状态，等待网格实例卸载完成，自动触发集群信息同步即可。

## 情况 2

集群卸载有残留。确定未知集群已不存在，手动删除残留集群信息，登录global集群，执行以下命令

![内存占用查看](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/troubleshoot/images/mc-delete-01.png)
