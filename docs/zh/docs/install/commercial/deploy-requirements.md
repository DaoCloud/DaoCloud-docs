
# 部署要求

部署 DCE 5.0 时需要先做好软件规划、硬件规划、网络规划。

## 操作系统要求

| **架构** | **操作系统**        | **内核版本**                               | 备注（安装指导文档）                    |
| -------- | ------------------- | ------------------------------------------ | -------------------------------- |
| AMD 64   | centos 7.X          | Kernel 3.10.0-1127.el7.x86_64 on an x86_64 | 操作系统推荐 CentOS 7.9<br />[离线安装 DCE 5.0 商业版](start-install.md) |
|          | Redhat 8.X          | 4.18.0-305.el8.x86_64                      | 操作系统推荐 Redhat 8.4<br />[离线安装 DCE 5.0 商业版](start-install.md) |
|          | Redhat 7.X          | 3.10.0-1160.e17.x86                        | 操作系统推荐 Redhat 7.9<br />[离线安装 DCE 5.0 商业版](start-install.md) |
| | Redhat 9.X | 5.14.0-284.11.1.e9_2.x86_64 | 操作系统推荐 Redhat 9.2<br />[离线安装 DCE 5.0 商业版](start-install.md)<br /> |
|          | Ubuntu 20.04        | 5.10.104                                   | [离线安装 DCE 5.0 商业版](start-install.md) |
|          | 统信 UOS V20 （1020a） | 5.4.0-125-generic                          | [UOS V20 (1020a) 操作系统上部署 DCE 5.0 商业版](../os-install/uos-v20-install-dce5.0.md) |
|          | openEuler 22.03     | 5.10.0-60.18.0.50.oe2203.x86_64            | [离线安装 DCE 5.0 商业版](start-install.md) |
| | Oracle Linux R9/R8 U1 | 5.15.0-3.60.5.1.el9uek.x86_64 | [Oracle Linux R9 U1 操作系统上部署 DCE 5.0 商业版](../os-install/oracleLinux-install-dce5.0.md) |
| | TencentOS Server 3.1 | 5.4.119-19.0009.14 | [TencentOS Server 3.1 操作系统上部署 DCE 5.0 商业版](../os-install/TencentOS-install-dce5.0.md) |
| ARM 64   | 银河麒麟 OS V10 SP2 | 4.19.90-24.4.v2101.ky10.aarch64            | [离线安装 DCE 5.0 商业版](start-install.md) |

!!! note

    非上述表中声明的操作系统，可以参考文档 [Other Linux 离线部署 DCE 5.0 商业版](../os-install/otherlinux.md) 进行安装部署。

## 硬件要求

| **类型** | **具体要求**                |
| -------- | --------------------------- |
| CPU      | 不得超售                    |
| 内存     | 不得超售                    |
| 硬盘     | IOPS > 500 吞吐量 >200 MB/s |

资源要求，可以参考[准备工作](./prepare.md)

## 网络要求

### 网络拓扑

假设使用 VIP 作为全局集群的负载均衡方式：

