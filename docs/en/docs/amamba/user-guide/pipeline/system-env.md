---
MTPE: windsonsea
Date: 2024-07-16
hide:
  - toc
---

# System Built-in Environment Variables

During the execution of a pipeline, you might need some system-built environment variables to use
while the pipeline is running. The table below lists the currently default environment variables
provided by the system. For more details, refer to the [Environment Variable Reference Documentation](./pipeline-syntax.md).

| Variable Name | Default Value | Description |
| ------------- | ------------- | ----------- |
| NODE_NAME | `base-1rcgq` | The name of the pod currently executing the build |
| POD_CONTAINER | `{container_name}` | The name of the container currently used for the build |
| NODE_LABELS | `base base-1rcgq` | List of labels assigned to the build node |
| WORKSPACE | `/home/jenkins/agent/workspace/{workspace_id}/{pipeline_name}` | The absolute path of the directory allocated as a workspace for the build |
| JENKINS_URL | `http://amamba-jenkins-jenkins:80/` | The URL of Jenkins |
| BUILD_URL | `http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/` | The URL of this pipeline build record |
| JOB_URL | `http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}` | The URL of this pipeline |
| RUN_CHANGES_DISPLAY_URL | `http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect?page` | |
| RUN_ARTIFACTS_DISPLAY_URL | `http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect?page` | |
| RUN_TESTS_DISPLAY_URL | `http://amamba-jenkins-jenkins:80/job/2/job/loooooong-log/12/display/redirect?page` | |
| JOB_DISPLAY_URL | `http://amamba-jenkins-jenkins:80/job/2/job/loooooong-log/display/redirect` | |
| RUN_DISPLAY_URL | `http://amamba-jenkins-jenkins:80/job/{workspace_id}/job/{pipeline_name}/{build_id}/display/redirect` | |
| HUDSON_URL | `http://amamba-jenkins-jenkins:80/` | |
| JENKINS_HOME | `/var/jenkins_home` | The absolute path of the directory where Jenkins stores data |
| JOB_NAME | `{workspace_id}/{pipeline_name}` | The name of the pipeline |
| JOB_BASE_NAME | `{pipeline_name}` | The short name of the pipeline, omitting the workspace ID |
| BUILD_ID | `{build_id}` | The current build record ID |
| BUILD_NUMBER | `{build_number}` | The current build record version |
| BUILD_DISPLAY_NAME | `#{build_id}` | The display name of the current build record |
| CI | TRUE | |
| SONAR_SCANNER_VERSION | 4.8.0.2856 | |
| GIT_BRANCH | | Present when the pipeline is created based on a repository Jenkinsfile or multi-branch |
| GIT_URL | | Present when the pipeline is created based on a repository Jenkinsfile or multi-branch |
| GIT_COMMIT | | Present when the pipeline is created based on a repository Jenkinsfile or multi-branch |
| BRANCH_NAME | | Present when the pipeline is created based on a multi-branch |
| GIT_PREVIOUS_COMMIT | | Present when the pipeline is created based on a multi-branch |
| TAG_TIMESTAMP | | Present when the pipeline is created based on a multi-branch |
| TAG_UNIXTIME | | Present when the pipeline is created based on a multi-branch |
| TAG_DATE | | Present when the pipeline is created based on a multi-branch |
| TAG_NAME | | Present when the pipeline is created based on a multi-branch |
