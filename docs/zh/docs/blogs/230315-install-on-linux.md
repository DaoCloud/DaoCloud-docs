# Linux 单机在线体验 DCE 5.0 社区版

本页说明如何通过 Docker 和 kind 在一台 Linux 机器上在线安装单机 DCE 5.0 社区版。

!!! tip

    这是一种极简安装方式，便于学习和体验，性能优于 [macOS 单机版](230315-install-on-macos.md)。原文作者是 [panpan0000](https://github.com/panpan0000)。

## 准备工作

- 准备一台 Linux 机器，资源建议：CPU > 8 核、内存 > 12 GB、磁盘空间 > 100 GB
- 确保这台机器能够连通公网
- 操作系统：CentOS 7 或 Ubuntu 22.04

检查系统资源和联网情况：

```bash
set -e
if [ $(free -g|grep Mem | awk '{print $2}')              -lt 12 ]; then (echo "insufficient memory! (should >=12G)"; exit 1); fi
if [ $(grep 'processor' /proc/cpuinfo |sort |uniq |wc -l) -lt 8 ]; then (echo "insufficient CPU! (should >=8C)"; exit 1); fi
if [ $(df -m / |tail -n 1 | awk '{print $4}') -lt 30720 ]; then (echo "insufficient free disk space of root partition!(should >=30G)"; exit 1); fi
ping daocloud.io -c 1 &> /dev/null || ( echo "no connection to internet! abort." &&  exit 1; )
echo "precheck pass.."
```

预期输出如下：

```console
precheck pass..
```

## 安装 Docker

如果主机上已有 Docker，并且版本高于 1.18，则可跳过此步骤。

=== "CentOS"

    依次执行以下命令，大概需要 5 分钟左右：

    ```bash
    set -e
    if  [ -x "$(command -v docker )" ] ;then
      echo "docker already installed : version = "$(docker -v);
      exit 0
    fi
    ```
    ```bash
    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    sudo sed -i 's+download.docker.com+mirrors.aliyun.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo
    sudo yum makecache fast
    sudo yum -y install docker-ce
    sudo service docker start
    sudo systemctl enable docker
    sudo yum install -y wget
    ```

=== "Ubuntu"

    依次执行以下命令，大概需要 5 分钟左右：

    ```bash
    set -e
    if  [ -x "$(command -v docker )" ] ;then
      echo "docker already installed : version = "$(docker -v);
      exit 0
    fi
    ```
    ```bash
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

!!! note

    - 如果机器上已有 Podman，但是没有 Docker，仍需要安装 Docker。
    - 这是因为一个已知问题：Podman 虽然可以启动 kind，但是会出现文件句柄不足的问题，并且重启会出现 IP 对不上的问题。
    - Docker 安装问题请参阅 [Docker 官方安装说明](https://docs.docker.com/desktop/install/linux-install/)。

## kind 集群

1. 下载 kind 的二进制文件包。

    ```bash
    curl -Lo ./kind https://qiniu-download-public.daocloud.io/kind/v0.17.0/kind-linux-amd64
    chmod +x ./kind
    old_kind=$(which kind)
    if [ -f "$old_kind" ]; then mv ./kind $old_kind; else mv ./kind /usr/bin/kind ; fi
    ```

    查看 kind 版本：

    ```bash
    kind version
    ```

    预期输出如下：

    ```console
    kind v0.17.0 go1.19.2 linux/amd64
    ```

1. 创建 `kind_cluster.yaml` 配置文件。暴露集群内的 32088 端口到 kind 对外的 8888 端口（可自行修改）。

    ```bash
    cat > kind_cluster.yaml << EOF
    apiVersion: kind.x-k8s.io/v1alpha4
    kind: Cluster
    nodes:
    - role: control-plane
      extraPortMappings:
      - containerPort: 32088
        hostPort: 8888
    EOF
    ```

1. 通过 kind 创建一个名为 `fire-kind-cluster` 的 K8s 集群，以 k8s 1.25.3 为例。

    ```bash
    kind create cluster --image docker.m.daocloud.io/kindest/node:v1.25.3  --name=fire-kind-cluster --config=kind_cluster.yaml 
    ```

    此步骤大概需要 3~5 分钟，取决于镜像下载的网速。预期输出如下：

    ```console
    Creating cluster "fire-kind-cluster" ...
     ✓ Ensuring node image (docker.m.daocloud.io/kindest/node:v1.25.3) 🖼 
     ✓ Preparing nodes 📦  
     ✓ Writing configuration 📜 
     ✓ Starting control-plane 🕹️ 
     ✓ Installing CNI 🔌 
     ✓ Installing StorageClass 💾 
    Set kubectl context to "kind-fire-kind-cluster"
    ```

1. 查看新创建的 kind 集群。

    ```console
    kind get clusters
    ```

    预期输出如下：

    ```console
    fire-kind-cluster
    ```

## 安装 DCE 5.0 社区版

1. 安装依赖项，另请参阅[依赖项安装说明](../install/install-tools.md)

    ```shell
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
    bash install_prerequisite.sh online community 
    ```

1. 在主机下载 dce5-installer 二进制文件（也可以[通过浏览器下载](../download/index.md)）

    ```shell
    export VERSION=v0.5.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer 
    ```

1. 执行以下命令开始安装。

    ```shell
    myIP=$(ip -o route get 1.1.1.1 | cut -d " " -f 7)
    ./dce5-installer install-app -z -k $myIP:8888
    ```

    !!! note

        - kind 集群仅支持 NodePort 模式。
        - 如果是公有云机器，则只能手动指定公网 IP：`./dce5-installer install-app -z -k {公网IP}:8888`

1. 安装完成后，命令行会提示安装成功。恭喜您！

    现在可以通过屏幕提示的 URL（默认为 `https://${主机 IP}:8888`），使用 **默认的账号和密码（admin/changeme）** 探索全新的 DCE 5.0 啦！

    ![安装成功](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)
