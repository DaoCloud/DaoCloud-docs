---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: NA
Date: 2023-01-04
---

# What is Spiderpool

Spiderpool is an underlay and RDMA network solution for the Kubernetes. It enhances the capabilities of [MacVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan), [IPVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan), [SR-IOV CNI](https://github.com/k8snetworkplumbingwg/sriov-cni), fulfills various networking needs, and supports to run on bare metal, virtual machine, and public cloud environments. Spiderpool delivers exceptional network performance, particularly benefiting network I/O-intensive and low-latency applications like storage, middleware, and AI. It could refer to [website](https://spidernet-io.github.io/spiderpool/latest/) for more details.

The features provided by SpiderPool are as follows.

| Feature | Description
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multiple ways to use IP Pool | 1. IP Pools can be associated with namespaces, nodes, and applications via Node Selector. <br />2. You can specify the IP Pool in the Annotation when the application is deployed and get the IP resources in the IP Pool in order of priority. |
| IP Pool's node affinity | Nodes within the same cluster may belong to different data centers or different subnets. Therefore different copies of the same application need to be assigned IP addresses under different subnets for scheduling. The node affinity of IP Pool supports this scenario. |
| IP Pool's namespace affinity | Based on the namespace affinity of IP Pool, the same IP Pool can be shared to multiple Namespaces at the same time. |
| Alternate IP Pool | When the IP address in the IP Pool has been assigned and the corresponding subnet is no longer available, you can create a new subnet and IP Pool and assign it to the application to prevent the application from failing to expand its capacity. |
| Fixed IPs | Automate the creation of an application fixed IP pool and select a fixed IP range. |
| Prevent IP address assignment conflicts   | 1. The IP addresses in IP Pools are staggered and the addresses between IP Pools do not overlap. <br />2. Strictly control the addition, deletion, and checking of IP Pools to avoid IP overlap. <br />3. The IP reservation mechanism can freeze the IPs that have been used by external nodes of the cluster to prevent IP conflicts. |
| Recycle mechanism to prevent IP address leakage | In the scenario of Pod failure, reboot, rebuild, etc., clean up the junk data where IP resources are occupied by some "zombie Pods" to circumvent the problem of available IP reduction. In overlay IPAM use cases, the problem is not prominent because of the large CIDR range. In the underlay scenario, IP resources are limited and some applications have the need for a fixed IP address range, so the problem affects the healthy operation of the application. |
| Support IPv4 and IPv6 | Supports ipv4-only, ipv6-only, and dual-stack. |
| Support Statefulset | Statefulset Pod consistently gets the same IP address in reboot and rebuild use cases. |
| Pod Multi-NIC| Work with Multus to enable IP assignment support for multi-NIC use cases. |
| Reserved IP | Reserve IPs to freeze IPs that are already used by external nodes in the cluster to prevent IP conflicts. |
| Multi-level custom route | Support subnet CIDR, IP Pool, and application-level custom route with low to high priority.  |
| Rich Metrics | Provide rich monitoring metrics to ensure cluster IP resource monitoring. |
