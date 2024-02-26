# 构建虚拟机镜像

本文将介绍如何构建需要的虚拟机镜像。

虚拟机镜像其实就是副本文件，是安装有操作系统的一个磁盘分区。常见的镜像文件格式包括 raw、qcow2、vmdk等。

## 构建镜像

下面是构建虚拟机镜像的一些详细步骤：

1. 下载系统镜像

    在构建虚拟机镜像之前，您需要下载所需的系统镜像。我们推荐使用 qcow2、raw 或 vmdk 格式的镜像。可以访问以下链接获取 CentOS 和 Fedora 的镜像：

    - [CentOS Cloud Images](https://cloud.centos.org/centos/7/images/?C=M;O=D)：支持从官方 CentOS 项目或其他资源中获取 CentOS 镜像。请确保选择与您的虚拟化平台兼容的版本。
    - [Fedora Cloud Images](https://fedoraproject.org/zh-Hans/cloud/download)： 支持从官方 Fedora 项目获取镜像。根据您的需求选择合适的版本。

2. 构建 Docker 镜像并推送到容器镜像仓库

    在此步骤中，我们将使用 Docker 构建一个镜像，并将其推送到容器镜像仓库，以便在需要时能够方便地部署和使用。

    - 创建 Dockerfile 文件

        ```Dockerfile
        FROM scratch
        ADD --chown=107:107 CentOS-7-x86_64-GenericCloud.qcow2 /disk/
        ```
     
        向基于空白镜像构建的镜像中添加名为 `CentOS-7-x86_64-GenericCloud.qcow2` 的文件，并将其放置在镜像中的 __/disk/__ 目录下。通过这个操作，镜像就包含了这个文件，可以在创建虚拟机时使用它来提供 CentOS 7 x86_64 的操作系统环境。

    - 构建镜像

        ```shell
        docker build -t release-ci.daocloud.io/ghippo/kubevirt-demo/centos7:v1 .
        ```
        
        上述命令将使用 Dockerfile 中的指令构建一个名为 `release-ci.daocloud.io/ghippo/kubevirt-demo/centos7:v1` 的镜像。您可以根据项目需求修改镜像名称。

    - 推送镜像至容器镜像仓库

        执行以下命令将构建好的镜像推送到名为 `release-ci.daocloud.io` 的镜像仓库，您还可以根据需要修改镜像仓库的名称和地址。

        ```shell
        docker push release-ci.daocloud.io/ghippo/kubevirt-demo/centos7:v1
        ```

以上是构建虚拟机镜像的详细步骤和说明。通过按照这些步骤操作，您将能够成功构建并推送用于虚拟机的镜像，以满足您的使用需求。
