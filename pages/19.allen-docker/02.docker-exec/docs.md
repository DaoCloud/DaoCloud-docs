---
title: '「Allen 谈 Docker 系列」之 docker exec 与容器日志'
---

<!-- reviewed by fiona -->

>**「Allen 谈 Docker 系列」**

>DaoCloud 正在启动 Docker 技术系列文章，每周都会为大家推送一期真材实料的精选 Docker 文章。主讲人为 DaoCloud 核心开发团队成员 Allen（孙宏亮），他是 InfoQ 「Docker 源码分析」专栏作者，已出版《Docker 源码分析》一书。Allen 接触 Docker 近两年，爱钻研系统实现原理，及 Linux 操作系统。

---

翻看 Docker 的历史，您会发现 Docker 一直在强调「Application」一词，Docker 也希望能为分布式应用提供容器化的解决方案。

从 Docker 化应用软件的生命周期来看，开发工作似乎位于 Docker 的构建之前，而后容器化的测试、部署与运维都与 Docker 容器息息相关。不得不说，Docker 思维下的应用软件，管理流程与传统场景有着很大的区别。

最大的区别当属 Docker 容器运行环境的封闭性。单一应用的运行，使得容器内部缺少功能丰富的服务。虽然用户可以通过 Docker 的层面，获取部分容器的信息，但是依然无法直接获悉应用内部的状态信息（虽然 Docker 倡导容器运行无状态的应用），比如应用容器内部持久化的日志文件、应用容器内部的临时存储等等。而这些信息在传统模式下，都可以较为轻易的获取。

为了缓解容器运行环境封闭性带来的使用障碍，Docker 提供了 `docker exec` 命令，方便用户在容器之外让容器执行指定的命令，以实现用户的需求。

今天你 `docker exec` 了吗？如果还没有的话，灵活穿越容器的感觉你值得拥有；如果有的话，那下面这些内容你不得不看。

## 1. 容器进程树与 docker exec

随着 Docker 的普及，相信越来越多的 Docker 爱好者已经意识到：

（1）Docker 容器其实就是若干进程构成；

（2）而「一般情况下」这些进程呈现出「树状」关系；

（3）容器内 pid 为 1 的进程为容器主进程；

（4）一旦容器主进程退出，容器内所有进程退出。

其实，在 Docker 1.3 之前还不支持 `docker exec` 的时候，以上观点鲜有不妥，但是现在的情况却已然不同，且看下图：

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/docker_exec-2.png)

## 2.docker exec 原理与容器日志

简述上图中 docker exec 的原理可以理解为以下两个步骤：

（1）Docker Daemon 创建一个用户指定的进程 `/bin/bash`，因此 `/bin/bash` 的父进程为 Docker Daemon；

（2）Docker Daemon 为进程 P5 设定限制，如：加入容器主进程 P1 所在的隔离环境（namespaces），与其他进程一样受到资源限制（cgroups）等。

观察上图，分析原理，不难发现，容器内部的进程关系已然不是树。然而，为什么总是强调「树状「」关系呢？答案是：树状的继承关系，有利于容器管理。以上文《docker logs 实现剖析》中卖的关子「docker exec 的标准输出不会作为容器日志」为例，Docker Daemon 创建容器主进程时，负责接管主进程的标准输出，从而保证容器主进程下所有进程的标准输出被接管，然而 Docker Daemon 在新创建 `docker exec` 所需执行的进程时，后者的标准输出并未与容器主进程作关联，也并未被 Docker Daemon 特殊处理，故 `docker exec` 所执行进程的标准输出不会进入容器的日志文件中。

虽然 `docker exec` 所执行的进程也是容器的一部分，但是更准确的理解 Docker 容器的日志，可以是这样子的：Docker 容器的日志只负责应用本身的标准输出，不包括 `docker exec` 衍生进程的标准输出。

虽然本文标题与日志相关，但是几乎都在谈论 `docker exec`，既然说到，不妨在这个屡试不爽的命令上提个醒：

（1）`docker exec` 完成容器内外的交互，但希望完成大量标准输出时需谨慎；

（2）每次 `docker exec`，Docker Daemon 均会记录一次 execID，切忌过于频繁。


从描述 `docker exec` 的原理到引入容器日志的一些小 trick，再加上前文的 docker logs 分析，相信很多人都会觉得对 Docker 容器的日志有了一个较为完整的认识。

然而，笔者却有不同的看法。应用 Docker 化之后，日志依然是一件非常棘手的事。笔者认为：容器内部日志文件 `app.log` 与 `docker logs` 依然无法满足传统模式下对日志的需求。

欲知后事如何，请关注「Allen 谈 Docker 系列」，且听下回《Docker 容器日志完结篇》分解。