---
hide:
  - toc
---

# 镜像仓库审计项汇总

| 事件名称 | 资源类型 | 备注 |
| --- | --- | --- |
| 镜像删除：Delete-Image | Image | |
| artifact删除：Delete-Artifacts | Artifacts | |
| 创建回收规则：Update-ReclaimRule | ReclaimRule | 创建和删除是同一个接口，因此均会被记录为 Update-ReclaimRule |
| 删除回收规则：Update-ReclaimRule | ReclaimRule |
| 手动运行回收规则：Manual-ReclaimRule | ReclaimRule | 
| 创建仓库集成：Create-IntegratedRegistryinWorkspace | IntegratedRegistryinWorkspace | |
| 删除仓库集成：Delete-IntegratedRegistryinWorkspace | IntegratedRegistryinWorkspace | |
| 更新仓库集成：Update-IntegratedRegistryinWorkspace | IntegratedRegistryinWorkspace | |
| 创建仓库集成：Create-IntegratedRegistrybyAdmin | IntegratedRegistrybyAdmin | |
| 删除仓库集成：Delete-IntegratedRegistrybyAdmin | IntegratedRegistrybyAdmin | |
| 更新仓库集成：Update-IntegratedRegistrybyAdmin | IntegratedRegistrybyAdmin | |
| 创建托管harbor：Create-Harbor | Harbor | |
| 删除托管Harbor：Delete-Harbor | Harbor | |
| 更新托管Harbor：Update-Harbor | Harbor | |