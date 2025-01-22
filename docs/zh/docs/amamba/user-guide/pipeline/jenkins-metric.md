# 流水线监控指标

下文介绍于流水线监控暴露的指标信息。

## Jenkins 组件内置指标

Jenkins 自身通过 [promethus-plugin](https://plugins.jenkins.io/prometheus/)
插件来暴露指标，可通过路径`http://JenkinsHost:JenkinsPort/prometheus/` 查看。

### 默认暴露出来的指标

| 监控指标 | 描述 | Prometheus 类型 |
| ------- | --- | --- |
| default_jenkins_disk_usage_bytes | Jenkins_HOME中一级文件夹的磁盘使用量（以字节为单位） | gauge |
| default_jenkins_job_usage_bytes | Jenkins中每个作业的磁盘使用量（以字节为单位） | gauge |
| default_jenkins_file_store_capacity_bytes | Jenkins使用的文件存储的总大小（以字节为单位） | gauge |
| default_jenkins_file_store_available_bytes | Jenkins使用的文件存储中估计的可用空间 | gauge |
| default_jenkins_executors_available | 可用的Jenkins执行器数量 | gauge |
| default_jenkins_executors_busy | 正在忙碌的Jenkins执行器数量 | gauge |
| default_jenkins_executors_connecting | 正在连接的Jenkins执行器数量 | gauge |
| default_jenkins_executors_defined | 已定义的Jenkins执行器数量 | gauge |
| default_jenkins_executors_idle | 空闲的Jenkins执行器数量 | gauge |
| default_jenkins_executors_online | 在线的Jenkins执行器数量 | gauge |
| default_jenkins_executors_queue_length | 可以运行但在等待空闲执行器的项目数量 | gauge |
| default_jenkins_version | Jenkins版本 | info |
| default_jenkins_up | 显示Jenkins是否准备好接收请求 | gauge |
| default_jenkins_uptime | 显示Jenkins自初始化以来的运行时间 | gauge |
| default_jenkins_nodes_online | 显示节点的在线状态 | gauge |
| default_jenkins_builds_duration_milliseconds_summary | 按作业总结的Jenkins构建时间（以毫秒为单位） | summary |
| default_jenkins_builds_success_build_count | 成功构建的数量 | counter |
| default_jenkins_builds_failed_build_count | 失败构建的数量 | counter |
| default_jenkins_builds_health_score | 作业的健康评分 | gauge |
| default_jenkins_builds_available_builds_count | 指示特定作业可用构建数量的仪表 | gauge |
| default_jenkins_builds_discard_active | 表示构建丢弃功能是否对该作业激活的仪表 | gauge |
| default_jenkins_builds_running_build_duration_milliseconds | 表示当前构建运行时长的仪表 | gauge |
| default_jenkins_builds_last_build_result_ordinal | 作业的构建状态（最后构建）（0=成功，1=不稳定，2=失败，3=未构建，4=已中止） | gauge |
| default_jenkins_builds_last_build_result | 作业的构建状态的布尔值（1或0）。<br/>其中1表示构建状态为成功或不稳定，0表示构建状态为失败、未构建或已中止 | gauge |
| default_jenkins_builds_last_build_duration_milliseconds | 最后构建的时间（以毫秒为单位） | gauge |
| default_jenkins_builds_last_build_start_time_milliseconds | 最后构建的开始时间戳（以毫秒为单位） | gauge |
| default_jenkins_builds_last_build_tests_total | 最后构建中测试的总数 | gauge |
| default_jenkins_builds_last_build_tests_failing | 最后构建中失败测试的数量 | gauge |
| default_jenkins_builds_last_stage_duration_milliseconds_summary | 按作业和阶段总结的最后构建中的Jenkins构建时间 | summary |

### 额外启用的指标

#### 暴露方式

1. 前往 Jenkins 配置界面，操作路径：**系统管理** -> **系统配置** -> **Prometheus** ，勾选
2. 开启后重启 Jenkins 实例

    ![jenkins-metric](../../images/jenkins-metric.png)

#### 指标

| 监控指标 | 描述 |
| ------ | ---- |
| default_jenkins_builds_build_result_ordinal | 作业的构建状态（最后构建）（0=成功，1=不稳定，2=失败，3=未构建，4=已中止） |
| default_jenkins_builds_build_result | 作业的构建状态的布尔值（1或0）。<br/>其中1表示构建状态为成功或不稳定，0表示构建状态为失败、未构建或已中止 |
| default_jenkins_builds_build_duration_milliseconds | 最近构建的时间（以毫秒为单位） |
| default_jenkins_builds_build_start_time_milliseconds | 最近构建的开始时间戳（以毫秒为单位） |
| default_jenkins_builds_build_tests_total | 最近构建中的总测试数量 |
| default_jenkins_builds_build_tests_skipped | 最近构建中跳过的测试数量 |
| default_jenkins_builds_build_tests_failing | 最近构建中失败的测试数量 |
| default_jenkins_builds_stage_duration_milliseconds_summary | 按作业和阶段总结的最后构建中的Jenkins构建时间 |

## 平台指标

由应用工作台暴露：

| 指标 | 描述 | Prometheus 类型 | 属性 | 用法举例 |
| --- | ---- | -------------- | --- | ------- |
| amamba_pipeline_run_duration | 流水线运行持续时间（毫秒） | Gauge | workspace_id (工作空间) pipeline_id (流水线名称) run_id (运行id) | 展示单条流水线运行时长计算每条流水线的平均时长统计流水线执行时长趋势流水线耗时Top |
| amamba_pipeline_run_total | 流水线运行次数 | Gauge | workspace_id (工作空间) pipeline_id (流水线名称) run_id (运行id) status (流水线状态) | 每条流水线执行的次数每条流水线的成功/失败率 流水线执行次数趋势Top |
| amamba_pipeline_status | 流水线最近运行状态 | Gauge | workspace_id (工作空间) pipeline_id (流水线名称) status (流水线状态) | 流水线的成功/失败率流水线的运行状态统计 |
