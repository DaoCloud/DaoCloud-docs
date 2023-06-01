# L2&BGP 模式说明

## MetalLB L2 模式

L2 模式下，`Metallb` 将会通过 ARP（for ipv4）、NDP（for ipv6）宣告 `LoadBalancerIP` 的地址。
在 `Metallb` < `v0.13.2` 之前，只能通过 `configMap` 来配置 `Metallb`。
在 `v0.13.2` 之后，通过 CRD 资源的方式配置 `Metallb`，另外 `configMap` 的方式已被弃用。

在 `Layer2` 模式下，当创建服务时，`Metallb`（`speaker` 组件）会为这个服务选举出集群中某个节点，作为这个服务对外暴露的主机。
当对 Service 的 `externalIP` 发出请求时，此节点会代替这个 `externalIP` 回复 `arp` 请求。
所以对 Service 发出的请求，会首先到达集群中这个节点，然后再经过这个节点上的 `kube-proxy` 组件，最后将流量导向这个 service 某个具体的端点 (endpoint)。

服务选举节点的逻辑主要有三点：

1. 首先过滤掉未 ready 的节点以及 endpoint 未 ready 所在的节点
2. 如果该服务的 endpoint 分布在同一个节点，那么筛选此节点作为该服务 IP 的 `arp` 响应者
3. 如果该服务的 endpoint 分布在不同的节点，那么通过 `sha256` 计算 `节点 + # + externalIP` 后，按照字典顺序取第一个

这样，MetalLB 就会为每个 Service 选择一个节点作为暴露的主机。
`metallb` 会将这单个 Service 的流量，全部导向某个节点，所以这个节点可能会成为限制性能的瓶颈。
Service 的带宽限制也会取决于单个节点的带宽，这也是使用 ARP 或 NDP 最主要的限制。

此外，当此节点发生故障时，MetalLB 需要为服务重新选择一个新的节点。
然后 `Metallb` 会给客户端发送一个"免费"的 `arp`，告知客户端需要更新他们的 Mac 地址缓存。
在客户端更新缓存前，流量仍会转发到故障节点。因此从某种程度来看：故障转移的时间，依赖于客户端更新 Mac 地址缓存的速度。

### 使用

- 创建 IP 池

    ```yaml
    apiVersion: metallb.io/v1beta1
    kind: IPAddressPool
    metadata:
      name: demo-pool
      namespace: metallb-system
      labels:
        ipaddresspool: demo
    spec:
      addresses:
      - 192.168.10.0/24
      - 192.168.9.1-192.168.9.5
      - fc00:f853:0ccd:e799::/124
      autoAssign: true
      avoidBuggyIPs: false
    ```

- `addresses`：IP 地址列表，每一个列表成员可以是一个 CIDR，可以是一个地址范围（如 192.168.9.1 - 192.168.9.5），也可以是不同 `ipFamily`、`Metallb` 会从其中分配 IP 给 `LoadBalancer` 服务

- `autoAssign`：是否自动分配 IP 地址，默认为 true。在某些情况下（IP 地址不足或公有 IP），不希望池中的 IP 被轻易地分配，可设置为 false。
  可以通过在 service 中设置 annotations: `metallb.universe.tf/address-pool: pool-name`。或者在 `spec.LoadBalancerIP` 字段设置 IP（注意这种方式已被k8s标记为遗弃）。

- `avoidBuggyIPs`：是否避免使用池中以 `.0` 或 `.255` 地址，默认为 false。

- 配置 `LoadBalancerIP` 通告规则 (L2)

    通过 `L2Advertisement` 绑定地址池，这样告诉 `Metallb` 这些地址应该由 `ARP` 或 `NDP` 通告出去。

    ```yaml
    apiVersion: metallb.io/v1beta1
    kind: L2Advertisement
    metadata:
      name: demo
      namespace: metallb-system  
    spec:
      ipAddressPools:
      - demo-pool
      ipAddressPoolSelectors:
      - matchLabels:
          ipaddresspool: demo
      nodeSelectors:
      - matchLabels:
          kubernetes.io/hostname: kind-control-plane
    ```

- `ipAddressPools`：可选，通过 name 筛选地址池，如 `ipAddressPools` 和 `ipAddressPoolSelectors` 同时未指定，则作用于所有地址池。

