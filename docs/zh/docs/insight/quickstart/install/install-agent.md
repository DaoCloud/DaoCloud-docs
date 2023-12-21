---
date: 2022-11-17
hide:
  - toc
---

# 在线安装 insight-agent

`insight-agent` 是集群观测数据采集的插件，支持对指标、链路、日志数据的统一观测。本文描述了如何在在线环境中为接入集群安装 insight-agent。

## 前提条件

- 集群已成功接入 `容器管理` 模块。如何接入集群，请参考：[接入集群](../../../kpanda/user-guide/clusters/integrate-cluster.md)

## 操作步骤

1. 进入`容器管理`模块，在`集群列表`中找到要安装 insight-agent 的集群名称。

    ![确定集群](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent01.png)

2. 选择`立即安装`跳转，或点击集群，在左侧导航栏内点击 `Helm 应用` -> `Helm 模板`，搜索框查询 `insight-agent` ，点击该卡片进入详情。

    ![查询 insight-agent](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent02.png)

3. 查看 insight-agent 的安装页面，点击`安装` 进入下一步。

    ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent03.png)

4. 选择安装的版本并在下方表单分别填写全局管理集群中对应数据存储组件的地址，确认填写的信息无误后，点击`确定`。

    - insight-agent 默认部署在集群的 insight-system 命名空间下。
    - 建议安装最新版本的 insight-agent。
      - 系统默认已填写数据上报的组件的地址，仍请您检查无误后再点击`确定` 进行安装。 如需修改数据上报地址，请参考：[获取数据上报地址](../install/gethosturl.md)。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent04.png)

5. 系统将自动返回 `Helm 应用` 列表，当应用 insight-agent 的状态从 `未就绪` 变为 `已部署` ，且所有的组件状态为 `运行中` 时，则安装成功。等待一段时间后，可在`可观测性` 模块查看该集群的数据。

    ![结束界面](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent05.png)

!!! note

    - 点击最右侧的 `⋮`，您可以在弹出菜单中执行更多操作，如 `更新`、`查看 YAML` 和 `删除`。
    - 对于实际的安装演示，观看 [insight-agent 安装视频演示](../../../videos/insight.md#install-insight-agent)。
