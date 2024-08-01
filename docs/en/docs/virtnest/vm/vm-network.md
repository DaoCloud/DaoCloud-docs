---
MTPE: ModetaNiu
DATE: 2024-07-11
---

# Virtual Machine Networking

This article will introduce how to configure network information when creating virtual machines.

In virtual machines, network management is a crucial part that allows us to manage and configure network connections 
for virtual machines in a Kubernetes environment. It can be configured according to different needs and scenarios, 
achieving a more flexible and diverse network architecture.

1. Single NIC Scenario: For simple applications that only require basic network connectivity or when there are 
   resource constraints, using a single NIC can save network resources and prevent waste of resources.
2. Multiple NIC Scenario: When security isolation between different network environments needs to be achieved, 
   multiple NICs can be used to divide different network areas. It also allows for control and management of traffic.

## Prerequisites

1. When selecting the Bridge network mode, some information needs to be configured in advance:

    - Create a Multus CR of type `ovs`. See [Creating a Multus CR](https://spidernet-io.github.io/spiderpool/v0.9/usage/install/underlay/get-started-ovs/)
    - Create a subnet and IP pool. See [Creating Subnets and IP Pools](../../network/config/ippool/createpool.md)
.
## Network Configuration

1. Network configuration can be combined according to the table information.

    | Network Mode       | CNI     | Spiderpool Installed | NIC Mode    | Fixed IP         | Live Migration |
    | ------------------ | ------- | -------------------- | ----------- | ----------------- | -------------- |
    | Masquerade (NAT)   | Calico  | ❌                   | Single NIC  | ❌               | ✅            |
    |                    | Cilium  | ❌                   | Single NIC  | ❌               | ✅            |
    |                    | Flannel | ❌                   | Single NIC  | ❌               | ✅            |
    | Bridge             | OVS     | ✅                   | Multiple NIC| ✅               | ✅           |
    
    ![Network Config](../images/createvm-net01.png)

2. Network Mode: There are two modes - Masquerade (NAT) and Bridge. Bridge mode requires the installation of 
   the spiderpool component.

    1. The default selection is Masquerade (NAT) network mode using the eth0 default NIC.
      
    2. If the cluster has the spiderpool component installed, then Bridge mode can be selected. The Bridge mode 
       supports multiple NICs.

        ![Network Mode](../images/createvm-net02.png)
        
        - When selecting Bridge mode, there are some prerequisites.
           - Create ovs type Multus CR, currently cannot be created on the page. Refer to [Creating ovs type Multus CR](https://spidernet-io.github.io/spiderpool/v0.9/usage/install/underlay/get-started-ovs-zh_CN/)
           - Create subnets and IP pools similar to passt mode.

3. Adding NICs
   
    1. Bridge modes support manually adding NICs. Click __Add NIC__ to configure the NIC IP pool. Choose a Multus CR 
       that matches the network mode, if not available, it needs to be created manually.
    
    2. If the __Use Default IP Pool__ switch is turned on, it will use the default IP pool in the multus CR 
       configuration. If turned off, manually select the IP pool.
       
        ![Add NIC](../images/createvm-net03.png)
