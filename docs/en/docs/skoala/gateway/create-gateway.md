---
hide:
  - heel
---

# Create a microservice gateway

The micro-service gateway supports the high-availability architecture of multi-tenant instances and is compatible with the unified gateway access capabilities of micro-services in various modes. This page describes how to create a microservice gateway instance.

To create a microservice gateway, perform the following steps:

1. In the left navigation bar, click `Cloud native Gateway`, and in the upper right corner of the `Gateway List` page, click `Create Gateway` to enter the page for creating the micro-service gateway.

    <!--![]()screenshots-->

2. Follow the instructions below to complete the basic configuration (required).

    - Gateway name: contains a maximum of 63 letters, digits, and underscores (_). The name cannot be changed after the gateway is created.
    - Deploy cluster: Select the cluster to deploy the gateway in.

        > If the target cluster does not appear in the optional list, you can go to the [Integrate](../../kpanda/user-guide/clusters/integrate-cluster.md) or [Create](../../kpanda/user-guide/clusters/create-cluster.md) cluster in the container management module and set the [The cluster or namespace under the cluster is bound to the current workspace ](../../../ghippo/user-guide/workspace/quota/#_4) through the global management module.

    - Namespace (deployment) : Select the namespace in which to deploy the gateway. Only one gateway can be deployed in a namespace.
    - Namespace (jurisdiction) : Sets which namespaces can be governed by the new gateway. Specifies the namespace of the default jurisdiction gateway. Supports managing multiple namespaces at the same time. A namespace cannot be managed by two gateways at the same time.

        <!--![]()screenshots-->

    - Service entry mode:

        - Intra-cluster access: Services can be accessed only within the same cluster

            <!--![]()screenshots-->

        - Node port: Access services from outside the cluster through the IP address and static port of a node

            <!--![]()screenshots-->

        - Load balancer: Use a cloud service provider"s load balancer to make services publicly accessible

            - External traffic policy: `Cluster` Indicates that traffic can be forwarded to pods on other nodes in the cluster. `Local` Indicates that traffic can be forwarded only to the Pod on the local node
            - Load balancing type: MetalLB or other
            - MetalLB IP pool: Supports automatic selection or assignment of IP pools
            - Load balancer IP address: You can automatically select or specify an IP address

                <!--![]()screenshots-->

    - Resource configuration: How many control nodes and working nodes are configured for the current gateway. Single copy is unstable, so select it with caution
    - Component version dependency: Displays the components that are required to create a gateway

        <!--![]()screenshots-->

3. Follow the instructions below to complete the advanced configuration (optional).

    - Log configuration: Sets log levels for working node (envoy) and Pod
    - Resource configuration: Configure CPU and memory resources for controller and working nodes

        <!--![]()screenshots-->

    - Update mechanism: `Create` indicates that the original gateway is deleted and a new gateway is created. `Rolling Update` indicates that the Pod related to the gateway is updated rolling instead of deleting the gateway
    - Number of proxy layers before the gateway: Several proxy endpoints must pass through the request from the client to the gateway. Enter this parameter based on the actual situation. For example, `Client-Nginx-Gateway` has one proxy level because only one Nginx proxy endpoint passes between them.

        <!--![]()screenshots-->

4. Click `OK` at the lower right corner of the page to return to the micro-service gateway list page. You can perform the operations [Update Gateway](update-gateway.md) or [Delte Gateway](delete-gateway.md) on the right.

    <!--![]()screenshots-->
