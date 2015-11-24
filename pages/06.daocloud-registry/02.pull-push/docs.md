---
title: 我的镜像
taxonomy:
    category:
        - docs
---

点击镜像名称后，进入镜像细节页面，在这个页面，您可以完成如下操作：

![](DashboardDaoCloud1.png?resize=800)

1. 查看镜像概览，这个概览的内容，来自您在代码仓库中的 Readme 文件，支持 markdown 格式。我们建议您在此写明镜像的介绍信息，和部署运行时的注意事项，便于团队内部其他成员知晓和协作。
2. 查看镜像版本，DaoCloud 将确保您在代码仓库每一次打 tag，我们都会完成一次镜像构建，这里列出了包括master-init在内的所有镜像历史版本
3. 在版本 tab，您还可以拉取镜像，部署镜像，把选定版本设置为 lastest，或删除镜像
4. 设置 tab，提供了镜像改名的功能

我的镜像是您的私有镜像仓库，您可以使用 Docker 客户端 pull 或者 push 镜像。以上图的镜像为例，以下是具体的操作步骤

在您的 Docker 主机的命令行界面，首先您需要完成登录，输入您的 DaoCloud ID 和密码即可完成

```
sudo docker login daocloud.io
Username:[您的 DaoCloud 用户名]
Password:［您的 DaoCloud 密码］
Email:［可以随便填］
Login Successed

```

```
docker pull daocloud.io/[你的 DaoCloud ID]/［镜像名称］:［Tag］  
```

```
docker tag
docker push
```

push 完成后，镜像会显示在「我的镜像」页面，您可以直接操作部署和其他修改。

>>>>> 注意，我们对所有用户都开通了镜像的 pull 功能，但是仅限付费用户使用 push 功能。另外，我们也建议您通过 Dockerfile 的方式在 DaoCloud 完成镜像的构建，或者直接使用 Docker Hub 上的镜像，尽量避免 push 本地镜像到 DaoCloud 平台，由于一些版本问题，如果你呢镜像版本较久，可能无法在 DaoCloud 完成部署。