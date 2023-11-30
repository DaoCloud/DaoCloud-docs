# 查看流水线运行记录

创建好流水线之后并运行过流水线，可以查看其流水线运行记录详情。

在`应用工作台`->`流水线` -> 进入`流水线详情`页面，选择某一条流水线运行记录，点击执行 ID。

![detail-run1](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-run1.png)

进入到流水线运行记录详情页面，可以查看到当前流水线运行的基本信息。

- 运行 ID：当前流水线运行记录的 ID，与流水线的第几次执行一致。

- 更新时间：当前流水线运行的时间

- 执行状态：当前流水线运行的状态，主要有以下状态：

  | 状态     | 描述                                           |
  | -------- | ---------------------------------------------- |
  | 执行成功 | 成功执行当前流水线所有的阶段                   |
  | 执行失败 | 流水线中存在阶段运行失败                       |
   | 执行中   | 流水线正在执行中                               |
  | 队列中   | 流水线任务已经下发，等待分配容器执行流水线任务 |
  | 终止     | 人为终止运行当前流水线                         |

![detail-run2](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-run2.png)

查看当前流水线记录的运行报告。点击流水线下的某个步骤，可查看相应步骤的执行日志及运行时间，也可查看全部日志。

![detail-run5](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-run5.png)

查看当前流水线记录的制品报告。当流水线中定义了`保存制品` 步骤，并且流水线执行该步骤后，即可缓存流水线定义中的制品，并支持用户进行下载，其中流水线的日志会默认保存为制品，如下图：

![detail-run3](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-run3.png)

查看当前流水线记录的测试报告。当流水线中拉取了远程代码并且定义了`收集测试报告` 步骤，并且流水线执行该步骤后，即可在当前界面查看到当前查看到测试报告的信息，如下图：

![detail-run5](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-run5.png)
