# 在线安装 DCE 5.0 社区版

本页简要说明 DCE 5.0 社区版的在线安装步骤。

!!! note

    点击[社区版部署 Demo](../videos/install.md)可观看视频演示。

    如果需要离线安装，请查阅[离线安装步骤](offline-install-community.md)。

## 准备工作

- 准备一个 K8s 集群

    !!! note

        - 集群可用资源：CPU > 10 核、内存 > 12 GB、磁盘空间 > 100 GB（目前默认多副本运行，后续单副本预计资源消耗为 4 核 8 GB）
        - 集群版本：推荐 Kubernetes 官方最高稳定版本，目前推荐版本是 v1.24，最低版本支持 v1.20
        - 支持的 CRI：Docker、containerd
        - 存储：需要提前准备好 StorageClass，并设置为默认 SC
        - 目前仅支持 X86_64 架构
        - 确保集群已安装 CoreDNS
        - 如果是单节点集群，请确保您已移除该节点的污点

- [安装依赖项](install-tools.md)

    !!! note

        如果集群中已安装所有依赖项，请确保依赖项版本符合要求：
        
        - helm ≥ 3.9.4
        - skopeo ≥ 1.9.2
        - kubectl ≥ 1.22.0
        - yq ≥ 4.27.5

## 在线安装（推荐）

1. 在 K8s 集群控制平面节点（Master 节点）下载 dce5-installer 二进制文件。

    ```shell
    # 假定 VERSION 为 v0.3.24
    export VERSION=v0.3.24
    curl -Lo ./dce5-installer  https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
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
          istioGatewayVip: 10.6.229.10/32     # 这是 Istio gateway 的 VIP，也会是DCE 5.0的控制台的浏览器访问IP
          insightVip: 10.6.229.11/32          # 这是 Global 集群的 Insight-Server 采集所有子集群的监控指标的网络路径所用的 VIP
        ```

    - 如果是公有云环境，并通过预先准备好的 Cloud Controller Manager 的机制提供了公有云的 K8s 负载均衡能力, 配置文件范例如下:

        ``` yaml
        apiVersion: provision.daocloud.io/v1alpha1
        kind: ClusterConfig
        spec:
          loadBalancer: cloudLB
        ```

    - 如果使用 NodePort 暴露控制台（仅推荐 PoC 使用），直接执行第 3 步。

3. 安装 DCE 5.0。

    ```shell
    ./dce5-installer install-app -c clusterConfig.yaml
    ```

    !!! note

        如果使用 NodePort 暴露控制台，则命令不需要指定 `-c` 参数。

4. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](images/success.png)

    !!! success

         请记录好提示的 URL，方便下次访问。

5. 另外，安装 DCE 5.0 成功之后，您需要正版授权后使用，请参考[申请社区免费体验](../dce/license0.md)。

## 在 Kind 集群中安装

!!! note

    如果是 kind 内的环境，仅可使用 NodePort 模式。

1. 确保 kind 创建集群时，暴露集群内的 32000 端口(固定)到 kind 对外的 8888 端口（可自行修改），kind 配置文件如下：
        
    ``` yaml
    apiVersion: provision.daocloud.io/v1alpha1
    kind: ClusterConfig
    spec:
      loadBalancer: cloudLB
    ```

2. 获取 kind 所在主机的 IP，假定为 `10.6.3.1`，进行安装。

    ```shell
    ./dce5-installer install-app -z -k 10.6.3.1:8888
    ```

3. 安装成功后，您可以前往 `https://10.6.3.1:8888` 访问 DCE 5.0！

!!! note

    如果安装过程中遇到什么问题，欢迎扫描二维码，与开发者畅快交流：

    ![社区版交流群](images/wechat.png)
