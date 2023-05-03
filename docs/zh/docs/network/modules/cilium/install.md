# 安装参数配置

本页说明使用 Kubean 安装 Cilium 时的各项参数配置，以及主要功能的开启情况和相关说明。

## 前提条件

1. 请确认 操作系统 Kernel 版本号\>= 4.9.17，推荐 5.10+

2. DCE 5.0 安装时，选择的网络 CNI 为 Cilium 
   在 DCE 5.0 中安装 Cilium，需要在`创建集群`—>`网络配置`页面下，`网络插件`选择 `cilium`。关于创建集群，请参阅[创建工作集群](../../../kpanda/user-guide/clusters/create-cluster.md)。

   ![](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/cilium-install1.jpg)

## 高级参数

如果用户需要为 Cilium 配置更多功能，可通过 Kubean 安装 Cilium。关于使用 Kubean 安装 Cilium 时的各项参数配置，请在`高级配置`—>`自定义参数`下根据需要添加并填写。

![cilium-arg](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/cilium-install2.png)

以下介绍使用 Kubean 安装 Cilium 时的各项参数配置：

- Cilium 数据模式

    默认使用 VXLAN 隧道模式，通过以下参数进行设置：

    ```yaml
    cilium_tunnel_mode: vxlan
    ```

    支持的值有 “vxlan”、“geneve” 及 “disabled”，其中 “disabled” 表示使用路由模式。

- IPAM 模式
    IPAM负责分配和管理网络端点（容器或其它）的IP地址。Cilium支持多种IPAM模式。默认使用 "Cluster Scope" 模式，可以通过以下参数进行设置：

    ```yaml
    cilium_ipam_mode: cluster-pool
    ```

    支持的值有 “cluster-pool”、“kubernetes” 及各大公有云定制的模式。

    1. `kubernetes`:  使用Kubernetes自带的 host-scope IPAM。地址分配委托给每个节点进行，per-node的 Pod CIDR存放在v1.Node中。

    2. `cluster-pool`:默认的 `IPAM` 模式，它分配`per-node`的Pod CIDR，并在每个节点上使用`host-scope`的分配器来分配IP地址。

       此模式和kubernetes 类似，区别在于后者在 v1.Node 资源中存储 per-node 的 Pod CIDR。

- IPV4 及 IPV6

    默认使用 IPV4，可以通过以下参数进行设置，如通过界面开启双栈开关，默认 IPv6 参数自动打开：

    ```yaml
    cilium_enable_ipv4: true
    cilium_enable_ipv6: false  # true 开启 IPV6
    ```

- 集群名称

    Cilium 集群的默认名称为 “default”，可以通过以下参数进行设置：

    ```yaml
    cilium_cluster_name: default
    ```

- 身份模式

    cilium id 存储结构，`crd` or `kvstore`，通常情况下直接使用 CRD 存储元信息会是一个更为便利的选择，不过在大规模集群下，拆分一组独立的 ETCD 给 cilium 单独使用会是一个更高效的选择。

    默认使用 “crd” 模式，可以通过以下参数进行设置：
    
    ```yaml
    cilium_identity_allocation_mode: crd
    ```


- 资源限制

    默认的值为：

    ```yaml
    cilium_memory_limit: 500M
    cilium_cpu_limit: 500m
    cilium_memory_requests: 64M
    cilium_cpu_requests: 100m
    ```

    用户可以根据自身集群情况进行相应的调整。

- Cilium DaemonSet 再次准备就绪的时间

    可以通过以下参数进行设置：

    ```yaml
    cilium_rolling_restart_wait_retries_count: 30
    cilium_rolling_restart_wait_retries_delay_seconds: 10
    ```

- 监控聚合级别

    默认使用 “medium”，可以通过以下参数进行设置：

    ```yaml
    cilium_monitor_aggregation: medium
    ```

    支持的值有 “none”、“low”、“medium” 及 “maximum”。

    第一次监控 TCP 标志时，会生成监视器通知，但是只有在聚合等级为 “medium” 或更高级别时生效。

    可以通过以下参数进行设置：

    ```yaml
    cilium_monitor_aggregation_flags: "all"
    ```

- 替换 kube-proxy

    默认不进行替换，可以在界面上开启或关闭，也可以通过以下参数进行设置：

    ```yaml
    cilium_kube_proxy_replacement: disabled
    ```

    支持的值有 “disabled”、“strict”、“probe” 及 “partial”。

- 当流量离开集群时是否做 SNAT

    Cilium 默认情况下会对离开集群的 IPv4、IPv6（若已开启）流量做 SNAT。可以通过以下参数进行设置：

    ```yaml
    cilium_enable_ipv4_masquerade: true
    cilium_enable_ipv6_masquerade: true
    ```

    做 SNAT 的方式默认使用 “iptables”，还支持 “eBPF” 模式。“eBPF” 模式更高效，但 “eBPF” 不支持 IPv6。

    可通过以下参数进行设置：

    ```yaml
    cilium_enable_bpf_masquerade: false
    ```

- Hubble

    默认安装并启用 Hubble。默认暴露的指标有：

    ```yaml
    - dns
    - drop
    - tcp
    - flow
    - icmp
    - http
    ```

    可通过以下相关参数进行设置：

    ```yaml
    cilium_hubble_install: true         # 安装 hubble
    cilium_enable_hubble: true          # 启用 hubble
    cilium_enable_hubble_metrics: true  # 开启 metrics
    cilium_hubble_metrics: {}           # metrics 内容
    cilium_hubble_tls_generate: true    # 自动更新 hubble-relay 证书
    ```

- cgroup2 文件系统的自动挂载

    默认启用 cgroup2 文件系统的自动挂载功能，默认挂载路径为 “/run/cilium/cgroupv2”。

    可以通过以下参数进行设置：

    ```yaml
    cilium_cgroup_auto_mount: true
    cilium_cgroup_host_root: "/run/cilium/cgroupv2"
    ```

- 绕过主机命名空间中的 netfilter

    默认绕过主机命名空间中的 netfilter，可以通过以下参数进行设置：

    ```yaml
    cilium_enable_host_legacy_routing: true
    ```

- 启用远程节点身份

    默认启用远程节点身份，可以通过以下参数进行设置：

    ```yaml
    cilium_enable_remote_node_identity: true
    ```

- 自定义参数

    Kubespray 支持的 Cilium 参数有限。如果要开启 Kubespray 不支持的配置，可通过以下参数进行设置：

    ```yaml
    cilium_config_extra_vars:
      enable-endpoint-routes: true
    ```

- Kubespray 支持的参数

    [Kubean](../../../community/kubean.md) 默认调用 Kubespray 来安装集群，参阅以下文档：

    - [通过 Kubespray 安装 Cilium](https://github.com/kubernetes-sigs/kubespray/blob/master/docs/cilium.md)
    - [Cilium 默认参数](https://github.com/kubernetes-sigs/kubespray/blob/b289f533b3b49ecf03baf755bd18b2da48608b3f/roles/network_plugin/cilium/defaults/main.yml)
