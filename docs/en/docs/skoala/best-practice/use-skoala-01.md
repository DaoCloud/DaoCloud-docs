# Sample application experience microservice governance

The micro service engine is a feature of DCE 5.0 Advanced edition, which includes registry center, configuration center, micro service governance (traditional micro service, cloud native micro service), cloud native gateway and other features. This page will walk you through the microservice governance capabilities of a sample application.

The full process of this best practice is as follows:

1. Deploy the sample application in Workbench and enable microservice governance
2. Enable the traditional micro-service governance plug-in in the micro-service engine
3. Configure the corresponding governance rules in the microservice engine
4. Expose apis and access applications in the microservice engine

## Sample application introduction

The sample application used in this practice is based on the OpenTelemetry standard demo application. The DaoCloud Large and Micro Services team has optimized it based on DCE 5.0 features to better reflect cloud native and observable capabilities, and to show the effects of micro-service governance. The sample application is open source on Github, visit [Github registry address ](https://github.com/openinsight-proj/openinsight-helm-charts) for more details.

The architecture diagram for the sample application is as follows:

<!--![]()screenshots-->-->

## Application deployment

[Workbench](../../amamba/intro/index.md) is an application management module of DCE 5.0. It supports the creation and maintenance of various types of applications, GitOps, and grayscale publishing, and can quickly deploy applications to any cluster. Workbench supports deployment of applications based on Git repository, Jar package, container image and Helm chart. This practice deployable the sample application based on `Helm chart`.

<!--![]()screenshots-->

Before deploying applications, the following conditions must be met:

- [Add Helm Repo](../../kpanda/user-guide/helm/helm-repo.md) in container management:

    <!--![]()screenshots-->

- [ Create the Nacos registry instance ](../trad-ms/hosted/index.md)

    > Notice Record the address of the registry for subsequent application installation.

    <!--![]()screenshots-->

### Deployment based on Helm chart

1. Locate the opentelemetry-demo application in `Workbench` -> __Wizard__ -> __From Helm chart__ and click the application card to install it

    <!--![]()screenshots-->

    <!--![]()screenshots-->

2. On the Helm installation interface, make sure that the deployment position is correct, and then update the parameter configuration in `JAVA_OPTS` according to the requirements below.

    <!--![]()screenshots-->

    Based on the registry address recorded above, update the parameter below with comments as follows:

    ```java
    -javaagent:./jmx_prometheus_javaagent-0.17.0.jar=12345:./prometheus-jmx-config.yaml
        -Dspring.extraAdLabel=Daocloud -Dspring.randomError=false
        -Dspring.matrixRow=200 -Dmeter.port=8888
        -Dspring.cloud.nacos.discovery.enabled=true       # change to true to enable
        -Dspring.cloud.nacos.config.enabled=true          # change to true to enable
        -Dspring.cloud.nacos.config.server-addr=nacos-test.skoala-test:8848           # change to address of Nacos
        -Dspring.application.name=adservice-springcloud
        -Dspring.cloud.nacos.discovery.server-addr=nacos-test.skoala-test:8848        # change to address of Nacos
        -Dspring.cloud.nacos.discovery.metadata.k8s_cluster_id=xxx                    # change to cluster ID of Nacos 
        -Dspring.cloud.nacos.discovery.metadata.k8s_cluster_name=skoala-dev           # change to cluster name of Nacos
        -Dspring.cloud.nacos.discovery.metadata.k8s_namespace_name=skoala-test        # change to ns of Nacos
        -Dspring.cloud.nacos.discovery.metadata.k8s_workload_type=deployment
        -Dspring.cloud.nacos.discovery.metadata.k8s_workload_name=adservice-springcloud
        -Dspring.cloud.nacos.discovery.metadata.k8s_service_name=adservice-springcloud
        -Dspring.cloud.nacos.discovery.metadata.k8s_pod_name=${HOSTNAME}
        -Dspring.cloud.sentinel.enabled=false          # change to true to enable Sentinel
        -Dspring.cloud.sentinel.transport.dashboard=nacos-test-sentinel.skoala-test:8080  # change to address of Sentinel console
    ```

    > For details about how to obtain the cluster ID, cluster name, and namespace name, see `kubectl get cluster <clusername> -o json | jq.metadata.uid`.

1. After the application is successfully created, the list of Helm applications in Workbench is displayed.

    <!--![]()screenshots-->

### Java project development and debugging

If other deployment modes are used, the method of configuring the registry address may be different. Java projects need to integrate the SDK of Nacos during development, and the registry provided by DCE 5.0 is fully compatible with open source Nacos, so you can directly use the SDK of open source Nacos. For details, see [ Deploy Java applications based on Jar packages ](../../amamba/user-guide/wizard/jar-java-app.md).

When using `java -jar` to start a project, add the corresponding environment variable configuration

```java
    -Dspring.cloud.nacos.discovery.enabled=false        # change to true to enable
    -Dspring.cloud.nacos.config.enabled=false           # change to true to enable
    -Dspring.cloud.sentinel.enabled=false               # change to true to enable
    -Dspring.cloud.nacos.config.server-addr=nacos-test.skoala-test:8848           # change to address of Nacos
    -Dspring.application.name=adservice-springcloud
    -Dspring.cloud.nacos.discovery.server-addr=nacos-test.skoala-test:8848        # change to address of Nacos
    -Dspring.cloud.nacos.discovery.metadata.k8s_cluster_id=xxx                    # change to cluster ID of Nacos
    -Dspring.cloud.nacos.discovery.metadata.k8s_cluster_name=skoala-dev           # change to cluster name of Nacos
    -Dspring.cloud.nacos.discovery.metadata.k8s_namespace_name=skoala-test        # change to ns of Nacos
    -Dspring.cloud.nacos.discovery.metadata.k8s_workload_type=deployment
    -Dspring.cloud.nacos.discovery.metadata.k8s_workload_name=adservice-springcloud
    -Dspring.cloud.nacos.discovery.metadata.k8s_service_name=adservice-springcloud
    -Dspring.cloud.nacos.discovery.metadata.k8s_pod_name=${HOSTNAME}
```

!!! note

    The `metadata` information above should not be missing, as the services displayed in the registry will lack this information.

### Use container image deployment

If you choose to deploy applications based on container images, you can directly enable micro-service governance in the user interface configuration and select the corresponding registry module for easier operation. For details, see [ Build micro-service application based on Git repository ](../../amamba/user-guide/wizard/create-app-git.md).

<!--![]()screenshots-->

## Enable traditional micro-service governance

Before using the micro-service governance function, you need to enable the corresponding governance plug-in in the plug-in center under the corresponding registry. The plug-in Center provides two plug-ins, Sentinel governance and Mesh governance, and supports visual configuration through the user interface. After the plug-in is installed, the micro-service governance capability can be expanded to meet service requirements in different cases.

In this practice, traditional micro-service governance is adopted, namely, Sentinel governance plug-in is opened. For details, see [ Enable the Sentinel governance plug-in ](../trad-ms/hosted/plugins/sentinel.md).

<!--![]()screenshots-->

## Configure corresponding governance rules

After the application is successfully deployed, you can view the corresponding service in `Microservice List` under the prepared registry. The microservice list provides traffic governance rules, such as flow control rules, circuit breaker degradation rules, hotspot rules, system rules, and authorization rules. This practice takes the flow control rule as an example to demonstrate.

<!--![]()screenshots-->

### Configure the flow control policy

Here is an example of a traffic limiting policy. You can add a corresponding traffic limiting policy to a service through simple configuration.

<!--![]()screenshots-->

### Test the flow control policy

By accessing the service address, we can see that if the number of requests in one minute is more than 2, the subsequent requests will be intercepted. It automatically recovers after more than 1 minute.

## Expose the API and access the application

After the deployment of a micro-service application is complete, the application portal needs to be opened to external access through the API gateway. This step is the complete service usage experience. To expose service apis, you need to create a cloud native gateway, connect services to the gateway, and create API routes.

### Create a cloud native gateway

Create a cloud native gateway. For details, see [Create Gateway](../gateway/index.md).

!!! note

    When creating a gateway, it is recommended to deploy the gateway in the cluster where the sample application is located, and the gateway should govern the namespace where the sample application resides.

<!--![]()screenshots-->

### Access service

Based on the DCE 5.0 feature, the cloud native gateway can automatically discover services in the managed namespace. Therefore, you do not need to manually access services.

Nacos Registry services are adopted in this demonstration, which greatly expands the number of services accessible to the gateway. Services accessible to Nacos registry can be selected from `Add Service`.

<!--![]()screenshots-->

!!! info

    When a service is not within the namespace governed by the gateway or when you want to access the registry or other external services (using domain names/IP), you can manually connect to the service.

### Create an API route

See [Add API](../gateway/api/index.md) to create an API route.

<!--![]()screenshots-->

### Access application

After the gateway API is created, you can access the application page by using ** Domain name ** and ** External API path ** configured during API creation, as shown in the following figure.

** The home page of the sample application **:

<!--![]()screenshots-->

** The order confirmation page for the sample application **:

<!--![]()screenshots-->

## Conclusion

This is the experience of the entire microservices engine module. With the support of the entire DCE 5.0 capability, we successfully completed application deployment, enabling micro-service governance, configuring and testing micro-service governance policies, opening apis through cloud native gateway, and actually accessing applications.

### More capabilities

After our application is deployed successfully, we rely heavily on the observation capability provided by DCE 5.0 for subsequent application maintenance. Next, we will add the corresponding observable capability practice.

- View the topology of the deployed application
- View application logs
- View API access logs of the CSA
