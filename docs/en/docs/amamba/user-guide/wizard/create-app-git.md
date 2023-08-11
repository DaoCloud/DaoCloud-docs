# Build microservice applications based on Git repository

Workbench supports building applications in four ways: Git repository, [Jar package](jar-java-app.md), container image, and Helm chart. This article introduces how to build a traditional microservice application through the source code of the Git warehouse, so as to manage the traffic of the application, view logs, monitor, traces and other features.

## prerequisites

- Need to create a workspace and a user, the user needs to join the workspace and give `workspace edit` role.
  Refer to [Creating a workspace](../../../ghippo/user-guide/workspace/workspace.md), [Users and roles](../../../ghippo/user-guide/access-control/user.md).
- Create two credentials that can access the code warehouse warehouse and mirror warehouse, refer to [credential management](../pipelines/credential.md).
- Prepare a Gitlab warehouse, Harbor warehouse.

## Create Credentials

1. Create two credentials on the Credentials page:

    - git-credential: username and password for accessing the code repository
    - registry-credential: username and password for accessing the mirror warehouse

1. After the creation is complete, you can see the credential information on the `Certificate List` page.

## Create a microservice application based on Git

1. On `Workbench` -> `Wizard` page, click `Build Based on Git Repository`.

    <!--![]()screenshots-->

2. Fill in the basic information by referring to the following instructions, and then click `Next`:

    - Name: Fill in the name of the application.
    - Resource type: supports stateless load and stateful load. This demo chooses stateless load.
    - Enter or select an application group.
    - Deployment location: Select which namespace under which cluster to deploy the application to. If you want to access microservices, please make sure that you have [created a registry](../../../skoala/trad-ms/hosted/create-registry.md) under the current workspace.
    - Number of instances: Fill in the number of instances and the number of Pods.

        <!--![]()screenshots-->

3. Fill in the pipeline configuration by referring to the instructions below, and then click `Next`.

    - Code repository: Enter the Git repository address, such as `https://gitlab.daocloud.cn/ndx/skoala.git`. Please use your own warehouse address in actual operation.
    - Branch: The default is `main`, here is `main`, no need to change.
    - Credentials: Select the credential `git-credential` for accessing the code warehouse. If it is a public warehouse, you do not need to fill in.
    - Dockerfile path: Enter the absolute path of the Dockerfile in the code warehouse, such as `demo/integration/springcloud-nacos-sentinel/code/Dockerfile`.
    - Target mirror name: Enter the name of the mirror warehouse, for example [`release-ci.daocloud.io/test-lfj/fromgit`](http://release-ci.daocloud.io/test-lfj/fromgit) .
    - Tag: Enter the mirror repository version, such as `v2.0.0`.
    - Credentials: Select the credential to access the registry, such as `registry-credential`.
    - ContextPath: ContextPath is the execution context path of the docker build command. Fill in the path relative to the root directory of the code, such as target, or the directory where the Dockerfile is located if not filled.
    - Build parameters: Build parameters will be passed to the parameters of the build command in the form of --build-arg, which supports setting the upstream product download address and upstream image download address as parameters, and supports custom arbitrary parameters.

        <!--![]()screenshots-->

4. Fill in the container configuration by referring to the instructions below, and click `Next`.

    - Service configuration: support intra-cluster access, node access, and load balancing. Example values ​​are as follows:

        ```
        - name: http protocol: TCP port: 8081 targetPort: 8081
        - name: health-http protocol: TCP port: 8999 targetPort: 8999
        - name: service protocol: TCP port: 9555 targetPort: 9555
        ```
        
        > For more detailed instructions on service configuration, please refer to [Create Service](../../../kpanda/user-guide/services-routes/create-services.md).
        
    - Resource limit: Specify the upper limit of resources that the application can use, including CPU and memory.

    - Lifecycle: Set the commands that need to be executed when the container starts, after it starts, and before it stops. For details, please refer to [Container Lifecycle Configuration](../../../kpanda/user-guide/workloads/pod-config/lifecycle.md).

    - Health check: used to judge the health status of containers and applications, which helps to improve the availability of applications. For details, please refer to [Container Health Check Configuration](../../../kpanda/user-guide/workloads/pod-config/health-check.md).

    - Environment variables: Configure container parameters in Pods, add environment variables or pass configurations to Pods, etc. For details, please refer to [Container environment variable configuration](../../../kpanda/user-guide/workloads/pod-config/env-variables.md).

    - Data Storage: Configure the settings for container mounted data volumes and data persistence.

        <!--![]()screenshots-->

5. On the `Advanced Configuration` page, click `Enable Microservice Access`, refer to the following instructions to configure parameters, and then click `OK`.

    - Select framework: support `Spring Cloud`, `Dubbo`, here choose `Spring Cloud`.
    - Registry instance: currently only supports the selection of [managed Nacos registry instance in the microservice engine](../../../skoala/trad-ms/hosted/create-registry.md).
    - Registry namespace: nacos namespace for microservice applications
    - Registry service grouping: service grouping of microservice applications
    - Username/Password: If the registry instance is authenticated, you need to fill in the username and password
    - Enable microservice governance: The selected registry instance should [enable the Sentinel or Mesh governance plugin](../../../skoala/trad-ms/hosted/plugins/plugin-center.md)
    - Monitoring: Select Enable, and you can view service-related monitoring information after enabling it
    - Log: enabled by default
    - Traces: After enabled, you can view the traces information of the service, currently only supports Java language

        <!--![]()screenshots-->

## View and access microservice related information

1. Click `Overview` on the left navigation bar, and in the `Native App` tab, hover the cursor over an app, and click `View More Details` on the floating menu.

    <!--![]()screenshots-->

1. Jump to the microservice engine to view service details.