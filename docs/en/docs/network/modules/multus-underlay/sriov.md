# SR-IOV CNI configuration

## Environmental requirements

To use SR-IOV CNI, you need to confirm whether the node is a physical host and the node has a physical network card that supports SR-IOV.
SR-IOV will not work if the node is a VM or does not have an SR-IOV capable NIC.
You can check whether the node has a network card that supports SR-IOV function in the following way.

### Check if SR-IOV is supported

Get all NICs with `ip link show`:

```shell
root@172-17-8-120:~# ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether b8:ca:3a:67:e5:fc brd ff:ff:ff:ff:ff:ff
    altname enp1s0f0
3: eno2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
    link/ether b8:ca:3a:67:e5:fd brd ff:ff:ff:ff:ff:ff
    altname enp1s0f1
4: eno3: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
    link/ether b8:ca:3a:67:e5:fe brd ff:ff:ff:ff:ff:ff
    altname enp1s0f2
5: eno4: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
    link/ether b8:ca:3a:67:e5:ff brd ff:ff:ff:ff:ff:ff
    altname enp1s0f3
6: enp4s0f0np0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 04:3f:72:d0:d2:86 brd ff:ff:ff:ff:ff:ff
7: enp4s0f1np1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 04:3f:72:d0:d2:87 brd ff:ff:ff:ff:ff:ff
8: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
    link/ether 02:42:60:cb:04:10 brd ff:ff:ff:ff:ff:ff
```

Filter common virtual NICs (such as docker0, cali*, vlan sub-interfaces, etc.), take `enp4s0f0np0` as an example, and confirm whether it supports SR-IOV:

```shell
root@172-17-8-120:~# ethtool -i enp4s0f0np0
driver: mlx5_core # network card driver
version: 5.15.0-52-generic
firmware-version: 16.27.6008 (LNV0000000033)
expansion-rom-version:
bus-info: 0000:04:00.0 # PCI device number
supports-statistics: yes
supports-test: yes
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: yes
```

Query its PCI device details via `bus-info`:

```shell
root@172-17-8-120:~# lspci -s 0000:04:00.0 -v | grep SR-IOV
Capabilities: [180] Single Root I/O Virtualization (SR-IOV)
```

If the above line is displayed in the output, it means that the network card supports SR-IOV. Get the vendor and device of this network card:

```shell
root@172-17-8-120:~# lspci -s 0000:04:00.0 -n
04:00.0 0200: 15b3:1017
```

in,

- `15b3`: Indicates the manufacturer number of this PCI device, such as `15b3` means Mellanox
- `1017`: indicates the device model of this PCI device, such as `1017` indicates a Mellanox MT27800 Family [ConnectX-5] series network card

> You can query all PCI device information through `https://devicehunt.com/all-pci-vendors`.

### Configure VF (Virtual Function)

Configure VF for the NIC that supports SR-IOV in the following way:

```shell
root@172-17-8-120:~# echo 8 > /sys/class/net/enp4s0f0np0/device/sriov_numvfs
```

Confirm that the VF configuration was successful:

```shell
root@172-17-8-120:~# cat /sys/class/net/enp4s0f0np0/device/sriov_numvfs
8
root@172-17-8-120:~# ip l show enp4s0f0np0
6: enp4s0f0np0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 04:3f:72:d0:d2:86 brd ff:ff:ff:ff:ff:ff
    vf 0 link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 1 link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 2 link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 3 link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 4 link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 5 link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 6 link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
    vf 7 link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking off, link-state auto, trust off, query_rss off
```

Output the content in the above figure, indicating that the configuration is successful.

## Install SR-IOV CNI

Install SR-IOV CNI by installing Multus-underlay. For the specific installation process, refer to [Installation](install.md).
Note, the `sriov-device-plugin` resource must be correctly configured during installation, including vendor, device and other information.
Otherwise SRIOV-Device-Plugin cannot find the correct VF.

## Configure SRIOV-Device-Plugin

After installing SR-IOV CNI, check whether SR-IOV CNI has discovered the VF on the host in the following way:

```shell
root@172-17-8-110:~# kubectl describe nodes 172-17-8-110
...
Allocatable:
  cpu: 24
  ephemeral-storage: 881675818368
  hugepages-1Gi: 0
  hugepages-2Mi: 0
  intel.com/sriov-netdevice: 8 # This line indicates that SR-IOV CNI successfully discovered the VFs on this host
  memory: 16250260Ki
  pods: 110
```

## use

There are three things to pay attention to when creating workloads using SR-IOV CNI:

- Verify that the `sriov-device-plugin` resource exists in the SR-IOV multus network-attachment-definition object:

    ```shell
    root@172-17-8-110:~# kubectl get network-attachment-definitions.k8s.cni.cncf.io -n kube-system sriov-vlan0 -o yaml
    apiVersion: k8s.cni.cncf.io/v1
    kind: NetworkAttachmentDefinition
    metadata:
      annotations:
        k8s.v1.cni.cncf.io/resourceName: intel.com/sriov_netdevice
      name: sriov-vlan0
      namespace: kube-system
    ```

    `resourceName` must be the same as the resource name registered in `kubelet` (i.e. the name in the Node object).

    > After creating the network-attachment-definition object, updating annotations: `k8s.v1.cni.cncf.io/resourceName` will not take effect!

- When creating a workload, you need to bind the specified network-attachment-definition object through the annotations of multus in the annotations field of the Pod.

    - If the type is sriov-overlay, you need to insert the following annotations in the Pod's Annotations:

        ```yaml
          annotations:
            k8s.v1.cni.cncf.io/networks: kube-system/sriov-overlay-vlan0
        ```

        `k8s.v1.cni.cncf.io/networks`: Indicates that an SR-IOV CNI network card will be inserted in addition to the default CNI in the Pod.

    - If the type is sriov-standalone, you need to insert the following annotations in the Pod's Annotations:

        ```yaml
          annotations:
            v1.multus-cni.io/default-network: kube-system/sriov-standalone-vlan0
        ```

        `v1.multus-cni.io/default-network`: Modify the default network card of the Pod. If not specified, the Pod will be assigned the first NIC via the cluster default CNI.

- Give containers SR-IOV resource quotas in the Pod's Resource field:

    ```yaml
    ...
      containers:
        resources:
          requests:
            intel.com/sriov-netdevice: '1'
          limits:
            intel.com/sriov-netdevice: '1'
    ...
    ```

    The name needs to be consistent, otherwise the Pod will fail to be created because the VF cannot be requested.