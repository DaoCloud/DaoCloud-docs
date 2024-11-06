---
hide:
  - toc
---

# 安装 DRBD（可选）

如需要使用高可用数据卷，请在部署 HwameiStor 时开启 DRBD。可采用以下几种安装方式。

## 安装 HwameiStor 时同步安装 DRBD

HwameiStor 安装时，可直接启用 DRBD 组件，详情可查看 [HwameiStor 安装](deploy-operator.md)。

## 通过 UI 界面

1. 进入 __容器管理__ -> __Helm 模板__，选择 __drbd-adapter__。

2. 点击 __drbd-adapter__ ，点击 __安装__ ，进入配置页面。

    ![drbd02](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/drbd02.jpg)

    - __命名空间__ ：建议同 HwameiStor 部署在相同的命名空间中，此示例创建的命名空间为 HwameiStor。
    - __版本__ ：默认选择最新版本。
    - __失败删除__：默认关闭。开启后，将默认同步开启安装等待，将在安装失败时删除安装。
    - __就绪等待__ ：默认关闭。 启用后，将等待应用下所有关联资源处于就绪状态才标记应用安装成功。
    - __详细日志__ ：默认关闭。开启安装过程日志的详细输出。

3. 点击 __确定__ 完成创建。

## 通过 Helm 安装

部署以下 `DaemonSet`。它将在每个 kubernetes 工作节点上启动一个 Pod 来安装 DRBD 模块和工具：

```bash
helm repo add drbd-adapter https://hwameistor.io/drbd-adapter/
helm repo update drbd-adapter
helm pull drbd-adapter/drbd-adapter --untar
helm install drbd-adapter ./drbd-adapter -n hwameistor --create-namespace
```

!!! tip

    国内用户可以使用镜像仓库 `daocloud.io/daocloud` 加速：

    ```bash
    helm install drbd-adapter ./drbd-adapter \
        -n hwameistor --create-namespace \
        --set imagePullPolicy=Always \
        --set registry=daocloud.io/daocloud
    ```
