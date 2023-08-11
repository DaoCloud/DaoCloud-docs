# Deploy Java applications based on Jar packages

Workbench supports building applications in four ways: [Git warehouse](create-app-git.md), Jar package, container image, and Helm chart. This article describes how to deploy a Java application via a Jar file.

## prerequisites

1. Create a [workspace](../../../ghippo/user-guide/workspace/workspace.md) and a [user](../../../ghippo/user-guide/access-control/user.md), the user needs to join the workspace and have the `Workspace Editor` role.

2. [Create a credential to access the registry](../pipelines/credential.md), such as `registry`.

3. Prepare a mirror repository, such as Harbor repository.

## Steps

1. Click `Wizards` on the left navigation bar, and then select `Build based on Jar package`.

    <!--![]()screenshots-->

2. Fill in the basic information with reference to the following requirements, and then click `Next`.

    - Name: Maximum 63 characters, can only contain lowercase letters, numbers, and a separator ("-"), and must start and end with a lowercase letter or number.
    - Resource Type: Select whether the application to be created is a stateless load or a stateful load.
    - Application Group: Select the group to which the application belongs. Empty means do not group this app.
    - Deployment location: Select which namespace under which cluster to deploy the application. Only clusters that exist in the current workspace can be selected.
    - Number of Instances: Set the number of Pods for the application.

        <!--![]()screenshots-->

3. Refer to the following requirements to configure the pipeline, and then click `Next`.

    - Target image name: Name the target image, including the storage path of the target image, for example `release-ci.daocloud.io/test-lfj/fromjar`.
    - Tag: Tag the target image, such as the version number `v1.0`.
    - Credentials: Select the credential to access the registry, such as `registry-credential`.
    - JAVA_OPTS: Variables used to set JVM-related operating parameters, such as `-server -Xms2048m -Xmx2048m -Xss512k`.
    - Build parameters: Build parameters will be passed to the build command in the form of `--build-arg`, which supports setting the upstream product download address and upstream mirror download address as parameters, and also supports custom arbitrary parameters.

        <!--![]()screenshots-->

4. Fill in the container configuration with reference to the following requirements, and click `Next`.

    - Access type: Support access to the application only within the cluster through clusterIP, or allow access outside the cluster through NodePort, or access through a load balancer.
    - Port configuration: fill in the port number that needs to be exposed according to the actual business scenario.

        > For more detailed instructions on service configuration, please refer to [Create Service](../../../kpanda/user-guide/services-routes/create-services.md).

    - Resource limits: CPU and memory quotas must not exceed the remaining resources in the current workspace of the application's namespace.

    - Lifecycle: Set the commands that need to be executed when the container starts, after it starts, and before it stops. For details, please refer to [Container Lifecycle Configuration](../../../kpanda/user-guide/workloads/pod-config/lifecycle.md).

    - Health check: used to judge the health status of containers and applications, which helps to improve the availability of applications. For details, please refer to [Container Health Check Configuration](../../../kpanda/user-guide/workloads/pod-config/health-check.md).

    - Environment variables: Configure container parameters in Pods, add environment variables or pass configurations to Pods, etc. For details, please refer to [Container environment variable configuration](../../../kpanda/user-guide/workloads/pod-config/env-variables.md).

    - Data Storage: Configure the settings for container mounted data volumes and data persistence.

        <!--![]()screenshots-->

5. Refer to the following instructions to choose whether to enable advanced features, and then click `Create and upload Jar package`.

    - Service Mesh: Choose whether to enable the [Service Mesh for DCE 5.0](../../../mspider/intro/index.md) module to govern microservice traffic.
    - Microservice Engine: Whether to connect the newly created application to the [DCE 5.0 Microservice Engine](../../../skoala/intro/index.md) module.
        > For the configuration of the microservice engine, please refer to [Build Microservice Application Based on Git Repository](create-app-git.md).
    - Grayscale publishing: Select whether to enable grayscale publishing. For more information about canary release, please refer to [Canary Release](../release/canary.md).

        <!--![]()screenshots-->

6. Select the file to be uploaded and click `OK`.

    <!--![]()screenshots-->

7. After the creation is successful, the corresponding pipeline will be triggered to run. Click `Pipeline` in the left navigation bar to view its running status.

    > The naming rule of the pipeline is "corresponding application name-random number". For example, the corresponding application name is `demo` through the pipeline name `demo-4615a8`.

    <!--![]()screenshots-->

8. After the pipeline is successfully executed, click `Overview` on the left navigation bar and select the `Native App` tab to view the newly created app.

    <!--![]()screenshots-->