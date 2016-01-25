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

关于 `meteorhack/meteord`，可以查看 https://hub.docker.com/r/meteorhacks/meteord/ 以获得更多信息。

##### 进阶

###### Kadira.io 接入

[Kadira.io](https://kadira.io) 是专业的 Meteor APM 平台。

完成注册后，Kadira.io 会要求你安装 `meteorhacks:kadira` 并设置 App ID 和 Secret。请按照 Kadira.io 的提示安装好 `meteorhacks:kadira`。在 Docker 化的平台上，建议采用环境变量的方法接入。

![kadira-env](kadira-env.png)

根据这些提示，在 DaoCloud 上设置对应的环境变量：

![daocloud-kadira-env](daocloud-kadira-env.png)

最后推送安装了 `meteorhacks:kadira` 包的版本并部署就好了。
