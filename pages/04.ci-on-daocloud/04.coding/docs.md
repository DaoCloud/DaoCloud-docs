---
title: '与 Coding 代码源绑定'
taxonomy:
    category:
        - docs
---

<!-- reviewed by fiona -->

<!-- 
Coding 的简单介绍

Coding 绑定流程的介绍和截图
DaoCloud GitHub 公有仓库提供了大量的开发示例代码，帮助用户快速上手，鼓励用户 Fork 这些项目。最后做一个链接，到写给开发者的例子这篇文章。
-->

---
### Coding

Coding 是国内新兴的第三方代码开发、托管和项目管理平台，拥有良好的用户体验和完备的功能。

![Coding](http://docs-static.daocloud.io/user/pages/04.ci-on-daocloud/04.coding/coding-1.jpg)

### 绑定 Coding 账号与 DaoCloud 账号

如需将托管在 Coding 上的项目代码拉取至 DaoCloud 并作为 Docker 镜像的构建基础，则需要先将您的 Coding 账号与 DaoCloud 账号绑定起来。

#### 第一步

在任意页面的右上角点击「账号信息」，并在新的页面中进入「第三方账号」标签页。

![第三方账户](http://docs-static.daocloud.io/user/pages/04.ci-on-daocloud/04.coding/github-12.jpg)

#### 第二步

点击 Coding 栏目中的「绑定账号」按钮。

![绑定账户](http://docs-static.daocloud.io/user/pages/04.ci-on-daocloud/04.coding/coding-2.jpg)

浏览器会自动跳转到 Coding 的授权请求页面，您只需要点击「**授权**」按钮，授权 DaoCloud 访问您的 Coding 账号即可。

![授权应用](http://docs-static.daocloud.io/user/pages/04.ci-on-daocloud/04.coding/coding-3.jpg)

#### 第三步

授权了 Coding 应用后，DaoCloud 将会自动完成与您的 GitHub 账号的绑定。

![完成绑定](http://docs-static.daocloud.io/user/pages/04.ci-on-daocloud/04.coding/coding-4.jpg)

>>>>> DaoCloud 为了更好地为您提供服务，会在认证请求中申请浏览私有库的权限。