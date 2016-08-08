---
title: 'Dockerfile 的结构和写法'
taxonomy:
    category:
        - docs
---

<!-- reviewed by fiona -->

Docker 为我们提供了 Dockerfile 来解决自动化的问题。我们将介绍什么是 Dockerfile，它能够做到的事情以及 Dockerfile 的一些基本语法。

#### Dockerfile 的语法规则

Dockerfile 包含创建镜像所需要的全部指令。基于在 Dockerfile 中的指令，我们可以使用 `Docker build` 命令来创建镜像。通过减少镜像和容器的创建过程来简化部署。

Dockerfile 支持支持的语法命令如下：

```shell
INSTRUCTION argument
```

**指令不区分大小写。但是，命名约定为全部大写。**

所有 Dockerfile 都必须以 `FROM` 命令开始。`FROM` 命令会指定镜像基于哪个基础镜像创建，接下来的命令也会基于这个基础镜像（注：CentOS 和 Ubuntu 有些命令可是不一样的）。`FROM` 命令可以多次使用，表示会创建多个镜像。具体语法如下：

```shell
FROM <image name>
```

例如：

```shell
FROM ubuntu
```

上面的指定告诉我们，新的镜像将基于 Ubuntu 的镜像来构建。

继 `FROM` 命令，DockefFile 还提供了一些其它的命令以实现自动化。在文本文件或 Dockerfile 文件中这些命令的顺序就是它们被执行的顺序。

让我们了解一下这些有趣的 Dockerfile 命令吧。

- MAINTAINER：设置该镜像的作者。语法如下：

```shell
MAINTAINER <author name>
```

- RUN：在 shell 或者 exec 的环境下执行的命令。`RUN`指令会在新创建的镜像上添加新的层面，接下来提交的结果用在Dockerfile的下一条指令中。语法如下：

```shell
RUN 《command》
```

- ADD：复制文件指令。它有两个参数<source>和<destination>。destination 是容器内的路径。source 可以是 URL 或者是启动配置上下文中的一个文件。语法如下：

```shell
ADD 《src》 《destination》
```

- CMD：提供了容器默认的执行命令。 Dockerfile 只允许使用一次 CMD 指令。 使用多个 CMD 会抵消之前所有的指令，只有最后一个指令生效。 CMD 有三种形式：

```shell
CMD ["executable","param1","param2"]
 CMD ["param1","param2"]
 CMD command param1 param2
```

- EXPOSE：指定容器在运行时监听的端口。语法如下：

```shell
EXPOSE <port>;
```

- ENTRYPOINT：配置给容器一个可执行的命令，这意味着在每次使用镜像创建容器时一个特定的应用程序可以被设置为默认程序。同时也意味着该镜像每次被调用时仅能运行指定的应用。类似于`CMD`，Docker只允许一个ENTRYPOINT，多个ENTRYPOINT会抵消之前所有的指令，只执行最后的ENTRYPOINT指令。语法如下：

```shell
ENTRYPOINT ["executable", "param1","param2"]
 ENTRYPOINT command param1 param2
```

- WORKDIR：指定`RUN`、`CMD`与`ENTRYPOINT`命令的工作目录。语法如下：

```shell
WORKDIR /path/to/workdir
```

- ENV：设置环境变量。它们使用键值对，增加运行程序的灵活性。语法如下：

```shell
ENV <key> <value>
```

- USER：镜像正在运行时设置一个 UID。语法如下：

```shell
USER <uid>
```

- VOLUME：授权访问从容器内到主机上的目录。语法如下：

```shell
VOLUME ["/data"]
```

#### Docker 入门教程

我们推荐 Flux7 的 Docker 入门教程，国内社区已有翻译，建议大家阅读学习。

+ Docker入门教程（一）[介绍](http://dockone.io/article/101)
+ Docker入门教程（二）[命令](http://dockone.io/article/102)
+ Docker入门教程（三）[DockerFile](http://dockone.io/article/103)
+ Docker入门教程（四）[Docker Registry](http://dockone.io/article/104)
+ Docker入门教程（五）[Docker安全](http://dockone.io/article/105)
+ Docker入门教程（六）[另外的15个Docker命令](http://dockone.io/article/106)
+ Docker入门教程（七）[Docker API](http://dockone.io/article/107)
+ Docker入门教程（八）[Docker Remote API](http://dockone.io/article/109)
+ Docker入门教程（九）[10个镜像相关的API](http://dockone.io/article/110)

>>>>> 本文及上述推荐文章的译者是田浩浩，他是悉尼大学（USYD）硕士研究生，目前在珠海从事 Android 应用开发工作。业余时间专注 Docker 的学习与研究。田浩浩已授权 DaoCloud 使用这些内容。