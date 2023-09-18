---
hide:
  - toc
---

# 容器管理权限说明

容器管理模块使用以下角色：

- Admin / Kpanda Owner
- [Cluster Admin](../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin)
- [NS Admin](../../kpanda/user-guide/permissions/permission-brief.md#ns-admin)
- [NS Editor](../../kpanda/user-guide/permissions/permission-brief.md#ns-edit)
- [NS Viewer](../../kpanda/user-guide/permissions/permission-brief.md#ns-view)

!!! note

    - 有关权限的更多信息，请参阅[容器管理权限体系说明](../../kpanda/user-guide/permissions/permission-brief.md)。
    - 有关角色的创建、管理和删除，请参阅[角色和权限管理](../user-guide/access-control/role.md)。
    - `Cluster Admin`, `NS Admin`, `NS Editor`, `NS Viewer` 的权限仅在当前的集群或命名空间内生效。

各角色所具备的权限如下：

<!--
有权限使用`&check;`，无权限使用`&cross;`
-->

| 一级功能 | 二级功能               | 权限点                   | Cluster Admin | Ns Admin | Ns Editor       | NS Viewer      |
| -------- | ---------------------- | ------------------------ | -------------------------------- | --------------------------- | --------------------------- | --------------------------- |
| 集群     | 集群列表               | 查看集群列表             | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 接入集群                 | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建集群                 | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          | 集群操作               | 进入控制台               | &check;                               | &check;（仅列表内可以进入）       | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 编辑基础配置             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 下载 kubeconfig          | &check;                               | &check;（下载ns权限的kubeconfig） | &check;（下载ns权限的kubeconfig） | &check;（下载ns权限的kubeconfig） |
|          |                        | 解除接入                 | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看日志                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 重试                     | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 卸载集群                 | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          | 集群概览               | 查看集群概览             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 节点管理               | 接入节点                 | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看节点列表             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看节点详情             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看yaml                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 暂停调度                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 修改标签                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 修改注解                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 修改污点                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 移除节点                 | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          | 无状态负载             | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 镜像创建                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 选择ns绑定的ws内的实例 | 选择镜像                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | IP 池查看                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 网卡编辑                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 负载伸缩                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-暂停升级            | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-停止                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-重启                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 有状态负载             | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 镜像创建                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 选择ns绑定的ws内的实例 | 选择镜像                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 负载伸缩                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-停止                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-重启                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 守护进程               | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 镜像创建                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 选择ns绑定的ws内的实例 | 选择镜像                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-重启                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 任务                   | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 镜像创建                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 实例列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          | 选择ns绑定的ws内的实例 | 选择镜像                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 重启                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看事件                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 定时任务               | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 镜像创建                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 选择ns绑定的ws内的实例 | 选择镜像                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 停止                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看任务列表             | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看事件                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 容器组                 | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 上传文件                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 下载文件                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看容器列表             | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看事件                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | ReplicaSet             | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | Helm 应用              | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | Helm 模板              | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看详情                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 安装模板                 | &check;                               | &check;（ns级别的可以）     | &cross;                           | &cross;                           |
|          |                        | 下载模板                 | &check;                               | &check;                          | &check;（和查看接口一致）         | &check;                          |
|          | Helm 仓库              | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 创建仓库                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 更新仓库                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 克隆仓库                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 刷新仓库                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 修改标签                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 修改注解                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 服务                   | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 创建                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看事件                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 路由                   | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 创建                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看事件                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 网络策略               | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 创建                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 网络配置               | 配置网络                 | &check;                               | &check;                          | &check;                          | &cross;                      |
|          | 自定义资源             | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看/管理详情            | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | yaml 创建                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | PVC                    | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 创建                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 选择sc                   | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 克隆                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | PV                     | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看/管理详情            | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | yaml 创建                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 更新                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 克隆                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 修改标签                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 修改注解                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | SC                     | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | yaml 创建                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看 yaml                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 更新                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 授权命名空间             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 解除授权                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 配置项                 | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 创建                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 导出配置项               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 密钥                   | 查看列表                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | yaml 创建                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 创建                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 导出密钥                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 命名空间               | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）                 |
|          |                        | yaml 创建                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 修改标签                 | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 解绑工作空间             | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 绑定工作空间             | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 配额管理                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 集群操作               | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看 yaml                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看日志                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | helm 操作              | 设置保留条数             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 查看日志                 | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          | 集群升级               | 查看详情                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 升级                     | &cross;                                | &cross;                           | &cross;                           | &cross;                           |
|          | 集群设置               | addon 插件配置           | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 高级配置                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
| 命名空间 |                        | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 创建                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &check;                          | &cross;                    |
|          |                        | 修改标签                 | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 绑定工作空间             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 配额管理                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
| 工作负载 | 无状态负载             | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 负载伸缩                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-暂停升级            | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-停止                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-重启                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 回退                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 修改标签注解             | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 有状态负载             | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 负载伸缩                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-停止                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-重启                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 守护进程               | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 编辑 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 更新                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 状态-重启                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 任务                   | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 重启                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看事件                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 定时任务               | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 查看事件                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
|          | 容器组                 | 查看列表                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看/管理详情            | &check;                               | &check;                          | &check;                          | &check;（仅查看）               |
|          |                        | 进入控制台               | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看监控                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看日志                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看 yaml                | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 上传文件                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 下载文件                 | &check;                               | &check;                          | &check;                          | &cross;                           |
|          |                        | 查看容器列表             | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 查看事件                 | &check;                               | &check;                          | &check;                          | &check;                          |
|          |                        | 删除                     | &check;                               | &check;                          | &check;                          | &cross;                           |
| 备份恢复 | 应用备份               | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看/管理详情            | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建备份计划             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看 yaml                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 更新计划                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 暂停                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 立即执行                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 恢复备份               | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看/管理详情            | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 恢复备份                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 备份点                 | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 对象存储               | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | ETCD备份               | 查看备份策略列表         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建备份策略             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看日志                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看 yaml                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 更新备份策略             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 停止/启动                | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 立即执行                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看/管理详情            | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除备份记录             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看备份点列表           | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 从备份恢复               | &check;                               | &cross;                           | &cross;                           | &cross;                           |
| 集群巡检 | 集群巡检               | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看/管理详情            | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 集群巡检                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 设置                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
| 权限管理 | 集群权限               | 查看列表                 | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 授权用户为 cluster admin | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 命名空间权限           | 查看列表                 | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 授权用户为 ns admin      | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 授权用户为 ns edit       | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 授权用户为 ns view       | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 编辑权限                 | &check;                               | &check;                          | &cross;                           | &cross;                           |
|          |                        | 删除                     | &check;                               | &check;                          | &cross;                           | &cross;                           |
| 安全管理 | 合规性扫描             | 查看扫描报告列表         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看扫描报告详情         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 下载扫描报告             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除扫描报告             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看扫描策略列表         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建扫描策略             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除扫描策略             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看扫描配置列表         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看扫描配置详情         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除扫描配置             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 权限扫描               | 查看扫描报告列表         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看扫描报告详情         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除扫描报告             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看扫描策略列表         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建扫描策略             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除扫描策略             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          | 漏洞扫描               | 查看扫描报告列表         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看扫描报告详情         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除扫描报告             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 查看扫描策略列表         | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 创建扫描策略             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
|          |                        | 删除扫描策略             | &check;                               | &cross;                           | &cross;                           | &cross;                           |
