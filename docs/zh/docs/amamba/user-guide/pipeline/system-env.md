# 系统内置环境变量

在流水线执行过程中，可能会需要一些系统内置的环境变量，以便在流水线运行的时候使用，下表中列举了目前系统默认的环境变量，使用环境变量[参考文档](./pipeline-syntax/#environment)。

| 变量名称                  | 默认值                                                       | 备注                                           |
| ------------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| NODE_NAME                 | base-1rcgq                                                   | 当前执行构建的容器组名称                                             |
| POD_CONTAINER             | {container_name}                                             | 目前构建使用的容器名称                         |
| NODE_LABELS               | base base-1rcgq                                              | 为构建节点分配的标签列表                                               |
| WORKSPACE                 | /home/jenkins/agent/workspace/{workspace_id}/{pipeline_name} | 作为工作空间分配给构建的目录的绝对路径                                               |
| JENKINS_URL               | http://amamba-jenkins-jenkins:80/                            | Jenkins 的 URL                                               |
| BUILD_URL                 | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/ | 该流水线构建记录的 URL                                               |
| JOB_URL                   | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name} | 该流水线的 URL                                               |
| RUN_CHANGES_DISPLAY_URL   | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect?page |                                    |
| RUN_ARTIFACTS_DISPLAY_URL | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect?page |                                    |
| RUN_TESTS_DISPLAY_URL     | http://amamba-jenkins-jenkins:80/job/2/job/loooooong-log/12/display/redirect?page |                                    |
| JOB_DISPLAY_URL           | http://amamba-jenkins-jenkins:80/job/2/job/loooooong-log/display/redirect |                                                |
| RUN_DISPLAY_URL           | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect |                                    |
| HUDSON_URL                | http://amamba-jenkins-jenkins:80/                            |                                                |
| JENKINS_HOME              | /var/jenkins_home                                            |  Jenkins 存储数据的目录的绝对路径                                              |
| JOB_NAME                  | {workspace_id}/{pipeline_name}                               | 流水线名称                                               |
| JOB_BASE_NAME             | {pipeline_name}                                              | 流水线短名称，省略了工作空间的 ID                                                |
| BUILD_ID                  | {build_id}                                                           | 当前构建记录 ID                                               |
| BUILD_NUMBER              | {build_number}                                                           | 当前构建记录 版本                                   |
| BUILD_DISPLAY_NAME        | #{build_id}                                                          | 当前构建记录显示名称                              |
| CI                        | TRUE                                                         |                                |
| SONAR_SCANNER_VERSION     | 4.8.0.2856                                                   |                                                |
| GIT_BRANCH                |                                                              | 当流水线基于代码仓库jenkinsfile 创建或者基于多分支创建时才会存在 |
| GIT_URL                   |                                                              | 当流水线基于代码仓库jenkinsfile 创建或者基于多分支创建时才会存在 |
| GIT_COMMIT        |                                                              | 当流水线基于代码仓库jenkinsfile 创建或者基于多分支创建时才会存在 |
| BRANCH_NAME                |                                                              | 当流水线基于多分支创建时才会存在 |
| GIT_PREVIOUS_COMMIT          |                                                              | 当流水线基于多分支创建时才会存在 |
| TAG_TIMESTAMP        |                                                              | 当流水线基于多分支创建时才会存在 |
| TAG_UNIXTIME       |                                                              | 当流水线基于多分支创建时才会存在 |
| TAG_DATE        |                                                              | 当流水线基于多分支创建时才会存在 |
| TAG_NAME        |                                                              | 当流水线基于多分支创建时才会存在 |
