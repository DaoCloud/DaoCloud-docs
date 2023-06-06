---
hide:
  - toc
---

# Network Planning

Based on the best practice of Overlay CNI + Underlay CNI [network card planning](./ethplan.md), the network planning diagram of the cluster is as follows:



**Planning Instructions**:

- In this plan, the default CNI is Calico/Cilium, which needs to be installed together with components such as Multus-underlay and Spiderpool.
- It is recommended that all nodes have multiple physical NICs with the same name.
- eth0 is the network card where the default route of the host is located, and the gateway points to the Gateway host, which forwards to the external network.
   The main uses are: communication between nodes, K8s management network card, Calico Pod communication.
- eth1 is the underlay service network card, no need to set an IP address.
   Create VLAN subinterfaces (eth1.1, eth1.2) based on eth1, corresponding to network segments such as 172.16.15.0/24 and 172.16.16.0/24.
   The created business application Pod uses the address of the corresponding network segment, which can meet the multi-VLAN and multi-subnet use cases.