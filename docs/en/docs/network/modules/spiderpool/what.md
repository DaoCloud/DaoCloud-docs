# What is Spiderpool

Spiderpool is an IP Address Management (IPAM) CNI plugin that assigns IP addresses for container cloud platforms.
Most overlay CNIs have a good implementation of IPAM. SpiderPool is primarily designed to work with Underlay CNIs
（such as [MacVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)、
[VLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan)、
[IPVLAN CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)）for fine-grained IP management.

Spiderpool works with any CNI plug-in that can interface with third-party IPAMs, especially those without the support of IPAMs,
including [SRI-OV](https://github.com/k8snetworkplumbingwg/sriov-cni),
[MacVLAN](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan),
[IPVLAN](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan),
[OVS-CNI](https://github.com/k8snetworkplumbingwg/ovs-cni), etc.
Some overlay CNIs come with their own IPAM , so Spiderpool is not intentionally designed for these cases, but still can be integrated with them.
