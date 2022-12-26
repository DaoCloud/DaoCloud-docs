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

## 替换 kube-proxy

Kubespray 支持使用参数 “cilium_kube_proxy_replacement” 启用该功能。
但是相关的高级功能并不支持参数配置。这些高级功能 Cilium 默认基本都是关闭的，开启方式也并不简单。这里对部分高级功能做一个简述。

### Maglev 哈希一致性

关于后续高级配置涉及到的参数，均为 Helm 参数。

```shell
--set loadBalancer.algorithm=maglev   # 开启
```

针对外部流量，根据五元组做哈希计算得到后端 Pod 地址，相同的五元组计算的结果都是一致的，所以不需要在各节点之间同步状态。
需要注意的是该策略只对外部流量生效，由于内部请求直接到后端，所以不受 Maglev 限制。而且也可以兼容配合使用 Cilium 的 XDP 加速技术。

该算法有两个参数可调整：

- maglev.tableSize：指定每个单一服务的 Maglev 查询表的大小。
  Maglev 建议表的大小（M）要远远大于预期的最大后端数量（N）。
  在实践中，这意味着 M 应该大于 100*N，以保证在后端变化时，重新分配的差异最多只有 1%。
  M 必须是一个素数。Cilium 使用默认的 M 大小为 16381。
  以下的 M 大小作为 maglev.tableSize Helm 选项被支持。
  支持的值有 251、509、1021、2039、4093、8191、16381、32749、65521、131071
- maglev.hashSeed：建议设置 maglev.hashSeed 选项，以使 Cilium 不依赖固定的内置种子。
  种子是一个 base64 编码的 12 字节的随机数。可运行以下命令

    ```sh
    head -c12 /dev/urandom | base64 -w0
    ```

    生成一次。集群中的每个 Cilium 代理必须使用相同的哈希种子，以使 Maglev 工作。

    具体设置方式为：

    ```sh
        --set maglev.tableSize=65521 \
        --set maglev.hashSeed=$SEED \
    ```

!!! note

    与 loadBalancer.algorithm=random 的默认值相比，启用 Maglev 将在每个 Cilium 管理的节点上有更高的内存消耗，因为随机不需要额外的查询表。
    然而，随机不会有一致的后端选择。

### 直接 SVC 返回 (DSR)

```sh
    --set tunnel=disabled \ 
    --set autoDirectNodeRoutes=true \ 
    --set loadBalancer.mode=dsr \ 
```

也是针对外部流量。必须运行在路由模式，同样可以保留源 IP。
当流量到达 LB 或者 NodePort 的节点时，转给后端 EP 时不做 SNAT，应答流量也不再经过 LB 或者流量进来的节点，而是直接返回给客户端。
所以需要 Pod 能够与外部路由是通的，Cilium 不能使用隧道模式。这样的话流量返回时就少了一跳起到了加速的作用，而且保留了源 IP。

由于一个 Pod 可以被多个 SVC 使用，所以返回的 SVC IP 及端口信息需告知 EP。
Cilium 将此信息编码在 Cilium 特定的 IPv4 选项或 IPv6 目标选项扩展标头中，代价是宣告一个较低的 MTU。
对于 TCP 服务，Cilium 只对 SYN 数据包的 SVC IP/端口进行编码，后续的数据包头中并不会携带这些信息。

所以要关闭源/目的检测功能。由于来去的路径不一致，所以会出现路由不对称的现象，所以有一些 iptables 规则会将这些流量丢弃。

### 混合 DSR 和 SNAT 模式

```sh
    --set tunnel=disabled \
    --set autoDirectNodeRoutes=true \
    --set loadBalancer.mode=hybrid \
```

在混合模式中，对 TCP 执行 DSR，对 UDP 执行 SNAT。
这样可以避免手动修改 MTU，又可以减少 TCP 的跳数。

loadBalancer.mode 默认为 snat，还可以支持 dsr、hybrid 模式。

### XDP 加速

```sh
--set loadBalancer.acceleration=native \
```

Cilium 可以对 NodePort、loadBalancer 及对外可访问的 SVC 都提供 XDP 加速的支持。XDP 加速需要底层驱动支持。
该功能支持 loadBalance 的 DSR、SNAT 及 Hybrid 模式。由于 XDP 加速阶段很早，所以使用 tcpdump 抓不到包。

需要注意只有网卡驱动支持 XDP 时，该功能才能使用。
如果 Cilium 自动检测使用多个网卡来暴露 NodePort，或者指定了多个 device，则所有的网卡驱动都要支持。

```sh
$ethtool -i eth0 | grep driver
driver: vmxnet3     # 网卡驱动
```

当前支持的驱动列表查看官网介绍：https://docs.cilium.io/en/stable/gettingstarted/kubeproxy-free/

### 在 Pod 命名空间中绕过 Socket LoadBalancer

```sh
    --set tunnel=disabled \
    --set autoDirectNodeRoutes=true \
    --set socketLB.hostNamespaceOnly=true
```

Cilium 默认在 Pod 中访问的是 SVC IP，则在 Pod 中就会做后端选举，直接连接到后端地址。
应用层看到的还是连接的 SVC IP，但是底层其实是对应的后端地址。
如果有些需要依赖 SVC IP 做负载时，则会失效。上面的选项可以将该功能关闭。

### 开启拓扑感知提示

```sh
    --set loadBalancer.serviceTopology=true \
```

Cilium kube-proxy 也实现了 K8s 服务 Topology Aware Hints 功能，可以让请求更偏向于同一区域的后端端点。

### 邻居发现

```sh
    --set --arping-refresh-period=30s \
```

Cilium 1.11 版本后，已经将邻居发现的库删除，完全依赖于 Linux 内核。
在 5.16 及以上版本的内核中，通过 “managed” 功能来实现，并用 “extern_learn” 来标记 arp 记录，以防被内核垃圾回收。
对于低版本的内核，通过 cilium-agent 定期将新节点的 IP 地址写入 Linux 内核中以进行动态解析。
默认是 30s，可通过上述参数进行设置。

### ClusterIP 对外可访问

```sh
    --set bpf.lbExternalClusterIP=true  \
```

Cilium 默认情况下不允许外部访问 ClusterIP SVC。可以通过 bpf.lbExternalClusterIP=true 启用。但需要自行打通相关的路由。

请参阅[替换 kube-proxy 高级配置](https://docs.cilium.io/en/stable/gettingstarted/kubeproxy-free/)。

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
