# vmstorge 磁盘扩容

本文描述了 vmstorge 磁盘扩容的方法，
vmstorge 磁盘规范请参考 [vmstorage 磁盘容量规划](../res-plan/vms-res-plan.md)。

## 操作步骤

### 开启存储池扩容

1. 以全局服务集群管理员权限登录 DCE 5.0 平台，点击 __容器管理__ -> __集群列表__ ，点击 __kpanda-global-cluster__ 集群。

1. 选择左侧导航 __容器存储__ -> __数据卷声明(PVC)__ ，找到 vmstorage 绑定的数据卷声明。

    ![找到vmstorage](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk01.png)

1. 点击某个 vmstorage PVC，进入 vmstorage 的数据卷声明详情，确认该 PVC 绑定的存储池。

    ![修改磁盘](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk02.png)

1. 选择左侧导航 __容器存储__ -> __存储池(SC)__ ，找到 __local-path__ ，点击目标右侧的 __⋮__ ，在弹出菜单中选择 __编辑__ 。

    ![编辑存储池](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk03.png)

1. 开启 __扩容__ 后点击 __确定__ 。

    ![开启扩容](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk04.png)

### 更改 vmstorage 的磁盘容量

1. 以全局服务集群管理员权限登录 DCE 5.0 平台，进入 __kpanda-global-cluster__ 集群详情。

1. 选择左侧导航 __自定义资源__ ，找到 __vmcluster__ 的自定义资源。

    ![vmcluster](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk05.png)

1. 点击该 vmcluster 自定义资源进入详情页，切换到 __insight-system__ 命名空间下，从 __insight-victoria-metrics-k8s-stack__ 右侧菜单选择 __编辑 YAML__ 。

    ![编辑 YAML](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk06.png)

1. 根据图例修改后点击 __确定__ 。

    ![修改 YAML](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk07.png)

1. 再次选择左侧导航 __容器存储__ -> __数据卷声明(PVC)__ ，找到 vmstorage 绑定的数据卷声明确认修改已生效。在某个 PVC 详情页，点击关联存储源 (PV)。

    ![关联存储源](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk08.png)

1. 打开数据卷详情页，点击右上角 __更新__ 按钮。

    ![更新](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk09.png)

1. 修改 __容量__ 后点击 __确定__ ，稍等片刻等到扩容成功。

    ![修改容量](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk10.png)

### 克隆存储卷

若存储卷扩容失败，可参考以下方法克隆存储卷。

1. 以全局服务集群管理员权限登录 DCE 5.0 平台，进入 __kpanda-global-cluster__ 集群详情。

1. 选择左侧导航 __工作负载__ -> __有状态负载__ ，找到 __vmstorage__ 的有状态负载，点击目标右侧的 __⋮__ ，在弹出菜单中选择 __状态__ -> __停止__ -> __确定__ 。

    ![状态停止](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk11.png)

1. 在命令行中登录 __kpanda-global-cluster__ 集群的 __master__ 节点后，执行以下命令复制 vmstorage 容器中的 vm-data 目录将指标信息存储在本地：

    ```bash
    kubectl cp -n insight-system vmstorage-insight-victoria-metrics-k8s-stack-1:vm-data ./vm-data
    ```

1. 登录 DCE 5.0 平台进入 __kpanda-global-cluster__ 集群详情，选择左侧导航 __容器存储__ -> __数据卷(PV)__ ，点击右上角的 __克隆__ ，并修改数据卷的容量。

    ![克隆](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk15.png)

    ![修改容量](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk12.png)

1. 删除之前 vmstorage 的数据卷。

    ![删除数据卷](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/vmdisk13.png)

1. 稍等片刻，待存储卷声明跟克隆的数据卷绑定后，执行以下命令将第 3 步中导出的数据导入到对应的容器中，然后开启之前暂停的 __vmstorage__ 。

    ```bash
    kubectl cp -n insight-system ./vm-data vmstorage-insight-victoria-metrics-k8s-stack-1:vm-data
    ```
