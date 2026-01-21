# 跨网络区域 IP 分配

本页介绍在多可用区/多子网场景下，如何使用 Spiderpool 实现跨网络区域的 IP 分配。

## 适用场景

- 集群节点位于不同机房或可用区
- 各区域只能使用特定子网
- 需要同一应用在不同节点分配到对应子网的 IP

## 原理说明

SpiderIPPool 支持 `nodeName` 与 `nodeAffinity`，用于限定 IPPool 的可用节点范围。Pod 调度到某个节点时，将从该节点匹配的 IPPool 中分配 IP。

## 前提条件

- 已安装 Spiderpool（参考 [安装 Spiderpool](../../modules/spiderpool/install/install.md)）
- 已准备好 Multus 配置（参考 [Multus CR 管理](../multus-cr.md)）

## 配置步骤

### 1. 创建跨区域 IPPool

为不同节点或区域创建不同的 IPPool：

```yaml
apiVersion: spiderpool.spidernet.io/v2beta1
kind: SpiderIPPool
metadata:
  name: ippool-zone-a
spec:
  subnet: 10.6.0.0/16
  ips:
    - 10.6.168.60-10.6.168.69
  gateway: 10.6.0.1
  nodeName:
  - node-a
---
apiVersion: spiderpool.spidernet.io/v2beta1
kind: SpiderIPPool
metadata:
  name: ippool-zone-b
spec:
  subnet: 10.7.0.0/16
  ips:
    - 10.7.168.60-10.7.168.69
  gateway: 10.7.0.1
  nodeName:
  - node-b
```

### 2. 为工作负载指定 IPPool

通过注解指定多个 IPPool，Spiderpool 会按顺序尝试分配：

```yaml
metadata:
  annotations:
    ipam.spidernet.io/ippool: |-
      {
        "ipv4": ["ippool-zone-a", "ippool-zone-b"]
      }
    v1.multus-cni.io/default-network: kube-system/macvlan-conf
```

## 验证

查看 Pod IP 是否落在对应子网内：

```shell
kubectl get pod -o wide
```

## 注意事项

- `nodeName` 适合小规模集群，`nodeAffinity` 更适合大规模或按标签管理的场景
- IPPool 子网与网关需与节点所在网络一致
