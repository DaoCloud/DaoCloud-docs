
# 端口要求

为了正常运行，需要打开一些端口。如果网络配置了防火墙规则，则需要确保基础设施组件可以通过特定端口相互通信。
确保所需的以下端口在网络上处于打开状态，并配置为允许主机之间的访问。某些端口是根据配置和用途可选的。

## 火种节点

| 协议 | 端口   | 描述     |
|----------|--------| ------------   |
| TCP      | 443    | Docker Registry |
| TCP      | 8081   | Chart Museum |
| TCP      | 9000   | Minio API  |
| TCP      | 9001   | Minio UI |

## Kube集群（包括全局集群和工作集群）

全局集群和工作集群都是通过 Kubean 部署的，因此他们需要打开同样的端口。
除了标准的 K8s 端口，对于 CNI 和部分网络组件，也需要打开端口。

### K8s 控制平面

| 协议 | 端口    | 描述     |
|----- |--------| ------------    |
| TCP  | 2379   | etcd client port|
| TCP  | 2380   | etcd peer port  |
| TCP  | 2381   | etcd metric port|
| TCP  | 6443   | kubernetes api  |
| TCP  | 10250  | kubelet api     |
| TCP  | 10257  | kube-scheduler  |
| TCP  | 10259  | kube-controller-manager  |

### 全部 K8s 节点

集群中的每一个节点都需要打开。

| 协议 | 端口   | 描述     |
|----- | ----- | ------------    |
| TCP  | 22         | ssh for ansible |
| TCP  | 9100       | node exporter (Insight-Agent) |
| TCP  | 10250      | kubelet api     |
| TCP  | 30000-32767| kube nodePort range |

参考 [Kubernetes 端口和协议文档](https://kubernetes.io/zh-cn/docs/reference/networking/ports-and-protocols/)。

### Calico（默认）

默认使用 Calico 作为　CNI， **全部 K8s 节点** 都需要打开。

| 协议 | 端口   | 描述     |
|----------|--------    | ------------  |
| TCP      | 179        | Calico networking (BGP) |
| UDP      | 4789       | Calico CNI with VXLAN enabled |
| TCP      | 5473       | Calico CNI with Typha enabled  |
| UDP      | 51820      | Calico with IPv4 Wireguard enabled |
| UDP      | 51821      | Calico with IPv6 Wireguard enabled |
| IPENCAP / IPIP | -    | Calico CNI with IPIP enabled  |

参考 [Calico 网络要求文档](https://docs.tigera.io/calico/latest/getting-started/kubernetes/requirements#network-requirements)。

### MetalLB（默认）

当启用 MetalLB 建 VIP 时， **全部 K8s 节点** 都需要打开。

| 协议 | 端口   | 描述     |
|----------|--------    | ------------  |
| TCP/UDP  | 7472       | metallb metrics ports |
| TCP/UDP  | 7946       | metallb L2 operating mode |

### Cilium（可选）

如果使用 Cilium 作为 CNI， **全部 K8s 节点** 都需要打开。

| 协议 | 端口   | 描述     |
|----------|--------  | ------------  |
| TCP      | 4240     | Cilium Health checks (``cilium-health``)  |
| TCP      | 4244     | Hubble server  |
| TCP      | 4245     | Hubble Relay  |
| UDP      | 8472     | VXLAN overlay  |
| TCP      | 9962     | Cilium-agent Prometheus metrics  |
| TCP      | 9963     | Cilium-operator Prometheus metrics  |
| TCP      | 9964     | Cilium-proxy Prometheus metrics  |
| UDP      | 51871    | WireGuard encryption tunnel endpoint  |
| ICMP     | -        | health checks  |

参考 [Cilium 系统要求文档](https://docs.cilium.io/en/v1.13/operations/system_requirements/)。

### SpiderPool（可选）

如果使用 SpiderPool 作为 CNI， **全部 K8s 节点** 都需要打开。

| 协议 | 端口   | 描述     |
|----------|--------  | ------------  |
| TCP      | 5710     | SpiderPool Agent HTTP Server   |
| TCP      | 5711     | SpiderPool Agent Metrics       |
| TCP      | 5712     | SpiderPool Agent gops enabled  |
| TCP      | 5720     | SpiderPool Controller HTTP Server   |
| TCP      | 5721     | SpiderPool Controller Metrics       |
| TCP      | 5722     | SpiderPool Controller Webhook Port       |
| TCP      | 5723     | Spiderpool-CLI HTTP server port.  |
| TCP      | 5724     | SpiderPool Controller gops enabled  |

参考文档：[spiderpool-controller](https://github.com/spidernet-io/spiderpool/blob/main/docs/reference/spiderpool-controller.md)
及 [spiderpool-agent](https://github.com/spidernet-io/spiderpool/blob/main/docs/reference/spiderpool-agent.md)。

### KubeVIP（可选）

当启用 KubeVIP 建 Kube API VIP 时， **全部 Control Plane 节点** 都需要打开。

| 协议 | 端口   | 描述     |
|----------|--------    | ------------  |
| TCP  | 2112           | kube-vip metrics ports |

<!--
#### 其他 Addon, 如 kube-vip
-->

## 全局管理集群其他需要开放的端口

### Istio-Gateway VIP

| 协议 | 端口       | 描述   | 使用方 |
|----------|--------    | ------------  | ------- |
| TCP      | 80         | Istio-Gateway HTTP   | Web Browser or API Client |
| TCP      | 443        | Istio-Gateway HTTPS  | Web Browser or API Client |

### Insight VIP

| 协议 | 端口       | 描述   | 使用方 |
|----------|--------    | ------------  | -------  |
| TCP      | 8480       | Insight VIP for Metrics  | 所有节点 |
| TCP      | 9200       | Insight VIP for Log      | 所有节点 |
| TCP      | 4317       | Insight VIP for Trace    | 所有节点 |
| TCP      | 8006       | Insight VIP for AduitLog | 所有节点 |

## 工作集群其他需要开放的端口

工作集群需要开放 K8s API 的 6443 端口，给到全局管理集群访问。如果要是用部署功能，还要开放 22 端口，给全局集群访问。

| 协议 | 端口       | 描述   | 使用方 |
|----------|--------    | ------------  | ------- |
| TCP      | 22         | 各节点 SSH (for ansible) | 全局管理集群 |
| TCP      | 6443       | K8s API 访问入口(如VIP) |  全局管理集群 |

## 其他各产品需要开放的端口

### 镜像仓库

| 协议 | 端口       | 描述   | 使用方 |
|----------|--------    | ------------  | ------- |
| TCP      | 443        | 访问入口(如VIP) 的端口 | 所有节点 |

<!--
### 其他 Gproduct端口
-->
