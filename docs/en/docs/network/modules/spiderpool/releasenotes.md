# Spiderpool Release Notes

This page lists the Release Notes of Spiderpool, so that you can understand the
evolution path and feature changes of each version.

## 2024-06-26

### v0.9.4

#### Bug fixes

- **Fixed** Add link-local IP to veth0 of istio Pod to ensure that the Pod on the same node can be accessed on the node.

- **Fixed** When creating a Pod with a subnet with a very large CIDR address range, the IP allocation performance is slow.

#### Feature Changes

- **Improvements** coordinator: Use arp instead of icmp when detecting the gateway to avoid check failures due to router prohibition of icmp, and icmp also needs arp to obtain the target mac.

## 2024-06-25

### v0.8.7

#### Bug fixes

- **Fixed** coordinator: Make sure the gw of hijickRoute comes from hostIPRouteForPod, not nodelocaldns.

- **Fixed** Add link-local IP to veth0 of istio Pod to ensure that the Pod on the same node is accessible on the node.

- **Fixed** When creating a Pod using a subnet with a very large CIDR address range, the IP allocation performance is slow.

#### Feature Changes

- **Improvements** coordinator: Use arp instead of icmp when detecting the gateway to avoid check failures due to routers prohibiting icmp, and icmp also requires arp to obtain the target mac.
