# EgressGateway

In a Kubernetes (k8s) cluster, when a Pod accesses external services, its egress IP address is not fixed.
In an overlay network, the egress IP address is the address of the node where the Pod is located, while in
an underlay network, the Pod directly uses its own IP address to communicate with the outside. Therefore,
when a Pod is rescheduled, regardless of the network mode, the IP address used for external communication
will change. This instability poses a challenge for IP address management for system administrators.
Especially when the cluster scales up and network troubleshooting is required, it is difficult to control
egress traffic based on the original egress IP of Pods outside the cluster. To address this issue,
EgressGateway is introduced into the k8s cluster. It is an open-source egress gateway designed to solve
the problem of egress IP address in different CNI network modes (Calico, Flannel, Weave, Spiderpool).
By flexibly configuring and managing egress policies, EgressGateway allows setting egress IP for tenant-level
or cluster-level workloads, ensuring that when Pods access external networks, a unified egress IP is used as
the egress address, thus providing a stable solution for egress traffic management.

## EgressGateway Architecture

![Architecture](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/egressgateway/architecture.png)

## Why Choose EgressGateway

### Features and advantages

* Solves the IPv4/IPv6 dual-stack connectivity issue, ensuring seamless network communication across different protocol stacks.
* Solves the high availability problem of egress nodes, ensuring network connectivity is not affected by single point failures.
* Allows more granular policy control, enabling flexible filtering of Pods' egress policies, including Destination CIDR.
* Allows filtering of egress applications (Pods), enabling more precise management of egress traffic for specific applications.
* Supports multiple instances of egress gateways, capable of handling communication between multiple network partitions or clusters.
* Supports tenant-level egress IP.
* Supports automatic detection of egress gateway policies for cluster traffic.
* Supports namespace default egress instances.
* Can be used in lower kernel versions, suitable for various Kubernetes deployment environments.

### Compatible with multiple network solutions

* [Calico](https://github.com/projectcalico/calico)
* [Flannel](https://github.com/flannel-io/flannel)
* [Weave](https://github.com/weaveworks/weave)
* [Spiderpool](https://github.com/spidernet-io/spiderpool)
