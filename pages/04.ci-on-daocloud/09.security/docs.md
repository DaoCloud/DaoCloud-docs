---
title: '绑定代码源后，是否会存在安全隐患 ?'
markdown:
    extra: true
gravui:
    enabled: true
    tabs: true
taxonomy:
    category:
        - docs
process:
    twig: true
---

<!-- reviewed by fiona -->

<!-- 

分三部分强调安全：

1. 采用 OAuth 方式登录和授权，标准化操作， DaoCloud 不保留任何用户名密码

2. DaoCloud 访问代码库通过 Deploy Key 方式，用户可在代码库内看到经过授权的 Deploy Key（截图）。除了在 DaoCloud 内部解除绑定，用户可以通过在代码仓库的配置页面删除 Deploy Key 的方式，强行终止 DaoCloud 访问代码，强调即使授权之后，用户也拥有绝对控制。

3. DaoCloud 拉取代码，结束镜像构建后，会实质性删除代码，DaoCloud 承诺不保留任何用户的代码。



-->

---

DaoCloud 通过在 GitHub 等第三方代码托管平台进行 OAuth 认证，将一个 [WebHook](https://developer.github.com/webhooks) 加入到你需要通过 DaoCloud 进行构建的代码库中。当您每次对该代码库进行修改操作时（如 Push、Pull Request 等），GitHub 等平台便会向 DaoCloud 发出通知。DaoCloud 收到来自代码托管平台的通知后，便会根据您在代码库中定义的 DaoCloud 持续集成配置文件进行拉取、构建和测试等工作。

### OAuth 认证机制

DaoCloud 与 GitHub 等平台之间采用 OAuth 的方法进行认证，这使得 DaoCloud 只会得到通过 GitHub 等平台返回的 **Access Token**，这是 DaoCloud 与 GitHub 等平台进行通讯的凭证，而它是具有时效性的。一旦 Access Token 过期，DaoCloud 就无法读取您账号中的信息，直到获得重新授权。

这同时也意味著 DaoCloud 并不会存储您的 GitHub 等平台的账号和密码。

### Deploy Key

当您在 DaoCloud 上选择了一个托管在 GitHub 等平台的代码库作为 Docker 镜像的代码源时，DaoCloud 会向该代码库中添加一个用于持续集成的 **Deploy Key**，这使得 DaoCloud 可以对该代码库中的源代码进行读取。

您除了可以在 DaoCloud 内部对该代码库解除绑定外，还可以通过在代码库的配置页面中，将 DaoCloud 的 Deploy Key 删除，这样可以强行终止 DaoCloud 对该代码库的访问。

也就是说，即便您授权了 DaoCloud 访问您的代码库，您还是有绝对权利控制 DaoCloud 对代码库的访问权限的。

### 拉取代码

在构建 Docker 镜像时，DaoCloud 会从第三方代码托管平台拉取您的代码库代码。当 DaoCloud 完成了对代码的构建后，会**物理**删除您的代码，以保证代码的安全性。DaoCloud 承诺不保留任何用户代码。