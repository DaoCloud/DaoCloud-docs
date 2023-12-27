# 构建 CentOS 7.9 离线 yum 源

## 使用场景介绍

当工作节点的内核版本与 Global 集群的控制节点内核版本或 OS 类型不一致时，需要用户手动构建离线 yum 源。

本文介绍如何构建离线 yum 源， 并在安装 Gpu Operator 时，通过 `RepoConfig.ConfigMapName` 参数来使用。

## 前提条件

1. 用户已经在平台上安装了 v0.12.0 及以上版本的 addon 离线包。
2. 准备一个能够和待部署 GPU Operator 的集群网络能够联通的文件服务器，如 nginx 或 minio。
3. 准备一个能够访问互联网、待部署 GPU Operator 的集群和文件服务器的节点，且节点上已经完成 [Docker 的安装](../../../../install/community/kind/online.md#安装-docker)。

## 操作步骤

本文以内核版本为 3.10.0-1160.95.1.el7.x86_64 的 CentOS 7.9 节点为例，介绍如何构建 GPU operator 离线包的 yum 源。

### 步骤一：检查集群节点的 OS 和内核版本

分别在 Global 集群的控制节点和待部署 GPU Operator 的节点执行如下命令，若两个节点的 OS 和内核版本一致则无需构建 yum 源，可参考[离线安装 GPU Operator](./install_nvidia_driver_of_operator.md) 文档直接安装；若两个节点的 OS 或内核版本不一致，请执行步骤二。

1、执行如下命令，查看集群下待部署 GPU Operator 节点的发行版名称和版本号。

```bash
cat /etc/redhat-release
```

预期输出如下：

```
CentOS Linux release 7.9 (Core)
```

输出结果为当前节点内核版本 `CentOS 7.9` 。

2、执行如下命令，查看集群下待部署 GPU Operator 节点的内核版本。

```bash
uname -a
```

预期输出如下：

```
Linux localhost.localdomain 3.10.0-1160.95.1.el7.x86_64 #1 SMP Mon Oct 19 16:18:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

输出结果为当前节点内核版本 `3.10.0-1160.el7.x86_64` 。



### 步骤二：制作离线 yum 源

本步骤在一个能够访问互联网和文件服务器的节点上进行操作。

1. 在一个能够访问互联网和文件服务器的节点上执行如下命令新建一个名为 __yum.sh__ 的脚本文件。

    ```bash
    vi yum.sh
    ```

    然后按下 i 键进入插入模式，输入以下内容：

    ```bash
    export TARGET_KERNEL_VERSION=$1

    cat >> run.sh << \EOF
    #! /bin/bash
    echo "start install kernel repo"
    echo ${KERNEL_VERSION}
    mkdir centos-base

    if [ "$OS" -eq 7 ]; then
        yum install --downloadonly --downloaddir=./centos-base perl
        yum install --downloadonly --downloaddir=./centos-base elfutils-libelf.x86_64
        yum install --downloadonly --downloaddir=./redhat-base elfutils-libelf-devel.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-headers-${KERNEL_VERSION}.el7.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-devel-${KERNEL_VERSION}.el7.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-${KERNEL_VERSION}.el7.x86_64
        yum install  -y --downloadonly --downloaddir=./centos-base groff-base
    elif [ "$OS" -eq 8 ]; then
        yum install --downloadonly --downloaddir=./centos-base perl
        yum install --downloadonly --downloaddir=./centos-base elfutils-libelf.x86_64
        yum install --downloadonly --downloaddir=./redhat-base elfutils-libelf-devel.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-headers-${KERNEL_VERSION}.el8.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-devel-${KERNEL_VERSION}.el8.x86_64
        yum install --downloadonly --downloaddir=./centos-base kernel-${KERNEL_VERSION}.el8.x86_64
        yum install  -y --downloadonly --downloaddir=./centos-base groff-base
    else
        echo "Error os version"
    fi

    createrepo centos-base/
    ls -lh centos-base/
    tar -zcf centos-base.tar.gz centos-base/
    echo "end install kernel repo"
    EOF

    cat >> Dockerfile << EOF
    FROM centos:7
    ENV KERNEL_VERSION=""
    ENV OS=7
    RUN yum install -y createrepo
    COPY run.sh .
    ENTRYPOINT ["/bin/bash","run.sh"]
    EOF

    docker build -t test:v1 -f Dockerfile .
    docker run -e KERNEL_VERSION=$TARGET_KERNEL_VERSION --name centos7.9 test:v1
    docker cp centos7.9:/centos-base.tar.gz .
    tar -xzf centos-base.tar.gz
    ```

    按下 __esc__ 键退出插入模式，然后输入 __:wq__ 保存并退出。

2. 运行 __yum.sh__ 文件：

    ```bash
    bash -x yum.sh TARGET_KERNEL_VERSION
    ```

    `TARGET_KERNEL_VERSION` 参数用于指定集群节点的内核版本，注意：发行版标识符（如： __.el7.x86_64 __ ）无需输入。

    例如：

    ```bash
    bash -x yum.sh 3.10.0-1160.95.1
    ```

至此，您已经生成了内核为 __3.10.0-1160.95.1.el7.x86_64__ 的离线的 yum 源： __centos-base__ 。

### 步骤三：上传离线 yum 源到文件服务器

本步骤继续在一个能够访问互联网和文件服务器的节点上进行操作。主要用于将上一步中生成的 yum 源上传到可以被待部署 GPU Operator 的集群进行访问的文件服务器中。
文件服务器可以为 Nginx 、 Minio 或其它支持 Http 协议的文件服务器。

本操作示例采用的是 DCE5 火种节点内置的 Minio 作为文件服务器，Minio 相关信息如下：

- 访问地址： `http://10.5.14.200:9000（一般为{火种节点 IP} + {9000 端口}）` 
- 登录用户名：rootuser
- 登录密码：rootpass123

1. 在节点当前路径下，执行如下命令将节点本地 mc 命令行工具和 minio 服务器建立链接。

    ```bash
    mc config host add minio http://10.5.14.200:9000 rootuser rootpass123
    ```

    预期输出如下：

    ```bash
    Added `minio` successfully.
    ```

    mc 命令行工具是 Minio 文件服务器提供的客户端命令行工具，详情请参考：
    [MinIO Client](https://min.io/docs/minio/linux/reference/minio-mc.html)。

2. 在节点当前路径下，新建一个名为 __centos-base__ 的存储桶(bucket)。

    ```bash
    mc mb -p minio/centos-base
    ```

    预期输出如下：

    ```bash
    Bucket created successfully __minio/centos-base__ .
    ```

3. 将存储桶 __centos-base__ 的访问策略设置为允许公开下载。以便在后期安装 GPU-operator 时能够被访问。

    ```bash
    mc anonymous set download minio/centos-base
    ```
    预期输出如下：

    ```bash
    Access permission for `minio/centos-base` is set to `download` 
    ```

4. 在节点当前路径下，将步骤二生成的离线 yum 源文件 __centos-base__ 复制到 minio 服务器的 __minio/centos-base__ 存储桶中。

    ```bash
    mc cp centos-base minio/centos-base --recursive
    ```

### 步骤四：在集群创建配置项用来保存 yum 源信息

本步骤在待部署 GPU Operator 集群的控制节点上进行操作。

1. 执行如下命令创建名为 __CentOS-Base.repo__ 的文件，用来指定 yum 源存储的配置信息。

    ```bash
    # 文件名称必须为 CentOS-Base.repo，否则安装 gpu-operator 时无法被识别
    cat > CentOS-Base.repo << EOF
    [extension-0]
    baseurl = http://10.5.14.200:9000/centos-base/centos-base #步骤三中，放置 yum 源的文件服务器地址
    gpgcheck = 0
    name = kubean extension 0
    
    [extension-1]
    baseurl = http://10.5.14.200:9000/centos-base/centos-base #步骤三中，放置 yum 源的文件服务器地址
    gpgcheck = 0
    name = kubean extension 1
    EOF
    ```

2. 基于创建的 __CentOS-Base.repo__ 文件，在 gpu-operator 命名空间下，创建名为 __local-repo-config__ 的配置文件：

    ```bash
    kubectl create configmap local-repo-config  -n gpu-operator --from-file=./CentOS-Base.repo 
    ```

    预期输出如下：

    ```
    configmap/local-repo-config created
    ```

    __local-repo-config__ 配置文件用于在安装 gpu-operator 时，提供 `RepoConfig.ConfigMapName` 参数的值，配置文件名称用户可自定义。

3. 查看 __local-repo-config__ 的配置文件的内容：

    ```bash
    kubectl get configmap local-repo-config  -n gpu-operator -oyaml
    ```

    预期输出如下：

    ```yaml
    apiVersion: v1
    data:
    CentOS-Base.repo: "[extension-0]\nbaseurl = http://10.6.232.5:32618/centos-base#步骤二中，放置 yum 源的文件服务器路径\ngpgcheck = 0\nname = kubean extension 0\n  \n[extension-1]\nbaseurl
        = http://10.6.232.5:32618/centos-base #步骤二中，放置 yum 源的文件服务器路径\ngpgcheck = 0\nname
        = kubean extension 1\n"
    kind: ConfigMap
    metadata:
    creationTimestamp: "2023-10-18T01:59:02Z"
    name: local-repo-config
    namespace: gpu-operator
    resourceVersion: "59445080"
    uid: c5f0ebab-046f-442c-b932-f9003e014387
    ```

至此，您已成功为待部署 GPU Operator 的集群创建了离线 yum 源配置文件。
通过在[离线安装 GPU Operator](./install_nvidia_driver_of_operator.md) 时通过 `RepoConfig.ConfigMapName` 参数来使用。
