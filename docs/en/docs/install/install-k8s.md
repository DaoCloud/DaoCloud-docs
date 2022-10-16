# Deploy K8S Clusters

It is recommended to use the following options to deploy your k8s clusters.

## Option 1: Deploy k8s cluster via kind

1. Download the `kind` binary package.

    https://files.m.daocloud.io/github.com/kubernetes-sigs/kind/releases/download/v0.15.0/kind-linux-amd64

2. Use `kind` to create k8s clusters.

	```shell
	kind create cluster --name kind --image docker.m.daocloud.io/kindest/node:v1.22.1
	```
	
!!! info

	DaoCloud has set up a dedicated mirror for domestic users to download. Links with `https://files.m.daocloud.io/` indicate that mirror acceleration has been provided.

## Option 2: Deploy k8s clusters via Kubeadm

1. Download the kubeadm binary package.

    https://files.m.daocloud.io/storage.googleapis.com/kubernetes-release/release/v1.24.4/bin/linux/amd64/kubeadm

2. Pull the k8s image.

	```
	kubeadm config images pull --image-repository k8s-gcr.m.daocloud.io
	```

3. Run `kubeadm init` to initialize your first k8s node, and run `kubeadm join` to join other nodes. For detailed flags, see [kubeadm documentation](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/).

4. Install CNIs. If you choose to use Calico, see [Calico documentation](https://projectcalico.docs.tigera.io/getting-started/kubernetes/self-managed-onprem/onpremises). If you choose other CNIs, see corresponding documentation.

5. Deploy StorageClass while you can select local-path. Refer to [local-path documentation](https://github.com/rancher/local-path-provisioner).

	```
	kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.22/deploy/local-path-storage.yaml
	```

	Set local-path to the default StorageClass.

	```
	kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'”
	```
