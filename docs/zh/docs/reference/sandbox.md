# Application contact emails

a@daocloud.io, b@daocloud.io

# Project Summary

Spiderpool: An IP Address Management (IPAM) CNI plugin of Kubernetes for managing static IP addresses in underlay networks

# Project Description

Why Spiderpool? Despite the increasing demand for IP Address Management (IPAM) solutions,
there has yet to be a comprehensive, user-friendly, and intelligent open-source solution
that meets the needs of underlay networks. That's where Spiderpool comes in - to eliminate
the complexity of allocating IP addresses to underlay networks.

With the goal of making IP allocation as simple as some overlay-network CNI, Spiderpool
offers a variety of features such as static application IP addresses, dynamic scalability
of IP addresses, multi-NIC, and dual-stack support.

Overall, Spiderpool aims to simplify IPAM operations and make them more efficient for
underlay networks. By providing a user-friendly interface and intelligent allocation features,
it will allow network administrators to allocate and manage IP addresses with ease.

We believe that Spiderpool has the potential to be a game-changer for open-source enthusiasts
who are looking for a comprehensive and reliable IPAM solution. With its advanced functionality
and simplicity in mind, we are confident that Spiderpool will be a valuable addition to any underlay network.

Spiderpool can work well with any CNI project that is compatible with third-party IPAM plugins, such as:

- [macvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan)
- [vlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan)
- [ipvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan)
- [SR-IOV CNI](https://github.com/k8snetworkplumbingwg/sriov-cni)
- [ovs CNI](https://github.com/k8snetworkplumbingwg/ovs-cni)
- [Multus CNI](https://github.com/k8snetworkplumbingwg/multus-cni)
- [calico CNI](https://github.com/projectcalico/calico)
- [weave CNI](https://github.com/weaveworks/weave)

## Features

Spiderpool provides many exciting features to support:

- Multiple subnet objects

  The administrator can create multiple subnet objects that map to each underlay CIDR.
  This allows applications to be assigned IP addresses within different subnets, which
  helps to accommodate the complex planning of underlay networks.
  See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/multi-interfaces-annotation.md) for more details.

- Automatical ippool for applications that require static IP addresses

  In order to assign static IP addresses, some open source projects require hardcoding
  them in the application's annotations. However, this approach is prone to operational
  errors and manual conflicts with IP addresses, resulting in higher IP management costs
  when scaling applications.

  By contrast, Spiderpool can automatically create, delete, scale up and down a dedicated
  IP pool with static IP addresses for individual applications, thereby minimizing the
  effort required for operations. This method also helps to manage IP addresses more
  efficiently, especially when applications need frequent scaling. By automating the process,
  it eliminates the need for manual intervention and reduces the overall cost of IP management.

  - For stateless applications, the IP address range can be automatically fixed and IP resources
    can be dynamically scaled according to the number of application replicas.
    See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/spider-subnet.md) for more details.

  - For stateful applications, IP addresses can be automatically fixed for each pod, and the
    overall IP scaling range can be fixed as well. Also, IP resources can be dynamically scaled
    according to the number of application replicas.
    See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/statefulset.md) for more details.

  - The dedicated IP pool can include some redundant IP addresses,
    which enable applications to perform a rolling update while creating new pods.

  - Support for third-party application controllers. See
    [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/third-party-controller.md) for details.

- Manual IP pooling is available for applications that require static IP addresses but
  where the administrator needs to manually specify the IP address. See
  [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/ippool-affinity-pod.md) for details.

- For applications not requiring static IP addresses, they can share an IP pool.
  See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/ippool-multi.md) for details

- For an application with pods running on nodes accessing different underlay subnets,
  Spiderpool can assign IP addresses within different subnets. See
  [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/ippool-affinity-node.md) for details.

- Multiple IP pools can be set for a pod for the usage of backup IP resources.
  See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/ippool-multi.md) for details

- Set global reserved IPs that will not be assigned to pods, it can avoid to misuse IP addresses
  already used by other network hosts. See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/reserved-ip.md) for details.

- Spiderpool can specify different subnets for each NIC when assigning multiple NICs to
  a pod with [Multus CNI](https://github.com/k8snetworkplumbingwg/multus-cni).
  See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/multi-interfaces-annotation.md) for details.

- IP pools can be shared by whole cluster or bound to a specific namespace.
  See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/ippool-affinity-namespace.md) for details.

