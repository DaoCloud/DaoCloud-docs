# 安装 DCE 5.0 社区版

本页简要说明 DCE 5.0 社区版的安装步骤。

!!! note

    点击[社区版部署 Demo](../videos/install.md)可观看视频演示。

## 前提条件

- 准备一个 k8s 集群，参阅[如何部署 k8s 集群](install-k8s.md)
  
    - 集群可用资源：CPU > 10 核、内存 > 12 GB、磁盘空间 > 100 GB（目前默认为多副本运行，后续支持单副本后预计资源消耗为 2 核 4 GB）
    - 集群版本：推荐 Kubernetes 官方最高稳定版本，目前推荐版本是 v1.24，最低版本支持 v1.21
    - 支持的 CRI：Docker、containerd
    - 存储：需要提前准备好 StorageClass，并设置为默认 SC。详情参见[部署 k8s 集群](install-k8s.md)
    - 目前仅支持 X86_64 架构
    - 确保集群已安装 CoreDNS
    
- [安装依赖项](install-tools.md)

    !!! note

        如果您集群中已安装所有依赖项，请确保依赖项版本符合我们的要求：

        - helm ≥ 3.9.4
        - skopeo ≥ 1.9.2
        - kubectl ≥ 1.22.0
        - yq ≥ 4.27.5

## 在线安装步骤（建议）

1. 在 某一个 k8s 集群 Control Plane节点 下载 DCE 5.0 安装器二进制文件。

    ```shell
    # 假定 VERSION 为 v0.3.12
    export VERSION=v0.3.12
    curl -Lo ./dce5-installer https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-${VERSION}
    ```

    为 `dce5-installer` 添加可执行权限：

    ```bash
    chmod +x dce5-installer
    ```

2. 设置配置文件 clusterConfig.yaml。

    - 如果使用 NodePort 暴露控制台（PoC 方式），可以不指定任何 clusterConfig 文件，直接执行第 3 步。

    - 如果是非公有云环境（虚拟机、物理机），请启用负载均衡 (metallb)，以规避 NodePort 因节点 IP 变动造成的不稳定。请仔细规划您的网络，设置 2 个必要的 VIP，配置文件范例如下：

        ```yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
        LoadBalancer: metallb
        istioGatewayVip: 10.6.229.10/32     # 这是 Istio gateway 的 VIP，也会是DCE5.0的控制台的浏览器访问IP
        insightVip: 10.6.229.11/32          # 这是 Global 集群的 Insight-Server 采集所有子集群的日志/指标/链路的网络路径所用的 VIP
        ```

    - 如果是公有云环境，并通过预先准备好的 Cloud Controller Manager 的机制提供了公有云的 k8s 负载均衡能力, 配置文件范例如下:

        ``` yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
        LoadBalancer: cloudLB
        ```

3. 安装 DCE 5.0，执行以下命令：

    > 如果使用 NodePort 暴露控制台，则如下命令不需要指定 `-c` 参数。

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```

4. 安装完成后，命令行会提示安装成功，您可以通过提供的 URL 访问 DCE 5.0 控制台。

   ![success](images/success.png)

## 离线安装步骤

1. 下载社区版的对应离线包并解压。

    ``` bash
    # 假定版本 VERSION=0.3.12
    export VERSION=v0.3.12
    wget https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-community-${VERSION}.tar
    tar -zxvf offline-community-${VERSION}.tar
    ```

2. 导入镜像。

    > 下文所有脚本下载地址： https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline_image_handler.sh

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

    - 如果没有镜像仓库，请将离线包拷贝到每一台节点之后，通过 `docker load/nerdctl load` 加载:

        ```shell
        # 指定离线包解压目录, 比如:
        export OFFLINE_DIR=$(pwd)/offline
        # 执行脚本加载镜像
        ./utils/offline_image_handler.sh load
        ```

3. 执行安装命令，通过 -p 指定解压离线包的 offline 目录，其中 clusterConfig.yaml 文件配置参考 **在线安装第 2 步** 说明。

    ``` shell
    ./dce5-installer install-app -c clusterConfig.yaml -p offline
    ```

4. 安装完成后，命令行会提示安装成功，您可以通过提供的 URL 访问 DCE 5.0 控制台。

## 卸载

卸载 DCE 5.0 将会从您的集群中上移除，卸载过程中不会进行任何备份，请谨慎操作。请执行以下命令：

```shell
kubectl -n mcamel-system delete mysql mcamel-common-mysql-cluster
kubectl -n mcamel-system delete elasticsearches mcamel-common-es-cluster-masters
kubectl -n mcamel-system delete redisfailover mcamel-common-redis-cluster
kubectl -n ghippo-system delete gateway ghippo-gateway
kubectl -n istio-system delete requestauthentications ghippo
helm -n mcamel-system  uninstall eck-operator mysql-operator redis-operator
helm -n ghippo-system  uninstall ghippo
helm -n insight-system uninstall insight-agent insight
helm -n ipavo-system   uninstall ipavo
helm -n kpanda-system  uninstall kpanda
helm -n istio-system   uninstall istio-base istio-ingressgateway istiod
```

