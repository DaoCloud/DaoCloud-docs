# 部署 Kubernetes 集群

DCE 5.0 支持的操作系统和 k8s

| 名称       | 版本                                                         | 说明 |
| ---------- | ------------------------------------------------------------ | ---- |
| Linux      |                                                              |      |
| Kubernetes | [1.23.7](https://github.com/kubernetes/kubernetes/releases/tag/v1.23.7) |      |
|            |                                                              |      |

建议使用以下两种方案来安装 Kubernetes。

## 方案 1：通过 kind 部署 k8s 集群

1. 下载 kind 二进制文件。

    https://files.m.daocloud.io/github.com/kubernetes-sigs/kind/releases/download/v0.15.0/kind-linux-amd64

2. 用 kind 创建 k8s 集群

	```shell
	kind create cluster --name kind --image docker.m.daocloud.io/kindest/node:v1.22.1
	```

## 方案 2：通过 Kubeadm 部署 k8s 集群

1. 下载 kubeadm 二进制文件。
 
    https://files.m.daocloud.io/storage.googleapis.com/kubernetes-release/release/v1.24.4/bin/linux/amd64/kubeadm

2. 拉取 k8s 镜像。

	```
	kubeadm config images pull --image-repository k8s-gcr.m.daocloud.io
	```

3. 执行 `kubeadm init` 初始化第一个 k8s 节点，执行 `kubeadm join` 接入其他节点。具体参见 [kubeadm 官方文档](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)。

4. 安装 CNI。如果选用 Calico，请参见 [Calico 安装文档](https://projectcalico.docs.tigera.io/getting-started/kubernetes/self-managed-onprem/onpremises)。

5. 部署 StorageClass，可选择 local-path 的开源存储，参见 [local-path 官方文档](https://github.com/rancher/local-path-provisioner)。

	```
	kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.22/deploy/local-path-storage.yaml
	```

6. 把 local-path 设置为默认 StorageClass。

	```
	kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'”
	```
