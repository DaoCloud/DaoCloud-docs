---
hide:
  - toc
---

# 创建自定义流水线

应用工作台流水线支持自定义创建，通过该方式创建的流水线，您可对流水线进行可视化编排。

## 前提条件

- [创建工作空间](../../../../ghippo/user-guide/workspace/workspace.md)、[创建用户](../../../../ghippo/user-guide/access-control/user.md)。
- 将该用户添加至该工作空间，并赋予 __workspace editor__ 或更高权限。

## 操作步骤

具体操作步骤如下：

1. 在流水线列表页点击 __创建流水线__ 。

    ![创建流水线](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/createpipelinbutton.png)

2. 在弹出的对话框中，选择 __自定义创建流水线__ ，点击 __确定__ 。

    ![自定义创建流水线](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/custom01.png)

3. 参考下列说明填写 __基本信息__ 、 __构建设置__ 、 __构建参数__ 。

    - 名称：流水线的名称。同一个工作空间下流水线名称必须唯一。
    - 删除过期流水线记录：删除之前的构建记录，以节省 Jenkins 使用的磁盘空间。

        - 构建记录保留期限：最多保留几天的构建记录，默认值为 7 天，即七天前的构建记录将被删除。
        - 构建记录最大数量：最多保留几条构建记录，默认值为 10， 即最多保留 10 条记录。超过 10 条记录时，时间最早的记录最先被删除。
        - __保留期限__ 和 __最大数量__ 这两条规则同时生效，只要满足其中之一就会开始删除记录。

    - 不允许并发构建：开启后，一次只能执行一个流水线构建任务。
    - 构建参数：在开始运行流水线时传入一个或多个构建参数。默认提供五种参数类型： __布尔值__ 、 __字符串__ 、 __多行文本__ 、 __选项__ 、 __密码__ 、 __上传文件__ 。
    - 添加构建参数后，运行流水线时需要为每个构建参数输入对应的取值。

    ![构建设置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/custom02.png)

4. 参考下列说明填写触发器参数。

    - 代码源触发：开启后，系统会根据 __定时仓库扫描计划__ 定期扫描仓库代码中用于构建流水线的特定分支，如果有更新内容，则重新运行流水线。
    - 定时扫描仓库：输入 CRON 表达式定义扫描仓库的时间周期。__输入表达式后下方会提示当前表达式的含义__ 。有关详细的表达式语法规则，可参考 [Cron 时间表语法](https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax)。
    - 定时触发：定时触发构建流水线，无论代码仓库是否有更新，都会在规定时间重新运行流水线。

    ![配置触发器](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/custom03.png)

5. 完成创建。确认所有参数输入完成后，点击 __确定__ 按钮，完成自定义流水线创建，自动返回流水线列表。点击列表右侧的 __┇__ 可以执行各项操作。

    ![完成创建](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/pipeline05.png)

!!! warning

    - 自定义流水线创建之后，需要手动定义流水线的各个阶段（即编辑流水线），然后才能运行流水线。如果定义流程就直接运行流水线，会出现 __构建失败__ 的错误。
    - 如果[基于模板创建流水线](template.md)或[基于 Jenkinsfile 创建流水线](jenkins.md)，则可以直接运行，无需手动编辑流水线。

下一步：[编辑流水线](../edit.md){ .md-button .md-button--primary }
