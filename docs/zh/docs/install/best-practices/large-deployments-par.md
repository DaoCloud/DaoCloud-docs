# 大规模集群参数说明

对于大规模部署，请考虑以下配置参数信息介绍。

## Kubean 集群配置参数文件示例

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster1-demo-vars-conf
  namespace: kubean-system
data:
  group_vars.yml: |
    gcr_image_repo: "gcr.m.daocloud.io"
    kube_image_repo: "k8s.m.daocloud.io"
    docker_image_repo: "docker.m.daocloud.io"
    quay_image_repo: "quay.m.daocloud.io"
    github_image_repo: "ghcr.m.daocloud.io"
 
    files_repo: "https://files.m.daocloud.io"
    kubeadm_download_url: "{{ files_repo }}/dl.k8s.io/release/{{ kubeadm_version }}/bin/linux/{{ image_arch }}/kubeadm"
    kubectl_download_url: "{{ files_repo }}/dl.k8s.io/release/{{ kube_version }}/bin/linux/{{ image_arch }}/kubectl"
    kubelet_download_url: "{{ files_repo }}/dl.k8s.io/release/{{ kube_version }}/bin/linux/{{ image_arch }}/kubelet"
    cni_download_url: "{{ files_repo }}/github.com/containernetworking/plugins/releases/download/{{ cni_version }}/cni-plugins-linux-{{ image_arch }}-{{ cni_version }}.tgz"
    crictl_download_url: "{{ files_repo }}/github.com/kubernetes-sigs/cri-tools/releases/download/{{ crictl_version }}/crictl-{{ crictl_version }}-{{ ansible_system | lower }}-{{ image_arch }}.tar.gz"
    etcd_download_url: "{{ files_repo }}/github.com/etcd-io/etcd/releases/download/{{ etcd_version }}/etcd-{{ etcd_version }}-linux-{{ image_arch }}.tar.gz"
    calicoctl_download_url: "{{ files_repo }}/github.com/projectcalico/calico/releases/download/{{ calico_ctl_version }}/calicoctl-linux-{{ image_arch }}"
    calicoctl_alternate_download_url: "{{ files_repo }}/github.com/projectcalico/calicoctl/releases/download/{{ calico_ctl_version }}/calicoctl-linux-{{ image_arch }}"
    calico_crds_download_url: "{{ files_repo }}/github.com/projectcalico/calico/archive/{{ calico_version }}.tar.gz"
    helm_download_url: "{{ files_repo }}/get.helm.sh/helm-{{ helm_version }}-linux-{{ image_arch }}.tar.gz"
    crun_download_url: "{{ files_repo }}/github.com/containers/crun/releases/download/{{ crun_version }}/crun-{{ crun_version }}-linux-{{ image_arch }}"
    kata_containers_download_url: "{{ files_repo }}/github.com/kata-containers/kata-containers/releases/download/{{ kata_containers_version }}/kata-static-{{ kata_containers_version }}-{{ ansible_architecture }}.tar.xz"
    runc_download_url: "{{ files_repo }}/github.com/opencontainers/runc/releases/download/{{ runc_version }}/runc.{{ image_arch }}"
    containerd_download_url: "{{ files_repo }}/github.com/containerd/containerd/releases/download/v{{ containerd_version }}/containerd-{{ containerd_version }}-linux-{{ image_arch }}.tar.gz"
    nerdctl_download_url: "{{ files_repo }}/github.com/containerd/nerdctl/releases/download/v{{ nerdctl_version }}/nerdctl-{{ nerdctl_version }}-{{ ansible_system | lower }}-{{ image_arch }}.tar.gz"
    cri_dockerd_download_url: "{{ files_repo }}/github.com/Mirantis/cri-dockerd/releases/download/v{{ cri_dockerd_version }}/cri-dockerd-{{ cri_dockerd_version }}.{{ image_arch }}.tgz"
    yq_download_url: "{{ files_repo }}/github.com/mikefarah/yq/releases/download/{{ yq_version }}/yq_linux_{{ image_arch }}"
 
    download_run_once: true
    download_localhost: true
    download_container: false
 
    ## etcd 参数

    etcd_deployment_type: kubeadm
    etcd_events_cluster_setup: true
    etcd_heartbeat_interval: 250
    etcd_election_timeout: 5000

    ## kube-controller-manager 参数
 
    kube_controller_node_monitor_grace_period: 20s
    kube_controller_node_monitor_period: 2s
    kube_kubeadm_controller_extra_args:
      kube-api-qps: 20
      kube-api-burst: 30
      concurrent-deployment-syncs: 5
      pvclaimbinder-sync-period: 15s

    ## kube-scheduler 参数
 
    kube_scheduler_config_extra_opts:
      percentageOfNodesToScore: 0 

    ## kube-apiserver 参数
 
    kube_apiserver_pod_eviction_not_ready_timeout_seconds: 30
    kube_apiserver_pod_eviction_unreachable_timeout_seconds: 30
    kube_apiserver_request_timeout: 1m0s
    kube_kubeadm_apiserver_extra_args:
      max-requests-inflight: 400

    ## kubelet 参数

    kubelet_status_update_frequency: 4s
    kubelet_max_pods: 110
    kubelet_pod_pids_limit: -1
    kubelet_cpu_manager_policy: static
    kubelet_cpu_manager_policy_options:
      full-pcpus-only: "true"
    kubelet_topology_manager_policy: single-numa-node
    kubelet_topology_manager_scope: container
    kubelet_config_extra_args:
      kubeAPIQPS: 50
      kubeAPIBurst: 100
      serializeImagePulls: false
      maxParallelImagePulls: 5
      volumeStatsAggPeriod: 1m
    kube_reserved: true
    kube_master_cpu_reserved: 1
    kube_master_memory_reserved: 2G
    system_reserved: true
    system_master_cpu_reserved: 1
    system_master_memory_reserved: 2G
    
    ## kubeproxy
 
    kube_proxy_mode: ipvs

    ## 集群网络
 
    kube_network_plugin: calico
    calico_cni_name: calico
    kube_pods_subnet: 10.233.64.0/18
    kube_network_node_prefix: 24
    kube_network_node_prefix_ipv6: 120
    kube_service_addresses: 10.233.0.0/18

    ## 应用网络

    dns_replicas: 3
    dns_cpu_limit: 300m
    dns_cpu_requests: 100m
    dns_memory_limit: 300Mi
    dns_memory_requests: 70Mi
    enable_nodelocaldns: true
 
    kube_vip_enabled: true
    kube_vip_controlplane_enabled: true
    kube_vip_arp_enabled: true
    kube_proxy_strict_arp: true
    kube_vip_address: 10.42.42.42

    metrics_server_enabled: true
    retry_stagger: 60
    cluster_id: 10.42.42.2
