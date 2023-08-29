# vmstorge 磁盘扩容

本文描述了 vmstorge 磁盘扩容的方法，
vmstorge 磁盘规范请参考 [vmstorage 磁盘容量规划](../res-plan/vms-res-plan.md)。

## 操作步骤

### 开启存储池扩容

1. 以全局服务集群管理员权限登录 DCE 5.0 平台，进入 `kpanda-global-cluster` 集群详情。
1. 选择左侧导航 `容器存储` -> `数据卷声明(PVC)`，找到 vmstorage 绑定的数据卷声明。

    ![找到vmstorage](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk01.png)

1. 点击某个 vmstorage PVC，进入 vmstorage 的数据卷声明详情，确认该 PVC 绑定的存储池。

    ![修改磁盘](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk02.png)

1. 选择左侧导航 `容器存储` -> `存储池(SC)`，找到 `local-path`，点击目标右侧的 `⋮`，在弹出菜单中选择`编辑`。

    ![编辑存储池](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk03.png)

1. 开启`扩容`后点击`确定`。

    ![开启扩容](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk04.png)

### 更改 vmstorage 的磁盘容量

1. 以全局服务集群管理员权限登录 DCE 5.0 平台，进入 `kpanda-global-cluster` 集群详情。
1. 选择左侧导航 `自定义资源`，找到 `vmcluster` 的自定义资源。

    ![vmcluster](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk05.png)

1. 点击该 vmcluster 自定义资源进入详情页，切换到 `insight-system` 命名空间下，从 `insight-victoria-metrics-k8s-stack` 右侧菜单选择`编辑 YAML`。

    ![编辑 YAML](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk06.png)

1. 根据图例修改后点击`确定`。

    ![修改 YAML](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk07.png)

1. 再次选择左侧导航 `容器存储` -> `数据卷声明(PVC)`，找到 vmstorage 绑定的数据卷声明确认修改已生效。在某个 PVC 详情页，点击关联存储源 (PV)。

    ![关联存储源](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk08.png)

1. 打开数据卷详情页，点击右上角`更新`按钮。

    ![更新](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk09.png)

1. 修改`容量`后点击`确定`，稍等片刻等到扩容成功。

    ![修改容量](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk10.png)

### 克隆存储卷

若存储卷扩容失败，可参考以下方法克隆存储卷。

1. 以全局服务集群管理员权限登录 DCE 5.0 平台，进入 `kpanda-global-cluster` 集群详情。
1. 选择左侧导航 `工作负载` -> `有状态负载`，找到 `vmstorage` 的有状态负载，点击目标右侧的 `⋮`，在弹出菜单中选择`状态` -> `停止`-> `确定`。

    ![状态停止](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk11.png)

1. 在命令行中登录 `kpanda-global-cluster` 集群的 `master` 节点后，执行以下命令复制 vmstorage 容器中的 vm-data 目录将指标信息存储在本地：

    ```bash
    kubectl cp -n insight-system vmstorage-insight-victoria-metrics-k8s-stack-1:vm-data ./vm-data
    ```

1. 登录 DCE 5.0 平台进入 `kpanda-global-cluster` 集群详情，选择左侧导航 `容器存储` -> `数据卷(PV)`，点击右上角的`克隆`，并修改数据卷的容量。

    ![克隆](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk12.png)

    ![修改容量](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk15.png)

1. 删除之前 vmstorage 的数据卷。

    ![删除数据卷](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk13.png)

1. 稍等片刻，待存储卷声明跟克隆的数据卷绑定后，执行以下命令将第 3 步中导出的数据导入到对应的容器中，然后开启之前暂停的 `vmstorage`。

    ```bash
    kubectl cp -n insight-system ./vm-data vmstorage-insight-victoria-metrics-k8s-stack-1:vm-data
    ```
