# 从零部署 K8s 集群到安装 DCE 5.0 社区版

本文在 3 个节点的集群中完成了从 0 到 1 的 DCE 5.0 社区版安装，包含了 K8s 集群、依赖项、网络、存储等细节及更多注意事项。

!!! note

    现阶段版本迭代较快，本文的安装方式可能与最新版有所差异，请以产品文档的[安装说明](../install/index.md)为准。

## 集群规划

使用 3 台 UCloud 的 VM，配置均为 8 核 16G。

| 角色   | 主机名         | 操作系统   | IP            | 配置           |
| ------ | -------------- | ---------- | ------------- | -------------- |
| control-plane | k8s-master01 | CentOS 8.3 | 10.23.*  | 8 核 16G 系统盘200GB |
| worker-node   | k8s-work01   | CentOS 8.3 | 10.23.* | 8 核 16G 系统盘200GB |
| worker-node  | k8s-work02    | CentOS 8.3 | 10.23.* | 8 核 16G 系统盘200GB |

本示例采用的组件为：

- Kubernetes：1.25.8
- CRI：containerd（因为新版本 K8s 已经不再直接支持 Docker）
- CNI：Calico
- StorageClass：local-path
- DCE 5.0 社区版：v0.13.0

## 准备节点

本节所述的所有操作都是必需的。

### 节点配置

安装前先分别对 3 个节点做了一些必要的设置。

1. 配置主机名。修改主机名（可选），避免主机名重名即可。

    ```bash
    hostnamectl set-hostname k8s-master01
    hostnamectl set-hostname k8s-work01 
    hostnamectl set-hostname k8s-work02
    ```

    建议修改后 exit 退出 SSH 会话，重新登录以显示新的主机名。

1. 禁用 Swap

    ```bash
    swapoff -a
    sed -i '/ swap / s/^/#/' /etc/fstab
    ```

1. 关闭防火墙（可选）

    ```bash
    systemctl stop firewalld
    systemctl disable firewalld
    ```

1. 设置内核参数并允许 iptables 进行桥接流量

    加载 `br_netfilter` 模块：

    ```bash
    cat <<EOF | tee /etc/modules-load.d/kubernetes.conf
    br_netfilter
    EOF

    # 加载模块
    sudo modprobe overlay
    sudo modprobe br_netfilter
    ```

    修改内核参数如 `ip_forward` 和 `bridge-nf-call-iptables`：

    ```bash
    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-iptables  = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    net.ipv4.ip_forward                 = 1
    EOF

    # 刷新配置
    sysctl --system
    ```

### 安装容器运行时（containerd）

1. 如果是 CentOS 8.x，要先卸载系统预装的 Podman，否则会版本冲突（[注意]🔥）

    ```bash
    yum erase podman buildah -y
    ```
  
1. 安装依赖

    ```bash
    sudo cd /etc/yum.repos.d/
    sudo mkdir bak
    sudo mv CentOS-*.repo ./bak
    sudo curl -o CentOS-base.repo http://mirrors.aliyun.com/repo/Centos-8.repo
    sudo yum clean all
    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    ```

1. 安装 containerd，可以用二进制也可以用 yum 包（yum 是 docker 社区维护的，本例中使用 yum 包）

    ```bash
    sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    sudo yum makecache
    yum install containerd.io -y
    ctr -v  # 显示安装的版本，例如 ctr containerd.io 1.6.20
    ```
  
1. 修改 containerd 的配置文件

    ```bash
    # 删除自带的 config.toml，避免后续 kubeadm 出现错误 CRI v1 runtime API is not implemented for endpoint
    mv /etc/containerd/config.toml /etc/containerd/config.toml.old

    # 重新初始化配置
    sudo containerd config default | sudo tee /etc/containerd/config.toml

    # 更新配置文件内容: 使用 systemd 作为 cgroup 驱动，并且替代 pause 镜像地址
    sed -i 's/SystemdCgroup\ =\ false/SystemdCgroup\ =\ true/' /etc/containerd/config.toml
    sed -i 's/k8s.gcr.io\/pause/k8s-gcr.m.daocloud.io\/pause/g' /etc/containerd/config.toml # 老的 pause 地址
    sed -i 's/registry.k8s.io\/pause/k8s-gcr.m.daocloud.io\/pause/g' /etc/containerd/config.toml
    sudo systemctl daemon-reload
    sudo systemctl restart containerd
    sudo systemctl enable containerd
    ```

1. 安装 CNI（可选）

    ```bash
    curl -JLO https://github.com/containernetworking/plugins/releases/download/v1.2.0/cni-plugins-linux-amd64-v1.2.0.tgz
    mkdir -p /opt/cni/bin &&  tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.2.0.tgz
    ```
  
1. 安装 nerdctl（可选）

    ```bash
    curl -LO https://github.com/containerd/nerdctl/releases/download/v1.2.1/nerdctl-1.2.1-linux-amd64.tar.gz
    tar xzvf nerdctl-1.2.1-linux-amd64.tar.gz
    mv nerdctl /usr/local/bin
    nerdctl -n k8s.io ps # 查看容器
    ```

## 安装 k8s 集群

### 安装 k8s 二进制组件

在三个节点上都需要如下操作：

1. 安装 Kubernetes 软件源 (这里采用国内阿里云的源加速)

    ```bash
    cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
    [kubernetes]
    name=Kubernetes
    baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
    enabled=1
    gpgcheck=1
    repo_gpgcheck=1
    gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
    EOF
    ```

1. 将 SELinux 设置为 permissive 模式（相当于将其禁用）

    ```bash
    sudo setenforce 0
    sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
    ```
  
