---
hide:
  - toc
---

# 集群设置

集群设置用于为您的集群自定义高级特性设置，包括是否启用 GPU、Helm 仓库刷新周期、Helm 操作记录保留等。

- 启用 GPU：需要预先在集群上安装 GPU 卡及对应驱动插件。

    点击目标集群的名称，在左侧导航栏点击 __最近操作__ -> __集群设置__ -> __Addon 插件__ 。

    ![配置gpu](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/settings01.png)

- Helm 操作基础镜像、仓库刷新周期、操作记录保留条数、是否开启集群删除保护（开启后集群将不能直接卸载）

    ![高级配置](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/Advanced-Configuration.png)
