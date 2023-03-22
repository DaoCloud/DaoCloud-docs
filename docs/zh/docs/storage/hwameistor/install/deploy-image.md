---
hide:
  - toc
---

# 通过镜像安装

当通过在线方式部署是，可通过镜像方式部署 Hwameistor。

## 前提条件

- 待使用节点上已准备空闲 HDD、SSD 磁盘
- 已完成[准备工作](prereq.md)中事项
- 如需要使用高可用数据卷，请提前完成[DRDB 安装](drbdinstall.md)
- 如部署环境为生产环境，请提前阅读[生产环境资源要求](proresource.md)
- 如果您的 Kubernetes 发行版使用不同的 `kubelet` 目录，请提前确认 `kubeletRootDir`。详细信息参考： [自定义 Kubelet 根目录](customized-kubelet.md)

## 操作步骤

!!! tip

    默认的镜像仓库是 `quay.io` 和 `ghcr.io`。
    
    如果无法访问，可尝试使用 DaoCloud 提供的镜像源：`quay.m.daocloud.io` 和 `ghcr.m.daocloud.io`。

要切换镜像仓库的镜像，请使用 `--set` 更改这两个参数值：`k8sImageRegistry` 和 `hwameistorImageRegistry`。

```console
helm install hwameistor ./hwameistor \
    -n hwameistor --create-namespace \
    --set k8sImageRegistry=k8s-gcr.m.daocloud.io \
    --set hwameistorImageRegistry=ghcr.m.daocloud.io
```

安装完成！要验证安装效果，请参见下一章[安装后检查](./post-check.md)。
