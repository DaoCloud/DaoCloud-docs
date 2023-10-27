# 构建 RedHat 8.4 离线 yum 源

## 使用场景介绍

DCE 5 预置了 CentOS 7.9，内核为 3.10.0-1160 的 GPU operator 离线包。其它 OS 类型的节点或内核需要用户手动构建离线 yum 源。

本文介绍如何基于 Global 集群任意节点构建 RedHat 8.4 离线 yum 源包，并在安装 Gpu Operator 时，通过 `RepoConfig.ConfigMapName` 参数来使用。

## 前提条件

1. 用户已经在平台上安装了 v0.12.0 及以上版本的 addon 离线包。
2. 待部署 GPU Operator 的集群节点 OS 必须为 RedHat 8.4，且内核版本完全一致。
3. 准备一个能够和待部署 GPU Operator 的集群网络能够联通的文件服务器，如 nginx 或 minio。
4. 准备一个能够访问互联网、待部署 GPU Operator 的集群和文件服务器的节点，且节点上已经完成 [Docker 的安装](../../../../install/community/kind/online.md#安装-docker)。
5. Global 集群的节点必须为 RedHat 8.4 4.18.0-305.el8.x86_64。

## 操作步骤

本文以 RedHat 8.4 4.18.0-305.el8.x86_64 节点为例，介绍如何基于 Global 集群任意节点构建 RedHat 8.4 离线 yum 源包，并在安装 Gpu Operator 时，通过 `RepoConfig.ConfigMapName` 参数来使用。

### 步骤一：下载火种节点中的 yum 源

以下操作在 global 集群的 master 节点上执行。

1. 使用 ssh 或其它方式进入 global 集群内任一节点执行如下命令：

    ```bash
    cat /etc/yum.repos.d/extension.repo #查看 extension.repo 中的内容。
    ```
    预期输出如下：
    ```bash
    [extension-0]
    baseurl = http://10.5.14.200:9000/kubean/redhat/$releasever/os/$basearch
    gpgcheck = 0
    name = kubean extension 0

    [extension-1]
    baseurl = http://10.5.14.200:9000/kubean/redhat-iso/$releasever/os/$basearch/AppStream
    gpgcheck = 0
    name = kubean extension 1

    [extension-2]
    baseurl = http://10.5.14.200:9000/kubean/redhat-iso/$releasever/os/$basearch/BaseOS
    gpgcheck = 0
    name = kubean extension 2
    ```

2. 在 `root` 路径下新建一个名为 `redhat-base-repo` 的文件夹

    ```bash
    mkdir redhat-base-repo
    ```

3. 下载 yum 源中的 rpm 包到本地：

    下载 extension-1 中的 rpm 包
    ```bash
    reposync  -p redhat-base-repo  -n --repoid=extension-1
    ```
    下载 extension-2 中的 rpm 包
    ```bash
    reposync  -p redhat-base-repo  -n --repoid=extension-1
    ```

### 步骤二：下载 elfutils-libelf-devel-0.187-4.el8.x86_64.rpm 包

以下操作在联网节点执行操作，在操作前，您需要保证联网节点和 Global 集群 master 节点间的网络联通性。

1. 在联网节点执行如下命令，下载 `elfutils-libelf-devel-0.187-4.el8.x86_64.rpm` 包：

    ```bash
    wget https://rpmfind.net/linux/centos/8-stream/BaseOS/x86_64/os/Packages/elfutils-libelf-devel-0.187-4.el8.x86_64.rpm
    ```

2. 在当前目录下将 `elfutils-libelf-devel-0.187-4.el8.x86_64.rpm` 包传输至步骤一中的节点上：

    ```bash
    scp  elfutils-libelf-devel-0.187-4.el8.x86_64.rpm user@ip:~/redhat-base-repo/extension-2/Packages/
    ```
    例如
    ```bash
    scp  elfutils-libelf-devel-0.187-4.el8.x86_64.rpm root@10.6.175.10:~/redhat-base-repo/extension-2/Packages/
    ```

### 步骤三：生成本地 yum repo

以下操作在步骤一中 global 集群的 master 节点上执行。

1. 创建 yum repo 目录：

    ```bash
    mkdir /root/redhat-base-repo/extension-1/repodata
    ```
    ```bash
    mkdir /root/redhat-base-repo/extension-2/repodata
    ```

2. 生成目录 repo 索引：

    ```bash
    createrepo -po ~/redhat-base-repo/extension-1/repodata ~/redhat-base-repo/extension-1/Packages
    ```

    ```bash
    createrepo -po ~/redhat-base-repo/extension-2/repodata ~/redhat-base-repo/extension-2/Packages
    ```

至此，您已经生成了内核为 `4.18.0-305.el8.x86_64` 的离线的 yum 源：`redhat-base-repo`。

### 步骤四：将本地生成的 yum repo 上传至文件服务器

本操作示例采用的是 DCE5 火种节点内置的 Minio 作为文件服务器，用户可基于自身情况选择文件服务器。Minio 相关信息如下：

- 访问地址：http://10.5.14.200:9000（一般为{火种节点 IP} + {9000 端口}）
- 登录用户名：rootuser
- 登录密码：rootpass123

1. 在节点当前路径下，执行如下命令将节点本地 mc 命令行工具和 minio 服务器建立链接。

    ```bash
    mc config host add minio 文件服务器访问地址 用户名 密码
    ```
    例如：
    ```bash
    mc config host add minio http://10.5.14.200:9000 rootuser rootpass123
    ```
    预期输出如下：
    ```bash
    Added `minio` successfully.
    ```
    mc 命令行工具是 Minio 文件服务器提供的客户端命令行工具，详情请参考：[MinIO Client](https://min.io/docs/minio/linux/reference/minio-mc.html)。

2. 在节点当前路径下，新建一个名为 `redhat-base` 的存储桶(bucket)。

    ```bash
    mc mb -p minio/redhat-base
    ```
    预期输出如下：
    ```bash
    Bucket created successfully `minio/redhat-base`.
    ```

3. 将存储桶 `redhat-base` 的访问策略设置为允许公开下载。以便在后期安装 GPU-operator 时能够被访问。

    ```bash
    mc anonymous set download minio/redhat-base
    ```
    预期输出如下：
    ```bash
    Access permission for `minio/redhat-base` is set to `download`
    ```

4. 在节点当前路径下，将步骤二生成的离线 yum 源文件 `redhat-base-repo` 复制到 minio 服务器的 `minio/redhat-base` 存储桶中。

    ```bash
    mc cp redhat-base-repo minio/redhat-base --recursive
    ```

### 步骤四：在集群创建配置项用来保存 yum 源信息。

本步骤在待部署 GPU Operator 集群的控制节点上进行操作。

1. 执行如下命令创建名为 `redhat.repo` 的文件，用来指定 yum 源存储的配置信息。

    ```bash
    # 文件名称必须为 redhat.repo，否则安装 gpu-operator 时无法被识别
    cat > redhat.repo.repo << EOF
    [extension-0]
    baseurl = http://10.5.14.200:9000/redhat-base/redhat-base-repo #步骤一中，放置 yum 源的文件服务器地址
    gpgcheck = 0
    name = kubean extension 0
    
    [extension-1]
    baseurl = http://10.5.14.200:9000/redhat-base/redhat-base-repo #步骤一中，放置 yum 源的文件服务器地址
    gpgcheck = 0
    name = kubean extension 1
    EOF
    ```

2. 基于创建的 `redhat.repo` 文件，在 gpu-operator 命名空间下，创建名为 `local-repo-config` 的配置文件：

    ```bash
    kubectl create configmap local-repo-config  -n gpu-operator --from-file=./redhat.repo 
    ```
    预期输出如下：
    ```
    configmap/local-repo-config created
    ```
    `local-repo-config` 配置文件用于在安装 gpu-operator 时，提供 `RepoConfig.ConfigMapName` 参数的值，配置文件名称用户可自定义。

3. 查看 `local-repo-config` 的配置文件的内容：

    ```bash
    kubectl get configmap local-repo-config  -n gpu-operator -oyaml
    ```

至此，您已成功为待部署 GPU Operator 的集群创建了离线 yum 源配置文件。通过在[离线安装 GPU Operator](./install_nvidia_driver_of_operator.md) 时通过 `RepoConfig.ConfigMapName` 参数来使用。

