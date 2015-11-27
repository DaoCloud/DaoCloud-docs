---
title: '「Allen 谈 Docker 系列」docker commit 的来龙去脉'
---

<!-- reviewed by fiona -->

>**「Allen 谈 Docker 系列」**

>DaoCloud 正在启动 Docker 技术系列文章，每周都会为大家推送一期真材实料的精选 Docker 文章。主讲人为 DaoCloud 核心开发团队成员 Allen（孙宏亮），他是 InfoQ 「Docker 源码分析」专栏作者，已出版《Docker 源码分析》一书。Allen 接触 Docker 近两年，爱钻研系统实现原理，及 Linux 操作系统。

---

相信无需再强调 Docker 镜像，大家都已经清楚 Docker 除了传统的 Linux 容器技术之外，还有另辟蹊径的镜像技术。镜像技术的采用，使得 Docker 自底向上打包一个完整的应用，将更多的精力专注于应用本身；而容器技术的延用，则更是在应用的基础上，囊括了应用对资源的需求，通过容器技术完成资源的隔离与管理。

Docker 镜像与 Docker 容器相辅相成，共同作为技术基础支撑着 Docker， 为 Docker 的生态带来巨大的凝聚力。然而，这两项技术并非相互孤立，两者之间的互相转换使得 Docker 的使用变得尤为方便。说到，Docker 镜像与 Docker 容器之间的转化，自然需要从两个角度来看待：从 Docker 镜像转化为 Docker 容器一般是通过 docker run 命令，而从 Docker 容器转化为 Docker 镜像，则完全依靠 `docker commit` 的实现。

## docker commit 的作用

是否还记得 `docker build` 的实现？Dockerfile 唯一的定义了一个镜像，`docker build` 对于 Dockerfile 中的每一条命令都会创建一个单独的镜像（包含镜像层内容和镜像 json 文件），最终产生一个含有标签（tag）的镜像，而之前与 Dockerfile 命令对应的镜像均是这个含有 tag 的镜像的祖先镜像。如以下 Dockerfile：

```
FROM ubuntu:14.04 
RUN apt-get update 
ADD run.sh /  
VOLUME /data  
CMD ["./run.sh"]  
``` 
`docker build` 实现 Dockerfile 到 Docker 镜像的构建，而对于单条 Dockerfile 中的命令（如命令`RUN apt-get update` ），则是通过针对 Docker 容器的 commit 操作，实现将其构建为单层镜像，也就是大家熟悉的 `docker commit` 操作。简单的示意图如下：


