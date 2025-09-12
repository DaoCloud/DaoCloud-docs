# 工作负载使用 RDMA

本章节主要介绍介绍工作负载如何配置并使用 RDMA 资源。目前支持使用 RDMA 直通模式有三种方式，详情参考：[RDMA 使用方式对比](rdmatype.md)

!!! note

    本章内容基于 SR-IOV 使用 RoCE 网卡为例。为方便测试 RDMA，配置镜像需使用：
    `docker.io/mellanox/rping-test`，且运行 `sh` 命令，防止操作过程中 Pod 异常退出，详情参考下文。

## 前提条件

- [已成功部署 Spiderpool](../modules/spiderpool/install/install.md)
- [已完成 RDMA 安装及使用前准备](../modules/spiderpool/install/rdmapara.md)
- [已创建 Multus CR](multus-cr.md)
- [已创建 IPPool](./ippool/createpool.md)

## 界面操作

1. 登录平台 UI，在左侧导航栏点击 __容器管理__ -> __集群列表__ ，找到对应集群。然后，在左侧导航栏选择 __无状态负载__ ，点击 __镜像创建__ 。

    ![镜像创建](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool01.png)

1. 在 __创建无状态负载__ 页面，镜像使用 `docker.io/mellanox/rping-test`。`Replica` 设置为 `2`，部署一组跨节点 Pod。

1. 填写 __基本信息__ ，进入 __容器配置__ 输入如下信息。

    ![rdma_sriov](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/rdma_sriov01.jpg)

    - 网络资源参数：
      
        - 基于 Macvlan/VLAN CNI 使用 RDMA 时，资源名称为 [RDMA 安装及使用准备](../modules/spiderpool/install/rdmapara.md)中创建 Spiderpool 时
          自定义名称，详情参考 [基于 Macvlan/IPvlan 共享 ROCE 网卡](../modules/spiderpool/install/rdmapara.md#macvlan-ipvlan-roce)

        - 基于 SR-IOV CNI 使用 RDMA 时，资源名称为 `SriovNetworkNodePolicy` 中定义的 `resourceName`。
          详情参考[基于 SRI-OV 使用 ROCE 网卡](../modules/spiderpool/install/rdmapara.md#sr-iov-roce)。
    
        示例中的 `spidernet.io/mellnoxrdma` 为 __基于 SR-IOV 使用 RoCE 网卡__ 的示例。请求值和限制值目前保持一致，输入值不大于最大可用值。
        
    - 运行命令：为防止 Pod 启动异常退出， 添加如下运行命令:
    
        ```para
        - sh
        - -c
        - |
          ls -l /dev/infiniband /sys/class/net
          sleep 1000000
        ```

1. 完成 __容器配置__ -> __服务配置__ 页面的信息输入后。然后，进入 __高级配置__ ，点击配置 __容器网卡__ 。

    ![容器网卡](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool02.png)

1. 选择[已创建的 Multus CR](multus-cr.md)，关闭创建固定 IP 池功能，选择[已创建 IPPool](ippool/createpool.md)，点击 __确定__ ，完成创建。

    ![rdma_usage01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/rdma_usage01.jpg)
