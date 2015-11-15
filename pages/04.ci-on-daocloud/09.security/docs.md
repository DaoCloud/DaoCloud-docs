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

<!-- 

分三部分强调安全：

1. 采用 OAuth 方式登陆和授权，标准化操作， DaoCloud 不保留任何用户名密码

2. DaoCloud 访问代码库通过 Deploy Key 方式，用户可在代码库内看到经过授权的 Deploy Key（截图）。除了在 DaoCloud 内部解除绑定，用户可以通过在代码仓库的配置页面删除 Deploy Key 的方式，强行终止 DaoCloud 访问代码，强调即使授权之后，用户也拥有绝对控制。

3. DaoCloud 拉取代码，结束镜像构建后，会实质性删除代码，DaoCloud 承诺不保留任何用户的代码。



-->