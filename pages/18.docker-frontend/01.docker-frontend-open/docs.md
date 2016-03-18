---
title: '前端开发者的 Docker 之旅－开篇'
---

<!-- reviewed by fiona -->

<!--「**JavaScript：世界上最被误解的语言**」这句话源自——说了半句，不完整，经考证，应该是来自 Douglas Crockford 的博客文章 http://javascript.crockford.com/zh/javascript.html -->

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/dalibao.jpg)

「Docker 开发大礼包」已经到了第三季。

「**JavaScript：世界上最被误解的语言**」这句话源于 JSON 的创建者 Douglas Crockford 的博客文章 「JavaScript:
The World's Most Misunderstood Programming Language」。JavaScript 的前缀很容易使人联想到 Java，并认为它是 Java 的子集或简化版的 Java。看起来最初给它选这个名字是别有用心的，是故意混淆概念，故意制造「误解」的。

前端其实是一个非常古老的话题，它的故事几乎伴随着 Web 技术发展的各个阶段，也同样经历了跌宕起伏、涅槃重生的激荡三十年。毫不夸张的说，前端的演化历史和成功，是工程师不断突破桎梏、迈向本我的探索旅程。


#### 前端出现在什么时候？

在 Web 技术出现的那一刻，前端一直伴随着 Web 技术的发展演化。可以说是 Web 技术的鼻祖。

#### 前端是由什么语言组成的？

前端开发技术，从狭义的定义来看，是指围绕 HTML、JavaScript、CSS 这样一套体系的开发技术，它的运行宿主是浏览器。

#### 前端最具代表性的技术革新在什么时候？

历史滚滚往前，2004 年 Gmail 像风一样的女子来到人间，很快 2005 年 Ajax 正式提出，加上 CDN 开始大量用于静态资源存储，于是出现了 JavaScript 王者归来的 SPA （Single Page Application 单页面应用）时代。

#### 下一个 JavaScript 版本？

ECMAScript 2015（亦称 ECMAScript Harmony，简称 ES2015）

#### 谁在主导前端的方向？

Facebook、Google

#### Angular 又是什么？

最好用的前端开发框架（仅代表 DaoCloud 意见）

#### 前端的包依赖怎么做？

NPM

#### 前端技术发展的下一阶段

Node 带来的全栈时代

#### 常见的前端技术栈和应用场景？

2015 年某宝双十一访问到的所有 www 域页面（包括首页、频道、会场等）全部是一个全栈 node 应用支撑的（[出处](http://www.zhihu.com/question/37379084)）。

#### 前端运维部署

自动化构建，甚至利用 Nginx 层解决前端一些硬伤，发布/回滚速度（包含编译）只需要 100s 发布到全部生产环境机器，供快速响应、迭代。

#### 前端的烦恼

然而，前端代码的交付并不是 copy 和 paste 这么简单，代码发布之前的前端构建、跟测试和生产环境不同 API 的对接、JS 代码混淆、不同发布分支的管理等等，这些体力劳动，每次发布时，都是挑起前端和运维团队大战的导火线。前端技术已经越发复杂，前端工程师并不希望把有限的生命花费在分发复杂应用的交付流程性的事物上！

#### 那怎么破的，能教教吗？

上 Docker!

欢迎进入由 DaoCloud 推出的「Docker 开发大礼包」第三季「前端应用 Docker 开发大礼包」，七篇由浅入深、精心设计的系列文章，将带领前端开发者领略 Docker 化应用开发和发布的全新体验。


* [运维也学学前端，那天下就太平了](../../docker-frontend/frontend-docker-together)
* [Hello Docker](../../docker-frontend/hello-docker)
* [Docker 和 Node Express 应用](../../docker-frontend/docker-node-express)
* [用 Docker 搭建 Angular 前端应用](../../docker-frontend/docker-angular)
* [Angular 应用根据环境变量切换不同的后端 API](../../docker-frontend/angular-api)
* [Angular 应用根据环境变量切换不同的 CDN](../../docker-frontend/angular-cdn)
* [Angular 应用 Docker 启动加速](../../docker-frontend/angular-docker)
