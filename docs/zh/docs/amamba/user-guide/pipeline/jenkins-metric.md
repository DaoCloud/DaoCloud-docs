---
hide:
  - toc
---

# 流水线监控指标

下文介绍于流水线监控暴露的指标信息。

## Jenkins 组件内置指标

Jenkins 自身通过 [promethus-plugin](https://plugins.jenkins.io/prometheus/) 插件来暴露指标，可通过路径`http://JenkinsHost:JenkinsPort/prometheus/` 查看。

### 默认暴露出来的指标

| 监控指标                                                     | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| default_jenkins_disk_usage_bytes                             | Disk usage of first level folder in JENKINS_HOME in bytes    |
| default_jenkins_job_usage_bytes                              | Amount of disk usage for each job in Jenkins in bytes        |
| default_jenkins_file_store_capacity_bytes                    | Total size in bytes of the file stores used by Jenkins       |
| default_jenkins_file_store_available_bytes                   | Estimated available space on the file stores used by Jenkins |
| default_jenkins_executors_available                          | Shows how many Jenkins Executors are available               |
| default_jenkins_executors_busy                               | Shows how many Jenkins Executors busy                        |
| default_jenkins_executors_connecting                         | Shows how many Jenkins Executors are connecting              |
| default_jenkins_executors_defined                            | Shows how many Jenkins Executors are defined                 |
| default_jenkins_executors_idle                               | Shows how many Jenkins Executors are idle                    |
| default_jenkins_executors_online                             | Shows how many Jenkins Executors are online                  |
| default_jenkins_executors_queue_length                       | Shows number of items that can run but waiting on free executor |
| default_jenkins_version                                      | Shows the jenkins Version                                    |
| default_jenkins_up                                           | Shows if jenkins ready to receive requests                   |
| default_jenkins_uptime                                       | Shows time since Jenkins was initialized                     |
| default_jenkins_nodes_online                                 | Shows Nodes online status                                    |
| default_jenkins_builds_duration_milliseconds_summary         | Summary of Jenkins build times in milliseconds by Job        |
| default_jenkins_builds_success_build_count                   | Successful build count                                       |
| default_jenkins_builds_failed_build_count                    | Failed build count                                           |
| default_jenkins_builds_health_score                          | Health score of a job                                        |
| default_jenkins_builds_available_builds_count                | Gauge which indicates how many builds are available for the given job |
| default_jenkins_builds_discard_active                        | Gauge which indicates if the build discard feature is active for the job. |
| default_jenkins_builds_running_build_duration_milliseconds   | Gauge which indicates the runtime of the current build.      |
| default_jenkins_builds_last_build_result_ordinal             | Build status of a job (last build) (0=SUCCESS,1=UNSTABLE,2=FAILURE,3=NOT_BUILT,4=ABORTED) |
| default_jenkins_builds_last_build_result                     | Build status of a job as a boolean value (1 or 0). <br/>Where 1 stands for the build status SUCCESS or UNSTABLE and 0 for the build states FAILURE,NOT_BUILT or ABORTED |
| default_jenkins_builds_last_build_duration_milliseconds      | Build times in milliseconds of last build                    |
| default_jenkins_builds_last_build_start_time_milliseconds    | Last build start timestamp in milliseconds                   |
| default_jenkins_builds_last_build_tests_total                | Number of total tests during the last build                  |
| default_jenkins_builds_last_build_tests_failing              | Number of failing tests during the last build                |
| default_jenkins_builds_last_stage_duration_milliseconds_summary | Summary of Jenkins build times by Job and Stage in the last build |

### 额外启用的指标

#### 暴露方式

1. 前往 jenkins 配置界面，操作路径：`系统管理 -> 系统配置 -> Prometheus -> 勾选 `

2. 开启后重启 Jenkins 实例

  ![jenkins-metric](../../images/jenkins-metric.png)

#### 指标

| 监控指标                                                   | description                                                  |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| default_jenkins_builds_build_result_ordinal                | Build status of a job (last build) (0=SUCCESS,1=UNSTABLE,2=FAILURE,3=NOT_BUILT,4=ABORTED) |
| default_jenkins_builds_build_result                        | Build status of a job as a boolean value (1 or 0). <br/>Where 1 stands for the build status SUCCESS or UNSTABLE and 0 for the build states FAILURE,NOT_BUILT or ABORTED |
| default_jenkins_builds_build_duration_milliseconds         | Build times in milliseconds of last build                    |
| default_jenkins_builds_build_start_time_milliseconds       | Last build start timestamp in milliseconds                   |
| default_jenkins_builds_build_tests_total                   | Number of total tests during the last build                  |
| default_jenkins_builds_build_tests_skipped                 | Number of skipped tests during the last build                |
| default_jenkins_builds_build_tests_failing                 | Number of failing tests during the last build                |
| default_jenkins_builds_stage_duration_milliseconds_summary | Summary of Jenkins build times by Job and Stage in the last build |

## 平台指标

由应用工作台暴露

| 指标                         | description                | Prometheus Type | attributes                                                   | some usage                                                   |
| ---------------------------- | -------------------------- | --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| amamba_pipeline_run_duration | 流水线运行持续时间（毫秒） | Gauge           | workspace_id (工作空间) pipeline_id (流水线名称) run_id (运行id) | 展示单条流水线运行时长计算每条流水线的平均时长统计流水线执行时长趋势流水线耗时Top |
| amamba_pipeline_run_total    | 流水线运行次数             | Gauge           | workspace_id (工作空间) pipeline_id (流水线名称) run_id (运行id) status (流水线状态) | 每条流水线执行的次数每条流水线的成功/失败率 流水线执行次数趋势Top |
| amamba_pipeline_status       | 流水线最近运行状态         | Gauge           | workspace_id (工作空间) pipeline_id (流水线名称) status (流水线状态) | 流水线的成功/失败率流水线的运行状态统计                      |