# 虚拟机自动漂移

本文将介绍当集群内某个节点因为断电或网络故障，导致该节点上的虚拟机无法访问时，
如何将正在运行的虚拟机无缝迁移到其他的节点上，同时保证业务的连续性和数据的安全性。

与自动漂移相比，实时迁移需要您在界面中主动操作，而不是系统自动触发迁移过程。

## 前提条件

实现自动漂移之前，需要满足以下前提条件：

- 虚拟机未进行磁盘落盘操作，或使用 rook-ceph 作为存储系统
- 节点失联时间超过五分钟
- 确保集群内至少有两个节点可供使用
- 虚拟机的 launcher pod 已被删除

## 操作步骤

1. 检查虚拟机 launcher pod 状态：

    ```sh
    kubectl get pod
    ```

    查看 launcher pod 是否处于 Terminating 状态。

2. 强制删除 launcher pod：

    如果 launcher pod 状态为 Terminating，可以执行以下命令进行强制删除：

    ```sh
    kubectl delete <launcher pod> --force
    ```

    替换 `<launcher pod>` 为你的 launcher pod 名称。

3. 等待重新创建并检查状态：

    删除后，系统将自动重新创建 launcher pod。
    等待其状态变为 running，然后刷新虚拟机列表，观察虚拟机是否成功迁移到新节点。

## 注意事项

如果使用 rook-ceph 作为存储，需要配置为 ReadWriteOnce 模式：

1. 强制删除 pod 后，需要等待大约六分钟以让 launcher pod 启动，或者可以通过以下命令立即启动 pod：

    ```sh
    kubectl get pv | grep <vm name>
    kubectl get VolumeAttachment | grep <pv name>
    ```

    替换 `<vm name>` 和 `<pv name>` 为你的虚拟机名称和持久卷名称。

2. 然后执行以下命令删除对应的 VolumeAttachment：

    ```sh
    kubectl delete VolumeAttachment <vm>
    ```

    替换 <vm> 为你的虚拟机名称。
