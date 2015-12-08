---
title: 'Hello Docker'
---

<!-- reviewed by fiona -->


![](http://7xi8kv.com5.z0.glb.qiniucdn.com/docker.jpg)

> 目标：使用静态页面来完成一个简单的 Docker Demo

本项目代码维护在 [front-end-docker-sample](https://github.com/Ye-Ting/front-end-docker-sample) 

Demo 地址: [http://yeting-front-end-docker-sample.daoapp.io/](http://yeting-front-end-docker-sample.daoapp.io/)

### Docker 化应用的关键元素

- 镜像是 Docker 应用的静态表示，是应用的交付件，镜像中包含了应用运行所需的所有依赖：包括应用代码、应用依赖库、应用运行时和操作系统。
- Dockerfile 是一个描述文件，描述了产生 Docker 镜像的过程。详细文档请参见 Dockerfile文档。
- 容器是镜像运行时的动态表示，如果把镜像想象为一个 Class 那么容器就是这个 Class 的 instance 实例。

一个应用 Docker 化的第一步就是通过 Dockerfile 产生应用镜像。

### 编写 Dockerfile

本次基础镜像使用 Nginx 官方镜像，也可以根据自己的项目需求与环境依赖使用定制基础镜像。

***Dockerfile***

**首先，选择官方的 nginx 镜像作为项目的基础镜像。**

```
FROM nginx

MAINTAINER YeTing "me@yeting.info"
```

**接着，将代码复制到目标目录。**

```
COPY . /usr/share/nginx/html
```

- ADD 与 COPY 的区别，总体来说 ADD 和 COPY 都是添加文件的操作，其中 ADD 比 COPY 功能更多，ADD 允许后面的参数为 URL，还有 ADD 添加的文件为压缩包的话，它将自动解压。
- CMD 为本次构建出来的镜像运行起来时候默认执行的命令，我们可以通过 docker run 的启动命令修改默认运行命令。
- Dockerfile 具体语法请参考：[Dockerfile](https://docs.docker.com/reference/builder/) 。

### 构建 Docker Image

有了 Dockerfile 以后，我们可以运行下面的命令构建前端镜像并命名为 my-front-end-app：

```bash
docker build -t my-front-end-app .
```

### 部署 Docker Image

**最后，让我们从镜像启动容器：**

```
docker run -p 80:80 my-front-end-app
```

如果看到这界面，那么就说明你成功进入到了一个 Docker 化的世界。

```
Hello Docker !!

欢迎进入 Docker 的世界!!
```

