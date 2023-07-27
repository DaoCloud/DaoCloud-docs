# 卸载 Hwameistor

本章节介绍了两种卸载 HwameiStor 系统的方式。

!!! danger

    请务必先备份好所有数据，再卸载 HwameiStor。

## 方式一：卸载并保留已有数据

如果想要卸载 HwameiStor 的系统组件，但是保留已经创建的数据卷并服务于数据应用，采用下列方式：

```console
$ kubectl get cluster.hwameistor.io
NAME             AGE
cluster-sample   21m

$ kubectl delete clusters.hwameistor.io  hwameistor-cluster
```

最终，所有的 HwameiStor 系统组件（Pods）将被删除。用下列命令检查，结果为空。

```sh
kubectl -n hwameistor get pod
```

## 方式二：完全卸载

如果想要卸载 HwameiStor 所有组件，并删除所有数据卷及数据，采用下列方式，请谨慎操作。

1. 清理有状态数据应用

    1. 删除应用

    2. 删除数据卷 PVC

        相关的 PV、LV、LVR、LVG 都将被删除。

2. 清理 HwameiStor 系统组件

    1. 删除 HwameiStor 组件

        ```shell
        kubectl delete clusters.hwameistor.io  hwameistor-cluster
        ```

    2. 删除 HwameiStor 系统空间

        ```shell
        kubectl delete ns hwameistor
        ```

    3. 删除 CRD、Hook 以及 RBAC

        ```shell
        kubectl get crd,mutatingwebhookconfiguration,clusterrolebinding,clusterrole -o name \
          | grep hwameistor \
          | xargs -t kubectl delete
        ```

    4. 删除 StorageClass

        ```shell
        kubectl get sc -o name \
          | grep hwameistor-storage-lvm- \
          | xargs -t kubectl delete
        ```

    5. 删除 hwameistor Operator

        ```shell
        helm uninstall hwameistor-operator -n hwameistor
        ```

最后，你仍然需要清理每个节点上的 LVM 配置，并采用额外的系统工具（例如 wipefs）清除磁盘上的所有数据。
