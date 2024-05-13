---
MTPE: windsonsea
Date: 2023-05-13
---

# What is Sriov-network-operator

Currently, using SRIOV is complex and cumbersome, requiring administrators to manually configure everything, such as verifying if the network card supports SRIOV, configuring PFs and VFs, etc., as referenced in [sriov](../multus-underlay/sriov.md). The community open-source [Sriov-network-operator](https://github.com/k8snetworkplumbingwg/sriov-network-operator) aims to reduce the complexity of using sriov-cni. The sriov-operator integrates sriov-cni and sriov-device-plugin projects, utilizing CRDs to uniformly manage and configure SRIOV, including the components themselves and the necessary configurations on the nodes, significantly simplifying usage.

## Components

```shell
[root@controller1 ~]# kubectl  get po -n sriov-network-operator -o wide
NAME                                                              READY   STATUS      RESTARTS   AGE    IP               NODE          NOMINATED NODE   READINESS GATES
sriov-device-plugin-kw8rc                                         1/1     Running     0          62s    10.5.212.132     worker1       <none>           <none>
sriov-network-config-daemon-nhmws                                 3/3     Running     0          76m    10.5.212.132     worker1       <none>           <none>
sriov-network-operator-6955b75d8c-gmpcc                           1/1     Running     0          67s    10.233.73.233    controller1   <none>           <none>
```

- **sriov-operator**: A control layer component that listens for changes in CRs and installs/configures sriov-cni and sriov-device-plugin components.
- **sriov-network-config-daemon**: Interacts with nodes to enable the SR-IOV functionality of node network cards and configure VFs. It embeds sriov-cni and copies the sriov-cni binary files to the `/opt/cni/bin` directory on the host.
- **sriov-device-plugin**: Discovers VFs on the host and announces them to kubelet.

## CRD

**SriovNetworkNodeState:** Discovers network cards on the host that support SR-IOV functionality and writes them into the status.

```shell
[root@controller1 ~]# kubectl get SriovNetworkNodeState -n sriov-network-operator worker1 -o yaml
```

```yaml
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

The information above indicates that the interfaces `enp4s0f0np0` and `enp4s0f1np1` on the `worker1` node have SR-IOV capabilities, and we can configure VFs based on them for use by Pods.

**SriovNetworkNodePolicy:** Used to configure the number of VFs and install the sriov-device-plugin component.

```shell
[root@controller1 ~]# kubectl get sriovnetworknodepolicies.sriovnetwork.openshift.io -n sriov-network-operator policy1 -o yaml
```

```yaml
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
    pfNames: # (1)!
      - enp4s0f0np0
  nodeSelector: # (2)!
    kubernetes.io/hostname: 10-20-1-240 # (3)!
  numVfs: 4 # (4)!
  resourceName: sriov_netdevice
```

1. List of PFs, VFs will be created based on the specified number in the list after creating the CR.
2. Nodes where this Policy will be effective. Note: sriov-device-plugin component will be installed on specified nodes.
3. Only applicable to node 10-20-1-240.
4. Desired number of VFs.
