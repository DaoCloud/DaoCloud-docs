# Create a Service

In a Kubernetes cluster, each Pod has an internal independent IP address, but Pods in the workload may be
created and deleted at any time, and directly using the Pod IP address cannot provide external services.

This requires creating a service. Through the service you get a fixed IP address, which decouples the
front-end and back-end of the workload and enables external users to access the service. In addition, the
service also provides the load balancing (LoadBalancer) feature, enabling users to access workloads from
the public network.

## Prerequisites

- In the Container Management module, you have [integrated the Kubernetes cluster](../clusters/integrate-cluster.md) or [created the Kubernetes cluster](../clusters/create-cluster.md), and can access the UI of the cluster.

- Completed a [namespace creation](../namespaces/createns.md), [user creation](../../../ghippo/user-guide/access-control/user.md), and authorized the user as [NS Editor](../permissions/permission-brief.md#ns-editor) role. For details, refer to [Namespace Authorization](../permissions/cluster-ns-auth.md).

- When there are multiple containers in a single instance, make sure that the ports used by the containers do not conflict, otherwise the deployment will fail.

## Create service

1. After successfully logging in as the __NS Editor__ user, click __Clusters__ in the upper left corner to enter the __Clusters__ page. In the list of clusters, click a cluster name.

     

2. In the left navigation bar, click __Container Network__ -> __Service__ to enter the service list, and click the __Create Service__ button in the upper right corner.

     

     !!! tip

         You can also [create a service via YAML](#yaml-example).

3. On the __Create Service__ page, select an access type, and configure it according to the following parameter tables.

     

    === "Create ClusterIP service"

        Select __Intra-Cluster Access (ClusterIP)__ , which means exposing the service through the internal IP of the cluster. Services of this type can only be accessed within the cluster. This is the default service type.

        | Parameter | Description | Example value |
        | --- | :-- | :---- |
        | Access type | [Type] Required<br />[Meaning] Specify the method of Pod service discovery, here select intra-cluster access (ClusterIP). | ClusterIP |
        | Service name | [Type] Required<br />[Meaning] Enter the name of the new service. <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | Svc-01 |
        | Namespace | [Type] Required<br />[Meaning] Select the namespace where the new service is located. For more information about namespaces, refer to [Namespace Overview](../namespaces/createns.md). <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | default |
        | Label selector | [Type] Required<br />[Meaning] Add a label, and the Service selects a Pod according to the label. After filling it in, click **Add** . You can also reference the label of an existing workload: click __Reference workload label__ , select the workload in the pop-up window, and the system will use the selected workload label as the selector by default. | app:job01 |
        | Port configuration | [Type] Required<br />[Meaning] To add a protocol port to the service, you need to select the port protocol type first. Currently, TCP and UDP transport protocols are supported. <br />**Port name**: Enter a custom port name. <br />**Service port (port)**: The access port through which the Pod provides services externally. <br />**Container port (targetport)**: The container port that the workload actually listens to, used to expose services within the cluster. | |
        | Session persistence | [Type] Optional<br />[Meaning] When enabled, requests from the same client will be forwarded to the same Pod | Enabled |
        | Maximum session persistence duration | [Type] Optional<br />[Meaning] After session persistence is enabled, the maximum duration to maintain it | 30 seconds |
        | Annotation | [Type] Optional<br />[Meaning] Add an annotation for the service | |

    === "Create NodePort service"

        Select __Node Access (NodePort)__ , which means exposing the service through the IP and static port ( __NodePort__ ) on each node.
        The __NodePort__ service is routed to the automatically created __ClusterIP__ service. By requesting __<Node IP>:<Node Port>__ ,
        you can access a __NodePort__ service from outside the cluster.

        | Parameter | Description | Example value |
        | --- | :-- | :---- |
        | Access type | [Type] Required<br />[Meaning] Specify the method of Pod service discovery | NodePort |
        | Service name | [Type] Required<br />[Meaning] Enter the name of the new service. <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | Svc-01 |
        | Namespace | [Type] Required<br />[Meaning] Select the namespace where the new service is located. For more information about namespaces, refer to [Namespace Overview](../namespaces/createns.md). <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | default |
        | Label selector | [Type] Required<br />[Meaning] Add a label, and the Service selects a Pod according to the label. After filling it in, click **Add** . You can also reference the label of an existing workload: click __Reference workload label__ , select the workload in the pop-up window, and the system will use the selected workload label as the selector by default. | |
        | Port configuration | [Type] Required<br />[Meaning] To add a protocol port to the service, you need to select the port protocol type first. Currently, TCP and UDP transport protocols are supported. <br />**Port name**: Enter a custom port name. <br />**Service port (port)**: The access port through which the Pod provides services externally. By default, for convenience, the service port is set to the same value as the container port field. <br />**Container port (targetport)**: The container port that the workload actually listens to. <br />**Node port (nodeport)**: The port of the node, which receives traffic transmitted from the ClusterIP. It is used as the entrance for external traffic access. | |
        | Session persistence | [Type] Optional<br />[Meaning] When enabled, requests from the same client will be forwarded to the same Pod<br />After it is enabled, the `.spec.sessionAffinity` of the Service is __ClientIP__ . For details, refer to [Session Affinity for a Service](https://kubernetes.io/docs/reference/networking/virtual-ips/#session-affinity) | Enabled |
        | Maximum session persistence duration | [Type] Optional<br />[Meaning] After session persistence is enabled, the maximum duration to maintain it<br />.spec.sessionAffinityConfig.clientIP.timeoutSeconds is set to 30 seconds by default | 30 seconds |
        | Annotation | [Type] Optional<br />[Meaning] Add an annotation for the service | |

    === "Create LoadBalancer service"

        Select __Load Balancing (LoadBalancer)__ , which means using the cloud provider's load balancer to expose the service to the outside.
        The external load balancer can route traffic to the automatically created __NodePort__ service and __ClusterIP__ service.

        | Parameter | Description | Example value |
        | --- | :--- | :--- |
        | Access type | [Type] Required<br />[Meaning] Specify the method of Pod service discovery | LoadBalancer |
        | Service name | [Type] Required<br />[Meaning] Enter the name of the new service. <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | Svc-01 |
        | Namespace | [Type] Required<br />[Meaning] Select the namespace where the new service is located. For more information about namespaces, refer to [Namespace Overview](../namespaces/createns.md). <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | default |
        | External traffic policy | [Type] Required<br />[Meaning] Set the external traffic policy. <br />**Cluster**: Traffic can be forwarded to Pods on all nodes in the cluster. <br />**Local**: Traffic is only sent to Pods on this node. <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | Cluster |
        | Label selector | [Type] Required<br />[Meaning] Add a label, and the Service selects a Pod according to the label. After filling it in, click **Add** . You can also reference the label of an existing workload: click __Reference workload label__ , select the workload in the pop-up window, and the system will use the selected workload label as the selector by default. | |
        | Load balancing type | [Type] Required<br />[Meaning] The load balancing type used. Currently, MetalLB and others are supported. | MetalLB |
        | MetalLB IP pool | [Type] Required<br />[Meaning] When the selected load balancing type is MetalLB, the LoadBalancer Service will allocate IP addresses from this pool by default and announce all IP addresses in this pool through ARP. For details, refer to [Install MetalLB](../../../network/modules/metallb/install.md) | |
        | Load balancing address | [Type] Required<br />[Meaning] <br />1. If you are using a public cloud CloudProvider, fill in the load balancing address provided by the cloud provider here;<br />2. If the above load balancing type is selected as MetalLB, the IP will be obtained from the above IP pool by default; if not filled in, it will be obtained automatically. | Automatically obtained |
        | Port configuration | [Type] Required<br />[Meaning] To add a protocol port to the service, you need to select the port protocol type first. Currently, TCP and UDP transport protocols are supported. <br />**Port name**: Enter a custom port name. <br />**Service port (port)**: The access port through which the Pod provides services externally. By default, for convenience, the service port is set to the same value as the container port field. <br />**Container port (targetport)**: The container port that the workload actually listens to. <br />**Node port (nodeport)**: The port of the node, which receives traffic transmitted from the ClusterIP. It is used as the entrance for external traffic access. | |
        | Annotation | [Type] Optional<br />[Meaning] Add an annotation for the service | |

    === "Create ExternalName service"

        Select __External Service (ExternalName)__ , which means exposing the service by mapping it to an external domain name.
        Services of this type do not create the typical ClusterIP or NodePort; instead, they resolve the DNS name to redirect requests to the external service address.

        | Parameter | Description | Example value |
        | --- | :--- | :--- |
        | Access type | [Type] Required<br />[Meaning] Specify the method of Pod service discovery, here select external service (ExternalName). | ExternalName |
        | Service name | [Type] Required<br />[Meaning] Enter the name of the new service. <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | Svc-01 |
        | Namespace | [Type] Required<br />[Meaning] Select the namespace where the new service is located. For more information about namespaces, refer to [Namespace Overview](../namespaces/createns.md). <br />[Note] Please enter a string of 4 to 63 characters, which can contain lowercase English letters, numbers and dashes (-), and start with a lowercase English letter and end with a lowercase English letter or number. | default |
        | Domain name | [Type] Required | |

4. After configuring all parameters, click the __OK__ button to automatically return to the service list. On the right side of the list, click __┇__ to modify or delete the selected service.

    ![Service list](../images/service04.png)

## YAML example

```yaml
kind: Service
apiVersion: v1
metadata:
  name: nvidia-dcgm-exporter
  namespace: gpu-operator
  uid: 7e412db9-2d23-4599-b48c-91e434aebef1
  resourceVersion: '408861'
  creationTimestamp: '2024-12-09T09:11:41Z'
  labels:
    app: nvidia-dcgm-exporter
  annotations:
    prometheus.io/scrape: 'true'
  ownerReferences:
    - apiVersion: nvidia.com/v1
      kind: ClusterPolicy
      name: cluster-policy
      uid: 59e6c966-abb9-45be-b13e-e51e31e7e55b
      controller: true
      blockOwnerDeletion: true
spec:
  ports:
    - name: gpu-metrics
      protocol: TCP
      port: 9400
      targetPort: 9400
  selector:
    app: nvidia-dcgm-exporter
  clusterIP: 10.233.29.230
  clusterIPs:
    - 10.233.29.230
  type: ClusterIP
  sessionAffinity: None
  ipFamilies:
    - IPv4
  ipFamilyPolicy: SingleStack
  internalTrafficPolicy: Cluster
status:
  loadBalancer: {}
```
