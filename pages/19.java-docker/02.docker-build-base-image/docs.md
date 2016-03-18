---
title: '构建基于 Maven 和 Tomcat 的基础镜像'
---

> 目标：构建基于 Maven 和 Tomcat 的基础镜像
> 
> 本项目代码维护在 **[DaoCloud/docker-demo-build-base-image](https://github.com/DaoCloud/docker-demo-build-base-image)** 项目中。
>
> 您可以在 GitHub 找到本项目并获取本文中所提到的所有代码文件。

### 前言

在 Java 开发的世界中，有很大一部分应用是基于 Maven 构建的，而最终的交付结果也是一个 war 包，所以，构建一个基于 Maven 和 Tomcat 的基础镜像很有必要，可以在一定程度减少应用 Dockerfile 的复杂度，也能提升交付效率。

### 编写 Dockerfile

在本教程中，我们选择官方维护的 `maven:3.3.3` 镜像作为我们的基础镜像，在此基础上添加 Tomcat 支持。

```
FROM maven:3.3.3
```
设置 Tomcat 相关的环境变量，并添加到系统 PATH 变量中，使 Tomcat 的启动脚本可以在 Shell 中直接访问。

```
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

```

添加 Tomcat GPG-KEY，用于 Tomcat 下载完后校验文件是否正确，该数据来自 **[Tomcat](https://www.apache.org/dist/tomcat/tomcat-8/KEYS)**。	
```
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \
	05AB33110949707C93A279E3D3EFE6B686867BA6 \
	07E48665A34DCAFAE522E5E6266191C37C037D42 \
	47309207D818FFD8DCD3F83F1931D684307A10A5 \
	541FBE7D8F78B25E055DDEE13C370389288584E7 \
	61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \
	79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \
	9BA44C2621385CB966EBA586F72C284D731FABEE \
	A27677289986DB50844682F8ACB77FC2E86E29AC \
	A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \
	DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \
	F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \
	F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23

```

设置 Tomcat 版本变量，构建时可以传入相应参数更改 Tomcat 版本，随后使用 `curl` 执行下载，并且验证后解压，同时删除多余的 `bat` 脚本，该脚本仅用于 `Windows` 环境，在镜像中无用。		
```	
ENV TOMCAT_VERSION 8.0.29
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz

RUN set -x \
	&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \
	&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \
	&& gpg --verify tomcat.tar.gz.asc \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
	&& rm bin/*.bat \
	&& rm tomcat.tar.gz*

```

暴露 Tomcat 默认的 8080 端口，并指定基于该镜像的容器启动时执行的脚本，该脚本为 Tomcat 启动脚本。	
```	
EXPOSE 8080
CMD ["catalina.sh", "run"]		
```

> 因为 `maven:3.3.3` 镜像依赖的 Java 版本是 1.8, 所以我们的 Tomcat 版本也选择 8.0 版本，保持一致可以最大化 Tomcat 的性能。

在这个 Dockerfile 中，添加了 8.0.29 版本的 Tomcat，并且设置了相应的环境变量。

### 构建基础镜像

```
docker build -t {owner}/base-tomcat-maven .
```

构建完后将生成一个包含 Maven 与 Tomcat 的基础镜像，可以被用在其他镜像中当作基础镜像。

### 完整 Dockerfile 文件
```
FROM maven:3.3.3

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \
	05AB33110949707C93A279E3D3EFE6B686867BA6 \
	07E48665A34DCAFAE522E5E6266191C37C037D42 \
	47309207D818FFD8DCD3F83F1931D684307A10A5 \
	541FBE7D8F78B25E055DDEE13C370389288584E7 \
	61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \
	79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \
	9BA44C2621385CB966EBA586F72C284D731FABEE \
	A27677289986DB50844682F8ACB77FC2E86E29AC \
	A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \
	DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \
	F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \
	F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23
	
ENV TOMCAT_VERSION 8.0.29
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz

RUN set -x \
	&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \
	&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \
	&& gpg --verify tomcat.tar.gz.asc \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
	&& rm bin/*.bat \
	&& rm tomcat.tar.gz*
	
EXPOSE 8080
CMD ["catalina.sh", "run"]	
```

#### 致谢

本文由 DaoCloud 社区用户**谭文科**提供