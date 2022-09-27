# 离线安装 DCE 5.0 社区版

本页简要说明 DCE 5.0 社区版的离线安装步骤。

!!! note

    点击[社区版部署 Demo](../videos/install.md)可观看视频演示。

## 准备工作

- 准备一个 Kubernetes 集群，参阅[如何部署 Kubernetes 集群](install-k8s.md)

    !!! note

        - 集群可用资源：CPU > 10 核、内存 > 12 GB、磁盘空间 > 100 GB（目前默认多副本运行，后续单副本预计资源消耗为 2 核 4 GB）
        - 集群版本：推荐 Kubernetes 官方最高稳定版本，目前推荐版本是 v1.24，最低版本支持 v1.21
        - 支持的 CRI：Docker、containerd
        - 存储：需要提前准备好 StorageClass，并设置为默认 SC。详情参见[部署 Kubernetes 集群](install-k8s.md)
        - 目前仅支持 X86_64 架构
        - 确保集群已安装 CoreDNS
    
- [安装依赖项](install-tools.md)

    !!! note

        如果集群中已安装所有依赖项，请确保依赖项版本符合要求：
        
        - helm ≥ 3.9.4
        - skopeo ≥ 1.9.2
        - kubectl ≥ 1.22.0
        - yq ≥ 4.27.5

## 离线安装

1. 下载社区版的对应离线包并解压。

    ``` bash
    # 假定版本 VERSION=0.3.18
    export VERSION=v0.3.18
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
        ./offline_image_handler.sh import
        ```
    
        !!! note
    
            若导入镜像的过程出现失败, 则失败会被跳过且脚本将继续执行，
            失败镜像信息将被记录在脚本同级目录 `import_image_failed.list` 文件中，便于定位。
        
        如果 docker pull 镜像时报错：http: server gave HTTP response to HTTPS client，
        请启用 Insecure Registry：
            
        - 在集群的每个节点上运行 `vim /etc/docker/daemon.json` 命令以编辑 daemon.json 文件，输入以下内容并保存更改。

            ```shell
            {
            "insecure-registries" : ["172.30.120.180:80"]
            }
            ```

            !!! note

                请确保将 `172.30.120.180:80` 替换为您自己的 Harbor 仓库地址。对于 Linux，daemon.json 文件的路径为 /etc/docker/daemon.json。

        - 运行以下命令重启 Docker。

            ```bash
            sudo systemctl daemon-reload
            sudo systemctl restart docker
            ```

    - 如果没有镜像仓库，请将离线包拷贝到每一台节点之后，通过 `docker load/nerdctl load` 命令加载：
    
        ```shell
        # 指定离线包解压目录
        export OFFLINE_DIR=$(pwd)/offline
        # 执行脚本加载镜像
        ./offline_image_handler.sh load
        ```
    
3. 解压安装。

    ``` shell
    ./dce5-installer install-app -c clusterConfig.yaml -p offline
    ```
    
    !!! note

        参数 -p 指定解压离线包的 offline 目录。
        
        有关 clusterConfig.yaml 文件设置，请参考上文的 **在线安装第 2 步** 。

4. 安装完成后，命令行会提示安装成功。恭喜您！:smile: 现在可以通过屏幕提示的 URL 使用默认的账户和密码（admin/changeme）探索全新的 DCE 5.0 啦！

    ![success](images/success.png)

    !!! success

         请记录好提示的 URL，方便下次访问。

5. 另外，安装 DCE 5.0 成功之后，您需要正版授权后使用，请参考[申请社区免费体验](../dce/license0.md)。
