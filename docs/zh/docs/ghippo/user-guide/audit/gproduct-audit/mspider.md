---
hide:
  - toc
---

# 服务网格审计项汇总

| 事件名称 | 资源类型 | 备注 |
| --- | --- | --- |
| 创建网格：create-MeshInstance | MeshInstance | |
| 删除网格：delete-MeshInstance | MeshInstance | |
| 接入集群：Add-Cluster | cluster | |
| 移除集群：Remove-Cluster | cluster | |
| 命名空间边车注入启用：InjectSidecarTo-Namespace | Namespace | |
| 命名空间边车注入禁用：ForbiddenInjectSidecarTo-Namespace | Namespace | |
| 工作负载边车注入启用：InjectSidecarTo-Workload | workload | |
| 工作负载边车注入禁用：ForbiddenInjectSidecarTo-Workload | workload | |
| 创建网格网关：create-MeshGateway | MeshGateway | |
| 删除网格网关：delete-MeshGateway | MeshGateway | |
| 启用多云：Enable-Multicloud | Multicloud | |
| 关闭多云：Close-Multicloud | Multicloud | |
| 启用互联：EnableInterconnection | MulticloudGroup | |
| 移出互联：DisableInterconnection | MulticloudGroup | |
