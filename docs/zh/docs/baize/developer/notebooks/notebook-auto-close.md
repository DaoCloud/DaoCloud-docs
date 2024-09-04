# Notebook 闲置超时自动关机

## 概述

在默认情况下，为优化资源利用，智能算力启用了 Notebook 闲置超时自动关机功能；
当 Notebook 长时间无操作时，系统会自动关机 Notebook，释放资源。

- 优点：通过这个方式，可以极大减少因为长时间无操作导致的资源浪费，提高资源利用效率。
- 缺点：如果 Notebook 未配置相关备份策略，可能导致数据丢失。

!!! note

    当前，此功能为集群级别配置，默认开启，默认超时时长为 30 分钟。

## 配置变更

目前配置修改方式为手动修改，后续会提供更加便捷的配置方式。

修改工作集群中 `baize-agent` 的部署参数，正确的修改方式为更新 Helm 应用，

### 界面化修改

在集群管理界面找到对应的工作集群，进入集群详情，选择 `Helm 应用`，找到在 `baize-system` 命名空间下的 `baize-agent`；

![baize-agent](../../images/notebook-idle.png)

点击 `更新`，按照如下配置修改：

![baize-agent](../../images/notebook-idle02.png)

确认参数修改成功后，保存即可。

### 命令行修改

使用 helm upgrade 命令，例如：

```bash
# 设定版本号
export VERSION=0.8.0

# 更新 Helm Chart 
helm upgrade --install baize-agent baize/baize-agent \
    --namespace baize-system \
    --create-namespace \
    --set global.imageRegistry=release.daocloud.io \
    --set notebook-controller.culling_enabled=true \    # 开启自动关机
    --set notebook-controller.cull_idle_time=120 \      # 设置超时时间为 120 分钟
    --set notebook-controller.idleness_check_period=1 \ # 设置检查间隔为 1 分钟
    --version=$VERSION
```

### 配置参数说明

- `notebook-controller.culling_enabled`：是否开启自动关机功能，默认为 `true`；
- `notebook-controller.cull_idle_time`：设置闲置超时时间，默认为 `30` 分钟；
- `notebook-controller.idleness_check_period`：设置检查间隔，默认为 `1` 分钟。

## 最佳实践指南

### 避免自动关机后丢失数据

可以升级到 `v0.8.0` 及之后版本，在 Notebook 配置中启用关机自动保存功能。
