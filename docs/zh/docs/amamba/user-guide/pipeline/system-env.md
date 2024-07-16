# 系统内置环境变量

在流水线执行过程中，可能会需要一些系统内置的环境变量，以便在流水线运行的时候使用，下表中列举了目前系统默认的环境变量，使用环境变量[参考文档](./pipeline-syntax/#environment)。

| 变量名称                  | 默认值                                                       | 备注                                           |
| ------------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| BUILD_URL                 | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/ |                                                |
| HOSTNAME                  | {pod_name}                                                   | 容器组名称                                     |
| POD_CONTAINER             | {container_name}                                             | 目前构建使用的容器名称                         |
| EXCLUDE_DOCKER            | 0                                                            | 这个意义是？？                                 |
| WORKSPACE                 | /home/jenkins/agent/workspace/{workspace_id}/{pipeline_name} |                                                |
| JOB_URL                   | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name} |                                                |
| RUN_CHANGES_DISPLAY_URL   | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect?page | 需要展示吗？                                   |
| RUN_ARTIFACTS_DISPLAY_URL | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect?page | 需要展示吗？                                   |
| RUN_TESTS_DISPLAY_URL     | http://amamba-jenkins-jenkins:80/job/2/job/loooooong-log/12/display/redirect?page | 是不是重复？                                   |
| JOB_DISPLAY_URL           | http://amamba-jenkins-jenkins:80/job/2/job/loooooong-log/display/redirect |                                                |
| JENKINS_HOME              | /var/jenkins_home                                            |                                                |
| HUDSON_HOME               | /var/jenkins_home                                            | 这个跟 JENKINS_HOME 重复是否删除               |
| RUN_DISPLAY_URL           | http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect | 需要展示吗？                                   |
| _                         | /usr/bin/printenv                                            |                                                |
| PWD                       | /home/jenkins/agent/workspace/{workspace_id}/{pipeline_name} |                                                |
| HUDSON_URL                | http://amamba-jenkins-jenkins:80/                            |                                                |
| JOB_NAME                  | {workspace_id}/{pipeline_name}                               |                                                |
| JOB_BASE_NAME             | {pipeline_name}                                              |                                                |
| GITLAB_OBJECT_KIND        | none                                                         | 这个是啊？                                     |
| JENKINS_URL               | http://amamba-jenkins-jenkins:80/                            |                                                |
| BUILD_ID                  | 12                                                           |                                                |
| BUILD_NUMBER              | 12                                                           | 是不是重复？                                   |
| BUILD_DISPLAY_NAME        | #12                                                          | 是不是没必要显示                               |
| CI                        | TRUE                                                         | 有必要展示吗？                                 |
| WORKSPACE_TMP             | /home/jenkins/agent/workspace/{workspace_id}/{pipeline_name}@tmp |                                                |
| NODE_LABELS               | base base-1rcgq                                              |                                                |
| NODE_NAME                 | base-1rcgq                                                   |                                                |
| SONAR_SCANNER_VERSION     | 4.8.0.2856                                                   |                                                |
| GIT_BRANCH                |                                                              | 当流水线基于代码仓库jenkinsfile 创建时才会存在 |
| GIT_LOCAL_BRANCH          |                                                              | 当流水线基于代码仓库jenkinsfile 创建时才会存在 |
| GIT_CHECKOUT_DIR          |                                                              | 当流水线基于代码仓库jenkinsfile 创建时才会存在 |
| GIT_URL                   |                                                              | 当流水线基于代码仓库jenkinsfile 创建时才会存在 |
| GIT_COMMITTER_NAME        |                                                              | 当流水线基于代码仓库jenkinsfile 创建时才会存在 |
| GIT_AUTHOR_NAME           |                                                              | 当流水线基于代码仓库jenkinsfile 创建时才会存在 |
| GIT_COMMITTER_EMAIL       |                                                              | 当流水线基于代码仓库jenkinsfile 创建时才会存在 |
| GIT_AUTHOR_EMAIL          |                                                              | 当流水线基于代码仓库jenkinsfile 创建时才会存在 |
