# Spiderpool

The Spiderpool is an IP Address Management (IPAM) CNI plugin that assigns IP addresses for kubernetes clusters.

Any Container Network Interface (CNI) plugin supporting third-party IPAM plugins can use the Spiderpool,
such as [MacVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan),
[VLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan), [IPVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan) etc.
The Spiderpool also supports
[Multus CNI](https://github.com/k8snetworkplumbingwg/multus-cni)
case to assign IP for multiple interfaces.
More CNIs will be tested for integration with Spiderpool.

Most overlay CNIs, like
[Cilium](https://github.com/cilium/cilium)
and [Calico](https://github.com/projectcalico/calico),
have a good implementation of IPAM, so the Spiderpool is not intentionally designed for these cases, but maybe integrated with them.

The Spiderpool is specifically designed to use with underlay network, where administrators can accurately manage each IP.

[Go to Spiderpool repo](https://github.com/spidernet-io){ .md-button }

[Go to Spiderpool website](https://spidernet-io.github.io/spiderpool/){ .md-button }
