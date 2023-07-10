# DPDK

本文主要介绍如何在 DCE 5.0 中快速创建第一个 DPDK 应用。

## 前置依赖

- 安装 Multus-underlay，并启用安装 SR-IOV 组件，参考[安装](install.md)
- 需要硬件支持：拥有支持 SR-IOV 系列的网卡并设置虚拟功能（VF），参考[SR-IOV](sriov.md)
- 需要切换网卡驱动为用户态驱动

```shell
# 下载 dpdk 源码
root@master:~/cyclinder/sriov/# wget https://fast.dpdk.org/rel/dpdk-22.07.tar.xz && cd dpdk-22.07/usertools
root@master:~/cyclinder/sriov/dpdk-22.07/usertools# ./dpdk-devbind.py --status
root@172-17-8-120:~/cyclinder/sriov/dpdk-22.07/usertools# ./dpdk-devbind.py --status
Network devices using kernel driver
===================================
0000:01:00.0 'I350 Gigabit Network Connection 1521' if=eno1 drv=igb unused=vfio-pci
0000:01:00.1 'I350 Gigabit Network Connection 1521' if=eno2 drv=igb unused=vfio-pci
0000:01:00.2 'I350 Gigabit Network Connection 1521' if=eno3 drv=igb unused=vfio-pci
0000:01:00.3 'I350 Gigabit Network Connection 1521' if=eno4 drv=igb unused=vfio-pci
0000:04:00.0 'MT27800 Family [ConnectX-5] 1017' if=enp4s0f0np0 drv=mlx5_core unused=vfio-pci *Active*
0000:04:00.1 'MT27800 Family [ConnectX-5] 1017' if=enp4s0f1np1 drv=mlx5_core unused=vfio-pci *Active*
0000:04:00.2 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v0 drv=mlx5_core unused=vfio-pci
0000:04:00.3 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v1 drv=mlx5_core unused=vfio-pci
0000:04:00.4 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v2 drv=mlx5_core unused=vfio-pci
0000:04:00.5 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v3 drv=mlx5_core unused=vfio-pci
0000:04:00.6 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v4 drv=mlx5_core unused=vfio-pci
0000:04:00.7 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v5 drv=mlx5_core unused=vfio-pci
0000:04:01.1 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v6 drv=mlx5_core unused=vfio-pci
```

以 `0000:04:00.2 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v0 drv=mlx5_core unused=vfio-pci` 为例：

- 0000:04:00.2：该 VF PCI 地址
- if=enp4s0f0v0：该 VF 网卡名称
- drv=mlx5_core：当前网卡驱动
- unused=vfio-pci：可切换的网卡驱动

DPDK 支持的用户态驱动有三种：

- vfio-pci：在启用 IoMMU 情况下，推荐使用此驱动，性能安全性最好
- igb-uio：适用性较 uio_pci_generic 更强，支持 SR-IOV VF，但需手动编译 module 并加载到内核
- uio_pci_generic：内核原生驱动，不兼容 SR-IOV VF，但支持在 VM 上使用

切换网卡驱动为 vfio-pci：

```shell
root@172-17-8-120:~/cyclinder/sriov/dpdk-22.07/usertools# ./dpdk-devbind.py --bind=vfio-pci 0000:04:01.1
```

查看绑定结果:

```shell
root@172-17-8-120:~/cyclinder/sriov/dpdk-22.07/usertools# ./dpdk-devbind.py --status

Network devices using DPDK-compatible driver
============================================
0000:04:01.1 'MT27800 Family [ConnectX-5 Virtual Function] 1018' drv=vfio-pci unused=mlx5_core

Network devices using kernel driver
===================================
0000:01:00.0 'I350 Gigabit Network Connection 1521' if=eno1 drv=igb unused=vfio-pci
0000:01:00.1 'I350 Gigabit Network Connection 1521' if=eno2 drv=igb unused=vfio-pci
0000:01:00.2 'I350 Gigabit Network Connection 1521' if=eno3 drv=igb unused=vfio-pci
0000:01:00.3 'I350 Gigabit Network Connection 1521' if=eno4 drv=igb unused=vfio-pci
0000:04:00.0 'MT27800 Family [ConnectX-5] 1017' if=enp4s0f0np0 drv=mlx5_core unused=vfio-pci *Active*
0000:04:00.1 'MT27800 Family [ConnectX-5] 1017' if=enp4s0f1np1 drv=mlx5_core unused=vfio-pci *Active*
0000:04:00.2 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v0 drv=mlx5_core unused=vfio-pci
0000:04:00.3 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v1 drv=mlx5_core unused=vfio-pci
0000:04:00.4 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v2 drv=mlx5_core unused=vfio-pci
0000:04:00.5 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v3 drv=mlx5_core unused=vfio-pci
0000:04:00.6 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v4 drv=mlx5_core unused=vfio-pci
0000:04:00.7 'MT27800 Family [ConnectX-5 Virtual Function] 1018' if=enp4s0f0v5 drv=mlx5_core unused=vfio-pci
```

`0000:04:01.1`：已经变为 vfio-pci 驱动

- 设置大页内存和开启 IoMMU（vfio-pci 驱动依赖 IOMMU 技术）：

    编辑 `/etc/default/grub`，在 `GRUB_CMDLINE_LINUX` 中加入以下内容：

    ```shell
    GRUB_CMDLINE_LINUX='default_hugepagesz=1GB hugepagesz=1GB hugepages=6 isolcpus=1-3 intel_iommu=on iommu=pt'
    update-grab && reboot
    ```

    !!! note

        更新上述配置，需要重启系统，重启系统前最好备份。
        如果不能更新配置，驱动需要切换为 igb-uio 驱动，需手动 build && insmod && modprobe，具体参考 https://github.com/atsgen/dpdk-kmod

