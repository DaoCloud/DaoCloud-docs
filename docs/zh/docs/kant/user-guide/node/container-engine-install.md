# 边缘节点安装容器引擎

边缘节点在接入系统之前，需要先配置节点环境，其中就包括安装容器引擎。本文介绍如何安装容器运行时组件 Containerd.

!!! note

    - 如果您安装的 KubeEdge 版本高于 v1.12.0，推荐安装 Containerd。
    - KubeEdge v1.15.0以及以上版本，请安装 v1.6.0 或更高版本的 Containerd。

## 安装 Containerd

边缘节点接入需要依赖 CNI 插件，所以建议直接安装带有 CNI 插件的 Containerd，操作步骤如下：

1. 下载 Containerd 安装包并上传到边缘节点，前往[下载地址](https://github.com/containerd/containerd/tags)，根据边缘节点操作系统以及 CPU 架构选择对应版本安装包。

2. 将安装包解压到根目录。

    ```shell
    tar xvzf {安装包名称} -C /
    ```

3. 生成 Containerd 配置文件。

    !!! note

        注意修改配置文件的 sandbox 镜像，国内可能拉不到 k8s 仓库的镜像，可以换成 DaoCloud 的镜像仓库：m.daocloud.io/k8s.gcr.io/pause:3.8。

    ```shell
    mkdir /etc/containerd
    containerd config default > /etc/containerd/config.toml
    ```

4. 启动 Containerd。

    ```shell
    systemctl start containerd && systemctl enable containerd
    ```

5. 验证 Containerd 是否安装成功并且成功运行。

    ```shell
    systemctl status containerd
    ```

## 安装 nerdctl 工具（可选）

建议安装 nerdctl 命令行工具，方便在节点上对容器进行运维调试，操作步骤如下：

1. 下载 nerdctl 安装包并上传到边缘节点，前往[下载](https://github.com/containerd/nerdctl/releases)。

    !!! note

        请根据实际操作系统以及 CPU 架构选择对应安装包，请安装 v1.7.0 或更高版本。

2. 解压安装包，并将二进制文件拷贝至 **/usr/local/bin** 目录下。

    ```shell
    tar -zxvf nerdctl-1.7.6-linux-amd64.tar.gz
    cd nerdctl-1.7.6-linux-amd64
    cp nerdctl /usr/local/bin
    ```

3. 验证 Containerd 是否安装成功。

    使用如下命令查看 Server 版本号，若果能正常显示，说明 nerdctl 已经成功安装。

    ```shell
    nerdctl version
    ```