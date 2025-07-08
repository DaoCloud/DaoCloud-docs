---
MTPE: WANG0608GitHub
Date: 2025-06-23
---

# Spiderpool Release Notes

This page lists the Release Notes of Spiderpool, so that you can understand the
evolution path and feature changes of each version.

## 2025-04-30

### v1.0.2

#### New Features

* **Added** support in `SpiderMultusConfig` to configure the MTU for Macvlan, IPVlan, and SR-IOV CNI plugins.
* **Added** Pause and Discards statistics to RDMA metrics, and improved the Grafana dashboard.
* **Added** support for validating whether IPs are still allocated when deleting IPPools and Subnets. When the `enableValidatingResourcesDeletedWebhook=true` option is set in the `spiderpool-conf` ConfigMap, the webhook will prevent deletion if IPs are still in use.

#### Bug Fixes

* **Fixed** an issue where RDMA multicast metrics on nodes were reported incorrectly.
* **Fixed** an issue where bandwidth limits (min/maxTxRateMbps) for SR-IOV in `SpiderMultusConfig` were not taking effect.
* **Fixed** an issue where, if a stateless application did not go through the normal CNI `Del` process, the IP could be garbage-collected but the `SpiderEndpoint` remained, preventing the IP from being reassigned and causing Pod startup failure.
* **Fixed** an issue where the `Spiderpool-agent` environment variable `EnableGCStatelessTerminatingPod(Not)ReadyNode=false` did not function. This variable controls whether Spiderpool should reclaim the IPs of stateless applications that are still running normally, helping avoid situations where the Pod exists but its IP has been reclaimed.

## 2025-02-13

### v1.0.1

#### Bug Fixes

* **Fixed** an issue in IPAM where, after IP conflict detection, a gratuitous ARP was not sent, causing the ARP cache to be outdated and resulting in network connectivity issues for newly created Pods.
* **Fixed** a bug to ensure the kernel sends Gratuitous ARP (GARP) packets to avoid communication failures.
* **Fixed** an issue where the Helm Chart used for validating `IPPool` and `Subnet` webhooks was not updated properly.

## 2025-01-26

### v1.0.0

#### New Features

* **Added** support for injecting the same annotation `cni.spidernet.io/network-resource-inject` into both `SpiderMultusConfig` and Pods, enabling the webhook to inject network interfaces and hardware resources defined in `SpiderMultusConfig` into the Pod.
* **Added** an upgrade to Multus version V4.0.
* **Added** support for Pod- and node-level RDMA monitoring for AI workloads.
* **Added** chain CNI support in `SpiderMultusConfig`, enabling compatibility with plugins like `tuning`.
* **Added** wildcard filtering support for `IPPool`.
* **Added** support for cleaning up resources during the uninstallation of Spiderpool.
* **Added** support for obtaining cluster subnets from the `kube-controller-manager` Pod, avoiding failures in scenarios where `kubeadm-config` does not provide subnet information.

#### Bug Fixes

* **Fixed** an issue in IPAM where StatefulSets could not run in multi-network interface mode.
* **Fixed** an issue where, if the `spiderpool-agent` container restarted but the Pod did not, the `00-multus.conf` file on the node could be deleted, preventing the Pod from using multiple interfaces.
* **Fixed** an issue where Spiderpool failed to properly garbage-collect IP addresses during StatefulSet Pod scaling, leading to IP conflicts.
* **Fixed** an issue where the Coordinator's policy routing table behaved abnormally in multi-interface scenarios, causing communication failures.
* **Fixed** overly permissive RBAC permissions that posed a potential CVE security risk.
* **Fixed** performance issues where IP assignment was slow when subnets were too large.
* **Fixed** an issue where Pods with multiple interfaces could not access NodePort services.

## 2025-01-26

### v0.9.9

#### New Features

* **Added** IP conflict and gateway reachability checks directly in IPAM instead of in the Coordinator plugin. This avoids incorrect ARP cache updates in the event of IP conflicts, which could cause short-term communication loss during migrations of applications using static IPs.

## 2025-01-03

### v0.9.8

#### New Features

* **Added** a switch to control whether Istio's `veth0` interface is configured with a link-local address. This prevents issues where Istio cannot intercept traffic.

#### Bug Fixes