```

## 大规模部署相关参数说明

| 一级                                   | 参数                                                    | 值                 | 说明                                                         |
| -------------------------------------- | ------------------------------------------------------- | ------------------ | ------------------------------------------------------------ |
| 资源分发                               | foo_image_repo                                          | url                | 设置指向内网地址或镜像站                                     |
|                                        | foo_download_url                                        | url                | 设置指向内网地址或镜像站                                     |
|                                        | download_run_once                                       | true/false         | 设置为`download_localhost: true` 使仅下载一次，后续从anisble 控制节点分发至各目标节点 |
|                                        | download_localhost                                      | true/false         | 设置为`download_localhost: true` 使仅下载一次，后续从anisble 控制节点分发至各目标节点 |
|                                        | download_container                                      | true/false         | 设置为`download_container: false` ，避免大规模镜像在不同节点上同步 |
| 集群核心组件 - etcd                    | etcd_events_cluster_setup                               | true/false         | 设置为 true 后存储事件将到单独的专用 etcd 实例               |
|                                        | etcd_heartbeat_interval                                 | 默认250，单位毫秒  | leader 通知 followers 的频率。                               |
|                                        | etcd_election_timeout                                   | 默认5000，单位毫秒 | 调整 followers 节点在试图成为 leader 之前没有听到心跳的时间  |
| 集群核心组件 - kube-controller-manager | kube_controller_node_monitor_grace_period               | 默认 40 s          | 代表在将Node标记为不健康状态之前，允许运行Node无响应的时间；注意必须是`kubelet_status_update_frequency` 的N倍 |
|                                        | kube_controller_node_monitor_period                     | 默认 5 s           | 代表同步 NodeStatus 的周期                                   |
|                                        | kube_kubeadm_controller_extra_args                      | 子元素             | kube-api-qps：默认为 20，与kub-apiserver通信时使用的QPS<br />kube-api-burst：默认为 30，与kube-apiserver信时允许的burst<br />concurrent-deployment-syncs：默认为 5，允许并发同步的deployment对象的数量。其他基础资源具有类似参数<br />pvclaimbinder-sync-period：默认为 15s，同步PV和PVC的周期 |
| 集群核心组件 - kube-scheduler          | kube_scheduler_config_extra_opts                        | 子元素             | percentageOfNodesToScore: 如果集群大小为 500 个节点，而该值为 30，那么调度程序在找到 150 个可行节点后，就会停止寻找更多可行节点。当值为 0 时，默认百分比（根据集群大小为 5%-50%）的节点将被计分。<br />只有当你更倾向于在可调度节点中任意选择一个节点来运行这个 Pod 时， 才使用很低的参数设置。 |
| 集群核心组件 -kube-apiserver           | kube_apiserver_pod_eviction_not_ready_timeout_seconds   | 默认 300           | 表示 notReady:NoExecute 容错的容错秒数，默认情况下，该容错秒数被添加到每个还没有容错的 pod 中。 |
|                                        | kube_apiserver_pod_eviction_unreachable_timeout_seconds | 默认 300           | 表示 unreachable:NoExecute 容忍度的容错秒数，默认情况下，该容忍度被添加到每个没有这种容忍度的pod中。 |
|                                        | kube_apiserver_request_timeout                          | 默认 1m0s          | 有时候可以限制住一些 巨大的请求 比如全命名空间的某些资源     |
|                                        | kube_kubeadm_apiserver_extra_args                       | 子元素             | max-requests-inflight：默认为400，限制正在运行的non-mutating请求的最大数量 |
| 集群核心组件 -kubelet                  | kubelet_status_update_frequency                         | 默认10s            | 上报 pod 状态至 apiserver 的频率，在集群node数量很大的时候，建议调大 |
|                                        | kubelet_max_pods                                        | 默认110            | 增大每个节点上能够创建的最大 pod 数                          |
|                                        | kubelet_pod_pids_limit                                  | -                  | 防止或允许 pod 使用较多的 pid，取值范围：[-1, 2的63次方-1]   |
|                                        | kubelet_cpu_manager_policy                              | -                  | 设置 CPU 管理器策略                                          |
|                                        | kubelet_cpu_manager_policy_options                      | -                  | 设置 CPU 管理器策略选型                                      |
|                                        | kubelet_topology_manager_policy                         | -                  | 设置拓扑管理器策略                                           |
|                                        | kubelet_topology_manager_scope                          | -                  | 设置拓扑管理器策略应用范围                                   |
|                                        | kube_reserved                                           | true/false         | 设置`kube_reserved: true`代表设置为非Kubernetes 组件配置资源 |
|                                        | kube_master_cpu_reserved                                | -                  |                                                              |
|                                        | kube_master_memory_reserved                             | -                  |                                                              |
|                                        | system_reserved                                         | true/false         | 设置`system_reserve: true`代表为 Kubernetes 组件配置资源     |
|                                        | system_master_cpu_reserved                              | -                  |                                                              |
|                                        | system_master_memory_reserved                           | -                  |                                                              |
|                                        | kubelet_config_extra_args                               | 子元素             | kubeAPIQPS：默认为50，与kub-apiserver通信时使用的QPS<br />kubeAPIBurst：默认为100，与kube-apiserver信时允许的burst<br />serializeImagePulls：默认为true，一次只拉取一个镜像<br />maxParallelImagePulls：默认为nil，最大并行拉取数，仅在 serializeImagePulls 为 false 时生效<br />volumeStatsAggPeriod：默认为1m，对于volume 比较多且磁盘压力大的情况，建议调大 |
| Kubeproxy                              | kube_proxy_mode                                         | -                  | 在 service 等变化频繁场景下 `ipvs` 性能比 `iptables` 好，设置 kube proxy 底座为 ipvs 时需要Linux 内核版本大于等于5.9，另外 Kube-Proxy IPVS 目前也存在一些问题     |
| 集群网络相关参数                       | kube_pods_subnet                                        | 10.233.64.0/18     | 增大 Pod 所能分配的网络                                      |
|                                        | kube_network_node_prefix                                | 24                 | 增大每个节点上 Pod 所能获得的子网范围                        |
|                                        | kube_network_node_prefix_ipv6                           | 120                | 增大每个节点上 Pod 所能获得的子网范围                        |
|                                        | kube_service_addresses                                  | 10.233.0.0/18      | 增大 K8s service ClusterIP 所能分配的网络                    |
| 应用稳定性                             | dns_replicas                                            | -                  | 指定 DNS 服务的副本数                                        |
|                                        | dns_cpu_limit                                           | -                  | 每个 DNS 服务 Pod 可以使用的最大 CPU 资源量                  |
|                                        | dns_cpu_requests                                        | -                  | 每个 DNS 服务 Pod 可以使用的最小 CPU 资源量                  |
|                                        | dns_memory_limit                                        | -                  | 每个 DNS 服务 Pod 可以使用的最大 Memory 资源量               |
|                                        | dns_memory_requests                                     | -                  | 每个 DNS 服务 Pod 可以使用的最小 Memory 资源量               |
|                                        | enable_nodelocaldns                                     | -                  | 设置 `enable_nodelocaldns: true`, 使 pod 与运行在同一节点上的 dns（core-dns）缓存代理建立联系，从而避免使用 iptables DNAT 规则和连接跟踪 |
|                                        | kube_vip_enabled                                        | -                  | 设置 `kube_vip_enabled: true` ，为集群提供虚拟IP和负载均衡器，用于控制平面(用于构建高可用性集群)和类型为LoadBalancer的Kubernetes服务。 |
|                                        | metrics_server_enabled                                  | -                  | 设置 `metrics_server_enabled: true` ，HPA 启动的必备条件     |
| 其他                                   | retry_stagger                                           | -                  | 增大任务失败重试次数                                         |

## 部分参数针对不同情况的一些建议

### 快速更新和快速反应

**参数设置：**

- `kubelet_status_update_frequency` 设置为 4s
-  `kube_controller_node_monitor_period` 设置为 2s（默认 5s）
- `kube_controller_node_monitor_period` 设置为 20s（默认 40s）。
- `kube_apiserver_pod_eviction_unreachable_timeout_seconds` 设置为 30（默认为 300 秒）。

在这种情况下，Pod 将在 50 秒内被驱逐，因为节点在 20 秒后将被视为已关闭，并且 `kube_apiserver_pod_eviction_not_ready_timeout_seconds` 或 `kube_apiserver_pod_eviction_unreachable_timeout_seconds` 会在 30 秒后发生。
然而，这种情况会在 etcd 上产生开销，因为每个节点都会尝试每 2 秒更新一次其状态。

**如果环境有 1000 个节点，则每分钟将有 15000 个节点更新，这可能需要大型 etcd 容器甚至 etcd 专用节点。**

### 中更新和平均反应（Medium Update and Average Reaction ）

**参数设置：**

- `kubelet_status_update_frequency` 设置为 20s
- `kube_controller_node_monitor_grace_period` 设置为 2m
- `kube_apiserver_pod_eviction_not_ready_timeout_seconds` 和 `kube_apiserver_pod_eviction_unreachable_timeout_seconds` 设置为 60。

在这种情况下，Kubelet 将尝试每隔 20 秒。因此，Kubernetes 控制器管理器需要 6 * 5= 30 次尝试才会考虑节点的不健康状态。
1m 后它将驱逐所有 Pod。驱逐过程之前的总时间为 3 分钟。

**这种场景适用于中等环境，因为 1000 个节点每分钟需要 3000 etcd 更新。**

## 其他注意事项

当部署 Calico 或 Canal 时，可以在 kubean 的主机清单文件中添加 `calico_rr` 节点，
通过 calico_rr 可以快速从主机/网络中断恢复。并需配置 cluster_id (格式为 ipv4 地址)。

**主机清单文件示例：**

```yaml
apiVersion: kubean.io/v1alpha1
kind: Cluster
metadata:
  name: cluster1-demo
