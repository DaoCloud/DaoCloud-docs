---
title: '「Allen 谈 Docker 系列」之 docker logs 实现剖析'
---

<!-- reviewed by fiona -->

>**「Allen 谈 Docker 系列」**

>DaoCloud 正在启动 Docker 技术系列文章，每周都会为大家推送一期真材实料的精选 Docker 文章。主讲人为 DaoCloud 核心开发团队成员 Allen（孙宏亮），他是 InfoQ 「Docker 源码分析」专栏作者，已出版《Docker 源码分析》一书。Allen 接触 Docker 近两年，爱钻研系统实现原理，及 Linux 操作系统。

---

Docker 完全可以轻易构建用户的应用，即为 build；

Docker 还可以将应用快速分发，即为 ship；

最后，Docker 依然有能力秒级启动应用，即为 run。

Build，Ship，Run，简单的3步，分分钟为 DevOps 创建了管理应用生命周期的捷径。

应用是运行起来了，应用运行后，运行状态相信是工程师最关心的点。这一点，Docker 如何帮工程师排忧解难呢？

想知道应用是否仍在运行？`docker ps` 会告诉您。

想获知应用的资源使用情况如何？`docker stats` 为您呈现。

想了解应用的运行日志？`docker logs` 绝对是您最好的选择。

如今，Docker 容器应用的日志分析，已经是一个获悉应用运行逻辑的状态，以及分析应用运行性能的不二法宝。

基于 Docker 容器的日志，已然有很多人在做；那大家是否了解 Docker 容器的日志是怎么来的呢？如果大家还不清楚 Docker 日志的实现原理，那么本文可以带您窥探 docker logs 的究竟。

## 1. Docker 容器应用如何产生日志？

大家可以试想一下，如果没有 Docker，您的应用如何打印日志？普遍情况有以下两种：

- 第一，向标准输出（stdout）中打印日志；
- 第二，设置日志文件 `app.log`（或其它文件名），向此文件中打印日志。

Docker 从诞生伊始，就从未对用户应用做出标准性规范，日志也不例外，从未有过限制。既然如此，Docker 容器应用的日志也不外乎以上两种。第二种很好理解，依然往容器中某个日志文件打印；然而第一种，应用通过标准输出（stdout）的方式打印日志，该如何呈现给用户？

## 2. Docker 容器应用的日志实现

对于日志文件，Docker 不可能也不应该深入应用内部逻辑，截获并接管日志文件内容，这只会破坏 Docker 的通用性。但是对于 Docker 容器内应用的标准输出，Docker 则是做了工作的。具体实现，可以参考下图：

![](http://7xi8kv.com5.z0.glb.qiniucdn.com/docker%20logs.png)

假设 application 是 Docker 容器内部运行的应用，那么对于应用的第一部分标准输出（stdout）日志，Docker Daemon 在运行这个容器时就会创建一个协程（goroutine），负责标准输出日志。

由于此 goroutine 绑定了整个容器内所有进程的标准输出文件描述符，因此容器内应用的所有标准输出日志，都会被 goroutine 接收。goroutine 接收到容器的标准输出内容时，立即将这部分内容，写入与此容器一一对应的日志文件中，日志文件位于 `/var/lib/docker/containers/<container_id>`，文件名为 `<container_id>-json.log`。

至此，关于容器内应用的所有标准输出日志信息，已经全部被 Docker Daemon 接管，并重定向到与容器一一对应的日志文件中。

## 3. 用户如何查看容器日志？

日志总是需要被用户查看的，Docker 则通过 `docker logs` 命令向用户提供日志接口。`docker logs` 实现原理的本质均基于与容器一一对应的 `<container-id>-json.log`，除了 `docker logs -f` 命令。

以下简要介绍 `docker logs` 命令下各参数的含义：

- 无参数：直接显示容器的所有日志信息
- tail：从尾部开始按需显示容器日志
- since：从某个时间开始显示容器日志
- timestamp：显示容器日志时显示日志时间戳
- f：将当前时间点，容器日志文件 `<container-id>-json.log` 中的日志信息全部打印；此时间点之后所有的日志信息与日志文件无关，直接接收goroutine 往日志文件中写的文件描述符，并显示

总而言之，Docker 容器日志的处理并不会很复杂。此文阅完，日志的来龙去脉，一清二楚。

当然，您也可以做两个实验检验以上内容：

- Experiement 1：通过 Docker 运行一个应用，日志会从标准输出打印日志，然后通过 `docker logs` 查看日志。
- Experiement 2：运行一个 Docker 容器，随后 `docker exec` 命令进入这个容器，接着通过 `echo`、`cat` 等命令向容器的标准输出中打印内容，最后通过 `docker logs` 查看日志。

实验是检验真理的唯一标准。您会发现，Experiement 1 中，查看日志会有日志；而 Experiement 2 中却找不到 `echo`、`cat` 等命令标准输出的日志内容。

Experiement 2 做完，瞬间毁三观，难道以上内容有差错？可以明确告诉您没有，那矛盾如何会存在？

欲知后事如何，关注「Allen 谈 Docker」系列，且听下回分解。