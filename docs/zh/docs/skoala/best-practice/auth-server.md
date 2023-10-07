# 微服务网关接入认证服务器

微服务网关支持接入第三方认证服务器。

## 前提条件

- [创建一个集群](../../kpanda/user-guide/clusters/create-cluster.md)或[接入一个集群](../../kpanda/user-guide/clusters/integrate-cluster.md)
- [创建一个网关](../gateway/create-gateway.md)

## 配置认证服务器

### 使用默认的认证服务器

1. 将认证服务器的代码模板克隆到本地。

    ```
    git clone https://github.com/projectsesame/envoy-authz-java
    ```
    
2. 直接使用 [all-in-one-contour.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml)
   以及 [all-in-one-contour.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml)
   下的默认镜像。

    默认镜像如下：
    
    - release.daocloud.io/skoala/demo/envoy-authz-java:0.1.0
    - release-ci.daocloud.io/skoala/demo/envoy-authz-java:0.1.0

3. 模板为简单的路径判断，当访问路径为 `/` 时通过认证，其余路径为拒绝访问。

### 使用自定义的认证服务器

1. 将认证服务器的代码模板克隆到本地。

    ```
    git clone https://github.com/projectsesame/envoy-authz-java
    ```
    
    该项目分为两个子模块：

    - API 模块是 envoy 的 `protobuf` 文件的定义（无需修改）
    - authz-grpc-server 模块是认证服务器的认证逻辑处理地址（在这里填写认证逻辑）
    - release.daocloud.io/skoala/demo/envoy-authz-java:0.1.0

2. 使用如下命令编译 API 模块，解决类找不到的问题

    ```bash
    mvn clean package
    ```

3. 成功编译之后，在 check 方法中编写自定义的认证逻辑。

    - check 方法在 envoy-authz-java/authz-grpc-server/src/main/java/envoy/projectsesame/io/authzgrpcserver/AuthzService.java  
    - 模板为简单的路径判断，当访问路径为 `/` 时通过认证，其余路径为拒绝访问。

4. 代码编写完成之后，使用 Docker 打包镜像。

    代码模板仓库中已存在 Dockerfile 文件，可以直接使用该模板构建镜像。

5. 将镜像地址填入 [all-in-one-contour.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml) 文件中的 Deployment 下的 `spec/template/spec/containers/image` 字段。

    ![填写镜像](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/jwt04.png)

## 接入认证服务器

1. 在网关所在的集群内创建以下资源。使用 `kubectl apply` 命令基于
   [all-in-one-contour.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml)
   文件可以一次性快速创建下述三项资源。

    - 认证服务器的 Deployment
    - 认证服务器的 Service
    - 认证服务器的 ExtensionService

2. 在网关下创建一个使用 `https` 协议的域名，填写基础信息。

    ![基础配置](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/jwt01.png)

3. 填写该域名的安全配置，指定认证服务器的地址。认证服务器地址格式为 `namespace/name`。

    ![基础配置](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/jwt02.png)

    !!! note

        认证服务器的 `namespace/name` 指的是
        [all-in-one-contour.yaml](https://github.com/projectsesame/envoy-authz-java/blob/main/all-in-one-contour.yaml)
        文件中 ExtensionService 下的 `metadata` 部分的 `namespace` 和 `name` 字段的取值。

        ![基础配置](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/jwt05.png)

4. 在网关下创建一个 API，`关联域名`填写刚才新创建的域名，匹配路径为 `/`，并开启`安全认证`，并将 API 上线。

    ![基础配置](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/jwt03.png)

5. 现在即可通过认证服务器访问该 API 了。
