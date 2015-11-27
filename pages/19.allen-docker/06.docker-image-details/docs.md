---
title: '「Allen 谈 Docker 系列」之 Docker 镜像内有啥，存哪？'
---

<!-- reviewed by fiona -->

<!--Docker 均为将其在 json 文件中更新。均未 or 均为-->

>**「Allen 谈 Docker 系列」**

>DaoCloud 正在启动 Docker 技术系列文章，每周都会为大家推送一期真材实料的精选 Docker 文章。主讲人为 DaoCloud 核心开发团队成员 Allen（孙宏亮），他是 InfoQ 「Docker 源码分析」专栏作者，已出版《Docker 源码分析》一书。Allen 接触 Docker 近两年，爱钻研系统实现原理，及 Linux 操作系统。

---

据说重要的事情要说三遍，那我再表述一下个人观点：`Docker 镜像`是 Docker 的灵魂所在。

前两讲关于 Docker 镜像的描述，已经从宏观的角度涉及一二。一旦掌握 Docker 对于镜像的层级管理方式，以及 Docker 镜像大小的真实情况之后，再来了解 Docker 镜像包含的内容以及存储，就显得简单很多。

## Docker 镜像内容

对于 Docker 镜像的认识总会有第一次，自那时开始，当然也少不了成长，笔者本人的认识过程不妨和大家一起分享：

1. **初次接触 Docker**：相信很多爱好者都会和我一样，有这样一个认识：Docker 镜像代表一个容器的文件系统内容；
2. **初步接触联合文件系统**：联合文件系统的概念，让我意识到镜像层级管理的技术，每一层镜像都是容器文件系统内容的一部分。
3. **研究镜像与容器的关系**：容器是一个动态的环境，每一层镜像中的文件属于静态内容，然而 `Dockerfile` 中的 `ENV`、`VOLUME`、`CMD` 等内容最终都需要落实到容器的运行环境中，而这些内容均不可能直接坐落到每一层镜像所包含的文件系统内容中，那这部分内容 Docker 该如何管理？

另外，在上述第三个步骤中，还有一种情况，相信大家并不陌生，很多个镜像层大小为 0，镜像层内部不存在任何文件内容。这又是怎么一回事？

大家可以回忆一下《一图看尽 Docker 容器文件系统内容》中，关于空镜像的生成部分，其中提到「更新镜像的 json 文件」。其实，前文埋下的伏笔，即暗示了真相—— **Docker 镜像内容由`镜像层文件内容`和`镜像 json 文件`组成**，不论静态内容还是动态信息，Docker 均为将其在 json 文件中更新。

Docker 每一层镜像的 json 文件，都扮演着一个非常重要的角色，其主要的作用如下：

1. **记录 Docker 镜像中与容器动态信息相关的内容**
2. **记录父子 Docker 镜像之间真实的差异关系**
3. **弥补 Docker 镜像内容的完整性与动态内容的缺失**

Docker 镜像的 json 文件可以认为是镜像的元数据信息，其重要性不言而喻，本系列将在下一篇文章重点分析 Docker 镜像 json 文件。敬请期待。

## Docker 镜像存储位置

Docker 镜像内容的理论分析，看着多少有些云里雾里，不论 Docker 镜像层的文件，还是 json 文件，读来都稍显乏味。倘若可以一窥 Docker 中的真实环境，相信对于镜像技术的理解定会有不少的帮助。

我们直奔主题，从 Docker 镜像的存储入手，看看这些`镜像层文件内容`与`镜像 json 文件`分别存储于何处。（以下展示的实验环境：宿主机操作系统为 Ubuntu 14.04、Docker 版本为 1.7.1、graphdriver 类型为 aufs，仅包含 `ubuntu:14.04` 一个镜像。）

### 查看镜像层组成

我们可以通过命令 `docker history ubuntu:14.04` 查看 `ubuntu:14.04`，结果如下：

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/docker_history.jpg)

图中显示 `ubuntu:14.04` 镜像共有 4 个镜像层。

### 镜像层文件内容存储

Docker 镜像层的内容一般在 Docker 根目录的 aufs 路径下，为 `/var/lib/docker/aufs/diff/`，具体情况如下：

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/images.jpg)

图中显示了镜像 `ubuntu:14.04` 的 4 个镜像层内容，以及每个镜像层内的一级目录情况。需要额外注意的是，镜像层 `d2a0ecffe6fa` 中没有任何内容。

### 镜像 json 文件存储

对于每一个镜像层，Docker 都会保存一份相应的 json 文件，json 文件的存储路径为 `/var/lib/docker/graph`，`ubuntu:14.04` 所有镜像层的 json 文件存储路径展示如下：

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/jsons.jpg)

除了 json 文件，大家还看到每一个镜像层还包含一个 layersize 文件，该文件主要记录镜像层内部文件内容的总大小。既然谈到了镜像 json 文件，为了给下文铺垫，以下贴出 `ubuntu:14.04` 中空镜像层 `d2a0ecffe6fa` 的 json 文件：

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/empty_json.jpg)

由于该镜像层的对应的 `Dockerfile` 指令为 `CMD`，所以镜像层的内容为空，而改镜像层的 json 文件会更新 Cmd 域，获取新的 Cmd 值，以便后续通过该镜像运行容器时，使用更新后的 Cmd。

## 总结

联合文件系统的使用，是 Docker 镜像技术的精髓，然而除此之外，对于镜像的元数据管理（即镜像 json 文件）打通了 Docker 镜像直接运行 Docker 容器的捷径。

**欲知 Docker 镜像更精彩的内容，关注「Allen 谈 Docker 系列」，且听下回分解：深入理解 Docker 镜像 json 文件。**