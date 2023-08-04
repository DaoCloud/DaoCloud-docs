# What is Calico

Calico creates and manages a flat, three-layer network (no overlay required), with each container assigned a routable IP.
Without packet encap/decap for communication, it has low network performance loss, and the convenience of both troubleshoot and horizontal scale.

Small-scale deployments can be interconnected directly through a BGP client, while large ones can be done through a designated BGP Route Reflector, which ensures that all data traffic is interconnected by IP routing.

Powered by iptables, Calico provides rich and flexible network policies, securing multi-tenant segregation of workloads, security groups and other access restrictions through ACLs on each node.

!!! info

    Calico literally means tabby cats, or cats with three colors as its logo shown below.

    

## Calico Components

Calico is composed of the following components, some of which are optional when deploying.

- [Calico API Server](#calico-api-server)
- [Felix](#felix)
- [BIRD](#bird)
- [confd](#confd)
- [Dikastes](#dikastes)
- [CNI plugin](#cni-plugin)
- [Datastore plugin](#datastore-plugin)
    - [Kubernetes API datastore（kdd）](#kubernetes-api-datastorekdd)
    - [etcd](#etcd)
- [IPAM plugin](#ipam-plugin)
- [kube-controller](#kube-controller)
- [Typha](#typha)
- [calicoctl](#calicoctl)
- [Plugins for cloud orchestrators](#plugins-for-cloud-orchestrators)

### Calico API Server

Let you manage Calico resources directly with kubectl.

### Felix

Run on each machine that hosts endpoints as an agent daemon. Program routes and ACLs, and anything else required on the host to provide desired connectivity for the endpoints on that host.

Depending on the specific orchestrator environment, Felix is responsible for:

- Interface management

    Program information about interfaces is written into the kernel so the kernel can correctly handle the traffic from that endpoint.
    In particular, it ensures that the host responds to ARP requests from each workload with the MAC of the host, and enables IP forwarding
    for interfaces that it manages. It also monitors interfaces to ensure that the programming is applied at the appropriate time.

- Route programming

    Program routes to the endpoints on its host into the Linux kernel FIB (Forwarding Information Base).
    This ensures that packets destined for those endpoints that arrive on at the host are forwarded accordingly.

- ACL programming

    Program ACLs into the Linux kernel to ensure that only valid traffic can be sent between endpoints, and that endpoints cannot circumvent Calico security measures.

- State reporting

    Provide network health data. In particular, it reports errors and problems when configuring its host.
    This data is written to the datastore so it is visible to other components and operators of the network.

### BIRD

BGP Internet Routing Daemon, or BIRD for short, gets routes from Felix and distributes to BGP peers on the network for inter-host routing. It runs on each node that hosts a Felix agent.

The BGP client is responsible for:

- Route distribution

    When Felix inserts routes into the Linux kernel FIB, the BGP client distributes them to other nodes in the deployment. This ensures efficient traffic routing for the deployment.

- BGP route reflector configuration

    BGP route reflectors are often configured for large deployments rather than a standard BGP client. BGP route reflectors acts as a central point for connecting BGP clients.
    (Standard BGP requires that every BGP client be connected to every other BGP client in a mesh topology, which is difficult to maintain.)

    For redundancy, you can seamlessly deploy multiple BGP route reflectors. BGP route reflectors are involved only in control of the network: no endpoint data passes through them.
    When the Calico BGP client advertises routes from its FIB to the route reflector, the route reflector advertises those routes out to the other nodes in the deployment.

### Confd

An open source tool for lightweight configuration management. Monitor Calico datastore for changes to BGP configuration and global defaults such as AS number, logging levels, and IPAM information.

Confd dynamically generates BIRD configuration files based on the updates to data in the datastore. When the configuration file changes, confd triggers BIRD to load the new files.

### Dikastes

Enforces network policy for Istio service mesh. Runs on a cluster as a sidecar proxy to Istio Envoy.

(Optional) Calico enforces network policy for workloads at both the Linux kernel (using iptables, L3-L4), and at L3-L7 using a Envoy sidecar proxy called Dikastes, with cryptographic authentication of requests. Using multiple enforcement points establishes the identity of the remote endpoint based on multiple criteria. The host Linux kernel enforcement protects your workloads even if the workload pod is compromised, and the Envoy proxy is bypassed.

### CNI plugin

Provides Calico networking for Kubernetes clusters.

The Calico binary that presents this API to Kubernetes is called the CNI plugin, and must be installed on every node in the Kubernetes cluster.
The Calico CNI plugin allows you to use Calico networking for any orchestrator that makes use of the CNI networking specification.

### Datastore plugin

Increases scale by reducing each node’s impact on the datastore. It is one of the Calico CNI plugins.

#### Kubernetes API datastore（kdd）

The advantages of using the Kubernetes API datastore (kdd) with Calico are:

- Simpler to manage because it does not require an extra datastore
- Use Kubernetes RBAC to control access to Calico resources
- Use Kubernetes audit logging to generate audit logs of changes to Calico resources

#### etcd

etcd is a consistent, highly-available distributed key-value store that provides data storage for the Calico network, and for communications between components.
etcd is supported for protecting only non-cluster hosts (as of Calico v3.1). For completeness, etcd advantages are:

- Let you run Calico on non-Kubernetes platforms
- Separate concerns between Kubernetes and Calico resources, such as allowing you to scale the datastores independently
- Let you run a Calico cluster that contains more than just a single Kubernetes cluster, for example, bare metal servers with Calico host protection interworking with a Kubernetes cluster; or multiple Kubernetes clusters.

### IPAM plugin

Use Calico’s IP pool resource to control how IP addresses are allocated to pods within the cluster.
It is the default plugin used by most Calico installations. It is one of the Calico CNI plugins.

### kube-controller

Monitor the Kubernetes API and performs actions based on cluster state.

The `tigera/kube-controllers` container includes the following controllers:

- Policy controller
- Namespace controller
- ServiceAccount controller
- WorkloadEndpoint controller
- Node controller

### Typha

Increase scale by reducing each node’s impact on the datastore. Run as a daemon between the datastore and instances of Felix. Installed by default, but not configured.

Typha maintains a single datastore connection on behalf of all of its clients like Felix and confd.
It caches the datastore state and deduplicates events so that they can be fanned out to many listeners.
Because one Typha instance can support hundreds of Felix instances, it reduces the load on the datastore by a large factor.
And because Typha can filter out updates that are not relevant to Felix, it also reduces Felix’s CPU usage.
In a high-scale (100+ node) Kubernetes cluster, this is essential because the number of updates generated by the API server scales with the number of nodes.

### Calicoctl

Calicoctl command line is available on any host with network access to the Calico datastore as either a binary or a container.

### Plugins for cloud orchestrators

Translate the orchestrator APIs for managing networks to the Calico data-model and datastore.

For cloud providers, Calico has a separate plugin for each major cloud orchestration platform.
This allows Calico to tightly bind to the orchestrator, so users can manage the Calico network using their orchestrator tools.
When required, the orchestrator plugin provides feedback from the Calico network to the orchestrator.
For example, providing information about Felix liveness, and marking specific endpoints as failed if network setup fails.
