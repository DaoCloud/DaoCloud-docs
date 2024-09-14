---
MTPE: WANG0608GitHub
Date: 2024-09-14
---

# Spiderpool Release Notes

This page lists the Release Notes of Spiderpool, so that you can understand the
evolution path and feature changes of each version.

## 2024-09-04

### v0.9.6

#### Bug Fixes

- **Fixed** the issue where tuneSysctlConfig value in the chart cannot working correctly.
- **Fixed** the ability to correctly update the GOMAXPROCS configuration.

## 2024-08-25

### v0.9.5

#### Bug Fixes

- **Fixed** the issue where StatefulSet Pod should change IP when recreating with a changed pool in annotation
- **Fixed** the issue where a pod fails to access NodePort when it has multiple NICs.
- **Fixed** the issue where pods could not start with the expected CNI when the health check of the spiderpool-agent failed, resulting in the loss of 00-multus.conf.
- **Fixed** the issue where the installation of the spiderpool-init pod may be blocked.
- **Fixed** the issue where the incorrect IP addresses from Spiderpool GC may cause IP conflicts during rapid scaling up/down of StatefulSet Pods.
- **Fixed** the issue where the coordinator sets rp_filter only for pods, not for nodes.
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

- **Fixed** the issue where modifying the pool used in the StatefulSet Pod annotations could lead to using the new pool's IP address when recreated.
- **Fixed** the issue where a pod cannot access NodePort when it has multiple NICs.
- **Fixed** the issue where pods could not start with the expected CNI when the health check of the spiderpool-agent failed, resulting in the loss of 00-multus.conf.
- **Fixed** the issue where the installation of the spiderpool-init pod may be blocked.
- **Fixed** the issue where the incorrect IP addresses from Spiderpool GC may cause IP conflicts during rapid scaling up/down of StatefulSet Pods.
- **Fixed** the issue where the coordinator sets rp_filter only for pods, not for nodes.
- **Fixed** the coordinator to fix the erroneous policy routing table when pods have multiple NICs.
- **Fixed** the issue where the tuneSysctlConfig value in the chart is not working correctly.

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
