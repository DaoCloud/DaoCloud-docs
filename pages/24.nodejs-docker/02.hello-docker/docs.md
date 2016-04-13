---
title: 'Hello Docker'
---

---
Node.js 官方在 Docker 成为主流容器化解决方案之后，便随即发布了官方的 Node.js Docker 镜像，并保持著与最新的 Node.js 版本同步更新，这说明了 Docker 已成为了大部份 Web 工程师中的一把利剑。

接下来，我们以一个简单的例子，看看要如何使用 Node.js Docker 镜像，将我们的 Node.js 应用 **Dockerify**，走上容器化之路。

### 第一步：准备 Node.js 程序

和以前的 Node.js 开发流程一样，我们首先要准备好 Node.js 应用的配置。

``` shell
$ mkdir -p node-docker-example
$ cd node-docker-example
```

我们开始编写主要的程序：

``` javascript
// server.js
var http = require('http')

var server = http.createServer(function(req, res) {
  res.writeHead(200, {
    'Content-Type': 'text/plain'
  })
  res.end('Hello World!')
})

server.listen(8080, function() {
  console.log('Docker DEMO with Node.js is running.')
})
```

运行这段代码，并在浏览器中打开 `http://localhost:8080/` 就能看到 `Hello World!` 字样。

### 第二步：扩展程序内容

这样的程序不能满足？那么我们来一段比较有意思的吧~

为了保持程序的简洁性，我们就写一段简易的路由器吧，以实现简单的 URL 分开处理。

``` javascript
function router(routes) {
  var paths = Object.keys(routes)
  var regexes = paths.map(function(path) {
    return new RegExp('^' + path + '$')
  })

  return function(req, res) {
    var i = 0
    while (!regexes[i].test(req.url)) i++
    return routes[paths[i]].call(null, req, res)
  }
}
```

通过这段简单的程序，我们可以实现下面这种功能：

``` javascript
var server = http.createServer(router({
  '/': function(req, res) {
    res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.end('Hello World!')
  },
  '/bye': function(req, res) {
    res.writeHead(200, { 'Content-Type': 'text/plain' })
    res.end('Bye~')
  }
}))
```

然后我们可以给该项目添加 Node.js Package 配置文件了。

``` shell
$ npm init -y
```

### 第三步：编写 Dockerfile

Dockerfile 是一个 Docker 镜像的核心部件，所有的构建、运行入口、容器配置都依赖于它。

>>>>> 详细的 Dockerfile 编写教程可以参见「[Dockerfile 的结构和写法](http://docs.daocloud.io/ci-image-build/dockerfile)」。

首先我们从 DockerHub 拉取一个 Node.js 的官方 Docker 镜像，作为我们的环境基础镜像。

``` 
FROM node:4.2.2
```

然后创建一个位于容器内部的代码运行文件夹，并将代码复制进去，且通过 [npm](http://npmjs.com) 来安装依赖包。

``` 
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app
```

我们部署的是一个 HTTP 服务，所以为了更好地体现出功能，我们通过 Docker 的端口暴露功能，为程序提供一个 80 端口作为 HTTP 服务端口。

``` 
EXPOSE 80
```

最后通过 `ENTRYPOINT` 指令，让 Node.js 程序作为该 Docker 镜像的主运行入口，并将其运行起来。

``` 
ENTRYPOINT node server.js
```

### 第四步：上传至 GitHub

为了能让 Docker 镜像通过 DaoCloud 进行自动构建，我们需要将代码发布到第三方代码托管平台上，此处我们以 GitHub 做为简单例子。

首先先在代码目录中初始化 Git。

``` shell
$ git init
```

然后添加好 GitHub 的仓库信息，并将其推送上去。

``` shell
$ git remote add origin git://github.com:example/daocloud-node.git
$ git add .
$ git commit -m 'Example init'
$ git push -u origin master
```

### 第五步：通过 DaoCloud 进行构建并部署

将代码上传到 GitHub 以后，就可以通过 DaoCloud 进行镜像构建和应用部署了。

1. 将 DaoCloud 账号与 GitHub 账号进行绑定的方法，请参见：「[与 GitHub 代码源绑定](http://docs.daocloud.io/ci-on-daocloud/github)」。
2. 使用 DaoCloud 进行代码构建的方法，请参见：「[开始持续集成和镜像构建](http://docs.daocloud.io/ci-image-build/start-ci-and-build)」。
3. 查看通过 DaoCloud 进行镜像构建的镜像，请参见：「[我的镜像](http://docs.daocloud.io/daocloud-registry/pull-push)」。
4. 希望免费尝试通过 DaoCloud 进行应用部署，请参见：「[添加胶囊主机](http://docs.daocloud.io/cluster-mgmt/add-cell-node)」。
5. 若希望通过 DaoCloud 快速部署应用所需的数据库或持续化服务，请参见：「[如何在容器中实现数据持久化](http://docs.daocloud.io/daocloud-services/save-data-in-container)」。
6. 通过 DaoCloud 向自由主机进行快速应用部署，请参见：「[向自有主机集群上发布应用](http://docs.daocloud.io/app-deploy-mgmt/deploy-to-cluster)」。