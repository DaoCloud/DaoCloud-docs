# Deploy a K8s Cluster from Scratch to DCE 5.0 Community

This article covers the installation of DCE 5.0 Community from scratch in a 3-node cluster, including details on Kubernetes cluster, dependencies, networking, storage, and more considerations.

!!! note

    The installation methods described in this article may differ from the latest version due to rapid version iterations. Please refer to the installation instructions in the product documentation for the most up-to-date information.

## Cluster Planning

The example uses 3 UCloud VM instances with the following configurations: 8 cores and 16GB RAM.

| Role           | Hostname     | Operating System | IP Address | Configuration            |
| -------------- | ------------ | ---------------- | ---------- | ------------------------ |
| control-plane  | k8s-master01 | CentOS 8.3       | 10.23.*    | 8 cores, 16GB RAM, 200GB system disk |
| worker-node    | k8s-work01   | CentOS 8.3       | 10.23.*    | 8 cores, 16GB RAM, 200GB system disk |
| worker-node    | k8s-work02   | CentOS 8.3       | 10.23.*    | 8 cores, 16GB RAM, 200GB system disk |

The components used in this example are:

- Kubernetes: 1.25.8
- CRI: containerd (as Docker is no longer directly supported in newer versions of Kubernetes)
- CNI: Calico
- StorageClass: local-path
- DCE 5.0 Community: v0.14.0

## Prepare Nodes

The following operations are necessary before installation.

### Node Configuration

Perform the following steps on each of the 3 nodes.

1. Configure the hostname. Modify the hostname to avoid hostname conflicts.

    ```bash
    hostnamectl set-hostname k8s-master01
    hostnamectl set-hostname k8s-work01
    hostnamectl set-hostname k8s-work02
    ```

    It is recommended to exit the SSH session after modifying the hostname and then log in again to display the new hostname.

2. Disable Swap

    ```bash
    swapoff -a
    sed -i '/ swap / s/^/#/' /etc/fstab
    ```

3. Disable Firewall (optional)

    ```bash
    systemctl stop firewalld
    systemctl disable firewalld
    ```

4. Set kernel parameters and enable iptables to handle bridged traffic

    Load the `br_netfilter` module:

    ```bash
    cat <<EOF | tee /etc/modules-load.d/kubernetes.conf
    br_netfilter
    EOF

    # Load the modules
    sudo modprobe overlay
    sudo modprobe br_netfilter
    ```

    Modify kernel parameters such as `ip_forward` and `bridge-nf-call-iptables`:

    ```bash
    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-iptables  = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    net.ipv4.ip_forward                 = 1
    EOF

    # Refresh the configuration
    sysctl --system
    ```

### Install Container Runtime (containerd)

1. If using CentOS 8.x, uninstall the pre-installed Podman to avoid version conflicts. (Note:🔥)

    ```bash
    yum erase podman buildah -y
    ```

2. Install dependencies

    ```bash
    sudo cd /etc/yum.repos.d/
    sudo mkdir bak
    sudo mv CentOS-*.repo ./bak
    sudo curl -o CentOS-base.repo http://mirrors.aliyun.com/repo/Centos-8.repo
    sudo yum clean all
    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    ```

3. Install containerd. You can use either the binary or yum package (yum package is maintained by the Docker community, and this example uses the yum package).

    ```bash
    sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
    sudo yum makecache
    yum install containerd.io -y
    ctr -v  # Verify the installed version, e.g., ctr containerd.io 1.6.20
    ```

4. Modify the containerd configuration file

    ```bash
    # Delete the default config.toml to avoid errors with kubeadm later on: CRI v1 runtime API is not implemented for endpoint
    mv /etc/containerd/config.toml /etc/containerd/config.toml.old

    # Reinitialize the configuration
    sudo containerd config default | sudo tee /etc/containerd/config.toml

    # Update the configuration: Use systemd as the cgroup driver and replace the pause image address
    sed -i 's/SystemdCgroup\ =\ false/SystemdCgroup\ =\ true/' /etc/containerd/config.toml
    sed -i 's/k8s.gcr.io\/pause/k8s-gcr.m.daocloud.io\/pause/g' /etc/containerd/config.toml # Old pause address
    sed -i 's/registry.k8s.io\/pause/k8s-gcr.m.daocloud.io\/pause/g' /etc/containerd/config.toml
    sudo systemctl daemon-reload
    sudo systemctl restart containerd
    sudo systemctl enable containerd
    ```

5. Install CNI (optional)

    ```bash
    curl -JLO https://github.com/containernetworking/plugins/releases/download/v1.2.0/cni-plugins-linux-amd64-v1.2.0.tgz
    mkdir -p /opt/cni/bin && tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.2.0.tgz
    ```

6. Install nerdctl (optional)

    ```bash
    curl -LO https://github.com/containerd/nerdctl/releases/download/v1.2.1/nerdctl-1.2.1-linux-amd64.tar.gz
    tar xzvf nerdctl-1.2.1-linux-amd64.tar.gz
    mv nerdctl /usr/local/bin
    nerdctl -n k8s.io ps # View containers
    ```

## Install Kubernetes Cluster

### Install Kubernetes Binary Components

Perform the following steps on all three nodes:

