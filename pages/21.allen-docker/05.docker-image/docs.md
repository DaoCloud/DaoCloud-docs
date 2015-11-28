---
title: '「Allen 谈 Docker 系列」之深刻理解 Docker 镜像大小'
---

<!-- reviewed by fiona -->

>**「Allen 谈 Docker 系列」**

>DaoCloud 正在启动 Docker 技术系列文章，每周都会为大家推送一期真材实料的精选 Docker 文章。主讲人为 DaoCloud 核心开发团队成员 Allen（孙宏亮），他是 InfoQ 「Docker 源码分析」专栏作者，已出版《Docker 源码分析》一书。Allen 接触 Docker 近两年，爱钻研系统实现原理，及 Linux 操作系统。

---

**都说容器大法好，但是如果没有 Docker 镜像，Docker 该是多无趣啊。**

是否还记得第一个接触 Docker 的时候，你从 Docker Hub 下拉的那个镜像呢？在那个处女镜像的基础上，你运行了容器生涯的处女容器。镜像的基石作用已经很明显，在 Docker 的世界里，可以说是「No Image, No Container」。

再进一步思考 Docker 镜像，大家可能很快就会联想到以下几类镜像：

1. **系统级镜像**：如 Ubuntu 镜像、CentOS 镜像以及 Debian 容器等；
2. **工具栈镜像**：如 Golang 镜像、Flask 镜像、Tomcat 镜像等；
3. **服务级镜像**：如 MySQL 镜像、MongoDB 镜像、RabbitMQ 镜像等；
4. **应用级镜像**：如 WordPress 镜像、Docker Registry 镜像等。

镜像林林总总，想要运行 Docker 容器，必须要有 Docker 镜像；想要有 Docker 镜像，必须要先下载 Docker 镜像；既然涉及到下载 Docker 镜像，自然会存在 Docker 镜像存储。谈到 Docker 镜像存储，那我们首先来聊聊 Docker 镜像大小方面的知识。

以下将从三个角度来分析 Docker 镜像的大小问题：「Dockerfile 与镜像」、「联合文件系统」以及「镜像共享关系」。

## Dockerfile 与镜像

`Dockerfile` 由多条指令构成，随着深入研究 `Dockerfile` 与镜像的关系，很快大家就会发现，`Dockerfile` 中的每一条指令都会对应于 Docker 镜像中的一层。

继续以如下 `Dockerfile` 为例：

```dockerfile
FROM ubuntu:14.04
ADD run.sh /
VOLUME /data
CMD ["./run.sh"]
```

通过 `docker build` 以上 `Dockerfile` 的时候，会在 `ubuntu:14.04` 镜像基础上，添加三层独立的镜像，依次对应于三条不同的命令。镜像示意图如下：

