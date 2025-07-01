# 边缘节点接入要求

边缘节点需要满足下表的规格要求。

## 操作系统 OS

- x86_64 架构

    Ubuntu LTS (Xenial Xerus / Bionic Beaver / Jammy Jellyfish / Focal Fossa)、CentOS、EulerOS、RHEL、银河麒麟、中兴新支点、中标麒麟、openEuler、Rocky Linux

<!-- - armv7i（arm32）架构

    Raspbian GNU/Linux (stretch) -->

- aarch64（arm64）架构

    Ubuntu LTS (Bionic Beaver)、CentOS、EulerOS、openEuler、Rocky Linux

## 内存

边缘软件常规开销约 150MB，具体视边缘管理压力适当增加。

为保证业务的正常运行，建议边缘节点的内存大于 256MB。

## CPU

不小于 1 核

## 硬盘

不小于 1GB

## 容器运行时

容器运行时支持 Docker 或 containerd。

- Docker 版本必须高于 v19.0，推荐使用 v19.03.6 版本。

须知：如果您安装的 KubeEdge 版本高于或等于 v1.14 且云端 Kubernetes 版本高于 v1.24，除 Docker 之外，还需要安装 CRI-Dockerd 。

- 如果您安装的 KubeEdge 版本高于 v1.12.0，推荐安装 containerd，安装流程参见[边缘节点安装容器引擎](./container-engine-install.md)。

## glibc

版本必须高于 2.17。

ubuntu 查看版本示例：

```sh
ldd --version
```

## 端口

边缘节点需要使用如下端口，请确保这些端口能够正常使用。

- 1883：边缘节点内置 MQTT broker 监听端口，并需要开放该端口。

## 时间同步

边缘节点时间需要与云端服务器时间保持一致，建议 UTC 标准时间。

## 组件调度

边端不支持运行 Calico、KubeProxy、Insight 等组件，为避免云上 Daemonset 应用调度到边缘，导致节点状态异常，需添加如下注解进行屏蔽。

```yaml
nodeAffinity:
  requiredDuringSchedulingIgnoredDuringExecution:
    nodeSelectorTerms:
      - matchExpressions:
        - key: node-role.kubernetes.io/edge
          operator: DoesNotExist
```
