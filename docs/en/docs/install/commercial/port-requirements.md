---
MTPE: windsonsea
date: 2024-05-11
---

# Port Requirements

To ensure proper operation, certain ports need to be opened. If firewall rules are configured on the network, it is necessary to ensure that the infrastructure components can communicate with each other through specific ports.
Ensure that the following ports are open on the network and configured to allow access between hosts. Some ports are optional depending on the configuration and usage.

## Bootstrap Node

| Protocol | Port   | Description |
|----------|--------| ------------   |
| TCP      | 443    | Docker Registry |
| TCP      | 8081   | Chart Museum |
| TCP      | 9000   | Minio API  |
| TCP      | 9001   | Minio UI |

## Kube Clusters (Including Global Cluster and Worker Cluster)

Both the global cluster and the worker cluster are deployed through Kubean, so they need to open the same ports.
In addition to the standard K8s ports, ports need to be opened for CNI and some network components.

### K8s Control Plane

| Protocol | Port    | Description |
|----- |--------| ------------    |
| TCP  | 2379   | etcd client port|
| TCP  | 2380   | etcd peer port  |
| TCP  | 6443   | kubernetes api  |
| TCP  | 10250  | kubelet api     |
| TCP  | 10257  | kube-scheduler  |
| TCP  | 10259  | kube-controller-manager  |

### All K8s Nodes

Each node in the cluster needs to open these ports.

| Protocol | Port   | Description |
|----- | ----- | ------------    |
| TCP   | 22         | ssh for ansible |
| TCP   | 9100       | node exporter (Insight-Agent) |
| TCP   | 10250      | kubelet api     |
| TCP   | 30000-32767| kube nodePort range |

Refer to the [Kubernetes Port and Protocol Documentation](https://kubernetes.io/docs/reference/networking/ports-and-protocols/).

### Calico (Default)

Calico is used as the CNI by default, and **all K8s nodes** need to open these ports.

| Protocol | Port   | Description |
|----------|--------| ------------  |
| TCP      | 179    | Calico networking (BGP) |
| UDP      | 4789   | Calico CNI with VXLAN enabled |
| TCP      | 5473   | Calico CNI with Typha enabled  |
| UDP      | 51820  | Calico with IPv4 Wireguard enabled |
| UDP      | 51821  | Calico with IPv6 Wireguard enabled |
| IPENCAP / IPIP | -    | Calico CNI with IPIP enabled  |

Refer to the [Calico Network Requirements Documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/requirements#network-requirements).

### MetalLB (Default)

When MetalLB is enabled to create VIPs, **all K8s nodes** need to open these ports.

| Protocol | Port   | Description |
|----------|--------| ------------  |
| TCP/UDP  | 7472   | metallb metrics ports |
| TCP/UDP  | 7946   | metallb L2 operating mode |

### Cilium (Optional)

If Cilium is used as the CNI, **all K8s nodes** need to open these ports.

| Protocol | Port   | Description |
|----------|--------| ------------  |
| TCP      | 4240   | Cilium Health checks (``cilium-health``)  |
| TCP      | 4244   | Hubble server  |
| TCP      | 4245   | Hubble Relay  |
| UDP      | 8472   | VXLAN overlay  |
| TCP      | 9962   | Cilium-agent Prometheus metrics  |
| TCP      | 9963   | Cilium-operator Prometheus metrics  |
| TCP      | 9964   | Cilium-proxy Prometheus metrics  |
| UDP      | 51871  | WireGuard encryption tunnel endpoint  |
| ICMP     | -      | health checks  |

Refer to the [Cilium System Requirements Documentation](https://docs.cilium.io/en/v1.13/operations/system_requirements/).

### SpiderPool (Optional)

If SpiderPool is used as the CNI, **all K8s nodes** need to open these ports.

| Protocol | Port   | Description |
|----------|--------| ------------  |
| TCP      | 5710   | SpiderPool Agent HTTP Server   |
| TCP      | 5711   | SpiderPool Agent Metrics       |
| TCP      | 5712   | SpiderPool Agent gops enabled  |
| TCP      | 5720   | SpiderPool Controller HTTP Server   |
| TCP      | 5721   | SpiderPool Controller Metrics       |
| TCP      | 5722   | SpiderPool Controller Webhook Port       |
| TCP      | 5723   | Spiderpool-CLI HTTP server port.  |
| TCP      | 5724   | SpiderPool Controller gops enabled  |

Refer to the documentation: [spiderpool-controller](https://github.com/spidernet-io/spiderpool/blob/main/docs/reference/spiderpool-controller.md)
and [spiderpool-agent](https://github.com/spidernet-io/spiderpool/blob/main/docs/reference/spiderpool-agent.md).

### KubeVIP (Optional)

When KubeVIP is enabled to create the Kube API VIP, **all Control Plane nodes** need to open these ports.

| Protocol | Port   | Description |
|----------|--------| ------------  |
| TCP      | 2112   | kube-vip metrics ports |

<!--
#### Other Addons, such as kube-vip
-->

## Other Ports to be Opened in the Global Management Cluster

### Istio-Gateway VIP

| Protocol | Port       | Description   | User |
|----------|--------    | ------------  | ------- |
| TCP      | 80         | Istio-Gateway HTTP   | Web Browser or API Client |
| TCP      | 443        | Istio-Gateway HTTPS  | Web Browser or API Client |

### Insight VIP

| Protocol | Port       | Description   | User |
|----------|--------    | ------------  | -------  |
| TCP      | 8480       | Insight VIP for Metrics  | All Nodes |
| TCP      | 9200       | Insight VIP for Log      | All Nodes |
| TCP      | 4317       | Insight VIP for Trace    | All Nodes |
| TCP      | 8006       | Insight VIP for AduitLog | All Nodes |

## Other Ports to be Opened in the Worker Cluster

The worker cluster needs to open port 6443 for K8s API access by the global management cluster. If the deployment function is used, port 22 also needs to be opened for access by the global cluster.

| Protocol | Port       | Description   | User |
|----------|--------    | ------------  | ------- |
| TCP      | 22         | SSH on each node (for ansible) | Global Management Cluster |
| TCP      | 6443       | K8s API access entry (such as VIP) |  Global Management Cluster |

## Other Ports to be Opened by Other Products

### Container Registry

| Protocol | Port       | Description   | User |
|----------|--------    | ------------  | ------- |
| TCP      | 443        | Port for access entry (such as VIP) | All Nodes |

<!--
### Other Gproduct Ports
-->
