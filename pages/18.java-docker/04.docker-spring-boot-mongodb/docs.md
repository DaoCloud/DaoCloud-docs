---
title: 'Docker 环境下的 Spring Boot 和 MongoDB 集成'
---

> 目标：开发一个基于 Spring Boot 和 MongoDB 的应用，使用 MongoDB 记录访问者信息
> 
> 本项目代码维护在 **[DaoCloud/docker-demo-java-mongo](https://github.com/DaoCloud/docker-demo-java-mongo)** 项目中。
>
> 您可以在 GitHub 找到本项目并获取本文中所提到的所有代码文件。

### 前言

生产环境中的应用，少不了数据库和缓存的配合，在我们的这个教程中，将会给大家演示如何基于 Spring Boot 和 MongoDB 来开发一个记录访问者次数的应用，并且将应用 Docker 化。

在本教程中，我们将使用 Docker Compose 对我们服务进行编排，请按照 **[安装 Docker Compose](http://get.daocloud.io/#install-compose)** 准备好 Docker Compose 环境。

### 创建应用

请大家回到 **[开发一个基于 Spring Boot 框架的 Docker 化的 Java 应用](http://docs.daocloud.io/java-docker/docker-java-spring-boot)** 这篇教程，准备好自己的应用框架。

#### 添加 MongoDB 支持

编辑 pom.xml 文件，添加如下依赖：
```
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```

编辑 application.properties 文件，添加 MongoDB 连接信息
```
spring.data.mongodb.host=mongodb
spring.data.mongodb.port=27017
spring.data.mongodb.database=docker-demo-java-mongo
spring.data.mongodb.repositories.enabled=true
```

> 在本教程中，MongoDB 容器将会通过 link 方式引入，故该配置文件中 `mongodb.host` 取值为 MongoDB 的 link 配置，请参阅下方 `docker-compose.yaml` 配置。

#### 创建 Entity 及 Data Access Object

新建 Visitor 类，添加如下属性：
```
String id;
String ip;
Date visitDate;

//忽略 getter、setter
```

新建 VisitorRepository 接口，继承 MongoRepository 接口：
```java
public interface VisitorRepository extends MongoRepository<Visitor,String>{
	
}
```

> 基于 Spring Data JPA 实现数据访问，该处无需对 VisitorRepositor 接口进行实现，更多信息请参考 [Spring Data JPA](http://projects.spring.io/spring-data/)

#### 创建控制器，添加来访者记录

修改 DockerJavaDemoApplication.java 类，添加来访者记录：
```
@SpringBootApplication
public class DockerDemoSpringBootApplication {
	
    @Resource
    VisitorRepository visitorRepository;
  
    public static void main(String[] args) {
        SpringApplication.run(DockerJavaDemoApplication.class, args);
    }

	@RequestMapping("")
	public String visit(HttpServletRequest request){
		
		Visitor visitor = new Visitor();
        visitor.setId(UUID.randomUUID().toString());
        visitor.setIp(request.getRemoteAddr());
        visitor.setVisitDate(new Date());

        visitorRepository.save(visitor);

        Long count =  visitorRepository.count();

        return String.format("你是来自%s的第%d位访问者。",request.getRemoteAddr(),count);
	}
}
```

### 编写 docker-compose.yaml 文件，引入 MongoDB 服务

```
web:
  build: .
  ports:
    - "8080:8080"
  links:
    - mongodb:mongodb

mongodb:
  image: daocloud.io/library/mongo:latest
  ports:
    - "27017:27017"

```

在该文件中，我们定于了两个服务：
- 基于我们应用构建的 docker-demo-java-mongo 镜像，用来提供 Web 服务
- 基于 DaoCloud 提供的 MongoDB 镜像，提供存储服务
- 通过 links 为 web 关联 mongo 服务

> 如果您需要在 DaoCloud 集成环境中部署您的应用，请保持该配置文件中 links 配置的 MongoDB 服务名称为 `mongodb`,这是 DaoCloud 默认的 MongoDB 服务名称。

### 启动 Docker Compose，体验服务编排的魅力
```
  docker-compose up
```

打开浏览器，或者使用 curl 访问如下地址：
```
http://127.0.0.1:8080
```

将会看到 "你是来自127.0.0.1的第1位访问者。"，多次访问后，能看到数字的累加，表示数据已经被持久化到 MongoDB 了，当然，如果要让服务停止后数据仍可以被记录，需要使用 Volume 指令挂载存储，请参阅 **[使用 Volume 实现容器状态持久化](http://docs.daocloud.io/daocloud-services/use-volume)**

#### 致谢

本文由 DaoCloud 社区用户**谭文科**提供