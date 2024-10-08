---
hide:
  - toc
---

# 容器管理审计项汇总

| 事件名称 | 资源类型 |
| ------- | ------ |
| 创建集群：Create-Cluster | Cluster |
| 卸载集群：Delete-Cluster | Cluster |
| 接入集群：Integrate-Cluster | Cluster |
| 解除接入的集群：Remove-Cluster | Cluster |
| 集群升级：Upgrade-Cluster | Cluster |
| 集群接入节点：Integrate-Node | Node |
| 集群节点移除：Remove-Node | Node |
| 集群节点 GPU 模式切换：Update-NodeGPUMode  | NodeGPUMode |
| helm仓库创建：Create-HelmRepo | HelmRepo |
| helm应用部署：Create-HelmApp | HelmApp |
| helm应用删除：Delete-HelmApp | HelmApp |
| 创建无状态负载：Create-Deployment | Deployment |
| 删除无状态负载：Delete-Deployment | Deployment |
| 创建守护进程：Create-DaemonSet | DaemonSet |
| 删除守护进程：Delete-DaemonSet | DaemonSet |
| 创建有状态负载：Create-StatefulSet | StatefulSet |
| 删除有状态负载：Delete-StatefulSet | StatefulSet |
| 创建任务：Create-Job | Job |
| 删除任务：Delete-Job | Job |
| 创建定时任务：Create-CronJob | CronJob |
| 删除定时任务：Delete-CronJob | CronJob |
| 删除容器组：Delete-Pod | Pod |
| 创建服务：Create-Service | Service |
| 删除服务：Delete-Service | Service |
| 创建路由：Create-Ingress | Ingress |
| 删除路由：Delete-Ingress | Ingress |
| 创建存储池：Create-StorageClass | StorageClass  |
| 删除存储池：Delete-StorageClass | StorageClass  |
| 创建数据卷：Create-PersistentVolume | PersistentVolume |
| 删除数据卷：Delete-PersistentVolume | PersistentVolume |
| 创建数据卷声明：Create-PersistentVolumeClaim | PersistentVolumeClaim |
| 删除数据卷声明：Delete-PersistentVolumeClaim | PersistentVolumeClaim |
| 删除副本集：Delete-ReplicaSet | ReplicaSet |
| ns绑定工作空间：BindResourceTo-Workspace | Workspace |
| ns解绑工作空间 ：UnBindResource-Workspace | Workspace |
| 集群绑定工作空间：BindResourceTo-Workspace | Workspace |
| 集群解绑工作空间：UnBindResource-Workspace | Workspace |
| 打开控制台：Create-CloudShell | CloudShell |
| 关闭控制台：Delete-CloudShell | CloudShell |
