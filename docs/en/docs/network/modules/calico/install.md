# Installation arguments configuration

This page describes the configuration of various arguments when installing Calico with Kubespray.

## Prerequisites

To install Calico in DCE 5.0, you need to select `calico` for `Network CNIs` on the `Create Cluster`->`Network Settings` page. For creating a cluster, see [create worker cluster](../../../kpanda/user-guide/clusters/create-cluster.md).

![calico-install](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/calico-install-1.png)

## Argument configuration

In the third step of `Create Cluster`: `network configuration`, configure the following parameters:

- `Dual Stack`: enable dual stack with off mode by default. `enable_dual_stack_networks`: when enabled, IPv4 and IPv6 networks will be provided for pods and services.
    
- `Interface Mode`: Calico NIC detection mode. When selected, traffic will be communicated through this NIC.
    - `FIRST FOUND`: the default mode. Enumerate all node IPs (ignore some common local NICs like docker0, kube-ipvs0, etc.) and select the first address.
    - `KUBERNETES INTERNAL IP`: selects the first internal address in the Status.addresses field of the Node object.
    - `INTERFACE REGEX`: specifies the NIC by NIC name or regular expression.
- `Calico IPtables Backend`: Calico relies on IPtables to implement SNAT and network policies, and needs to be consistent with the host's IPtables mode, otherwise it may cause communication problems. It supports `Legacy`, `NFT`, and `Auto` modes, with `Legacy` mode by default. If you are using CentOS 8 / RHEL 8 / OracleLinux 8 series node system, please select NFT mode.
- `Tunnel Mode`: Calico supports two packet encapsulation modes: IPIP and VXLAN, and both support Always and CrossSubnet modes.
    - `VXLAN Always`: all cross-node packets will be encapsulated using VXLAN, regardless of whether the nodes are on the same segment, which satisfies most  use cases.
    - `VXLAN CrossSubnet`: cross-node packets are encapsulated only when the nodes are on different network segments.
    - `IPIP CrossSubnet`: cross-node packets are encapsulated only when the nodes are on different network segments.
    - `IPIP Always`: all cross-node packets are encapsulated using IPIP regardless of whether the nodes are on the same network segment, which satisfies most  use cases.
- `Pod CIDR`—>`IPv4 CIDR`: `kube_pods_subnet`, the same as `ipv4_pools` by default. The network segment used by the containers in a cluster determines the maximum number of containers in that cluster. It cannot be modified after creation. The default is 10.233.64.0/18.
- `Pod CIDR`—>`IPv6 CIDR`: `kube_pods_subnet_ipv6`, the same as `ipv6_pools` by default. The network segment used by the containers in a cluster determines the maximum number of containers in that cluster. It cannot be modified after creation. You need to enter this network segment information after opening the dual stack.
- `Service CIDR`: the segment of Service resources used by containers in the same cluster to access each other determines the upper limit of Service resources. It cannot be modified after creation. The default is 10.244.0.0/18.


The following describes the configuration of each parameter when installing Calico with Kubespray:

!!! Note 

    If you need to configure more features for Calico, you can install Calico via Kubespray. for the configuration of the parameters for Calico installation using Kubespray, please add and fill in as needed under `Advanced Settings`->`Custom Parameters`.
    ![calico-install](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/calico-install-2.png)

> It is recommended to turn on as appropriate and can be used as an installation configuration item.

- `calico_pool_blocksize`: the default blockSize of ippool(ipv4).

    By default, this field is undefined and controlled by the global variable `kube_pods_subnet`, which defaults to 24.

    > You can use the default configuration, but it must be set according to the size of the cluster. At least each node has a block, which can expose ConfigMaps during installation.

- `calico_pool_blocksize_ipv6`: the default blockSize of ippool(ipv6).

    Defined by `calico_pool_blocksize_ipv6`, and defaults to 116.

    > You can use the default configuration, but it must be set according to the size of the cluster. At least each node has a block, which can expose ConfigMaps during installation.

- `calico_felix_prometheusmetricsenabled`: exposes felix metrics.

    It is disabled by default, and you can decide whether to open it according to your needs.

    > You can expose ConfigMaps during installation. The default is false.

- `nat_outgoing`: accesses across ippools, whether snat is required.

    Enabled by default, and recommended to be enabled.

    > You can expose ConfigMaps during installation. The default is true.

- `calico_allow_ip_forwarding`: enables `ip_forwarding` in the container namespace.

    The default is false, and recommended to be enabled.

    > It is not recommended as a basic ConfigMap, but can be used as an advanced ConfigMap.

- `calico_datastore`: Calico datastore engine, kdd or etcd.

    The default is kdd, and recommended to be kdd.
