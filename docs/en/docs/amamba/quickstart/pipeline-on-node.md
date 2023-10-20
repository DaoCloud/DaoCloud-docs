# run the pipeline on the specified node

This article describes how to run the customer's pipeline tasks on the specified nodes in Workbench.

## Modify the configuration file jenkins-casc-config

1. Go to the `Container Management` module and enter the details page of the target cluster, such as the `kpanda-global-cluster` cluster.

     <!--![]()screenshots-->

2. Click `Configuration and Keys`->`Configuration Items` in the left navigation.

     <!--![]()screenshots-->

3. Search `jenkins-casc-config`, select `Edit YAML` from the list.

     <!--![]()screenshots-->

4. Add `nodeSelector: "ci=base"` for a specific Agent under `jenkins.cloud.kubernetes.templates` in the YAML configuration item `jenkins.yaml`, and click `OK` to save the changes.

     <!--![]()screenshots-->

## Select the specified node to add a label

1. Enter the `Container Management` module, on the `kpanda-global-cluster` cluster details page, click `Node Management` on the left navigation.

     <!--![]()screenshots-->

2. Select the target worker node (for example, demo-dev-worker-03), and click `Modify Label`.

     <!--![]()screenshots-->

3. Add the `ci=base` tag and click `OK` to save the changes.

     <!--![]()screenshots-->

## Visit Jenkins Dashbord, reload configuration

First of all, it is necessary to expose the access address of Jenkins Dashbord through NodePort (other exposure methods are exposed according to the actual business situation).

1. Enter `Container Management` module, on the `kpanda-global-cluster` cluster page, click `Container Network` -> `Service` in the left navigation bar.

     <!--![]()screenshots-->

2. Search `amamba-jenkins` and select `Update` from the list.

     <!--![]()screenshots-->

3. Change the access type to NodePort, and the node port selection will be automatically generated.

     <!--![]()screenshots-->

4. Click OK, then return to the details page and click the link to access the Jenkins Dashboard.

     <!--![]()screenshots-->

5. Enter the account/password (the default is `admin/Admin01`) to enter the Jenkins Dashboard page.

     <!--![]()screenshots-->

6. Select `Manage Jenkins` in the left navigation bar.

     <!--![]()screenshots-->

7. Click `Configuration as Code`.

     <!--![]()screenshots-->

8. Click `Reload existing configuration` in `Configuration as Code`. If there is no prompt on the current page after clicking, it means that the configuration loading takes effect.

     <!--![]()screenshots-->

## Run the pipeline and check if it is on the specified node

1. Create a pipeline job in `Workbench`, and edit `Jenkinsfile` as follows:

    ```groovy        
    pipeline {
      agent {
        node {
          label 'base'
        }

      }
      stages {
        stage('Hello') {
          agent none
          steps {
            container('base') {
              echo 'Hello World'
              sh 'sleep 300'
            }

          }
        }

      }
    }
    ```

    !!! note

        It should be noted that the agent part needs to select label as base. Because the specified node is only set for the base in the configuration file, if it needs to be set for other agents. Repeat the above operation.

1. Click `Run Now` for the pipeline, and go to `Container Management` to view the running node of the Pod that executes the task.

     <!--![]()screenshots-->

2. You can see that the Pod executing the pipeline task is running on the expected `demo-dev-worker-03` node.
