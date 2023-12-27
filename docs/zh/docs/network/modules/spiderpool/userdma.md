# 工作负载使用 RDMA

本章节主要介绍介绍工作负载如何配置并使用 RDMA 资源

## 前提条件
1. [SpiderPool 已成功部署](../../modules/spiderpool/install.md)。
2. [完成RDMA 安装及使用前准备](rdmapara.md)。
3. [已创建 的Multus CR](../../config/multus-cr.md)
4. [已创建 IP Pool](createpool.md)
## 界面操作
1. 登录平台 UI，在左侧导航栏点击`容器管理`->`集群列表`，找到对应集群。然后，在左侧导航栏选择`无状态负载`，点击`镜像创建`。
   ![镜像创建](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool01.png)
2. 在`创建无状态负载`页面，镜像使用：`docker.io/mellanox/rping-test`。 `Replica` 设置为 `2`，部署一组跨节点 Pod。
3. 完成`基本信息`、进入`容器配置`完成如下信息输入。
   ![rdma_sriov](../../images/rdma_sriov01.jpg)
   `网络资源参数`：资源名称为 [RDMA 安装及使用准备 ](rdmapara.md) 中创建 spiderPool 时自定义名称，如示例中的`spidernet.io/mellnoxrdma` 为 **基于 SRIOV 使用 RoCE 网卡**  的示例。请求值和限制值目前保持一致，输入值不大于 最大可用值 。详情参考：RDMA 安装及使用准备 
   `运行命令`：添加如下内容:
   ```
   - sh
           - -c
           - |
             ls -l /dev/infiniband /sys/class/net
             sleep 1000000
   ```
4. 完成`容器配置`、`服务配置`页面的信息输入后。然后，进入`高级配置`，点击配置`容器网卡`。
   ![容器网卡](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool02.png)
5. 选择 [已创建 的Multus CR](../../config/multus-cr.md)，关闭创建固定 IP 池功能，选择[已创建 IP Pool](createpool.md)，点击确定，完成创建。
   ![rdma_usage01](../../images/rdma_usage01.jpg)
6. 部署完成后，打开Pod Console 可验证Pod 之间的通信能力。
   ```
    ib_read_lat 172.50.0.67
   ```
   ![rdma_usage](../../images/rdma_usage02.jpg)

