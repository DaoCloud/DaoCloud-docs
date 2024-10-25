---
MTPE: WANG0608GitHub
date: 2024-07-22
---

# Known Network Component Issues and Kernel Compatibility

This page summarizes known issues with various network components that may have a significant impact on production environments, along with some recommendations and solutions.

## kube-proxy

### IPVS mode

Accessing services may encounter 1s delay or failed requests.

- Symptoms:

    1. Accessing services through Service experiences a 1s delay.
    2. Some requests fail during a rolling update.

- Impacts：

    | kubernetes Versions | kube-proxy Behaviors | Symptoms |
    | ------ | -------------- | -------- |
    | <= v1.17 | net.ipv4.vs.conn_reuse_mode=0 | RealServer could not be removed, and some requests fail during a rolling update. |
    | >= v1.19 | net.ipv4.vs.conn_reuse_mode=0 (kernel > v4.1)<br />net.ipv4.vs.conn_reuse_mode=1 (kernel < v4.1) | The default kernel version of CentOS 7.6-7.9 is earlier than v4.1, and accessing services through Service experiences a 1s delay. <br /> The default kernel version of CentOS 8 is higher than v4.1, and RealServer could not be removed, and some requests fail during a rolling update. |
    | >= v1.22 | The net.ipv4.vs.conn_reuse_mode value (kernel > v5.6) is not modified<br />net.ipv4.vs.conn_reuse_mode=0 (kernel > v4.1)<br />net.ipv4.vs.conn_reuse_mode = 1 (kernel < v4.1) <br /> | The default kernel version of CentOS 7.6-7.9 is earlier than v4.1, and accessing services through Service experiences a 1s delay. <br /> The default kernel v4.16 of CentOS 8 is higher than v4.1, and RealServer could not be removed, and some requests fail during a rolling update. <br /> The default kernel v5.15 of Ubuntu 22.04 is higher than v5.9 kernel, and does not have the issue. |

- Recommendation: IPVS mode is not recommended when the kernel version is below v5.9.

