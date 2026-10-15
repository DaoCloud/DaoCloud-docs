---
hide:
  - toc
---

# ClawOS Permissions

[ClawOS](../../clawos/intro/quickstart.md) supports four user roles:

- Admin: has full create, read, update, and delete permissions on all features under **Workspace View** and **Operations**.
- Workspace Admin: has full create, read, update, and delete permissions on all features under the authorized workspace view.
- Workspace Editor: has update and read permissions on all features under the authorized workspace view.
- Workspace Viewer: has read permissions on all features under the authorized workspace view.

Each role has different permissions, which are described below.

<!--
Use `&check;`for permissions granted and `&cross;`for permissions not granted.
-->

| Menu Objects | Actions | Admin | Workspace Admin | Workspace Editor | Workspace Viewer |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| **Workspace View** | | | | | |
| Overview | View overview | &check; | &check; | &check; | &check; |
| ClawHub Management | View Skill Marketplace | &check; | &check; | &check; | &check; |
| OpenClaw Instances | View (can only view your own OpenClaw instances) | &check; | &check; | &check; | &cross; |
| | Create | &check; | &check; | &check; | &cross; |
| | Edit (including edit/restart/power on/power off) | &check; | &check; | &check; | &cross; |
| | Delete | &check; | &check; | &check; | &cross; |
| | View all instances (can view all OpenClaw instances under the workspace) | &check; | &check; | &cross; | &cross; |
| | Manage all instances (can manage all OpenClaw instances under the workspace) | &check; | &cross; | &cross; | &cross; |
| **Administrator View** | | | | | |
| Overview | View overview | &check; | &check; | &cross; | &cross; |
| ClawHub Skill Management | View | &check; | &check; | &cross; | &cross; |
| | Create | &check; | &check; | &cross; | &cross; |
| | Edit (including listing and delisting) | &check; | &check; | &cross; | &cross; |
| | Delete | &check; | &check; | &cross; | &cross; |
