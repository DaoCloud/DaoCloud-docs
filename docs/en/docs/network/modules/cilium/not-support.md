# Cilium Features Not Supported by Kubespray

This page describes the Cilium features that Kubespray does not support.

> Because [Cilium features](https://docs.cilium.io/en/stable/) are numerous, this page briefly
> introduces only a few of them.

## Egress Gateway

Cilium uses `CiliumEgressGatewayPolicy` to define which traffic leaving the cluster can specify the
corresponding node and the source IP for leaving the cluster.

> Note that Cilium does not maintain the egress source IP itself, and currently only IPv4 is supported.

Currently, Egress Gateway is not compatible with L7 policies. That is, when an Egress Gateway policy
and an L7 policy both match an endpoint, the Egress Gateway policy becomes invalid.

### Enable Egress Gateway

```yaml
enable-bpf-masquerade: true
enable-ipv4-egress-gateway: true
enable-l7-proxy: false
kube-proxy-replacement: strict
```

When installing Cilium with Kubean, you can configure it through `cilium_config_extra_vars`.
Refer to the [Egress Gateway documentation](https://docs.cilium.io/en/stable/network/egress-gateway/).

## Cluster Mesh

Cilium supports the Cluster Mesh feature, which connects multiple Cilium clusters together.
This feature enables connectivity between Pods in different clusters, and supports defining global
services and performing load balancing across multiple clusters.

> This feature cannot be enabled when the cluster is created; it must be enabled separately after
> the cluster is created.

### Set Up Cluster Mesh

#### Prerequisites

- The Cilium network mode of all clusters is the same, either tunnel mode or routing mode.
- Set the Cilium cluster name `--set cluster.name` and ID `--set cluster.id`, and make sure the
  cluster name and ID are unique. The ID ranges from 1 to 255. Because the ID is written into the
  identity, if you modify the cluster ID after the cluster is created (corresponding to
  `cluster-name` and `cluster-id` in the cm), you need to restart all Pods.
- The PodCIDR ranges of all clusters and all nodes do not conflict.
- The network between all cluster nodes must be reachable.
- Make sure the ports for inter-cluster communication are opened in the firewall.
- The Cilium CLI is installed in all clusters.
- All clusters need a context that can be used externally.
- Cluster names cannot contain uppercase letters; otherwise, the generated domain name is invalid.

If routing mode is used, the additional requirements are as follows:

- The `native-routing-cidr` of each cluster should include the Pod CIDR ranges of all clusters.
- Pods on all nodes and in all clusters must be able to communicate directly, including L3 and L4 connectivity.

#### Service Type to Select When Enabling

In some cases, the service type may not be automatically identified, and you need to manually specify
the type of clustermesh-apiserver. It can be specified as:

- LoadBalance: This mode is recommended. However, the premise is that the cluster supports LB;
  otherwise it stays pending, waiting for the allocation of EXTERNAL-IP.
- NodePort: This has a drawback. If the node used for access fails, you need to reconnect to another
  node, which may cause a network interruption. If all nodes fail, you need to reconnect to the cluster
  to obtain a new IP.
- ClusterIP: ClusterIP must be routable across clusters.

#### Enable clustermesh

- Enable clustermesh on the first cluster

    Use the `--create-ca` parameter to enable clustermesh on the first cluster and create the CA
    certificate for hubble-relay. Export the created Secret CA certificate to other clusters.

    ```shell
    # Enable clustermesh and create the CA certificate
    cilium clustermesh enable --create-ca --context x1 --service-type NodePort

    # Export the CA certificate
    kubectl -n kube-system secret cilium-ca -oyaml > cilium-ca.yaml

    # Import the CA in other clusters
    kubectl apply -f cilium-ca.yaml
    ```

- Enable clustermesh on other clusters

    ```shell
    # Specify the --service-type as needed
    cilium  clustermesh enable --context x2 --service-type NodePort
    ```

#### Connect Clusters

The operation of connecting to other clusters only needs to be performed on one cluster.

```sh
cilium  clustermesh connect --context x1 --destination-context x2
```

### Load Balancing and Service Discovery

Add annotations to the service to make it a global service that can be discovered or accessed by
other clusters. You can also specify whether the service of this cluster can be accessed by other
clusters and the load balancing mode of the service.

- io.cilium/global-service: "true/false": Defines the service as a global service that can be
  discovered by other clusters
- io.cilium/shared-service: "true/false": There is a global service with the same name, but when the
  value of the service in this cluster is set to false, it cannot be discovered or accessed by other clusters
- io.cilium/service-affinity: "none/local/remote/": The load balancing mode of the service. The default
  is `none`, which means load balancing across all clusters. `local` means preferring load balancing
  to the local cluster. `remote` means preferring load balancing to other clusters.

### Data Storage

When clustermesh is enabled, a clustermesh APIServer Pod is started for data synchronization between
clusters. An ETCD instance is also started for data storage. Run the following commands to view the data:

```sh
# Enter the clustermesh APIServer Pod and configure the ETCD certificates
alias etcdctl='etcdctl --cacert=/var/lib/etcd-secrets/ca.crt --cert=/var/lib/etcd-secrets/tls.crt --key=/var/lib/etcd-secrets/tls.key '

# Identity storage path
etcdctl get --prefix cilium/state/identities/v1

# Used IP storage path
etcdctl get --prefix cilium/state/ip/v1/<NS>

# Nodes
etcdctl get --prefix cilium/state/nodes/v1

# Services
etcdctl get --prefix cilium/state/services/v1/<clusterName>/<NS>
```

Refer to the [Cluster Mesh documentation](https://docs.cilium.io/en/stable/network/clustermesh/clustermesh/#gs-clustermesh).

## Service Mesh

Currently, Cilium does not support enabling Service Mesh directly by modifying certain parameters.
It can only be enabled through the Cilium CLI or Helm. Therefore, clusters installed with Kubean or
Kubespray cannot enable this feature by configuring parameters.

Refer to the [Service Mesh documentation](https://docs.cilium.io/en/stable/network/servicemesh/ingress/).

## Bandwidth Management

When Kubespray <= v2.20.0, this feature can only be enabled by setting the `enable-bandwidth-manager`
variable to true through `cilium_config_extra_vars`.
Later versions can enable it directly through `cilium_enable_bandwidth_manager`.

Refer to the [Bandwidth Manager documentation](https://docs.cilium.io/en/stable/network/kubernetes/bandwidth-manager/).

## Replace kube-proxy

Kubespray supports enabling this feature through the `cilium_kube_proxy_replacement` parameter.
However, related advanced features do not support parameter configuration. Cilium disables these
advanced features by default, and enabling them is complex. Some advanced features are briefly
described here.

> The parameters involved in the following advanced configurations are all Helm parameters.

### Maglev Consistent Hashing

Enable Maglev consistent hashing:

```shell
--set loadBalancer.algorithm=maglev   # Enable
```

For external traffic, a hash calculation is performed based on the 5-tuple to obtain the backend Pod
address. The result of the calculation is consistent for the same 5-tuple, so there is no need to
synchronize state between nodes. Note that this policy takes effect only for external traffic.
Because internal requests go directly to the backend, they are not restricted by Maglev. This policy
is also compatible with the Cilium XDP acceleration technology.

This algorithm has two adjustable parameters:

- maglev.tableSize: Specifies the size of the Maglev lookup table for each single service.
  Maglev recommends that the table size (M) be much larger than the expected maximum number of
  backends (N). In practice, this means M should be greater than 100*N to ensure that when backends
  change, the difference in redistribution is at most 1%.
  M must be a prime number. Cilium uses a default M size of 16381.
  The following M sizes are supported as the maglev.tableSize Helm option.
  Supported values are 251, 509, 1021, 2039, 4093, 8191, 16381, 32749, 65521, 131071.
- maglev.hashSeed: It is recommended to set the maglev.hashSeed option so that Cilium does not rely
  on a fixed built-in seed. The seed is a base64-encoded 12-byte random number, which can be generated
  once by running the following command:

    ```sh
    head -c12 /dev/urandom | base64 -w0
    ```

    Each Cilium agent in the cluster must use the same hash seed for Maglev to work.

    The specific configuration is as follows:

    ```sh
        --set maglev.tableSize=65521 \
        --set maglev.hashSeed=$SEED \
    ```

!!! note

    Compared with the default value of loadBalancer.algorithm=random, enabling Maglev results in
    higher memory consumption on each node managed by Cilium. This is because random does not need
    an additional lookup table. However, the backend selection of random is inconsistent.

### Direct Server Return (DSR)

Enable DSR mode:

```sh
    --set tunnel=disabled \
    --set autoDirectNodeRoutes=true \
    --set loadBalancer.mode=dsr \
```

For external traffic. It must run in routing mode and can preserve the source IP.
When traffic reaches the node of the LB or NodePort and is forwarded to the backend endpoint,
no SNAT is performed, and the reply traffic no longer passes through the LB or the node where the
traffic came in, but is returned directly to the client.
Therefore, this requires Pods to be routable to the external network, and Cilium cannot use tunnel mode.
As a result, one hop is saved when traffic returns, which has an acceleration effect and preserves the source IP.

Because a Pod can be used by multiple services, the returned service IP and port information must be
communicated to the endpoint. Cilium encodes this information in the Cilium-specific IPv4 option or
the IPv6 destination option extension header, at the cost of a smaller MTU value.
For TCP services, Cilium encodes the service IP/port only in SYN packets; subsequent data packets
do not carry this information. Therefore, the source/destination check must be disabled.

In addition, because the forward and return paths are inconsistent, asymmetric routing occurs,
and some iptables rules discard such traffic.

### Hybrid DSR and SNAT Mode

Configure hybrid mode:

```sh
    --set tunnel=disabled \
    --set autoDirectNodeRoutes=true \
    --set loadBalancer.mode=hybrid \
```

In hybrid mode, DSR is performed for TCP and SNAT is performed for UDP.
This avoids manually modifying the MTU and reduces the number of TCP hops.

`loadBalancer.mode` defaults to snat, and also supports the dsr and hybrid modes.

### XDP Acceleration

Enable XDP acceleration:

```sh
--set loadBalancer.acceleration=native \
```

Cilium can provide XDP acceleration support for NodePort, LoadBalancer, and externally accessible
services. XDP acceleration requires underlying driver support.
This feature supports the DSR, SNAT, and Hybrid modes of load balancing. Because the XDP acceleration
stage is very early, tcpdump cannot capture the packets.

> This feature can be used only when the NIC driver supports XDP.
> If Cilium automatically detects that multiple NICs are used to expose NodePort, or multiple devices
> are specified, all NIC drivers must support XDP.

View the driver used by a device:

```sh
$ethtool -i eth0 | grep driver
driver: vmxnet3     # NIC driver
```

For the list of currently supported drivers, see
[LoadBalancer & NodePort XDP Acceleration](https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/#loadbalancer-nodeport-xdp-acceleration).

### Bypass Socket LoadBalancer in the Pod Namespace

Configuration for bypassing Socket LB in a kube-proxy-free environment:

```sh
    --set tunnel=disabled \
    --set autoDirectNodeRoutes=true \
    --set socketLB.hostNamespaceOnly=true
```

By default, Cilium accesses the service IP in a Pod, so backend election is performed in the Pod and
the connection is made directly to the backend address.
The application layer still sees the service IP being connected, but the underlying connection is
actually to the corresponding backend address.
If you need to rely on the service IP for load balancing, this feature becomes invalid. You can
disable it through the configuration above.

### Enable Topology Aware Hints

Enable Topology Aware Hints:

```sh
    --set loadBalancer.serviceTopology=true \
```

Cilium kube-proxy also implements the Kubernetes service Topology Aware Hints feature, which makes
requests prefer backend endpoints in the same zone.

### Neighbor Discovery

Starting from Cilium 1.11, the neighbor discovery library has been removed, and neighbor discovery
relies entirely on the Linux kernel.
In kernel 5.16 and later, it is implemented through the "managed" feature, and ARP records are marked
with "extern_learn" to prevent them from being garbage collected by the kernel.
For earlier kernel versions, cilium-agent periodically writes the IP addresses of new nodes into the
Linux kernel for dynamic resolution.
The default is 30s, which can be set through the following parameter:

```sh
    --set --arping-refresh-period=30s \
```

### External Access to ClusterIP

Allow external access to ClusterIP services:

```sh
    --set bpf.lbExternalClusterIP=true  \
```

By default, Cilium does not allow external access to ClusterIP services. It can be enabled through
`bpf.lbExternalClusterIP=true`. However, you need to set up the related routes yourself.

For more information, see [Advanced configuration for replacing kube-proxy](https://docs.cilium.io/en/stable/network/kubernetes/kubeproxy-free/#kubeproxy-free).
