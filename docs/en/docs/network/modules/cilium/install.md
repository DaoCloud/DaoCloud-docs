# Installation Arguments Configuration

This page describes the configuration of various arguments when installing Cilium with Kubean, as well as the enablement of the main features and related instructions.

## Prerequisites

To install Cilium in DCE 5.0, you need to select `cilium` for `Network Plugins` on the `Create Cluster`->`Network Configuration` page. For creating a cluster, see [create worker cluster](../../../kpanda/07UserGuide/Clusters/CreateCluster.md).

![cilium-install](../../images/cilium-install1.png)

## Argument configuration

If you need to configure more features for Cilium, you can install Cilium via Kubean. Add and fill in arguments as needed under `Advanced Configuration`->`Custom arguments` when installing Cilium using Kubean.

![cilium-arg](../../images/cilium-install2.png)

The following describes the configuration of each argument when installing Cilium with Kubean：

- Cilium data schema

    By default, the VXLAN tunnel mode is used, which is set by the following parameters:

    ```yaml
    cilium_tunnel_mode: vxlan
    ```

    Supported values ​​are "vxlan", "geneve" and "disabled", where "disabled" means use route mode.

- IPAM mode

    By default, "Cluster Scope" mode is used, which can be set by the following parameters:

    ```yaml
    cilium_ipam_mode: cluster-pool
    ```

    Supported values ​​include "cluster-pool", "kubernetes" and modes customized by major public clouds.

- IPV4 and IPV6

By default, IPV4 is used, which can be set by the following parameters:

```yaml
cilium_enable_ipv4: true
cilium_enable_ipv6: false # true enable IPV6
```

- cluster name

    The default Cilium cluster name is "default", which can be set by the following parameters:

    ```yaml
    cilium_cluster_name: default
    ```

- identity mode

    The "crd" mode is used by default, which can be set by the following parameters:

    ```yaml
    cilium_identity_allocation_mode: crd
    ```

    Supported values ​​are "crd" and "kvstore".

- Resource Limits

    The default values ​​are:

    ```yaml
    cilium_memory_limit: 500M
    cilium_cpu_limit: 500m
    cilium_memory_requests: 64M
    cilium_cpu_requests: 100m
    ```

    Users can make corresponding adjustments according to their own cluster conditions.

- Time for Cilium DaemonSet to be ready again

    It can be set by the following parameters:

    ```yaml
    cilium_rolling_restart_wait_retries_count: 30
    cilium_rolling_restart_wait_retries_delay_seconds: 10
    ```

- Monitor aggregation level

    By default, "medium" is used, which can be set by the following parameters:

    ```yaml
    cilium_monitor_aggregation: medium
    ```

    Supported values ​​are "none", "low", "medium", and "maximum".

    Generate a monitor notification when TCP which flags are monitored for the first time. And only takes effect when the aggregation level is "medium" or higher.

    It can be set by the following parameters:

    ```yaml
    cilium_monitor_aggregation_flags: "all"
    ```

- replace kube-proxy

    By default, no replacement is performed, and it can be turned on or off on the interface, or set through the following parameters:

    ```yaml
    cilium_kube_proxy_replacement: disabled
    ```

    Supported values ​​are "disabled", "strict", "probe", and "partial".

- Whether to do SNAT when traffic leaves the cluster

    Cilium by default does SNAT on IPv4 and IPv6 (if enabled) traffic leaving the cluster. It can be set by the following parameters:

    ```yaml
    cilium_enable_ipv4_masquerade: true
    cilium_enable_ipv6_masquerade: true
    ```

    The way to do SNAT uses "iptables" by default, and also supports "eBPF" mode, which is more efficient, but "eBPF" does not support IPv6.

    Can be set via the following parameters:

    ```yaml
    cilium_enable_bpf_masquerade: false
    ```

- Hubble

    Hubble is installed and enabled by default, and how to enable Hubble metrics. The indicators exposed by default are:

    ```yaml
    - dns
    - drop
    -tcp
    - flow
    - icmp
    - http
    ```

    It can be set through the following related parameters:

    ```yaml
    cilium_hubble_install: true # install hubble
    cilium_enable_hubble: true # enable hubble
    cilium_enable_hubble_metrics: true # enable metrics
    cilium_hubble_metrics: {} # metrics content
    cilium_hubble_tls_generate: true # Automatically update the hubble-relay certificate
    ```

- Automatic mount of cgroup2 file system

    By default, the automatic mounting function of the cgroup2 file system is enabled, and the default mounting path is "/run/cilium/cgroupv2".

    It can be set by the following parameters:

    ```yaml
    cilium_cgroup_auto_mount: true
    cilium_cgroup_host_root: "/run/cilium/cgroupv2"
    ```

- Bypass netfilter in the host namespace

    By default, netfilter in the host namespace is bypassed, which can be set by the following parameters:

    ```yaml
    cilium_enable_host_legacy_routing: true
    ```

- Enable remote node identity

    Remote node identity is enabled by default and can be set with the following parameters:

    ```yaml
    cilium_enable_remote_node_identity: true
    ```

- Custom parameters

    Kubespray supports limited Cilium parameters. If you want to enable configurations that Kubespray does not support, you can set them through the following parameters:

    ```yaml
    cilium_config_extra_vars:
      enable-endpoint-routes: true
    ```

- Kubespray supported parameters

    [Kubean](../../../community/kubean.md) calls Kubespray by default to install the cluster, see the following documentation:

    - [Install Cilium via Kubespray](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/cilium.md)
    - [Cilium default parameters](https://github.com/kubernetes-sigs/kubespray/blob/b289f533b3b49ecf03baf755bd18b2da48608b3f/roles/network_plugin/cilium/defaults/main.yml)