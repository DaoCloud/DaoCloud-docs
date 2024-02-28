# Istio resource management

The __Istio Resource Management__ page lists all Istio resources by resource type, providing users with the ability to display, create, edit, and delete various resources.

This page provides the following resource types:

### Traffic management class

| **Resource Type** | **Description** |
| --------------------------- | --------------------- ------------------------------------------ |
| DestinationRule (target rule) | Destination rule is an important part of service governance. Destination rule divides request traffic by port, service version, etc., and customizes Envoy traffic policy for each request traffic, and applies it to the traffic policy Not only load balancing, but also the minimum number of connections, fuses, etc. |
| EnvoyFilter | This resource provides the ability to configure Envoy, which can define new filters, listeners\clusters, etc. Be cautious when using this resource. Misconfiguration may have a great impact on the stability of the entire mesh environment. Note: <br> - EnvoyFilter can be configured in the Istio root directory (effective for all workloads) or a certain workload (use the workload selection tag); <br> - When multiple EnvoyFilters act on the same workload, they will Priority execution in order of creation; |
| Gateway (gateway rules) | Gateway rules are used to define the load balancer at the edge of the mesh, to expose services outside the mesh, or to provide external access to internal services. Compared with the ingress object of k8s, the gateway rule of istio adds more features: l L4-L6 load balancing l external mTLS l SNI support l other internal network features already implemented in istio: Fault Injection, Traffic Shifting, Circuit Breaking, image For the support of L7, gateway rules are realized by cooperating with virtual services. |
| ProxyConfig | Used to expose configuration options for the proxy, such as the number of threads for the proxy. This resource is optional, if not created, the system will use the built-in default value; Note:<br> - Any configuration changes in ProxyConfig need to restart the related workload to take effect;<br > - Act on the mesh or namespace The ProxyConfig cannot contain any workload selection tags, otherwise it will only be applied to the selected workload; |
| WorkloadEntry | This resource provides a description of non-k8s standard workloads, such as workloads running on virtual machines. WorkloadEntry needs to be used in conjunction with service entries, and service entries establish the correspondence between services and workloads through filters; |
| ServiceEntry (Service Entry) | ServiceEntry allows adding additional entries to Istio's internal service registry so that auto-discovered services in the mesh can access/route to these manually specified services. The service entry describes the attributes of the service, including: DNS name, VIP, port, protocol, endpoint, etc. These services can be external to the mesh (eg: web API) or services inside the mesh that cannot be registered automatically (eg: a database, several VMs). |
| SideCar | Sidecar is used to describe the traffic forwarding configuration between a sidecar pair of workload instances. By default, Istio will support forwarding communication between all workload instances in the mesh and accept all port traffic related to the workload. Note: <br> - The SideCar under the root namespace takes effect for all namespaces and workloads that are not configured with SideCar; <br> - if there are multiple SideCars in any namespace or workload, it will be defined as undefined behavior (no effective resource); |
| VirtualService (virtual service) | In the virtual service, it provides routing support for HTTP, TCP, and TLS protocols, and can implement routing for different regions and user requests through multiple matching methods (port, host, header, etc.) Forwarding, distribution to specific service versions, dividing the load according to the weight ratio, and providing various governance tools such as fault injection and traffic image. |
| WorkloadGroup | A WorkloadGroup describes a collection of workload instances and defines the specification details of a workload instance bootstrap agent, including metadata and identity. WorkloadGroup is only for non-Kubernetes workloads, simulate sidecar injection and deployment in Kubernetes, bootstrap Istio proxy, |

### Security Governance Class

| **Resource Type** | **Description** |
| ----------------------------------------- | ----------- -------------------------------------------------- |
| AuthorizationPolicy (authorization policy) | Authorization policy is similar to a four-layer to seven-layer "firewall". It will analyze and match the data flow like a traditional firewall, and then perform corresponding actions. Whether it is a request from the outside or a request between services in the mesh, the authorization policy is applicable. |
| PeerAuthentication (peer-to-peer identity authentication) | Peer-to-peer identity authentication provides two-way security authentication between services. At the same time, the creation, distribution, and rotation of keys and certificates are also automatically completed by the system, which is transparent to users, thus greatly reducing security configuration management. of complexity. |
| RequestAuthentication (request identity authentication) | Request identity authentication is used for authentication of requests initiated by external users to internal services of the mesh. Users use jwt to implement request encryption; each request identity authentication needs to configure an authorization policy |

### Proxy extension class

| **Resource Type** | **Description** |
| ------------ | ------------------------------------ ------------------------ |
| WasmPlugin | WasmPlugin provides extended features for the Istio proxy through the WebAssembly filter, and the filter capability it provides can form a complex interactive relationship with the internal filter of Istio. |

### System settings class

| **Resource Type** | **Description** |
| ------------ | ------------------------------------ ------------------------ |
| Telementry | This resource defines how to generate telemetry for workloads in the mesh, and provides Istio with the configuration of three observability tools: metrics, logs, and full link tracing. Note: Telemetry resources created in the Istio root directory and without workload selectors will be globally available to the mesh. |

## UI operation example

Users can add, delete, modify and query resources in the form of YAML. Here is an example creation/deletion of a telemetry resource.

1. Click __Mesh Configuration__ -> __Istio Resource Management__ in the left navigation bar, and click the __Create with YAML__ button in the upper right corner.

     

2. On the Create with YAML page, enter the correct YAML statement and click __OK__ .

     

     ```yaml
     apiVersion: telemetry.istio.io/v1alpha1
     kind: Telemetry
     metadata:
       name: namespace-metrics
       namespace: default
     spec:
       # Unspecified selector, applies to all workloads in the namespace
       metrics:
       - providers:
         - name: prometheus
         overrides:
         - tagOverrides:
     ​ request_method:
     ​ value: "request.method"
     ​ request_host:
     ​ value: "request.host"
     ```

3. Return to the resource list, click the __⋮__ button in the operation column, and you can select more operations such as edit and delete from the pop-up menu.

     