- `ipAddressPoolSelectors`：可选，通过 labels 筛选地址池，如 `ipAddressPools` 和 `ipAddressPoolSelectors` 同时未指定，则作用于所有地址池。

- `nodeSelectors`：可选，用于筛选哪些节点作为 `loadBalancerIP` 的下一跳，默认所有节点。

- 创建`LoadBalancer Service`

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: metallb1-cluster
      labels:
        name: metallb
          #annotations:
          #metallb.universe.tf/address-pool: lan
    spec:
      type: LoadBalancer
      allocateLoadBalancerNodePorts: false
      ports:
      - port: 18081
        targetPort: 8080
        protocol: TCP
      selector:
        app: metallb-cluster
    ```

    只需要指定 `spec.type=LoadBalancer`，这样 `Metallb` 就会自然接管此 `Service` 的生命周期。

    !!! note

        如果想让 Service 从指定的地址池中分配地址，通过 `annotations: metallb.universe.tf/address-pool: <pool-name>` 指定。或者通过 `service.spec.loadBalancerIP` 字段指定 IP（需要保证存在于一个池中，不推荐这种方式）。
        如果存在多种负载均衡器，可通过 `service.spec.loadBalancerClass` 字段指定。在部署 `Metallb` 时，可通过 `--lb-class` flag 进行配置。

### 负载均衡性

- 当 `Service.spec.externalTrafficPolicy=cluster`

    这种模式下，具有良好的负载均衡性，但流量可能经历多跳，这会隐藏客户端源 IP。

    ```none
                                      ______________________________________________________________________________
                                    |                       -> kube-proxy(SNAT) -> pod A                          |
                                    |                      |                                                      |
    client -> loadBalancerIP:port -> | -> node A（Leader） ->                                                       |
                                    |                      |                                                      ｜
                                    |                       -> kube-proxy(SNAT) -> node B -> kube-proxy -> pod B  ｜
                                      ------------------------------------------------------------------------------
    ```

- 当 `Service.spec.externalTrafficPolicy=local`

    这种模式下，会保留客户端源IP，但负载均衡性较差，流量会一直到某一个后端Pod。

    ```none
                                      __________________________________________________________________________________________
                                    |                       -> kube-proxy -> pod A (后端Pod在本节点)                            |
                                    |                      |                                                                  |
    client -> loadBalancerIP:port -> | -> node A（Leader） ->                                                                   |
                                    |                      |                                                                  ｜
                                    |                       -> kube-proxy -> node B -> kube-proxy -> pod B (后端Pod在不同节点)  ｜
                                      ------------------------------------------------------------------------——————————————————
    ```

## MetalLB BGP 模式(L3)

`Layer2` 模式局限在一个二层网络中，流向 Service 的流量都会先转发到某一个特定的节点，这并不算真正意义上的负载均衡。
BGP 模式不局限于一个二层网络，集群中每个节点都会跟 BGP Router 建立 BGP 会话，宣告 Service 的 `ExternalIP` 的下一跳为集群节点本身。
这样外部流量就可以通过 BGP Router 接入到集群内部，BGP Router 每次接收到目的是 `LoadBalancer` IP 地址的新流量时，它都会创建一个到节点的新连接。
但选择哪一个节点，每个路由器厂商都有一个特定的算法来实现。所以从这个角度来看，这具有良好的负载均衡性。

### 使用

- 创建 IP 池

    ```yaml
    apiVersion: metallb.io/v1beta1
    kind: IPAddressPool
    metadata:
      name: bgp-pool
      namespace: metallb-system
      labels:
        ipaddresspool: demo
    spec:
      addresses:
      - 192.168.10.0/24
      autoAssign: true
      avoidBuggyIPs: false
    ```

- 配置 `LoadBalancerIP` 通告规则 (L3)

    !!! note

        BGP 模式需要硬件支持运行 BGP 协议。若无，可使用如 `frr`、`bird` 等软件代替。

    推荐使用 `frr` 进行安装:

    ```shell
    # ubuntu
    apt install frr
    # centos
    yum install frr
    ```

    `frr` 配置 `BGP`：

    ```shell
    router bgp 7675  # bgp as number
    bgp router-id 172.16.1.1  # route-id 常常是接口IP
    no bgp ebgp-requires-policy # 关闭 ebpf filter !!!
    neighbor 172.16.1.11 remote-as 7776  # 配置 ebgp -> neighbor 1, 172.16.1.11 为集群一节点
    neighbor 172.16.1.11 description master1 # description
    neighbor 172.16.2.21 remote-as 7776  # 节点 2
    neighbor 172.16.2.21 description woker1 
    ```

    `Metallb` 配置：

- 配置 `BGPAdvertisement`

    此 CRD 主要用于指定需要通过 BGP 宣告的地址池，同 L2 模式，可通过池名称或者 `labelSelector`筛选。同时可配置BGP一些属性：

    ```yaml
    apiVersion: metallb.io/v1beta1
    kind: BGPAdvertisement
    metadata:
      name: local
      namespace: metallb-system
    spec:
      ipAddressPools:
      - bgp-pool
      aggregationLength: 32
    ```

    - `aggregationLength`：路由后缀聚合长度，默认为 32，意味这 BGP 通告的路由的掩码为 32，值调小可聚合路由条数
    - `aggregationLengthV6`：同上，用于 ipv6，默认为 128
    - `ipAddressPools`：[]string，选择需要 BGP 通告的地址池
    - `ipAddressPoolSelectors`：通过 label 筛选地址池
    - `nodeSelectors`：通过 node label 筛选 `loadBalancerIP` 的下一跳节点，默认为全部节点
    - `peers`：[]string，`BGPPeer` 对象的名称，用于声明此 `BGPAdvertisement` 作用于哪些 BGP 会话
    - `communities`：参考 BGP communities，可以直接配置，也可以指定 communities CRD 的名称

- 配置 BGP Peer

    BGP Peer 用于配置 BGP 会话的配置，包括对端 BGP AS 及 IP 等。

    ```yaml
    apiVersion: metallb.io/v1beta2
    kind: BGPPeer
    metadata:
      name: test
      namespace: metallb-system
    spec:
      myASN: 7776
      peerASN: 7675
      peerAddress: 172.16.1.1
      routerID: 172.16.1.11
    ```

    - `myASN`：本端 ASN，范围为 `1-64511(public AS)`、`64512-65535(private AS)`
    - `peerASN`：对端 ASN，范围同上。如果二者相等，则为 `iBGP`；否则为 `eBGP`
    - `peerAddress`：对端路由器 IP 地址
    - `sourceAddress`：指定本段建立 BGP 会话的地址，默认从本节点网卡自动选择
    - `nodeSelectors`：根据 node label 指定哪些节点需要跟 BGP Router 建立会话

- 创建 `LoadBalancer` 类型的 Service

    ```shell
    $ kubectl get svc | grep LoadBalancer
    metallb-demo   LoadBalancer   172.31.63.207   10.254.254.1   18081:30531/TCP   3h38m
    ```

### 验证

在 BGP Router 上可以看到通过 BGP 学习到的路由：

```shell
$ vtysh

