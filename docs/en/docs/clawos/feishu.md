# Feishu Integration

This document explains how to integrate OpenClaw with Feishu to enable conversations with OpenClaw directly in Feishu.

## Creating a Feishu Application

### Create an Enterprise Self-Built Application

1. Log in to the [Feishu Open Platform](https://open.feishu.cn/app).

2. Click **Create Enterprise Self-Built Application**.

    

### Configure Application Information

Set the application name, description, and icon, then click **Create** to finish setup.



### Add Bot Capability

1. In the left navigation tree, go to **App Capabilities** -> **Add App Capabilities**.  
2. Select the **By Capability** tab.  
3. Click **Add** on the **Bot** capability card.

    

## Configure Permissions

### Import Permission Configuration

1. In the left navigation tree, go to **Development Configuration** -> **Permissions Management**.

2. Click **Batch Import/Export Permissions**.

    

3. In the **Import** tab, paste the [permission configuration code](#permission-config).

4. Click **Next: Confirm New Permissions**.

5. In the pop-up dialog, verify the permissions and click **Apply**.

    

### Permission Configuration Code

<details id="permission-config">
<summary>Click to view permission configuration code</summary>

```json
{
  "scopes": {
    "tenant": [
      "contact:contact.base:readonly",
      "docx:document:readonly",
      "im:chat:read",
      "im:chat:update",
      "im:message.group_at_msg:readonly",
      "im:message.p2p_msg:readonly",
      "im:message.pins:read",
      "im:message.pins:write_only",
      "im:message.reactions:read",
      "im:message.reactions:write_only",
      "im:message:readonly",
      "im:message:recall",
      "im:message:send_as_bot",
      "im:message:send_multi_users",
      "im:message:send_sys_msg",
      "im:message:update",
      "im:resource",
      "application:application:self_manage",
      "cardkit:card:write",
      "cardkit:card:read"
    ],
    "user": [
      "contact:user.employee_id:readonly",
      "offline_access",
      "base:app:copy",
      "base:field:create",
      "base:field:delete",
      "base:field:read",
      "base:field:update",
      "base:record:create",
      "base:record:delete",
      "base:record:retrieve",
      "base:record:update",
      "base:table:create",
      "base:table:delete",
      "base:table:read",
      "base:table:update",
      "base:view:read",
      "base:view:write_only",
      "base:app:create",
      "base:app:update",
      "base:app:read",
      "sheets:spreadsheet.meta:read",
      "sheets:spreadsheet:read",
      "sheets:spreadsheet:create",
      "sheets:spreadsheet:write_only",
      "docs:document:export",
      "docs:document.media:upload",
      "board:whiteboard:node:create",
      "board:whiteboard:node:read",
      "calendar:calendar:read",
      "calendar:calendar.event:create",
      "calendar:calendar.event:delete",
      "calendar:calendar.event:read",
      "calendar:calendar.event:reply",
      "calendar:calendar.event:update",
      "calendar:calendar.free_busy:read",
      "contact:contact.base:readonly",
      "contact:user.base:readonly",
      "contact:user:search",
      "docs:document.comment:create",
      "docs:document.comment:read",
      "docs:document.comment:update",
      "docs:document.media:download",
      "docs:document:copy",
      "docx:document:create",
      "docx:document:readonly",
      "docx:document:write_only",
      "drive:drive.metadata:readonly",
      "drive:file:download",
      "drive:file:upload",
      "im:chat.members:read",
      "im:chat:read",
      "im:message",
      "im:message.group_msg:get_as_user",
      "im:message.p2p_msg:get_as_user",
      "im:message:readonly",
      "search:docs:read",
      "search:message",
      "space:document:delete",
      "space:document:move",
      "space:document:retrieve",
      "task:comment:read",
      "task:comment:write",
      "task:task:read",
      "task:task:write",
      "task:task:writeonly",
      "task:tasklist:read",
      "task:tasklist:write",
      "wiki:node:copy",
      "wiki:node:create",
      "wiki:node:move",
      "wiki:node:read",
      "wiki:node:retrieve",
      "wiki:space:read",
      "wiki:space:retrieve",
      "wiki:space:write_only"
    ]
  }
}
```

</details>

> For detailed meanings of these permissions, see the [Feishu API Permission List](https://open.larkoffice.com/document/server-docs/application-scope/scope-list).

## Publish the Application

### Create Version and Publish

1. Click **Create Version** at the top of the page.

   

2. Configure version number, default capabilities, and release notes as needed.

   

3. Click **Save** at the bottom of the page to create the version.

   

4. Click **Confirm Publish** in the top-right corner.

   

### Get Configuration Information

1. In the left navigation tree, go to **Basic Information** -> **Credentials & Basic Info**.

2. In the **App Credentials** section, copy and record the **App ID** and **App Secret**.

   

## Configure Event Subscription & Callback Long Connection

!!! caution

    For bot applications without long connection enabled, you must start an OpenClaw instance after obtaining the **App ID** and **App Secret**
    in order to save event subscription and callback long connection settings. See the [OpenClaw Quick Start](./quickstart.md) guide.

### Configure Event Subscription

1. Go to **Event & Callback** and set the event subscription mode to **Long Connection**.

   

2. Add message receiving events (other events can also be added as needed):

   

### Configure Callback

1. Click **Callback Configuration**.

2. Select **Long Connection** as the configuration method.

   

3. Add a callback configuration.

   

### Publish Version

Publish the version and wait for approval.



## Start Conversation

Find your bot in Feishu and start chatting with OpenClaw!


