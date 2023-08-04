# Network Portfolio Solutions

Based on open source projects, DCE 5.0 Cloud Native Networking provides not only single CNI network support, but also multiple CNI portfolio solutions.

[Free Trial Now](../../dce/license0.md){ .md-button .md-button--primary }

## Solution 1: Cilium + Macvlan/Ipvlan/SR-IOV + SpiderPool + Multus

This solution is suitable for Linux OS with high kernel version (4.19.57+), using Multus as the scheduling core and multiple CNIs to meet different network use cases and create cross-cloud and cross-cluster network connectivity.  
Moreover, SpiderPool is employed to strengthen the IP management allocation and IP recovery of Underlay network, realizing flexible IPAM management.  
Different IP pools meets various use cases of application communication. The main features of this portfolio are as follows:

1. With Multus as the scheduling core, it achieves multi CNI IP allocation to Pod and polymorphic network communication for an application. Open source solutions are used to realize cross CNI Pod communication within the cluster.
   The installation of Multus is not a must, if the application does not require multiple Pod NICs and different network modes.
2. Spiderpool serves as the IPAM management component of Underlay CNI to achieve fine-grained IP management and flexible IP planning and allocation.
   The installation of SpiderPool is not a must, if Underlay CNI is not installed in the application scenario.
3. Cilium, a high-performance Overlay CNI, provides many capabilities, including eBPF kernel acceleration, cross-cluster Pod communication, cross-cluster Service communication, flexible fine-grained network policy distribution, and traffic observation.
   Cilium is a must-have network CNI in this portfolio.
4. The external access IP provided through Ipvlan CNI / MacVLAN CNI / SR-IOV CNI enables Pod Layer 2 external communication. Complemented by Calico dynamic virtual network, it reduces chores of network operation and maintenance and also saves IP resources.
   If there is no external access requirement in the application scenario, you do not need to install Underlay CNI.



## Solution 2：Calico + Macvlan/Ipvlan/SRIOV + SpiderPool + Multus

This solution is suitable for low kernel versions of Linux OS, and applicable for cross-cluster connectivity, multiple CNIs and other diversified use cases.

1. With Multus as the scheduling core in the same way, it achieves multi CNI IP allocation and polymorphic network communication. Open source solutions are used to realize cross CNI Pod communication within the cluster.
   The installation of Multus is not a must, if the application does not require multiple Pod NICs and different network modes.
2. Spiderpool serves as the IPAM management component of Underlay CNI to achieve fine-grained IP management and flexible IP planning and allocation.
   The installation of SpiderPool is not a must, if Underlay CNI is not installed in the application scenario.
3. The external access IP provided through Ipvlan CNI / MacVLAN CNI / SR-IOV CNI enables Pod Layer 2 external communication. Complemented by Calico dynamic virtual network, it reduces chores of network operation and maintenance and also saves IP resources.
   Calico is a must-have network CNI in this portfolio. If there is no external access requirement in the application scenario, you do not need to install Underlay CNI.
4. The Submariner component provides cross-cluster Pod communication.Both Submariner and Core DNS service discovery makes cross-cluster service discovery possible. Submariner can be installed according to your demand.



## Network components

Regrading the two solutions mentioned above, DCE 5.0 allows to install the following network components:

- Cert Manager：certificate manager
- [Calico](../modules/calico/index.md)：a network solution based on iptables
- [Cilium](../modules/cilium/index.md)：a network solution based on eBPF kernel
- MacVLAN：virtual network based on Docker
- Multus：core component for multi-NIC and multi-CNI support
- MetalLB: A load-balancer implementation for bare metal Kubernetes clusters, using standard routing protocols.
- [Spiderpool](../modules/spiderpool/index.md)：an automation tool to manage IP resources

Other components such as CNI and Ingress can be installed on demand.
