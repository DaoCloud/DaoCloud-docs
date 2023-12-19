---
hide:
  - toc
---

# 卸载/解除接入集群

通过 DCE 5.0 [容器管理](../../intro/index.md)平台 **创建的集群** 支持 __卸载集群__ 或 __解除接入__ 操作，从其他环境直接 **接入的集群** 仅支持 __解除接入__ 操作。

!!! Info

    如果想彻底删除一个接入型的集群，需要前往创建该集群的原始平台操作。DCE 5.0 不支持删除接入型的集群。

在 DCE 5.0 平台中， __卸载集群__ 和 __解除接入__ 的区别在于：

- __卸载集群__ 操作会销毁该集群，并重置集群下所有节点的数据。所有数据都将被销毁，建议做好备份。后期需要时必须重新创建一个集群。
- __解除接入__ 操作会将当前集群从平台中移除，不会摧毁集群，也不会销毁数据。

## 卸载集群

!!! note

    - 当前操作用户应具备 [Admin](../../../ghippo/user-guide/access-control/role.md) 或 [Kpanda Owner](../../../ghippo/user-guide/access-control/global.md) 权限才能执行卸载或解除接入的操作。
    - 卸载集群之前，应该在 __集群设置__ -> __高级配置__ 中关闭 __集群删除保护__ ，否则不显示 __卸载集群__ 的选项。
    - __全局服务集群__ 不支持卸载或移除操作。

1. 在 __集群列表__ 页找到需要卸载集群，点击右侧的 __⋮__ 并在下拉列表中点击 __卸载集群__ 。

    ![点击删除按钮](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/delete001.png)

2. 输入集群名称进行确认，然后点击 __删除__ 。

    ![确认删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/delete002.png)

3. 返回 __集群列表__ 页可以看到该集群的状态已经变成 __删除中__ 。卸载集群可能需要一段时间，请您耐心等候。

    ![删除中状态](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/delete004.png)

## 解除接入集群

1. 在 __集群列表__ 页找到需要卸载集群，点击右侧的 __⋮__ 并在下拉列表中点击 __解除接入__ 。

    ![点击删除按钮](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/delete001.png)

2. 输入集群名称进行确认，然后点击 __删除__ 。

    ![确认删除](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/delete003.png)

## 清理解除接入集群配置数据

集群被移除后，集群中原有的管理平台数据不会被自动清除，如需将集群接入至新管理平台则需要手动执行如下操作：

1. 删除 kpanda-system、insight-system 命名空间

    ```
    kubectl delete ns kpanda-system insight-system
    ```

2. 如果为当前集群启用了服务网格能力，请参考[删除网格](../../../mspider/user-guide/service-mesh/delete.md)文档删除当前集群中的网格实例。

