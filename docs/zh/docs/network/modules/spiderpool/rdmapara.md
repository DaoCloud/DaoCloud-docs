---
hide:
  - toc


---

# RDMA 环境准备及安装

本章节主要介绍安装 Spiderpool 时，RDMA 相关参数说明，目前 RDMA 支持如下两种使用方式：

1. 基于  Macvlan/IPVLAN CNI，使用 **RDMA Shared 模式**，暴露主机上的 RoCE 网卡给到 Pod 使用，需要部署 [Shared Device Plugin](https://github.com/Mellanox/k8s-rdma-shared-dev-plugin)来完成 RDMA 网卡资源的暴露和 Pod 调度

2. 基于 SR-IOV CNI， 使用 **RDMA Exclusive 模式**，暴露主机上的 RoCE 网卡给到 Pod 使用，需要使用 [RDMA CNI](https://github.com/k8snetworkplumbingwg/rdma-cni) 来完成 RDMA 设备隔离。

   详情参数配置请参考下文。

## 前提条件

1. 请确认集群环境中已具备 RDMA  设备。

2. 请确认集群中已对应的 OFED 驱动，本示例中采用具备 RoCE 功能的 mellanox ConnectX 5 网卡，可按照 [NVIDIA 官方指导](https://developer.nvidia.com/networking/ethernet-software) 安装最新的 OFED 驱动。使用如下命令，可查询到 RDMA 设备：

   ```
   rdma link show
   link mlx5_0/1 state ACTIVE physical_state LINK_UP netdev ens6f0np0
   link mlx5_1/1 state ACTIVE physical_state LINK_UP netdev ens6f1np1
   ```

   如基于 **SR-IOV CNI 隔离使用 RDMA 网卡**，请满足如下其一条件：

   - 内核版本要求 5.3.0 或更高版本，并在系统中加载 RDMA 模块。**rdma-core** 软件包提供了在系统启动时自动加载相关模块的功能。
   - Mellanox OFED 要求 4.7 或更高版本。此时不需要使用 5.3.0 或更新版本的内核。

   

## 基于 Mavlan /IPVLAN 共享 RoCE 网卡

1. 基于 Macvlan /IPVLAN 暴露 RoCE 网卡时，需要确认主机上的 RDMA 子系统工作在 **Shared 模式**下，否则，请切换到 **Shared 模式**。

   ```
   # 查看 RoCE 网卡模式
   rdma system
   netns shared copy-on-fork on
   
   # 切换到 shared 模式
   ~# rdma system set netns shared
   ```

2. 确认 RDMA 网卡的信息，用于后续 device plugin 发现设备资源。

   输入如下命令，可查看到：网卡 vendors 为 15b3，网卡 deviceIDs 为 1017,此信息在部署 SpiderPool 需要使用。

   ```
   ~# lspci -nn | grep Ethernet
   af:00.0 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
   af:00.1 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
   ```

3. 安装 SpiderPool 并配置 [Shared Device Plugin](https://github.com/Mellanox/k8s-rdma-shared-dev-plugin) 相关参数，部署详情请参考[安装 Spiderpool](install.md)

   | 参数                                             | 值                 | 说明                                                     |
   | ------------------------------------------------ | ------------------ | -------------------------------------------------------- |
   | RdmaSharedDevicePlugin.install                   | True               | 是否开启 **RdmaSharedDevicePlugin**                      |
   | rdmaSharedDevicePlugin.deviceConfig.resourceName | hca_shared_devices | 定义Shared RDMA Device 资源名称，创建Workload 时需要使用 |
   | rdmaSharedDevicePlugin.deviceConfig.deviceIDs    | 1017               | 设备 ID 号， 同上步骤 2 中查询信息一致                   |
   | rdmaSharedDevicePlugin.deviceConfig.vendors      | 15b3               | 网卡 Vendors 信息，同上步骤 2 中查询信息一致             |

   	![rdmamacvlan](../../images/rdma_macvlan01.jpg)

   成功部署后，可查看已安装组件。
   	![resource](../../images/rdma_macvlan02.jpg)

4. 安装完成后，可登录控制器节点，查看上报的 RDMA 设备资源。

   ```
   ~# kubectl get no -o json | jq -r '[.items[] | {name:.metadata.name, allocable:.status.allocatable}]'
     [
       {
         "name": "10-20-1-10",
         "allocable": {
           "cpu": "40",
           "memory": "263518036Ki",
           "pods": "110",
           "spidernet.io/hca_shared_devices": "500", # 可使用的 hca_shared_devices  数量
           ...
         }
       },
       ...
     ]
   
   ```

   如果上报的资源数为 0，可能的原因：

   - 请确认 Configmap **spiderpool-rdma-shared-device-plugin** 中的 **vendors** 和 **deviceID** 与实际相符

   - 查看 **rdma-shared-device-plugin** 的日志，对于支持 RDMA 网卡报错如下日志，可尝试在主机上安装 **apt-get install rdma-core** 或 **dnf install rdma-core**

     ```
     error creating new device: "missing RDMA device spec for device 0000:04:00.0, RDMA device \"issm\" not found"
     ```

5. 如果 SpiderPool 已成功部署，并且Device 资源已成功发现，则请完成如下操作：

   - 完成创建 Multus 实例，详情参考: [创建 Multus CR](../../config/multus-cr.md)
   - 完成创建 IP Pool，详情参考：[创建子网及 IP Pool](createpool.md)

6. 创建完成后，可使用此资源池创建 工作负载，详情请参考：[工作负载使用 RDMA](userdma.md)，更多使用方式请参考：[工作负载使用 IP 池](usage.md)

## 基于 SR-IOV 使用 RoCE 网卡

1. 基于 SR-IOV 暴露 RoCE 网卡时，需要确认主机上的 RDMA 子系统工作在 **exclusive 模式**下，否则，请切换到 **exclusive 模式**。

   ```
   # 切换到 exclusive 模式，重启主机后失效 
   ~# rdma system set netns exclusive
   
   # 持久化配置，修改后请重启机器
   ~# echo "options ib_core netns_mode=0" >> /etc/modprobe.d/ib_core.conf
   
   ~# rdma system
   netns exclusive copy-on-fork on
   ```

2. 确认网卡具备 SR-IOV 功能，查看支持的最大 VF 数量：

   ```
   ~# cat /sys/class/net/ens6f0np0/device/sriov_totalvfs
   8
   ```

3. 确认 RDMA 网卡的信息，用于后续 Device Plugin 发现设备资源。

   本演示环境，输入如下，网卡 **vendors** 为 15b3，网卡 **deviceIDs** 为 1017 ，步骤 6 中创建 **SriovNetworkNodePolicy** 需要使用

   ```
   ~# lspci -nn | grep Ethernet
   04:00.0 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
   04:00.1 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
   ```

4. 安装 SpiderPool 并开启 RDMA CNI,SR-IOV CNI。安装详情请参考:[安装 Spiderpool](install.md)

   | 参数                              | 值         | 说明                                                         |
   | --------------------------------- | ---------- | ------------------------------------------------------------ |
   | multus.multusCNI.defaultCniCRName | sriov-rdma | 默认 CNI 名称，指定 multus 默认使用的 CNI 的 NetworkAttachmentDefinition 实例名。<br />1. 如果 `multus.multusCNI.defaultCniCRName` 选项不为空，则安装后会自动生成一个数据为空的 NetworkAttachmentDefinition 对应实例。<br />2.如果 `multus.multusCNI.defaultCniCRName` 选项为空，会尝试通过 /etc/cni/net.d 目录下的第一个 CNI 配置来创建对应的 NetworkAttachmentDefinition 实例，否则会自动生成一个名为 `default` 的 NetworkAttachmentDefinition 实例，以完成 multus 的安装。 |
   | sriov.install                     | true       | 开启 SR-IOV CNI                                              |
   | plugins.installRdmaCNI            | true       | 开启 RDMA CNI                                                |

   ![sriov01](../../images/sriov01.jpg)

   ​	![sriov02](../../images/sriov02.jpg)

   ​	![sriov03](../../images/sriov03.jpg)

5. 完成后，安装的组件如下:
   ![sriov04](../../images/sriov04.jpg)

6. 如下**SriovNetworkNodePolicy**配置，使得 SR-IOV operator 能够在宿主机上创建出 VF，并上报资源
   YAML 配置；

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: policyrdma
     namespace: kube-system
   spec:
     nodeSelector:
       kubernetes.io/os: "linux"
     resourceName: mellanoxrdma  #自定义 resource 名称，创建应用时需要使用
     priority: 99
     numVfs: 8  # 可用的numVFS 数量，不能大于步骤 2 中查询的最大可用数
     nicSelector:
         deviceID: "1017" #步骤 3 中查询的设备 ID
         rootDevices: # 步骤 3 中查询的 rootDevices pfNames
         - 0000:04:00.0 
         vendor: "15b3" #步骤 3 中查询的网卡 vendors 
     deviceType: netdevice
     isRdma: true  # 需要开启 RDMA
   ```

   界面配置：
   ![sriov05](../../images/sriov05.jpg)

   ![sriov06](../../images/sriov06.jpg)

7. 安装完成后查看可用的设备资源：

   ```
   # kubectl get no -o json | jq -r '[.items[] | {name:.metadata.name, allocable:.status.allocatable}]'
   [
     {
       "name": "10-20-1-220",
       "allocable": {
         "cpu": "56",
         "ephemeral-storage": "3971227249029",
         "hugepages-1Gi": "0",
         "hugepages-2Mi": "0",
         "memory": "131779740Ki",
         "pods": "110",
         "spidernet.io/hca_shared_devices": "0",
         "spidernet.io/mellanoxrdma": "8", # 可用的设备资源
         ...
       }
     }
   ```

 8.如果 SpiderPool 已成功部署，并且Device 资源已成功发现，则请完成如下操作：

- 完成创建 Multus 实例，详情参考: [创建 Multus CR](../../config/multus-cr.md)
- 完成创建 IP Pool，详情参考：[创建子网及 IP Pool](createpool.md)

 创建完成后，可使用此资源池创建 工作负载，详情请参考：[工作负载使用 RDMA](userdma.md)，更多使用方式请参考：[工作负载使用 IP 池](usage.md)

