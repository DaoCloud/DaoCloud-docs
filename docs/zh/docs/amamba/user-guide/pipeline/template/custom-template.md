# 创建自定义流水线模板

应用工作台模块支持自定义流水线模板，用户可以根据真实业务场景制作流水线模板，然后基于自定义模板快速创建符合要求的流水线。

## 前提条件

- [创建工作空间](../../../../ghippo/user-guide/workspace/workspace.md)、[创建用户](../../../../ghippo/user-guide/access-control/user.md)。
- 将该用户添加至该工作空间，并赋予 **workspace editor** 或更高权限。
- 配置好[流水线模板文件](info.md)。

### 操作步骤

1. 在**自定义流水线模板**页面点击**创建模板**

    ![click-create](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/template04.png)

2. 参考以下说明填写基本信息，然后点击**确定** 。

    - 模板名称：填写流水线模板的名称。
    - 描述信息：对当前流水线的描述信息，支持中文。
    - 模板文件：参考[流水线模板文件](info.md)填写或粘贴事先准备好的参数。

        ![config](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/template05.png)

3. 返回流水线模板列表页面，点击模板卡片可以删除或修改模板。

    ![config](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/template06.png)