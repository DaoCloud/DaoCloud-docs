# run the pipeline on the specified node

This article describes how to run the customer's pipeline tasks on the specified nodes in Workbench.

## Modify the configuration file jenkins-casc-config

1. Go to the __Container Management__ module and enter the details page of the target cluster, such as the __kpanda-global-cluster__ cluster.

     <!--![]()screenshots-->

2. Click __Configuration and Keys__->__Configuration Items__ in the left navigation.

     <!--![]()screenshots-->

3. Search __jenkins-casc-config__, select __Edit YAML__ from the list.

     <!--![]()screenshots-->

4. Add __nodeSelector: "ci=base"__ for a specific Agent under __jenkins.cloud.kubernetes.templates__ in the YAML configuration item __jenkins.yaml__, and click __OK__ to save the changes.

     <!--![]()screenshots-->

## Select the specified node to add a label

1. Enter the __Container Management__ module, on the __kpanda-global-cluster__ cluster details page, click __Node Management__ on the left navigation.

     <!--![]()screenshots-->

2. Select the target worker node (for example, demo-dev-worker-03), and click __Modify Label__.

     <!--![]()screenshots-->

3. Add the __ci=base__ tag and click __OK__ to save the changes.

     <!--![]()screenshots-->

## Visit Jenkins Dashbord, reload configuration

First of all, it is necessary to expose the access address of Jenkins Dashbord through NodePort (other exposure methods are exposed according to the actual business situation).

1. Enter __Container Management__ module, on the __kpanda-global-cluster__ cluster page, click __Container Network__ -> __Service__ in the left navigation bar.

     <!--![]()screenshots-->

2. Search __amamba-jenkins__ and select __Update__ from the list.

     <!--![]()screenshots-->

3. Change the access type to NodePort, and the node port selection will be automatically generated.

     <!--![]()screenshots-->

4. Click OK, then return to the details page and click the link to access the Jenkins Dashboard.

     <!--![]()screenshots-->

5. Enter the account/password (the default is __admin/Admin01__) to enter the Jenkins Dashboard page.

     <!--![]()screenshots-->

6. Select __Manage Jenkins__ in the left navigation bar.

     <!--![]()screenshots-->

7. Click __Configuration as Code__.

     <!--![]()screenshots-->

8. Click __Reload existing configuration__ in __Configuration as Code__. If there is no prompt on the current page after clicking, it means that the configuration loading takes effect.

     <!--![]()screenshots-->

## Run the pipeline and check if it is on the specified node

1. Create a pipeline job in __Workbench__, and edit __Jenkinsfile__ as follows:

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

1. Click __Run Now__ for the pipeline, and go to __Container Management__ to view the running node of the Pod that executes the task.

     <!--![]()screenshots-->

2. You can see that the Pod executing the pipeline task is running on the expected __demo-dev-worker-03__ node.
