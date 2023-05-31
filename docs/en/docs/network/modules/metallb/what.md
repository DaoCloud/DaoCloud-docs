# Metallb

In Kubernetes, for the `LoadBalancer` type, it is necessary to use the cloud provider's load balancer to expose the service to the outside, and the external load balancer can route traffic to the automatically created `NodePort` service and `ClusterIP` service.
Therefore, for the service of type `LoadBalancer`, it must be supported by `Cloud Provider` to realize it.
That is to say, services of type `LoadBalancer` cannot be used in bare-metal K8s clusters. Otherwise, you will find that the service of `LoadBalancer` is always in Pending state.



`Metallb` is an open source software that uses standard routing protocols (ARP or BGP) to implement load balancing for bare metal K8s clusters.

## L2 mode (ARP)

In L2 mode, `Metalb` will elect a Leader node through `memberlist`, and this node is responsible for announcing `LoadBalancerIP` to the local network.
From a network standpoint, this machine appears to have multiple IP addresses, and it responds to `ARP` requests from `LoadBalancerIP`.
The biggest advantage of L2 mode is that it can work without relying on hardware such as routers.

- Advantages: universal, no additional hardware support required
- Disadvantages: Bandwidth limitation of a single node, slightly slow failover (about 10s)

## L3 mode (BGP)

In BGP mode, each node in the cluster will establish a BGP Peer with the router, and use this session to advertise the `LoadBalanceIP` of the cluster service to the outside of the cluster.
BGP Router selects a next hop based on each different connection (that is, a certain node in the cluster, which is different from all traffic in L2 mode first arriving at a certain Leader node).

- Advantage: better load balancing
- Disadvantage: When a node fails, all BGP sessions will be interrupted