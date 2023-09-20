# Create a route (Ingress)

In a Kubernetes cluster, [Ingress](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.24/#ingress-v1beta1-networking-k8s-io) exposes services from outside the cluster to inside the cluster HTTP and HTTPS routing.
Traffic routing is controlled by rules defined on the Ingress resource. Here's an example of a simple Ingress that sends all traffic to the same Service:

![ingress-diagram](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/ingress.svg)

Ingress is an API object that manages external access to services in the cluster, and the typical access method is HTTP. Ingress can provide load balancing, SSL termination, and name-based virtual hosting.

## Prerequisites

- Container management module [connected to Kubernetes cluster](../clusters/integrate-cluster.md) or [created Kubernetes](../clusters/create-cluster.md), and can access the cluster UI interface.
- Completed a [namespace creation](../namespaces/createns.md), [user creation](../../../ghippo/user-guide/access-control/user.md), and authorize the user as [`NS Edit`](../permissions/permission-brief.md#ns-edit) role, for details, please refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).
- Completed [Create Ingress Instance](../../../network/modules/ingress-nginx/install.md), [Deploy Application Workload](../workloads/create-deployment.md), and have [created the corresponding Service](create-services.md)
- When there are multiple containers in a single instance, please make sure that the ports used by the containers do not conflict, otherwise the deployment will fail.

## create route

1. After successfully logging in as the `NS Edit` user, click `Cluster List` in the upper left corner to enter the `Cluster List` page. In the list of clusters, click a cluster name.

     

2. In the left navigation bar, click `Container Network`->`Routing` to enter the service list, and click the `Create Route` button in the upper right corner.

     

     !!! tip

         It is also possible to create a route via `YAML`.

3. Open `Create Route` page to configure. There are two protocol types to choose from, please refer to the following two parameter tables for configuration.

     

### Create HTTP protocol route

- | parameter | description | example value |
   | -------------- | :--------------------------------- -------------------------- | :------------------ |
   | Route name | [Type] Required<br />[Meaning] Enter the name of the new route. <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter, lowercase English letters or numbers. | Ing-01 |
   | Namespace | [Type] Required<br />[Meaning] Select the namespace where the new service is located. For more information about namespaces, please refer to [Namespace Overview](../namespaces/createns.md). <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | default |
   | Protocol | [Type] Required<br /> [Meaning] Refers to the protocol that authorizes inbound access to the cluster service, and supports HTTP (no identity authentication required) or HTTPS (identity authentication needs to be configured) protocol. Here select the route of HTTP protocol. | HTTP |
   | Domain Name | [Type] Required<br /> [Meaning] Use the domain name to provide external access services. The default is the domain name of the cluster | testing.daocloud.io |
   | Load Balancer Type | [Type] Required<br /> [Meaning] The usage range of the Ingress instance. [Scope of use of Ingress](../../../network/modules/ingress-nginx/scope.md)<br /> `Platform-level load balancer`: In the same cluster, share the same Ingress instance, where all Pods can receive requests distributed by the load balancer. <br />`Tenant-level load balancer`: Tenant load balancer, the Ingress instance belongs exclusively to the current namespace, or belongs to a certain workspace, and the set workspace includes the current namespace, and all Pods can receive it Requests distributed by this load balancer. | Platform Level Load Balancer |
   | Ingress Class | [Type] Optional<br />[Meaning] Select the corresponding Ingress instance, and import traffic to the specified Ingress instance after selection. When it is None, the default DefaultClass is used. Please set the DefaultClass when creating an Ingress instance. For more information, please refer to [Ingress Class](../../../network/modules/ingress-nginx/ingressclass.md)< br /> | Ngnix |
   | Session persistence| [Type] Optional<br />[Meaning] Session persistence is divided into three types: `L4 source address hash`, `Cookie Key`, `L7 Header Name`. Keep<br />`L4 Source Address Hash`: : When enabled, the following tag is added to the Annotation by default: nginx.ingress.kubernetes.io/upstream-hash-by: "$binary_remote_addr"<br /> `Cookie Key` : When enabled, the connection from a specific client will be passed to the same Pod. After enabled, the following parameters are added to the Annotation by default:<br /> nginx.ingress.kubernetes.io/affinity: "cookie"<br /> nginx.ingress.kubernetes .io/affinity-mode: persistent<br />`L7 Header Name`: After enabled, the following tag is added to the Annotation by default: nginx.ingress.kubernetes.io/upstream-hash-by: "$http_x_forwarded_for" | Close |
   | Path Rewriting| [Type] Optional<br /> [Meaning] `rewrite-target`, in some cases, the URL exposed by the backend service is different from the path specified in the Ingress rule. If no URL rewriting configuration is performed, There will be an error when accessing. | close |
   | Redirect | [Type] Optional<br />[Meaning] `permanent-redirect`, permanent redirection, after entering the rewriting path, the access path will be redirected to the set address. | close |
   | Traffic Distribution | [Type] Optional<br />[Meaning] After enabled and set, traffic distribution will be performed according to the set conditions. <br />`Based on weight`: After setting the weight, add the following Annotation to the created Ingress: `nginx.ingress.kubernetes.io/canary-weight: "10"`<br />`Based on Cookie`: set After the cookie rules, the traffic will be distributed according to the set cookie conditions<br /> `Based on Header`: After setting the header rules, the traffic will be distributed according to the set header conditions | Close |
   | Label | [Type] Optional<br /> [Meaning] Add a label for the route<br /> | - |
   | Annotation | [Type] Optional<br /> [Meaning] Add annotation for routing<br /> | - |

### Create HTTPS protocol route

| parameter | description | example value |
| :------------- | :--------------------------------- -------------------------- | :------------------ |
| Route name | [Type] Required<br />[Meaning] Enter the name of the new route. <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter, lowercase English letters or numbers. | Ing-01 |
| Namespace | [Type] Required<br />[Meaning] Select the namespace where the new service is located. For more information about namespaces, please refer to [Namespace Overview](../namespaces/createns.md). <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | default |
| Protocol | [Type] Required<br /> [Meaning] Refers to the protocol that authorizes inbound access to the cluster service, and supports HTTP (no identity authentication required) or HTTPS (identity authentication needs to be configured) protocol. Here select the route of HTTPS protocol. | HTTPS |
| Domain Name | [Type] Required<br /> [Meaning] Use the domain name to provide external access services. The default is the domain name of the cluster | testing.daocloud.io |
| Secret | [Type] Required<br /> [Meaning] Https TLS certificate, [Create Secret](../configmaps-secrets/create-secret.md). | |
| Forwarding strategy | [Type] Optional<br />[Meaning] Specify the access strategy of Ingress. <br />**Path**: Specifies the URL path for service access, the default is the root path/<br />**directoryTarget service**: Service name for routing<br />**Target service port**: Port exposed by the service | |
| Load Balancer Type | [Type] Required<br /> [Meaning] The usage range of the Ingress instance. <br />`Platform-level load balancer`: In the same cluster, the same Ingress instance is shared, and all Pods can receive requests distributed by the load balancer. <br />`Tenant-level load balancer`: Tenant load balancer, the Ingress instance belongs exclusively to the current namespace or to a certain workspace. This workspace contains the current namespace, and all Pods can receive the load from this Balanced distribution of requests. | Platform Level Load Balancer |
| Ingress Class | [Type] Optional<br />[Meaning] Select the corresponding Ingress instance, and import traffic to the specified Ingress instance after selection. When it is None, the default DefaultClass is used. Please set the DefaultClass when creating an Ingress instance. For more information, please refer to [Ingress Class](../../../network/modules/ingress-nginx/ingressclass.md)< br /> | None |
| Session persistence| [Type] Optional<br />[Meaning] Session persistence is divided into three types: `L4 source address hash`, `Cookie Key`, `L7 Header Name`. Keep<br />`L4 Source Address Hash`: : When enabled, the following tag is added to the Annotation by default: nginx.ingress.kubernetes.io/upstream-hash-by: "$binary_remote_addr"<br /> `Cookie Key` : When enabled, the connection from a specific client will be passed to the same Pod. After enabled, the following parameters are added to the Annotation by default:<br /> nginx.ingress.kubernetes.io/affinity: "cookie"<br /> nginx.ingress.kubernetes .io/affinity-mode: persistent<br />`L7 Header Name`: After enabled, the following tag is added to the Annotation by default: nginx.ingress.kubernetes.io/upstream-hash-by: "$http_x_forwarded_for" | Close |
| Label | [Type] Optional<br /> [Meaning] Add a label for the route | |
| Annotation | [Type] Optional<br />[Meaning] Add annotation for routing | |

### Complete route creation

After configuring all the parameters, click the `OK` button to return to the routing list automatically. On the right side of the list, click `︙` to modify or delete the selected route.

