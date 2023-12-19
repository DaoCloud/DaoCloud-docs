# 数据卷声明(PVC)

持久卷声明（PersistentVolumeClaim，PVC）表达的是用户对存储的请求。PVC 消耗 PV 资源，申领使用特定大小、特定访问模式的数据卷，例如要求 PV 卷以 ReadWriteOnce、ReadOnlyMany 或 ReadWriteMany 等模式来挂载。

## 创建数据卷声明

目前支持通过 YAML 和表单两种方式创建数据卷声明，这两种方式各有优劣，可以满足不同用户的使用需求。

- 通过 YAML 创建步骤更少、更高效，但门槛要求较高，需要熟悉数据卷声明的 YAML 文件配置。

- 通过表单创建更直观更简单，根据提示填写对应的值即可，但步骤更加繁琐。

### YAML 创建

1. 在集群列表中点击目标集群的名称，然后在左侧导航栏点击 __容器存储__ -> __数据卷声明 (PVC)__ -> __YAML 创建__ 。

    ![路径](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc01.png)

2. 在弹框中输入或粘贴事先准备好的 YAML 文件，然后在弹框底部点击 __确定__ 。

    > 支持从本地导入 YAML 文件或将填写好的文件下载保存到本地。

    ![yaml](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc02.png)

### 表单创建

1. 在集群列表中点击目标集群的名称，然后在左侧导航栏点击 __容器存储__ -> __数据卷声明 (PVC)__ -> __创建数据卷声明 (PVC)__ 。

    ![路径](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc03.png)

2. 填写基本信息。

    - 数据卷声明的名称、命名空间、创建方式、数据卷、容量、访问模式在创建之后不可更改。
    - 创建方式：在已有的存储池或者数据卷中动态创建新的数据卷声明，或者基于数据卷声明的快照创建新的数据卷声明。

        > 基于快照创建时无法修改数据卷声明的容量，可以在创建完成后再进行修改。

    - 选择创建方式之后，在下拉列表中选择想要使用的存储池/数据卷/快照。
    - 访问模式：

      - ReadWriteOnce，数据卷声明可以被一个节点以读写方式挂载。
      - ReadWriteMany，数据卷声明可以被多个节点以读写方式挂载。
      - ReadOnlyMany，数据卷声明可以被多个节点以只读方式挂载。
      - ReadWriteOncePod，数据卷声明可以被单个 Pod 以读写方式挂载。

        ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc04.png)

## 查看数据卷声明

在集群列表中点击目标集群的名称，然后在左侧导航栏点击 __容器存储__ -> __数据卷声明(PVC)__ 。

- 该页面可以查看当前集群中的所有数据卷声明，以及各个数据卷声明的状态、容量、命名空间等信息。

- 支持按照数据卷声明的名称、状态、命名空间、创建时间进行顺序或逆序排序。

    ![详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc06.png)

- 点击数据卷声明的名称，可以查看该数据卷声明的基本配置、存储池信息、标签、注解等信息。

    ![详情](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc05.png)

## 扩容数据卷声明

1. 在左侧导航栏点击 __容器存储__ -> __数据卷声明(PVC)__ ，找到想要调整容量的数据卷声明。

    ![扩容](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc14.png)

2. 点击数据卷声明的名称，然后在页面右上角点击操作按钮选择 __扩容__ 。

    ![扩容](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc15.png)

3. 输入目标容量，然后点击 __确定__ 。

    ![克隆](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc16.png)

## 克隆数据卷声明

通过克隆数据卷声明，可以基于被克隆数据卷声明的配置，重新创建一个新的数据卷声明。

1. 进入克隆页面

    - 在数据卷声明列表页面，找到需要克隆的数据卷声明，在右侧的操作栏下选择 __克隆__ 。

        > 也可以点击数据卷声明的名称，在详情页面的右上角点击操作按钮选择 __克隆__ 。

        ![克隆](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc11.png)

2. 直接使用原配置，或者按需进行修改，然后在页面底部点击 __确定__ 。

    ![克隆](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc12.png)

## 更新数据卷声明

有两种途径可以更新数据卷声明。支持通过表单或 YAML 文件更新数据卷声明。

!!! note

    仅支持更新数据卷声明的别名、标签和注解。

- 在数据卷列表页面，找到需要更新的数据卷声明，在右侧的操作栏下选择 __更新__ 即可通过表单更新，选择 __编辑 YAML__ 即可通过 YAML 更新。

    ![更新](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc07.png)

- 点击数据卷声明的名称，进入数据卷声明的详情页面后，在页面右上角选择 __更新__ 即可通过表单更新，选择 __编辑 YAML__ 即可通过 YAML 更新。

    ![更新](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc08.png)

## 删除数据卷声明

在数据卷声明列表页面，找到需要删除的数据，在右侧的操作栏下选择 __删除__ 。

> 也可以点击数据卷声明的名称，在详情页面的右上角点击操作按钮选择 __删除__ 。

![删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc09.png)

## 常见问题

1. 如果列表中没有可选的存储池或数据卷，可以[创建存储池](sc.md)或[创建数据卷](pv.md)。

2. 如果列表中没有可选的快照，可以进入数据卷声明的详情页，在右上角制作快照。

    ![制作快照](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc17.png)

3. 如果数据卷声明所使用的存储池 (SC) 没有启用快照，则无法制作快照，页面不会显示“制作快照”选项。
4. 如果数据卷声明所使用的存储池 (SC) 没有开启扩容功能，则该数据卷不支持扩容，页面不会显示扩容选项。

    ![开启快照](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/pvc18.png)
