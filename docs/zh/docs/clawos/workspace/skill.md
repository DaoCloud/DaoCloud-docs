# Skill 市场

Skill 市场是 ClawHub 中面向工作空间成员的 Skill 浏览与安装入口。用户可以在这里查看当前可用的 Skill，并根据安装说明前往 OpenClaw 实例中安装使用。

Skill 是 OpenClaw 实例可调用的能力扩展。安装 Skill 后，OpenClaw 可以获得对应能力，例如文件处理、数据分析、系统查询、业务工具调用等。

Skill 市场分为两类：

- **公开 Skill**：由超级管理员发布，所有工作空间成员都可以查看和使用
- **私有 Skill**：由当前工作空间发布并审核通过，仅当前工作空间成员可见和使用

## 查看 Skill

进入 **ClawHub > Skill 市场** 后，可以在页面上方切换 **公开 Skill** 和 **私有 Skill**。点击 Skill 卡片中的 **详情**，可进入 Skill 详情页。

详情页一般包含三个 Tab：

| Tab | 说明 |
| --- | --- |
| **概览** | 展示 Skill 的 README 或使用说明，帮助用户理解该 Skill 的用途和使用方法 |
| **文件** | 展示 Skill 包中的文件结构，可查看 README、配置文件、依赖文件、脚本等内容 |
| **版本** | 展示该 Skill 的历史版本、当前版本和安全审核结果 |

## 安装 Skill

在 Skill 详情页右侧会展示安装说明。用户可以按页面提示安装 Skill，通常有两种方式：

1. 复制安装命令，进入 OpenClaw 实例后执行安装
2. 前往 OpenClaw 实例，在 **技能** 或相关入口中选择该 Skill 进行安装

安装完成后，该 OpenClaw 实例即可使用该 Skill 提供的能力。

## 使用建议

普通用户通常只需要在 Skill 市场中完成三件事：

1. 找到需要的 Skill
2. 查看说明，确认它能解决自己的问题
3. 按安装说明前往 OpenClaw 实例安装

如果找不到需要的 Skill，可以联系工作空间管理员发布私有 Skill（参见 [Skill 管理](./skill-manage.md)），或由平台管理员发布公开 Skill。