![Network-Topology](https://docs.daocloud.io/daocloud-docs-images/docs/install/commercial/images/Network-Topology.png)

### 网络要求

| **资源**          | **要求**   | **说明**                              |
| ----------------- | ---------- | ------------------------------------- |
| `istioGatewayVip` | 1 个       | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 DCE 的 UI 界面和 OpenAPI 访问入口                                                   |
| `insightVip`      | 1 个       | 如果负载均衡模式是 metallb，则需要指定一个 VIP，供给 GLobal 集群的 insight 数据收集入口使用，子集群的 insight-agent 可上报数据到这个 VIP |
| 网络速率          | 1000 M/s   | 不低于千兆，建议万兆。                                                                                                                   |
| 协议              | -          | 支持 IPv6。                                                                                                                              |
| 保留 IP 地址段    | 需保留两段 | 供 Pod（默认 10.233.64.0/18） 和 Service （默认 10.233.0.0/18 使用）。如果已经在使用了，可以自定义其他网段避免 IP 地址冲突。             |
| 路由              | -          | 服务器有 default 或指向 0.0.0.0 这个地址的路由。                                                                                         |
| NTP 服务地址      | 1~4 个     | 确保您的数据中心有可以访问的 NTP 服务器 IP 地址。                                                                                        |
| DNS 服务地址      | 1~2 个     | 如果您的应用需要 DNS 服务，请准备可以访问 DNS 服务器 IP 地址。                                                                           |

## 端口要求

为了正常运行，需要打开一些端口。如果网络配置了防火墙规则，则需要确保基础设施组件可以通过特定端口相互通信。
确保所需的以下端口在网络上处于打开状态，并配置为允许主机之间的访问。某些端口是根据配置和用途可选的。

### 火种节点

| Protocol | Port   | Description     |
|----------|--------| ------------    |
| TCP      | 443    | Docker Registry  |
| TCP      | 8081   | Chart Museum
| TCP      | 9000   | Minio API  |
| TCP      | 9001   | Minio UI |

### Kube集群（包括 全局集群 和 工作集群）

全局集群 和 工作集群都是通过 Kubean 部署的，因此他们需要打开同样的端口
除了标准的 k8s 端口，对于 CNI 和 部分网络组件，也需要打开端口。

#### k8s Control plane

| Protocol | Port   | Description     |
|----------|--------| ------------    |
| TCP      | 2379   | etcd client port|
| TCP      | 2380   | etcd peer port  |
| TCP      | 6443   | kubernetes api  |
| TCP      | 10250  | kubelet api     |
| TCP      | 10257  | kube-scheduler  |
| TCP      | 10259  | kube-controller-manager  |

#### 全部 k8s 节点

集群中的每一个节点都需要打开。

| Protocol | Port       | Description     |
|----------|--------    | ------------    |
| TCP      | 22         | ssh for ansible |
| TCP      | 9100       | node exporter(Insight-Agent) |
| TCP      | 10250      | kubelet api     |
| TCP      | 30000-32767| kube nodePort range |

参考: [Kubernetes Docs](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)

#### Calico (默认)

默认情况下，会使用 Calico 作为　CNI , 因此 **全部 k8s 节点** 都需要打开。

| Protocol | Port       | Description   |
|----------|--------    | ------------  |
| TCP      | 179        | Calico networking (BGP) |
| UDP      | 4789       | Calico CNI with VXLAN enabled |
| TCP      | 5473       | Calico CNI with Typha enabled  |
| UDP      | 51820      | Calico with IPv4 Wireguard enabled |
| UDP      | 51821      | Calico with IPv6 Wireguard enabled |
| IPENCAP / IPIP | -    | Calico CNI with IPIP enabled  |

参考:  [Calico Docs](https://docs.tigera.io/calico/latest/getting-started/kubernetes/requirements#network-requirements)

#### MetalLB (默认)

当启用 MetalLB 建 VIP 的时候， **全部 k8s 节点** 都需要打开。

| Protocol | Port       | Description   |
|----------|--------    | ------------  |
| TCP/UDP  | 7472       | metallb metrics ports |
| TCP/UDP  | 7946       | metallb L2 operating mode |

#### Cilium (可选)

如果使用 Cilium 作为　CNI , 因此 **全部 k8s 节点** 都需要打开。

| Protocol | Port     | Description   |
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

参考: [Cilium Docs](https://docs.cilium.io/en/v1.13/operations/system_requirements/)

#### SpiderPool (可选)

如果使用 SpiderPool 作为　CNI , 因此 **全部 k8s 节点** 都需要打开。

| Protocol | Port     | Description   |
|----------|--------  | ------------  |
| TCP      | 5710     | SpiderPool Agent HTTP Server   |
| TCP      | 5711     | SpiderPool Agent Metrics       |
| TCP      | 5712     | SpiderPool Agent gops enabled  |
| TCP      | 5720     | SpiderPool Controller HTTP Server   |
| TCP      | 5721     | SpiderPool Controller Metrics       |
| TCP      | 5722     | SpiderPool Controller Webhook Port       |
| TCP      | 5723     | Spiderpool-CLI HTTP server port.  |
| TCP      | 5724     | SpiderPool Controller gops enabled  |

参考: [SpiderPool Docs](https://github.com/spidernet-io/spiderpool/blob/main/docs/concepts/config.md)

#### KubeVIP - (可选)

当启用 KubeVIP 建 Kube API VIP 的时候， **全部 Control Plane 节点** 都需要打开。

| Protocol | Port       | Description   |
|----------|--------    | ------------  |
| TCP  | 2112           | kube-vip metrics ports |

<!--
#### 其他 Addon, 如 kube-vip
-->

### 全局集群 其他 需要开放的端口

#### Istio-Gateway VIP

| Protocol | Port       | Description   | Used By |
|----------|--------    | ------------  | ------- |
| TCP      | 80         | Istio-Gateway HTTP   | Web Browser or API Client |
| TCP      | 443        | Istio-Gateway HTTPS  | Web Browser or API Client |

#### Insight VIP

| Protocol | Port       | Description   |  Used By |
|----------|--------    | ------------  | -------  |
| TCP      | 8480       | Insight VIP for Metrics  | 所有节点 |
| TCP      | 9200       | Insight VIP for Log      | 所有节点 |
| TCP      | 4317       | Insight VIP for Trace    | 所有节点 |
| TCP      | 8006       | Insight VIP for AduitLog | 所有节点 |

### 工作集群 其他 需要开放的端口

工作集群需要开放 k8s API 的 6443 端口，给到全局管理集群访问。如果要是用部署功能，还要开放 22 端口，给全局集群访问。

| Protocol | Port       | Description   | Used By |
|----------|--------    | ------------  | ------- |
| TCP      | 22         | 各节点 SSH (for ansible) | 全局管理集群 |
| TCP      | 6443       | k8s API 访问入口(如VIP) |  全局管理集群 |

### 其他各产品需要开放的端口

#### 镜像仓库

| Protocol | Port       | Description   | Used By |
|----------|--------    | ------------  | ------- |
| TCP      | 443        | 访问入口(如VIP) 的端口 | 所有节点 |

<!--
### 其他 Gproduct端口
-->

## 客户端浏览器的要求

- Firefox **≥** 49
- Chrome **≥** 54
