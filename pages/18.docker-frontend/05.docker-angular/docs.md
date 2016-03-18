---
title: '用 Docker 搭建 Angular 前端应用'
---

<!-- reviewed by fiona -->

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/ang.jpg)

> 目标：用 Docker 镜像的方式搭建 Angular 前端应用

本项目代码维护在 [angular-docker-sample](https://github.com/Ye-Ting/angular-docker-sample)

### Angular 应用搭建

首先，借助 [generator-gulp-angular](https://github.com/Swiip/generator-gulp-angular) 生成一个 Angular 应用。 

具体的操作大致是

```
npm install -g yo gulp bower

npm install -g generator-gulp-angular

yo gulp-angular
```

值得注意的是：

- 项目依赖 node bower gulp 
- 调试命令 gulp serve
- 调试发布命令 gulp serve:dist
- 构建命令 gulp build 
- 构建目录 /dist
- 构建出来的是纯静态文件

该应用有个小问题，fonts 文件在 build 之后就不显示了，需要修改 `bower.json`。

```
{
"dependencies": {
    .....
  },
"overrides": {
    "bootstrap-sass-official": {
      "main": [
        "assets/stylesheets/_bootstrap.scss",
        "assets/fonts/bootstrap/glyphicons-halflings-regular.eot",
        "assets/fonts/bootstrap/glyphicons-halflings-regular.svg",
        "assets/fonts/bootstrap/glyphicons-halflings-regular.ttf",
        "assets/fonts/bootstrap/glyphicons-halflings-regular.woff",
        "assets/fonts/bootstrap/glyphicons-halflings-regular.woff2"
      ]
    }
  }
}

```

### Dockerfile 编写

首先，选择官方的 node 镜像作为项目的基础镜像。一般采用 node:0.12.7-wheezy ，不会缺少各种各样的东西。

```
FROM node:0.12.7-wheezy

MAINTAINER YeTing "me@yeting.info"
```

其次，由于该项目生成是纯静态文件，我们需要 Nginx 来作为 Web 服务器。

```
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.7.12-1~wheezy

RUN apt-get update && \
    apt-get install -y ca-certificates nginx && \
    rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80
```

- Web 根目录 `/usr/share/nginx/html`
- 访问日志输出到了标准输出，可通过 `docker logs` 查看
- 暴露 80 端口

接着，下载项目所需的依赖工具 `bower`、`gulp`。

```
RUN npm install -g bower gulp

WORKDIR /app
```

紧接着，优先将 `./package.json` 和 `./bower.json` 复制到镜像中，预先加载第三方依赖。

```
COPY ./package.json /app/
COPY ./bower.json /app/

RUN npm install && bower install --allow-root
```

> bower 默认不允许 Root 权限运行，所以要加入 `--allow-root` 参数。


然后，执行 Angular 构建命令，将构建生成的静态文件复制到 Web 根目录。

```
COPY . /app/

RUN gulp build 

RUN cp -R /app/dist/*  /usr/share/nginx/html
```

最后，设置 Docker 默认运行命令，启动 Nginx 为前台运行。

```
CMD ["nginx", "-g", "daemon off;"]
```

> Nginx 设置为前台运行主要是为了 Docker 容器启动不中断。

### 构建 Docker Image

**完整的 Dockerfile**

```
FROM node:0.12.7-wheezy

MAINTAINER YeTing "me@yeting.info"

RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list

ENV NGINX_VERSION 1.7.12-1~wheezy

RUN apt-get update && \
    apt-get install -y ca-certificates nginx && \
    rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

RUN npm install -g bower gulp

WORKDIR /app

COPY ./package.json /app/
COPY ./bower.json /app/
RUN npm install && bower install --allow-root

COPY . /app/

RUN gulp build 

RUN cp -R /app/dist/*  /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
```

有了 Dockerfile 以后，我们可以运行下面的命令构建前端镜像并命名为 my-angular-app：

```bash
docker build -t my-angular-app .
```

### 部署 Docker Image

最后，让我们从镜像启动容器：

```
docker run -p 80:80 my-angular-app
```

这样子我们就能从 80 端口去访问我们的 Angular 应用。


非常好，我们现在已经得到了一个优良的 Angular Docker Seed，快来加入你的逻辑去完成你的 Angular 应用吧。