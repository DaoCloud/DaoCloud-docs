# Known Issues and Kernel Compatibility for Network Components

## kube-proxy

### IPVS Mode

#### Issue 1: 1-second delay or request failure when accessing services

Symptoms:

1. 1-second delay when accessing services through a Service.
2. Some requests fail during rolling updates of the application.

Impact:

| k8s Version | kube-proxy Behavior                                            | Corresponding Symptoms                                                                                                                                                                   |
|-------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <=1.17      | `net.ipv4.vs.conn_reuse_mode=0`                                | RealServer cannot be removed, causing some requests to fail during rolling updates of the application.                                                                                   |
| >=1.19      | `net.ipv4.vs.conn_reuse_mode=0` (kernel > 4.1)<br />`net.ipv4.vs.conn_reuse_mode=1` (kernel < 4.1) | CentOS 7.6-7.9 has a default kernel version below 4.1, causing a 1-second delay when accessing services through a Service.<br />CentOS 8 with a default kernel version above 4.1 faces RealServer removal issues during rolling updates. |
| >=1.22      | No change to `net.ipv4.vs.conn_reuse_mode` (kernel > 5.6)<br />`net.ipv4.vs.conn_reuse_mode=0` (kernel > 4.1)<br />`net.ipv4.vs.conn_reuse_mode=1` (kernel < 4.1) | CentOS 7.6-7.9 has a default kernel version below 4.1, causing a 1-second delay when accessing services through a Service.<br />CentOS 8 with a default kernel version above 4.1 faces RealServer removal issues during rolling updates.<br />Ubuntu 22.04 with a default kernel version 5.15 (higher than 5.9) does not face this issue. |

Recommendation:

IPVS mode is not recommended for systems with kernel versions lower than 5.9.

Reference:
* [Kubernetes Issue #93297](https://github.com/kubernetes/kubernetes/issues/93297)

### iptables Mode

#### Issue 1: Source port NAT randomness causing 1-second delay

Impact:

| Kernel | iptables Version | Corresponding Symptoms                    |
|--------|------------------|-------------------------------------------|
| < 3.13 | 1.6.2            | Source port NAT randomness causing a 1-second delay. |

Recommendation:

Upgrade the kernel based on the system distribution.

## Calico

#### Issue 1: Offload VXLAN causing access delay

Impact:

| Calico Version | Behavior                                                         | Impact                                                  |
|----------------|------------------------------------------------------------------|---------------------------------------------------------|
| <v3.20         | No handling                                                      | Kernel < 5.7, causing a 63-second delay between Pod and Service. |
| >=v3.20        | Configurable via `FelixConfiguration`, defaulting to disable VXLAN offload. | Low NIC performance, achieving only 1-2 Gbps/s.         |
| >=3.28         | VXLAN offload automatically enabled on kernel 5.7+, resolving previous ClusterIP packet loss issues and improving performance. | Kernel < 5.7, causing low NIC performance, achieving only 1-2 Gbps/s. |

Recommendation:

For versions of Calico with access delay issues, use `ethtool --offload vxlan.calico rx off tx off` to mitigate. Higher versions of Calico automatically disable VXLAN offload by default; customers needing higher network performance should upgrade the kernel to 5.7 to resolve the issue.

References:

* [Calico Issue #3145](https://github.com/projectcalico/calico/issues/3145)
* [Felix Pull Request #2811](https://github.com/projectcalico/felix/pull/2811)
