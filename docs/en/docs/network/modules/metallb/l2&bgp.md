# MetalLB L2 and BGP mode

## MetalLB L2 mode

In L2 mode, `Metalb` will announce the address of `LoadBalancerIP` through ARP (for ipv4), NDP (for ipv6).
Before `Metallb` < `v0.13.2`, `Metallb` can only be configured via `configMap`.
After `v0.13.2`, `Metallb` is configured through CRD resources, and the method of `configMap` has been deprecated.

In `Layer2` mode, when creating a service, `Metalb` (`speaker` component) will elect a node in the cluster for this service as the host exposed to the outside world.
When a request is made to the `externalIP` of the Service, this node will reply to the `arp` request instead of this `externalIP`.
Therefore, the request sent to the Service will first reach this node in the cluster, then pass through the `kube-proxy` component on this node, and finally direct the traffic to a specific endpoint (endpoint) of this service.

There are three main points in the logic of service election nodes:

1. First filter out the nodes that are not ready and the nodes where the endpoint is not ready
2. If the endpoint of the service is distributed on the same node, then filter this node as the `arp` responder of the service IP
3. If the endpoints of the service are distributed on different nodes, after calculating `node + # + externalIP` through `sha256`, take the first one according to the dictionary order

In this way, MetalLB will select a node for each Service as the exposed host.
`metallb` will direct the traffic of this single Service to a certain node, so this node may become a bottleneck that limits performance.
The bandwidth limit of Service will also depend on the bandwidth of a single node, which is also the most important limitation of using ARP or NDP.

Also, when this node fails, MetalLB needs to re-elect a new node for the service.
`Metallb` will then send a "gratis" `arp` to the client, telling the client that their Mac address cache needs to be updated.
Traffic is still forwarded to the failed node until the client updates the cache. So from a certain point of view: the time of failover depends on the speed at which the client updates the Mac address cache.

### Usage

- Create an IP pool

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

- `addresses`: IP address list, each list member can be a CIDR, it can be an address range (such as 192.168.9.1 - 192.168.9.5), or it can be different `ipFamily`, `Metallb` will allocate IP from it Service `LoadBalancer`

- `autoAssign`: Whether to automatically assign the IP address, the default is true. In some cases (insufficient IP addresses or public IPs), you don't want the IPs in the pool to be assigned easily, can be set to false.
   You can set annotations: `metallb.universe.tf/address-pool: pool-name` in service. Or set the IP in the `spec.LoadBalancerIP` field (note that this method has been marked as abandoned by k8s).

- `avoidBuggyIPs`: Whether to avoid using `.0` or `.255` addresses in the pool, the default is false.

- Configure `LoadBalancerIP` advertisement rule (L2)

    Bind IP pools via `L2Advertisement`, which tells `Metallb` that these addresses should be advertised by `ARP` or `NDP`.

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

- `ipAddressPools`: optional, filter IP pools by name, if `ipAddressPools` and `ipAddressPoolSelectors` are not specified at the same time, it will be applied to all IP pools.

- `ipAddressPoolSelectors`: optional, filter IP pools through labels, if `ipAddressPools` and `ipAddressPoolSelectors` are not specified at the same time, it will act on all IP pools.

- `nodeSelectors`: Optional, used to filter which nodes are used as the next hop of `loadBalancerIP`, default to all nodes.

- Create `LoadBalancerService`

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

    Just specify `spec.type=LoadBalancer`, so that `Metallb` will naturally take over the lifecycle of this `Service`.

    !!! note

        If you want the Service to allocate addresses from the specified IP pool, specify through `annotations: metallb.universe.tf/address-pool: <pool-name>`. Or specify the IP through the `service.spec.loadBalancerIP` field (need to ensure that it exists in a pool, this method is not recommended).
        If there are multiple load balancers, they can be specified through the `service.spec.loadBalancerClass` field. When deploying `Metalb`, it can be configured by `--lb-class` flag.

### Load Balancing

- When `Service.spec.externalTrafficPolicy=cluster`

    In this mode, it has good load balancing, but the traffic may go through multiple hops, which will hide the source IP of the client.

    ```none
                                      ______________________________________________________________________________
                                    |                       -> kube-proxy(SNAT) -> pod A                          |
                                    |                      |                                                      |
    client -> loadBalancerIP:port -> | -> node A（Leader） ->                                                       |
                                    |                      |                                                      ｜
                                    |                       -> kube-proxy(SNAT) -> node B -> kube-proxy -> pod B  ｜
                                      ------------------------------------------------------------------------------
    ```

- When `Service.spec.externalTrafficPolicy=local`

    In this mode, the source IP of the client will be reserved, but the load balancing is poor, and the traffic will go to a certain backend Pod.

    ```none
                                      __________________________________________________________________________________________
                                    |                       -> kube-proxy -> pod A (the backend Pod is on this node)                            |
                                    |                      |                                                                  |
    client -> loadBalancerIP:port -> | -> node A（Leader） ->                                                                   |
                                    |                      |                                                                  ｜
                                    |                       -> kube-proxy -> node B -> kube-proxy -> pod B (the backend Pod is on a different node)  ｜
                                      ------------------------------------------------------------------------——————————————————
    ```

