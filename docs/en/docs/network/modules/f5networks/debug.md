---
hide:
  - toc
---

# Summary of F5network installation problems

This page introduces some problems encountered when installing F5network components and their solutions.
For the installation steps of F5network components, please refer to the [Installation](./install.md) document.

Some common installation problems are summarized below.

1. After installing the F5network component, the `f5 ipam controller` service cannot be started.

    If this component uses Layer 4 load balancing mode, `f5 ipam controller` will be installed, and `f5 ipam controller` requires the cluster to have storage components and provide PVC services.
    This problem occurs when there is no storage component. Refer to the relevant storage component installation manual for installation.

1. `cis.f5.com/ipamLabel: LabelName` is specified in the Service, but it cannot be assigned an IP.

    Please check if there are other loadbalancer components in the cluster. If there is, it will cause the F5 IPAM component to fail to assign an IP address to the Service, please uninstall other loadbalancer components.

1. There is no Pool Member on the F5 side

    Please check if the Service has an Endpoint. If not, there will be no Pool Member on the F5 side.

1. F5 traffic cannot be forwarded to the nodePort of the cluster node.

    Please run `kubectl describe pod <f5Name>-f5-bigip-ctlr-<xxx> -n <namespace>` to check if --node-label-selector is set.
    If it is set, but the relevant node does not have a corresponding label, F5 will not know how to forward it.