# Large-Scale Cluster Parameter Description

For large-scale deployments, refer to the following parameter configuration.

## Kubean Cluster Parameters

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
 
    ## etcd parameters

    etcd_deployment_type: kubeadm
    etcd_events_cluster_setup: true
    etcd_heartbeat_interval: 250
    etcd_election_timeout: 5000

    ## kube-controller-manager parameters
 
    kube_controller_node_monitor_grace_period: 20s
    kube_controller_node_monitor_period: 2s
    kube_kubeadm_controller_extra_args:
      kube-api-qps: 20
      kube-api-burst: 30
      concurrent-deployment-syncs: 5
      pvclaimbinder-sync-period: 15s

    ## kube-scheduler parameters
 
    kube_scheduler_config_extra_opts:
      percentageOfNodesToScore: 0 

    ## kube-apiserver parameters
 
    kube_apiserver_pod_eviction_not_ready_timeout_seconds: 30
    kube_apiserver_pod_eviction_unreachable_timeout_seconds: 30
    kube_apiserver_request_timeout: 1m0s
    kube_kubeadm_apiserver_extra_args:
      max-requests-inflight: 400

    ## kubelet parameters

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

    ## Cluster network
 
    kube_network_plugin: calico
    calico_cni_name: calico
    kube_pods_subnet: 10.233.64.0/18
    kube_network_node_prefix: 24
    kube_network_node_prefix_ipv6: 120
    kube_service_addresses: 10.233.0.0/18

    ## App network

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

## Large-Scale Deployment Parameters

| Category | Parameter | Value | Description |
| --- | ---- | -- | --- |
| Resource Distribution | foo_image_repo | url | Set to point to an intranet address or mirror site |
| | foo_download_url | url | Set to point to an intranet address or mirror site |
| | download_run_once | true/false | Set to `download_localhost: true` to download only once, then distribute from the Ansible control node to each target node |
| | download_localhost | true/false | Set to `download_localhost: true` to download only once, then distribute from the Ansible control node to each target node |
| | download_container | true/false | Set to `download_container: false` to avoid synchronizing large-scale images on different nodes |
| Core Cluster Components - etcd | etcd_events_cluster_setup | true/false | Set to true to store events in a separate dedicated etcd instance |
| | etcd_heartbeat_interval | Default 250, in milliseconds | Frequency at which the leader notifies the followers |
| | etcd_election_timeout | Default 5000, in milliseconds | Time a follower node waits before attempting to become the leader if it hasn't heard a heartbeat |
| Core Cluster Components - kube-controller-manager | kube_controller_node_monitor_grace_period | Default 40s | Time allowed for a node to be unresponsive before being marked as unhealthy; must be a multiple of `kubelet_status_update_frequency` |
| | kube_controller_node_monitor_period | Default 5s | Interval for synchronizing NodeStatus |
| | kube_kubeadm_controller_extra_args | Sub-elements | kube-api-qps: Default 20, QPS used for communication with kube-apiserver<br />kube-api-burst: Default 30, burst allowed when communicating with kube-apiserver<br />concurrent-deployment-syncs: Default 5, number of deployment objects allowed to sync concurrently. Other basic resources have similar parameters<br />pvclaimbinder-sync-period: Default 15s, interval for synchronizing PV and PVC |
| Core Cluster Components - kube-scheduler | kube_scheduler_config_extra_opts | Sub-elements | percentageOfNodesToScore: If the cluster size is 500 nodes and this value is 30, the scheduler stops looking for more feasible nodes after finding 150. When set to 0, a default percentage (5%-50% based on cluster size) of nodes will be scored. Use a low setting only if you prefer to select any schedulable node to run the Pod. |
| Core Cluster Components - kube-apiserver | kube_apiserver_pod_eviction_not_ready_timeout_seconds | Default 300 | Toleration seconds for notReady:NoExecute; by default, this time is added to each pod without this toleration |
| | kube_apiserver_pod_eviction_unreachable_timeout_seconds | Default 300 | Toleration seconds for unreachable:NoExecute; by default, this time is added to each pod without this toleration |
| | kube_apiserver_request_timeout | Default 1m0s | Can limit some large requests, such as certain resources in all namespaces |
| | kube_kubeadm_apiserver_extra_args | Sub-elements | max-requests-inflight: Default 400, limits the maximum number of ongoing non-mutating requests |
| Core Cluster Components - kubelet | kubelet_status_update_frequency | Default 10s | Frequency of reporting pod status to the apiserver; it is recommended to increase this value in large clusters |
| | kubelet_max_pods | Default 110 | Increases the maximum number of pods that can be created on each node |
| | kubelet_pod_pids_limit | - | Prevents or allows pods to use a large number of PIDs, range: [-1, 2^63-1] |
| | kubelet_cpu_manager_policy | - | Sets the CPU manager policy |
| | kubelet_cpu_manager_policy_options | - | Sets options for the CPU manager policy |
| | kubelet_topology_manager_policy | - | Sets the topology manager policy |
| | kubelet_topology_manager_scope | - | Sets the scope of the topology manager policy |
| | kube_reserved | true/false | Setting `kube_reserved: true` means allocating resources for non-Kubernetes components |
| | kube_master_cpu_reserved | - | |
| | kube_master_memory_reserved | - | |
| | system_reserved | true/false | Setting `system_reserved: true` means allocating resources for Kubernetes components |
| | system_master_cpu_reserved | - | |
| | system_master_memory_reserved | - | |
| | kubelet_config_extra_args | Sub-elements | kubeAPIQPS: Default 50, QPS used for communication with kube-apiserver<br />kubeAPIBurst: Default 100, burst allowed when communicating with kube-apiserver<br />serializeImagePulls: Default true, pulls only one image at a time<br />maxParallelImagePulls: Default nil, maximum number of parallel pulls; effective only when serializeImagePulls is false<br />volumeStatsAggPeriod: Default 1m, recommended to increase in cases of many volumes and high disk pressure |
| Kubeproxy | kube_proxy_mode | - | In scenarios with frequent service changes, `ipvs` performs better than `iptables`. Setting kube proxy mode to ipvs requires a Linux kernel version of 5.9 or higher. Note that Kube-Proxy IPVS also has some issues |
| Cluster Network Parameters | kube_pods_subnet | 10.233.64.0/18 | Increases the network allocation for pods |
| | kube_network_node_prefix | 24 | Increases the subnet range that each node can allocate to pods |
| | kube_network_node_prefix_ipv6 | 120 | Increases the subnet range that each node can allocate to pods |
| | kube_service_addresses | 10.233.0.0/18 | Increases the network allocation for K8s service ClusterIP |
| Application Stability | dns_replicas | - | Specifies the number of DNS service replicas |
| | dns_cpu_limit | - | Maximum CPU resources that each DNS service pod can use |
| | dns_cpu_requests | - | Minimum CPU resources that each DNS service pod can use |
| | dns_memory_limit | - | Maximum memory resources that each DNS service pod can use |
| | dns_memory_requests | - | Minimum memory resources that each DNS service pod can use |
| | enable_nodelocaldns | - | Setting `enable_nodelocaldns: true` allows pods to connect to a DNS (core-dns) cache agent running on the same node, avoiding the use of iptables DNAT rules and connection tracking |
| | kube_vip_enabled | - | Setting `kube_vip_enabled: true` provides a virtual IP and load balancer for the cluster, used for the control plane (to build a highly available cluster) and Kubernetes services of type LoadBalancer |
| | metrics_server_enabled | - | Setting `metrics_server_enabled: true` is a prerequisite for starting HPA |
| Others | retry_stagger | - | Increases the number of retry attempts for failed tasks |

