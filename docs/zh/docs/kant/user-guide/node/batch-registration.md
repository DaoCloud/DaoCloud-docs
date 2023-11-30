# 批量注册边缘节点

相同类型的边缘节点能够设定相同的边缘节点配置，通过创建批量任务，获取边缘节点配置文件和安装程序。
批量注册节点与边缘节点满足一对多的关系，提高管理效率，也节约了运维成本。

下文说明批量注册边缘节点的步骤。

## 创建批量任务

1. 边缘节点列表 页面，点击`批量管理`按钮，进入`批量管理`页，选择`批量注册`页签，点击右上角`创建批量任务`按钮。

    ![批量管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/node-batch-01.png)

2. 填写注册信息。

    - 任务名称：批量任务名称不能为空，长度限制为 63 位。
    - 名称前缀：通过批量任务接入的节点，节点名称由“前缀+随机码组成”。
    - 驱动方式：控制组（CGroup）的驱动，用于对 Pod 和容器进行资源管理和资源配置，如CPU和内存资源的请求和限制。
    - CRI 服务地址：CRI Client 和 CRI Server 在本地进行通信的 socket 文件或者 TCP 地址，
      例如 `unix:///run/containerd/containerd.sock`
    - KubeEdge 镜像仓库：KubeEdge 云端组件镜像仓库，自动填入边缘单元中设置的 KubeEdge 镜像仓库地址，用户可修改。
    - 描述：批量任务描述信息。
    - 标签：批量任务标签信息。

    ![创建批量任务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kant/images/node-batch-02.png)

3. 完成注册信息填写后，点击 创建 按钮，完成节点批量任务创建。

## 后续操作

完成注册后，将自动跳转到`安装指南`界面，您需要对边缘节点执行纳管操作，具体请参见[纳管边缘节点](./managed-node.md)。
