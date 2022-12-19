# Create a route (Ingress)

In a Kubernetes cluster, [Ingress](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#ingress-v1beta1-networking-k8s-io) exposes services from outside the cluster to inside the cluster HTTP and HTTPS routing.
Traffic routing is controlled by rules defined on the Ingress resource. Here's an example of a simple Ingress that sends all traffic to the same Service:

![ingress-diagram](../../images/ingress.svg)

Ingress is an API object that manages external access to services in the cluster, and the typical access method is HTTP. Ingress can provide load balancing, SSL termination, and name-based virtual hosting.

## prerequisites

- Container management platform [connected to Kubernetes cluster](../Clusters/JoinACluster.md) or [created Kubernetes](../Clusters/CreateCluster.md), and can access the cluster UI interface.
- A [Namespace Creation](../Namespaces/createtens.md), [User Creation](../../../ghippo/04UserGuide/01UserandAccess/User.md) has been completed, and the user Authorization is the [`NS Edit`](../Permissions/PermissionBrief.md#ns-edit) role, for details, please refer to [Namespace Authorization](../Permissions/Cluster-NSAuth.md).

- When there are multiple containers in a single instance, please make sure that the ports used by the containers do not conflict, otherwise the deployment will fail.

### Create routes

1. After successfully logging in as the `NS Edit` user, click `Cluster List` in the upper left corner to enter the `Cluster List` page. In the list of clusters, click a cluster name.

    ![Cluster List](../../images/service01.png)

2. Click `Services and Routing` on the left, click the `Routing` tab, and click the `Create Routing` button in the upper right corner.

    ![Service and Routing](../../images/ingress01.png)

    !!! tip
    
        It is also possible to create a route via `YAML`.

3. Open `Create Route` page to configure. There are two protocol types to choose from, please refer to the following two parameter tables for configuration.

    ![create route](../../images/ingress02.png)

#### Create a route with protocol HTTP

| parameter | description | example value |
   | -------- | :--------------------------------------- -------------------- | :------ |
| Route name | 【Type】Required<br />【Meaning】Enter the name of the new route. <br />【Note】Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter, lowercase English letters or numbers. | Ing-01 |
| Namespace | 【Type】Required<br />【Meaning】Select the namespace where the new service is located. For more information about namespaces, please refer to [Namespace Overview](../Namespaces/createns.md). <br />【Note】Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | default |
| Protocol | [Type] Required<br /> [Meaning] Refers to the protocol that authorizes inbound access to the cluster service, and supports HTTP (no identity authentication required) or HTTPS (identity authentication needs to be configured) protocol. Here select the route of HTTP protocol. | HTTP |
| Domain Name | [Type] Required<br /> [Meaning] Use the domain name to provide external access services. The default is the domain name of the cluster | |
| Label | [Type] Optional<br /> [Meaning] Add a label for the route<br /> | |
| Annotation | 【Type】Optional<br />【Meaning】Add annotation for routing<br /> | |
   
#### Create a route with protocol HTTPS

| parameter | description | example value |
| :------- | :--------------------------------------- -------------------- | :------ |
| Route name | 【Type】Required<br />【Meaning】Enter the name of the new route. <br />【Note】Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter, lowercase English letters or numbers. | Ing-01 |
| Namespace | 【Type】Required<br />【Meaning】Select the namespace where the new service is located. For more information about namespaces, please refer to [Namespace Overview](../Namespaces/createns.md). <br />【Note】Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | default |
| Protocol | [Type] Required<br /> [Meaning] Refers to the protocol that authorizes inbound access to the cluster service, and supports HTTP (no identity authentication required) or HTTPS (identity authentication needs to be configured) protocol. Here select the route of HTTPS protocol. | HTTPS |
| Domain Name | [Type] Required<br /> [Meaning] Use the domain name to provide external access services. The default is the domain name of the cluster | |
| CA certificate | 【Type】Required<br />【Meaning】Certificate for identity authentication between the server and the client, and you can also upload it locally. | |
| Forwarding strategy | 【Type】Optional<br />【Meaning】Specify the access strategy of Ingress. <br />**Path**: Specify the URL path for service access, the default is the root path/<br />**Target Service**: The service name for routing<br />**Target Service Port**: The port exposed by the service | |
| Label | [Type] Optional<br /> [Meaning] Add a label for the route | |
| Annotation | 【Type】Optional<br />【Meaning】Add annotation for routing | |

### Complete route creation

After configuring all the parameters, click the `OK` button to return to the routing list automatically. On the right side of the list, click `︙` to modify or delete the selected route.

![route list](../../images/ingress03.png)