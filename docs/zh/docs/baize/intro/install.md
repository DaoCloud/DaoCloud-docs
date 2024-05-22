# 算力集群初始化

默认情况下，DCE 5.0 商业版安装时可以同步安装智算能力模块，请联系交付支持团队获取商业版安装包。

## 安装智能算力

确保全局管理集群内已经安装了智算能力组件，确认方式为通过 DCE 5.0 管理界面查看是否有智算能力模块。

!!! info

    一级导航栏有 `智能算力` 入口。

如何不存在，可以通过以下方式安装，注意需要在 `kpanda-global-cluster` 全局管理集群内安装：

```bash
# baize 是智算能力组件的开发代号
helm repo add baize https://release.daocloud.io/chartrepo/baize
helm repo update
export VERSION=v0.1.1
helm upgrade --install baize baize/baize \
    --create-namespace \
    -n baize-system \
    --set global.imageRegistry=release.daocloud.io \
    --version=${VERSION}
```

如果是在已有的 `DCE` 环境中安装，可以添加 `helm` 源到容器管理内，采用界面化安装方式亦可。

## 工作集群初始化

在每个有算力资源的工作集群内，需要部署对应的算力基础组件，主要组件包含如下：

- `gpu-operator` 初始化集群中的 GPU 资源，**这部分会因 GPU 资源类型安装方式不同**，
  详情参考 [GPU 管理](../../kpanda/user-guide/gpu/index.md)
- `insight-agent` 可观测组件，用于采集集群的基础设施信息，包含日志、指标、事件
- `baize-agent` 包含了智能算力的核心组件，调度、监控、Pytorch、Tensorflow 等算力组件
- `nfs` 存储服务，用于数据集的预热

!!! danger

    **以上组件必须安装，否则会导致功能使用不正常。**

以上工作完成后，已经可以在智能算力内，进行任务训练和模型开发。

### 预热组件介绍

智能算力模块提供的数据管理中，数据集的预热能力依赖存储服务，推荐使用 NFS 服务：

- 部署 NFS Server
    - 如果已存在 NFS 可以跳过此步骤
    - 如果不存在，可以参考最佳实践中的 [NFS 服务部署](../../baize/best-practice/deploy-nfs-in-worker.md)
- 部署 `nfs-driver-csi`
- 部署 `StorageClass`

## 结语

以上完成后，就可以在工作集群内正常体验智能算力的全部功能了，祝你使用愉快！
