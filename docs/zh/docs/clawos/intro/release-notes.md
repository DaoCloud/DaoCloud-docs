# Release Notes

本页列出 ClawOS 的 Release Notes，便于您了解各版本的演进路径和特性变化。ClawOS 智能体面向企业级 AI 智能体使用场景，提供基于 DCE 的 OpenClaw 托管运行能力，帮助用户快速创建、访问和管理自己的 AI 数字员工。OpenClaw 不再只是被动回答问题的 AI 助手，而是能够主动规划任务、调用工具、执行代码、操作文件和完成端到端工作流的智能体运行时。

## 2026-05-31

### v0.3.3

- **新增** 支持自定义 ClawOS 角色
- **新增** 支持 Skill 市场
- **优化** 创建 OpenClaw 实例时，自动对 API key 可见性进行隔离


## 2026-04-30

### v0.3.2

- **新增** 一键创建 OpenClaw 实例
- **新增** 一键集成飞书
- **新增** 支持手动配置飞书应用信息
- **新增** 安全容器沙箱隔离
- **新增** 支持通过快捷入口一键访问 OpenClaw 实例
- **新增** 支持通过远程桌面访问 OpenClaw 实例
- **新增** 支持通过文件管理器上传文件
- **新增** 支持选择公有/私有模型创建 OpenClaw 实例
- **新增** 支持在管理员模式下查看工作空间下的 overview


!!! info

    从 v0.2.0 升级到 v0.3.2 有 breaking change， 需要更新已有的 OpenClaw 实例，下载 [agentclaw_upgrade_v0.3_patch_tool.tar.gz](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/agentclaw_upgrade_v0.3_patch_tool.tar.gz) 
    工具，通过它自动完成更新。具体使用手册在压缩包中。


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
