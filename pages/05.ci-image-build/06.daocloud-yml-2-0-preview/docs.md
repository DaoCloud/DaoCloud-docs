---
title: 'daocloud.yml 2.0'
---

我们对持续集成、持续构建功能进行了升级，拓展了 daocloud.yml 的使用，支持最新的 daocloud.yml 2.0 语法。

## daocloud.yml 2.0

```yaml
version: 2.0
test:
build:
```
daocloud.yml 2.0 主要分成 3 节，`version` 版本号，当前值为 `2.0`。`test` 的内容为旧版本的 daocloud.yml 内容，定义持续集成，这节可选，`test` 的具体写法见[持续集成文档](http://docs.daocloud.io/ci-image-build/daocloud-yml)。
`build`  说明的是镜像构建部分，包括两种构建方式 `lite_image` 和 `image`，这节可选。

##  常规镜像（image） 功能
```yaml
build:
    image:
        dockerfile_path: Dockerfile
        build_dir: /
        cache: true
```
以上代码来源于 [golang-redis-sample](https://github.com/DaoCloud/golang-redis-sample/blob/ship2.0.normal/daocloud.yml)，
该功能即我们常用的镜像构建功能，指定了三个参数：  
`dockerfile_path`：Dockerfile 相对代码根目录的路径，默认值为 `Dockerfile`  
`build_dir`：构建目录，`dockerfile_path` 必须在这个目录之下，默认是代码根目录，即 `/`  
`cache`：是否开启缓存，值为 `true`（开启）和 `false`（关闭）

## 安全镜像（lite_image） 功能

常规镜像功能的不足之处：
1. 众所周知，Dockerfile 中的 `ADD` 和 `COPY` 指令会把源目录全部复制到镜像中，而 docker 镜像是分层，每层 layer 都会保存相应指令执行结果，即使后面的指令删除了前面指令的内容，这层 layer 并不会消失，所以源码还在镜像里，存在源码泄漏隐患。
2. 由于 docker 镜像是分层，每层 layer 都会保存相应指令执行结果，而我们在构建时，经常下载各种依赖和保存中间结果，所以整个构建出来的镜像有时会非常大。实际上，有时我们只需要最后的二进制文件而已。

以上几点的一个解决方案是，用一个 Dockerfile 来下载依赖、编译源码得到最终的可执行文件，然后接着用另一个 Dockerfile 来将这个可执行文件安装到小镜像中，得到最终目标镜像，这样我们既实现了保护源码也实现了缩小镜像的目标。这就是我们的安全镜像功能，构建一个干净、安全、不含源代码的生产级别镜像。

```yaml
build:
    lite_image:
        compile:
            dockerfile_path: Dockerfile
            build_dir: /
            cache: true
        extract:
            - /go/bin/app
        package:
              dockerfile_path: Dockerfile.sec
              build_dir: /
              cache: true
```

以上代码来源于 [golang-redis-sample](https://github.com/DaoCloud/golang-redis-sample/blob/ship2.0/daocloud.yml)。

### compile
`compile` 节说明的是代码的编译期，需要指定三个参数：  
`dockerfile_path`：Dockerfile 的相对代码根目录的路径，默认值为 `Dockerfile`  
`build_dir`：构建目录，`dockerfile_path` 必须在这个目录之下，默认是代码根目录，即 `/`  
`cache`：是否开启缓存，值为 `true`（开启）和 `false`（关闭）

```Dockerfile
FROM golang:1.5.1

MAINTAINER Sakeven "sakeven.jiang@daocloud.io"

# 将源码复制到 $GOPATH/src/app，$GOPATH 为 /go
ADD . $GOPATH/src/app
# 下载安装依赖
RUN go get app
# 静态编译安装，最终可执行文件为 /go/bin/app
RUN CGO_ENABLED=0 go install -a app
```
可以看到这个 [Dockerfile](https://github.com/DaoCloud/golang-redis-sample/blob/ship2.0/Dockerfile) 静态编译产生一个 /go/bin/app 程序。这个 Dockerfile 产生的镜像大约 774 MB。

### extract

`extract` 节说明的是编译期产生的目标文件列表。我们将会把它们提取出来，并放在 `package` 节的 `build_dir` 下，以供 `package` 时使用。
比如要提取的是 `/go/bin/app`， `package.build_dir` 为 `bin`，那么我们会将这个文件放在源代码的 `bin/go/bin/app` 。

### package
`package` 节说明的是可执行文件打包期，需要指定三个参数，与`compile` 节一样。这里我们主要将可执行文件加到最终镜像中。

```Dockerfile
FROM busybox

ADD go/bin/app /usr/bin/app

EXPOSE 80
CMD /usr/bin/app
```
可以看到这个 [Dockerfile.sec](https://github.com/DaoCloud/golang-redis-sample/blob/ship2.0/Dockerfile.sec) 将之前的 go 程序，安装到 busybox，暴露 80 端口，并且通过 `/usr/bin/app` 启动。这个 Dockerfile 产生的镜像大约 8 MB，可见 lite_image 功能可以缩小镜像近 100 倍。

最后完整的 `daocloud.yml` 为

```yaml

version: 2.0

test:
    image:
        daocloud/ci-golang:1.4

    services:
        - redis

    # using default docker-link env
    env:
        - REDIS_PORT_6379_TCP_PROTO = "tcp"
        - REDIS_PASSWORD = ""

    install:
        - sudo apt-get update

    before_script:
        - mkdir -p /gopath/src/golang-redis-sample
        - mv ./* /gopath/src/golang-redis-sample

    script:
        - export GOPATH=/gopath
        - go get -t golang-redis-sample
        - go test golang-redis-sample

build:
    lite_image:
        compile:
            dockerfile_path: Dockerfile
            build_dir: /
            cache: true

        extract:
            - /go/bin/app

        package:
              dockerfile_path: Dockerfile.sec
              build_dir: /
              cache: true
```
