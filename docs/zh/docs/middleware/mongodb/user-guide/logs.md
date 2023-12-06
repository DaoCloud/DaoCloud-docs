---
hide:
  - toc
---

# 查看 MongoDB 日志

## 操作步骤

通过访问每个 MongoDB 的实例详情页面，可以支持查看 MongoDB 的日志。

1. 在 MongoDB 实例列表中，选择想要查看的日志，点击 `实例名称` 进入到实例详情页面。

    ![日志](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/images/mongo-logs01.png)

2. 在实例的左侧菜单栏，会发现有一个日志查看的菜单栏选项。

    ![日志](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/images/mongo-logs02.png)

3. 点击 `日志查看` 即可进入到日志查看页面（[Insight](../../../insight/intro/index.md) 日志查看）。

## 日志查看说明

在日志查看页面可以很方便的进行日志查看。常用操作说明如下：

* 支持自定义日志时间范围，在日志页面右上角，可以方便地切换查看日志的时间范围（可查看的日志范围以 可观测系统设置内保存的日志时长为准）
* 支持关键字检索日志，左侧检索区域支持查看更多的日志信息
* 支持日志量分布查看，中上区域柱状图，可以查看在时间范围内的日志数量分布
* 支持查看日志的上下文，点击右侧 `上下文` 图标即可
* 支持导出日志
