# Known Network Component Issues and Kernel Compatibility

This page summarizes known issues with various network components that may have a significant impact on production environments, along with some recommendations and solutions.

## kube-proxy

### IPVS Mode - 1s Delay or Request Failure When Accessing Services

**Symptoms:**

1. 1-second delay when accessing services through a Service.
2. Some requests fail during rolling updates.

**Impact:**

| k8s Version | kube-proxy Behavior | Phenomenon |
| --- | --- | --- |
| <=1.17 | net.ipv4.vs.conn_reuse_mode=0 | RealServer cannot be removed, causing some requests to fail during rolling updates.|
| >=1.19 | net.ipv4.vs.conn_reuse_mode=0 (kernel > 4.1)<br />net.ipv4.vs.conn_reuse_mode=1 (kernel < 4.1) | CentOS 7.6-7.9, default kernel version below 4.1, experiencing a 1s delay when accessing services through a Service.<br />CentOS 8 default kernel 4.16 above 4.1, RealServer cannot be removed, causing some requests to fail during rolling updates.|
| >=1.22 | Do not modify net.ipv4.vs.conn_reuse_mode (kernel > 5.6)<br />net.ipv4.vs.conn_reuse_mode=0 (kernel > 4.1)<br />net.ipv4.vs.conn_reuse_mode=1 (kernel < 4.1) | CentOS 7.6-7.9, default kernel version below 4.1, experiencing a 1s delay when accessing services through a Service.<br />CentOS 8 default kernel 4.16 above 4.1, RealServer cannot be removed, causing some requests to fail during rolling updates. <br />Ubuntu 22.04 default kernel version 5.15, above 5.9 kernel, does not have this issue.|

**Recommendation:** For systems with kernels below 5.9, the use of IPVS mode is not recommended.

**Reference:** [Kubernetes Issue #93297](https://github.com/kubernetes/kubernetes/issues/93297)

### iptables Mode - Source Port NAT Not Random Enough, Causing 1s Delay

**Impact:**

| Kernel | iptables Version | Phenomenon |
| --- | --- | --- |
| < 3.13 | 1.6.2 | Source port NAT not random enough, causing 1s delay.|

**Recommendation:** Refer to system distribution version, upgrade kernel.

### externalIPs Not Working Under externalTrafficPolicy: Local

**Impact:**

1.26.0 <= Affected Versions < 1.30.0

**Recommendation:** Upgrade to 1.30.0

**Reference:**

https://github.com/kubernetes/kubernetes/pull/121919

### Delay in Service Endpoint Rule Updates

**Impact:**

1.27.0 <= Affected Versions < 1.30.0

**Recommendation:** Upgrade to 1.30.0

**Reference:**

https://github.com/kubernetes/kubernetes/pull/122204

### LoadBalancerSourceRanges Not Working in nftables Mode

**Recommendation:** Upgrade to 1.30.0

**Reference:**

https://github.com/kubernetes/kubernetes/pull/122614

### Iptables nft and legacy Mode Selection Issue

**Impact:**

| Version | Behavior | Impact |
| --- | --- | --- |
| <v1.18 | Uses iptables-legacy | Kube-proxy might not work. |
| >=v1.18 | Automatically calculated, prioritizes nft. | |

**Reference:**

https://github.com/kubernetes-sigs/iptables-wrappers/tree/master

## Calico

### Offload vxlan Causing Access Delay Issue

**Impact:**

| Calico Version | Behavior | Impact |
| --- | --- | --- |
| <v3.20 | Not handled | Kernel < 5.7, 63s delay between Pod and Service.|
| >=v3.20 | Can configure through FelixConfiguration, offload vxlan off by default. | Leads to low NIC performance, only capable of 1-2 Gbps/s.|
| >= 3.28 | Automatically enables vxlan offload on kernel 5.7, resolving previous issues with ClusterIP packet loss, improving performance. | Kernel < 5.7, leads to low NIC performance, only capable of 1-2 Gbps/s.|

**Recommendation:** For older versions of Calico with access delay issues, the command `ethtool --offload vxlan.calico rx off tx off` can be used as a workaround.

**Reference:**

* [Calico Issue #3145](https://github.com/projectcalico/calico/issues/3145)
* [Felix Pull Request #2811](https://github.com/projectcalico/felix/pull/2811)

### vxlan Parent Device Changed, Routes Not Updated

**Impact:**

| Calico Version | Behavior | Impact |
| --- | --- | --- |
| <v3.28.0 | Not handled | Route table not updated to use the new parent device, even after restarting felix, old routes cannot be cleaned. |
| >=v3.28.0 | VXLAN manager recreates the route table when the parent device changes. | None |

**Recommendation:** 

Upgrade to version v3.28.0.

**Reference:**

https://github.com/projectcalico/calico/pull/8279

### Cluster calico-kube-controllers Cache Out of Sync, Causing Memory Leak

**Recommendation:** 

Upgrade to version v3.26.0.

### IPIP Mode Pod Cross-Node Network Not Communicating

**Impact:**

| Calico Version | Behavior | Impact |
| --- | --- | --- |
| <v3.28.0 | Not handled | Due to `iptables --random-fully` and checksum incompatibility, cross-node network may not work on kernel < 5.7. |
| >=v3.28.0 | Checksum calculation disabled by default. | None |

**Recommendation:** 

Upgrade to version v3.28.0+. For lower versions, the command `ethtool -K tunl0 tx off` can be used to manually disable it.

**Reference:**

https://github.com/projectcalico/calico/pull/8031

### Iptables nft and legacy Mode Selection Issue

**Impact:**

| Calico Version | Behavior | Impact |
| --- | --- | --- |
| <v3.26.0 | Only supports manual specification, automatic calculation has logical issues. | Incorrect iptables mode selection may cause Service network anomalies. |
| >=v3.26.0 | Automatically calculated. | None |

**Recommendation:** 

Upgrade to version v3.26.0+. For lower versions, manually specify the `FELIX_IPTABLESBACKEND` variable, options are NFT or LEGACY.

**Reference:**

https://github.com/projectcalico/calico/pull/7111