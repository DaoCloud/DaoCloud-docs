# Install Community on kind Cluster Online

This page explains how to install DCE Community package on a kind cluster online.

!!! note

    Click [Online Installation of Community Package](../../../videos/install.md#3) to watch the video tutorial.

## Preparation

- A node with CPU > 8 cores, memory > 12 GB, disk > 100 GB.
- Ensure that the node can access the Internet.

Run the following script to check the system resources and network connectivity:

```shell
set -e
if [ $(free -g|grep Mem | awk '{print $2}')              -lt 12 ]; then (echo "insufficient memory! (should >=12G)";); fi
if [ $(grep 'processor' /proc/cpuinfo |sort |uniq |wc -l) -lt 8 ]; then (echo "insufficient CPU! (should >=8C)";); fi
if [ $(df -m / |tail -n 1 | awk '{print $4}') -lt 30720 ]; then (echo "insufficient free disk space of root partition!(should >=30G)";); fi
ping daocloud.io -c 1 &> /dev/null || ( echo "no connection to internet! abort.")
echo "precheck pass.."
```

Expected output is something like:

```none
precheck pass...
```

## Install Docker

!!! note

    - If you have installed Docker v1.18+, skip this step.
    - Use domestic source to accelerate: <https://developer.aliyun.com/mirror/docker-ce>
    - If you have Podman on your node but not Docker, you still need to install Docker.This is because of a known bug: although Podman can start kind, there will be a problem of insufficient file handles and IP mismatch.

=== "On CentOS"

     ```shell
     set -e
     if  [ -x "$(command -v docker )" ] ;then
        echo "docker already installed : version = "$(docker -v);
     else
        echo "docker not found, please install it first."
     fi
    
     sudo yum install -y yum-utils device-mapper-persistent-data lvm2
     sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
     sudo sed -i 's+download.docker.com+mirrors.aliyun.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo
     sudo yum makecache fast
     sudo yum -y install docker-ce
     sudo service docker start
     sudo systemctl enable docker
     sudo yum install -y wget
     ```

=== "On Ubuntu"

     ```shell
     set -e
     if  [ -x "$(command -v docker )" ] ;then
        echo "docker already installed : version = "$(docker -v);
     else
        echo "docker not found, please install it first."
     fi
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

## Install kind cluster

1. Download the binary package of kind .

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

    The expected output is like:

    ```console
    kind v0.17.0 go1.19.2 linux/amd64
    ```

2. Modify the `kind_cluster.yaml` to make it applicable in your environment.

    Expose the internal port `32088` to port 8888 (customizable) for external communication. The configuration file example is as follows:

    ```yaml title="kind_cluster.yaml"
    apiVersion: kind.x-k8s.io/v1alpha4
    kind: Cluster
    nodes:
    -role: control-plane
      extraPortMappings:
      - containerPort: 32088
        hostPort: 8888
    ```

3. Create a Kubernetes cluster of v1.25.3, named (for example) `fire-kind-cluster`.

     ```shell
     kind create cluster --image release.daocloud.io/kpanda/kindest-node:v1.25.3 --name=fire-kind-cluster --config=kind_cluster.yaml
     ```

     The expected output is like:

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

4. Check the newly created cluster.

     ```shell
     kind get clusters
     ```

     The expected output is like:

     ```console
     fire-kind-cluster
     ```

## Install DCE Community package

1. [Install dependencies](../../install-tools.md).

    You must install all dependencies of certain versions:

        - helm ≥ 3.11.1
        - skopeo ≥ 1.11.1
        - kubectl ≥ 1.25.6
        - yq ≥ 4.31.1

2. Download the `dce5-installer` binary file on the kind host.

    Takve VERSION=v0.10.0 as an example:

    ```shell
    export VERSION=v0.10.0
    curl -Lo ./dce5-installer https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/dce5-installer-$VERSION
    chmod +x ./dce5-installer
    ```

3. Get the IP of the node where kind is installed, and start installing DCE 5.0.

    ```shell
    myIP=$(ip -o route get 1.1.1.1 | cut -d " " -f 7)
    ./dce5-installer install-app -z -k $myIP:8888
    ```

    !!! note

        The kind cluster only supports NodePort mode.
        The installation lasts more than 30 minutes, depending on the network speed of image pull.
        You can observe the Pod startup during the installation with the following command:

        ```shell
        docker exec -it fire-kind-cluster-control-plane kubectl get po -A -w
        ```

4. After the installation is complete, the command line will prompt that the installation is successful. Congratulations!

    Now you can use the **default account and password (admin/changeme)** to explore the new DCE 5.0 through the URL prompted on the screen!

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/install/images/success.png)

    !!! success

        Please write down the prompted URL for your next visit.

!!! success

     - Keep the DCE 5.0 URL for the next visit.
     - As DCE Community package is installed, please [apply for a free license](../../../dce/license0.md).
     - If you have any problems about DCE 5.0, please scan the QR code and communicate with the developer freely:
    
        ![Community Package Exchange Group](https://docs.daocloud.io/daocloud-docs-images/docs/images/assist.png)
