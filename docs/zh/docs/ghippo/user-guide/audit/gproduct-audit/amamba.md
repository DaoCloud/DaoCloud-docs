# 应用工作台审计汇总

| 事件名称    |  资源类型   |  备注   |
| --- | --- | --- |
| 创建原生应用：Create-Application | Application |     |
| 更新原生应用：Update-Application | Application | 编辑yaml、创建版本快照、回滚 |
| 删除原生应用：Delete-Application | Application |     |
| 创建 OAM 应用：Create-OAMApplication | OAMApplication |     |
| 更新 OAM 应用：Update-OAMApplication | OAMApplication | 编辑yaml |
| 添加 OAM 应用组件:Add-OAMApplicationComponent | OAMApplicationComponent | 添加组件 |
| 更新 OAM 组件运维特征:Update-OAMApplicationComponentTrait | OAMApplicationComponentTrait | 更新应用组件运维特征 |
| 删除 OAM 应用：Delete-OAMApplication | OAMApplication |     |
| 创建 HELM 应用：Create-HelmApplication | HelmApplication |     |
| 创建OLM 应用：Create-OLMApplication | OLMApplication |     |
| 更新OLM 应用：Update-OLMApplication | OLMApplication |     |
| 创建OLM 应用：Delete-OLMApplication | OLMApplication |     |
| 创建命名空间：Create-Namespace | Namespace |     |
| 更新命名空间配额：Update-NamespaceQuota | NamespaceQuota |     |
| 删除命名空间：Delete-Namespace | Namespace |     |
| 创建流水线：Create-Pipeline | Pipeline |     |
| 更新流水线：Update-Pipeline | Pipeline | 包含所有的更新操作(编辑jenkinsfile、编辑配置、编辑图形化、) |
| 运行流水线：Run-Pipeline | Pipeline | 立即运行c奥做 |
| 重新运行：ReRun-Pipeline | Pipeline | 重新执行操作 |
| 终止流水线：Abort-Pipeline | Pipeline | 终止操作+审批步骤的终止操作 |
| 审批流水线：Approval-Pipeline | Pipeline | 审批通过流水线 |
| 删除流水线：Delete-Pipeline | Pipeline |     |
| 创建流水线凭证：Create-PipelineCredential | PipelineCredential |     |
| 删除流水线凭证：Delete-PipelineCredential | PipelineCredential |     |
| 创建灰度发布任务：Create-GrayscaleTask | GrayscaleTask | 是否要区分是蓝绿还是金丝雀 |
| 更新灰度发布任务：Update-GrayscaleTask | GrayscaleTask | 更新发布任务、更新版本、编辑yaml、更新实例数 |
| 发布灰度发布任务任务：Upgrade-GrayscaleTask | GrayscaleTask |     |
| 终止灰度发布任务：Abort-GrayscaleTask | GrayscaleTask |     |
| 回滚灰度发布任务：Undo-GrayscaleTask | GrayscaleTask |     |
| 删除灰度发布任务：Delete-GrayscaleTask | GrayscaleTask |     |
| 创建GitOps应用：Create-GitOpsApplication | GitOpsApplication |     |
| 更新GitOps应用：Update-GitOpsApplication | GitOpsApplication |     |
| 同步GitOps应用：Sync-GitOpsApplication | GitOpsApplication |     |
| 删除GitOps应用：Delete-GitOpsApplication | GitOpsApplication |     |
| 导入 GitOps 仓库：Import-GitOpsRepository | GitOpsRepository |     |
| 删除 GitOps 仓库：Delete-GitOpsRepository | GitOpsRepository |     |
| 工具链集成：Integrated-Toolchain | Toolchain |     |
| 解除集成工具链：Delete-Toolchain | Toolchain |     |
| 绑定工具链项目：Bind-ToolchainProject | ToolchainProject | jira、gitlab 支持 管理员视觉下sonarqube 也支持 |
| 解除绑定工具链工具链项目：Unbind-ToolchainProject | ToolchainProject | jira、gitlab 支持 管理员视觉下sonarqube 也支持 |