---
hide:
  - toc
---

# Challenges facing the network

**Network connectivity under multicloud and multicluster**

In a multicluster environment, it is not only necessary to consider the use of different network CNIs by each cluster, but also to realize the interconnection of each cluster.
Therefore, issues such as Cluster IP intercommunication and DNS intercommunication need to be resolved.

**Unified IP resource management under multicloud and multicluster**

To achieve network interoperability in a multicloud and multicluster environment, the IPs within the cluster and within the cluster cannot be duplicated or conflicted. Therefore, IP management and planning should be based on the multicluster perspective to avoid IP conflicts and network segment conflicts (Underlay IP, Service IP, etc.).

**Single CNI is difficult to meet the needs of diverse use cases**

Faced with diverse network use cases, different types of applications currently have different network requirements. It is difficult for a single network CNI to meet the needs of diverse use cases. Therefore, specific CNI needs to be used to meet business requirements in specific cases, and CNI combination is also required in more complex cases.

**There is a strong demand for fixed and externally accessible IP, but there is a lack of flexible and efficient IPAM mechanism**

A fixed and externally accessible IP is implemented based on Underlay CNI, but IP resources in Underlay CNI are relatively scarce and require strict firewall control. Therefore, the use of Underlay IP requires strict planning and allocation.
When the IP address release and allocation fail, it needs to be recovered in time to prevent resource waste.

**Unified management of network security policies and network traffic**

It is necessary to unify the distribution of network security policies for different clusters, and to control and encrypt network traffic between different clusters.

**New challenges brought by the combination of new technologies such as software and hardware integration, network acceleration**

In order to meet the high-performance and low-latency network requirements, the combination with hardware-based virtualization acceleration network solutions such as SR-IOV and network acceleration solutions such as eBPF is also a major opportunity and challenge for cloud native container networks.