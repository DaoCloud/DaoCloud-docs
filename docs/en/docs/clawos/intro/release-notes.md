# ClawOS Release Notes

This page lists the release notes for ClawOS, providing an overview of version evolution and feature changes.

## 2026-03-23

### v0.2.0

#### AgentClaw Server

- **Added** `ListWorkspaceAgentImage` API to list available Agent container images
- **Added** Full CRUD API for Agent instances (**AgentInstance**): create, query, update, delete
- **Added** Grafana **Overview** dashboard
- **Fixed** Nil token causing exceptions when listing Agent instances
- **Fixed** Pagination errors in Agent instance list
- **Optimized** Unified `/v1` prefix for all API base URLs
- **Upgraded** Frontend UI to v0.1.0
