---
title: '如何制作一个定制的 Python 基础 Docker 镜像'
---

<!-- reviewed by fiona -->

> 目标：准备一个定制的 Python 基础镜像。基础镜像，通常为含最小功能的系统镜像，之后的应用镜像都以此为基础。
> 
> 本项目代码维护在 **[DaoCloud/python-sample-base-image](https://github.com/DaoCloud/python-sample-base-image)** 项目中。
>
> 您可以在 GitHub 找到本项目并获取本文中所提到的所有脚本文件。

#### 制作基础镜像

- 选择 Ubuntu 官方的 14.04 版本为我们依赖的系统镜像。

```dockerfile
FROM ubuntu:trusty
```

> 因所有官方镜像均位于境外服务器，为了确保所有示例能正常运行，可以使用与官方镜像保持同步的 DaoCloud 境内镜像：
>
>```dockerfile
>FROM daocloud.io/ubuntu:trusty
>```

- 设置镜像的维护者，相当于镜像的作者或发行方。

```dockerfile
MAINTAINER Captain Dao <support@daocloud.io>
```

- 用 `RUN` 命令调用 apt-get 包管理器安装 Python 环境所依赖的程序包。

> 安装依赖包相对比较固定，因此该动作应该尽量提前，这样做有助于提高镜像层的复用率。
> 
> 安装完依赖后打扫卫生可以显著的减少镜像大小。

```dockerfile
RUN apt-get update && \
  	apt-get install -y python \
    				   python-dev \
                       python-pip && \
  	rm -rf /var/lib/apt/lists/*
```

> *以下这个方法不建议采用，原因是比上述命令多添加了一层镜像，然而并没有降低总镜像的体积。*
>
>```dockerfile
>RUN apt-get update && \
>  	apt-get install -y python \
>    				   python-dev \
>                       python-pip 
>RUN rm -rf /var/lib/apt/lists/*
>```

- 用 `RUN` 命令调用 `mkdir` 来准备一个干净的放置代码的目录。

```dockerfile
RUN mkdir -p /app
```

- 指定其为当前的工作目录。

```dockerfile
WORKDIR /app
```

- 指定暴露的容器内端口地址，最后设置默认启动命令。

```dockerfile
EXPOSE 80
CMD ["bash"]
```

至此一个 Python 的基础镜像制作完毕，您可以在本地运行 `docker build -t my-python-base .` 来构建出这个镜像并命名为 `my-python-base`。

Python 家族成员众多，因此需要一个通用的基础镜像，并在此基础上根据需求进行定制。

> 由于国内网络环境的特殊，在本地运行 `docker build` 的时间会很长，并且有可能失败。推荐使用 **[DaoCloud Toolbox](http://blog.daocloud.io/toolbox)** 和 DaoCloud 的云端 **[代码构建](http://help.daocloud.io/features/build-flows.html)** 功能。

#### 完整的 Dockerfile

```dockerfile
# Ubuntu 14.04，Trusty Tahr（可靠的塔尔羊）发行版
FROM daocloud.io/ubuntu:trusty

# 道客船长荣誉出品
MAINTAINER Captain Dao <support@daocloud.io>

# APT 自动安装 PHP 相关的依赖包，如需其他依赖包在此添加
RUN apt-get update && \
  	apt-get install -y python \
    				   python-dev \
                       python-pip  \
    # 用完包管理器后安排打扫卫生可以显著的减少镜像大小
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

# 配置默认放置 App 的目录
RUN mkdir -p /app
WORKDIR /app
EXPOSE 80
CMD ["bash"]
```