---
MTPE: WANG0608GitHub
date: 2024-08-09
---

# Macvlan

Macvlan is a NIC virtualization solution for Linux, which can virtualize a physical NIC into multiple virtual NICs.
With Multus, one or more Macvlan NICs can be assigned to pods, so that pods can communicate externally through Macvlan NICs.

## Install

In Kubernetes, Macvlan is just a binary file stored under `/opt/cni/bin` of each node, and there is no separate installation method.
By default, multiple plugins including Macvlan are copied to `/opt/cni/bin` on each node when the cluster is installed.
If no Macvlan binaries are found under `/opt/cni/bin` on the node,
you need to manually download [cni-plugins](https://github.com/containernetworking/plugins/releases/download/v1.1.1/cni-plugins-linux-amd64-v1.1.1.tgz),
and extract it to each node. When multus-underlay is installed, only the Multus network-attachment-definition CRD object belonging to Macvlan is created.

## Description

Multus + Macvlan generally has two use cases:

- Macvlan-standalone

    The type is Macvlan-standalone, which means that the first NIC (eth0) of the pod is the NIC allocated by Macvlan, by inserting the following field in the `annotations` of the pod:

    ```yaml
    annotations:
      v1.multus-cni.io/default-network: kube-system/macvlan-standalone-vlan0
    ```

    Note that Macvlan-standalone only works with Macvlan-standalone type, not with Macvlan-overlay. You can insert multiple Macvlan NICs into a pod in the following ways:

    ```yaml
    annotations:
      v1.multus-cni.io/default-network: kube-system/macvlan-standalone-vlan0
      k8s.v1.cni.cncf.io/networks: kube-system/macvlan-standalone-vlan0
    ```

- Macvlan-overlay

    This type means that for Macvlan-overlay CNI configurations (such as calico or cilium), Macvlan is not used as the default CNI for the pod, that is, it will not be the first NIC (eth0) of the pod.
    Therefore, pods of type Macvlan-overlay must communicate with pods of overlay type normally. You can assign an additional NIC to a pod in the following ways:

    ```yaml
    annotations:
      k8s.v1.cni.cncf.io/networks:kube-system/macvlan-overlay-vlan0
    ```

    !!!caution

        The value of `v1.multus-cni.io/default-network` cannot be a CRD of Macvlan-overlay type, that is, Macvlan-overlay cannot be used as the first NIC of a pod.

## Other

A common network scenario using Macvlan:

![](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/vlan.png)

As shown in the figure, combine two physical interfaces (ens224, ens256) on the host into a bond0,
and then create two VLAN sub-interfaces based on bond0, namely bond0.100 and bond0.200.
Then connect bond0 (that is, ens224 and ens256) to the switch trunk. And configure on the switch to
allow VLAN100 and VLAN200 to pass through.

Then create two instances of Macvlan-multus with different vlans, and their master interfaces are bond0.100 and bond0.200 respectively.
In this way, pods created using different Macvlan-multus instances also belong to different vlans. But they can all communicate with the same vlan or between different vlans through the switch.

!!! note

    Their network management should point to the proper VLANIF IP address of the switch.

This is a relatively common and slightly complex network topology. Summarize:

- Create bond and VLAN interfaces on the host
- Configure the switch
- Create multus CRD instance
- Create different Spiderpool IPPools
- Specify the proper instance and select the corresponding spiderpool IPPool in the annotations of the pod

To create interfaces such as bond and VLAN on the host, you can refer to [nmstat usage](nmstat.md).
