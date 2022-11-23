---
hide:
  - toc
---

# 部署 Kubernetes 集群

[安装 DCE 5.0](./install-dce-community.md) 之前，需要先参照以下步骤部署一个或多个 Kubernetes 集群，本例采用 Kubeadm 来部署。

1. 下载 kubeadm 二进制文件。

    https://files.m.daocloud.io/storage.googleapis.com/kubernetes-release/release/v1.24.4/bin/linux/amd64/kubeadm

2. 拉取 Kubernetes 镜像。

	```sh
	kubeadm config images pull --image-repository k8s-gcr.m.daocloud.io
	```

3. 执行 `kubeadm init` 初始化第一个 Kubernetes 节点，执行 `kubeadm join` 接入其他节点。详细命令参数参见 [kubeadm 官方文档](https://kubernetes.io/zh-cn/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)。

4. 安装 CNI。如果选用 Calico，请参见 [Calico 安装文档](https://projectcalico.docs.tigera.io/getting-started/kubernetes/self-managed-onprem/onpremises)。如果选用其他 CNI，请参见对应文档。

5. 部署 StorageClass，可选择 local-path 的开源存储，参见 [local-path 官方文档](https://github.com/rancher/local-path-provisioner)。

	```sh
	kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.22/deploy/local-path-storage.yaml
	```

	把 local-path 设置为默认 StorageClass。

	```sh
	kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
	```
	
!!! info

	接下来需要[安装一些依赖项](./install-tools.md)，保证运行环境完备。
	DaoCloud 设立了国内镜像站，便于国内用户下载。链接中带有 `https://*.daocloud.io/` 表示已提供国内镜像加速。
