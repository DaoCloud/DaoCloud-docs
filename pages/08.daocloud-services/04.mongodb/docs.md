---
title: '使用和管理 Mongo 服务'
taxonomy:
    category:
        - docs
---

创建 MongoDB 服务

使用 MongoDB 服务

管理 MongoDB 服务

MongoDB 使用注意事项




![](http://blog.daocloud.io/wp-content/uploads/2015/05/MongoDB.png)

## Mongo Express 是什么？

**Mongo Express** 是使用 Node.js 和 Express 框架实现的轻量级 MongoDB 数据库管理程序，通过它您可以轻松管理您的 MongoDB 数据库。

DaoCloud 平台有大量用户使用 MongoDB 服务，我们在镜像仓库中增加了 Mongo Express 工具，方便用户管理和维护 MongoDB 实例。

> 注意：目前在 DaoCloud 镜像仓库提供的 Mongo Express 版本不支持授权认证，您启动 Mongo Express 容器后，容器的 URL 是公开访问的。所以在您使用完毕后请立即「停止」容器，防止 MongoDB 数据库被他人操作。

## 如何部署 Mongo Express？

### 启动步骤

1. 从最新镜像启动 mongo-express 容器。
2. 绑定一个需要管理的 MongoDB 服务实例，设置服务别名为「MongoDB」（不区分大小写）。
3. 启动容器。

### 具体的创建过程

#### 首先保证存在一个或新建一个需要被管理的 MongoDB 服务实例（如果已有 MongoDB 服务实例，可跳过这个步骤）

1. 在控制台，点击「服务集成」。
2. 在 Dao 服务中，点击 MongoDB。
3. 点击「创建服务实例」。
4. 为服务实例命名，并点击“创建”。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/mongo-express-1.jpg)

#### 接着，我们启动 mongo-express 容器

1. 在控制台，点击「镜像仓库」。
2. 在 DaoCloud 镜像中，点击「mongo-express」图标。
3. 点击「部署新版本」。
4. 为 mongo-express 容器命名。
5. 选择容器配置和运行环境。
6. 点击「服务&环境」。
7. 点击之前创建的 MongoDB 实例，显示「待绑定」。
8. 在环境变量的服务别名中，输入 MongoDB。
9. 点击「立即部署」。
10. 部署完成后，访问返回的 URL，使用 Mongo Express。

![](http://blog.daocloud.io/wp-content/uploads/2015/05/mongo-express-2.jpg)

![](http://blog.daocloud.io/wp-content/uploads/2015/05/mongo-express-3.jpg)

> 提示：Mongo Express 的使用方式，请参考 NPM 上的 [mongo-express](https://www.npmjs.com/package/mongo-express)
