---
title: 'Submodule 支持'
---

有些项目的代码组织中使用了 git submodule 功能，但是如果某个项目引用的 submodule 是私有的，会导致代码构建／持续集成时拉取代码失败。这时可以参考下面的流程进行操作达到支持私有 submodule 的目的。

_下面的例子以 GitLab 为例_

### 创建项目
按照正常流程创建代码构建项目，项目创建后，DaoCloud 会自动在对应的 Git 代码项目中设置项目的 Deploy Key。

### 复制 Deploy Key
在对应代码项目设置中找到 DaoCloud 设置的 Deploy Key，并复制到任意文本文件中待后续使用

![](gitlab_setting_deploykey.png)

![](gitlab_deploykey_key.png)

### 删除 Deploy Key
删除上述项目的 Deploy Key
![](gitlab_deploykey_remove.png)

### 添加到用户的SSH_key
在某个 Git 用户账户下添加上面复制的 Deploy Key 为用户的 SSH_Key。请注意，该用户需要有对应代码项目以及所有依赖的 submodule 项目的访问权限

![](gitlab_sshkey_add.png)

![](gitlab_sshkey_addkey.png)

### 完成
完成上述设置后，就可以在构建项目／持续集成过程中正常拉取代码了

