---
MTPE: WANG0608GitHub
date: 2024-07-16
---

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

## Spiderpool

**Recommendations:**

If you encounter the following problems, please try to update Spiderpool to a higher version to solve them.

### Known issues in v0.9

#### An error occurred during spidercoordinator synchronization, but its status remains running

If the cluster CIDR information failed to be obtained, we should update its status to NotReady, which will prevent the normal creation of Pods. Otherwise, Pods will run with incorrect CIDRs, which will cause network connectivity problems.

**References:**

https://github.com/spidernet-io/spiderpool/pull/2929

#### values.multus.multusCNI.uninstall function does not take effect, leading to improper deletion of multus resources 

After Values.multus.multusCNI.uninstall is set to true, after uninstalling Spiderpool, it is found that multus related resources still exist and they are not deleted as expected.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2974

#### When kubeadm-config is missing, serviceCIDR cannot be obtained from kubeControllerManager Pod

In some scenarios, kubeadm is not used to create a cluster, so there may be no kubeadm-config configMap. It will try to obtain it from kubeControllerManager. However, due to a bug, serviceCIDR cannot be obtained from kubeControllerManager Pod, resulting in the failure of Spidercoordinator status update.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/3020

#### Upgrading from v0.7.0 to v0.9.0 will cause a panic due to a new attribute in the SpiderCoordinator CRD

Spiderpool v0.9.0 adds a new attribute `TxQueueLen` to the SpiderCoordinator CRD, but it does not have a default value during the upgrade operation, which will cause panic. You need to use it and treat it as a default value of 0.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/3118

#### Different cluster deployment methods cause SpiderCoordinator to return an empty serviceCIDR, preventing Pod creation

Due to different cluster deployment methods, there are two types of CIDRs recorded in the cluster kube-controller-manager Pod: `Spec.Containers[0].Command` and `Spec.Containers[0].Args`. For example, the RKE2 cluster is `Spec.Containers[0].Args` instead of `Spec.Containers[0].Command`, and `Spec.Containers[0].Command` is hardcoded in the original logic, resulting in abnormal judgment, returning an empty serviceCIDR, and failing to create a Pod.

**References:**

https://github.com/spidernet-io/spiderpool/pull/3211

### Known Issues in v0.8

#### ifacer cannot create bond using vlan 0

When using vlan 0, creating a bond via ifacer will fail.

**References:**

https://github.com/spidernet-io/spiderpool/pull/2639

#### Disable multus feature, still create multus CR resource

When installing, multus feature is disabled, still create multus CR resource, which is not as expected.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2756

#### spidercoordinator cannot detect gateway connections in Pod's netns

Currently spidercoordinator uses plugins to use errgroup to concurrently check gateway reachability and IP conflicts to improve detection speed. Since each operating system thread can have a different network namespace and Go's thread scheduling is highly variable, the caller cannot guarantee to set any specific namespace, but when starting a goroutine in netns.Do, the Go runtime cannot guarantee that the code will be executed in the specified network namespace, so it is necessary to modify Go's errgroup method: manually switch to the target network namespace when starting the goroutine, and return to the original network namespace after execution, so as to ensure that gateway reachability and IP conflicts can be checked.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2738

#### When kubevirt fixed IP function is turned off, spiderpool-agent Pod crashes

When kubevirt fixed IP function is turned off, spiderpool-agent Pod will crash and fail to run, affecting the overall IPAM function.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2971

#### SpiderIPPool resource does not inherit the gateway and route attributes of SpiderSubnet

If you create a SpiderSubnet resource first, and then create a SpiderIPPool resource for the corresponding subnet, SpiderIPPool will inherit the gateway and routes of SpiderSubnet. However, if you first create an isolated SpiderIPPool and then create the corresponding SpiderSubnet resource; then the SpiderIPPool resource will not inherit the SpiderSubnet attributes.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/3011

### Known issues in v0.7

#### Statefulset Pod cannot be restarted due to IP conflict

Since the StatefulSet Pod is restarted, GC scanAll will release the previous IP address at this time, because the system believes that the Pod UID is different from the IP address recorded by IPPool, thus prompting a conflict.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2538

#### Spiderpool cannot recognize third-party controllers like RedisCluster, preventing StatefulSet Pods from having fixed IP addresses

For third-party controllers: RedisCluster -> StatefulSet -> Pod, if Spiderpool sets the SpiderSubnet automatic pool annotation for it, the Pod will not be able to start successfully.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2370

#### Empty spidermultusconfig.spec will cause spiderpool-controller Pod crash

Use empty spidermultusconfig.spec to create CR, webhook verification is successful, but no related network-attachment-definitions are generated, and spiderpool-controller panics.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2444

#### Wrong overlayPodCIDR is obtained in cilium mode

Spidercoordinator auto mode obtains the wrong `podCIDRType` type, and the update of spidercoordinator status does not meet expectations; creating Pods may cause network problems.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2434

#### In one-to-one Pod-to-IP mapping scenarios, IPAM allocation is blocked, preventing some Pods from running and affecting IP allocation performance

An IPPool with 1,000 IP addresses is created, and a Deployment with 1,000 replicas is created. After a certain number of IP addresses are allocated, it is observed that the allocation performance has dropped significantly, and even IP addresses cannot be allocated anymore. A Pod cannot start normally without an IP address. The Pod has been recorded in the actual IPPool resource and its IP has been allocated, but the Pod corresponding to the SpiderEndpoint does not exist.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2518

#### Disabling IP GC function, spiderpool-controller cannot start correctly

Disable IP GC function, spiderpool-controller component will not start correctly due to readiness health check failure.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2532

#### Incorrect namespace parsing in IPPool.Spec.MultusName causes affinity to fail, making the multusName unfindable

Specified Pod Annotation: `v1.multus-cni.io/default-network: kube-system/ipvlan-eth0`, due to Spiderpool's incorrect parsing of namespace, the wrong namespace is used when querying network-attachment-definitions, resulting in the failure to find the corresponding network-attachment-definitions, and thus the Pod cannot be successfully created.

**Reference:**

https://github.com/spidernet-io/spiderpool/pull/2514
