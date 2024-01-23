---
hide:
  - heel
---

# Microservice Gateway

The micro-service gateway supports the high-availability architecture of multi-tenant instances and is compatible with the unified gateway access capabilities of micro-services in various modes.

## Create

To create a microservice gateway, perform the following steps:

1. In the left navigation bar, click `Cloud native Gateway`, and in the upper right corner of the `Gateway List` page, click `Create Gateway` to enter the page for creating the micro-service gateway.

    ![go to the create page](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create01.png)

2. Follow the instructions below to complete the basic configuration (required).

    - Gateway name: contains a maximum of 63 letters, digits, hyphen (-) and must start and end with a letter or number character. The name cannot be changed after the gateway is created.
    - Deploy cluster: Select the cluster to deploy the gateway in.

        > If the target cluster does not appear in the optional list, you can go to the [Integrate](../../kpanda/user-guide/clusters/integrate-cluster.md) or [Create](../../kpanda/user-guide/clusters/create-cluster.md) cluster in the container management module and set the [The cluster or namespace under the cluster is bound to the current workspace ](../../../ghippo/user-guide/workspace/quota/#_4) through the global management module.

    - Namespace (deployment) : Select the namespace in which to deploy the gateway. Only one gateway can be deployed in a namespace.
    - Environment check : After the cluster and namespace are selected, the system automatically detects the installation environment. If the check fails, the system displays the cause and operation suggestions. You can perform operations as prompted.
    - Namespace (jurisdiction) : Sets which namespaces can be governed by the new gateway. Specifies the namespace of the default jurisdiction gateway. Supports managing multiple namespaces at the same time. A namespace cannot be managed by two gateways at the same time.

        ![fill in the basic configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create02.png)

3. Enter the configuration information according to the following instructions

    === "Service entry mode"

        - Intra-cluster access: Services can be accessed only within the same cluster

            ![fill in the basic configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create03.png)

        - Node port: Access services from outside the cluster through the IP address and static port of a node
              
            External traffic policy: 'Cluster' refers to Pods where traffic can be forwarded to other nodes in the cluster; 'Local' indicates that traffic can only be forwarded to the Pod on the local node.

            ![fill in the basic configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create04.png)

        - Load balancer: Use a cloud service provider"s load balancer to make services publicly accessible

            - External traffic policy: `Cluster` Indicates that traffic can be forwarded to pods on other nodes in the cluster. `Local` Indicates that traffic can be forwarded only to the Pod on the local node
            - Load balancing type: MetalLB or other
            - MetalLB IP pool: Supports automatic selection or assignment of IP pools
            - Load balancer IP address: You can automatically select or specify an IP address

            ![fill in the basic configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create05.png)

    === "Resource Settings"
           
        How many control nodes and working nodes are configured for the current gateway. Single copy is unstable, so select it with caution.

        ![fill in the basic configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create06.png)

    === "Advanced Settings"

        - Control node: Sets how many CPU and memory resources to configure for the control node (contour)
        - Working node: Sets how many CPU and memory resources are allocated to the working node (envoy)
            
        ![fill in the basic configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create07.png)

4. Follow the instructions below to complete the advanced configuration (optional).

    - Log Level: Sets log levels for working node (envoy) and Pod
    - Update Mode: 'Recreate' means to delete the original gateway and create a new gateway, 'rolling update' means not to delete the gateway, but to roll to update the gateway related Pod
    - Front-end Proxy: specifies how many proxy endpoints a request must pass through before reaching the gateway from the client. Set this parameter based on actual conditions. For example, 'client-nginx-gateway' has one agent layer because only one Nginx agent endpoint passes through it.
    - Gateway tracing: After this function is enabled, link information can be generated based on requests made through the gateway and sent to the observable module for data collection.

    ![fill in advanced settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create08.png)

5. Please refer to the following information to fill in the plug-in configuration (optional), and finally click 'confirm' in the lower right corner of the page.
    
    Select whether to enable the Global Rate Limit plugin.

    You need to access the plugin in the plugin center in advance, or click the blue text on the current page to jump to the corresponding page to access and create.

    ![fill in advanced settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create09.png)

!!! note

    Click `OK` at the lower right corner of the page to return to the micro-service gateway list page. You can perform the operations [Update Gateway](update-gateway.md) or [Delte Gateway](delete-gateway.md) on the right.

    ![confirm the information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/gw-create10.png)

## View

You can view the gateway details on `Overview`, including the name, deployment location, gateway running status, service entry mode, controller/working node health status, API, and plug-in information.

### Gateway details

On the `Gateway List` page, select the name of the target gateway to access the gateway overview page ".

![overview](./images/overview.png)

Gateway details are divided into basic information, network information, TOP10 popular apis, resource information, resource load, and plug-in information.

Some of the data are described as follows:

- Control/Working Node Instances: Displays the total number and health of node instances. `/` The number on the left represents the number of instances currently online, and the number on the right represents the total number of node instances.

    - If the online node `/left no.` is equal to all the online nodes `/right no.`, it is displayed in green.
    - If the online node `/left no.` is less than all the nodes that should be online `/right no.`, it is displayed in red.

- Top 10 APIs: The top 10 apis in descending order by number of API response codes (2xx, 4xx, and 5xx) are in descending order by default by number of response codes (200). You can view the data of the past 15 minutes, 1 hour, or 24 hours.
- Resource load: The CPU usage and Memory usage of the gateway control node and the working node in the last 1 hour or the last 3 hours are displayed as line charts.
- Plug-in information: Displays the start and stop of the current gateway plug-in and other available plug-ins.

### Related operation

In addition to viewing the gateway details, you can update the gateway configuration and delete the gateway on the gateway details page.

- Update gateway: Click `Edit` at the top of the page to jump to the page for updating gateway configuration. For details, see [Update Gateway Settings](update-gateway.md).
- Delete gateway: Click `...` at the top of the page and select `Delete` to go to the page for deleting gateway. For details, see [Delete Gateway](delete-gateway.md).

## Update

The micro-service gateway supports the high-availability architecture of multi-tenant instances and is compatible with the unified gateway access capabilities of micro-services in various modes.

## Update gateway configuration

There are two ways to update the gateway configuration.

- In the `Gateway List` page choose the gateway instance needs to be updated, at the instance of right click `...` and select `Edit`.

    ![update1](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/update1.png)

- Click the gateway name to access the overview page. In the upper right corner, click `Edit`.

    ![update2](./images/overview.png)

## Delete

The micro-service gateway supports the high-availability architecture of multi-tenant instances and is compatible with the unified gateway access capabilities of micro-services in various modes.

There are also two ways to delete a gateway. To ensure that services are not affected, release the API of all routes to the gateway before deleting it.

!!! danger

    Gateway deletion is irreversible, so please proceed with caution.

- In the `Gateway List` page choose the need to remove the gateway instance, at the instance of right click `...` and select `Delete`.

    ![delete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/gateway/images/delete.png)

- After entering into the overview page, click the gateway name in the upper right corner of the `...` and select `Delete`.

    ![delete-gateway](./images/delete-gateway.png)
