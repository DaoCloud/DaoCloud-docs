# Deployment requirements

When deploying DCE 5.0, software planning, hardware planning, and network planning need to be done well.

## Operating System Requirements

| **Architecture** | **Operating System** | **Kernel Version**                          | Remarks (Installation Guide)                                     |
| ---------------- | -------------------- | -------------------------------------------- | ------------------------------------------------------- |
| AMD 64           | CentOS 7.X           | Kernel 3.10.0-1127.el7.x86_64 on an x86_64   | Recommended OS: CentOS 7.9<br />[Offline Installation of DCE 5.0 Enterprise](start-install.md) |
|                  | Redhat 8.X           | 4.18.0-305.el8.x86_64                        | Recommended OS: Redhat 8.4<br />[Offline Installation of DCE 5.0 Enterprise](start-install.md) |
|                  | Redhat 7.X           | 3.10.0-1160.e17.x86                          | Recommended OS: Redhat 7.9<br />[Offline Installation of DCE 5.0 Enterprise](start-install.md) |
| | Redhat 9.X | 5.14.0-284.11.1.e9_2.x86_64 | Recommended OS: Redhat 9.2<br />[Offline Installation of DCE 5.0 Enterprise](start-install.md)<br /> |
|                  | Ubuntu 20.04         | 5.10.104                                     | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |
|                  | UOS V20 (1020a)      | 5.4.0-125-generic                            | [Deploying DCE 5.0 Enterprise on UOS V20 (1020a)](../os-install/uos-v20-install-dce5.0.md) |
|                  | openEuler 22.03      | 5.10.0-60.18.0.50.oe2203.x86_64              | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |
|                  | Oracle Linux R9/R8 U1 | 5.15.0-3.60.5.1.el9uek.x86_64                | [Deploying DCE 5.0 Enterprise on Oracle Linux R9 U1](../os-install/oracleLinux-install-dce5.0.md) |
|                  | TencentOS Server 3.1 | 5.4.119-19.0009.14                           | [Deploying DCE 5.0 Enterprise on TencentOS Server 3.1](../os-install/TencentOS-install-dce5.0.md) |
| ARM 64           | Kylin OS V10 SP2     | 4.19.90-24.4.v2101.ky10.aarch64              | [Offline Installation of DCE 5.0 Enterprise](start-install.md) |

!!! note

    For operating systems not mentioned in the table above, please refer to the documentation [Other Linux Offline Deployment of DCE 5.0 Enterprise](../os-install/otherlinux.md) for installation and deployment instructions.

## Hardware Requirements

| **Type** | **Specific Requirements** |
| -------- | --------------------------- |
| CPU | No Oversubscription |
| Memory | No Oversold |
| HDD | IOPS > 500 Throughput >200 MB/s |

For resource requirements, please refer to [Preparation](./prepare.md)

## Network Requirements

### Network topology

Assuming that VIP is used as the load balancing method of the global cluster:

