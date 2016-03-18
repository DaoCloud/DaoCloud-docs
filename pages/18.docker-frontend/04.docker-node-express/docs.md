---
title: '用 Docker 搭建 Node Express 应用'
---

<!-- reviewed by fiona -->

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/node.jpg)

> 目标： 用 Docker 镜像的方式搭建 Node Express 应用

本项目代码：[node-express-docker-sample](https://github.com/Ye-Ting/node-express-docker-sample)

Demo ：http://yeting-front-node-express-docker-sample.daoapp.io/

### Node Express 应用搭建

首先，借助 [Yeomen Express generator](https://github.com/petecoop/generator-express) 生成一个 Node Express 应用 。

具体的操作都在上面的 Repo 中有说明，这里不做赘述。

值得注意的是：

- Express 默认暴露 3000 端口，通过环境变量 PORT 修改
- 启动命令 node bin/www 
- 调试命令 gulp 

### Dockerfile 编写

**首先，选择官方的 node 镜像作为项目的基础镜像**。

```
FROM node:0.12.7-wheezy

MAINTAINER YeTing "me@yeting.info"
```

**接着，优先将 `./package.json` 复制到镜像中，预先加载第三方依赖**。

```
WORKDIR /app

COPY ./package.json /app/

RUN npm install
```

> 每次 Dokcer 构建成功之后就会有缓存，这样的写法能提高缓存的命中率，优化 Docker 构建镜像的速度。

**最后，将 Express 应用程序复制到 /app，暴露 3000 端口**。

```
COPY . /app/
 
EXPOSE 3000

CMD node bin/www 
```

> Docker Container 之间是通过 link 机制来做通信的，EXPOSE 3000 ，是别的容器想要访问 该容器 3000 端口的前提条件。

### 构建 Docker Image

**完整的 Dockerfile**

```
FROM node:0.12.7-wheezy

MAINTAINER YeTing "me@yeting.info"

WORKDIR /app

COPY ./package.json /app/

RUN npm install

COPY . /app/
 
EXPOSE 3000

CMD node bin/www 
```

有了 Dockerfile 以后，我们可以运行下面的命令构建前端镜像并命名为 my-express-app：

```bash
docker build -t my-express-app .
```

### 部署 Docker Image

最后，让我们从镜像启动容器：

```
docker run -p 80:3000 my-express-app
```

这样子我们就能从 80 端口去访问我们的 Express 应用。


### Node Express 应用运行优化

当然， Node 是公认的不稳定，经常会出现服务器内存溢出，而崩溃退出。

我们针对这一点，可以对 Express 启动命令做优化。引入 forever 插件，通过 forever 来启动 express 应用。

**Dockerfile** 

```
FROM node:0.12.7-wheezy

MAINTAINER YeTing "me@yeting.info"

WORKDIR /app

RUN npm install -g forever

COPY ./package.json /app/

RUN npm install

COPY . /app/
 
EXPOSE 3000

CMD forever bin/www 
```

非常好，我们现在已经得到了一个优良的 Express Docker Seed，快来加入你的逻辑去完成你的 Express 应用吧。