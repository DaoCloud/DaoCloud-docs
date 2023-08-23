# Linux stand-alone online experience DCE Community

This page explains how to install a stand-alone DCE Community online on a Linux machine via Docker and kind.

!!! tip

     This is a minimal installation method, which is easy to learn and experience, and its performance is better than [macOS stand-alone version](230315-install-on-macos.md). The original author is [panpan0000](https://github.com/panpan0000).

## Preparation

- Prepare a Linux machine, recommended resources: CPU > 8 cores, memory > 12 GB, disk space > 100 GB
- Make sure this machine can connect to the public network
- OS: CentOS 7 or Ubuntu 22.04

Check system resources and networking:

```bash
set -e
if [ $(free -g|grep Mem | awk '{print $2}') -lt 12 ]; then (echo "insufficient memory! (should >=12G)"; exit 1); fi
if [ $(grep 'processor' /proc/cpuinfo |sort |uniq |wc -l) -lt 8 ]; then (echo "insufficient CPU! (should >=8C)"; exit 1); fi
if [ $(df -m / |tail -n 1 | awk '{print $4}') -lt 30720 ]; then (echo "insufficient free disk space of root partition!(should >=30G)"; exit 1) ;
ping daocloud.io -c 1 &> /dev/null || ( echo "no connection to internet! abort." && exit 1; )
echo "precheck pass.."
```

The expected output is as follows:

```console
precheck pass..
```

## Install Docker

If you already have Docker on the host, and the version is higher than 1.18, you can skip this step.

=== "CentOS"

     run the following commands one by one, it will take about 5 minutes:

     ```bash
     set -e
     if [ -x "$(command -v docker )" ] ;then
       echo "docker already installed : version = "$(docker -v);
       exit 0
     the fi
     ```
     ```bash
     sudo yum install -y yum-utils device-mapper-persistent-data lvm2
     sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
     sudo sed -i 's+download.docker.com+mirrors.aliyun.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo
     sudo yum makecache fast
     sudo yum -y install docker-ce
     sudo service docker start
     sudo systemctl enable docker
     sudo yum install -y wget
     ```

=== "Ubuntu"

     run the following commands one by one, it will take about 5 minutes:

     ```bash
     set -e
     if [ -x "$(command -v docker )" ] ;then
       echo "docker already installed : version = "$(docker -v);
       exit 0
     the fi
     ```
     ```bash
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

!!! note

     - If you already have Podman on your machine but not Docker, you still need to install Docker.
     - This is because of a known problem: Although Podman can start kind, there will be a problem of insufficient file handles, and the problem of IP mismatch will occur after restarting.
     - For Docker installation issues, please refer to [Docker Official Installation Instructions](https://docs.docker.com/desktop/install/linux-install/).

## kind cluster

1. Download the kind binary package.

     ```bash
     curl -Lo ./kind https://qiniu-download-public.daocloud.io/kind/v0.17.0/kind-linux-amd64
     chmod +x ./kind
     old_kind=$(which kind)
     if [ -f "$old_kind" ]; then mv ./kind $old_kind; else mv ./kind /usr/bin/kind ;
     ```

     View the kind version:

     ```bash
     kind version
     ```

     The expected output is as follows:

     ```console
     kind v0.17.0 go1.19.2 linux/amd64
     ```

1. Create `kind_cluster.yaml` configuration file. Expose port 32088 in the cluster to port 8888 external to kind (can be modified by yourself).

     ```bash
     cat > kind_cluster.yaml << EOF
     apiVersion: kind.x-k8s.io/v1alpha4
     kind: Cluster
     nodes:
     -role: control-plane
       extraPortMappings:
       - containerPort: 32088
         hostPort: 8888
     EOF
     ```

1. Create a K8s cluster named `fire-kind-cluster` through kind, taking k8s 1.25.3 as an example.

     ```bash
     kind create cluster --image docker.m.daocloud.io/kindest/node:v1.25.3 --name=fire-kind-cluster --config=kind_cluster.yaml
     ```

     This step will take about 3~5 minutes, depending on the network speed of the image download. The expected output is as follows:

     ```console
     Creating cluster "fire-kind-cluster" ...
      ✓ Ensuring node image (docker.m.daocloud.io/kindest/node:v1.25.3) 🖼
      ✓ Preparing nodes 📦
      ✓ Writing configuration 📜
      ✓ Starting control-plane 🕹️
      ✓ Installing CNI 🔌
      ✓ Installing StorageClass 💾
     Set kubectl context to "kind-fire-kind-cluster"
     ```

1. View the newly created kind cluster.

     ```console
     kind get clusters
     ```

     The expected output is as follows:

     ```console
     fire-kind-cluster
     ```

## Install DCE Community

1. Install dependencies, see also [Dependency Installation Instructions](../install/install-tools.md)

     ```shell
     curl -LO https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/install_prerequisite.sh
     bash install_prerequisite.sh online community
     ```

1. Download the dce5-installer binary file on the host (you can also [download via browser](../download/index.md)

     ```shell
     export VERSION=v0.5.0
     curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
     chmod +x ./dce5-installer
     ```

1. run the following command to start the installation.

     ```shell
     myIP=$(ip -o route get 1.1.1.1 | cut -d " " -f 7)
     ./dce5-installer install-app -z -k $myIP:8888
     ```

     !!! note

         The kind cluster only supports NodePort mode.

1. After the installation is complete, the command line will prompt that the installation is successful. congratulations!

     Now you can use the **default account and password (admin/changeme)** to explore the new DCE 5.0 through the URL prompted on the screen (the default is `https://${host IP}:8888`)!

     ![Installation succeeded](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)
