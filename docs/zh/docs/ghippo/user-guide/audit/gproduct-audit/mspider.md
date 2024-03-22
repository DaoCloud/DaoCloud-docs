# 服务网格审计汇总

|  事件名称   | 资源类型    | 备注    |
| --- | --- | --- |
| 创建网格create-MeshInstance | MeshInstance |     |
| 删除网格delete-MeshInstance | MeshInstance |     |
| 接入集群Add-Cluster | cluster |     |
| 移除集群Remove-Cluster | cluster |     |
| 命名空间边车注入启用InjectSidecarTo-Namespace | Namespace |     |
| 命名空间边车注入禁用ForbiddenInjectSidecarTo-Namespace | Namespace |     |
| 工作负载边车注入启用InjectSidecarTo-Workload | workload |     |
| 工作负载边车注入禁用ForbiddenInjectSidecarTo-Workload | workload |     |
| 创建网格网关create-MeshGateway | MeshGateway |     |
| 删除网格网关delete-MeshGateway | MeshGateway |     |
| 启用多云：Enable-Multicloud | Multicloud |     |
| 关闭多云Close-Multicloud | Multicloud |     |
| 启用互联EnableInterconnection | MulticloudGroup |     |
| 移出互联DisableInterconnection | MulticloudGroup |     |