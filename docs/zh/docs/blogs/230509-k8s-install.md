# 安装 Kubernetes 教程 (KLTS 版)

本文以 DaoCloud 自主维护的 [KLTS (Kubernetes Long Term Support)](https://klts.io/zh/docs/intro/) 为例，简要介绍如何安装 Kubernetes。

## 准备工作

- 准备一台兼容的 Linux 主机。Kubernetes 项目为基于 Debian 和 Red Hat 的 Linux
  发行版以及一些不提供包管理器的发行版提供通用的指令。
- 每台主机至少 2 GB 或更多的内存（如果内存太少将影响应用的运行）
- CPU 2 核或更多
- 集群中所有主机的网络连通（公网和内网）
- 单个节点上不能有重复的主机名、MAC 地址或 product_uuid，请参阅[确保每个节点上 MAC 地址和 product_uuid 的唯一性](#mac-product-uuid)
- 开启主机上的某些端口，请参阅[检查所需端口](#_3)。
- 禁用交换分区。为了保证 kubelet 正常工作，您必须禁用交换分区。

### 确保节点上 MAC 地址和 product_uuid 的唯一性

- 使用命令 __ip link__ 或 __ifconfig -a__ 来获取网络接口的 MAC 地址
- 使用 __sudo cat /sys/class/dmi/id/product_uuid__ 命令来校验 product_uuid

一般来讲，硬件设备拥有唯一的地址，但是有些虚拟机的地址可能会重复。
Kubernetes 使用 MAC 地址和 product_uuid 来确定集群中的唯一节点。
如果这些值在每个节点上不唯一，可能会导致安装[失败](https://github.com/kubernetes/kubeadm/issues/31)。

### 检查网络适配器

如果您有一个以上的网络适配器，同时您的 Kubernetes 组件通过默认路由不可达，
我们建议您预先添加 IP 路由规则，这样 Kubernetes 集群就可以通过对应的适配器完成连接。

### 允许 iptables 检查桥接流量

确保 __br_netfilter__ 模块被加载。这一操作可以通过运行 __lsmod | grep br_netfilter__
来完成。若要显式加载该模块，可执行命令 __sudo modprobe br_netfilter__。

为了让您的 Linux 节点上的 iptables 能够正确地查看桥接流量，您需要确保在
__sysctl__ 配置中将 __net.bridge.bridge-nf-call-iptables__ 设置为 1。例如：

```bash
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl --system
```

更多细节请查阅[网络插件需求](https://kubernetes.io/zh-cn/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#network-plugin-requirements)页面。

### 检查所需端口

#### 控制平面节点

| 协议 | 方向 | 端口范围  | 作用                    | 使用者                       |
| ---- | ---- | --------- | ----------------------- | ---------------------------- |
| TCP  | 入站 | 6443      | Kubernetes API 服务器   | 所有组件                     |
| TCP  | 入站 | 2379-2380 | etcd 服务器客户端 API   | kube-apiserver、etcd         |
| TCP  | 入站 | 10250     | Kubelet API             | kubelet 自身、控制平面组件   |
| TCP  | 入站 | 10251     | kube-scheduler          | kube-scheduler 自身          |
| TCP  | 入站 | 10252     | kube-controller-manager | kube-controller-manager 自身 |

#### 工作节点

| 协议 | 方向 | 端口范围    | 作用          | 使用者                     |
| ---- | ---- | ----------- | ------------- | -------------------------- |
| TCP  | 入站 | 10250       | Kubelet API   | kubelet 自身、控制平面组件 |
| TCP  | 入站 | 30000-32767 | NodePort 服务 | 所有组件                   |

以上是 [NodePort 服务](https://kubernetes.io/zh-cn/docs/concepts/services-networking/service/)的默认端口范围。

使用 * 标记的任意端口号都可以被覆盖，所以您需要保证定制的端口是开放的。

虽然控制平面节点已经包含了 etcd 的端口，您也可以使用自定义的外部 etcd 集群，或指定自定义端口。

您使用的 Pod 网络插件 (见下) 也可能需要某些特定端口开启。由于各个 Pod 网络插件都有所不同，请参阅相应文档中的端口要求。

### 设置节点名字

命令的语法格式如下：

```bash
hostnamectl set-hostname your-new-host-name
echo "127.0.0.1 $(hostname)" >> /etc/hosts
echo "::1       $(hostname)" >> /etc/hosts
```

### 关闭 Swap

执行以下命令关闭 Swap：

```bash
swapoff -a
```

如果需要永久关闭，请编辑 __/etc/fstab__ 文件，注释掉 Swap 的挂载路径。

### 关闭 Selinux

执行以下命令关闭 Selinux：

```bash
setenforce 0
```

如果需要永久关闭，请编辑 __/etc/sysconfig/selinux__ 将 __SELINUX=enforcing__ 替换为 __SELINUX=disabled__。

### 安装运行时

为了在 Pod 中运行容器，Kubernetes 使用容器运行时（Container Runtime）。

#### 如果是 Linux 节点

默认情况下，Kubernetes 使用容器运行时接口（Container Runtime Interface，CRI）来与您所选择的容器运行时交互。

如果您不指定运行时，则 kubeadm 会自动尝试检测系统上已经安装的运行时，方法是扫描一组众所周知的 Unix 域套接字。

下面的表格列举了一些容器运行时及其对应的套接字路径：

| 运行时     | 域套接字                        |
| ---------- | ------------------------------- |
| Docker     | /var/run/dockershim.sock        |
| Containerd | /run/containerd/containerd.sock |
| CRI-O      | /var/run/crio/crio.sock         |

如果同时检测到 Docker 和 Containerd，则优先选择 Docker。
这是必然的，即使您仅安装了 Docker，因为 Docker 18.09 附带了 Containerd，所以两者都是可以检测到的。
如果检测到其他两个或多个运行时，则 kubeadm 输出错误信息并退出。

kubelet 通过内置的 __dockershim__ CRI 实现与 Docker 集成。

**对于 Docker**

=== “基于 Red Hat 发行版”

    执行以下命令安装基于 Red Hat 发行版的 Docker：

    ```bash
    yum install docker
    ```

=== “基于 Debian 发行版”

    执行以下命令安装基于 Debian 发行版的 Docker：

    ```bash
    apt-get install docker.io
    ```

**对于 containerd**

containerd 官方默认只提供 amd64 架构的下载包，如果您采用的是其他基础架构，
可以从 Docker 官方仓库安装 __containerd.io__ 软件包。在[安装 Docker 引擎](https://docs.docker.com/engine/install/#server)中
找到为各自的 Linux 发行版设置 Docker 存储库和安装 containerd.io 软件包的有关说明。

也可以使用以下源代码构建。

```bash
VERSION=1.5.4
wget -c https://github.com/containerd/containerd/releases/download/v${VERSION}/containerd-${VERSION}-linux-amd64.tar.gz
tar xvf containerd-${VERSION}-linux-amd64.tar.gz -C /usr/local/
mkdir /etc/containerd/ && containerd config default > /etc/containerd/config.toml
wget -c -O /etc/systemd/system/containerd.service https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
systemctl start containerd && systemctl enable containerd
```

#### 如果是其它操作系统

默认情况下，kubeadm 使用 docker 作为容器运行时。kubelet 通过内置的 __dockershim__ CRI 实现与 Docker 集成。

**对于 Docker**

=== “基于 Red Hat 发行版”

    执行以下命令安装基于 Red Hat 发行版的 Docker：

    ```bash
    yum install docker
    ```

=== “基于 Debian 发行版”

    执行以下命令安装基于 Debian 发行版的 Docker：

    ```bash
    apt-get install docker.io
    ```

**对于 containerd**

containerd 官方默认只提供 amd64 架构的下载包，如果您采用的是其他基础架构，
可以从 Docker 官方仓库安装 __containerd.io__ 软件包。在[安装 Docker 引擎](https://docs.docker.com/engine/install/#server)中
找到为各自的 Linux 发行版设置 Docker 存储库和安装 containerd.io 软件包的有关说明。

也可以使用以下源代码构建。

```bash
VERSION=1.5.4
wget -c https://github.com/containerd/containerd/releases/download/v${VERSION}/containerd-${VERSION}-linux-amd64.tar.gz
tar xvf containerd-${VERSION}-linux-amd64.tar.gz -C /usr/local/
mkdir /etc/containerd/ && containerd config default > /etc/containerd/config.toml
wget -c -O /etc/systemd/system/containerd.service https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
systemctl start containerd && systemctl enable containerd
```

参阅[容器运行时](https://kubernetes.io/zh-cn/docs/setup/production-environment/container-runtimes/)以了解更多信息。

## 安装 KLTS

KLTS 提供了基于 deb 和 rpm 软件源的安装方式，您可以选择适合的安装方式。

### 设置 KLTS 软件源

=== "基于 Red Hat 的发行版"

    执行以下代码设置下载 KLTS 的软件源：

    ```bash
    VERSION=1.18.20-lts.2
    cat << EOF > /etc/yum.repos.d/klts.repo
    [klts]
    name=klts
    baseurl=https://raw.githubusercontent.com/klts-io/kubernetes-lts/rpm-v${VERSION}/\$basearch/
    enabled=1
    gpgcheck=0
    [klts-other]
    name=klts-others
    baseurl=https://raw.githubusercontent.com/klts-io/others/rpm/\$basearch/
    enabled=1
    gpgcheck=0
    EOF

    yum makecache
    ```

=== "基于 Debian 的发行版"

    执行以下代码设置下载 KLTS 的软件源：

    ```bash
    VERSION=1.18.20-lts.2
    cat << EOF > /etc/apt/sources.list.d/klts.list
    deb [trusted=yes] https://raw.githubusercontent.com/klts-io/kubernetes-lts/deb-v${VERSION} stable main
    deb [trusted=yes] https://raw.githubusercontent.com/klts-io/others/deb stable main
    EOF

    apt-get update
    ```

=== "基于 Red Hat 的发行版, 国内加速 🚀"

    !!! note

        以下加速均来自第三方, 安全和稳定性不做保障, 仅建议测试环境使用!!!

    执行以下代码设置下载 KLTS 的软件源：

    === "/etc/hosts"

        ```bash
        curl https://raw.githubusercontent.com/wzshiming/github-hosts/master/hosts >>/etc/hosts

        VERSION=1.18.20-lts.2
        cat << EOF > /etc/yum.repos.d/klts.repo
        [klts]
        name=klts
        baseurl=https://raw.githubusercontent.com/klts-io/kubernetes-lts/rpm-v${VERSION}/\$basearch/
        enabled=1
        gpgcheck=0
        [klts-other]
        name=klts-others
        baseurl=https://raw.githubusercontent.com/klts-io/others/rpm/\$basearch/
        enabled=1
        gpgcheck=0
        EOF

        yum makecache
        ```

    === "hub.fastgit.org"

        ```bash
        VERSION=1.18.20-lts.2
        cat << EOF > /etc/yum.repos.d/klts.repo
        [klts]
        name=klts
        baseurl=https://hub.fastgit.org/klts-io/kubernetes-lts/raw/rpm-v${VERSION}/\$basearch/
        enabled=1
        gpgcheck=0
        [klts-other]
        name=klts-others
        baseurl=https://hub.fastgit.org/klts-io/others/raw/rpm/\$basearch/
        enabled=1
        gpgcheck=0
        EOF

        yum makecache
        ```

    === "ghproxy.com"

        ```bash
        VERSION=1.18.20-lts.2
        cat << EOF > /etc/yum.repos.d/klts.repo
        [klts]
        name=klts
        baseurl=https://ghproxy.com/https://raw.githubusercontent.com/klts-io/kubernetes-lts/rpm-v${VERSION}/\$basearch/
        enabled=1
        gpgcheck=0
        [klts-other]
        name=klts-others
        baseurl=https://ghproxy.com/https://raw.githubusercontent.com/klts-io/others/rpm/\$basearch/
        enabled=1
        gpgcheck=0
        EOF

        yum makecache
        ```

    === "raw.githubusercontents.com"

        ```bash
        VERSION=1.18.20-lts.2
        cat << EOF > /etc/yum.repos.d/klts.repo
        [klts]
        name=klts
        baseurl=https://raw.githubusercontents.com/klts-io/kubernetes-lts/rpm-v${VERSION}/\$basearch/
        enabled=1
        gpgcheck=0
        [klts-other]
        name=klts-others
        baseurl=https://raw.githubusercontents.com/klts-io/others/rpm/\$basearch/
        enabled=1
        gpgcheck=0
        EOF

        yum makecache
        ```

    === "raw.staticdn.net"

        ```bash
        VERSION=1.18.20-lts.2
        cat << EOF > /etc/yum.repos.d/klts.repo
        [klts]
        name=klts
        baseurl=https://raw.staticdn.net/klts-io/kubernetes-lts/rpm-v${VERSION}/\$basearch/
        enabled=1
        gpgcheck=0
        [klts-other]
        name=klts-others
        baseurl=https://raw.staticdn.net/klts-io/others/rpm/\$basearch/
        enabled=1
        gpgcheck=0
        EOF

        yum makecache
        ```

=== "基于 Debian 的发行版, 国内加速 🚀"

    !!! note

        以下加速均来自第三方, 安全和稳定性不做保障, 仅建议测试环境使用!!!

    执行以下代码设置下载 KLTS 的软件源：

    === "/etc/hosts"

        ```bash
        curl https://raw.githubusercontent.com/wzshiming/github-hosts/master/hosts >>/etc/hosts

        VERSION=1.18.20-lts.2
        cat << EOF > /etc/apt/sources.list.d/klts.list
        deb [trusted=yes] https://raw.githubusercontent.com/klts-io/kubernetes-lts/deb-v${VERSION} stable main
        deb [trusted=yes] https://raw.githubusercontent.com/klts-io/others/deb stable main
        EOF

        apt-get update
        ```

    === "hub.fastgit.org"

        ```bash
        VERSION=1.18.20-lts.2
        cat << EOF > /etc/apt/sources.list.d/klts.list
        deb [trusted=yes] https://hub.fastgit.org/klts-io/kubernetes-lts/raw/deb-v${VERSION} stable main
        deb [trusted=yes] https://hub.fastgit.org/klts-io/others/raw/deb stable main
        EOF

        apt-get update
        ```

    === "ghproxy.com"

        ```bash
        VERSION=1.18.20-lts.2
        cat << EOF > /etc/apt/sources.list.d/klts.list
        deb [trusted=yes] https://ghproxy.com/https://raw.githubusercontent.com/klts-io/kubernetes-lts/deb-v${VERSION} stable main
        deb [trusted=yes] https://ghproxy.com/https://raw.githubusercontent.com/klts-io/others/deb stable main
        EOF

        apt-get update
        ```

    === "raw.githubusercontents.com"

        ```bash
        VERSION=1.18.20-lts.2
        cat << EOF > /etc/apt/sources.list.d/klts.list
        deb [trusted=yes] https://raw.githubusercontents.com/klts-io/kubernetes-lts/deb-v${VERSION} stable main
        deb [trusted=yes] https://raw.githubusercontents.com/klts-io/others/deb stable main
        EOF

        apt-get update
        ```

    === "raw.staticdn.net"

        ```bash
        VERSION=1.18.20-lts.2
        cat << EOF > /etc/apt/sources.list.d/klts.list
        deb [trusted=yes] https://raw.staticdn.net/klts-io/kubernetes-lts/deb-v${VERSION} stable main
        deb [trusted=yes] https://raw.staticdn.net/klts-io/kubernetes-lts/deb stable main
        EOF

        apt-get update
        ```

### 开始安装 KLTS

=== "基于 Red Hat 的发行版"

    执行以下命令安装：

    ```bash
    yum install kubeadm kubelet kubectl
    ```

=== "基于 Debian 的发行版"

    执行以下命令安装：

    ```bash
    apt-get install kubeadm kubelet kubectl
    ```

### 开机自动启动 Kubelet

执行以下命令开机自动启动 Kubelet：

```
systemctl enable kubelet
```

### 拉取依赖镜像

=== "默认"

    执行以下命令 pull 依赖的镜像：

    ```bash
    VERSION=1.18.20-lts.2
    REPOS=ghcr.io/klts-io/kubernetes-lts
    kubeadm config images pull --image-repository ${REPOS} --kubernetes-version v${VERSION}
    ```

=== "国内加速 🚀"

    执行以下命令 pull 依赖的镜像：

    ```bash
    VERSION=1.18.20-lts.2
    REPOS=ghcr.m.daocloud.io/klts-io/kubernetes-lts
    kubeadm config images pull --image-repository ${REPOS} --kubernetes-version v${VERSION}
    ```

后续对 kubeadm 的操作都需要加上 __--image-repository__ 和 __--kubernetes-version__ 以主动指定镜像。

### 初始化控制面节点

=== "默认"

    执行以下命令初始化控制面的节点：

    ```bash
    VERSION=1.18.20-lts.2
    REPOS=ghcr.io/klts-io/kubernetes-lts
    kubeadm init --image-repository ${REPOS} --kubernetes-version v${VERSION}
    ```

=== "国内加速 🚀"

    执行以下命令初始化控制面的节点：

    ```bash
    VERSION=1.18.20-lts.2
    REPOS=ghcr.m.daocloud.io/klts-io/kubernetes-lts
    kubeadm init --image-repository ${REPOS} --kubernetes-version v${VERSION}
    ```

## 脚本一键安装

除了上述正常安装方式外，KLTS 还支持脚本自动完成安装流程。

```bash
wget https://github.com/klts-io/klts/raw/main/install.sh
chmod +x install.sh
./install.sh
```

```console
Usage: ./install.sh [OPTIONS]
  -h, --help : Display this help and exit
  --kubernetes-container-registry=ghcr.io/klts-io/kubernetes-lts : Kubernetes container registry
  --kubernetes-version=1.18.20-lts.1 : Kubernetes version to install
  --containerd-version=1.3.10-lts.0 : Containerd version to install
  --runc-version=1.0.2-lts.0 : Runc version to install
  --kubernetes-rpm-source=https://github.com/klts-io/kubernetes-lts/raw/rpm-v1.18.20-lts.2 : Kubernetes RPM source
  --containerd-rpm-source=https://github.com/klts-io/containerd-lts/raw/rpm-v1.3.10-lts.0 : Containerd RPM source
  --runc-rpm-source=https://github.com/klts-io/runc-lts/raw/rpm-v1.0.2-lts.0 : Runc RPM source
  --others-rpm-source=https://github.com/klts-io/others/raw/rpm : Other RPM source
  --kubernetes-deb-source=https://github.com/klts-io/kubernetes-lts/raw/deb-v1.18.20-lts.2 : Kubernetes DEB source
  --containerd-deb-source=https://github.com/klts-io/containerd-lts/raw/deb-v1.3.10-lts.0 : Containerd DEB source
  --runc-deb-source=https://github.com/klts-io/runc-lts/raw/deb-v1.0.2-lts.0 : Runc DEB source
  --others-deb-source=https://github.com/klts-io/others/raw/deb : Other DEB source
  --focus=enable-iptables-discover-bridged-traffic,disable-swap,disable-selinux,setup-source,install-kubernetes,install-containerd,install-runc,install-crictl,install-cniplugins,setup-crictl-config,setup-containerd-cni-config,setup-kubelet-config,setup-containerd-config,daemon-reload,start-containerd,status-containerd,enable-containerd,start-kubelet,status-kubelet,enable-kubelet,images-pull,control-plane-init,status-nodes,show-join-command : Focus on specific step
  --skip='' : Skip on specific step
```

## 更多安装方式

- [保姆式部署三节点 K8s 集群](./230405-step-by-step-dce5.md#k8s)
- [使用 kubeadm 创建集群](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [使用 kOps 安装 K8s](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kops/)
- [使用 Kubespray 安装 K8s](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubespray/)
