# Sriov-network-operator

[Sriov-network-operator](https://github.com/k8snetworkplumbingwg/sriov-network-operator) is an open-source project that aims to simplify the usage of SR-IOV technology by integrating the sriov-cni and sriov-device-plugin projects. It uses Custom Resource Definitions (CRDs) to configure and manage SR-IOV, making it easier for administrators to use.

## Components

```shell
[root@controller1 ~]# kubectl  get po -n sriov-network-operator -o wide
NAME                                                              READY   STATUS      RESTARTS   AGE    IP               NODE          NOMINATED NODE   READINESS GATES
sriov-device-plugin-kw8rc                                         1/1     Running     0          62s    10.5.212.132     worker1       <none>           <none>
sriov-network-config-daemon-nhmws                                 3/3     Running     0          76m    10.5.212.132     worker1       <none>           <none>
sriov-network-operator-6955b75d8c-gmpcc                           1/1     Running     0          67s    10.233.73.233    controller1   <none>           <none>
```

The Sriov-network-operator consists of the following components:

- **sriov-operator**: This controller monitors changes in CRs and installs/configures the sriov-cni and sriov-device-plugin components.
- **sriov-network-config-daemon**: This component interacts with the nodes to enable SR-IOV on the network interfaces and configure Virtual Functions (VFs). It contains the sriov-cni binary and copies it to the `/opt/cni/bin` directory on the host.
- **sriov-device-plugin**: This component discovers the VFs available on the host and exposes them to the kubelet.

## Custom Resource Definitions (CRDs)

The Sriov-network-operator introduces two CRDs:

**SriovNetworkNodeState**: This CRD discovers network interfaces on the host that support SR-IOV and writes them into the status field.

Example:

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

The above example shows that the interfaces `enp4s0f0np0` and `enp4s0f1np1` on worker1 have SR-IOV capability and can be used to configure VFs for Pods.

**SriovNetworkNodePolicy**: This CRD is used to configure the number of VFs and install the sriov-device-plugin component.

Example:

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
    pfNames:
    - enp4s0f0np0
  nodeSelector:
    kubernetes.io/hostname: 10-20-1-240  # Only effect to the node 10-20-1-240
  numVfs: 4 # Desired VFs quantity
  resourceName: sriov_netdevice
```

- **spec.nicSelector.pfNames**: The list of PFs where the specified number of VFs will be created.
- **spec.nodeSelector**: Specifies the nodes where this policy should be applied. Note: The sriov-device-plugin component will be installed on the specified nodes.
