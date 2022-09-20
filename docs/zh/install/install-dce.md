# 安装 DCE 5.0 社区版

本页简要说明 DCE 5.0 社区版的安装步骤。

!!! note

    点击[社区版部署 Demo](../videos/install.md)可观看视频演示。

## 准备工作

- 准备一个 k8s 集群，参阅[如何部署 k8s 集群](install-k8s.md)

    !!! note

        - 集群可用资源：CPU > 10 核、内存 > 12 GB、磁盘空间 > 100 GB（目前默认多副本运行，后续单副本预计资源消耗为 2 核 4 GB）
        - 集群版本：推荐 Kubernetes 官方最高稳定版本，目前推荐版本是 v1.24，最低版本支持 v1.21
        - 支持的 CRI：Docker、containerd
        - 存储：需要提前准备好 StorageClass，并设置为默认 SC。详情参见[部署 k8s 集群](install-k8s.md)
        - 目前仅支持 X86_64 架构
        - 确保集群已安装 CoreDNS
    
- [安装依赖项](install-tools.md)

    !!! note

        如果集群中已安装所有依赖项，请确保依赖项版本符合要求：

        - helm ≥ 3.9.4
        - skopeo ≥ 1.9.2
        - kubectl ≥ 1.22.0
        - yq ≥ 4.27.5

## 在线安装（推荐）

1. 在 k8s 集群控制平面节点（Master 节点）下载 dce5-installer 二进制文件。

    ```shell
    # 假定 VERSION 为 v0.3.12
    export VERSION=v0.3.12
    curl -Lo ./dce5-installer https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-${VERSION}
    ```

    为 `dce5-installer` 添加可执行权限：

    ```bash
    chmod +x dce5-installer
    ```

2. 设置配置文件 clusterConfig.yaml

    - 如果是非公有云环境（虚拟机、物理机），请启用负载均衡 (metallb)，以规避 NodePort 因节点 IP 变动造成的不稳定。请仔细规划您的网络，设置 2 个必要的 VIP，配置文件范例如下：

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
        loadBalancer: metallb
        istioGatewayVip: 10.6.229.10/32     # 这是 Istio gateway 的 VIP，也会是DCE5.0的控制台的浏览器访问IP
        insightVip: 10.6.229.11/32          # 这是 Global 集群的 Insight-Server 采集所有子集群的日志/指标/链路的网络路径所用的 VIP
        ```

    - 如果是公有云环境，并通过预先准备好的 Cloud Controller Manager 的机制提供了公有云的 k8s 负载均衡能力, 配置文件范例如下:

        ``` yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
        loadBalancer: cloudLB
        ```

    - 如果使用 NodePort 暴露控制台（PoC 方式），可以不指定任何 clusterConfig 文件，直接执行第 3 步。

3. 安装 DCE 5.0。

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```
    
    !!! note

        如果使用 NodePort 暴露控制台，则命令不需要指定 `-c` 参数。

4. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 探索全新的 DCE 5.0 啦！

    ![success](images/success.png)

    !!! note

         请记录好提示的 URL，方便下次访问。

## 离线安装

1. 下载社区版的对应离线包并解压。

    ``` bash
    # 假定版本 VERSION=0.3.12
    export VERSION=v0.3.12
    wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-${VERSION}.tar
    tar -zxvf offline-community-${VERSION}.tar
    ```

2. 导入镜像。

    !!! note
        
        这一步所用的脚本下载地址为： https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline_image_handler.sh

    - 如果使用镜像仓库，请将离线包的镜像推送到镜像仓库。

        ```bash
        # 指定镜像仓库地址, 比如:
        export REGISTRY_ADDR=registry.daocloud.io:30080
        # 指定离线包解压目录, 比如:
        export OFFLINE_DIR=$(pwd)/offline
        # 执行脚本导入镜像
        ./utils/offline_image_handler.sh import
        ```

        !!! note

            若导入镜像的过程出现失败, 则失败会被跳过且脚本将继续执行，
            失败镜像信息将被记录在脚本同级目录 `import_image_failed.list` 文件中，便于定位。

    - 如果没有镜像仓库，请将离线包拷贝到每一台节点之后，通过 `docker load/nerdctl load` 命令加载：

        ```shell
        # 指定离线包解压目录
        export OFFLINE_DIR=$(pwd)/offline
        # 执行脚本加载镜像
        ./utils/offline_image_handler.sh load
        ```

3. 解压安装。

    ``` shell
    ./dce5-installer install-app -c clusterConfig.yaml -p offline
    ```
    
    !!! note

        参数 -p 指定解压离线包的 offline 目录。

        有关 clusterConfig.yaml 文件设置，请参考上文的 **在线安装第 2 步** 。

4. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 探索全新的 DCE 5.0 啦！

    ![success](images/success.png)

    !!! note

         请记录好提示的 URL，方便下次访问。
