# GitOps 相关问题

本页列出使用应用工作台 GitOps 时可能遇到的一些问题并给出相应的解决方案。

## 在 GitOps 模块下添加 GitHub 仓库时报错

由于 GitHub 移除了对 username/password 的支持，所以通过 HTTP 方式导入 **GitHub** 仓库时会导入失败，可能出现如下报错信息：

```bash
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/DaoCloud/dce-installer.git/'
```

**解决方案**：

使用 SSH 方式导入 **GitHub** 仓库。

## 在某个工作空间下在 GitOps 模块中添加仓库时提示仓库已经存在

目前一个仓库绑定只能到一个工作空间，不能绑定到不同工作空间。如果一个仓库已经绑定到了 A 工作空间，此时尝试在 B 工作空间下将其添加到 GitOps 中就会提示仓库已经存在。

**解决方案**：

先将该仓库与其当前绑定的工作空间解绑，然后再重新将其添加到目标的工作空间。
