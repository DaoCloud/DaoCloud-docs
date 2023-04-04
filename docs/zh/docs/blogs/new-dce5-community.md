---
layout: post
tagline: ""
description: ""
category: Kubernetes
tags: []
last_updated: 
---

# 保姆式安装 DCE 5.0 社区版

作者：[SAMZONG](https://github.com/SAMZONG)
作者：[Peter Pan](https://github.com/panpan0000)


本文完成了从 0 到 1 的 DCE 5.0 社区版安装，包含了 K8s 集群、依赖项、网络、存储等细节及更多注意事项。

> 现阶段版本迭代较快，本文的安装方式可能与最新版有所差异，请以产品文档的[安装说明](../install/intro.md)为准。

## 集群规划

使用 3 台 UCloud 的 VM，配置均为 8 核 16G。

| 角色   | 主机名         | 操作系统   | IP            | 配置           |
| ------ | -------------- | ---------- | ------------- | -------------- |
| control-plane | k8s-master01 | CentOS 8.3 | 10.23.*  | 8 核 16G 系统盘200GB |
| worker-node   | k8s-work01   | CentOS 8.3 | 10.23.* | 8 核 16G 系统盘200GB |
| worker-node  | k8s-work02    | CentOS 8.3 | 10.23.* | 8 核 16G 系统盘200GB |

本示例采用的组件为：

- Kubernetes:1.25.8
- CRI:containerd （因为新版本K8s已经不再直接支持docker）
- CNI:Calico
- StorageClass:local-path
- DCE5.0社区版: v0.5.0

## 节点配置

安装前先分别对 3 个节点做了一些设置

1. 配置主机名

    ```bash
    修改主机名（可选）。避免主机名重名即可
    hostnamectl set-hostname k8s-master01
    hostnamectl set-hostname k8s-work01 
    hostnamectl set-hostname k8s-work02
    修改之建议后exit退出SSH 会话，重新登录以显示新的主机名。
  ```


1. 禁用 Swap

    ```bash
    swapoff -a
    sed -i '/ swap / s/^/#/' /etc/fstab
    ```

1. 禁用 SElinux

    ```bash
    setenforce 0
    sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
    ```

1. 关闭防火墙

    ```bash
    systemctl stop firewalld
    systemctl disable firewalld
    ```

1. 允许 iptables 检查桥接流量

    加载 `br_netfilter` 模块：

    ```bash linenums="1"
    cat <<EOF | tee /etc/modules-load.d/kubernetes.conf
    br_netfilter
    EOF

    # 加载模块
    sudo modprobe overlay
    sudo modprobe br_netfilter
    ```

    修改内核参数 如`ip_forward` 和`bridge-nf-call-iptables`：

    ```bash linenums="3"
    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-iptables  = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    net.ipv4.ip_forward                 = 1
    EOF

    # 刷新配置
    sysctl --system
    ```
    
## 安装容器运行时（containerd）


1. [注意]如果是Centos 8.x要先卸载podman，否则会冲突
  ```
   yum erase podman buildah -y
  ```
1.安装依赖
  ```bash
  sudo yum install -y yum-utils device-mapper-persistent-data lvm2
  ```
  
1.安装containerd，可以用二进制也可以用yum包（yum是docker社区维护的，如下使用yum包）
  ```bash
  sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
  sudo yum makecache
  yum install containerd.io -y
  ctr -v           
  #显示安装的版本，例如ctr containerd.io 1.6.20
  ```
  
1.修改containerd的配置文件
  ```
  #删除自带的config.toml， 避免后续kubeadm出现错误CRI v1 runtime API is not implemented for endpoint
  mv /etc/containerd/config.toml /etc/containerd/config.toml.old
  # 重新初始化配置
  sudo containerd config default | sudo tee /etc/containerd/config.toml
  # 更新配置文件内容: 使用systemd作为Cgroup驱动，并且替代pause镜像地址
  sed -i 's/SystemdCgroup\ =\ false/SystemdCgroup\ =\ true/' /etc/containerd/config.toml
  sed -i 's/k8s.gcr.io\/pause/k8s-gcr.m.daocloud.io\/pause/g' /etc/containerd/config.toml #老的pause地址
  sed -i 's/registry.k8s.io\/pause/k8s-gcr.m.daocloud.io\/pause/g' /etc/containerd/config.toml
  sudo systemctl daemon-reload
  sudo systemctl restart containerd
  sudo systemctl enable containerd
  ```


1. 安装CNI

  ```bash
  curl -JLO https://github.com/containernetworking/plugins/releases/download/v1.2.0/cni-plugins-linux-amd64-v1.2.0.tgz
  mkdir -p /opt/cni/bin &&  tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.2.0.tgz
  ```
  
1. 安装nerdctl(可选)
   ```bash
   curl -LO https://github.com/containerd/nerdctl/releases/download/v1.2.1/nerdctl-1.2.1-linux-amd64.tar.gz
   tar xzvf nerdctl-1.2.1-linux-amd64.tar.gz
   mv nerdctl /usr/local/bin
   nerdctl -n k8s.io ps #查看容器
   ```



#安装k8s二进制组件

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
  ```
  sudo setenforce 0
  sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
  ```
  
1. 安装 Kubernetes 组件, 版本以1.25.8为例（DCE 0.5.0对1.26暂时不支持）
  ```
  export K8sVersion=1.25.8
  sudo yum install -y kubelet-$K8sVersion
  sudo yum install -y kubeadm-$K8sVersion
  sudo yum install -y kubectl-$K8sVersion
  sudo systemctl enable --now kubelet
  ```

# kubeadm安装第一个master
# kubeadm安装第一个jjie dian 
# kubeadm安装第一个
