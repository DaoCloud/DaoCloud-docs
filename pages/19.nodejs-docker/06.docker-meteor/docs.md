---
title: '用 Docker 镜像的方式构建 Meteor 应用'
---

Meteor 是构建 Web 应用的极易上手的环境。本文将介绍如何利用 MeteorHacks 提供的 `meteorhacks/meteord` 镜像在 DaoCloud 平台上构建和部署。

##### 准备

首先当然要准备好所有的 Meteor 工具。强大的 `meteord` 镜像可以让我们不必在本地测试镜像，意味着本地可以不需要 Docker 环境。

```
curl https://install.meteor.com | sh
meteor create docker-meteor
cd docker-meteor
```

你当然可以选择进入已有的 Meteor 应用的目录。

##### Dockerfile

`meteord` 镜像已经为我们做好了很多工作，我们的 Dockerfile 也就极度简化了。执行：

```
echo "FROM meteorhacks/meteord:onbuild" > Dockerfile
```

##### 构建 & 部署

在当前（应用）目录里建立你的 Git 仓库，提交并推送到远端 Git 仓库，在 DaoCloud 上创建项目并且按照默认设置触发第一次构建就行了。

部署时，所有应用需要的环境变量直接传入容器即可。值得注意的是，`MONGO_URL` 和 `ROOT_URL` 是必须设定的。MongoDB 的连接字符串可以自己通过 DaoCloud 的服务绑定自行拼接出来。

```
MONGO_URL=mongodb://user:pwd@host:port/instance
ROOT_URL=http://myapp.daoapp.io
```

##### 其他提示

这样构建，每次都会下载 Meteor、构建、删除 Meteor。如果造成调试不方便，试试使用 devbuild 这个 tag 下的镜像。
