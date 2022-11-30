# Kubespray 未支持的 Cilium 功能说明

本页说明 Kubespray 不支持的 Cilium 功能。由于 [Cilium 功能繁多](https://docs.cilium.io/en/stable/)，全部枚举比较冗长，本页简要介绍几个功能特性。

## Egress Gateway

Cilium 通过 `CiliumEgressGatewayPolicy` 来定义哪些流量离开集群时可以指定相应的节点以及出集群的源 IP。
需要注意的是，Cilium 并不自行维护出口的源 IP。而且当前只支持 IPv4。

当前 Egress Gateway 与 L7 策略并不兼容，当 Egress Gateway 的策略与 L7 策略同时命中一个端点时，Egress Gateway 策略将失效。

### 开启条件

```yaml
enable-bpf-masquerade: true
enable-ipv4-egress-gateway: true
enable-l7-proxy: false
kube-proxy-replacement: strict
```

使用 Kubean 安装 Cilium 时，可以通过 “cilium_config_extra_vars” 进行配置。参阅 [Egress Gateway 文档](https://docs.cilium.io/en/stable/gettingstarted/egress-gateway/)。

## Cluster Mesh

Cilium 支持 Cluster Mesh 功能，可以将多个 Cilium 集群连接在一起。
打通各个集群中 Pod 的连通性，还可以定义全局 SVC，可在多个集群之间进行负载均衡。
该功能并不能在创建集群时开启，需在完成集群创建后单独开启。

### 开启前置条件

- 所有集群的 Cilium 网络模式一样，都是隧道模式或者路由模式
- 设置 Cilium 集群名称及 ID。
  `--set cluster.name`、`--set cluster.id` 且集群名称与 ID 是唯一的，ID 范围在（1-255）。如果创建集群后修改集群 ID (cm 中对应为 cluster-name、cluster-id )，则需要重启所有的 Pod，这是因为 ID 会写入身份中
- 所有集群的所有节点及 PodCIDR 范围不冲突
- 所有集群中节点之间的网络必须是连通的
- 集群之间的通信，相关的端口都要放开，不要被防火墙禁了
- 所有集群都安装了 Cilium CLI
- 所有集群都需要准备一个能够被外部使用的 context
- 集群名称不能使用大写，否则生成的域名会认为是非法的

如果使用路由模式，额外的要求如下：

-  任何集群的 native-routing-cidr 都应该包含所有的集群 Pod CIDR 的范围
-  除了节点之间外，所有集群之间的 Pod 必须能直接通信，其中包括了三层、四层是通的

### 关于开启时需要选择服务类型

在某些情况下，可能无法自动识别 SVC 类型，需要手动指定 clustermesh-apiserver 的类型，可以指定为：

- LoadBalance：前提是集群能支持 LB，否则会一直 pending，等待 EXTERNAL-IP 的分配。推荐使用该模式。
- NodePort：存在一个弊端，如果用于访问的节点挂了，则需要重新连接到另外一个节点，这可能会造成网络中断。如果所有节点都挂了，则需要重新连接集群以提取新 IP。
- ClusterIP：需要 ClusterIP 能跨集群路由。

### 开启 clustermesh

在第一个集群开启 clustermesh，使用 `--create-ca` 参数同时创建 ca 证书，用于 hubble-rely。将创建好的 Secret ca 证书导出到其他集群。

```shell
# 开启 clustermesh，同时创建 ca 证书
cilium clustermesh enable --create-ca --context x1 --service-type NodePort

# 导出 ca 证书
kubectl -n kube-system secret cilium-ca -oyaml > cilium-ca.yaml

# 在其他集群导入 ca
kubectl apply -f cilium-ca.yaml
```

### 在其他集群开启 clustermesh

```shell
# 根据需要指定 --service-type 类型
cilium  clustermesh enable --context x2 --service-type NodePort
```

### 连接集群

只要在一个集群中执行连接其他集群即可。

```sh
cilium  clustermesh connect --context x1 --destination-context x2
```

### 使用方式

在 SVC 中添加注解，让其成为全局的 SVC，可在其他集群发现或访问。同时还可指定本集群的服务能否被其他集群访问及负载均衡方式。

- io.cilium/global-service: "true/false"：将 SVC 定义为全局的 SVC，可在其他集群发现
- io.cilium/shared-service: "true/false"： 当有一个同名的 Global 的 SVC，但将本集群的 SVC 值设置为 false，则其他集群不可发现与访问
- io.cilium/service-affinity: "none/local/remote/"：SVC 负载均衡的方式。默认为 `none`，表示在所有集群中负载均衡。`local `表示优先负载均衡到本地集群。`remote` 表示优先负载均衡到其他集群。

### 数据存储

开启 clustermesh 时，会启动一个 clustermesh APIServer 的 Pod，用于集群间数据同步。同时还会启动一个 ETCD 用于数据存储。参照以下命令查看数据：

```sh
# 进入 clustermesh APIServer Pod，配置 ETCD 相关相关证书
alias etcdctl='etcdctl --cacert=/var/lib/etcd-secrets/ca.crt --cert=/var/lib/etcd-secrets/tls.crt --key=/var/lib/etcd-secrets/tls.key '

# 身份存储路径
etcdctl get --prefix cilium/state/identities/v1

# 已使用IP存储路径
etcdctl get --prefix cilium/state/ip/v1/<NS>

# 节点
etcdctl get --prefix cilium/state/nodes/v1

# SVC 
etcdctl get --prefix cilium/state/services/v1/<clusterName>/<NS>
```

请参阅 [Cluster Mesh 文档](https://docs.cilium.io/en/stable/gettingstarted/clustermesh/clustermesh/)。

## Service Mesh

当前 Cilium 并不支持直接通过修改某些参数的方式来直接开启 Service Mesh 功能。
只支持 Cilium CLI 或 Helm 的方式来开启。所以使用 Kubean 或 Kubespray 安装的集群，无法通过配置参数的方式来启用该功能。

请参阅 [Service Mesh 文档](https://docs.cilium.io/en/stable/gettingstarted/servicemesh/ingress/)。

## 带宽管理

当 Kubespray <= v2.20.0 时，只能使用 “cilium_config_extra_vars” 方式将 “enable-bandwidth-manager” 变量设置为 true 来开启。
之后的版本可通过 "cilium_enable_bandwidth_manager" 直接开启。

请参阅 [Bandwidth Manager 文档](https://docs.cilium.io/en/stable/gettingstarted/bandwidth-manager/)。

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

### clusterIP 对外可访问

```sh
    --set bpf.lbExternalClusterIP=true  \
```

Cilium 默认情况下不允许外部访问 ClusterIP SVC。可以通过 bpf.lbExternalClusterIP=true 启用。但需要自行打通相关的路由。

请参阅[替换 kube-proxy 高级配置](https://docs.cilium.io/en/stable/gettingstarted/kubeproxy-free/)。
