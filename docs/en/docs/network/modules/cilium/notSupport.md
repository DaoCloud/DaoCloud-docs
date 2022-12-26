---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: NA
Date: 2022-12-26
---

# Cilium features not supported by Kubespray

This page describes the Cilium features that are not supported by Kubespray.

> Due to the large number of [Cilium features](https://docs.cilium.io/en/stable/), only a few features are briefly described on this page.

## Egress Gateway

Cilium uses `CiliumEgressGatewayPolicy` to define which traffic leaves the cluster with the appropriate node and source IP out of the cluster.

> Note that Cilium does not maintain its own source IPs for egress, and currently only supports IPv4.

The current Egress Gateway is not compatible with L7 policies. That is, when an Egress Gateway policy hits an endpoint at the same time as an L7 policy, the Egress Gateway policy will fail.

### Enabling Egress Gateway

```yaml
enable-bpf-masquerade: true
enable-ipv4-egress-gateway: true
enable-l7-proxy: false
kube-proxy-replacement: strict
```

When installing Cilium with Kubean, you can configure it with "cilium_config_extra_vars". See the [Egress Gateway documentation](https://docs.cilium.io/en/stable/gettingstarted/egress-gateway/).

## Cluster Mesh

Cilium supports the Cluster Mesh feature, which allows multiple Cilium clusters to be connected together.
This feature opens up the connectivity of Pods in each cluster and supports defining global SVCs for load balancing across multiple clusters.

> This feature is not supported when creating a cluster, but must be enabled separately after the cluster is created.

### Set up Cluster Mesh

#### Prerequisites to enable Cluster Mesh

- All clusters have the same Cilium network mode, either tunneling or routing mode.
- Set the Cilium cluster name `--set cluster.name` and ID `--set cluster.id`, and the cluster name and ID are unique, with IDs in the range 1-255. Since IDs are written to the identity, if you change the cluster ID (corresponding to cluster-name, cluster-id in cm) after creating the cluster, you need to restart all Pods.
- PodCIDR ranges for all clusters and all nodes do not conflict
- The network between all cluster nodes must be connected
- Ensure that the relevant ports for inter-cluster communication are opened in the firewall
- All clusters have the Cilium CLI installed
- All clusters need to have a context that can be used externally
- Cluster names cannot be in upper case, otherwise the generated domain name will be illegal

If using routing mode, additional requirements are as follows:

- The native-routing-cidr for each cluster should include the full range of Pod CIDRs for all clusters
- All nodes and Pods between clusters must be able to communicate directly, including Layer 3 and Layer 4 connectivity.

#### Service type to be selected for boot up

In some cases, the SVC type may not be recognized automatically and the type of clustermesh-apiserver needs to be specified manually, which can be specified as

- LoadBalance: It is recommended to use this mode. But only if the cluster can support LB, otherwise it will always be pending, waiting for the assignment of EXTERNAL-IP.
- NodePort: There is a disadvantage that if the node used for access fails, it needs to reconnect to another node, which may cause a network outage. If all nodes fail, the cluster needs to be reconnected to extract the new IP.
- ClusterIP: Requires ClusterIP to be able to route across the cluster.

#### Enable clustermesh

- Enable clustermesh in the first cluster

    Use the `-create-ca` parameter to enable clustermesh in the first cluster, and create ca certificates for hubble-rely. export the created Secret ca certificates to other clusters.

    ```shell
    # Enable clustermesh and create ca certificates
    cilium clustermesh enable --create-ca --context x1 --service-type NodePort

    # Export the ca certificate
    kubectl -n kube-system secret cilium-ca -oyaml > cilium-ca.yaml

    # Import ca in other clusters
    kubectl apply -f cilium-ca.yaml
    ```

- Enable clustermesh in other clusters

    ```shell
    # Specify the --service-type type as needed
    cilium clustermesh enable --context x2 --service-type NodePort
    ```

#### Connecting to a cluster

Only need to perform connections to other clusters in one cluster.

```sh
cilium clustermesh connect --context x1 --destination-context x2
```

### Load balancing and service discovery

Add annotations to the SVC to make it a global SVC that can be discovered or accessed by other clusters. And specify whether services from this cluster can be accessed by other clusters and how the services are load balanced.

- io.cilium/global-service: "true/false": defines the SVC as a global SVC that can be discovered by other clusters
- io.cilium/shared-service: "true/false": there is a global SVC with the same name. But if the SVC value for this cluster is set to false, it cannot be discovered or accessed by other clusters
- io.cilium/service-affinity: `none/local/remote/`: The way the SVC is load balanced. Default is `none`, which means load balancing across all clusters. `local` indicates priority load balancing to local clusters. `remote` indicates priority load balancing to other clusters.

### Data storage

When clustermesh is started, a pod of clustermesh APIServer is started for inter-cluster data synchronization. An ETCD will also be started for data storage. Refer to the following command to view the data:

```sh
# Enter the clustermesh APIServer Pod and configure the ETCD related certificates
alias etcdctl='etcdctl --cacert=/var/lib/etcd-secrets/ca.crt --cert=/var/lib/etcd-secrets/tls.crt --key=/var/lib/etcd-secrets/tls.key '

# Identity storage path
etcdctl get --prefix cilium/state/identities/v1

# Used IP storage paths
etcdctl get --prefix cilium/state/ip/v1/<NS>

# Nodes
etcdctl get --prefix cilium/state/nodes/v1

# SVC 
etcdctl get --prefix cilium/state/services/v1/<clusterName>/<NS>
```

See the [Cluster Mesh documentation](https://docs.cilium.io/en/stable/gettingstarted/clustermesh/clustermesh/).

## Service Mesh

Currently Cilium does not support directly enabling Service Mesh by modifying certain parameters.
It can only be enabled via the Cilium CLI or Helm. Therefore, clusters installed with Kubean or Kubespray cannot be enabled by configuring parameters.

See the [Service Mesh documentation](https://docs.cilium.io/en/stable/gettingstarted/servicemesh/ingress/).

## Bandwidth Management

When Kubespray <= v2.20.0, it can only be enabled by setting the "enable-bandwidth-manager" variable to true using the "cilium_config_extra_vars" method.
Later versions can be enabled directly by "cilium_enable_bandwidth_manager".

See [Bandwidth Manager documentation](https://docs.cilium.io/en/stable/gettingstarted/bandwidth-manager/).

## Replace kube-proxy

Kubespray supports enabling this feature with the parameter "cilium_kube_proxy_replacement".
Cilium disables these advanced features by default, and enables them in a more complex way. Here is a brief description of some of the advanced features.

> The parameters involved in the subsequent advanced configuration are Helm parameters.

### Maglev hash consistency

To enable Maglev hash consistency:

```shell
--set loadBalancer.algorithm=maglev # Enables
```

Maglev hash consistency is targeted for external traffic. Do hash calculations based on the quintet to get the back-end Pod address. The results of the same quintet calculations are consistent, so there is no need to synchronize the state between nodes.
Note that this policy only works for external traffic, and is not restricted by Maglev since internal requests go directly to the backend. The policy is also compatible with Cilium's XDP acceleration technology.

The algorithm has two tunable parameters:

- maglev.tableSize: specifies the size of the Maglev query table for each single service.
  Maglev recommends that the table size (M) be much larger than the expected maximum number of backends (N).
  In practice, this means that M should be larger than 100*N to ensure that the difference in redistribution is at most 1% when the backend changes.
  M must be a prime number. cilium uses a default M size of 16381.
  The following M sizes are supported as maglev.tableSize Helm options.
  The supported values are 251, 509, 1021, 2039, 4093, 8191, 16381, 32749, 65521, 131071
- maglev.hashSeed: It is recommended to set the maglev.hashSeed option to induce Cilium not to rely on a fixed built-in seed.
  The seed is a base64-encoded 12-byte random number that can be generated once by running the following command:

    ```sh
    head -c12 /dev/urandom | base64 -w0
    ```

    Each Cilium agent in the cluster must use the same hash seed for Maglev to work.

    Set the maglev table size:

    ```sh
        --set maglev.tableSize=65521 \
        --set maglev.hashSeed=$SEED \
    ```

!!! note

    Enable Maglev will result in higher memory consumption on each node managed by Cilium compared to the default value of loadBalancer.algorithm=random. This is because random does not require an additional lookup table, however, the random backend selection is inconsistent.

### Direct SVC Return (DSR)

To enable DSR mode.

```sh
    --set tunnel=disabled \ 
    --set autoDirectNodeRoutes=true \ 
    --set loadBalancer.mode=dsr \ 
```

DSR is targeted for external traffic. It must be running in routed mode and can retain the source IP.
When traffic reaches the LB or the node of the NodePort, it is forwarded to the back-end EP without SNAT and the answering traffic no longer passes through the LB or the node where the traffic came in, but is returned directly to the client.
So this requires the Pod to be able to connect to external routes, and Cilium cannot use tunnel mode. As a result, the traffic returns with one less hop, which acts as a speedup, and the source IP is preserved.

Since a Pod can be used by multiple SVCs, the returned SVC IP and port information needs to be communicated to the EP.
Cilium encodes this information in a Cilium-specific IPv4 option or IPv6 target option extension header, at the cost of a smaller MTU value.
For TCP services, Cilium encodes only the SVC IP/port of the SYN packet, and subsequent data headers do not carry this information. So turn off source/destination detection.

In addition, routing asymmetry can occur because of inconsistent paths to and from, and there are iptables rules that discard this traffic.

### Hybrid DSR and SNAT mode

To configure the hybrid mode:

```sh
    --set tunnel=disabled \
    --set autoDirectNodeRoutes=true \
    --set loadBalancer.mode=hybrid \
```

In the hybrid mode, DSR is performed for TCP and SNAT for UDP.
This avoids manual modification of MTU and reduces the number of TCP hops.

loadBalancer.mode defaults to snat, and also supports DSR and the hybrid mode.

### XDP acceleration

To enable XDP acceleration:

```sh
--set loadBalancer.acceleration=native \
```

Cilium can provide XDP acceleration support for NodePort, loadBalancer and externally accessible SVCs.
This feature supports DSR, SNAT and Hybrid modes of loadBalance. Due to the early stage of XDP acceleration, packets are not captured using tcpdump.

> This feature is only available if the NIC driver supports XDP.
If Cilium automatically detects that multiple NICs are used to expose NodePort, or if multiple devices are specified, all NIC drivers should support XDP.

View the drivers used by a device:

```sh
$ethtool -i eth0 | grep driver
driver: vmxnet3 # NIC driver
```

A list of currently supported drivers can be found at [LoadBalancer & NodePort XDP Acceleration](https://docs.cilium.io/en/stable/gettingstarted/kubeproxy-free/#loadbalancer-nodeport-xdp-acceleration).

### Bypass Socket LoadBalancer in Pod namespace

Configuration for bypassing the Socket LB in a kube-proxy-free environment:

```sh
    --set tunnel=disabled \
    --set autoDirectNodeRoutes=true \
    --set socketLB.hostNamespaceOnly=true
```

Cilium accesses the SVC IP by default in the Pod, so it does a backend election in the Pod and connects directly to the backend address.
The application layer still sees the connected SVC IP, but the underlying layer is actually the corresponding backend address.
If you need to rely on the SVC IP for load, this feature will fail and can be turned off with the above configuration.

### Enable topology-aware hints

To enable topology-aware hints.

```sh
    --set loadBalancer.serviceTopology=true \
```

Cilium kube-proxy also implements the K8s Service Topology Aware Hints feature, which allows requests to be more biased towards back-end endpoints in the same region.

### Neighbor Discovery

With Cilium version 1.11, the neighbor discovery library has been removed and relies entirely on the Linux kernel to implement neighbor discovery.
In kernels 5.16 and above, this is done with the "managed" function and with "extern_learn" to mark arp records in case they are garbage collected by the kernel.
For lower kernel versions, the IP address of the new node is periodically written to the Linux kernel via the cilium-agent for dynamic resolution.
The default is 30s, which can be set with the following parameters:

```sh
    --set --arping-refresh-period=30s \
```

### External access to clusterIP

Allows external access to the ClusterIP Service:

```sh
    --set bpf.lbExternalClusterIP=true \
```

Cilium does not allow external access to ClusterIP SVC by default, you can enable it with bpf.lbExternalClusterIP=true. However, you need to break the relevant routes yourself.

See [Replacing kube-proxy advanced configuration](https://docs.cilium.io/en/stable/gettingstarted/kubeproxy-free/) for more details.
