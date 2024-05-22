---
MTPE: windsonsea
date: 2024-05-22
hide:
  - toc
---

# Workbench Audit Items

| Events | Resource Type | Notes |
| --- | --- | --- |
| Create-Application | Application | |
| Update-Application | Application | Edit YAML, create snapshots, rollback |
| Delete-Application | Application | |
| Create-OAMApplication | OAMApplication | |
| Update-OAMApplication | OAMApplication | Edit YAML |
| Add-OAMApplicationComponent | OAMApplicationComponent | Add component |
| Update-OAMApplicationComponentTrait | OAMApplicationComponentTrait | Update OAM features for application component |
| Delete-OAMApplication | OAMApplication | |
| Create-HelmApplication | HelmApplication | |
| Create-OLMApplication | OLMApplication | |
| Update-OLMApplication | OLMApplication | |
| Delete-OLMApplication | OLMApplication | |
| Create-Namespace | Namespace | |
| Update-NamespaceQuota | NamespaceQuota | |
| Delete-Namespace | Namespace | |
| Create-Pipeline | Pipeline | |
| Update-Pipeline | Pipeline | Includes all update operations (edit Jenkinsfile, edit configuration, edit graphical) |
| Run-Pipeline | Pipeline | Run immediately |
| ReRun-Pipeline | Pipeline | Re-run operation |
| Abort-Pipeline | Pipeline | Terminate operation + termination of approval step |
| Approval-Pipeline | Pipeline | Approve pipeline |
| Delete-Pipeline | Pipeline | |
| Create-PipelineCredential | PipelineCredential | |
| Delete-PipelineCredential | PipelineCredential | |
| Create-GrayscaleTask | GrayscaleTask | Whether to distinguish between blue-green or canary |
| Update-GrayscaleTask | GrayscaleTask | Update release task, update version, edit YAML, update number of instances |
| Upgrade-GrayscaleTask | GrayscaleTask | |
| Abort-GrayscaleTask | GrayscaleTask | |
| Undo-GrayscaleTask | GrayscaleTask | |
| Delete-GrayscaleTask | GrayscaleTask | |
| Create-GitOpsApplication | GitOpsApplication | |
| Update-GitOpsApplication | GitOpsApplication | |
| Sync-GitOpsApplication | GitOpsApplication | |
| Delete-GitOpsApplication | GitOpsApplication | |
| Import-GitOpsRepository | GitOpsRepository | |
| Delete-GitOpsRepository | GitOpsRepository | |
| Integrated-Toolchain | Toolchain | |
| Delete-Toolchain | Toolchain | |
| Bind-ToolchainProject | ToolchainProject | Jira and GitLab support SonarQube from an administrator's perspective as well |
| Unbind-ToolchainProject | ToolchainProject | Jira and GitLab support SonarQube from an administrator's perspective as well |