1. Install the Kubernetes software repository (using Aliyun's mirror for acceleration)

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

2. Set SELinux to permissive mode (equivalent to disabling it)

    ```bash
    sudo setenforce 0
    sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
    ```

3. Install Kubernetes components (use version 1.25.8 as an example)

    ```bash
    export K8sVersion=1.25.8
    sudo yum install -y kubelet-$K8sVersion
    sudo yum install -y kubeadm-$K8sVersion
    sudo yum install -y kubectl-$K8sVersion
    sudo systemctl enable --now kubelet
    ```

### Install the First Master Node using kubeadm

1. Pre-download the images for faster installation using DaoCloud's image repository

    ```bash
    # Specify the Kubernetes version and pull the images
    kubeadm config images pull --image-repository k8s-gcr.m.daocloud.io --kubernetes-version=v1.25.8
    ```

2. Initialize the first node using kubeadm (using DaoCloud's image repository)

    !!! note

        The Pod CIDR should not overlap with the IP address range of the physical network of the host machine (this CIDR will need to be consistent with the Calico configuration in the future).

    ```bash
    sudo kubeadm init --kubernetes-version=v1.25.8 --image-repository=k8s-gcr.m.daocloud.io --pod-network-cidr=192.168.0.0/16
    ```

    After about ten minutes, you will see the following successful output (remember to note down the `kubeadm join` command and the corresponding token, as they will be used later on.🔥)

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

3. Configure the kubeconfig file for easier management of the cluster using kubectl

    ```bash
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    kubectl get no # You will see the first node, but it will still be NotReady
    ```

4. Install CNI, using Calico as an example

    Please refer to the official installation guide for the correct installation method. Refer to the [official Calico installation documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises#install-calico)

    1. Download the Calico deployment manifest:

        ```bash
        wget https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml
        ```

    2. Use the following command to accelerate image pulling:

        ```bash
        sed -i 's?docker.io?docker.m.daocloud.io?g' calico.yaml
        ```

    3. Install Calico using the following command:

        ```bash
        kubectl apply -f calico.yaml
        ```

    4. Wait for the deployment to succeed:

        ```bash
        kubectl get po -n calico-system -w # Wait for all Pods to be Running
        kubectl get no # You will see the first node become ready
        ```

### Add Additional Worker Nodes

Finally, execute the join command on the other worker nodes. When executing `kubeadm init`
on the master node, the following command will be printed on the screen
(note that all three parameters are environment-specific and should not be copied directly):

```bash
kubeadm join $IP_of_the_first_master:6443 --token p...7 --discovery-token-ca-cert-hash s....x
```

After successfully joining, the output will be similar to:

```none
This node has joined the cluster:
* Certificate signing request was sent to the apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.
```

On the master node, confirm that all nodes have been added and wait for them to become Ready.

```bash
kubectl get no -w
```

### Install Default Storage CSI (Using Local Storage)

```bash
# Reference: https://github.com/rancher/local-path-provisioner
wget https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.24/deploy/local-path-storage.yaml
sed -i "s/image: rancher/image: docker.m.daocloud.io\/rancher/g" local-path-storage.yaml # Replace docker.io with the actual image
sed -i "s/image: busybox/image: docker.m.daocloud.io\/busybox/g" local-path-storage.yaml
kubectl apply -f local-path-storage.yaml
kubectl get po -n local-path-storage -w # Wait for all Pods to be running

# Set local-path as the default StorageClass
kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
kubectl get sc # You will see something like: local-path (default)
```

## Install DCE 5.0 Community

Now that everything is ready, let's install DCE 5.0 Community.

### Install Basic Dependencies

```bash
curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
bash install_prerequisite.sh online community
```

### Download dce5-installer

```bash
export VERSION=v0.14.0
curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
chmod +x ./dce5-installer
```

### Confirm the External Reachable IP Address of the Nodes

1. If your browser can directly access the IP address of the master node, no additional steps are required.

2. If the IP address of the master node is internal (e.g., in the case of public cloud instances in this example):

    - Create a publicly reachable IP address for it in the public cloud.
    - In the public cloud configuration, allow inbound and outbound traffic on port 32088 in the firewall rules for this host.
    - The above port 32088 is the NodePort port of `kubectl -n istio-system get svc istio-ingressgateway`.

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/firewall.png)

### Execute the Installation

1. If your browser can directly access the IP address of the master node, run the following command:

    ```bash
    ./dce5-installer install-app -z
    ```

2. If the IP address of the master node is internal (e.g., in the case of public cloud instances
   in this example), make sure the external IP and firewall configuration mentioned above are
   ready, and then execute the following command:

    ```bash
    ./dce5-installer install-app -z -k $EXTERNAL_IP:32088
    ```

    Note: The above port 32088 is the NodePort port of `kubectl -n istio-system get svc istio-ingressgateway`.

3. Open the login page in your browser.

    ![Login](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/login.png)

4. Log in to DCE 5.0 with the username `admin` and password `changeme`.

    ![Successful login](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/firstscreen.png)

[Download DCE 5.0](../../../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../index.md){ .md-button .md-button--primary }
[Free Trial](../../../dce/license0.md){ .md-button .md-button--primary }
