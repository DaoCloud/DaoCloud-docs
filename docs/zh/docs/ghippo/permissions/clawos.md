# ClawOS 权限说明

[ClawOS](../../clawos/intro/quickstart.md)支持四种用户角色：

- Admin ：拥有 `工作空间视角` 和 `运维管理` 全部功能的增删改查的权限。
- Workspace Admin：拥有授权工作空间视角全部功能的增删改查的权限。
- Workspace Editor：拥有授权工作空间视角全部功能的更新、查询的权限。
- Workspace Viewer：拥有授权工作空间视角全部功能的查询的权限。

每种角色具有不同的权限，具体说明如下。

<!--
有权限使用 `&check;`，无权限使用 `&cross;`
-->

| 菜单对象 | 操作 | Admin | Workspace Admin | Workspace Editor | Workspace Viewer |
|-----------|-----------|-----------|-----------|-----------|-----------|
| **工作空间视角** | | | | | |
| 概览 | 查看概览 | &check; | &check; | &check; | &check; |
| ClawHub 管理 | 查看 Skill 市场 | &check; | &check; | &check; | &check; |
| OpenClaw 实例 | 查看（仅可查看自己的 OpenClaw 实例） | &check; | &check; | &check; | &cross; |
| | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑（包含编辑/重启/开机/关机） | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看所有实例（可以查看 workspace 下的全部 OpenClaw 实例） | &check; | &check; | &cross; | &cross; |
| | 管理所有实例（可以管理 workspace 下的全部 OpenClaw 实例） | &check; | &cross; | &cross; | &cross; |
| **管理员视角** | | | | | |
| 概览 | 查看概览 | &check; | &check; | &cross; | &cross; |
| ClawHub Skill 管理 | 查看 | &check; | &check; | &cross; | &cross; |
| | 创建 | &check; | &check; | &cross; | &cross; |
| | 编辑（包含上下架操作） | &check; | &check; | &cross; | &cross; |
| | 删除 | &check; | &check; | &cross; | &cross; |