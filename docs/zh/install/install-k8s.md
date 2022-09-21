# 部署 k8s 集群

建议使用以下两种方案来部署 k8s 集群。

## 方案 1：通过 Kubeadm 部署 k8s 集群

1. 下载 kubeadm 二进制文件。

    https://files.m.daocloud.io/storage.googleapis.com/kubernetes-release/release/v1.24.4/bin/linux/amd64/kubeadm

2. 拉取 k8s 镜像。

	```
	kubeadm config images pull --image-repository k8s-gcr.m.daocloud.io
	```

3. 执行 `kubeadm init` 初始化第一个 k8s 节点，执行 `kubeadm join` 接入其他节点。详细命令参数参见 [kubeadm 官方文档](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)。

4. 安装 CNI。如果选用 Calico，请参见 [Calico 安装文档](https://projectcalico.docs.tigera.io/getting-started/kubernetes/self-managed-onprem/onpremises)。如果选用其他 CNI，请参见对应文档。

5. 部署 StorageClass，可选择 local-path 的开源存储，参见 [local-path 官方文档](https://github.com/rancher/local-path-provisioner)。

	```
	kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.22/deploy/local-path-storage.yaml
	```

	把 local-path 设置为默认 StorageClass。

	```
	kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
	```

## 方案 2：通过 kind 部署 k8s 集群

1. 下载 kind 二进制文件。

    https://files.m.daocloud.io/github.com/kubernetes-sigs/kind/releases/download/v0.15.0/kind-linux-amd64

2. 用 kind 创建 k8s 集群。

	```shell
	kind create cluster --name kind --image docker.m.daocloud.io/kindest/node:v1.22.1
	```
	
!!! info

	- DaoCloud 设立了国内镜像站，便于国内用户下载。链接中带有 `https://*.daocloud.io/` 表示已提供国内镜像加速。
	- 如果需要 NodePort 或 metallb，也需要暴露端口，部署过程可能会比较复杂。如有问题无法解决，请联系我们。
