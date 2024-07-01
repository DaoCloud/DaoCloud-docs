# 查看流水线详情

创建好流水线之后，可以根据需要查看流水线详情或更新配置，流水线详情页面包含流水线的运行记录、代码质量扫描。

在 __应用工作台__ -> __流水线__ 页面，选择某一条流水线，点击流水线的名称。

![流水线页面](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-pipeline1.png)

进入到流水线详情页面，可以查看到当前流水线的基本信息。

- 执行次数：流水线运行的总次数
- 成功次数：流水线运行成功的次数
- 最近运行状态：流水线最新一条运行记录的状态
- 创建方式：流水线的创建方式，有自定义创建、多分支创建、模板创建、基于代码仓库Jenkinfile 创建四种创建方式
- 描述：流水线的具体描述
- 创建时间：流水线的创建时间

![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-pipeline2.png)

查看流水运行记录列表，展示当前流水线运行的记录的列表，支持通过 ID 搜索，还支持取消、重新运行操作。

![记录列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-pipeline3.png)

查看流水线代码质量扫描结果。查看结果需要确保完成以下要求：

- 请确保当前工作空间已经集成或绑定了 SonarQube 实例
- 当前流水线定义了 SonarQube 配置步骤
- 成功执行流水线

完成上述要求后，您可以在详情界面查看到扫描结果，点击查看更多可以跳转到 SonarQube 后台查看更详细的结果，如下图：

![详情界面](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/detail-pipeline4.png)
