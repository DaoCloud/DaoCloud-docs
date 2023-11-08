# 新手尝鲜在线安装 DCE 5.0 社区版

本页说明如何使用 kind 集群实现新手尝鲜在线安装 DCE 5.0 社区版。

!!! note

    点击[在线安装社区版](../../../videos/install.md#3)可观看视频演示。

## 准备工作

- 准备一台机器，机器资源建议：CPU > 8 核、内存 > 12 GB、磁盘空间 > 100 GB。
- 确保机器能够连通互联网。

执行如下脚本，检查系统资源和联网情况：

```shell
set -e
if [ $(free -g|grep Mem | awk '{print $2}')              -lt 12 ]; then (echo "insufficient memory! (should >=12G)";); fi
if [ $(grep 'processor' /proc/cpuinfo |sort |uniq |wc -l) -lt 8 ]; then (echo "insufficient CPU! (should >=8C)";); fi
if [ $(df -m / |tail -n 1 | awk '{print $4}') -lt 30720 ]; then (echo "insufficient free disk space of root partition!(should >=30G)";); fi
ping daocloud.io -c 1 &> /dev/null || ( echo "no connection to internet! abort.")
echo "precheck pass.."
```

预期输出类似于：

```none
precheck pass..
```

## 安装 Docker

> 如果您的机器已安装了 Docker 且版本高于 1.18，请跳过这一步。
>
> 安装 Docker 时可使用国内源：<https://developer.aliyun.com/mirror/docker-ce>

=== "如果是 CentOS"

    ```shell
    set -e
    if  [ -x "$(command -v docker )" ] ;then
        echo "docker already installed : version = "$(docker -v);
    else
        echo "docker not found, please install it first."
    fi
    
    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    sudo sed -i 's+download.docker.com+mirrors.aliyun.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo
    sudo yum makecache fast
    sudo yum -y install docker-ce
    sudo service docker start
    sudo systemctl enable docker
    sudo yum install -y wget
    ```

=== "如果是 Ubuntu"

    ```shell
    set -e
    if  [ -x "$(command -v docker )" ] ;then
        echo "docker already installed : version = "$(docker -v);
    else
        echo "docker not found, please install it first."
    fi
    sudo apt-get update
    sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository --yes "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get -y update
    sudo apt-get -y install docker-ce
    sudo apt-get -y install wget
    sudo service docker start
    sudo systemctl enable docker
    ```

请注意，如果机器上已有 Podman，但没有 Docker，依然需要安装 Docker。
这是因为一个已知问题：Podman 虽然可以启动 kind，但是会出现文件句柄不足的问题，并且重启会出现 IP 对不上的问题。

## 安装 kind 集群

1. 下载 kind 的二进制文件包。

    ```shell
    curl -Lo ./kind https://qiniu-download-public.daocloud.io/kind/v0.17.0/kind-linux-amd64
    chmod +x ./kind
    old_kind=$(which kind)
    if [ -f "$old_kind" ]; then mv ./kind $old_kind; else mv ./kind /usr/bin/kind ; fi
    ```

1. 查看 kind 版本。

    ```shell
    kind version
    ```

    预期输出如下：

    ```console
    kind v0.17.0 go1.19.2 linux/amd64
    ```

1. 设置 `kind_cluster.yaml` 配置文件。

    注意，暴露集群内的 32088 端口到 kind 对外的 8888 端口（可自行修改），配置文件示例如下：

    ```yaml title="kind_cluster.yaml"
    apiVersion: kind.x-k8s.io/v1alpha4
    kind: Cluster
    nodes:
    - role: control-plane
      extraPortMappings:
      - containerPort: 32088
        hostPort: 8888
    ```

1. 创建一个名为 `fire-kind-cluster` 的 K8s v1.25.3 示例集群。

    ```shell
    kind create cluster --image release.daocloud.io/kpanda/kindest-node:v1.25.3 --name=fire-kind-cluster --config=kind_cluster.yaml 
    ```

    预期输出如下：

    ```console
    Creating cluster "fire-kind-cluster" ...
     ✓ Ensuring node image (release.daocloud.io/kpanda/kindest-node:v1.25.3) 🖼 
     ✓ Preparing nodes 📦  
     ✓ Writing configuration 📜 
     ✓ Starting control-plane 🕹️ 
     ✓ Installing CNI 🔌 
     ✓ Installing StorageClass 💾 
    Set kubectl context to "kind-fire-kind-cluster"
    ```

1. 查看新创建的集群。

    ```shell
    kind get clusters
    ```

    预期输出如下：

    ```console
    fire-kind-cluster
    ```

## 安装 DCE 5.0 社区版

1. [安装依赖项](../../install-tools.md)。

    !!! note

        如果集群中已安装所有依赖项，请确保依赖项版本符合要求：
        
        - helm ≥ 3.11.1
        - skopeo ≥ 1.11.1
        - kubectl ≥ 1.25.6
        - yq ≥ 4.31.1

1. 在 kind 主机下载 dce5-installer 二进制文件。

    假定 VERSION 为 v0.12.0

    ```shell
    export VERSION=v0.12.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer
    ```

1. 获取 kind 所在主机的 IP，然后开始安装 DCE 5.0。

    ```shell
    myIP=$(ip -o route get 1.1.1.1 | cut -d " " -f 7)
    ./dce5-installer install-app -z -k $myIP:8888
    ```

    !!! note

        kind 集群仅支持 NodePort 模式。
        安装过程持续 30 分钟以上，具体取决于镜像拉取的网速。
        可通过以下命令观察安装过程中的 Pod 启动情况：

        ```shell
        docker exec -it fire-kind-cluster-control-plane kubectl get po -A -w
        ```

1. 安装完成后，命令行会提示安装成功。恭喜您！
   现在可以通过屏幕提示的 URL 使用 **默认的账号和密码（admin/changeme）** 探索全新的 DCE 5.0 啦！

    ![安装成功](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

!!! success

    - 请记录好提示的 URL，方便下次访问。
    - 成功安装 DCE 5.0 社区版后，请[申请社区免费体验](../../../dce/license0.md)。
    - 如果安装过程中遇到什么问题，欢迎扫描二维码，与开发者畅快交流：
    
        ![社区版交流群](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)