1. 安装 Kubernetes 组件，版本以 1.25.8 为例（DCE 5.0 对 1.26 暂时不支持）

    ```bash
    export K8sVersion=1.25.8
    sudo yum install -y kubelet-$K8sVersion
    sudo yum install -y kubeadm-$K8sVersion
    sudo yum install -y kubectl-$K8sVersion
    sudo systemctl enable --now kubelet
    ```

### kubeadm 安装第一个 master 节点

1. 预先下载镜像以加速安装，使用 DaoCloud 的加速仓库

    ```bash
    # 指定 K8s 版本，并拉取镜像
    kubeadm config images pull --image-repository k8s-gcr.m.daocloud.io --kubernetes-version=v1.25.8
    ```

1. 调用 kubeadm 初始化第一个节点（使用 DaoCloud 加速仓库）

    !!! note

        如下 Pod CIDR 不能与宿主机物理网络的网段重合（该 CIDR 未来还需要跟 Calico 的配置一致)。

    ```bash
    sudo kubeadm init --kubernetes-version=v1.25.8 --image-repository=k8s-gcr.m.daocloud.io --pod-network-cidr=192.168.0.0/16
    ```

    经过十几分钟，你能看到打印成功的信息如下（请记住最后打印出的 `kubeadm join` 命令和相应 token，后续会用到 🔥）

    ```none
    Your Kubernetes control-plane has initialized successfully!
    To start using your cluster, you need to run the following as a regular user:
    
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

    Alternatively, if you are the root user, you can run:
    export KUBECONFIG=/etc/kubernetes/admin.conf
    You should now deploy a pod network to the cluster.
    Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
    https://kubernetes.io/docs/concepts/cluster-administration/addons/

    Then you can join any number of worker nodes by running the following on each as root:

    kubeadm join 10.23.207.16:6443 --token p4vw62.shjjzm1ce3fza6q7 \
    --discovery-token-ca-cert-hash sha256:cb1946b96502cbd2826c52959d0400b6e214e06cc8462cdd13c1cb1dc6aa8155
    ```

1. 配置 kubeconfig 文件，以便用 kubectl 更方便管理集群

    ```bash
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    kubectl get no # 你能看到第一个节点，但是仍然 NotReady
    ```

1. 安装 CNI，以 Calico 为例

    【请以官方安装方案为准。参考[官方 Calico 安装文档](https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises#install-calico)】

    1. 下载 Calico 的部署清单文件:

        ```bash
        wget https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml
        ```

    1. 使用以下命令加速镜像拉取:

        ```bash
        sed -i 's?docker.io?docker.m.daocloud.io?g' calico.yaml
        ```

    1. 使用以下命令安装 Calico:

        ```bash
        kubectl apply -f calico.yaml
        ```

    1. 等待部署成功

        ```bash
        kubectl get po -n calico-system -w # 等待 Pod 都 Running
        kubectl get no # 可以看到第一个节点变为 ready 状态了
        ```

### 接入其他 worker 工作节点

最后在其他 worker 节点执行 join 命令。
在上述 master 节点执行 `kubeadm init` 时最后会在屏幕打出（注意三个参数都是跟环境相关的，请勿直接拷贝）

```bash
kubeadm join $第一台master的IP:6443 --token p...7 --discovery-token-ca-cert-hash s....x
```

成功 join 之后，输出类似于：

```none
This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.
```

在 master 节点确认节点都被接入，并且等待其都变为 Ready 状态。

```bash
kubectl get no -w
```

### 安装默认存储 CSI（使用本地存储）

```bash
# 参考： https://github.com/rancher/local-path-provisioner
wget https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.24/deploy/local-path-storage.yaml
sed -i "s/image: rancher/image: docker.m.daocloud.io\/rancher/g" local-path-storage.yaml # 替换 docker.io 为实际镜像
sed -i "s/image: busybox/image: docker.m.daocloud.io\/busybox/g" local-path-storage.yaml
kubectl apply -f local-path-storage.yaml
kubectl get po -n local-path-storage -w # 等待 Pod 都 running

# 把 local-path 设置为默认 SC
kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
kubectl get sc # 可以看到形如: local-path (default)
```

## 安装 DCE 5.0 社区版

现在一切准备就绪，开始安装 DCE 5.0 社区版。

### 安装基础依赖

```bash
curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
bash install_prerequisite.sh online community 
```

### 下载 dce5-installer

```bash
export VERSION=v0.13.0
curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
chmod +x ./dce5-installer 
```

### 确认节点的外部可达 IP 地址

1. 如果你的浏览器跟 master 节点的 IP 是可以直通的，无需额外操作。

1. 如果 master 节点的 IP 是内网（比如本示例的公有云机器）：

    - 请在公有云中为其创建外网可达的 IP
    - 请在公有云配置中，在该主机的的防火墙规则中，允许 32088 端口的进出
    - 如上的 32088 端口是 `kubectl -n istio-system get svc istio-ingressgateway` 的 NodePort 端口

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/firewall.png)

### 执行安装

1. 如果你的浏览器跟 master 节点的 IP 是可以直通的，直接执行

    ```bash
    ./dce5-installer install-app -z
    ```

1. 如果 master 节点的 IP 是内网（比如本示例的公有云机器），请确认上述外部 IP 和防火墙配置完毕，然后执行如下命令：

    ```bash
    ./dce5-installer install-app -z -k $外部IP:32088
    ```

    注意：上述的 32088 是 `kubectl -n istio-system get svc istio-ingressgateway` 的 NodePort 端口

1. 在浏览器中打开登录界面。

    ![登录](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/login.png)

1. 以用户名 admin 密码 changeme 登录 DCE 5.0。

    ![成功登录](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/firstscreen.png)

[下载 DCE 5.0](../../../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../../index.md){ .md-button .md-button--primary }
[申请社区免费体验](../../../dce/license0.md){ .md-button .md-button--primary }
