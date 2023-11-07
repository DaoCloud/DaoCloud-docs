# Creating a Multus CR

Multus CR management is the secondary encapsulation of configuration instances in Multus CNI by Spiderpool. It aims to provide more flexible network connectivity and configuration options for containers to meet different network requirements and provide users with a simpler and more cost-effective experience. This page explains how to create a Multus CR before using multiple NIC configurations for creating workloads.

- If you have already created a Multus CR instance during the deployment of the SpiderPool components, you can directly use that Multus CR instance to create [workloads](https://docs.daocloud.io/network/modules/spiderpool/usage.html).
- If you need to create a new Multus CR instance, you can refer to this document.

## Prerequisites

- [SpiderPool successfully deployed](../modules/spiderpool/install.md), the new version of SpiderPool includes all the features of Multus-underlay.

## UI Interface Operations

1. After logging in to the DCE UI, click `Container Management` -> `Cluster List` in the left navigation menu to find the corresponding cluster. Then click `Container Network` -> `Network Configuration` on the left navigation menu.


2. Go to `Network Configuration` -> `Multus CR Management`, and click `Create Multus CR`.


    !!! note

        Note: When creating a Multus CR, the CNI type can only be one of the following four types: `macvlan`, `ipvlan`, `sriov`, or `custom`. There are three scenarios available.

3. Enter the creation page

    Scenario 1: When the CNI type is `macvlan` or `ipvlan`, enter the following parameters:

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

    Scenario 2: When the CNI type is `sriov`, enter the following parameters:


    - The `Name`, `Description`, `CNI Type`, `IPv4 Default Pool`, `IPv6 Default Pool`, and `Vlan ID` configurations are the same as in scenario 1.
    - `SR-IOV Resource`: Only used for the `sriov` type, enter the resource name, which cannot be empty.

    Scenario 3: When the CNI type is `custom`, enter the following parameters:


    - `JSON`: For custom types, make sure to input a valid JSON file.

4. After creating it, you can use the Multus CR to manage [workloads](../modules/spiderpool/usage.md).
