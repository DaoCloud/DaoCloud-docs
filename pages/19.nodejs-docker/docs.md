---
title: 'Node.js 开发者的 Docker 之旅'
---

---

![Node.js](https://nodejs.org/static/images/logos/nodejs-2560x1440.png)

「**能用 JavaScript 编写的程序，都终将会以 JavaScript 编写。**」这句话曾经听起来十分高傲，但是随著 Node.js 的发展，我们渐渐地明白到这句话的远见性──JavaScript 真的越来越强大了。

Node.js 是一个非常新兴的开发工具，它诞生自 2009 年，年龄远不如 Python、Ruby、PHP 等老大哥，但是它确实有史以来发展最快的开发工具，没有之一。在这短短的几年间，我们看到了 Node.js 从当初的一无所有到如今的飞速发展，这是没有任何其他开发工具能够媲美的。

### 谁创造了 Node.js

Ryan Dahl，网名 ry，虽然如今已经没有多少人了解这一名字。是的，他就是 Node.js 的亲爹，我们依稀还记得那个安装 Node.js 需要执行这行命令的日子。

``` shell
$ git clone https://github.com/ry/node.git
```

### Node.js 的名字的由来？

其实 Node.js 最开始叫 「Web.js」（发布之前），后来因为 API 设计越来越庞大，ry 和他的团队依稀感觉到 Web.js 已经过于狭隘了，于是就有了现在的名字。

### Node.js 发展最快的是什么时候？

API 开始大面积进入 Stable 和 Locked 状态时，大批开发者便开始使用 Node.js 干各种事情，这个区间是 v0.6~v0.8 之间。Joyent 公司收购了 Node.js 原开发团队也是推动力之一。

### 为什么后来又出现了 Io.js？现在又到哪里去了？

Io.js 的出现是因为在 Node.js 的核心开发者群体中，出现了一些不太友好的性别歧视事件，导致核心开发组与 Joyent 公司决裂，直接从 Node.js 的 GitHub 代码库 Fork 了一个出来，并重命名为 Io.js。而很长一段时间内，Io.js 确实 Node.js 世界真正的主导，因为无论是核心开发者还是核心用户群都聚集在 Io.js 社区中，而且 Io.js 很大的优势便是原生开启 ES Harmony 支持模式，而不需要使用「`--harmony`」。

合久必分，分久必合。如今 Io.js 社区已经与 Joyent 公司达成共识，代码库再次回归到 Node.js 主线中来，Node.js 开发组委会也由原 Io.js 开发组和 Joyent 公司联合建立。

### NPM 现在是怎样的一种存在？

NPM 目前已经是一家独立的公司，由它的发明者 Issac 建立，是如今世界上最大的包管理平台之一，也是发展最快的一个。目前已有 **210,081** 个模块，每天下载次数达到 **83,000,000** 次。

### Node.js 究竟怎样的一个发展历程？

1. 混沌期：发布初期，创始人 Ryan Dahl 带著他的团队开发出了以 Web 为中心的“Web.js”，一切都是非常混乱，API大多都还除外研究阶段。
2. 成长期：Node.js 的核心用户 Isaac Z. Schlueter 开发出奠定了 Node.js 如今地位的重要工具--npm。同时也为他后来成为 Ryan 的接班人的重要条件。
3. 高速期：connect, express, socket.io 等库的出现吸引了一大波爱好者加入到 Node.js 开发者的阵营中来。CoffeeScript 的出现更是让不少 Ruby 和 Python 开发者找到了学习的理由。期间一大波以 Node.js 作为运行环境的 CLI 工具涌现，其中不乏有用于加速前端开发的优秀工具，如 less, UglifyJS, browserify, grunt 等等。Node.js 的发展势如破竹。
4. 更迭期：经过了一大批一线工程师的探索实践后，Node.js 也开始进入了时代的更迭期，新模式代替旧模式，新技术代替旧技术，好实践代替旧实践。ES6 也开始出现在 Node.js 世界中。
5. 分裂期：ES6 的发展越来越明显，v8 也对 ES6 中的部分特性实现了支持，如 Generator 等等，利用 `--harmony` 作为开启阀门。后来，诞生了 Io.js 分支，再后来也回到了 Node.js 主线上。
6. 飞速发展期：随著 ES2015 的发展和最终定稿，一大批利用 ES2015 特性开发的新模块出现，如原 [express](http://expressjs.com) 核心团队所开发的 [koa](http://koajs.com)。

### Node.js 适合做那些场景的开发？

Node.js 可以说是一种轻量的、可模块化的开发工具，就目前而言，它适合作为以下场景的开发工具：

1. Web 后端服务
2. Web API 服务
3. CLI 工具开发
4. 简易的 Native 应用开发

### Node.js Web 应用的运维部署

Node.js 的运维部署一直处在一个演变的进行时，从一开始的 `nohup` 原生命令，到利用 `supervisor` 工具，后来出现了 `forever`、`pm2`，还有以 Nginx 插件存在的 [Passion Passenger](https://www.phusionpassenger.com/)。

### Node.js 的运维压力

Node.js 与 Go、Java 等语言不同的是，JavaScript 是一门解析型语言，任何非语法上的错误在默认情况下都不会在被运行之前抛出，这就导致了 Node.js 的进程对于错误来说是脆弱的。所以我们需要一些“保姆进程”来保证进程的存活。

而且 Node.js 的环境部署虽然较几年前已经简单了非常多，但是依然是需要数次的等待。

### 有更好的办法吗？

当然有！Node.js 官方已经提供了 Node.js Docker 镜像，你可以直接从 DaoCloud 的镜像仓库中获取。

这里奉上使用 DaoCloud 构建 Node.js 应用的实例：[DaoCloud Node.js Example](https://coding.net/u/iwillwen/p/daocloud-example-repo/git)。