![Network-Topology](https://docs.daocloud.io/daocloud-docs-images/docs/install/commercial/images/Network-Topology.png)

### Network Requirements

| **Resources** | **Requirements** | **Instructions** |
| ----------------- | ---------- | -------------------- ----------------- |
| `istioGatewayVip` | 1 | If the load balancing mode is metallb, you need to specify a VIP for DCE UI and OpenAPI access |
| `insightVip` | 1 | If the load balancing mode is metallb, you need to specify a VIP for the insight data collection portal of the GLobal cluster, and the insight-agent of the sub-cluster can report data to this VIP |
| Network speed | 1000 M/s | Not less than Gigabit, 10 Gigabit is recommended. |
| Protocol | - | IPv6 is supported. |
| Reserved IP address segments | Two segments need to be reserved | for Pod (10.233.64.0/18 by default) and Service (10.233.0.0/18 by default). If it is already in use, you can customize other network segments to avoid IP address conflicts. |
| Route | - | The server has a default or route to 0.0.0.0. |
| NTP service address | 1~4 | Make sure your data center has an accessible NTP server IP address. |
| DNS service address | 1~2 | If your application needs DNS service, please be prepared to access the DNS server IP address. |

## Port requirements

In order To function properly, some ports need to be open. If your network is configured with firewall rules, you need to ensure that infrastructure components can communicate with each other over specific ports.
Make sure the required following ports are open on the network and configured to allow access between hosts. Some ports are optional based on configuration and usage.

### bootstrapping node

| Protocol | Port | Description |
|----------|--------| ------------|
| TCP | 443 | Docker Registry |
| TCP | 8081 |
| TCP | 9000 | Minio API |
| TCP | 9001 | Minio UI |

### Kube cluster (including global cluster and working cluster)

Both global and worker clusters are deployed via Kubean, so they need to open the same ports
In addition to standard k8s ports, ports also need to be opened for CNI and some network components.

#### k8s Control plane

| Protocol | Port | Description |
|----------|--------| ------------|
| TCP | 2379 | etcd client port|
| TCP | 2380 | etcd peer port |
| TCP | 6443 | kubernetes-api |
| TCP | 10250 | kubelet-api |
| TCP | 10257 | kube-scheduler |
| TCP | 10259 | kube-controller-manager |

#### All k8s nodes

Every node in the cluster needs to be turned on.

| Protocol | Port | Description |
|----------|-------- | ------------ |
| TCP | 22 | ssh for ansible |
| TCP | 9100 | node exporter(Insight-Agent) |
| TCP | 10250 | kubelet-api |
| TCP | 30000-32767 | kube nodePort range |

Reference: [Kubernetes Docs](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)

#### Calico (default)

By default, Calico will be used as CNI, so **all k8s nodes** need to be turned on.

| Protocol | Port | Description |
|----------|-------- | ------------ |
| TCP | 179 | Calico networking (BGP) |
| UDP | 4789 | Calico CNI with VXLAN enabled |
| TCP | 5473 | Calico CNI with Typha enabled |
| UDP | 51820 | Calico with IPv4 Wireguard enabled |
| UDP | 51821 | Calico with IPv6 Wireguard enabled |
| IPENCAP / IPIP | - | Calico CNI with IPIP enabled |

Reference: [Calico Docs](https://docs.tigera.io/calico/latest/getting-started/kubernetes/requirements#network-requirements)

#### MetalLB (default)

When enabling MetalLB to build a VIP, **all k8s nodes** need to be turned on.

| Protocol | Port | Description |
|----------|-------- | ------------|
| TCP/UDP | 7472 | metallb metrics ports |
| TCP/UDP | 7946 | metallb L2 operating mode |

#### Cilium (optional)

If you use Cilium as CNI, **all k8s nodes** need to be opened.

| Protocol | Port | Description |
|----------|-------- | ------------ |
| TCP | 4240 | Cilium Health checks (``cilium-health``) |
| TCP | 4244 | Hubble server |
| TCP | 4245 | Hubble Relay |
| UDP | 8472 | VXLAN overlay |
| TCP | 9962 | Cilium-agent Prometheus metrics |
| TCP | 9963 | Cilium-operator Prometheus metrics |
| TCP | 9964 | Cilium-proxy Prometheus metrics |
| UDP | 51871 | WireGuard encryption tunnel endpoint |
| ICMP | - | health checks |

Reference: [Cilium Docs](https://docs.cilium.io/en/v1.13/operations/system_requirements/)

#### SpiderPool (optional)

If SpiderPool is used as CNI, **all k8s nodes** need to be opened.

| Protocol | Port | Description |
|----------|-------- | ------------ |
| TCP | 5710 | SpiderPool Agent HTTP Server |
| TCP | 5711 | SpiderPool Agent Metrics |
| TCP | 5712 | SpiderPool Agent gops enabled |
| TCP | 5720 | SpiderPool Controller HTTP Server |
| TCP | 5721 | SpiderPool Controller Metrics |
| TCP | 5722 | SpiderPool Controller Webhook Port |
| TCP | 5723 | Spiderpool-CLI HTTP server port. |
| TCP | 5724 | SpiderPool Controller gops enabled |

Reference: [spiderpool-controller](https://github.com/spidernet-io/spiderpool/blob/main/docs/reference/spiderpool-controller.md) and [spiderpool-agent](https://github.com/spidernet-io/spiderpool/blob/main/docs/reference/spiderpool-agent.md)

#### KubeVIP - (optional)

When KubeVIP is enabled to create a Kube API VIP, **all Control Plane nodes** need to be opened.

| Protocol | Port | Description |
|----------|-------- | ------------ |
| TCP | 2112 | kube-vip metrics ports |

<!--
#### Other Addons, such as kube-vip
-->

### Global cluster Other ports that need to be opened

#### Istio-Gateway VIP

| Protocol | Port | Description | Used By |
|----------|-------- | ------------ | ------- |
| TCP | 80 | Istio-Gateway HTTP | Web Browser or API Client |
| TCP | 443 | Istio-Gateway HTTPS | Web Browser or API Client |

#### Insight VIP

| Protocol | Port | Description | Used By |
|----------|-------- | ------------ | ------- |
| TCP | 8480 | Insight VIP for Metrics | All Nodes |
| TCP | 9200 | Insight VIP for Log | All Nodes |
| TCP | 4317 | Insight VIP for Trace | All Nodes |
| TCP | 8006 | Insight VIP for AduitLog | All Nodes |

### Working cluster Other ports that need to be opened

The working cluster needs to open port 6443 of the k8s API to give access to the global management cluster. If you want to use the deployment function, you need to open port 22 for global cluster access.

| Protocol | Port | Description | Used By |
|----------|-------- | ------------ | ------- |
| TCP | 22 | Each node SSH (for ansible) | Global management cluster |
| TCP | 6443 | k8s API access entry (such as VIP) | global management cluster |

### Other products need to open ports

#### Container registry

| Protocol | Port | Description | Used By |
|----------|-------- | ------------ | ------- |
| TCP | 443 | Port of access portal (such as VIP) | All nodes |

<!--
### Other Gproduct ports
-->

## Client browser requirements

- Firefox **≥** 49
- Chrome **≥** 54
