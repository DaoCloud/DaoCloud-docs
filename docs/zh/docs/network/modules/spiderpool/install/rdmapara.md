# RDMA 环境准备及安装

本章节主要介绍安装 Spiderpool 时，RDMA 相关参数说明，目前 RDMA 支持如下两种使用方式：

- 基于 Macvlan/IPvlan CNI，使用 **RDMA Shared 模式** ，暴露主机上的 RoCE 网卡给 Pod 使用，
  需要部署 [Shared Device Plugin](https://github.com/Mellanox/k8s-rdma-shared-dev-plugin)来完成
  RDMA 网卡资源的暴露和 Pod 调度。

- 基于 SR-IOV CNI，使用 **RDMA Exclusive 模式** ，暴露主机上的 RoCE 网卡给 Pod 使用，
  需要使用 [RDMA CNI](https://github.com/k8snetworkplumbingwg/rdma-cni) 来完成 RDMA 设备隔离。

以下是上面两种 RDMA 使用方式的区别:

| 比较维度     | Macvlan/IPvlan 共享 RDMA 方案           | SR-IOV CNI 隔离 RDMA 方案          |
| ------------| ------------------------------------- | --------------------------------- |
| 网络隔离      | 所有容器共享 RDMA 设备，隔离性较差        | 容器独享 RDMA 设备，隔离性较好        |
| 性能         | 性能较高                               | 硬件直通，性能最优                   |
| 资源利用率    | 资源利用率较高                          | 较低，受硬件支持的 VFs 数量限制       |
| 使用复杂度    | 配置相对简单                            | 配置较为复杂，需要硬件支持和配置       |
| 兼容性       | 兼容性较好，适用于大多数环境               | 依赖硬件支持，兼容性较差              |
| 适用场景      | 适用于大多数场景，包括裸金属，虚拟机等      | 只适用于裸金属，不适用于虚拟机场景     |
| 成本         | 成本较低，因为不需要额外的硬件支持          | 成本较高，需要支持 SR-IOV 的硬件设备 |
| RDMA 协议支持 | 支持 Roce 协议, 不支持 Ininiband 协议    | 支持 Roce 和 Infiniband 协议        |

如果您的硬件支持 SR-IOV, 优先推荐使用基于 [SR-IOV CNI 的 **RDMA Exclusive 模式**](#基于-sr-iov-使用-roce-网卡) ，这具有更好的隔离型，更好的性能。并且 Spiderpool 同时提供了 RDMA exporter 功能和 grafana 监控面板，通过实时监控 Pod/Node RDMA 网络的性能，包括吞吐量、延迟、丢包率等，可以时发现问题并采取措施解决，提高网络的可靠性和性能。

## 前提条件

1. 请确认集群环境中已具备 RDMA 设备。

2. 请确认集群中节点具备 RoCE 功能的 mellanox 网卡，本示例中采用 mellanox ConnectX 5 型号网卡。
   并且已安装对应的 OFED 驱动，如未安装，可参考 [安装 OFED 驱动](./ofed_driver.md)文档安装驱动。

## 基于 Macvlan /IPvlan 共享 RoCE 网卡

注意: Macvlan/IPvlan 不支持 Infiniband 网卡。

1. 基于 Macvlan/IPvlan 暴露 RoCE 网卡时，需要确认主机上的 RDMA 子系统工作在 **Shared 模式** 下，否则，请切换到 **Shared 模式** 。

    ```sh
    # 查看 RoCE 网卡模式
    rdma system
    netns shared copy-on-fork on
   
    # 切换到 shared 模式
    rdma system set netns shared
    ```

1. 确认 RDMA 网卡的信息，用于后续 device plugin 发现设备资源。

    输入如下命令，可查看到：网卡 vendors 为 15b3，网卡 deviceIDs 为 1017。
    此信息在部署 Spiderpool 时需要用到。

    ```sh
    $ lspci -nn | grep Ethernet
    af:00.0 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    af:00.1 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    ```

1. 安装 Spiderpool 并配置 [Shared Device Plugin](https://github.com/Mellanox/k8s-rdma-shared-dev-plugin)
   相关参数，部署详情请参考[安装 Spiderpool](install.md)。

    | 参数                                    | 值              | 说明 |
    | --------------------------------------- | -------------- | --- |
    | RdmaSharedDevicePlugin.install          | True           | 是否开启 **RdmaSharedDevicePlugin** |
    | rdmaSharedDevicePlugin.deviceConfig.resourceName | hca_shared_devices | 定义 Shared RDMA Device 资源名称，创建 Workload 时需要使用 |
    | rdmaSharedDevicePlugin.deviceConfig.deviceIDs    | 1017 | 设备 ID 号，同上一步查询的信息一致 |
    | rdmaSharedDevicePlugin.deviceConfig.vendors     | 15b3 | 网卡 Vendors 信息，同上一步查询的信息一致 |

    ![rdmamacvlan](../../../images/rdma_macvlan01.png)

    成功部署后，可查看已安装组件。

    ![resource](../../../images/rdma_macvlan02.png)

1. 安装完成后，可登录控制器节点，查看上报的 RDMA 设备资源。

    ```sh
    kubectl get no -o json | jq -r '[.items[] | {name:.metadata.name, allocable:.status.allocatable}]'
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
    - 查看 **rdma-shared-device-plugin** 的日志。对于支持 RDMA 的网卡，如果日志中有如下报错，
      可尝试在主机上运行 `apt-get install rdma-core` 或 `dnf install rdma-core` 来安装 rdma-core

    ```console
    error creating new device: "missing RDMA device spec for device 0000:04:00.0, RDMA device \"issm\" not found"
    ```

1. 如果 Spiderpool 已成功部署，并且 Device 资源已成功发现，则请完成如下操作：

    - 完成创建 Multus 实例，详情参考[创建 Multus CR](../../../config/multus-cr.md)
    - 完成创建 IP Pool，详情参考[创建子网及 IP Pool](../../../config/ippool/createpool.md)

1. 创建完成后，可使用此资源池创建工作负载，详情请参考[工作负载使用 RDMA](../../../config/userdma.md)。
   更多使用方式请参考[工作负载使用 IP 池](../../../config/use-ippool/usage.md)。

## 基于 SR-IOV 使用 RoCE 网卡

1. 基于 SR-IOV 暴露 RoCE 网卡时，需要确认主机上的 RDMA 子系统工作在 **exclusive 模式** 下，否则，请切换到 **exclusive 模式** 。

    ```sh
    # 切换到 exclusive 模式，重启主机后失效 
    rdma system set netns exclusive
   
    # 持久化配置，修改后请重启机器
    echo "options ib_core netns_mode=0" >> /etc/modprobe.d/ib_core.conf
   
    rdma system
    netns exclusive copy-on-fork on
    ```

2. 确认网卡具备 SR-IOV 功能，查看支持的最大 VF 数量：

    ```sh
    cat /sys/class/net/ens6f0np0/device/sriov_totalvfs
    ```

    输出类似于：

    ```output
    8
    ```

3. 确认 RDMA 网卡的信息，用于后续 Device Plugin 发现设备资源。

    在本演示环境中，网卡 **vendors** 为 15b3，网卡 **deviceIDs** 为 1017。
    在后续步骤创建 **SriovNetworkNodePolicy** 时需要用到这些信息。

    ```sh
    lspci -nn | grep Mellanox
    ```

    输出类似于：

    ```output
    04:00.0 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    04:00.1 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    ```

4. 安装 Spiderpool 并开启 RDMA CNI、SR-IOV CNI, 推荐开启 Spiderpool-agent RDMA 监控功能，安装详情请参考[安装 Spiderpool](install.md)。

    <table>
      <tr>
        <th>参数</th>
        <th>值</th>
        <th>说明</th>
      </tr>
      <tr>
        <td>multus.multusCNI.defaultCniCRName</td>
        <td>sriov-rdma</td>
        <td>
          默认 CNI 名称，指定 multus 默认使用的 CNI 的 NetworkAttachmentDefinition 实例名。<br />
          <ul>
            <li>
              如果 <code>multus.multusCNI.defaultCniCRName</code> 选项不为空，则安装后会自动生成一个数据为空的 NetworkAttachmentDefinition 对应实例。
            </li>
            <li>
              如果 <code>multus.multusCNI.defaultCniCRName</code> 选项为空，会尝试通过 <code>/etc/cni/net.d</code> 目录下的第一个 CNI 配置来创建对应的 NetworkAttachmentDefinition 实例，否则会自动生成一个名为 <code>default</code> 的 NetworkAttachmentDefinition 实例，以完成 multus 的安装。
            </li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>sriov.install</td>
        <td>true</td>
        <td>开启 SR-IOV CNI</td>
      </tr>
      <tr>
        <td>plugins.installRdmaCNI</td>
        <td>true</td>
        <td>开启 RDMA CNI</td>
      </tr>
    </table>

    ![sriov01](../../../images/sriov01.png)

    ![sriov02](../../../images/sriov02.png)

    ![sriov03](../../../images/sriov03.png)

5. 完成后，安装的组件如下：

    ![sriov04](../../../images/sriov04.png)

6. 参考如下 **SriovNetworkNodePolicy** 配置，使得 SR-IOV Operator 能够在宿主机上创建出 VF，并上报资源

    YAML 配置示例如下：

    ```yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: policyrdma
      namespace: kube-system
    spec:
      nodeSelector:
        kubernetes.io/os: "linux"
      resourceName: mellanoxrdma  # 自定义 resource 名称，创建应用时需要使用
      priority: 99
      numVfs: 8  # 可用的numVFS 数量，不能大于步骤 2 中查询的最大可用数
      nicSelector:
        deviceID: "1017" # 步骤 3 中查询的设备 ID
        rootDevices: # 步骤 3 中查询的 rootDevices pfNames
        - 0000:04:00.0 
        vendor: "15b3" # 步骤 3 中查询的网卡 vendors 
      deviceType: netdevice
      isRdma: true  # 需要开启 RDMA
    ```

    界面配置：

    ![sriov05](../../../images/sriov05.png)

    ![sriov06](../../../images/sriov06.png)

7. 安装完成后查看可用的设备资源：

    ```sh
    kubectl get no -o json | jq -r '[.items[] | {name:.metadata.name, allocable:.status.allocatable}]'
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

8. 如果 Spiderpool 已成功部署，并且 Device 资源已成功发现，则请完成如下操作：

    - 完成创建 Multus 实例，详情参考[创建 Multus CR](../../../config/multus-cr.md)
    - 完成创建 IP Pool，详情参考[创建子网及 IP Pool](../../../config/ippool/createpool.md)

    创建完成后，可使用此资源池创建工作负载，详情请参考[工作负载使用 RDMA](../../../config/userdma.md)。
    更多使用方式请参考[工作负载使用 IP 池](../../../config/use-ippool/usage.md)。
