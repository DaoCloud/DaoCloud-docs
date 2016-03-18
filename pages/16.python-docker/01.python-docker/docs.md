---
title: 'Python 开发者的 Docker 之旅－开篇'
taxonomy:
    category:
        - docs
process:
    twig: true
---

<!-- reviewed by fiona -->

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/python900-500.jpg)

「**人生苦短，我用 Python**」这句话用作「Docker 开发大礼包」第二季的开篇引言是再合适不过了。这句话的出处是 Bruce Eckel，对，就是那个 C++ 和 Java 生命里最重要那个男人。这大概就是传说中的大是大非之后痛彻心扉的领悟。

Python 其实是一门非常古老的语言，他的故事几乎伴随着我国改革开放的历史步伐一路走来，也同样经历了跌宕起伏、涅槃重生的激荡二十年。毫不夸张的说，Python 的演化历史和成果，是程序员自强不息摆脱机器思维，迈向本我的探索旅程。

##### 谁创造了 Python？

Guido van Rossum，荷兰人。在这个诞生了梵高和克鲁伊夫的国家，1989 年，因为圣诞节过于寂寞难耐，有个百无聊赖的年轻人创造了一个新的脚本语言。

##### Python 是什么的缩写？

不是缩写。因为作者 Guido 当时在看一部叫「Monty Python's Flying Circus」的英国腐剧，因此得名。

##### Python 最著名的版本？

Python 2.0 于 2000 年 10 月 16 日发布，实现了完整的垃圾回收，并且支持 Unicode。以此为契机，开发过程变的更加透明，社区对开发进度的影响逐渐扩大。

##### 下一个 Python 版本？

Python 3.5

##### Python 的形象代言人？

两条盘在一起的蟒蛇，小蓝在上面，小黄在下面。

##### 谁在主导 Python 的方向？

Guido，Python 的神和独裁者。

##### Flask 又是什么？

最好用的 Python Web 开发框架（仅代表 DaoCloud 意见）

##### Python 的包依赖怎么做？

pip（Python Package Index）

##### Python 的单元测试怎么做？

unittest

##### 常见的 Python 技术栈和应用场景？

Python 是动态语言的启蒙，常年作为 Google 的主要开发语言。Dropbox 的完整技术栈都是基于 Python，后来他们从 Google 挖走了 Guido。

Web 2.0 时代，豆瓣在洪教授的带领下，完成了对中国互联网技术圈的 Python 启蒙。

##### 都是动态语言，Python 和 Ruby 有什么区别？

Python 的设计哲学是「用一种方法，最好是只有一种方法来做一件事」，因此代码具备高度的可阅读性。

Ruby 对以上两点持保留意见。

##### 就 Python 趋势，Guido 怎么看？

> In my daily work, I work on very large, complex, distributed systems built out of many Python modules and packages. The focus is very similar to what you find, for example, in Java and, in general, in systems programming languages.

##### 那怎么破的，能教教吗？

上 Docker!

欢迎进入由 DaoCloud 推出的「Docker 开发大礼包」第二季「Python 应用 Docker 开发大礼包」，四篇由浅入深、精心设计的系列文章，将带领 Python 开发者领略 Docker 化应用开发和发布的全新体验。

* [如何开发一个基于 Docker 的 Python 应用（一）](../../python-docker/docker-python-001)
* [如何制作一个定制的 Python 基础 Docker 镜像（二）](../../python-docker/python-docker-002)
* [如何用 Docker Compose 配置 Django 应用开发环境（三）](../../python-docker/docker-compose-django)
* [如何构建具有持续交付能力的 Docker 化 Django 应用（四）](../../python-docker/docker-django)