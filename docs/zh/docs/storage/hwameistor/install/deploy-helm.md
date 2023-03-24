---
hide:
  - toc
---

# 通过 Helm Chart 安装

HwameiStor 的任何组件都可以通过 Helm Chart 进行安装。

## 前提条件

- 待使用节点上已准备空闲 HDD、SSD 磁盘
- 已完成[准备工作](prereq.md)中事项
- 如需要使用高可用数据卷，请提前完成[DRDB 安装](drbdinstall.md)
- 如部署环境为生产环境，请提前阅读[生产环境资源要求](proresource.md)
- 如果您的 Kubernetes 发行版使用不同的 `kubelet` 目录，请提前确认 `kubeletRootDir`。详细信息参考： [自定义 Kubelet 根目录](customized-kubelet.md)

## 操作步骤

1. 准备 Helm 工具，安装 [Helm](https://helm.sh/) 命令行工具，请参阅 [Helm 文档](https://helm.sh/docs/)。

2. 下载 `hwameistor` Repo，下载并解压 Repo 文件到本地

    ```console
    helm repo add hwameistor http://hwameistor.io/hwameistor
    helm repo update hwameistor
    helm pull hwameistor/hwameistor --untar
    ```
    
3. 安装 HwameiStor，命名如下：

    ```console
    helm install hwameistor ./hwameistor \
        -n hwameistor --create-namespace
    ```

!!! success

    安装完成！要验证安装效果，请参见下一章[安装后检查](./post-check.md)。

如需要`自定义 Kubelet 根目录` 请参考： [自定义 Kubelet 根目录](customized-kubelet.md)

安装完成！要验证安装效果，请参见下一章[安装后检查](./post-check.md)。

