---
MTPE: WANG0608GitHub
DATE: 2024-08-01
---

# MetalLB

In Kubernetes, for the LoadBalancer service, it is necessary to use the cloud provider's load balancer
to expose the service externally.
The external load balancer can route traffic to
the automatically created NodePort service and ClusterIP service.
Therefore, the LoadBalancer service must be supported by Cloud Provider to implement it.
That is to say, LoadBalancer service cannot be used in bare-metal K8s clusters.
Otherwise, you will find that LoadBalancer service is always in Pending state.

![MetalLB](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/lbservice.png)

MetalLB is an open source software that uses standard routing protocols (ARP or BGP) to implement
load balancing for bare-metal K8s clusters.

## L2 mode (ARP)

In L2 mode, MetalLB will elect a Leader node through memberlist, and this node is responsible
for announcing LoadBalancerIP to the local network.
From a network perspective, this machine appears to have multiple IP addresses, and it responds to ARP requests from LoadBalancerIP.
The biggest advantage of L2 mode is that it can work without relying on hardware such as routers.

- Advantages: universal, no additional hardware support required
- Disadvantages: Bandwidth limitation of a single node, slightly slow failover (about 10s)

## L3 mode (BGP)

In BGP mode, each node in the cluster will establish a BGP Peer with the router,
and use this session to advertise the LoadBalanceIP of the cluster service to the outside of the cluster.
BGP Router selects the next-hop (a certain node in the cluster. It is different from all traffic in the L2 mode
first arriving at a certain Leader node) based on each different connection.

- Advantage: better load balancing
- Disadvantage:
    - When a node fails, all BGP sessions will be interrupted
    - Calico BGP mode cannot coexist with MetaLB L3 mode, as conflicts will arise.
      For more details, please refer to [ISSUES WITH CALICO](https://metallb.universe.tf/configuration/calico/)
