#Macvlan

Macvlan is a network card virtualization solution for Linux, which can virtualize a physical network card into multiple virtual network cards.
With Mutus, one or more Macvlan NICs can be assigned to Pods, so that Pods can communicate with the outside world through macvlan NICs.

## Install

In Kubernetes, Macvlan is just a binary file stored under `/opt/cni/bin` of each node, and there is no separate installation method.
By default, multiple plugins including macvlan are copied to `/opt/cni/bin` on each node when the cluster is installed.
If no macvlan binaries are found under `/opt/cni/bin` on the node,
Then you need to manually download [cni-plugins](https://github.com/containernetworking/plugins/releases/download/v1.1.1/cni-plugins-linux-amd64-v1.1.1.tgz),
And extract it to each node. When multus-underlay is installed, only the Multus network-attachment-definition CRD object belonging to Macvlan is created.

## Illustrate

Multus + Macvlan generally has two usage scenarios:

-macvlan-standalone

    The type is `macvlan-standalone`, which means that the first network card (eth0) of the Pod is the network card allocated by macvlan, by inserting the following field in the `annotations` of the Pod:

    ```yaml
    annotations:
      v1.multus-cni.io/default-network: kube-system/macvlan-standalone-vlan0
    ```

    Note: macvlan-standalone only works with macvlan-standalone type, not with macvlan-overlay. You can insert multiple macvlan NICs into a Pod in the following ways:

    ```yaml
    annotations:
      v1.multus-cni.io/default-network: kube-system/macvlan-standalone-vlan0
      k8s.v1.cni.cncf.io/networks: kube-system/macvlan-standalone-vlan0
    ```

- macvlan-overlay

    This type means that macvlan is paired with an overlay type of CNI (such as calico or cilium), and macvlan is not used as the default CNI of the Pod, that is, it will not be the first network card (eth0) of the Pod.
    Therefore, Pods of type macvlan-overlay must communicate with Pods of overlay type normally. You can assign an additional NIC to a Pod in the following ways:

    ```yaml
    annotations:
      k8s.v1.cni.cncf.io/networks:kube-system/macvlan-overlay-vlan0
    ```

    !!!caution

        The value of `v1.multus-cni.io/default-network` cannot be a CRD of macvlan-overlay type, that is, macvlan-overlay cannot be used as the first NIC of a Pod.

## other

A common network scenario using macvlan:



As shown in the figure, combine two physical interfaces (ens224, ens256) on the host into a bond0, and then create two VLAN sub-interfaces based on bond0, namely bond0.100 and bond0.200.
Then connect bond0 (that is, ens224 and ens256) to the switch trunk. And configure on the switch to allow vlan100 and vlan200 to pass through.

Then create two instances of macvlan multus with different vlans, and their master interfaces are bond0.100 and bond0.200 respectively.
In this way, Pods created using different macvlan multus instances also belong to different vlans. But they can all communicate with the same vlan or between different vlans through the switch.

Note: Their network management should point to the corresponding vlanif IP address of the switch.

This is a relatively common and slightly complex network topology. Summarize:

- Create bond and vlan interfaces on the host
- Configure the switch
- Create multus CRD instance
- Create different Spiderpool IP pools
- Specify the corresponding instance and select the corresponding spiderpool IP pool in the annotations of the Pod

To create interfaces such as bond and vlan on the host, you can refer to [nmstat usage](nmstat.md).