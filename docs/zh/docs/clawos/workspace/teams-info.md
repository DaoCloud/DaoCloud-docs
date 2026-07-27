# OpenClaw 对接 Microsoft Teams

本文介绍如何注册 Microsoft Entra 单租户应用，创建 Azure Bot，并将 OpenClaw 接入 Microsoft Teams。

## 1、前置条件

开始前请确认：

- 已拥有客户 Microsoft Entra 租户和 Azure 订阅。
- 具备创建应用注册和 Azure Bot 的权限。
- Messaging endpoint 是公网可访问的 HTTPS 地址。

## 2、字段对应关系

| OpenClaw 字段 | Microsoft 中的名称 | 填写内容 | 注意事项 |
| --- | --- | --- | --- |
| Client ID | Application (client) ID / Microsoft App ID | Entra 应用注册概览页中的 GUID | 不要填写 Object ID |
| Client Secret | Client secret → Value | 创建客户端密码后显示的 Value | 不要填写 Secret ID；Value 只显示一次 |
| Tenant ID | Directory (tenant) ID / App Tenant ID | Entra 租户 GUID | 必须与应用注册所在租户一致 |
| Messaging endpoint | Azure Bot → Configuration → Messaging endpoint | OpenClaw 提供的完整 URL | 必须使用完整 HTTPS 地址 |

## 3、获取 Client ID、Tenant ID 及 Client Secret

### 3.1 注册应用

访问 [Microsoft Entra 管理中心](https://entra.microsoft.com/)，选择：

> Entra ID → App registrations → New registration

填写：

- **Name**：例如 `OpenClaw-Teams-Prod`
- **Supported account types**：选择 `Accounts in this organizational directory only`
- **Redirect URI**：本文流程通常不需要填写

注册完成后，在 **Overview** 页面复制：

- **Application (client) ID**：作为 OpenClaw 的 Client ID
- **Directory (tenant) ID**：作为 OpenClaw 的 Tenant ID

### 3.2 创建 Client Secret

在应用注册中选择：

> Certificates & secrets → Client secrets → New client secret

填写描述和有效期，选择 **Add**。

创建后立即复制 **Value**，该值就是 OpenClaw 的 Client Secret。

> **注意：** Microsoft 不会再次显示 Secret Value。如果忘记保存，只能重新创建一个 Client Secret。

## 4、创建并配置 Azure Bot

打开 [Azure 门户](https://portal.azure.com/)，选择：

> Create a resource → 搜索 `bot` → Azure Bot → Create

### 4.1 配置应用身份

在 **Microsoft App ID** 或身份配置区域：

1. 选择 **Single Tenant**。
2. 选择 **Use existing app registration**。
3. 输入前面创建的 **Application (client) ID**。
4. 如果页面要求输入 Tenant ID，填写同一个 **Directory (tenant) ID**。

完成配置后选择：

> Review + create → Create

### 4.2 配置 Messaging endpoint

进入 Azure Bot 资源：

> Settings → Configuration

将 OpenClaw 提供的完整 endpoint 填入 **Messaging endpoint**，然后选择 **Apply**。

该地址必须：

- 使用 HTTPS；
- 可以从公网访问；
- 保留 OpenClaw 提供的完整路径。

### 4.3 启用 Microsoft Teams channel

进入：

> Channels → Microsoft Teams

同意相关条款。如果页面显示 **Cloud environment**，选择与客户 Teams 环境匹配的选项，然后选择 **Apply**。

## 5、在 OpenClaw 中填写信息

| OpenClaw 输入框 | 填写内容 |
| --- | --- |
| Client ID | Entra 应用的 Application (client) ID |
| Client Secret | Entra Client secret 的 Value |
| Tenant ID | Entra 应用的 Directory (tenant) ID |

保存后，确认各字段没有多余空格或换行。

## 6、将 Bot 添加到 Teams

启用 Teams channel 后，还需要将 Bot 添加到 Teams。

### 测试环境

在 Azure Bot 的：

> Channels → Microsoft Teams

页面获取 Teams 测试链接，打开后选择 Teams 客户端或 Teams Web，将 Bot 添加到 Teams。

### 生产环境

生产环境建议创建 Teams App，将 Bot ID 设置为 Entra 应用的 **Application (client) ID**，然后上传或发布到客户 Teams 租户。

仅通过 Bot GUID 添加适合测试，不建议用于生产环境。

## 7、验证清单

| 检查项 | 通过标准 |
| --- | --- |
| 应用注册 | 应用类型为 Single Tenant |
| Client ID | OpenClaw、Entra 和 Azure Bot 中的应用 ID 一致 |
| Client Secret | 使用 Secret Value，且未过期 |
| Tenant ID | OpenClaw 与 Entra 的 Tenant ID 一致 |
| Messaging endpoint | 配置为 OpenClaw 提供的完整 HTTPS 地址 |
| Teams channel | Microsoft Teams channel 已启用 |
| Teams 安装 | Bot 已添加到 Teams |
| 消息测试 | Teams 消息能够触发 OpenClaw 回复 |

## 8、密钥轮换

Client Secret 到期前：

1. 创建新的 Client Secret。
2. 将新的 Value 更新到 OpenClaw。
3. 发送 Teams 测试消息确认生效。
4. 再删除旧 Secret。

## 9、常见问题

### Teams 中找不到 Bot

检查 Teams channel 是否启用，以及 Bot 是否已经通过测试链接或 Teams App 添加到 Teams。

### 发送消息后没有回复

检查以下内容：

- Messaging endpoint 是否完整；
- endpoint 是否可以公网访问；
- Client ID、Client Secret 和 Tenant ID 是否填写正确；
- Cloud environment 是否选择正确。

### 出现 401 或 403

重点检查：

- 是否误填了 Secret ID；
- Client Secret 是否已过期；
- Tenant ID 是否属于当前应用注册所在的租户。

## 10、参考文档

- [Register a bot with Azure](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-quickstart-registration?tabs=++userassigned&view=azure-bot-service-4.0)
- [Connect a Bot Framework bot to Microsoft Teams](https://learn.microsoft.com/en-us/azure/bot-service/channel-connect-teams?view=azure-bot-service-4.0)