- Reference: [Kubernetes Issue #93297](https://github.com/kubernetes/kubernetes/issues/93297)

### iptables mode

- Symptom: The source port is not random enough after NAT, resulting in a 1s delay

- Impact:

    | Kernel | iptables Version | Symptom |
    | ------ | ------------- | ----- |
    | < v3.13 | v1.6.2 | The source port is not random enough after NAT, resulting in a 1s delay |

- Recommendation: An upgrade of the kernel version is advised by considering released versions.

### externalIPs does not work under `externalTrafficPolicy: Local`

- Impact: v1.26.0 <= affected version < v1.30.0

- Recommendation: Update kubernetes to v1.30.0

- Reference: [Kubernetes PR #121919](https://github.com/kubernetes/kubernetes/pull/121919)

### When endpoint in Service is updated, the rules of new endpoint don't take effect until much later

- Impact: v1.27.0 <= affected versions < v1.30.0

- Recommendation: Update kubernetes to v1.30.0

- Reference: [Kubernetes PR #122204](https://github.com/kubernetes/kubernetes/pull/122204)

### LoadBalancerSourceRanges does not work properly in nftables mode

- Recommendation: Update kubernetes to v1.30.0

- Reference: [Kubernetes PR #122614](https://github.com/kubernetes/kubernetes/pull/122614)

### iptables nft and legacy mode selection issue

- Impacts:

    | Versions | Behaviors | Impacts |
    | ------- | --- | --- |
    | < v1.18 | Using iptables-legacy | kube-proxy may not work |
    | >= v1.18 | Prefer to choose nft | None |

- Reference: [kubernetes-sigs/iptables-wrappers](https://github.com/kubernetes-sigs/iptables-wrappers/tree/master)

## Calico

### Offload VXLAN causes a delay during access

- Impacts:

    | Calico Versions | Behaviors | Impacts |
    | ---------- | ---- | --- |
    | < v3.20 | No response | When the kernel version is lower than v5.7, a 63s delay experiences between pods and Service.|
    | >= v3.20 | VXLAN offload is automatically disabled by default via FelixConfiguration.| The performance of NICs is low, only running 1-2 Gbps/s.|
    | >= v3.28 |VXLAN offload is automatically enabled in kernel v5.7, addressing previous packet loss issues with ClusterIP and improving performance.| When the kernel version is lower than v5.7, the performance of NICs is low, only running 1-2 Gbps/s. |

- Recommendations:

    * When lower versions Calico have access latency issue, it can be avoided by `ethtool --offload vxlan.calico rx off tx off`.
    * Higher versions Calico will automatically disable VXLAN offload by default, so customers with network performance requirements can update the kernel version to v5.7 to solve the problem.

- References:

    * [Calico Issue #3145](https://github.com/projectcalico/calico/issues/3145)
    * [Felix PR #2811](https://github.com/projectcalico/felix/pull/2811)

### The parent device of VXLAN is modified but the route is not updated

- Impacts:

    | Calico Versions | Behaviors | Impacts |
    | ----------- | ------------- | ------- |
    | < v3.28.0 | No response | If routing tables do not to use new parent NIC, old routes can't be cleaned up even after restarting felix. |
    | >= v3.28.0 | The VXLAN Manager recreates a routing table when the parent device changes. | None |

- Recommendation: Update Calico to v3.28.0

- Reference: [Calico PR #8279](https://github.com/projectcalico/calico/pull/8279)

### Caches of Cluster calico-kube-controllers are out of sync, causing memory leaks

- Recommendation: Update Calico to v3.26.0

### Inter-node networking is not functioning properly for pods in the IPIP mode

- Impacts:

    | Calico Versions | Behaviors | Impacts |
    | ----------- | --- | --- |
    | < v3.28.0 | No response | The inter-node networking may fail for pods in kernel < v5.7 due to incompatibility between checksum calculation and `iptables --random-fully`. |
    | >= v3.28.0 | The checksum calculation is disabled by default | None |

- Recommendation: Update Calico to v3.28.0+. For earlier versions, you can manually turn off the feature using the`ethtool -K tunl0 tx off` command.

- Reference: [Calico PR #8031](https://github.com/projectcalico/calico/pull/8031)

### iptables nft and legacy mode selection issue

- Impacts:

    | Calico Versions | Behaviors | Impacts |
    | ----------- | --- | --- |
    | < v3.26.0 | It needs to be specified manually, and there are some logical problems with automatic calculations. | Service network anomalies may occur due to a incorrect iptables mode selection. |
    | >= v3.26.0 | Automatic calculation | None |

- Recommendations: Update Calico to v3.26.0+. For earlier versions, you need to manually specify the `FELIX_IPTABLESBACKEND` variable with either the NFT or LEGACY option.

- Reference: [Calico PR #7111](https://github.com/projectcalico/calico/pull/7111)

## Spiderpool

- Recommendation: If you encounter the following problem, please try to update Spiderpool to a higher version to solve it.

### Known issues in v0.9

#### SpiderCoordinator has an error synchronizing status, but the status is still running

- Analysis: If getting the CIDR information for the cluster fails, we should update its status to NotReady, which prevents the pod from being created properly. Otherwise, the pod will run with an incorrect CIDR, which makes network connectivity fail.

- Reference: [Spiderpool PR #2929](https://github.com/spidernet-io/spiderpool/pull/2929)

#### `Values.multus.multusCNI.uninstall` does not take effect after setting, resulting in multus resources not being deleted correctly

- Analysis: After `Values.multus.multusCNI.uninstall` set to true and Spiderpool uninstalled, multus-related resources are still present and not removed as expected.

- Reference: [Spiderpool PR #2974](https://github.com/spidernet-io/spiderpool/pull/2974)

#### serviceCIDR cannot be gotten from kubeControllerManager pod when kubeadm-config is missing

- Analysis: In some scenarios where kubeadm is not used to create a cluster, there may not be a kubeadm-config configMap,
  so that an attempt will be made to get the serviceCIDR from kubeControllerManager.
  Due to a bug, the serviceCIDR cannot be gotten from the kubeControllerManager pod, causing the SpiderCoordinator to fail to update status.

- Reference: [Spiderpool PR #3020](https://github.com/spidernet-io/spiderpool/pull/3020)

#### Upgrading from v0.7.0 to v0.9.0 will cause a panic due to a new attribute `TxQueueLen` to the SpiderCoordinator CRD

- Analysis: In Spiderpool v0.9.0, a new attribute `TxQueueLen` is added to SpiderCoordinator CRD.
  However, during the upgrade operation, there is no default value, which may cause a panic.
  Therefore, you need to use it and treat it as default value 0.

- Reference: [Spiderpool PR #3118](https://github.com/spidernet-io/spiderpool/pull/3118)

#### Different cluster deployment methods cause SpiderCoordinator to return an empty serviceCIDR, which prevents pods to be create

- Analysis: Due to different cluster deployment methods, there are two types of CIDRs recorded in the cluster kube-controller-manager pod:

    - `Spec.Containers[0].Command`
    - `Spec.Containers[0].Args`

    For example, the RKE2 cluster is `Spec.Containers[0].Args` instead of `Spec.Containers[0].Command`.
    The `Spec.Containers[0].Command` is hardcoded in the original implementation logic, leading to a judgment error that results in an empty `serviceCIDR` and subsequently causes pods creation to fail.

- Reference: [Spiderpool PR #3211](https://github.com/spidernet-io/spiderpool/pull/3211)

### Known Issues in v0.8

#### ifacer cannot create bond using vlan 0

- Analysis: Creating a bond via ifacer fails when vlan 0 is used.

- Reference: [Spiderpool PR #2639](https://github.com/spidernet-io/spiderpool/pull/2639)

#### The multus feature is disabled but multus CR resource still is created

- Symptom: During installation, the multus feature is disabled, but the multus CR resource is still created, which is not as expected.

- Reference: [Spiderpool PR #2756](https://github.com/spidernet-io/spiderpool/pull/2756)

#### spiderCoordinator fails to detect gateway connections in netns of pods

- Analysis: Currently, spiderCoordinator uses a plugin to use errgroup to concurrently check for gateway reachability and IP conflicts to improve detection speed.
  Each OS thread can have different network namespaces and the thread scheduling of Go is highly variable, so the caller is not guaranteed to set any particular namespaces.
  However, when starting a goroutine in netns.Do, the code is not guaranteed to execute in the specified network namespace when the Go is running.
  Therefore, the errgroup method of Go needs to be modified to manually switch to the target network namespace when starting goroutine, and then return to the original network namespace after execution to ensure that gateway reachability and IP conflicts can be checked.

- Reference: [Spiderpool PR #2738](https://github.com/spidernet-io/spiderpool/pull/2738)

#### The spiderpool-agent pod crashes when kubevirt fixed IP feature is turned off

- Analysis: When the kubevirt fixed IP feature is turned off, the spiderpool-agent pod crashes and fails to run, affecting the overall IPAM functionality.

- Reference: [Spiderpool PR #2971](https://github.com/spidernet-io/spiderpool/pull/2971)

#### SpiderIPPool resource does not inherit attributes of SpiderSubnet, such as gateway and route

- Analysis: If you create a SpiderSubnet resource first, and then create a SpiderIPPool resource for the corresponding subnet, the SpiderIPPool will inherit the gateway and routes of the SpiderSubnet.
  However, if you create an isolated SpiderIPPool first, and then create the corresponding SpiderSubnet resource, the SpiderIPPool resource will not inherit the attributes of SpiderSubnet.

- Reference: [Spiderpool PR #3011](https://github.com/spidernet-io/spiderpool/pull/3011)

### Known issues in v0.7

#### IP conflicts will be notified when the StatefulSet type pod receives the IP allocation after restarting

- Analysis: As the StatefulSet pod restarts, GC scanAll will release the previous IP address, because the system considers that the pod UID is different from the IP address recorded by IPPool so that notifies conflicts.

- Reference: [Spiderpool PR #2538](https://github.com/spidernet-io/spiderpool/pull/2538)

#### Spiderpool cannot recognize third-party controllers, preventing StatefulSet pod from having fixed IP addresses

- Symptom: Spiderpool cannot recognize third-party controllers like RedisCluster, so that the pod of StatefulSet controlled by them cannot use fixed IPs.

- Analysis: For third party controllers: RedisCluster -> StatefulSet -> Pod, if Spiderpool sets SpiderSubnet autopool annotations for them, the pod will not start successfully.

- Reference: [Spiderpool PR #2370](https://github.com/spidernet-io/spiderpool/pull/2370)

#### Empty `spidermultusconfig.spec` will cause the spiderpool-controller pod to crash

- Symptom: After creating CR with empty `spidermultusconfig.spec`, webhook checksum succeeds, but the related
  network-attachment-definitions is not generated and spiderpool-controller experiences a panic.

- Reference: [Spiderpool PR #2444](https://github.com/spidernet-io/spiderpool/pull/2444)

#### Cilium gets wrong overlayPodCIDR

- Symptoms:
    * In the auto SpiderCoordinator mode, it is failed to get `podCIDRType`, so that the status of SpiderCoordinator is not as expected after updating.
    * Creating a Pod may cause network issues.

- Reference: [Spiderpool PR #2434](https://github.com/spidernet-io/spiderpool/pull/2434)

#### In a 1:1 Pod-to-IP scenario, IPAM allocation can be blocked, preventing some pods from running and affecting IP allocation performance

- Analysis: An IPPool with 1000 IP addresses and a Deployment with 1000 replicas is created.
  After allocating a certain number of IP addresses, you will observe a significant decrease in allocation performance, even cannot continue to allocate IP addresses, while a pod cannot start normally without an IP address.
  An actual IPPool resource has already recorded the pod and assigned its IP address, but the pod corresponding to the SpiderEndpoint does not exist.

- Reference: [Spiderpool PR #2518](https://github.com/spidernet-io/spiderpool/pull/2518)

#### After disabling the IP GC feature, the spiderpool-controller component will not start correctly due to a readiness health check failure

- Analysis: After disabling the IP GC feature, the spiderpool-controller component will not start correctly due to a readiness health check failure

- Reference: [Spiderpool PR #2532](https://github.com/spidernet-io/spiderpool/pull/2532)

#### `IPPool.Spec.MultusName` specifies namespace/multusName, but the associated multusName cannot be found due to a namespace parsing error

- Symptom: `IPPool.Spec.MultusName` specifies namespace/multusName, but a namespace parsing error makes the multusName unfindable, causinhg affinity to fail.

- Analysis: The pod annotation `v1.multus-cni.io/default-network: kube-system/ipvlan-eth0` is specified.
  However, due to Spiderpool's incorrect resolution of namespace, the wrong namespace is used when querying network-attachment-definitions, and the corresponding network-attachment-definitions not being found, so that the pod could not be created successfully.

- Reference: [Spiderpool PR #2514](https://github.com/spidernet-io/spiderpool/pull/2514)
