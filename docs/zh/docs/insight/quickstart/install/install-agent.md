---
date: 2022-11-17
hide:
  - toc
---

# 在线安装 insight-agent

`insight-agent` 是集群观测数据采集的插件，支持对指标、链路、日志数据的统一观测。本文描述了如何在在线环境中为接入集群安装 insight-agent。

## 前提条件

- 集群已成功接入 `容器管理 模块。如何接入集群，请参考：

## 操作步骤

1. 进入`容器管理`模块，在`容器列表`中点击要安装 insight-agent 的集群名称。

     ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent01.png)

2. 选择左侧导航栏 `Helm 应用 -> Helm 模板`，在搜索框查询 `insight-agent` ，点击该卡片进入详情。

     ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent02.png)

3. 查看 insight-agent 的 Readme，点击`安装` 进入下一步。

     ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent03.png)

4. 选择安装的版本并在下方表单分别填写全局管理集群中对应数据存储组件的地址，确认填写的信息无误后，点击`确定`。

      - insight-agent 默认部署在集群的 insight-system 命名空间下。
      - 建议安装最新版本的 insight-agent。
      - 系统默认已填写数据上报的组件的地址，仍请您检查无误后再点击`确定` 进行安装。 如需修改数据上报地址，请参考：[获取数据上报地址](../install/gethosturl.md)。

     ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent04.png)

5. 系统将自动返回 `Helm 应用` 列表，当应用 insight-agent 的状态从 `未就绪` 变为 `已部署` ，且所有的组件状态为 `运行中` 时，则安装成功。等待一段时间后，可在`可观测性` 模块查看该集群的数据。

     ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight-agent05.png)