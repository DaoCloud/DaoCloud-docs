# 通过 Docker 和 kind 在 macOS 电脑上安装 DCE 5.0 社区版

本页说明如何使用 macOS 笔记本电脑创建单节点的 kind 集群，然后在线安装 DCE 5.0 社区版。

!!! note

    这是针对初学者的简化安装体验步骤，实际生产很少会使用 macOS。
    原文作者是 [panpan0000](https://github.com/panpan0000)。

## 硬件环境

确认 MacBook 的性能和资源是否满足需求。最低配置为：

- CPU：8C
- 内存：16G
- 磁盘剩余空间 >= 20G

## 安装和调整 Docker

根据 MacBook 的芯片（Intel 或 M1），安装 [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/)。

调整容器资源上限：

1. 启动 Docker。
1. 点击右上角的 ⚙️，以打开 `Settings` 页面。
1. 点击左侧的 `Resource`，调整启动容器的资源上限（上调到 8C14G），点击 `Apply & Restart` 按钮。

![调整资源](./images/docker.png)

## 安装 kind

参照 [kind 安装说明](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)安装 kind：

```shell
# 对于 Intel Mac
[ $(uname -m) = x86_64 ]&& curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-darwin-amd64
# 对于 M1 / ARM Mac
[ $(uname -m) = arm64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-darwin-arm64
chmod +x ./kind
sudo mv kind /usr/local/bin/kind
kind version # 确认 kind 是否安装成功
```

## 创建 kind 配置文件

暴露集群内的 32088 端口到 kind 对外的 8888 端口（可自行修改）：

```shell
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

## kind 创建 K8s 集群

以 K8s 1.25.3 版本为例，执行以下命令创建一个 K8s 集群：

```shell
kind create cluster --image docker.m.daocloud.io/kindest/node:v1.25.3 --name=fire-kind-cluster --config=kind_cluster.yaml
```

确认 kind 集群创建是否成功：

```shell
docker exec -it fire-kind-cluster-control-plane  kubectl get no
```

期望输出：

```console
NAME                              STATUS   ROLES           AGE   VERSION
fire-kind-cluster-control-plane   Ready    control-plane   18h   v1.25.3
```

## 安装 DCE 5.0 社区版

1. 安装依赖项

    ```shell
    cat <<EOF | docker exec -i fire-kind-cluster-control-plane  bash
    curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
    bash install_prerequisite.sh online community
    apt-get update && apt-get install -y wget
    EOF
    ```

1. 在 kind 容器里，下载 dce5-installer 二进制文件

    ```shell
    # 假定 VERSION 为 v0.5.0
    cat <<EOF | docker exec -i fire-kind-cluster-control-plane  bash
    export VERSION=v0.5.0; 
    curl -Lo ./dce5-installer  https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer 
    EOF
    ```

1. 安装 DCE5 社区版，过程大概持续 30 分钟以上，取决于镜像拉取的网速

    ```shell
    myIP=$(ip r get 1.1.1.1| awk '{print $NF}') # 获取本机 IP
    docker exec -it fire-kind-cluster-control-plane bash -c "./dce5-installer install-app -z -k $myIP:8888"
    ```

1. 可以在安装过程中另起一个窗口，执行如下命令，观察 Pod 启动情况

    ```shell
    docker exec -it fire-kind-cluster-control-plane kubectl get po -A -w
    ```

如果有 Pod 已在运行，则表明安装成功。
