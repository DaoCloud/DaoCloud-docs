# 边缘节点接入要求

边缘节点需要满足下表的规格要求。

## 操作系统 OS

- x86_64 架构

    Ubuntu LTS (Xenial Xerus)、Ubuntu LTS (Bionic Beaver) 、CentOS、EulerOS、RHEL、银河麒麟、中兴新支点、中标麒麟、openEuler

- armv7i（arm32）架构

    Raspbian GNU/Linux (stretch)

- aarch64（arm64）架构

    Ubuntu LTS (Bionic Beaver)、CentOS、EulerOS、openEuler

## 内存

边缘软件常规开销约 150MB，具体视边缘管理压力适当增加。

为保证业务的正常运行，建议边缘节点的内存大于 256MB。

## CPU

不小于 1 核

## 硬盘

不小于 1GB

## GPU（可选）

1. 当前支持 Nvidia Tesla 系列 P4、P40、T4 等型号 GPU

    含有 GPU 硬件的机器，作为边缘节点的时候可以不使用 GPU。

    如果边缘节点使用 GPU，您需要在纳管前安装 GPU 驱动及 Nvidia Docker 适配（nvidia-docker2）。

    需设置容器引擎的默认 runtime 为 nvidia。

    ```sh
    /etc/docker/daemon.json
    ```

    ```json
    {
      "default-runtime": "nvidia",
      "runtimes": {
        "nvidia": {
          "path": "nvidia-container-runtime",
          "runtimeArgs": []
        }
      }
    }
    ```

2. ARM64 架构 Nvidia GPU 其它要求

    - 建议系统安装 Jetpack4.5+
    - 镜像需使用托管在 nvidia l4t 上的[基础镜像构建](https://catalog.ngc.nvidia.com/containers)

3. 环境验证

    ```sh
    nvidia-container-cli -k -d /dev/tty info
    ```

    当以上命令为 successful 时，即可接入（上述工具安装 nvidia-docker2 后自带）。

## 容器运行时

Docker 版本必须高于 19.0，推荐使用 19.03.6 版本。

## glibc

版本必须高于 2.17。

查看方法：

```sh
ubuntu：ldd --version
```

## 端口

边缘节点需要使用如下端口，请确保这些端口能够正常使用。

- 1883：边缘节点内置 MQTT broker 监听端口，并需要开放该端口。

## 时间同步

边缘节点时间需要与云端服务器时间保持一致，建议 UTC 标准时间。
