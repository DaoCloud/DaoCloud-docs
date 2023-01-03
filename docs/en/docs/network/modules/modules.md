---
hide:
  - toc
---

# Network components

The network solution provided by DCE 5.0 is an optimized combination of current mainstream open source network components, which can meet the needs of various complex scenarios.

![Web Components](../images/components.png)

Currently, the network components supported by DCE 5.0 include:

- [Calico](../modules/calico/what.md): Virtual Router implemented based on Linux kernel technology to complete data plane forwarding.
- [Cilium](../modules/cilium/what.md): Network solution based on eBPF kernel
- [Contour](../modules/contour/what.md): An open source Kubernetes Ingress controller that uses Envoy as the data plane.
- [f5networks](../modules/f5networks/what.md): Fully control the F5 devices, synchronize the service and ingress configurations in the cluster to the F5 hardware devices, and realize the load balancing of the northbound ingress of the cluster.
- [Ingress-nginx](../modules/metallb/what.md): Ingress controller hosted by the Kubernetes community, using nginx as a reverse proxy and load balancer.
- [MetalLB](../modules/metallb/what.md): Kubernetes load balancer solution for Bare Metal.
- [Multus-underlay](../modules/multus-underlay/what.md): Multi-NIC solution based on Multus with Macvlan + SRIOV-CNI.
- [Spiderpool](../modules/spiderpool/what.md): Automatically manage IP resources

    > All the above components such as CNI and Ingress can be installed on demand.