![image](http://7xi8kv.com5.z0.glb.qiniucdn.com/docker_commit.jpg)

## docker commit 的原理

深入学习`docker commit`的原理前，我不妨先来看看一下 `docker help` 中关于 commit 命令的阐述：

```
commit    Create a new image from a container's changes
```

结合上图与命令`docker commit`的描述，我们可以发现有三个关键字`Image`、`Container`与`Changes`。如何理解这三个关键字，我们可以从以下三个步骤入手：

**1. Docker Daemon 会通过一个 Docker 镜像运行一个 Docker 容器，Docker 通过层级文件系统为 Docker 容器提供文件系统视角，最上层的是可读可写层（Read-Write Layer）。**

**2. Docker 容器初始的可读可写层内容均为空，Docker 容器对文件系统的内容更新将全部更新于可读可写层（Read-Write Layer）。**

**3. 实现 docker commit 操作时，Docker 仅仅是将可读可写层（Read-Write Layer）中的更新内容，打包为一个全新的镜像。**

具体的 docker commit 示意图如下：
![image](http://7xi8kv.com5.z0.glb.qiniucdn.com/docker_commit_all.jpg)

观察上图，我们可以发现：对于 commit 命令，几乎所有的操作都围绕着可读可写层（Read-Write Layer），一次 commit 将可读可写层打包为一个全新的镜像，同时也保证镜像之间的独立性。当然，由于一个镜像同时包含镜像层文件系统内容和镜像 json 文件，因此对于一个 commit 操作，Docker Daemon 还会为镜像产生一个全新的 json 文件。

结合上图，我们也看到 `docker commit`命令也会有一些注意事项，最为重要的是：`docker commit 命令仅仅打包可读写写层内容`。对于 Docker 容器而言，文件系统视角包含的内容有 Docker 镜像构成的内容（一个可读可写层加上多个只读层）、数据卷 VOLUME 挂载的目录内容，还有类似于 hosts、hostsname 和resolv.conf 等挂载文件，当然还有一些如 /proc 和 /sys 等虚拟文件系统的内容。commit 操作只专注于可读可写层（Read-Write Layer），因此其他的内容都将不会出现在打包后的镜像中。举例说明，类似于 MySQL 的数据容器，由于其自身的数据一般都持久化到数据卷 VOLUME 中，因此 MySQL在运行过程中产生的数据将不会在 commit 操作后被打包进入镜像。

## 从 docker commit 看 build 注意事项

命令`docker commit`可以实现将一个运行中容器的可读写层，打包为一个镜像。对于 Dockerfile 中的 `RUN` 命令，Docker的机制同样如此，主要的步骤如下：

**1.以一个容器的形式运行 RUN 关键字后紧跟的命令，假设为 command；**

**2.运行命令 command 时，容器对文件系统的所有更新都将体现在容器的可读写层上；**

**3.Docker 守护进程等待并判断命令 command 运行后的返回状态；**

**4.若 command 返回状态为0，则表示命令运行完成，Docker 守护进程打包可读写层，创建并提交新镜像；**

**5.若 command 返回状态非0，则表示命令未正常运行，构建流程失败，留下构建失败现场；**

**6.若 command 将无休止运行，则此次构建操作也将永远进行，同样不是一个成功的构建。**

以上步骤完整的展现了 Dockerfile 中 RUN 命令的操作流程，说到注意事项，大家有必要将目光聚焦于两个关键词`「容器」`与`「返回状态」`。一旦缺乏对这两个关键词的认识，很容易在镜像构建过程中遇到棘手的问题。

首先，从`容器`的角度谈注意事项。谈到容器，大家第一印象自然是`docker run `运行的容器，很难想到`docker build`的世界中也会存在容器的概念。既然如此，前者的容器应该受到资源的限制，大家应该不难理解，本身`docker run`命令有诸多的参数来限制容器资源。那么，大家是否应该想到，后者`docker build`构建流程中的容器同样应该受到相应的资源限制呢？一旦`docker build`过程中容器运行的命令将占用大量的资源，隔离效果不佳的情况下，很难保证宿主机上其他任务的正常运行。因此，这一点不得不防。在早版本的 Docker 中,`docker build`命令不支持任何的资源限制，自然很难达到生产化的要求。随着 Docker 的发展，新版本中逐渐加入了对部分资源的限制，改善了隔离的现状，但是依然没有达到`docker run`的隔离程度，另外除了资源之外，`docker build`还缺少对容器权限以及能力的管理，如 Linux Capabilities。

再者，我们从`返回状态`的角度谈注意事项。返回状态包括三种情况，0、非 0、无返回状态。返回状态为 0 的情况，皆大欢喜；返回非 0，那就是命令的运行出现了异常。异常之下，尤其需要注意失败现场。当前命令的构建失败意味着整个 `docker build` 命令的运行失败，当前命令的构建失败将导致当前的镜像层没有成功构建。然而对于已经成功构建的镜像层，Docker 守护进程并不会对其做任何的处理。在主机管理员没有意识的情况下，如果出现大量的构建失败，很有可能导致主机磁盘的无辜消耗，最终殆尽。无返回状态，同样是一件令人头疼的事。命令较长时间处于运行中，我们也无法确定程序是否进入死循环，带来的不确定性既会占用资源，同样也给运维带来极大的不便。

## 总结

笔者一直认为，深入理解 Docker 的原理，必须从 `docker build` 命令入手，而 `docker commit` 又是 `docker build` 的实现原型。原因很简单，这两个命令打通了 Dockerfile 到 Docker 容器，再到 Docker 镜像的整个流程，几乎涵盖了 Docker 中所有的概念，实属深入学习 Docker 的必经之路。
