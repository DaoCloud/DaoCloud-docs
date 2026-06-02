# Release Notes

This page lists the release notes for ClawOS, providing an overview of version evolution and feature changes. ClawOS is designed for enterprise-grade AI agent scenarios, offering DCE-based OpenClaw managed runtime capabilities that help users quickly create, access, and manage their own AI digital employees. OpenClaw is no longer just a passive AI assistant that answers questions, but an agent runtime capable of proactively planning tasks, invoking tools, executing code, operating files, and completing end-to-end workflows.

## 2026-05-31

### v0.3.3

- **Added** support for customizing ClawOS roles
- **Added** skill marketplace support
- **Optimized** automatic isolation of API key visibility when creating OpenClaw instances


## 2026-04-30

### v0.3.2

- **Added** one-click creation of OpenClaw instances
- **Added** one-click Feishu integration
- **Added** support for manually configuring Feishu application information
- **Added** secure container sandbox isolation
- **Added** support for accessing OpenClaw instances via quick entry
- **Added** support for accessing OpenClaw instances via remote desktop
- **Added** support for uploading files through the file manager
- **Added** support for selecting public/private models when creating OpenClaw instances
- **Added** support for viewing workspace overview in administrator mode


!!! info

    Upgrading from v0.2.0 to v0.3.2 contains breaking changes. Existing OpenClaw instances need to be updated. Download the tool from
    [agentclaw_upgrade_v0.3_patch_tool.tar.gz](https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/agentclaw_upgrade_v0.3_patch_tool.tar.gz)
    to complete the update automatically. The detailed usage manual is included in the archive.


## 2026-03-23

### v0.2.0

#### AgentClaw Server

- **Added** `ListWorkspaceAgentImage` API to list available Agent container images
- **Added** full CRUD API for Agent instances (**AgentInstance**): create, query, update, delete
- **Added** Grafana **Overview** dashboard
- **Fixed** Nil token causing exceptions when listing Agent instances
- **Fixed** pagination errors in Agent instance list
- **Optimized** unified `/v1` prefix for all API base URLs
- **Upgraded** frontend UI to v0.1.0
