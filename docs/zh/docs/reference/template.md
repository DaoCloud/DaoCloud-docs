# Application contact emails

weizhou.lan@daocloud.io

# Project Summary

spiderpool: An IP Address Management (IPAM) CNI plugin of Kubernetes for managing static ip for underlay network

# Project Description

Why Spiderpool? Given that there has not yet been a comprehensive, user-friendly and intelligent open source solution for what underlay networks' IPAMs need, Spiderpool comes in to eliminate the complexity of allocating IP addresses to underlay networks.
With the hope of the operations of IP allocation being as simple as some overlay-network CNI, Spiderpool supports many features, such as static application IP addresses, dynamic scalability of IP addresses, multi-NIC, dual-stack support, etc.
Hopefully, Spiderpool will be a new IPAM alternative for open source enthusiasts.

Spiderpool can work well with any CNI project that is compatible with third-party IPAM plugins. such as:

* [macvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)

* [vlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan)

* [ipvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)

* [sriov CNI](https://github.com/k8snetworkplumbingwg/sriov-cni)

* [ovs CNI](https://github.com/k8snetworkplumbingwg/ovs-cni)

* [Multus CNI](https://github.com/k8snetworkplumbingwg/multus-cni)

* [calico CNI](https://github.com/projectcalico/calico)

* [weave CNI](https://github.com/weaveworks/weave)

there are much exciting features:

* Multiple subnet objects

  The administrator can create multiple subnets objects mapping to each underlay CIDR, and applications can be assigned IP addresses within different subnets. to meet the complex planning of underlay networks. See [example](./docs/usage/multi-interfaces-annotation.md) for more details.

* Automatical ippool for applications needing static ip

  To realize static IP addresses, some open source projects need hardcode IP addresses in the application's annotation, which is prone to operations accidents, manual operations of IP address conflicts, higher IP management costs caused by application scalability.
  Spiderpool could automatically create, delete, scale up and down a dedicated ippool with static IP address just for one application, which could minimize operation efforts.

    * For stateless applications, the IP address range can be automatically fixed and IP resources can be dynamically scaled according to the number of application replicas. See [example](./docs/usage/spider-subnet.md) for more details.

    * For stateful applications, IP addresses can be automatically fixed for each POD, and the overall IP scaling range can be fixed as well. And IP resources can be dynamically scaled according to the number of application replicas. See [example](./docs/usage/statefulset.md) for more details.

    * The dedicated ippool could have keep some redundant IP address, which supports application to performance a rolling update when creating new pods. See [example](./docs/usage/????) for more details.

    * Support for third-party application controllers. See [example](./docs/usage/third-party-controller.md) for details

* Manual ippool for applications needing static ip but the administrator expects specify IP address by hand. See [example](./docs/usage/ippool-affinity-pod.md) for details

* For applications not requiring static IP addresses, they can share an IP pool. See [example](./docs/usage/ippool-multi.md) for details

* For one application with pods running on nodes accessing different underlay subnet, spiderpool could assign IP addresses within different subnets. See [example](./docs/usage/ippool-affinity-node.md) for details

* Multiple IP pools can be set for a pod for the usage of backup IP resources. See [example](./docs/usage/ippool-multi.md) for details

* Set global reserved IPs that will not be assigned to Pods, it can avoid to misuse IP address already used by other network hosts. See [example](./docs/usage/reserved-ip.md) for details

* when assigning multiple NICs to a pod with [Multus CNI](https://github.com/k8snetworkplumbingwg/multus-cni), spiderpool could specify different subnet for each NIC. See [example](./docs/usage/multi-interfaces-annotation.md) for details

* IP pools can be shared by whole cluster or bound to a specified namespace. See [example](./docs/usage/ippool-affinity-namespace.md) for details

* An additional plugin [veth](https://github.com/spidernet-io/plugins) provided by spiderpool has features:

    * help some CNI addons be able to access clusterIP and pod-healthy check , such as [macvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan),
      [vlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan),
      [ipvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan),
      [sriov CNI](https://github.com/k8snetworkplumbingwg/sriov-cni),
      [ovs CNI](https://github.com/k8snetworkplumbingwg/ovs-cni). See [example](./get-started-macvlan.md) for details.

    * help coordinate routes of each NIC, for pods who has multiple NICs assigned by [Multus](https://github.com/k8snetworkplumbingwg/multus-cni). See [example](./docs/usage/multi-interfaces-annotation.md) for details

* Private IPv4 address is rare, spiderpool provides a reasonable IP recycling mechanism, especially for running new pods when nodes or old pods are abnormal. See [example](./docs/usage/gc.md) for details

* The administrator could specify customized route. See [example](./docs/usage/route.md) for details

* Good performance for assigning and release Pod IP, to guarantee the application release, to guarantee disaster recovery for the cluster. See [example](docs/usage/performance.md) for details

* All above features can work in ipv4-only, ipv6-only, and dual-stack scenarios. See [example](./docs/usage/ipv6.md) for details


# Org repo URL

https://github.com/spidernet-io

# Project repo URL

https://github.com/spidernet-io/spiderpool

# Additional repos

No response

# Website URL

https://spidernet-io.github.io/spiderpool/

# Roadmap

https://github.com/spidernet-io/spiderpool/blob/main/docs/develop/roadmap.md

# Roadmap context


# Contributing Guide

https://github.com/spidernet-io/spiderpool/blob/main/docs/develop/contributing.md

# Code of Conduct (CoC)

https://github.com/spidernet-io/spiderpool/blob/main/docs/develop/CODE-OF-CONDUCT.md

# Maintainers file

https://github.com/spidernet-io/spiderpool/blob/main/MAINTAINERS.md

# Why CNCF?

CNCF is the open source, vendor-neutral hub of cloud native computing, it has become a very import project helping popularize cloud native technology.
The spiderpool community deeply agrees with the CNCF's idea.

* To be a ecosystem project of CNCF, it could help increase the awareness of the project, and spiderpool could give a new CNI solution to benefit more people with underlay network needs.

* With the guidance of CNCF, spiderpool could follow its requirements, and set goals in right direction.
 
# Benefit to the Landscape

We believe our community will contribute significant advancements in CNI addon:

* Currently, there is no pure IPAM CNI project in the Landscape, spiderpool could help lots of main CNI addon to manage IP address, especially
   for CNI without IPAM abilility, such as [vlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan),
 [ipvlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan),
 [sriov](https://github.com/k8snetworkplumbingwg/sriov-cni),
 [ovs](https://github.com/k8snetworkplumbingwg/ovs-cni),
 [macvlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan),

* In the CNI opensource community, there is few project helping solve underlay network needs. 
    For the underlay network, the IPAM needs is more complex than overlay network. For example, the pod needs static IP for firewall reason.
    For example, the private IPv4 address is rare, and Spiderpool must help release IP address taken by abnormal pods for new pods. 
    So, spiderpool is very special, all features is mainly for underlay network, its design comes from best practice of product environment.

* Before open spiderpool project, we has a similar private IPAM project, so the idea and design of spiderpool comes from much experience of production environment.
  spiderpool project has been released about one year, and it is very practical and stable.

# Cloud Native 'Fit'

The spiderpool follows the [CNI Specification](https://github.com/containernetworking/cni/blob/main/SPEC.md) and assign IP address to main CNI addon.
Based on CRD and operator design, all request and information is saved in the CR instance

# Cloud Native 'Integration'

The Spiderpool could help assign IP address for any main CNI addon who could use third-party IPAM addon. Especially,Spiderpool is designed for underlay network use,
cooperating with CNI addon like [macvlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan),
 [calico BGP mode](https://github.com/projectcalico/calico),
 [weave](https://github.com/weaveworks/weave),
 [vlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan),
 [ipvlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan),
 [sriov](https://github.com/k8snetworkplumbingwg/sriov-cni),
 [ovs](https://github.com/k8snetworkplumbingwg/ovs-cni),
 [Multus](https://github.com/k8snetworkplumbingwg/multus-cni).

The Spiderpool has usage documentation showing how to solve underlay network problem integrating with these CNI addon:
xxxxxxxx

# Cloud Native Overlap

We do not think there is direct overlap at this time with other CNCF projects. However, we do touch on some of the areas that other projects are investigating in the space of configuration management, scalable kubernetes, and alternative object storage (kine).

# Similar projects

* [whereabout](https://github.com/k8snetworkplumbingwg/whereabouts) 
    it is a IPAM project , but not a landscape project. spiderpool has much differences with it:
    * spiderpool could automatically assign static IP to application, but whereabout does not
    * For stateful applications, IP addresses can be automatically fixed for each POD. Spiderpool does support but whereabout does not
    * For one application with pods running on nodes accessing different underlay subnet, spiderpool could assign IP addresses within different subnets. but whereabout does not
    * spiderpool have subnet and ippool CRD storage, but whereabout does not 
    * spiderpool support assign IP in different subnets for multi-Nic case, but whereabout does not
    * spiderpool support customize pod route, but whereabout does not

# Product or Service to Project separation

N/A