Hello, this is FRRouting (version 8.1).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

router# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,
       f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure

K>* 0.0.0.0/0 [0/100] via 10.0.2.2, eth0, src 10.0.2.15, 03:52:17
C>* 10.0.2.0/24 [0/100] is directly connected, eth0, 03:52:17
K>* 10.0.2.2/32 [0/100] is directly connected, eth0, 03:52:17
B>* 10.254.254.1/32 [20/0] via 172.16.1.11, eth1, weight 1, 03:32:16
  *                        via 172.16.2.21, eth2, weight 1, 03:32:16
C>* 172.16.1.0/24 is directly connected, eth1, 03:52:17
```

可以看到通往 `LoadBalancerIP` 的下一跳分别是集群节点 1 和节点 2，在 BGP Router 执行连通性测试：

```shell
root@router:~# curl 10.254.254.1:18081
{"pod_name":"metallb-demo","pod_ip":"172.20.166.20","host_name":"worker1","client_ip":"172.20.161.0"}
```

### `FRR Mode`

目前 `Metallb` BGP 模式有两种 Backend 实现：`Native BGP` 和 `FRR BGP`。

`FRR BGP` 目前是实验阶段，对比 `Native BGP`，`FRR BGP` 主要有以下几个优点：

- `BFD` 协议支持（提高故障反应能力，缩短故障时间）
- 支持 `IPV6 BGP`
- 支持 `ECMP`
