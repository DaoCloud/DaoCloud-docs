---
title: '使用 Docker 运行 Tomcat ＋ WAR 包 Java 应用'
---

> 目标：用 Tomcat 容器运行一个 J2EE 应用
> 
> 本项目代码维护在 **[DaoCloud/docker-demo-java-tomcat]()** 项目中。
>
> 您可以在 GitHub 找到本项目并获取本文中所提到的所有代码文件。

### 前言

在第一篇教程中，基于 Spring Boot 框架创建了一个 Docker 化的 Java 应用，应用编译的结果是一个 jar 包，而通常我们的 J2EE 应用的产出物是一个 war 包，在本教程中，我们将使用基于 Tomcat 的 Docker 容器运行我们的应用。

### 创建一个新的 Maven Webapp 项目

执行如下命令，生成 Maven Webapp 项目

```
	mvn archetype:generate -DgroupId=io.daocloud.demo -DartifactId=docker-demo-java-tomcat -DarchetypeArtifactId=maven-archetype-webapp
```

如同上一个教程，我们在	pom.xml 文件中加上 `maven-docker-plugin` 插件的配置，这样在编译打包应用的同时，可以构建 Docker 镜像。

```
<plugin>
	<groupId>com.spotify</groupId>
	<artifactId>docker-maven-plugin</artifactId>
	<version>0.3.6</version>
	<executions>
		<execution>
			<phase>package</phase>
			<goals>
				<goal>build</goal>
			</goals>
		</execution>
	</executions>
	<configuration>
	<imageName>${project.artifactId}</imageName>
	<dockerDirectory>${project.basedir}/src/main/docker</dockerDirectory>
	<resources>
		<resource>
			<targetPath>/</targetPath>
			<directory>${project.build.directory}</directory>
			<include>${project.build.finalName}.jar</include>
		</resource>
	</resources>
	</configuration>
</plugin>
```

### 编写 Dockerfile 文件

```
FROM tomcat:8
ADD *.war $CATALINA_HOME/webapps/demo.war
```

在这个 Dockerfile 中，我们选择了官方维护的 `tomcat:8` 镜像作为我们的基础镜像，并且也只做了一件事情，将我们应用编译的 war 包添加到镜像中。

### 启动 Docker 镜像，享受 Docker 世界带来的便利

根据 pom.xml 文件的配置，我们生成的 Docker 镜像名称为应用的 artifactId，即为 `docker-demo-java-tomcat`，运行这个镜像。

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