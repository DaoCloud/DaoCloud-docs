# Install the Kubernetes Tutorial (KLTS version)

This article takes [KLTS (Kubernetes Long Term Support)](https://klts.io/docs/intro/) self-maintained by DaoCloud as an example to briefly introduce how to install Kubernetes.

## Preparation

- Prepare a compatible Linux host. The Kubernetes project for Linux based on Debian and Red Hat
   Distributions, and some distributions that don't provide a package manager, provide common instructions.
- At least 2 GB or more of memory per host (too little memory will affect the operation of the application)
- CPU 2 cores or more
- Network connectivity of all hosts in the cluster (public and intranet)
- No duplicate hostname, MAC address or product_uuid on a single node, see [Ensure uniqueness of MAC address and product_uuid on each node](#mac-product-uuid)
- Open some ports on the host, see [Check Required Ports](#check-required-ports).
- Disable swap partition. In order for the kubelet to work properly, you must disable swap.

### Ensure the uniqueness of the MAC address and product_uuid on the node

- Use the command __ip link__ or __ifconfig -a__ to get the MAC address of the network interface
- Use __sudo cat /sys/class/dmi/id/product_uuid__ command to verify product_uuid

Generally speaking, hardware devices have unique addresses, but the addresses of some virtual machines may be repeated.
Kubernetes uses the MAC address and product_uuid to identify unique nodes in the cluster.
If these values are not unique on each node, it may cause the installation to [fail](https://github.com/kubernetes/kubeadm/issues/31).

### Check Network Adapter

If you have more than one network adapter and your Kubernetes components are not reachable via default routes,
We recommend that you pre-add IP routing rules so that Kubernetes clusters can be connected through corresponding adapters.

### Allow iptables to inspect bridged traffic

Make sure the __br_netfilter__ module is loaded. This can be done by running __lsmod | grep br_netfilter__
To be done. To explicitly load this module, run the command __sudo modprobe br_netfilter__.

In order for iptables on your Linux nodes to properly see bridged traffic, you need to ensure that the
Set __net.bridge.bridge-nf-call-iptables__ to 1 in __sysctl__ configuration. For example:

```bash
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables=1
net.bridge.bridge-nf-call-iptables=1
EOF
sudo sysctl --system
```

For more details, please refer to the [Network Plugin Requirements](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/#network-plugin-requirements) page.

### Check required ports

#### Control Plane Node

| Protocol | Direction | Port Range | Role | User |
| ---- | ---- | --------- | ----------------------- | ----- ----------------------- |
| TCP | Inbound | 6443 | Kubernetes API Server | All Components |
| TCP | Inbound | 2379-2380 | etcd server client API | kube-apiserver, etcd |
| TCP | Inbound | 10250 | Kubelet API | kubelet itself, control plane components |
| TCP | Inbound | 10251 | kube-scheduler | kube-scheduler itself |
| TCP | Inbound | 10252 | kube-controller-manager | kube-controller-manager itself |

#### Worker nodes

| Protocol | Direction | Port Range | Role | User |
| ---- | ---- | ----------- | ------------- | ------------- ------------- |
| TCP | Inbound | 10250 | Kubelet API | kubelet itself, control plane components |
| TCP | Inbound | 30000-32767 | NodePort Service | All Components |

The above is the default port range of [NodePort service](https://kubernetes.io/docs/concepts/services-networking/service/).

Any port number marked with * can be overridden, so you need to make sure the custom port is open.

Although the control plane nodes already include ports for etcd, you can also use a custom external etcd cluster, or specify a custom port.

The Pod networking plugin (see below) you use may also require certain ports to be open. Since individual Pod network plugins are different, please refer to the appropriate documentation for port requirements.

### Set node name

The syntax of the command is as follows:

```bash
hostnamectl set-hostname your-new-host-name
echo "127.0.0.1 $(hostname)" >> /etc/hosts
echo "::1 $(hostname)" >> /etc/hosts
```

### Close Swap

Run the following command to close Swap:

```bash
swapoff -a
```

If you need to shut down permanently, please edit the __/etc/fstab__ file and comment out the mount path of Swap.

### Shutdown Selinux

Run the following command to shut down Selinux:

```bash
setenforce 0
```

To disable permanently, edit __/etc/sysconfig/selinux__ and replace __SELINUX=enforcing__ with __SELINUX=disabled__.

### Install the runtime

To run containers in Pods, Kubernetes uses a Container Runtime.

#### If it is a Linux node

By default, Kubernetes uses the Container Runtime Interface (CRI) to interact with the container runtime of your choice.

If you do not specify a runtime, kubeadm automatically tries to detect a runtime already installed on the system by scanning a set of well-known Unix domain sockets.

The following table lists some container runtimes and their corresponding socket paths:

| runtime | domain socket |
| ---------- | ------------------------------- |
| Docker | /var/run/dockershim.sock |
| Containerd | /run/containerd/containerd.sock |
| CRI-O | /var/run/crio/crio.sock |

If both Docker and Containerd are detected, Docker will be preferred.
This is true even if you only have Docker installed, since Docker 18.09 ships with Containerd, so both are detectable.
If two or more other runtimes are detected, kubeadm outputs an error message and exits.

The kubelet integrates with Docker through the built-in __dockershim__ CRI.

**For Docker**

=== "Red Hat based distribution"

     run the following command to install a Red Hat based distribution of Docker:

     ```bash
     yum install docker
     ```

=== "Debian-based distribution"

     run the following command to install Docker on Debian based distributions:

     ```bash
     apt-get install docker.io
     ```

**for containerd**

By default, containerd only provides download packages for the amd64 architecture. If you use other infrastructures,
The __containerd.io__ package can be installed from the official Docker repository. In [Install Docker Engine](https://docs.docker.com/engine/install/#server)
Find instructions on setting up a Docker repository and installing the containerd.io package for your respective Linux distribution.

It can also be built using the following source code.

```bash
VERSION=1.5.4
wget -c https://github.com/containerd/containerd/releases/download/v${VERSION}/containerd-${VERSION}-linux-amd64.tar.gz
tar xvf containerd-${VERSION}-linux-amd64.tar.gz -C /usr/local/
mkdir /etc/containerd/ && containerd config default > /etc/containerd/config.toml
wget -c -O /etc/systemd/system/containerd.service https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
systemctl start containerd && systemctl enable containerd
```

#### If other OS

By default, kubeadm uses docker as the container runtime. The kubelet integrates with Docker through the built-in __dockershim__ CRI.

**For Docker**

=== "Red Hat based distribution"

     run the following command to install a Red Hat based distribution of Docker:

     ```bash
     yum install docker
     ```

=== "Debian-based distribution"

     run the following command to install Docker on Debian based distributions:

     ```bash
     apt-get install docker.io
     ```
**for containerd**

By default, containerd only provides download packages for the amd64 architecture. If you use other infrastructures,
The __containerd.io__ package can be installed from the official Docker repository. In [Install Docker Engine](https://docs.docker.com/engine/install/#server)
Find instructions on setting up a Docker repository and installing the containerd.io package for your respective Linux distribution.

It can also be built using the following source code.

```bash
VERSION=1.5.4
wget -c https://github.com/containerd/containerd/releases/download/v${VERSION}/containerd-${VERSION}-linux-amd64.tar.gz
tar xvf containerd-${VERSION}-linux-amd64.tar.gz -C /usr/local/
mkdir /etc/containerd/ && containerd config default > /etc/containerd/config.toml
wget -c -O /etc/systemd/system/containerd.service https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
systemctl start containerd && systemctl enable containerd
```

See [Container Runtimes](https://kubernetes.io/en-us/docs/setup/production-environment/container-runtimes/) for more information.

## Install KLTS

KLTS provides installation methods based on deb and rpm software sources, and you can choose the appropriate installation method.

### Set KLTS software source

=== "Red Hat-based distributions"

     run the following code to set the software source for downloading KLTS:

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

=== "Debian-based distributions"

     run the following code to set the software source for downloading KLTS:

     ```bash
     VERSION=1.18.20-lts.2
     cat << EOF > /etc/apt/sources.list.d/klts.list
     deb [trusted=yes] https://raw.githubusercontent.com/klts-io/kubernetes-lts/deb-v${VERSION} stable main
     deb [trusted=yes] https://raw.githubusercontent.com/klts-io/others/deb stable main
     EOF

     apt-get update
     ```

=== "Red Hat based distribution, domestic acceleration 🚀"

     !!! note

         The following accelerations are all from third parties, and the safety and stability are not guaranteed. It is only recommended to be used in a test environment!!!

     run the following code to set the software source for downloading KLTS:

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

=== "Debian-based distribution, domestic acceleration 🚀"

     !!! note

         The following accelerations are all from third parties, and the safety and stability are not guaranteed. It is only recommended to be used in a test environment!!!

     run the following code to set the software source for downloading KLTS:

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

### Start installing KLTS

=== "Red Hat-based distributions"

     run the following command to install:

     ```bash
     yum install kubeadm kubelet kubectl
     ```

=== "Debian-based distributions"

     run the following command to install:

    ```bash
    apt-get install kubeadm kubelet kubectl
    ```

### Automatically start Kubelet at boot

Run the following command to automatically start Kubelet on boot:

```
systemctl enable kubelet
```

### Pull dependent image

=== "Default"

     run the following command to pull the dependent image:

     ```bash
     VERSION=1.18.20-lts.2
     REPOS=ghcr.io/klts-io/kubernetes-lts
     kubeadm config images pull --image-repository ${REPOS} --kubernetes-version v${VERSION}
     ```

=== "Domestic Acceleration 🚀"

     run the following command to pull the dependent image:

     ```bash
     VERSION=1.18.20-lts.2
     REPOS=ghcr.m.daocloud.io/klts-io/kubernetes-lts
     kubeadm config images pull --image-repository ${REPOS} --kubernetes-version v${VERSION}
     ```

Subsequent operations on kubeadm need to add __--image-repository__ and __--kubernetes-version__ to actively specify the image.

### Initialize control plane nodes

=== "Default"

     run the following command to initialize the nodes of the control plane:

     ```bash
     VERSION=1.18.20-lts.2
     REPOS=ghcr.io/klts-io/kubernetes-lts
     kubeadm init --image-repository ${REPOS} --kubernetes-version v${VERSION}
     ```

=== "Domestic Acceleration 🚀"

     run the following command to initialize the nodes of the control plane:

     ```bash
     VERSION=1.18.20-lts.2
     REPOS=ghcr.m.daocloud.io/klts-io/kubernetes-lts
     kubeadm init --image-repository ${REPOS} --kubernetes-version v${VERSION}
     ```

## Script one-click installation

In addition to the above normal installation methods, KLTS also supports scripts to automate the installation process.

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

## More ways to install

- [Nanny deployment three-node K8s cluster](./230405-step-by-step-dce5.md#k8s)
- [Using kubeadm to create a cluster](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [Install K8s with kOps](https://kubernetes.io/docs/setup/production-environment/tools/kops/)
- [Install K8s using Kubespray](https://kubernetes.io/docs/setup/production-environment/tools/kubespray/)

