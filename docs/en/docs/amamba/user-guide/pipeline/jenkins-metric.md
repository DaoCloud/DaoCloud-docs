---
MTPE: windsonsea
Date: 2024-08-21
---

# Pipeline Metrics

This page introduces the metrics exposed by pipeline.

## Built-in Metrics of Jenkins Components

Jenkins itself exposes metrics through the [prometheus-plugin](https://plugins.jenkins.io/prometheus/),
which can be viewed at the path `http://JenkinsHost:JenkinsPort/prometheus/`.

### Default Exposed Metrics

| Monitoring Metric | Description |
|-------------------|-------------|
| default_jenkins_disk_usage_bytes | Disk usage of the first-level folder in JENKINS_HOME in bytes |
| default_jenkins_job_usage_bytes | Amount of disk usage for each job in Jenkins in bytes |
| default_jenkins_file_store_capacity_bytes | Total size in bytes of the file stores used by Jenkins |
| default_jenkins_file_store_available_bytes | Estimated available space on the file stores used by Jenkins |
| default_jenkins_executors_available | Shows how many Jenkins Executors are available |
| default_jenkins_executors_busy | Shows how many Jenkins Executors are busy |
| default_jenkins_executors_connecting | Shows how many Jenkins Executors are connecting |
| default_jenkins_executors_defined | Shows how many Jenkins Executors are defined |
| default_jenkins_executors_idle | Shows how many Jenkins Executors are idle |
| default_jenkins_executors_online | Shows how many Jenkins Executors are online |
| default_jenkins_executors_queue_length | Shows the number of items that can run but are waiting on a free executor |
| default_jenkins_version | Shows the Jenkins version |
| default_jenkins_up | Shows if Jenkins is ready to receive requests |
| default_jenkins_uptime | Shows the time since Jenkins was initialized |
| default_jenkins_nodes_online | Shows the online status of nodes |
| default_jenkins_builds_duration_milliseconds_summary | Summary of Jenkins build times in milliseconds by Job |
| default_jenkins_builds_success_build_count | Successful build count |
| default_jenkins_builds_failed_build_count | Failed build count |
| default_jenkins_builds_health_score | Health score of a job |
| default_jenkins_builds_available_builds_count | Gauge indicating how many builds are available for the given job |
| default_jenkins_builds_discard_active | Gauge indicating if the build discard feature is active for the job. |
| default_jenkins_builds_running_build_duration_milliseconds | Gauge indicating the runtime of the current build. |
| default_jenkins_builds_last_build_result_ordinal | Build status of a job (last build) (0=SUCCESS, 1=UNSTABLE, 2=FAILURE, 3=NOT_BUILT, 4=ABORTED) |
| default_jenkins_builds_last_build_result | Build status of a job as a boolean value (1 or 0). <br/>Where 1 stands for the build status SUCCESS or UNSTABLE and 0 for the build statuses FAILURE, NOT_BUILT or ABORTED |
| default_jenkins_builds_last_build_duration_milliseconds | Build times in milliseconds of the last build |
| default_jenkins_builds_last_build_start_time_milliseconds | Last build start timestamp in milliseconds |
| default_jenkins_builds_last_build_tests_total | Number of total tests during the last build |
| default_jenkins_builds_last_build_tests_failing | Number of failing tests during the last build |
| default_jenkins_builds_last_stage_duration_milliseconds_summary | Summary of Jenkins build times by Job and Stage in the last build |

### Additional Enabled Metrics

#### Exposure Method

1. Go to the Jenkins configuration interface, operation path: `Manage Jenkins -> Configure System -> Prometheus -> Check`
  
2. After enabling, restart the Jenkins instance

    ![jenkins-metric](../../images/jenkins-metric.png)

#### Metrics

| Monitoring Metric | Description |
|-------------------|-------------|
| default_jenkins_builds_build_result_ordinal | Build status of a job (last build) (0=SUCCESS, 1=UNSTABLE, 2=FAILURE, 3=NOT_BUILT, 4=ABORTED) |
| default_jenkins_builds_build_result | Build status of a job as a boolean value (1 or 0). <br/>Where 1 stands for the build status SUCCESS or UNSTABLE and 0 for the build statuses FAILURE, NOT_BUILT or ABORTED |
| default_jenkins_builds_build_duration_milliseconds | Build times in milliseconds of the last build |
| default_jenkins_builds_build_start_time_milliseconds | Last build start timestamp in milliseconds |
| default_jenkins_builds_build_tests_total | Number of total tests during the last build |
| default_jenkins_builds_build_tests_skipped | Number of skipped tests during the last build |
| default_jenkins_builds_build_tests_failing | Number of failing tests during the last build |
| default_jenkins_builds_stage_duration_milliseconds_summary | Summary of Jenkins build times by Job and Stage in the last build |

## Platform Metrics

Exposed by the application workspace

| Metric | Description | Prometheus Type | Attributes | Some Usage |
|--------|-------------|-----------------|------------|------------|
| amamba_pipeline_run_duration | Pipeline run duration (milliseconds) | Gauge | workspace_id (Workspace) pipeline_id (Pipeline Name) run_id (Run ID) | Displays the duration of a single pipeline run, calculates the average duration for each pipeline, tracks the trend of pipeline execution duration, and identifies the top time-consuming pipelines |
| amamba_pipeline_run_total | Total pipeline runs | Gauge | workspace_id (Workspace) pipeline_id (Pipeline Name) run_id (Run ID) status (Pipeline Status) | Number of executions for each pipeline, success/failure rate for each pipeline, and trends of pipeline execution counts |
| amamba_pipeline_status | Recent pipeline run status | Gauge | workspace_id (Workspace) pipeline_id (Pipeline Name) status (Pipeline Status) | Success/failure rates of pipelines and statistics on pipeline run status |
