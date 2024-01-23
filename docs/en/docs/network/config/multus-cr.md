# Creating a Multus CR

Multus CR management is the secondary encapsulation of configuration instances in Multus CNI by Spiderpool. It aims to provide more flexible network connectivity and configuration options for containers to meet different network requirements and provide users with a simpler and more cost-effective experience. This page explains how to create a Multus CR before using multiple NIC configurations for creating workloads.
If you need to create a new **Multus CR instance**, you can refer to this document.

## Prerequisites

[SpiderPool successfully deployed](../modules/spiderpool/install/install.md), the new version of SpiderPool includes all the features of Multus-underlay.

## UI Interface Operations

1. After logging in to the DCE UI, click `Container Management` -> `Clusters` in the left navigation menu to find the corresponding cluster. Then click `Container Network` -> `Network Configuration` on the left navigation menu.

    ![config](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/networkconfig01.png)

2. Go to `Network Configuration` -> `Multus CR Management`, and click `Create Multus CR`.

    ![Multus CR management](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/networkconfig02.png)

    !!! note

        When creating a Multus CR, the CNI type can only be one of the following four types: `macvlan`, `ipvlan`, `sriov`, or `custom`. There are three scenarios available.

### Create a Multus CR for macvlan or ipvlan

Enter the following parameters:

![multus cr](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/networkconfig03.png)

- `Name`: The instance name of the Multus CNI configuration, which is the Multus CR name.
- `Description`: Description of the instance.
- `CNI Type`: The type of CNI. Currently, you can choose between `macvlan` and `ipvlan`.
- `IPv4 Default Pool`: IPv4 default pool in the CNI configuration file.
- `IPv6 Default Pool`: IPv6 default pool in the CNI configuration file.
- `Vlan ID`: Only allowed to be configured when the CNI type is `macvlan`, `ipvlan`, or `sriov`. "0" and "" have the same effect.
- `NIC Configuration`: NIC configuration includes interface configuration information. When the number of NIC interfaces is one, there will only be one NIC interface in the default NIC configuration. When the number of added interfaces is greater than or equal to two, bond-related configuration can be done.
- `NIC Interface`: Only used for `macvlan` and `ipvlan` CNI types, at least one element is required. If there are two or more elements, bond must not be empty.
- `Bond Information`: The name cannot be empty, and the mode must be within the range [0, 6], corresponding to the seven modes:
    - balance-rr
    - active-backup
    - balance-xor
    - broadcast
    - 802.3ad
    - balance-tlb
    - balance-alb

Parameters are optional, and the input format is `k1=v1;k2=v2;k3=v3`, separated by `;`.

#### VLAN Configuration

- Underlay network refers to the underlying physical network, usually involving VLAN networks. If the Underlay network does not involve VLAN networks, there is no need to configure the VLAN ID (default value is 0).
- **For VLAN subinterfaces**:
    - If the network administrator has already created the VLAN subinterfaces, there is no need to fill in the VLAN ID (default value is 0), just fill in the created VLAN subinterface in the "Network Interface" (Master) field.
    - If automatic creation of VLAN subinterfaces is required, the VLAN ID needs to be configured, and the main network interface (Master) should be set to the corresponding parent interface. When creating a Pod, Spiderpool dynamically creates a subinterface named `<master>.<vlanID>` on the host to connect the Pod to the VLAN network.
- **For Bond NIC**:
    - If the network administrator has already created the Bond NIC and is using it to connect the Pod to the Underlay network, there is no need to fill in the VLAN ID (default value is 0), just fill in the name of the created Bond NIC in the "Network Interface" (Master) field.
    - If automatic creation of Bond NIC is required without creating VLAN subinterfaces, set the VLAN ID to 0 and configure at least 2 network interfaces (Master) to form the Bond's Slave NICs. Spiderpool dynamically creates a Bond NIC on the host when creating a Pod to connect it to the Underlay network.
- **For RDMA NIC**:
    - If exposing the RoCE NIC on the host to the Pod based on Macvlan/IPVLAN/SRIOV, the VLAN ID does not need to be filled in and defaults to 0.
- **Using Bond NIC to create VLAN subinterfaces**:
    - If it is required to create VLAN subinterfaces at the same time when creating the Bond NIC to accommodate the Pod network, the VLAN ID needs to be configured. Spiderpool dynamically creates a VLAN subinterface named `<bondName>.<vlanID>` on the host when creating a Pod to connect it to the VLAN network.
    - All interfaces created through Spiderpool are not configured with IP addresses, and these interfaces are not persistent. If they are accidentally deleted or the node is restarted, these interfaces will be deleted, and they will be automatically re-created after restarting the Pod. If persistence of these interfaces or configuration of IP addresses is required, consider using the [nmcli](https://networkmanager.dev/docs/api/latest/nmcli.html) tool.

### Create a Multus CR for SR-IOV

Enter the following parameters:

![multus cr](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/networkconfig04.png)

- `CNI Type`: Select SR-IOV.
- `RDMA`: Not enabled by default. If you need to enable it, please meet the [RDMA resource usage requirements](../modules/spiderpool/rdmapara.md).
- `IPv4/IPv6 Default Pool`: Not set by default. If set, it will be used as the default IP Pool when creating a workload without adding an IP Pool.
- `VLAN ID`: Must be filled in as `0`.
- `SR-IOV Resources`: Only used for the `sriov` type, enter the resource name, which cannot be empty. Refer to [SR-IOV CNI Configuration](../modules/multus-underlay/sriov.md) for how to view SR-IOV resources.

**SR-IOV Resource Configuration Description:**

`SR-IOV resourceName` is the custom name used when deploying `sriovnetworknodepolicies`.

If using **SR-IOV with RDMA**, the SR-IOV resource configuration can be queried as follows:

**Command Query:**

The `spidernet.io/sriov_netdevice_enp4s0f0np0` below is the queried resource name.

```sh
   kubectl get no -o json | jq -r '[.items[] | {name:.metadata.name, allocable:.status.allocatable}]'
   [
     {
       "name": "10-20-1-220",
       "allocable": {
         "cpu": "56",
         "ephemeral-storage": "3971227249029",
         "hugepages-1Gi": "0",
         "hugepages-2Mi": "0",
         "memory": "131779740Ki",
         "pods": "110",
         "spidernet.io/hca_shared_devices": "0",
         "spidernet.io/mellanoxrdma": "0",
         "spidernet.io/sriov_netdevice": "0",
         "spidernet.io/sriov_netdevice_enp4s0f0np0": "8", # 查询的 RDMA 设备资源名称及数量
         ...
       }
     }
```

**GUI Query:**

The queried `resourceName` needs to be prefixed with `spidernet.io/`.

### Create a Custom Multus CR

![multus cr](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/networkconfig05.png)

- `JSON`: for custom types, make sure to input a valid JSON file.

After creating it, you can use the Multus CR to manage [workloads](use-ippool/usage.md).
