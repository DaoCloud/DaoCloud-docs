# Installing Jenkins

## Prerequisites

- Before installing Jenkins, make sure there is a default storage class in the cluster where Jenkins will be installed.
- Please ensure that it is installed in the `amamba-system` namespace.
- If installing on a global service cluster, make sure to have an instance of `amamba-jenkins` in the `Container Management` -> `Helm Applications`, under the `amamba-system` namespace.

## Getting Started with Installation

1. Go to the `Container Management` module and find the cluster where you want to install Jenkins in the `Cluster List`. Click the name of that cluster.

    !!! note

        Select the deployment cluster for Jenkins based on your actual situation. Currently, it is not recommended to deploy it on the global service cluster as executing pipelines in Jenkins with high concurrency can consume a significant amount of resources and may cause the global service cluster to become unresponsive.

    ![Click Cluster Name](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/install-jenkins11.png)

2. In the left navigation bar, select `Helm Applications` -> `Helm Templates`, and find and click `Jenkins`.

    ![jenkins helm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/install-jenkins12.png)

3. In the `Version Selection`, choose the desired version of Jenkins to install, and click `Install`.

    ![Install](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/install-jenkins13.png)

4. On the installation page, fill in the required installation parameters, and finally click the `OK` button at the bottom right.

    ![Fill in Configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/install-jenkins14.png)

    Here are some important parameter explanations. Change and write the parameters according to your actual business needs.

    | Parameter  | Description     |
    | ---------- | --------------- |
    | ContainerRuntime  | Select a runtime like podman or docker   |
    | AdminUser  | Username for Jenkins   |
    | AdminPassword     | Password for Jenkins   |
    | Deploy.JenkinsHost      | Access link to Jenkins. If using Node Port, the access address will be: http://{cluster address:port} |
    | JavaOpts   | Specify JVM startup parameters for running Jenkins      |
    | ServiceType | Default is ClusterIP, supports ClusterIP, NodePort, LoadBalancer |
    | ServicePort | Service access port    |
    | NodePort   | Required if ServiceType=NodePort, range: 30000-32767    |
    | resources.requests      | Resource requests for Jenkins |
    | resources.limits  | Resource limits for Jenkins   |
    | image.registry    | Jenkins image   |
    | eventProxy.enabled      | true means deployment on a non-global service cluster<br />false means deployment on a global service cluster |
    | eventProxy.image.registry      | Required if enabled=true      |
    | eventProxy.image.repository    | Required if enabled=true      |
    | eventProxy.image.tag    | Required if enabled=true      |
    | eventProxy.imagePullPolicy     | Required if enabled=true      |
    | eventProxy.configMap.eventroxy.host  | Required if enabled=true      |
    | eventProxy.configMap.eventroxy.proto | Required if enabled=true      |
    | eventProxy.configMap.eventroxy.token | Required if enabled=true<br />Refer to the [Global Access Key Document](../../../ghippo/user-guide/personal-center/accesstoken.md) for token acquisition |

5. Go to Helm Applications to check the deployment result.

    ![Deployment Completed](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/install-jenkins15.png)

## Integrating Jenkins

Note: Currently, only integration with Jenkins installed via the DCE 5.0 platform is supported.

1. Log in to DCE 5.0 with a user who has the role of an Workbench Administrator and go to the Workbench.

    ![Deployment Completed](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/install-jenkins16.png)

2. On the left navigation bar under Platform Management, click `Toolchain Integration` and then click the `Integrate` button in the upper right corner.

    ![Deployment Completed](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/install-jenkins17.png)

3. Select the toolchain type as `Jenkins`, fill in the integration name, Jenkins address, username, and password.
   If the Jenkins address is using the HTTPS protocol, provide the certificate. By default, the account/password for Jenkins deployed through Helm is `admin/Admin01`.

    ![Deployment Completed](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/amamba/images/install-jenkins18.png)

4. After the integration is complete, a record will be successfully generated on the `Toolchain List` page.


5. Now you can proceed to create pipelines in the workspace. [Create a pipeline](create/custom.md).

## Integration Considerations

If the integrated Jenkins instance is deployed on a cluster other than `kpanda-global-cluster`, it will cause the Application Workbench to be unable to update the configuration file of the Jenkins instance (in subsequent versions, integration with the Jenkins instance will require specifying the cluster and namespace it belongs to), leading to the following two issues:

- In the pipeline `notification` step, when configuring the mail server address in Global Management -> Platform Settings -> Email Server Settings, the configuration cannot be updated in Jenkins.
- In the pipeline `SonarQube Configuration` step, after integrating the SonarQube instance into the toolchain and binding it to the current workspace, using that instance will not work.

To address these issues, you need to go to the Jenkins backend for relevant configurations.

### Configuring Email Notifications in the Jenkins Backend for the Notification Step

1. Go to the Jenkins backend, click on Manage Jenkins -> Configure System, and then scroll down to the `Email Notification` section.

2. Fill in the relevant parameters. The parameter descriptions are as follows:

   - SMTP Server: The address of the SMTP server that provides email services.
   - Use SMTP Authentication: Choose according to your requirements. It is recommended to enable SMTP authentication.
   - Username: The name of the SMTP user.
   - Password: The password of the SMTP user.
   - SMTP Port: The port used to send emails. If left blank, the default protocol port will be used.

    !!! note

        To configure the sender's email address, click on the top-right user icon -> Settings, and then scroll down to `Email Address`.

### Configuring SonarQube Server Address in the Jenkins Backend for the SonarQube Configuration Step

1. Go to the Jenkins backend, click on Manage Jenkins -> Configure System, and then scroll down to `SonarQube servers`. Click on `Add SonarQube`.

2. Fill in the relevant parameters. The parameter descriptions are as follows:

   - Name: Assign a name to the SonarQube server configuration. This name will be required in the SonarQube Configuration step of the Application Workbench pipeline.
   - Server URL: The URL of the SonarQube server.
   - Server authentication token: The authentication token for the SonarQube server. You can generate a token in the SonarQube console.
