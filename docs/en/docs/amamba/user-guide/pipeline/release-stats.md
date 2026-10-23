# Release Stats

> This feature is supported since v0.36.

## Feature Introduction

The Release Stats (ReleaseStats) feature is used to show the execution status of pipelines of the
**release** type, helping users understand the release history and status of versions more intuitively.

## Enable Release Stats

By default, the release stats feature is disabled. You can enable it by modifying the configuration file.

### 1. Modify the configuration file

1. In **Container Management**, select the [global service cluster](../../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster), and search for `amamba-config` in **ConfigMaps**.

    ![git1](../../images/git1.jpg)

2. Click **Edit YAML**, and add `ReleaseStats=true` to the `featureGates` of apiServerConfig and devopsConfig.

    ```yaml
    amamba-config.yaml: |
      apiServerConfig:
        featureGates:
        - ReleaseStats=true
      devopsConfig:
        featureGates:
        - ReleaseStats=true
    ```

    ![feature-gates-release](../../images/feature-gates-release.jpeg)

3. After the modification is successful, search for `amamba-apiserver` and `amamba-devops-server` in Deployments, and click **Restart**.

    ![git3](../../images/git3.jpg)

### 2. Confirm the feature is enabled

After the restart is successful, enter the **Workbench**, and you will see the release feature on the relevant pages.

## Use Release Stats

1. Create a pipeline

    Select `release` as the pipeline type.

    ![Create pipeline](../../images/release-stats1.jpeg)


2. Edit and run the pipeline

    Since we identify business-related information through **environment variables** and **run parameters**,
    the pipeline needs to contain the following keywords (case-insensitive; if both are contained, the
    information in the run parameters prevails):

    - `application`: the application name
    - `image`: the image name and version
    - `cluster`: the cluster name
    - `namespace`: the namespace name

    Update the Jenkinsfile as follows:

    ```groovy
    pipeline {
      agent {
        node {
          label 'base'
        }
      }
      parameters {
        choice(name: 'cluster', choices: ['sh-02', 'eu-01'], description: '')
        choice(name: 'namespace', choices: ['biz1', 'biz2'],, description: '')
      }
      
      stages {
        stage('Stage-RnIJL') {
          steps {
            container('base') {
              echo "123"
            }

          }
        }
      }
      environment {
        application = 'test-2'
        image = 'docker.io/library/nginx:latest'
      }
    }
    ```

    Run the pipeline.

3. View the release stats

    In the left navigation bar, select **Release Stats**. On the list page, the system will show all
    version releases related to the current pipeline.

    ![View release stats](../../images/release-stats2.jpeg)
