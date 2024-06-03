# K8s 集群基于 Docker 运行时的容器磁盘容量限制

Docker 提供了配置项可以限制容器占用磁盘空间的大小，此大小影响镜像和容器文件系统，默认 10G，本文将介绍部署集群时如何配置参数来修改该值的大小。

## 前提条件

根据 Docker 官方文档关于 overlay2-options 的描述：在配置 Docker overlay2.size 之前，需要调整操作系统中文件系统类型 xfs

- 集群运行时为 Docker
- 节点操作系统文件类型为 xfs

另外本操作步骤以 CentOS 7 为例，节点的基本信息如下：

```bash
$ cat /etc/os-release
NAME="CentOS Linux"
VERSION="7 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="7"
PRETTY_NAME="CentOS Linux 7 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:7"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"
 
CENTOS_MANTISBT_PROJECT="CentOS-7"
CENTOS_MANTISBT_PROJECT_VERSION="7"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="7"
 
$ uname -a
Linux localhost.localdomain 3.10.0-957.el7.x86_64 # (1)!
```

1. SMP Thu Nov 8 23:39:32 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

## 操作指南

- 参考容器管理[创建集群](../../kpanda/user-guide/clusters/create-cluster.md)，其他信息填写完毕后进入到 **高级配置** 模块

- 在 **高级配置** 界面中自定义参数中增加以下一行：

    ```config
    docker_storage_options: -s overlay2 --storage-opt overlay2.size=1G
    ```

    [image](../images/pquota2.png)

    该参数意味着限制 Docker 单一容器的最大磁盘占用为 1G，超出 1G 将无法继续写入。

## 验证

集群部署完成后，验证容器磁盘占用限制是否生效。

- 在集群节点上创建一个测试容器：

    ```bash
    docker run --name test -d busybox:latest sleep infinity
    ```

- 进入容器内，测试大文件对容器磁盘的占用限制：

    ```bash
    docker exec -it test sh

    dd if=/dev/zero of=a bs=100M count=10
    ```

- 现象为一开始能够成功创建 100M 的文件 a，然后再次创建 100M 的文件 b 时，报错 “No space left on device”，证明磁盘限制已生效，如下图：

    [image](../images/pquota1.png)