## 配置 SRIOV-Device-Plugin

- 更新 SRIOV-Device-plugin 的 configmap：新建资源池 sriov_netdevice_dpdk，让其能够找到支持 dpdk 的 VF：

    ```shell
    kubectl edit cm -n kube-system sriov-0.1.1-config
    apiVersion: v1
    data:
      config.json: |-
        {
          "resourceList":
          [{
            "resourceName": "sriov_netdevice",
            "resourcePrefix": "intel.com",
            "selectors": {
              "device": ["1018"],
              "vendors": ["15b3"],
              "drivers": ["mlx5_core"],
              "pfNames": []
            }
          },{
            "resourceName": "sriov_netdevice_dpdk",
            "resourcePrefix": "intel.com",
            "selectors": {
              "drivers": ["vfio-pci"]
            }
          }]
        }
    ```

    新增 sriov_netdevice_dpdk。注意 selectors 中 driver 指定 vfio-pci 后将重启 sriov-device-plugin。

    ```shell
    kubectl delete po -n kube-system -l app=sriov-dp
    ```

    等待重启完成, 查看 Node 是否加载 sriov_netdevice_dpdk 资源：

    ```sh
    kubectl describe nodes 172-17-8-120
    ...
    Allocatable:
      cpu:                             24
      ephemeral-storage:               881675818368
      hugepages-1Gi:                   6Gi
      hugepages-2Mi:                   0
      intel.com/sriov_netdevice:       6
      intel.com/sriov_netdevice_dpdk:  1  # 这里显示表示已经可用了
    ```

- 创建 Multus DPDK CRD：

    ```shell
    cat EOF | kubectl apply -f -
    > apiVersion: k8s.cni.cncf.io/v1
    kind: NetworkAttachmentDefinition
    metadata:
      annotations:
        helm.sh/hook: post-install
        helm.sh/resource-policy: keep
        k8s.v1.cni.cncf.io/resourceName: intel.com/sriov_netdevice_dpdk
        v1.multus-underlay-cni.io/coexist-types: '["default"]'
        v1.multus-underlay-cni.io/default-cni: "false"
        v1.multus-underlay-cni.io/instance-type: sriov_dpdk
        v1.multus-underlay-cni.io/underlay-cni: "true"
        v1.multus-underlay-cni.io/vlanId: "0"
      name: sriov-dpdk-vlan0
      namespace: kube-system
    spec:
      config: |-
        {
          "cniVersion": "0.3.1",
          "name": "sriov-dpdk",
          "type": "sriov",
          "vlan": 0
        }
    > EOF
    ```

## 创建 DPDK 测试 Pod

```shell
cat << EOF | kubectl apply -f -
> apiVersion: v1
kind: Pod
metadata:
  name: dpdk-demo
  annotations:
    k8s.v1.cni.cncf.io/networks: kube-system/sriov-dpdk-vlan0
spec:
  containers:
  - name: sriov-dpdk
    image: docker.io/bmcfall/dpdk-app-centos
    securityContext:
      privileged: true
    volumeMounts:
    - mountPath: /etc/podnetinfo
      name: podnetinfo
      readOnly: false
    - mountPath: /dev/hugepages
      name: hugepage
    resources:
      requests:
        memory: 1Gi
        #cpu: "4"
        intel.com/sriov_netdevice_dpdk: '1'
      limits:
        hugepages-1Gi: 2Gi
        #cpu: "4"
        intel.com/sriov_netdevice_dpdk: '1'
    # Uncomment to control which DPDK App is running in container.
    # If not provided, l3fwd is default.
    #   Options: l2fwd l3fwd testpmd
    env:
    - name: DPDK_SAMPLE_APP
      value: "testpmd"
    #
    # Uncomment to debug DPDK App or to run manually to change
    # DPDK command line options.
    command: ["sleep", "infinity"]
  volumes:
  - name: podnetinfo
    downwardAPI:
      items:
        - path: "labels"
          fieldRef:
            fieldPath: metadata.labels
        - path: "annotations"
          fieldRef:
            fieldPath: metadata.annotations
  - name: hugepage
    emptyDir:
      medium: HugePages
> EOF
```

等待 Pod Running，然后进入 Pod 中：

```shell
root@172-17-8-120:~# kubectl exec -it sriov-pod-2 sh
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
sh-4.4# dpdk-app
ENTER dpdk-app:
 argc=1
 dpdk-app
E1031 08:17:36.431877     116 resource.go:31] Error getting cpuset info: open /proc/116/root/sys/fs/cgroup/cpuset/cpuset.cpus: no such file or directory
E1031 08:17:36.432266     116 netutil_c_api.go:119] netlib.GetCPUInfo() err: open /proc/116/root/sys/fs/cgroup/cpuset/cpuset.cpus: no such file or directory
Couldn't get CPU info, err code: 1
  Interface[0]:
    IfName=""  Name="kube-system/k8s-pod-network"  Type=SR-IOV
    MAC=""  IP="10.244.5.197"  IP="fd00:10:244:0:eb50:e529:8533:7884"
    PCIAddress=0000:04:01.1
  Interface[1]:
    IfName="net1"  Name="kube-system/sriov-dpdk-vlan0"  Type=SR-IOV
    MAC=""

 myArgc=14
 dpdk-app -n 4 -l 1 --master-lcore 1 -w 0000:04:01.1 -- -p 0x1 -P --config="(0,0,1)" --parse-ptype
```

dpdk-app 会打印出当前 Pod 的相关信息，包括 eth0 的 IP、MAC 和 type 等。
其中值得注意: net1 网卡没有任何 IP 和 MAC 等网络信息，这符合 DPDK 的特性，不需要内核网络协议栈也能工作。
