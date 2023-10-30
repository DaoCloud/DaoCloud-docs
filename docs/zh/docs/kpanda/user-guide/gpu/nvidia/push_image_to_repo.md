# 向火种节点仓库上传 RedHat GPU Opreator 离线镜像

本文以 RedHat 8.4 的 `nvcr.io/nvidia/driver:525.105.17-rhel8.4` 离线驱动镜像为例， 介绍如何向火种节点仓库上传离线镜像。

## 前提条件

1. 火种节点及其组件状态运行正常。
1. 准备一个能够访问互联网、火种节点的节点，且节点上已经完成 [Docker 的安装](../../../../install/community/kind/online.md#安装-docker)。

## 操作步骤

### 步骤一：在联网节点获取离线镜像

以下操作在联网节点上进行。

1. 在有网机器拉取 `nvcr.io/nvidia/driver:525.105.17-rhel8.4` 离线驱动镜像：

    ```bash
    docker pull nvcr.io/nvidia/driver:525.105.17-rhel8.4
    ```

2. 等待镜像拉取完成后，打包镜像为 `nvidia-driver.tar` 压缩包：

    ```bash
    docker save nvcr.io/nvidia/driver:525.105.17-rhel8.4 > nvidia-driver.tar
    ```

3. 将打包好的镜像压缩包 `nvidia-driver.tar` 拷贝到火种节点：

    ```bash
    scp  nvidia-driver.tar user@ip:/root
    ```

    例如：

    ```bash
    scp  nvidia-driver.tar root@10.6.175.10:/root
    ```

### 步骤二：推送镜像到火种节点仓库

以下操作子啊火种节点上进行。

1. 登陆火种节点，将联网节点拷贝的镜像压缩包 `nvidia-driver.tar` 导入本地。

    ```bash
    docker load -i nvidia-driver.tar
    ```

2. 查看刚刚导入的镜像：

    ```bash
    docker images -a |grep nvidia
    ```

    预期输出：

    ```bash
    nvcr.io/nvidia/driver                 e3ed7dee73e9   1 days ago   1.02GB
    ```

3. 为镜像重新标记，使其与远程 Registry 仓库中的目标仓库对应：

    ```bash
    docker tag <image-name> <registry-url>/<repository-name>:<tag>
    ```

    `<image-name>` 是上一步 nvidia 镜像的名称，`<registry-url>` 是火种节点上 Registry 服务的地址，`<repository-name>` 是您要推送到的仓库名称，`<tag>` 是您为镜像指定的标签。

    例如：

    ```bash
    registry：docker tag nvcr.io/nvidia/driver 10.6.10.5/nvcr.io/nvidia/driver:525.105.17-rhel8.4
    ```

4. 将镜像火种镜像仓库：

    ```bash
    docker push {ip}/nvcr.io/nvidia/driver:525.105.17-rhel8.4
    ```

## 接下来

参考[构建 RedHat 8.4 离线 yum 源](./upgrade_yum_source_redhat8_4.md)和
[GPU Operator 离线安装](./install_nvidia_driver_of_operator.md)来为集群部署 GPU Operator。
