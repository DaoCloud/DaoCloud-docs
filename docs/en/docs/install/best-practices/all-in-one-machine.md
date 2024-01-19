# DCE 5.0 All-in-One Deployment

This document explains how to deploy DCE 5.0 on an all-in-one machine.

## Environment Preparation

First, you need to prepare a good network environment and capacity planning.

### Network Requirements

**Hardware**

- Usually, the all-in-one machine has multiple network cards or one network card with multiple ports, so it is recommended to create a Bond and make the Bond with LACP port group highly available.
- It is not recommended to divide into multiple planes temporarily, and share one data plane.
- The network port needs to be in trunk mode.

**Reserved VLANs**

At least 2 VLANs are required: 1 for BMC VLAN, 1 for management/business VLAN, and 1 for storage VLAN (optional).
If you need to allocate "static IP" for Pods, you need to create sub-interfaces and allocate VLANs additionally.

| Name | Purpose |
| --- | --- |
| Management/Business VLAN | Used for SSH, management interface, API, business traffic, load balancing, and internal communication within the cluster |
| BMC VLAN | Used for BMC management of servers |
| Storage VLAN (optional) | Used for local and remote storage access |

**IP**

| Resource | Requirement | Description |
| --- | --- | --- |
| istioGatewayVip | 1 | If the load balancing mode is metallb, you need to specify a VIP for the UI interface and OpenAPI access of DCE. |
| insightVip | 1 | If the load balancing mode is metallb, you need to specify a VIP for insight data collection of the Global cluster, and the insight-agent of the sub-cluster can report data to this VIP. |
| Protocol | - | Supports IPv6. |
| Reserved IP Address Range | 2 ranges need to be reserved | Used by Pods (default is 10.233.64.0/18) and Services (default is 10.233.0.0/18). If they are already in use, you can customize other network segments to avoid IP address conflicts. |
| Routing | - | The server has a default route or a route pointing to the address 0.0.0.0. |
| NTP Server Addresses | 1-4 | Ensure that your data center has NTP server IP addresses that can be accessed. |
| DNS Server Addresses | 1-2 | If your application requires DNS services, please prepare DNS server IP addresses that can be accessed. |

**Network Ports**

[Port Requirements](../commercial/port-requirements.md)

### Capacity Planning

**CPU, Memory, Disk**

| Physical Machine | CPU | Memory | containerd and k8s use the root disk by default | Remarks |
| --- | --- | --- | --- | --- |
| master01 | >= 12 C | >= 20 G | 480G, SSD disk, RAID1 | Recommended to allocate higher resources as "boostrap machine + cluster control node" |
| master02 | >= 12 C | >= 20 G | 480G, SSD disk, RAID1 | - |
| master03 | >= 12 C | >= 20 G | 480G, SSD disk, RAID1 | - |

**Environment Preparation Checklist**

| Category | Check Item | Level | Result |
| --- | --- | --- | --- |
| Category | Sufficient rack space (1 server requires 2U space) | Required | - |
| | Sufficient power supply in the rack, each server at least has a rated power of 750W | Required | - |
| | The rack has UPS power protection | Optional | - |
| | Any special requirements for power cords (default provides 2 C13 standard power cords) | Required | - |
| | Any special requirements for network cables (default provides 4 SFP+ optical modules or 4 5m LC-LC multimode fiber optic cables or 3m Cat6 network jumpers) | Required | - |
| | Access to the all-in-one machine using Chrome browser (able to connect to the required VLAN) | Required | - |
| | A switch for connecting to the BMC RJ45 port, 1 port per server needs to be reserved | Required | - |
| | Two switches for connecting to the data traffic SFP+ ports, 2 ports per server need to be reserved, a total of 4 ports | Recommended | - |
| | If it is not possible to configure "two redundant switches", at least one switch with SFP+ ports is required, 2 ports per server need to be reserved | Required | - |
| | The ports connected to the SFP+ ports on the switch are configured as Trunk and allow the corresponding VLAN | Required | - |
| | The switch connected to the SFP+ ports has enabled IPv4 and IPv6 multicast, ensuring multicast between switches | Required | - |
| | If you are using redundant switches, configure the corresponding stacking | Required | - |
| Network | At least 2 VLANs are required: 1 for BMC VLAN, 1 for management/business VLAN, and 1 for storage VLAN (optional) | Required | - |
| | If you need to allocate "static IP" for Pods, you need to create sub-interfaces and allocate VLANs additionally | Optional | - |
| | NTP server IP addresses accessible within the cluster | Required | - |
| | If your application requires DNS services, prepare DNS server IP addresses accessible within the cluster | Recommended | - |
| | Ensure that there are enough consecutive IP addresses in the reserved BMC VLAN for each server to have 1 IP address in that VLAN | Required | - |
| | Ensure that there are enough consecutive IP addresses in the reserved management/business VLAN for each server to have 1 IP address, and the entire cluster needs an additional 1 IP address (management interface) | Required | - |
| | The entire cluster needs an additional 2 IP addresses (istioGatewayVip, insightVip) | Required | - |
| | Ensure that there are enough consecutive IP addresses in the reserved storage VLAN for each server to have 1 IP address in that VLAN | Optional | - |
| | Reserved IP address range (used by Calico and Kube-Proxy), default is clusterCIDR: 10.233.64.0/18, serviceCIDR: 10.233.0.0/18. If they are already in use, you can customize other network segments to avoid IP address conflicts. | Required | - |
| Capacity Planning | Ensure that you have done capacity planning and the current cluster capacity (CPU, memory, network, disk) and performance can support your containerized business | Required | - |
| | Ensure that in the event of an arbitrary server failure, the remaining cluster has sufficient capacity to support it | Required | - |
| | If you plan to expand in the future, you need to prepare rack space, switch ports, and corresponding VLAN IP addresses in advance | Recommended | - |

## Installation Steps (3 Physical Machines)

### Install Prerequisites

[Install Dependencies](../install-tools.md)

### Offline Installation

[Start Installation](../commercial/start-install.md)

**Precautions before installation:**

- Select one of the three physical machines as the boostrap machine to execute the deployment of DCE 5.0. In the cluster configuration file `ClusterConfig.yaml`, the bootstrapNode parameter can specify the IP of the boostrap machine.

    ```yaml
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      clusterName: my-cluster
    
      # The domain name or IP of the boostrap node, which is resolved to the IP of the default gateway of the boostrap node by default;
      # You can manually enter the IP or domain name, if it is a domain name, if it is unable to resolve, an automatic mapping between this domain name and the default IP of the boostrap node will be established
      # bootstrapNode: auto  ## Automatically resolved by default
      ...
    ...
    ```

- In the cluster configuration file ClusterConfig.yaml, configure the information of the 3 physical machines in masterNodes.

    ```yaml
    ...
    apiVersion: provision.daocloud.io/v1alpha3
    kind: ClusterConfig
    metadata:
    spec:
      ...
      masterNodes:
        - nodeName: "g-master1" # Physical machine 1 acts as the control plane node + boostrap node
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
          #ansibleSSHPort: "22"
          #ansibleExtraArgs: "" 
        - nodeName: "g-master2"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
          #ansibleSSHPort: "22"
          #ansibleExtraArgs: ""
        - nodeName: "g-master3"
          ip: xx.xx.xx.xx
          ansibleUser: "root"
          ansiblePass: "dangerous"
          #ansibleSSHPort: "22"
          #ansibleExtraArgs: ""
        ...
    ...
    ```
