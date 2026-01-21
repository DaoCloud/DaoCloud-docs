---
hide:
  - toc
---

# 网络配置

DCE 5.0 中的容器网络支持在[全局服务集群](../../kpanda/user-guide/clusters/cluster-role.md#_2)（即 kpanda-global-cluster）中：

- 静态 IP 池
    - [管理静态 IP 池](./ippool/createpool.md)
    - [工作负载使用静态 IP 池](./use-ippool/usage.md)
    - [第三方工作负载使用静态 IP 池](./use-ippool/cutomizedusage.md)
    - [跨网络区域 IP 分配](./ippool/topology.md)
- 设备管理
    - [管理 Multus CR](./multus-cr.md)
    - [SR-IOV 节点策略](./sriov-node-policy.md)
- 组件/场景适配
    - [KubeVirt 固定 IP 与 Underlay 网络](./kubevirt.md)
    - [Istio 服务网格适配（Underlay）](./istio.md)
