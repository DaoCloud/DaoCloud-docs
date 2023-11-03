# 已有 Kubernetes 集群离线安装社区版

本页简要说明如何在已有 Kubernetes 集群上离线安装 DCE 5.0 社区版。

点击[社区版部署 Demo](../../../videos/install.md)可观看视频演示。

## 准备工作

- 准备一个 Kubernetes 集群，集群配置请参考文档[资源规划](../resources.md)。

    - 存储：需要提前准备好 StorageClass，并设置为默认 SC
    - 确保集群已安装 CoreDNS
    - 如果是单节点集群，请确保您已移除该节点的污点

- [安装依赖项](../../install-tools.md)。

    如果集群中已安装所有依赖项，请确保依赖项版本符合要求：
        
    - helm ≥ 3.11.1
    - skopeo ≥ 1.11.1
    - kubectl ≥ 1.25.6
    - yq ≥ 4.31.1

## 下载和安装

1. 在 k8s 集群控制平面节点（Controller Node）下载社区版的对应离线包并解压，
   或者从[下载中心](../../../download/index.md)下载离线包并解压。

    假定版本 VERSION=0.12.0

    ```bash
    export VERSION=v0.12.0
    wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-$VERSION-amd64.tar
    tar -xvf offline-community-$VERSION-amd64.tar
    ```

1. 设置集群配置文件 clusterConfig.yaml

    - 如果是非公有云环境（虚拟机、物理机），请启用负载均衡 (metallb)，以规避 NodePort 因节点 IP 变动造成的不稳定。请仔细规划您的网络，设置 2 个必要的 VIP，配置文件范例如下：

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: metallb
            istioGatewayVip: 10.6.229.10/32
            insightVip: 10.6.229.11/32      
          fullPackagePath: absolute-path-of-the-offline-directory # 解压离线包后的路径
          imagesAndCharts:        # 镜像仓库
            type: external 
            externalImageRepo: your-external-registry # 镜像仓库地址，必须是 http 或者 https
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
        ```

    - 如果是公有云环境，并通过预先准备好的 Cloud Controller Manager 的机制提供了公有云的 k8s 负载均衡能力, 配置文件范例如下:

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: cloudLB
          fullPackagePath: absolute-path-of-the-offline-directory # 解压离线包后的路径
          imagesAndCharts:        # 镜像仓库
            type: external 
            externalImageRepo: your-external-registry # 镜像仓库地址，必须是 http 或者 https
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
        ```

    - 如果使用 NodePort 暴露控制台（仅推荐 PoC 使用），配置文件范例如下:

        ```yaml title="clusterConfig.yaml"
        apiVersion: provision.daocloud.io/v1alpha3
        kind: ClusterConfig
        spec:
          loadBalancer:
            type: NodePort
          fullPackagePath: absolute-path-of-the-offline-directory # 解压离线包后的路径
          imagesAndCharts:        # 镜像仓库
            type: external 
            externalImageRepo: your-external-registry # 镜像仓库地址，必须是 http 或者 https
            # externalImageRepoUsername: admin
            # externalImageRepoPassword: Harbor123456
        ```

1. 安装 DCE 5.0。

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```

    !!! note

        - 有关 clusterConfig.yaml 文件设置，请参考[在线安装第 2 步](online.md#_2)。
        - `-z` 最小化安装
        - `-c` 指定集群配置文件。使用 NodePort 暴露控制台时不需要指定 `-c`。
        - `-d` 开启 debug 模式
        - `--serial` 指定后所有安装任务串行执行

1. 安装完成后，命令行会提示安装成功。恭喜您！
   现在可以通过屏幕提示的 URL 使用默认的账号和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        请记录好提示的 URL，方便下次访问。

1. 另外，安装 DCE 5.0 成功之后，您需要正版授权后使用，请参考[申请社区免费体验](../../../dce/license0.md)。