- Spiderpool also provides an additional plugin [veth](https://github.com/spidernet-io/plugins) to:

  - help some CNI addons to access clusterIP and perform pod-health check,
    such as [macvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan),
    [vlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan),
    [ipvlan CNI](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan),
    [SR-IOV CNI](https://github.com/k8snetworkplumbingwg/sriov-cni),
    [ovs CNI](https://github.com/k8snetworkplumbingwg/ovs-cni).
    See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/get-started-macvlan.md) for details.

  - help coordinate routes for each NIC in pods that have multiple NICs assigned by
    [Multus](https://github.com/k8snetworkplumbingwg/multus-cni).
    See [an example](https://github.com/windsonsea/spiderpool/blob/main/docs/usage/multi-interfaces-annotation.md) for details.

- Private IPv4 addresses are scarce, but Spiderpool provides a reasonable IP recycling mechanism,
  especially for running new pods when nodes or old pods are abnormal. See
  [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/gc.md) for details.

- An administrator can specify customized route with Spiderpool.
  See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/route.md) for details.

- Efficient performance in assigning and releasing Pod IPs ensures smooth application release and disaster recovery for the cluster.
  See [an example](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/performance.md) for details.

- All above features can work in ipv4-only, ipv6-only, and dual-stack scenarios.
  See [example](https://github.com/windsonsea/spiderpool/blob/main/docs/usage/ipv6.md) for details.

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

We are actively working on a longer-term roadmap which should be available in the next 30 days. For now we have a near-term roadmap.

# Contributing Guide

https://github.com/spidernet-io/spiderpool/blob/main/docs/develop/contributing.md

# Code of Conduct (CoC)

https://github.com/spidernet-io/spiderpool/blob/main/docs/develop/CODE-OF-CONDUCT.md

# Maintainers file

https://github.com/spidernet-io/spiderpool/blob/main/MAINTAINERS.md

# Why CNCF?

The Cloud Native Computing Foundation (CNCF) is the vendor-neutral, open-source hub of cloud-native computing
that has become an essential project in promoting cloud-native technology. The Spiderpool community fully supports CNCF's vision.

- Being an ecosystem project of CNCF can increase awareness of the Spiderpool project and
  Spiderpool can enable more CNI solutions to benefit more people with underlying network needs.
- With the guidance of CNCF, Spiderpool can adhere to its requirements and set goals in the right direction.

# Benefit to the Landscape

We believe that our community will contribute significantly to the advancements in CNI add-ons.

- Currently, there is no pure IPAM CNI project in the landscape.
  Spiderpool could help many of the main CNI addons to manage IP addresses,
  especially for CNIs without IPAM capabilities,
  such as [vlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan),
  [ipvlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan),
  [SR-IOV](https://github.com/k8snetworkplumbingwg/sriov-cni),
  [ovs](https://github.com/k8snetworkplumbingwg/ovs-cni),
  [macvlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan),

- In the CNI open-source community, there are few projects that help solve underlay network requirements.
  The IPAM needs for underlay networks are more complex than those for overlay networks. For example, pods
  may require static IP addresses for firewall reasons. Additionally, private IPv4 addresses are scarce,
  and Spiderpool must release IP addresses taken by abnormal pods to make them available for new pods.
  Therefore, Spiderpool is unique in that all its features are primarily designed for underlay networks.
  Its design is based on best practices in production environments.

- Before the Spiderpool project was launched, we had developed a similar private IPAM project.
  The idea and design of Spiderpool were based on our extensive experience in production environments.
  Spiderpool has been available for approximately one year, and it has proven to be both practical and stable.

# Cloud Native 'Fit'

Spiderpool adheres to the [CNI Specification](https://github.com/containernetworking/cni/blob/main/SPEC.md)
and assigns IP addresses to the main CNI addons. Using a custom resource definition (CRD) and operator design,
all requests and information are saved in the CR instance. This allows for effective management of IP address
allocation, ensuring that addresses are used efficiently and conflicts are avoided.

# Cloud Native 'Integration'

Spiderpool can assign IP addresses to any main CNI addon that can use third-party IPAM addons.
It is specifically designed for underlay network use and works well in cooperation with CNI addons
like [macvlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/macvlan),
[calico BGP mode](https://github.com/projectcalico/calico),
[weave](https://github.com/weaveworks/weave),
[vlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/vlan),
[ipvlan](https://github.com/containernetworking/plugins/tree/main/plugins/main/ipvlan),
[SR-IOV](https://github.com/k8snetworkplumbingwg/sriov-cni),
[ovs](https://github.com/k8snetworkplumbingwg/ovs-cni),
[Multus](https://github.com/k8snetworkplumbingwg/multus-cni).

Spiderpool offers extensive [usage documentation](https://github.com/spidernet-io/spiderpool/tree/main/docs/usage)
that demonstrates how to solve underlay network problems by integrating with various CNI addons.

Spiderpool's documentation offers clear guidance on best practices for managing IP address allocation
in complex container network environments. Users can learn how to set up Spiderpool with different
CNI plugins and configure it to meet their specific needs, ensuring that they can effectively manage
their container networks regardless of the container orchestration platform they are using.

# Cloud Native Overlap

At this time, we do not believe that there is significant overlap between Spiderpool and other CNCF projects.
However, we do address some of the same areas that other projects are investigating in the space of configuration
management, scalable Kubernetes, and alternative object storage (e.g., Kine).

Spiderpool's focus on IP address allocation and management complements other container networking projects
and can be used in conjunction with them to improve overall container network efficiency and reliability.
By providing a flexible and scalable IPAM solution, Spiderpool helps to address common challenges in managing container networks at scale.

# Similar projects

[Whereabouts](https://github.com/k8snetworkplumbingwg/whereabouts) is an IPAM project, but not a landscape project.
Spiderpool differs from Whereabouts in several ways:

- Spiderpool can automatically assign static IP addresses to applications, whereas Whereabouts cannot.
- For stateful applications, Spiderpool can automatically fix IP addresses for each pod,
  while Whereabouts does not support this feature.
- When an application has pods running on nodes accessing different underlay subnets,
  Spiderpool can assign IP addresses within different subnets, but Whereabouts does not have this capability.
- Spiderpool has subnet and ippool CRD storage, while Whereabouts does not.
- Spiderpool supports assigning IP addresses in different subnets for multi-NIC cases, but Whereabouts does not.
- Spiderpool supports customized pod routing, while Whereabouts does not.

Overall, while both projects are focused on IP address management,
Spiderpool offers several features that distinguish it from Whereabouts
and make it a useful tool for managing container networks in complex environments.

# Product or Service to Project separation

N/A