* **Fixed** a validation issue in `SpiderMultusConfig` that checks for name conflicts in the `multus.spidernet.io/cr-name` field.
* **Fixed** an issue in IPAM where IP shortage on one network interface could exhaust the IP pool of other interfaces in multi-interface scenarios.
* **Fixed** a panic issue in the `spiderpool-controller` when running Cilium in multi-pool IPAM mode.
* **Fixed** a problem where IP conflict detection occurred after the gateway check, which could lead to communication failures. The fix ensures conflict detection happens first.

## 2024-09-26

### v0.9.7

#### Bug Fixes

* **Fixed** a panic error in the webhook when validating the `podRPFilter` field during the creation of a `SpiderMultusConfig`.
* **Fixed** an issue in the webhook that ensures the `podMACPrefix` in `SpiderMultusConfig` is a unicast MAC address.

## 2024-09-04

### v0.9.6

#### Bug Fixes

- **Fixed** an issue where tuneSysctlConfig value in the chart cannot working correctly.
- **Fixed** an issue to correctly update the GOMAXPROCS configuration.

## 2024-08-25

### v0.9.5

#### Bug Fixes

- **Fixed** an issue where StatefulSet Pod should change IP when recreating with a changed pool in annotation
- **Fixed** an issue where a pod fails to access NodePort when it has multiple NICs.
- **Fixed** an issue where pods could not start with the expected CNI when the health check of the spiderpool-agent failed, resulting in the loss of 00-multus.conf.
- **Fixed** an issue where the installation of the spiderpool-init pod may be blocked.
- **Fixed** an issue where the incorrect IP addresses from Spiderpool GC may cause IP conflicts during rapid scaling up/down of StatefulSet Pods.
- **Fixed** an issue where the coordinator sets rp_filter only for pods, not for nodes.
- **Fixed** the coordinator to fix the erroneous policy routing table when pods have multiple NICs.

#### Feature Changes

- **Added** spiderpool-agent to support configuring sysctl settings.
- **Added** spiderpool-agent which can set rp_filter for each node to 0.
- **Added** chainCNI support for spidermultusconfig.

## 2024-06-26

### v0.9.4

#### Bug Fixes

- **Fixed** the addition of link-local IP to the veth0 of the istio Pod to ensure that pods on the same node are accessible.

- **Fixed** When creating a pod with a subnet with a very large CIDR address range, the IP allocation performance is slow.

#### Feature Changes

- **Improved** coordinator to use arp instead of icmp when detecting the gateway to avoid check failures due to router prohibition of icmp, and icmp also needs arp to obtain the target mac.

## 2024-08-25

### v0.8.8

#### Bug Fixes

- **Fixed** an issue where modifying the pool used in the StatefulSet Pod annotations could lead to using the new pool's IP address when recreated.
- **Fixed** an issue where a pod cannot access NodePort when it has multiple NICs.
- **Fixed** an issue where pods could not start with the expected CNI when the health check of the spiderpool-agent failed, resulting in the loss of 00-multus.conf.
- **Fixed** an issue where the installation of the spiderpool-init pod may be blocked.
- **Fixed** an issue where the incorrect IP addresses from Spiderpool GC may cause IP conflicts during rapid scaling up/down of StatefulSet Pods.
- **Fixed** an issue where the coordinator sets rp_filter only for pods, not for nodes.
- **Fixed** the coordinator to fix the erroneous policy routing table when pods have multiple NICs.
- **Fixed** an issue where the tuneSysctlConfig value in the chart is not working correctly.

#### Feature Changes

- **Added** spiderpool-agent to support configuring sysctl settings.
- **Added** spiderpool-agent to set rp_filter for each node to 0.
- **Added** chainCNI support for spidermultusconfig.

## 2024-06-25

### v0.8.7

#### Bug fixes

- **Fixed** coordinator to make sure the gw of hijickRoute comes from hostIPRouteForPod, not nodelocaldns.
- **Fixed** the addition of link-local IP to the veth0 of the istio Pod to ensure that the pod on the same node is accessible on the node.
- **Fixed** When creating a pod using a subnet with a very large CIDR address range, the IP allocation performance is slow.

#### Feature Changes

- **Improved** coordinator to use arp instead of icmp when detecting the gateway to avoid check failures due to routers prohibiting icmp, and icmp also requires arp to get the target mac.
