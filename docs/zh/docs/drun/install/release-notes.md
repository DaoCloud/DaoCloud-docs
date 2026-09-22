# d.run AI 安装器 Release Notes

本页列出 d.run AI 安装器的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2026-08-31

### v0.44.0

- **新增** 支持 gitops 模式部署的基础框架功能
- **新增** 支持 gitops 模式组件最小化部署
- **修复** 修复火种镜像串行检测问题 #3447
- **修复** 修复 helm rollback 进程卡死问题 #3461

## 2026-07-31

### v0.43.0

- **新增** 支持离线镜像的 clean 能力
- **新增** agentclaw 组件进入安装器
- **优化** metallb 负载均衡模式下，ES、Kafka 复用 insightVip 对外暴露，不再降级使用节点 IP
- **修复** 通过脚本导入镜像时 OCI 索引解析失败、镜像漏采集问题

## 2026-06-30

### v0.42.0

- **新增** 支持生成 token 工厂模式的 manifest 配置
- **新增** 支持从 deployment 中解析 mgr 镜像标签
- **优化** kube_version 更新到 v1.35.5
- **优化** 支持 RHEL10 离线 os pkg 依赖
- **修复** argocd 镜像离线化问题
