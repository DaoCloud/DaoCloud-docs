---
title: 'Angular 应用 Docker 启动加速'
---

<!-- reviewed by fiona -->

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/ang.jpg)

在 Angular 项目在实际运用中，我们的项目需要根据不同的开发要求，对接不同后端 API。怎么通过单一的 Docker image 实现对接不同的后端 API 呢？

这里我们给出了答案：[Angular 应用根据环境变量切换不同的后端 API](../angular-api)。

但是这样做导致了 Docker 启动时要经过一段时间的前端项目的构建，牺牲了 Docker 秒级启动的特性。针对此，我们继续对这个流程进行优化。做到 Docker 秒级启动。

思路很简单，就是把耗时的事情，放在 Docker Build 的时候做。

### Angular 项目构建优化

**首先，我们对 `/src/config.json` 文件，添加了 `needReplace`**。

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
  },
  "needReplace": {
    "config": {
      "apiUrl": "THIS_IS_API_URL_NEED_REPLACE"
    }
  }
}
```

**接着，我们修改 `/gulp/env.js` 文件，将 `env:config` 默认配置设置成 `needReplace`**。

添加 `env:replace` task ，将 `cdn` task 作为前置条件

```
gulp.task('env:config', function () {
  var env = process.env.APP_ENV || 'needReplace'; // 修改了这里

  return gulp.src(
    path.join(conf.paths.src, '/config.json')
  )
    .pipe($.ngConfig('app.config', {
      environment: env
    }))
    .pipe(gulp.dest(path.join(conf.paths.tmp, '/serve/app/')));

});

gulp.task('env:replace', ['cdn'], function () {
  var envConfig   = jsonfile.readFileSync(path.join(conf.paths.src,
    '/config.json'));
  var needReplace = envConfig.needReplace;
  var env         = process.env.APP_ENV || 'local';

  var stream = gulp.src(
    path.join(conf.paths.dist, '/scripts/*.js')
  );
  for (var key in needReplace.config) {
    stream = stream.pipe(
      $.replace(
        needReplace.config[key],
        envConfig[env]['config'][key])
    );
    console.log(key, needReplace.config[key]);
    console.log(key, envConfig[env]['config'][key]);
  }

  return stream.pipe(gulp.dest(path.join(conf.paths.dist, '/scripts')));

});
```

### 构建 Docker Image

**Dockerfile**

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

RUN gulp build 

CMD gulp env:replace && cp -r dist/* /usr/share/nginx/html/ && nginx -g 'daemon off;'
```

有了 Dockerfile 以后，我们可以运行下面的命令构建前端镜像并命名为 my-angular-app：

```bash
docker build -t my-angular-app .
```

### 部署 Docker Image

**最后，让我们从镜像启动容器**：

```
docker run -p 80:80 -e "APP_ENV=production" my-angular-app
```

这样的我们的 Angular 项目的启动速度就达到了秒级。
