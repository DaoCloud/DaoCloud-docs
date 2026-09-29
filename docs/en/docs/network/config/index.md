---
hide:
  - toc
---

# Network Configuration

The container network in DCE supports the following in the
[global service cluster](../../kpanda/user-guide/clusters/cluster-role.md#_2)
(that is, kpanda-global-cluster):

- Static IP pool

    - [Manage Static IP Pools](./ippool/createpool.md)
    - [Use Static IP Pools for Workloads](./use-ippool/usage.md)
    - [Use Static IP Pools for Third-Party Workloads](./use-ippool/cutomizedusage.md)
    - [Cross-Network Zone IP Allocation](./ippool/topology.md)

- Device management

    - [Manage Multus CR](./multus-cr.md)
    - [SR-IOV Node Policy](./sriov-node-policy.md)

- Component/Scenario adaptation

    - [KubeVirt Fixed IP and Underlay Network](./kubevirt.md)
    - [Istio Service Mesh Adaptation (Underlay)](./istio.md)
