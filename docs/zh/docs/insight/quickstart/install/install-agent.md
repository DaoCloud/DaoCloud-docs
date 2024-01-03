---
date: 2022-11-17
hide:
  - toc
---

# 在线安装 insight-agent

 __insight-agent__ 是集群观测数据采集的插件，支持对指标、链路、日志数据的统一观测。本文描述了如何在在线环境中为接入集群安装 insight-agent。

## 前提条件

- 集群已成功接入 __容器管理__ 模块。如何接入集群，请参考：[接入集群](../../../kpanda/user-guide/clusters/integrate-cluster.md)

## 操作步骤

1. 进入 __容器管理__ 模块，在 __集群列表__ 中找到要安装 insight-agent 的集群名称。

    ![确定集群](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent01.png)

2. 选择 __立即安装__ 跳转，或点击集群，在左侧导航栏内点击 __Helm 应用__ -> __Helm 模板__ ，搜索框查询 __insight-agent__ ，点击该卡片进入详情。

    ![查询 insight-agent](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent02.png)

3. 查看 insight-agent 的安装页面，点击 __安装__ 进入下一步。

    ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent03.png)

4. 选择安装的版本并在下方表单分别填写全局管理集群中对应数据存储组件的地址，确认填写的信息无误后，点击 __确定__ 。

    - insight-agent 默认部署在集群的 insight-system 命名空间下。
    - 建议安装最新版本的 insight-agent。
      - 系统默认已填写数据上报的组件的地址，仍请您检查无误后再点击 __确定__  进行安装。 如需修改数据上报地址，请参考：[获取数据上报地址](../install/gethosturl.md)。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent04.png)

5. 系统将自动返回  __Helm 应用__ 列表，当应用 insight-agent 的状态从  __未就绪__ 变为 __已部署__ ，且所有的组件状态为 __运行中__ 时，则安装成功。等待一段时间后，可在 __可观测性__ 模块查看该集群的数据。

    ![结束界面](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent05.png)

!!! note

    - 点击最右侧的 __⋮__ ，您可以在弹出菜单中执行更多操作，如 __更新__ 、 __查看 YAML__ 和 __删除__ 。
    - 对于实际的安装演示，观看 [insight-agent 安装视频演示](../../../videos/insight.md#install-insight-agent)。