## MetalLB BGP Mode(L3)

The `Layer2` mode is limited to a two-layer network, and the traffic flowing to the Service will be forwarded to a specific node first, which is not a real load balancing.
The BGP mode is not limited to a Layer 2 network. Each node in the cluster will establish a BGP session with the BGP Router, and declare that the next hop of the `ExternalIP` of the Service is the cluster node itself.
In this way, external traffic can be connected to the cluster through the BGP Router, and every time the BGP Router receives new traffic destined for the `LoadBalancer` IP address, it will create a new connection to the node.
But which node to choose, each router manufacturer has a specific algorithm to achieve. So from that point of view, this has good load balancing.

### Usage

- Create an IP pool

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

- Configure `LoadBalancerIP` advertisement rule (L3)

    !!! note

        BGP mode requires hardware support to run the BGP protocol. If not, software such as `frr`, `bird` can be used instead.

    It is recommended to use `frr` for installation:

    ```shell
    #ubuntu
    apt install frr
    #centos
    yum install frr
    ```

    `frr` configures `BGP`:

    ```shell
    router bgp 7675 # Bgp as number
    bgp router-id 172.16.1.1 # route-id is usually the interface IP
    no bgp ebgp-requires-policy # close ebpf filter !!!
    neighbor 172.16.1.11 remote-as 7776 # Configure ebgp -> neighbor 1, 172.16.1.11 as a cluster node
    neighbor 172.16.1.11 description master1 # description
    neighbor 172.16.2.21 remote-as 7776 # node 2
    neighbor 172.16.2.21 description woker1
    ```

    `Metalb` configuration:

- Configure `BGPAdvertisement`

    This CRD is mainly used to specify the IP pool that needs to be announced through BGP. Like the L2 mode, it can be filtered by the pool name or `labelSelector`. At the same time, some attributes of BGP can be configured:

    ```yaml
    apiVersion: metallb.io/v1beta1
    kind: BGPAdvertisement
    metadata:
      name: local
      namespace: metallb-system
    spec:
      ipAddressPools:
      -bgp-pool
      aggregationLength: 32
    ```

    - `aggregationLength`: route suffix aggregation length, the default is 32, which means that the mask of the route advertised by BGP is 32, the value can be reduced to aggregate the number of routes
    - `aggregationLengthV6`: Same as above, for ipv6, default is 128
    - `ipAddressPools`: []string, select the IP pools that need to be advertised by BGP
    - `ipAddressPoolSelectors`: filter IP pools by label
    - `nodeSelectors`: Filter the next hop nodes of `loadBalancerIP` by node label, default is all nodes
    - `peers`: []string, the name of a `BGPPeer` object declaring which BGP sessions this `BGPAdvertisement` applies to
    - `communities`: Refer to BGP communities, you can configure it directly, or specify the name of the communities CRD

- Configure BGP Peers

    BGP Peer is used to configure BGP session configuration, including peer BGP AS and IP, etc.

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

    - `myASN`: local ASN, the range is `1-64511(public AS)`, `64512-65535(private AS)`
    - `peerASN`: Peer ASN, the scope is the same as above. if both are equal, then `iBGP`; otherwise, `eBGP`
    - `peerAddress`: peer router IP address
    - `sourceAddress`: Specify the address for establishing a BGP session in this segment, which is automatically selected from the network card of this node by default
    - `nodeSelectors`: Specify which nodes need to establish a session with the BGP Router according to the node label

- Create a Service of type `LoadBalancer`

    ```shell
    $ kubectl get svc | grep LoadBalancer
    metallb-demo LoadBalancer 172.31.63.207 10.254.254.1 18081:30531/TCP 3h38m
    ```

### Verify

You can see the routes learned through BGP on the BGP Router:

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
        t-trapped, o-offload failure
K>* 0.0.0.0/0 [0/100] via 10.0.2.2, eth0, src 10.0.2.15, 03:52:17
C>* 10.0.2.0/24 [0/100] is directly connected, eth0, 03:52:17
K>* 10.0.2.2/32 [0/100] is directly connected, eth0, 03:52:17
B>* 10.254.254.1/32 [20/0] via 172.16.1.11, eth1, weight 1, 03:32:16
   * via 172.16.2.21, eth2, weight 1, 03:32:16
C>* 172.16.1.0/24 is directly connected, eth1, 03:52:17
```

You can see that the next hops to `LoadBalancerIP` are cluster node 1 and node 2 respectively, and perform a connectivity test on the BGP Router:

```shell
root@router:~# curl 10.254.254.1:18081
{"pod_name":"metallb-demo","pod_ip":"172.20.166.20","host_name":"worker1","client_ip":"172.20.161.0"}
```

### `FRR Mode`

Currently there are two Backend implementations of `Metallb` BGP mode: `Native BGP` and `FRR BGP`.

`FRR BGP` is currently in the experimental stage. Compared with `Native BGP`, `FRR BGP` has the following advantages:

- `BFD` protocol support (improves fault response capability, shortens fault time)
- Support `IPV6 BGP`
- Support `ECMP`