![镜像示意图](http://7xi8kv.com5.z0.glb.qiniucdn.com/Dockerfile.png)

有了 `Dockerfile` 与镜像关系的初步认识之后，我们再进一步联系到每一层镜像的大小。

不得不说，在层级化管理的 Docker 镜像中，有不少层大小都为 0。那些镜像层大小**不为 0** 的情况，归根结底的原因是，构建 Docker 镜像时，对当前的文件系统造成了修改更新。而修改更新的情况主要有两种：

1. **`ADD` 或 `COPY` 命令**：`ADD` 或者 `COPY` 的作用是在 `docker build` 构建镜像时向容器中添加内容，只要内容添加成功，当前构建的那层镜像就是添加内容的大小，如以上命令 `ADD run.sh /`，新构建的那层镜像大小为文件 `run.sh` 的大小。
2. **`RUN` 命令**：`RUN` 命令的作用是在当前空的镜像层内运行一条命令，倘若运行的命令需要更新磁盘文件，那么所有的更新内容都在存储在当前镜像层中。举例说明：`RUN echo DaoCloud` 命令不涉及文件系统内容的修改，故命令运行完之后当前镜像层的大小为 **0**；`RUN wget http://abc.com/def.tar` 命令会将压缩包下载至当前目录下，因此当前这一层镜像的大小为对文件系统内容的**增量修改部分**，即 `def.tar` 文件的大小（在成功执行的情况下）。

## 联合文件系统

`Dockerfile` 中命令与镜像层一一对应，那么是否意味着 `docker build` 完毕之后，镜像的总大小是否等于每一层镜像的大小总和呢？答案是肯定的。依然以上图为例：如果 `ubuntu:14.04` 镜像的大小为 200 MB，而 `run.sh` 的大小为 5 MB，那么以上三层镜像从上到下，每层大小依次为 0、0 以及 5 MB，那么最终构建出的镜像大小的确为 0 + 0 + 5 + 200 = 205 MB。

虽然最终镜像的大小是每层镜像的累加，但是需要额外注意的是，Docker 镜像的大小**并不等于**容器中文件系统内容的大小（不包括挂载文件，`/proc`、`/sys` 等虚拟文件）。个中缘由，就和联合文件系统有很大的关系了。

首先来看一下这个简单的 `Dockerfile` 例子（假设在 `Dockerfile` 当前目录下有一个 100 MB 的压缩文件 `compressed.tar`）：

```dockerfile
FROM ubuntu:14.04
ADD compressed.tar /
RUN rm /compressed.tar
ADD compressed.tar /
```

1. **`FROM ubuntu:14.04`**：镜像 `ubuntu:14.04` 的大小为 200 MB；
2. **`ADD compressed.tar /`**： `compressed.tar` 文件为 100 MB，因此当前镜像层的大小为 100 MB，镜像总大小为 300 MB；
3. **`RUN rm /compressed.tar`**：删除文件 `compressed.tar`，此时的删除并不会删除下一层的 `compressed.tar` 文件，只会在当前层产生一个 `compressed.tar` 的删除标记，确保通过该层将看不到 `compressed.tar`，因此当前镜像层的大小也为 0，镜像总大小为 300 MB；
4. **`ADD compressed.tar /`**：`compressed.tar` 文件为 100 MB，因此当前镜像层的大小为 300 MB + 100 MB，镜像总大小为 400 MB；

分析完毕之后，我们发现镜像的总大小为 400 MB，但是如果运行该镜像的话，我们很快可以发现在容器根目录下执行 `du -sh` 之后，显示的数值并非 400 MB，而是 300 MB 左右。主要的原因还是，联合文件系统的性质保证了两个拥有 `compressed.tar` 文件的镜像层，容器仅能看到一个。同时这也说明了一个现状，当用户基于一个非常大，甚至好几个 GB 的镜像运行容器时，在容器内部查看根目录大小，发现竟然只有 500 MB 不到，甚至更小。

分析至此，有一点大家需要非常注意：**镜像大小和容器大小有着本质的区别**。

## 镜像共享关系

Docker 镜像说大不大，说小不小，但是一旦镜像的总数上来之后，岂不是对本地磁盘造成很大的存储压力？平均每个镜像 500 MB，岂不是 100 个镜像就需要准备 50 GB 的存储空间？

结果往往不是我们想象的那样，Docker 在镜像复用方面设计得非常出色，大大节省镜像占用的磁盘空间。Docker 镜像的复用主要体现在多个不同的 Docker 镜像可以共享相同的镜像层。

假设本地镜像存储中只有一个 `ubuntu:14.04` 的镜像，我们以两个 Dockerfile 来说明镜像复用：

```dockerfile
FROM ubuntu:14.04
RUN apt-get update
```

```dockerfile
FROM ubuntu:14.04
ADD compressed.tar /
```

假设最终 `docker build` 构建出来的镜像名分别为 `image 1` 和 `image 2`，由于两个 `Dockerfile` 均基于 `ubuntu:14.04`，因此，`image 1` 和 `image 2` 这两个镜像均复用了镜像 `ubuntu:14.04`。 假设 `RUN apt-get update` 修改的文件系统内容为 20 MB，最终本地三个镜像的大小关系应该如下：

**`ubuntu:14.04`**： 200 MB

**`image 1`**：200 MB（`ubuntu:14.04` 的大小）+ 20 MB = 220 MB

**`image 2`**：200 MB（`ubuntu:14.04` 的大小）+ 100 MB = 300 MB

如果仅仅是单纯的累加三个镜像的大小，那结果应该是：200 + 220 + 300 = 720 MB，但是由于镜像复用的存在，实际占用的磁盘空间大小是：200 + 20 + 100 + 320 MB，足足节省了 400 MB 的磁盘空间。在此，足以证明镜像复用的巨大好处。

## 总结

学习 Docker 的同时，往往有三部分内容是分不开的，那就是 Dockerfile、Docker 镜像与 Docker 容器，分析 Docker 镜像大小也是如此。Docker 镜像的大小，貌似平淡无奇，却是优化镜像、容器磁盘限额必须要涉及的内容。

本系列将通过以下多篇文章来分析 Docker 镜像：

1. 深刻理解 Docker 镜像大小
2. 其实 `docker commit` 很简单
3. 不得不说的 `docker save` 与 `docker export` 区别
4. 为什么有些容器文件动不得
5. 打破 `MNT Namespace` 的容器 `VOLUME`

**欲知 Docker 镜像更精彩的内容，关注「Allen 谈 Docker 系列」，且听下回分解。**