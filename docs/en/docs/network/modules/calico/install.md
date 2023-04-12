# Installation Arguments Configuration

This page describes the configuration of various arguments when installing Calico with Kubespray.

## Prerequisites

To install Calico in DCE 5.0, you need to select `calico` for `Network Plugins` on the `Create Cluster`->`Network Configuration` page. For creating a cluster, see [create worker cluster](../../../kpanda/07UserGuide/Clusters/CreateCluster.md).



## Argument configuration

If you need to configure more features for Calico, you can install Calico via Kubespray. Add and fill in arguments as needed under `Advanced Configuration`->`Custom arguments` when installing Calico using Kubespray.



The following describes the configuration of each argument when installing Calico with Kubespray：

- `enable_dual_stack_networks`: If set to `true`, both IPv4 and IPv6 networks will be provided for pods and services.

    > It is recommended to enable it according to the actual situation, and it can be used as an installation ConfigMap.

- `ipv4_pools`: Default IPv4 address pools. Specified by `calico_pool_cidr` (not set by default, specified by the global variable `kube_pods_subnet`).

    > It is recommended to be consistent with `kube_pods_subnet`, which can expose ConfigMaps at installation time.

- `ipv6_pools`: Default IPv6 address pools. Specified by `calico_pool_cidr_ipv6` (not set by default, specified by the global variable `kube_pods_subnet_ipv6`).

    > It is recommended to be consistent with `kube_pods_subnet_ipv6`, which can expose ConfigMaps during installation.

- `calico_pool_blocksize`: The default blockSize of ippool(ipv4).

    By default, this field is undefined and controlled by the global variable `kube_pods_subnet`, which defaults to 24.

    > You can use the default configuration, but it must be set according to the size of the cluster. At least each node has a block, which can expose ConfigMaps during installation.

- `calico_pool_blocksize_ipv6`: The default blockSize of ippool(ipv6).

    Defined by `calico_pool_blocksize_ipv6`, defaults to 116.

    > You can use the default configuration, but it must be set according to the size of the cluster. At least each node has a block, which can expose ConfigMaps during installation.

- `calico_vxlan_mode`: Whether to enable VXLAN tunnel mode.

    Enabled by default. If there is no special requirement, VXLAN mode is enabled by default.

    > The ConfigMaps can be exposed during installation, the default is always.

- `calico_ipip_mode`: Whether to enable IPIP tunnel mode.

    Disabled by default. If there is no special requirement, VXLAN mode is enabled by default.

    > Can expose ConfigMaps during installation, the default is Never.

- `calico_felix_prometheusmetricsenabled`: Whether to expose felix metrics.

    It is closed by default, and you can decide whether to open it according to your needs.

    > Can expose ConfigMaps during installation, default false.

- `nat_outgoing`: Access across ippool pools, whether snat is required.

    Enabled by default, recommended to be enabled.

    > Can expose ConfigMaps during installation, default true.

- `calico_allow_ip_forwarding`: Whether to enable `ip_forwarding` in the container namespace.

    The default is false, and false is recommended.

    > It is not recommended as a basic ConfigMap, but can be used as an advanced ConfigMap.

- `calico_datastore`: Calico datastore engine, kdd or etcd.

    Default kdd, recommend kdd.

- `calico_iptables_backend`: `calico iptables backend mode` under CentOS 8.0 needs to be consistent with the host’s iptables mode.

    Configured by `calico_iptables_backend`, defaults to "Auto".

    > Only for CentOS 8.0.