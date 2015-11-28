---
title: '「Allen 谈 Docker 系列」之一图看尽 docker 容器文件系统'
---

<!-- reviewed by fiona -->

>**「Allen 谈 Docker 系列」**

>DaoCloud 正在启动 Docker 技术系列文章，每周都会为大家推送一期真材实料的精选 Docker 文章。主讲人为 DaoCloud 核心开发团队成员 Allen（孙宏亮），他是 InfoQ 「Docker 源码分析」专栏作者，已出版《Docker 源码分析》一书。Allen 接触 Docker 近两年，爱钻研系统实现原理，及 Linux 操作系统。

---

**Dockerfile** 是软件的原材料，**Docker 镜像**是软件的交付品，而 **Docker 容器**则可以认为是软件的运行态。从应用软件的角度来看，**Dockerfile**、**Docker 镜像**与 **Docker 容器**分别代表软件的三个不同阶段，**Dockerfile** 面向开发，**Docker 镜像**成为交付标准，**Docker 容器**则涉及部署与运维，三者缺一不可，合力充当 Docker 体系的基石。

## Docker 镜像

Docker 镜像是 `Dockerfile` 的产物，是 Docker 容器的前提，大有承前启后之意。Docker 技术发展两年有余，相信大家很早就听说过 Docker 大多采用**联合文件系统**（Union Filesystem），为 Docker 容器提供文件系统服务。

关于 Docker 镜像，有以下特性：

- **由 `Dockerfile` 生成**
- **呈现层级结构**
- **每层镜像包含：镜像文件以及镜像 json 元数据信息**

## Docker 容器

Docker 容器是 Docker 镜像的运行态体现。概括而言，就是在 Docker 镜像之上，运行进程。进程启动的方式有两种，用户既可以选择运行自己另行指定的命令，也可以选择运行 Docker 镜像内部指定的命令。

Docker 容器的文件系统，可以说大部分由 Docker 镜像来提供。为什么说是大部分呢？其实是有原因的，镜像内容虽多，但依然不是全部。下面，我会带大家看看，Docker 镜像中有什么，而 Docker 容器的哪些内容不在 Docker 镜像中。

## Docker 容器文件系统

让我们一图看尽 Docker 容器的文件系统：

![Docker 容器文件系统](http://7xi8kv.com5.z0.glb.qiniucdn.com/一图看尽Docker容器文件系统.png)

上图从一个较为全面的角度阐述了 `Dockerfile`、Docker 镜像与 Docker 容器三者的关系。

#### Dockerfile 体现

Docker 容器已经在运行，但是追本溯源，我们依然可以找到 `Dockerfile` 的影子。上图中，我们可以发现，Docker 容器依附 Docker 镜像，而 Docker 镜像的 `Dockerfile` 是这样的：

```dockerfile
FROM ubuntu:14.04
ADD run.sh /
VOLUME /data
CMD ["./run.sh"]
```

我们可以看到，以上 `Dockerfile` 中的每一条命令，都在 Docker 镜像中以一个独立镜像层的形式存在。

#### Docker 镜像体现

毫无疑问，Docker 镜像是由 `Dockerfile` 构建而成，我们也可以看到图中下四层被标记为 Docker 镜像。作为 Docker 技术的核心，我们必须了解 Docker 如何构建镜像，以及 Docker 镜像构建之后的产物是什么。

初次接触 Docker，了解层级管理的 Docker 镜像之后，很容易就认为：每一层 Docker 镜像中都含有相应的文件系统文件。其实不然，以上 `Dockerfile` 中的四条命令，则是一个很好的佐证。

- **`FROM ubuntu:14.04`**：设置基础镜像，此时会使用基础镜像 `ubuntu:14.04` 的所有镜像层，为简单起见，图中将其作为一个整体展示。
- **`ADD run.sh /`**：将 `Dockerfile` 所在目录的文件 `run.sh` 加至镜像的根目录，此时新一层的镜像只有一项内容，即根目录下的 `run.sh`。
- **`VOLUME /data`**：设定镜像的 `VOLUME`，此 `VOLUME` 在容器内部的路径为 `/data`。需要注意的是，此时并未在新一层的镜像中添加任何文件，但更新了镜像的 json 文件，以便通过此镜像启动容器时获取这方面的信息。
- **`CMD ["./run.sh"]`**：设置镜像的默认执行入口，此命令同样不会在新建镜像中添加任何文件，仅仅在上一层镜像 json 文件的基础上更新新建镜像的 json 文件。

#### Docker 容器体现

涉及到 Docker 容器，便是动态的内容，一切似乎都有了生命。上文曾提及，Docker 容器的文件系统中不仅包含 Docker 镜像。此言不虚，图中的顶上两层，就是 Docker 为 Docker 容器新建的内容，而这两层恰恰不属于镜像范畴。

这两层分别为 Docker 容器的初始层（Init Layer）与可读写层（Read-Write Layer），初始层中大多是初始化容器环境时，与容器相关的环境信息，如容器主机名，主机 host 信息以及域名服务文件等。

再来看可读写层，这一层的作用非常大，Docker 的镜像层以及顶上的两层加起来，Docker 容器内的进程只对可读写层拥有写权限，其他层对进程而言都是只读的（Read-Only）。如 AUFS 等文件系统下，写下层镜像内容即会涉及 `COW` （Copy-on-Write）技术。另外，关于 `VOLUME` 以及容器的 `hosts`、`hostname`、`resolv.conf` 文件等都会挂载到这里。需要额外注意的是，虽然 Docker 容器有能力在可读写层看到 `VOLUME` 以及 `hosts` 文件等内容，但那都仅仅是挂载点，真实内容位于宿主机上。

## 总结

Docker 镜像属静态，Docker 容器属动态，两者之间有着千丝万缕的关系。从 Docker 容器文件系统的角度来认识两者，我相信会对大家有很大的帮助。

Docker 镜像以及 Docker 容器文件系统，绝对是非常细致的内容，基于这些概念，实在有太多有意思的话题可以展开，本系列后续会有以下多篇文章来分析：

1. 深刻理解 Docker 镜像大小
2. 其实 `docker commit` 很简单
3. 不得不说的 `docker save` 与 `docker export` 区别
4. 为什么有些容器文件动不得
5. 打破 `MNT Namespace` 的容器 `VOLUME`

**欲知 Docker 镜像更精彩的内容，请关注「Allen 谈 Docker 系列」，且听下回分解**