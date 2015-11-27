---
title: 'Angular 应用根据环境变量切换不同的 CDN'
---

<!-- reviewed by fiona -->

<!--我们基于 [Angular Docker]() 来做一些改进。——缺链接 已修改 叶挺-->

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/ang.jpg)

在 Angular 项目在实际运用中，我们需要静态文件放在 CDN 上。那怎么通过单一的 Docker image 实现 CDN 地址可变呢？

我们基于 [用 Docker 搭建 Angular 前端应用](../../docker-frontend/docker-angular) 来做一些改进。

gulp 是一个很好用的构建工具，不仅是因为他的语法灵活，更是因为有非常多的插件供我们使用。

在这个例子中，我们使用 [gulp-cdnizer](https://www.npmjs.com/package/gulp-cdnizer)。

### Angular 项目构建优化

**首先，安装插件 `gulp-cdnizer`**。

```
npm install gulp-ng-config --save-dev
```

**接着，我们在 `/gulp/env.js` 文件下编写相应的 Task**。

```
gulp.task('cdn', function () {

  var cdn = process.env.APP_CDN || '';

  return gulp.src(
    path.join(conf.paths.dist, '*.html')
  )
    .pipe($.cdnizer({
      defaultCDNBase: cdn,
      files         : [
        'scripts/*.js',
        'styles/*.css'
      ]
    }))
    .pipe(gulp.dest(
      path.join(conf.paths.dist)
    ));
});

```

### 构建 Docker Image

**对 Dockerfile 启动命令 CMD 进行细微的调整**。

```
FROM node:0.12.7-wheezy

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

CMD gulp build && gulp cdn && cp -r dist/* /usr/share/nginx/html/ && nginx -g 'daemon off;'
```

有了 Dockerfile 以后，我们可以运行下面的命令构建前端镜像并命名为 my-angular-cdn-app：

```bash
docker build -t my-angular-cdn-app .
```

### 部署 Docker Image

**最后，让我们从镜像启动容器**：

```
docker run -p 80:80 -e "APP_CDN=这里填写你自己的CDN" my-angular-cdn-app
```

这样子我们就能从 80 端口去访问我们的 Angular 应用，并且该 Angular 应用是对应着不同的 CDN。