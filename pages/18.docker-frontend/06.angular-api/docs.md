---
title: 'Angular 应用根据环境变量切换不同的后端 API'
---

<!-- reviewed by fiona -->

<!-- 我们基于 [Angular Docker]() 来做一些改进。——缺链接 已修改 叶挺 -->

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/ang.jpg)

在 Angular 项目在实际运用中，我们的项目需要根据不同的开发要求，对接不同后端 API。怎么通过单一的 Docker image 实现对接不同的后端 API 呢？

我们基于 [用 Docker 搭建 Angular 前端应用](../../docker-frontend/docker-angular) 来做一些改进。

gulp 是一个很好用的构建工具，不仅是因为他的语法灵活，更是因为有非常多的插件可供我们使用。在这个例子中，我们使用 [gulp-ng-config](https://www.npmjs.com/package/gulp-ng-config)。

### Angular 项目构建优化

**首先，安装插件 `gulp-ng-config`**。

```
npm install gulp-ng-config --save-dev
```

**接着，我们在 `/gulp/env.js` 文件下编写相应的 Task**。

```
gulp.task('env:config', function () {
  var env = process.env.APP_ENV || 'local';   // 暴露 APP_ENV 环境变零

  return gulp.src(
    path.join(conf.paths.src, '/config.json')
  )
    .pipe($.ngConfig('app.config', {
      environment: env
    }))
    .pipe(gulp.dest(path.join(conf.paths.tmp, '/serve/app/')));

});
```

**并将 `env:config` task 加入到 `inject` task (`/gulp/inject.js:12`) 之前**。
```
gulp.task('inject', ['scripts', 'styles','env:config'], function () { ...})
```

**然后，我们在 `/src/config.json` 文件下，不同的环境设置不同的 apiUrl**。

```
{
  "local": {
    "config": {
      "apiUrl": "http://api.angular-docker-sample.app/api/local"
    }
  },
  "test": {
    "config": {
      "apiUrl": "http://api.angular-docker-sample.app/api/test"
    }
  },
  "production": {
    "config": {
      "apiUrl": "http://api.angular-docker-sample.app/api/production"
    }    
  }
}

```

**最后，修改 `/src/index.module.js` 引入配置 module**。

```
(function() {
  'use strict';

  angular
    .module('angularDockerSample', [
        // core
        'app.config', // 这里是新添加的
        // vendor
        'ngAnimate', 
        'ngCookies', 
        'ngTouch', 
        'ngSanitize', 
        'ngResource', 
        'ui.router', 
        'ui.bootstrap'
        ]);

})();
```

### 构建 Docker Image

使用下面的 Dockerfile。

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

CMD gulp build && cp -r dist/* /usr/share/nginx/html/ && nginx -g 'daemon off;'
```

有了 Dockerfile 以后，我们可以运行下面的命令构建前端镜像并命名为 my-angular-api-app：

```bash
docker build -t my-angular-api-app .
```

### 部署 Docker Image

最后，让我们从镜像启动容器：

```
docker run -p 80:80 -e "APP_ENV=production" my-angular-api-app
```

这样子我们就能从 80 端口去访问我们的 Angular 应用，并且该 Angular 应用是对应着不同的 apiUrl。