## Recommendations for Different Scenarios

### Fast Update and Fast Reaction

**Parameter Settings:**

- `kubelet_status_update_frequency` set to 4s
- `kube_controller_node_monitor_period` set to 2s (default 5s)
- `kube_controller_node_monitor_grace_period` set to 20s (default 40s)
- `kube_apiserver_pod_eviction_unreachable_timeout_seconds` set to 30 (default 300s)

In this scenario, Pods will be evicted within 50 seconds because the node will be considered down
after 20 seconds, and `kube_apiserver_pod_eviction_not_ready_timeout_seconds` or
`kube_apiserver_pod_eviction_unreachable_timeout_seconds` will occur after 30 seconds.
However, this setup will impose a load on etcd, as each node will attempt to update its status every 2 seconds.

**If the environment has 1000 nodes, there will be 15000 node updates per minute, potentially requiring large etcd containers or even dedicated etcd nodes.**

### Medium Update and Average Reaction

**Parameter Settings:**

- `kubelet_status_update_frequency` set to 20s
- `kube_controller_node_monitor_grace_period` set to 2m
- `kube_apiserver_pod_eviction_not_ready_timeout_seconds` and `kube_apiserver_pod_eviction_unreachable_timeout_seconds` set to 60.

In this scenario, Kubelet will attempt every 20 seconds.
Therefore, the Kubernetes controller manager will take 6 * 5 = 30 attempts to consider the node unhealthy.
After 1 minute, it will evict all Pods. The total time before eviction is 3 minutes.

**This scenario is suitable for medium environments since 1000 nodes require 3000 etcd updates per minute.**

## Other Considerations

When deploying Calico or Canal, you can add `calico_rr` nodes in the Kubean host manifest,
which allows for quick recovery from host/network interruptions.
You need to configure the cluster_id (formatted as an IPv4 address).

**Host Manifest Example:**

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

- The attributes of the Ansible configuration file can be set in the ClusterOperation file
  of Kubean to configure concurrency and connection timeout.
    - Concurrency: `forks: 50`
    - Connection Timeout: `timeout: 600`
