---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: NA
Date: 2023-01-04
---

# 什么是 Sriov-network-operator

目前使用 sriov 比较复杂繁琐，需要管理员完全手动配置,  如手动确认网卡是否支持SRIOV、配置PF 和 VF等，参考 [sriov](../multus-underlay/sriov.md)。 社区开源 [Sriov-network-operator](https://github.com/k8snetworkplumbingwg/sriov-network-operator) ，旨在降低使用 sriov-cni 的难度。sriov-operator 整合 sriov-cni 和 sriov-device-plugin 两个项目，完全使用 CRD 的方式统一使用和配置 sriov，包括组件本身和节点上的必要配置，极大的降低了使用难度。

## 组件组成

```shell
[root@controller1 ~]# kubectl  get po -n sriov-network-operator -o wide
NAME                                                              READY   STATUS      RESTARTS   AGE    IP               NODE          NOMINATED NODE   READINESS GATES
sriov-device-plugin-kw8rc                                         1/1     Running     0          62s    10.5.212.132     worker1       <none>           <none>
sriov-network-config-daemon-nhmws                                 3/3     Running     0          76m    10.5.212.132     worker1       <none>           <none>
sriov-network-operator-6955b75d8c-gmpcc                           1/1     Running     0          67s    10.233.73.233    controller1   <none>           <none>
```

- sriov-operator: 控制层面组件，监听 CRs 变化，安装和配置 sriov-cni 和 sriov-device-plugin 组件
- sriov-network-config-daemon：与节点交互，用于开启节点网卡的 SR-IOV 功能和配置 VFs。内置 srivo-cni, 将 sriov-cni 的二进制文件拷贝至主机的 `/opt/cni/bin` 目录下
- sriov-device-plugin: 发现主机上的 VFs ，并宣告给 kubelet

## CRD

- SriovNetworkNodeState: SriovNetworkNodeState 发现主机上支持 SR-IOV 功能的网卡，并且写入到 status 中

```shell
[root@controller1 ~]# kubectl  get SriovNetworkNodeState -n sriov-network-operator worker1 -o yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodeState
metadata:
  creationTimestamp: "2023-06-25T07:01:04Z"
  generation: 4
  name: worker1
  namespace: sriov-network-operator
  ownerReferences:
  - apiVersion: sriovnetwork.openshift.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: SriovNetworkNodePolicy
    name: default
    uid: 111e692f-cc3c-40da-aa28-de3a7f8f7c0e
  resourceVersion: "11353566"
  uid: d1bef95a-82c5-4a5c-8eb1-0ff7744eff0f
spec:
  dpConfigVersion: "11351926"
status:
  interfaces:
  - deviceID: "1017"
    driver: mlx5_core
    linkSpeed: 10000 Mb/s
    linkType: ETH
    mac: 04:3f:72:d0:d2:86
    mtu: 1500
    name: enp4s0f0np0
    pciAddress: "0000:04:00.0"
    totalvfs: 8
    vendor: 15b3
  - deviceID: "1017"
    driver: mlx5_core
    linkSpeed: 10000 Mb/s
    linkType: ETH
    mac: 04:3f:72:d0:d2:87
    mtu: 1500
    name: enp4s0f1np1
    pciAddress: "0000:04:00.1"
    totalvfs: 8
    vendor: 15b3
  syncStatus: Succeeded
```

上面信息说明: 在 `worker1` 节点上的接口 `enp4s0f0np0` 和 `enp4s0f1np1` 具有 SR-IOV 功能，我们可以基于它们配置 VFs，供 Pod 使用。

- SriovNetworkNodePolicy：用于配置 VFs 的数量和安装 sriov-device-plugin 组件

```shell

[root@controller1 ~]# kubectl get sriovnetworknodepolicies.sriovnetwork.openshift.io -n sriov-network-operator policy1 -o yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"sriovnetwork.openshift.io/v1","kind":"SriovNetworkNodePolicy","metadata":{"annotations":{},"name":"policy1","namespace":"sriov-network-operator"},"spec":{"deviceType":"netdevice","nicSelector":{"pfNames":["enp4s0f0np0"],"vendor":"15b3"},"nodeSelector":{"kubernetes.io/os":"linux"},"numVfs":4,"resourceName":"sriov_netdevice"}}
  creationTimestamp: "2023-06-25T07:01:28Z"
  generation: 3
  name: policy1
  namespace: sriov-network-operator
  resourceVersion: "11350025"
  uid: b0513a9c-8c64-421d-97cc-d780fd7e8cec
spec:
  deviceType: netdevice
  nicSelector:
    pfNames:
    - enp4s0f0np0
  nodeSelector:
    kubernetes.io/hostname: 10-20-1-240  # 只作用于 10-20-1-240 这个节点
  numVfs: 4 # 渴望的 VFs 数量
  resourceName: sriov_netdevice
```

- **spce.nicSelector.pfNames**: PF 的列表，创建 CR 后将基于列表中的 PF 创建指定数量的 VFs
- **spec.nodeSelector**: 此 Policy 在哪些节点生效. 注: 会安装 sriov-device-plugin 组件到指定节点
