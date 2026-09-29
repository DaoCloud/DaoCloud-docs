# KubeVirt Fixed IP and Underlay Network

This page describes the recommended configuration for using Spiderpool in DCE to provide fixed IP
and Underlay network capabilities for KubeVirt virtual machines.

## Scenarios

- KubeVirt virtual machines need to keep the same IP after restart, rebuild, or live migration
- VMs need to be directly connected to the Underlay network

## Differences Between Network Modes and Capabilities

| Mode | Typical CNI | NIC Count | Service Mesh | Live Migration | Description |
| --- | --- | --- | --- | --- | --- |
| passt | macvlan/ipvlan | Single NIC | Supported | Not supported | Suitable for lightweight scenarios |
| bridge | ovs-cni | Multiple NICs | Not supported | Not supported | Suitable for multi-NIC scenarios |

> Note: Spiderpool records the fixed IP of a KubeVirt VM at the VM level rather than the Pod level.

## Prerequisites

- Spiderpool is installed (refer to [Install Spiderpool](../modules/spiderpool/install/install.md))
- An Underlay CNI is ready (Macvlan/IPvlan or OVS)

## Key Configuration

Spiderpool enables the KubeVirt fixed IP feature by default. To disable it, set the following
when installing Spiderpool:

- `ipam.enableKubevirtStaticIP=false`

## Example Procedure (passthrough + macvlan)

1. Create the Multus configuration for macvlan (refer to [Manage Multus CR](multus-cr.md)).
2. Create an IPPool (refer to [Create Subnet and IP Pool](ippool/createpool.md)).
3. Create a VM and specify the default NIC configuration:

```yaml
metadata:
  annotations:
    v1.multus-cni.io/default-network: kube-system/macvlan-ens192
```

After creation, the VM Pod keeps obtaining the same IP across restart and rebuild scenarios.

!!! note

    - In the KubeVirt live migration scenario, Spiderpool does not perform IP conflict detection
    - The passt mode supports only a single NIC; the bridge mode supports multiple NICs but does not
      support Service Mesh
