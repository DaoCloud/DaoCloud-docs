---
title: '使用 Docker 运行 Tomcat ＋ WAR 包 Java 应用'
---

> 目标：用 Tomcat 容器运行一个 J2EE 应用
> 
> 本项目代码维护在 **[DaoCloud/docker-demo-java-tomcat](https://github.com/DaoCloud/docker-demo-java-tomcat)** 项目中。
>
> 您可以在 GitHub 找到本项目并获取本文中所提到的所有代码文件。

### 前言

在第一篇教程中，基于 Spring Boot 框架创建了一个 Docker 化的 Java 应用，应用编译的结果是一个 jar 包，而通常我们的 J2EE 应用的产出物是一个 war 包，在本教程中，我们将使用基于 Tomcat 的 Docker 容器运行我们的应用。

### 创建一个新的 Maven Webapp 项目

执行如下命令，生成 Maven Webapp 项目

```
	mvn archetype:generate -DgroupId=io.daocloud.demo \
                           -DartifactId=docker-demo-java-tomcat \
                           -DarchetypeArtifactId=maven-archetype-webapp
```


### 编写 Dockerfile 文件

在教程 **[构建基于 Maven 和 Tomcat 的基础镜像](http://docs.daocloud.io/java-docker/docker-build-base-image)** 中，构建了一个基于 Maven 和 Tomcat 的基础镜像，如果您还没来得及阅读，建议您先阅读该教程，可以在本教程中减少 Dockerfile 文件的复杂度和构建时间。

#### 选择基础镜像

如果您已经构建了自己的基础镜像，那么在接下来的教程中，将使用您构建的基础镜像作为开始：
```
FROM base-tomcat-maven:latest
```

如果您使用了 DaoCloud 的代码构建，且当前项目也是使用的 DaoCloud 代码构建，请把 Dockerfile 中的基础镜像修改为您在 DaoCloud 上的镜像地址，如:
```
FROM daocloud.io/rockytan/docker-base-maven-tomcat:latest
```

> 上文中的 rockytan 为作者的镜像仓库名称，请替换成您自己的仓库名称。

如果您没有构建自己的基础镜像，现在需要构建一个同时包含 Maven 和 Tomcat 的镜像，那我们从头开始构建：

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
		&& rm -rf webapps/* \
        && rm tomcat.tar.gz*
```

同样的，我们的选择了官方维护的 `maven:3.3.3` 镜像，并且在之上加入了 Tomcat 的支持。

#### 添加项目构建

```
ADD pom.xml /tmp/build/
RUN cd /tmp/build && mvn -q dependency:resolve

ADD src /tmp/build/src
        #构建应用
RUN cd /tmp/build && mvn -q -DskipTests=true package \
        #拷贝编译结果到指定目录
        && rm -rf $CATALINA_HOME/webapps/* \
        && mv target/*.war $CATALINA_HOME/webapps/ROOT.war \
        #清理编译痕迹
        && cd / && rm -rf /tmp/build

EXPOSE 8080
CMD["catalina.sh","run"]
```


#### 执行镜像构建
```
docker build -t docker-demo-java-tomcat .
```

### 启动 Docker 镜像，享受 Docker 世界带来的便利

基于镜像创建容器：

```
docker run -d -p 8080:8080 docker-demo-java-tomcat
```

随后，打开浏览器，或者使用 curl 命令访问如下地址:
```
http://127.0.0.1:8080/demo
```

将会看到 Hello World! 的输出，这表示我们基于 J2EE 应用编译的 war 包已经成功使用 Docker 运行起来了。

#### 致谢

本文由 DaoCloud 社区用户**谭文科**提供