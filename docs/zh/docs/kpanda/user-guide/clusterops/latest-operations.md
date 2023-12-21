---
hide:
  - toc
---

# 最近操作

在该页面可以查看最近的集群操作记录和 Helm 操作记录，以及各项操作的 YAML 文件和日志，也可以删除某一条记录。

![操作记录](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/operations01.png)

设置 Helm 操作的保留条数：

系统默认保留最近 100 条 Helm 操作记录。若保留条数太多，可能会造成数据冗余，保留条数太少可能会造成您所需要的关键操作记录的缺失。需要根据实际情况设置合理的保留数量。具体步骤如下：

1. 点击目标集群的名称，在左侧导航栏点击 __最近操作__ -> __Helm 操作__ -> __设置保留条数__ 。

    ![保留条数](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/operations02.png)

2. 设置需要保留多少条 Helm 操作记录，并点击 __确定__ 。

    ![保留条数](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/operations03.png)
