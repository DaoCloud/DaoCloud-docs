---
hide:
  - toc
---

# 凭证管理

凭证可以保存敏感信息，例如用户名密码、访问令牌（Access Token）、Kubeconfig 等，使保存的数据更安全灵活并免于暴露到镜像中。
当流水线运行时，大多数情况下会与第三方网站或应用程序进行交互，如 Git 仓库、镜像仓库等。
此过程中需要提供相应的凭证，所以需要用户来为流水线配置凭证，用户配置凭证后，便可以利用这些凭证来与第三方网站或应用程序进行交互。

目前，您可以在应用工作台中创建以下 3 种类型的凭证：

- __用户名和密码__ ：用于存储用户名和密码的认证信息，若第三方网站或应用程序支持用户名/密码的方式访问，则可以选择这种类型，例如 GitHub、GitLab 和 Docker Hub 的帐户。

- __访问令牌（Access Token）__ ：API token 之类的 token (如 GitHub 个人访问 token)。

- __kubeconfig__ ：用于配置跨集群认证。

- __SSH__ ：SSH 公钥/私钥对。

    !!! note

        SSH 类型的凭证在使用时（比如git clone）需要验证主机的身份，目前直接执行会报错。需要前往 Jenkins 后台在 'Manage Jenkins' -> 'Configure Global Security' -> 'Git Host Key Verification Configuration' 这个配置项里修改选项为：'No verification'

创建和管理凭证的具体步骤如下：

1. 在左侧导航栏中点击 __流水线__ -> __凭证__ ，进入凭证列表，点击右上角的 __新建凭证__ 。

    ![新建凭证](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cred01.png)

2. 在 __创建凭证__ 页面中，配置相关参数后点击 __确定__ 。

    ![配置参数](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cred02.png)

    - 填写 __凭证名称__ ，设置可以在流水线中使用的 ID，例如 __dockerhub-id__ 。注意：一旦设置就不能再进行更改。
    - 在 __类型__ 字段中，选择要添加的凭证类型。
    - 根据不同的凭证类型填写相应的字段：

        - 用户名和密码：在对应字段指定凭证的 __用户名__ 和 __密码__ 。
        - 访问令牌（Secret text）：复制加密文本到 __令牌__ 字段中。
        - Kubeconfig：复制集群证书到 __Kubeconfig__ 字段中。
        - SSH：定义：__用户名__（是用于登录远程服务器的账户名）和 __SSH Key 对应的私钥__（用于身份验证的SSH私钥）和 __密码短语__（如果私钥被密码短语保护，需要提供这个密码短语才能使用私钥）

3. 屏幕提示创建成功，新创建的凭证默认位于第一个。

    ![创建成功](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/cred03.png)

4. 点击列表右侧的 __┇__ ，可以在弹出菜单中选择编辑或删除等操作。

    !!! warning

        如果删除了某个流水线正使用的凭证，可能会影响流水线的访问，请谨慎操作。
