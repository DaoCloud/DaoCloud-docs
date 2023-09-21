# Install Jenkins

## prerequisites

- Before installing Jenkins, you need to ensure that the default storage class exists in the cluster that will be Jenkins.
- Make sure to install under `amamba-system` namespace.
- If installed in the global service cluster, please ensure that the `amamba-jenkins` instance under the `amamba-system` namespace is in `Container Management -> Helm Application`.

## start installation

1. Enter the `Container Management` module, find the cluster where Jenkins needs to be installed in the `Cluster List`, and click the name of the cluster.

    !!! note

        The Jenkins deployment cluster needs to be selected according to the actual situation. It is not recommended to deploy it in the global service cluster at present, because Jenkins will occupy a lot of resources when executing the pipeline with high concurrency, which may lead to the paralysis of the global service cluster.

    <!--![]()screenshots-->

2. In the left navigation bar, select `Helm Apps` -> `Helm Charts`, find and click `Jenkins`.

    <!--![]()screenshots-->

3. In `Version Selection`, select the version you want to install, and click `Install`.

    <!--![]()screenshots-->

4. In the installation interface, fill in the required installation parameters, and finally click the `OK` button in the lower right corner.

    <!--![]()screenshots-->

    The following are important parameter descriptions, which are written according to actual business needs.

    | Parameters | Description |
    | ------------------------------------ | ------------ --------------------------------------------------- |
    | AdminUser | username for Jenkins |
    | AdminPassword | Password for Jenkins |
    | Deploy.JenkinsHost | Access link for Jenkins. If you choose the Node Port method, the access address rule is: http://{cluster address: port} |
    | JavaOpts | Specify the JVM startup parameters to start Jenkins |
    | ServiceType | Default is ClusterIP, supports ClusterIP, NodePort, LoadBalancer |
    | ServicePort | Service access port |
    | NodePort | Required if ServiceType=NodePort, range: 30000-32767 |
    | resources.requests | Jenkins resource request values ​​|
    | resources.limits | Resource limits for Jenkins |
    | image.registry | jenkins image |
    | eventProxy.enabled | true means deployed in a non-global service cluster<br />false means deployed in a global service cluster |
    | eventProxy.image.registry | Required if enabled=true |
    | eventProxy.image.repository | Required if enabled=true |
    | eventProxy.image.tag | Required if enabled=true |
    | eventProxy.imagePullPolicy | Required if enabled=true |
    | eventProxy.configMap.eventroxy.host | Required if enabled=true |
    | eventProxy.configMap.eventroxy.proto | Required if enabled=true |
    | eventProxy.configMap.eventroxy.token | If enabled=true must be filled in<br />Token acquisition method refers to the global management access key document: https://docs.daocloud.io/ghippo/user-guide/personal-center/Password/ |

5. Go to the Helm app to view the deployment results.

    <!--![]()screenshots-->

## Integrate Jenkins

Note: currently only supports the integration of Jenkins installed through the DCE 5.0 platform.

1. Log in to DCE 5.0 as a user with the `Workbench Admin` role and navigate to Workbench.

    <!--![]()screenshots-->

2. Click `Toolchain Integration` under Platform Management in the left navigation bar, and click the `Integration` button in the upper right corner.

    <!--![]()screenshots-->

3. Select the toolchain type `Jenkins`, fill in the integration name, Jenkins address, username and password. If the Jenkins address is https protocol, a certificate needs to be provided. The default account password of jenkins deployed through helm is `admin/Admin01`.

    <!--![]()screenshots-->

4. After the integration is complete, a record will be successfully generated on the `Toolchain List` page.

    <!--![]()screenshots-->

5. Next, you can go to [Create Pipeline] (create/custom.md) in the workspace.