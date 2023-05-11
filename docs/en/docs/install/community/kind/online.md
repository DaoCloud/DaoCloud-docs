# Install DCE 5.0 Community Release online using the kind cluster

This page explains how to install DCE 5.0 Community Release online using a kind cluster.

!!! note

     Click [Install Community Release Online](../../../videos/install.md#3) to watch a video demo.

## Preparation

- Prepare a machine, recommended machine resources: CPU > 8 cores, memory > 12 GB, disk space > 100 GB.
- Make sure the machine can connect to the Internet.

Execute the following script to check system resources and networking:

```shell
set -e
if [ $(free -g|grep Mem | awk '{print $2}') -lt 12 ]; then (echo "insufficient memory! (should >=12G)"; exit 1); fi
if [ $(grep 'processor' /proc/cpuinfo |sort |uniq |wc -l) -lt 8 ]; then (echo "insufficient CPU! (should >=8C)"; exit 1); fi
if [ $(df -m / |tail -n 1 | awk '{print $4}') -lt 30720 ]; then (echo "insufficient free disk space of root partition!(should >=30G)"; exit 1) ;
ping daocloud.io -c 1 &> /dev/null || ( echo "no connection to internet! abort." && exit 1; )
echo "precheck pass.."
```

Expected output is something like:

```none
precheck pass..
```

## Install Docker

> If your machine has already installed Docker and the version is higher than 1.18, please skip this step.
>
> Domestic sources can be used when installing Docker: <https://developer.aliyun.com/mirror/docker-ce>

=== "If CentOS"

     ```shell
     set -e
     if [ -x "$(command -v docker )" ] ;then
     echo "docker already installed : version = "$(docker -v);
     exit 0
     the fi
    
     sudo yum install -y yum-utils device-mapper-persistent-data lvm2
     sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
     sudo sed -i 's+download.docker.com+mirrors.aliyun.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo
     sudo yum makecache fast
     sudo yum -y install docker-ce
     sudo service docker start
     sudo systemctl enable docker
     sudo yum install -y wget
     ```

=== "If Ubuntu"

     ```shell
     set -e
     if [ -x "$(command -v docker )" ] ;then
     echo "docker already installed : version = "$(docker -v);
     exit 0
     the fi
     sudo apt-get update
     sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
     curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
     sudo add-apt-repository --yes "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
     sudo apt-get -y update
     sudo apt-get -y install docker-ce
     sudo apt-get -y install wget
     sudo service docker start
     sudo systemctl enable docker
     ```

Note that if you already have Podman on your machine but not Docker, you still need to install Docker.
This is because of a known problem: although Podman can start kind, there will be a problem of insufficient file handles, and the problem of IP mismatch will occur after restarting.

## Install kind cluster

1. Download the kind binary package.

     ```shell
     curl -Lo ./kind https://qiniu-download-public.daocloud.io/kind/v0.17.0/kind-linux-amd64
     chmod +x ./kind
     old_kind=$(which kind)
     if [ -f "$old_kind" ]; then mv ./kind $old_kind; else mv ./kind /usr/bin/kind ;
     ```

1. Check the kind version.

     ```shell
     kind version
     ```

     The expected output is as follows:

     ```console
     kind v0.17.0 go1.19.2 linux/amd64
     ```

1. Set up the `kind_cluster.yaml` configuration file.

     Note that port 32088 in the cluster is exposed to port 8888 external to kind (you can modify it yourself). The configuration file example is as follows:

     ```yaml title="kind_cluster.yaml"
     apiVersion: kind.x-k8s.io/v1alpha4
     kind: Cluster
     nodes:
     -role: control-plane
       extraPortMappings:
       - containerPort: 32088
         hostPort: 8888
     ```

1. Create a K8s v1.25.3 example cluster named `fire-kind-cluster`.

     ```shell
     kind create cluster --image release.daocloud.io/kpanda/kindest-node:v1.25.3 --name=fire-kind-cluster --config=kind_cluster.yaml
     ```

     The expected output is as follows:

     ```console
     Creating cluster "fire-kind-cluster" ...
      ✓ Ensuring node image (release.daocloud.io/kpanda/kindest-node:v1.25.3) 🖼
      ✓ Preparing nodes 📦
      ✓ Writing configuration 📜
      ✓ Starting control-plane 🕹️
      ✓ Installing CNI 🔌
      ✓ Installing StorageClass 💾
     Set kubectl context to "kind-fire-kind-cluster"
     ```

1. View the newly created cluster.

     ```shell
     kind get clusters
     ```

     The expected output is as follows:

     ```console
     fire-kind-cluster
     ```

## Install DCE 5.0 Community Release

1. [Install dependencies](../../install-tools.md).

     !!! note

         If all dependencies are installed in the cluster, make sure the dependency versions meet the requirements:
        
         - helm ≥ 3.11.1
         - skopeo ≥ 1.11.1
         - kubectl ≥ 1.25.6
         - yq ≥ 4.31.1

1. Download the dce5-installer binary on the kind host.

     Assume VERSION is v0.7.0

     ```shell
     export VERSION=v0.7.0
     curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
     chmod +x ./dce5-installer
     ```

1. Get the IP of the host where kind is located, and start installing DCE 5.0.

     ```shell
     myIP=$(ip -o route get 1.1.1.1 | cut -d " " -f 7)
     ./dce5-installer install-app -z -k $myIP:8888
     ```

     !!! note

         The kind cluster only supports NodePort mode.
         The installation process lasts more than 30 minutes, depending on the network speed of the mirror pull.
         You can observe the Pod startup during the installation process with the following command:

         ```shell
         docker exec -it fire-kind-cluster-control-plane kubectl get po -A -w
         ```

1. After the installation is complete, the command line will prompt that the installation is successful. congratulations!
    Now you can use the **default account and password (admin/changeme)** to explore the new DCE 5.0 through the URL prompted on the screen!

     ![Installation succeeded](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

!!! success

     - Please record the URL of the reminder for the next visit.
     - After successfully installing DCE 5.0 Community Release, please [apply for a community free trial](../../../dce/license0.md).
     - If you encounter any problems during the installation process, please scan the QR code and communicate with the developer freely:
    
         ![Community Release Exchange Group](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)
