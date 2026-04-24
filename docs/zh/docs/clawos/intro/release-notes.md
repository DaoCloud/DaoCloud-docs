# ClawOS Release Notes

本页列出 ClawOS 的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2026-03-23

### v0.2.0

#### AgentClaw Server

- **新增** `ListWorkspaceAgentImage` API，支持列举可用的 Agent 容器镜像
- **新增** Agent 实例（**AgentInstance**）完整 CRUD 接口：创建、查询、更新、删除
- **新增** Grafana 总览（**Overview**）仪表盘
- **修复** 列举 Agent 实例时 Token 为空（nil）导致的异常
- **修复** Agent 实例列表分页（Pagination）错误
- **优化** API Base URL 统一增加 `/v1` 前缀
- **升级** 前端 UI 至 v0.1.0