spec:
  hostsConfRef:
    namespace: kubean-system
    name: cluster1-demo-hosts-conf
  varsConfRef:
    namespace: kubean-system
    name: cluster1-demo-vars-conf
---
apiVersion: v1
ind: ConfigMap
etadata:
 name: cluster1-demo-hosts-conf
 namespace: kubean-system
ata:
 hosts.yml: |
   all:
     hosts:
       node1:
         ansible_connection: ssh
         ansible_host: 10.42.42.2
         ansible_user: root
         ansible_ssh_pass: dangerous
        node2:
         ansible_connection: ssh
         ansible_host: 10.42.42.3
         ansible_user: root
         ansible_ssh_pass: dangerous
        node3:
         ansible_connection: ssh
         ansible_host: 10.42.42.4
         ansible_user: root
         ansible_ssh_pass: dangerous
     children:
       kube_control_plane:
         hosts:
           node1:
           node2:
           node3:
       kube_node:
         hosts:
           node1:
           node2:
           node3:
       etcd:
         hosts:
          node1:
          node2:
          node3:
       k8s_cluster:
         children:
           kube_control_plane:
           kube_node:
       calico_rr:
         hosts:
           node1:
           node2:
           node3:
```

- ansible 配置文件的属性设置，可以在 kubean 的 ClusterOperation 文件中配置并发数、连接超时时间

    - 并发数：`forks: 50`
    - 连接超时时间: `timeout: 600`
