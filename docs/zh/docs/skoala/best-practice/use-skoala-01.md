# 示例应用体验微服务治理

微服务引擎属于 DCE 5.0 高级版功能，其中包含注册中心、配置中心、微服务治理（传统微服务、云原生微服务）、云原生网关等功能。
本文将通过示例应用带您体验其中的微服务治理功能。

此次最佳实践包含的全部流程如下：

1. 在应用工作台部署示例应用，并启用微服务治理功能
2. 在微服务引擎中启用传统微服务治理插件
3. 在微服务引擎中配置对应的治理规则
4. 在微服务引擎暴露 API 并访问应用

## 示例应用介绍

本次实践使用的示例应用基于 OpenTelemetry 的标准演示应用，由 DaoCloud 大微服务团队根据 DCE 5.0
的功能加以优化，以便更好地体现云原生以及可观测能力，呈现微服务治理效果。

示例应用已经在 Github 开源，访问该应用的
[Github 仓库地址](https://github.com/openinsight-proj/openinsight-helm-charts)可以获取详细信息。

示例应用的架构图如下：

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/demo-arch.png)

## 应用部署

[应用工作台](../../amamba/intro/index.md)是 DCE 5.0 的应用管理模块，支持创建/维护多种类型的应用、GitOps
和灰度发布等功能，可以快速将应用部署到任何集群。应用工作台支持基于 Git 仓、Jar 包、容器镜像、Helm 模板部署应用。
本次实践基于 `Helm 模板` 部署示例应用。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/chooseInstalltype.png)

部署应用之前需要满足如下的前提条件：

- 在容器管理中[添加 Helm 仓库](../../kpanda/user-guide/helm/helm-repo.md):

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/addhelmrepo.png)

- 在微服务引擎中[创建 Nacos 注册中心实例](../trad-ms/hosted/create-registry.md)

    > 注意记录注册中心的地址信息，后续安装应用时需要用到。

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/registry.png)

### 基于 Helm 模板部署

1. 在`应用工作台`->`向导`->`基于 Helm 模板`中，找到 opentelemetry-demo 应用，点击应用卡片进行安装

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/helmtemplate.png)

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/templatedetail.png)

2. 在 Helm 的安装界面，注意确认部署位置是否正确，然后按照下方要求更新 `JAVA_OPTS` 部分的参数配置。

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/installchart.png)

    根据上方记录的注册中心地址，将下方带有注释的参数更新如下：

    ```java
    -javaagent:./jmx_prometheus_javaagent-0.17.0.jar=12345:./prometheus-jmx-config.yaml
        -Dspring.extraAdLabel=Daocloud -Dspring.randomError=false
        -Dspring.matrixRow=200 -Dmeter.port=8888
        -Dspring.cloud.nacos.discovery.enabled=true       # 修改，以启用 Nacos 服务注册发现
        -Dspring.cloud.nacos.config.enabled=true          # 修改，以启用 Nacos 配置管理能力
        -Dspring.cloud.nacos.config.server-addr=nacos-test.skoala-test:8848           # 修改，以配置 Nacos 注册中心地址
        -Dspring.application.name=adservice-springcloud
        -Dspring.cloud.nacos.discovery.server-addr=nacos-test.skoala-test:8848        # 修改，以配置 Nacos 注册中心地址
        -Dspring.cloud.nacos.discovery.metadata.k8s_cluster_id=xxx                    # 修改，以配置 Nacos 注册中心所在集群 ID
        -Dspring.cloud.nacos.discovery.metadata.k8s_cluster_name=skoala-dev           # 修改，以配置 Nacos 注册中心所在集群名称
        -Dspring.cloud.nacos.discovery.metadata.k8s_namespace_name=skoala-test        # 修改，以配置 Nacos 注册中心所在命名空间
        -Dspring.cloud.nacos.discovery.metadata.k8s_workload_type=deployment
        -Dspring.cloud.nacos.discovery.metadata.k8s_workload_name=adservice-springcloud
        -Dspring.cloud.nacos.discovery.metadata.k8s_service_name=adservice-springcloud
        -Dspring.cloud.nacos.discovery.metadata.k8s_pod_name=${HOSTNAME}
        -Dspring.cloud.sentinel.enabled=false          # 修改，以启用 Sentinel
        -Dspring.cloud.sentinel.transport.dashboard=nacos-test-sentinel.skoala-test:8080  # 修改，以配置 Sentinel 控制台地址
    ```

   > 获取集群 ID、集群名称、命名空间名称的方法可参考：`kubectl get cluster <clusername> -o json | jq .metadata.uid`

3. 应用创建成功后，会显示在应用工作台的 Helm 应用列表。

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/helmapplist.png)

### Java 项目自行开发调试

如果采用其他部署方式，配置注册中心地址的方法可能有所不同。Java 项目在开发时需要集成 Nacos 的 SDK，
而 DCE 5.0 提供的注册中心完全兼容开源 Nacos，所以可以直接使用开源 Nacos 的 SDK。
具体操作步骤可参考[基于 Jar 包部署 Java 应用](../../amamba/user-guide/wizard/jar-java-app.md)。

使用 `java -jar` 启动项目时，添加对应的环境变量配置：

```java
    -Dspring.cloud.nacos.discovery.enabled=false        # 启用 Nacos 服务注册发现
    -Dspring.cloud.nacos.config.enabled=false           # 启用 Nacos 配置管理能力
    -Dspring.cloud.sentinel.enabled=false               # 启用 Sentinel
    -Dspring.cloud.nacos.config.server-addr=nacos-test.skoala-test:8848           # 配置 Nacos 注册中心地址
    -Dspring.application.name=adservice-springcloud
    -Dspring.cloud.nacos.discovery.server-addr=nacos-test.skoala-test:8848        # 配置 Nacos 注册中心地址
    -Dspring.cloud.nacos.discovery.metadata.k8s_cluster_id=xxx                    # 配置 Nacos 注册中心所在集群 ID
    -Dspring.cloud.nacos.discovery.metadata.k8s_cluster_name=skoala-dev           # 配置 Nacos 注册中心所在集群名称
    -Dspring.cloud.nacos.discovery.metadata.k8s_namespace_name=skoala-test        # 配置 Nacos 注册中心所在命名空间
    -Dspring.cloud.nacos.discovery.metadata.k8s_workload_type=deployment
    -Dspring.cloud.nacos.discovery.metadata.k8s_workload_name=adservice-springcloud
    -Dspring.cloud.nacos.discovery.metadata.k8s_service_name=adservice-springcloud
    -Dspring.cloud.nacos.discovery.metadata.k8s_pod_name=${HOSTNAME}
```

!!! note

    上面的 `metadata` 信息不能缺失，否则注册中心中呈现的服务会缺失这部分信息。

### 使用容器镜像部署

如果选择基于容器镜像部署应用，可以直接在用户界面配置中开启微服务治理并选取对应的注册中心模块，操作更简便。
具体步骤可参考[基于 Git 仓构建微服务应用](../../amamba/user-guide/wizard/create-app-git.md)。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/createbyimage.png)

## 启用传统微服务治理

开始使用微服务治理功能之前，需要在对应注册中心下的插件中心开启对应的治理插件。
插件中心提供 Sentinel 治理和 Mesh 治理两种插件，支持通过用户界面实现可视化配置。
安装插件后可以扩展微服务治理能力，满足不同场景下的业务诉求。

本次实践采用传统微服务治理，即开启 Sentinel 治理插件。
如需了解详细步骤，可参考[启用 Sentinel 治理插件](../trad-ms/hosted/plugins/sentinel.md)。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/registry/managed/plugins/imgs/plugincenter01.png)

## 配置对应的治理规则

应用部署成功后，可以在之前准备注册中心下的`微服务列表`中查看对应的服务。
微服务列表提供流控规则、熔断降级、热点规则、系统规则、授权规则等流量治理规则。本次实践以流控规则为例进行演示。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/nacosservicelist.png)

### 配置流控策略

这里限流策略示例，我们通过简单的配置即可为服务增加对应的限流策略。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/createratelimitrule.png)

### 测试流控策略

通过访问服务地址，我们可以看到在 1 分钟内请求次数大于 2 次之后，后续请求都会被拦截；在超过 1 分钟后自动恢复。

## 暴露 API 并访问应用

微服务应用部署完成后，需要通过 API 网关将应用入口开放给外部访问，完成这一步才是完成的服务使用体验。
为了暴露服务 API，需要创建云原生网关，将服务接入该网关，并创建对应的 API 路由。

### 创建云原生网关

首先需要创建一个云原生网关，具体操作步骤可以参考： [创建云原生网关](../gateway/create-gateway.md)

!!! note

    创建网关时，应该将网关部署在示例应用所在的集群，并且该网关需要管辖示例应用所在的命名空间。

    ![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/gatewaylist.png)

### 接入服务

基于 DCE 5.0 的特性，云原生网关可以自动发现所管辖命名空间内的服务，所以无需手动接入服务。

本次演示采用 Nacos 注册中心的服务，很大程度上扩宽了网关可接入的服务数量，可以在`服务接入`中选择接入 Nacos 注册中心的服务。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/gatewayservicelist.png)

!!! info

    当服务不在网关所管辖的命名空间内，或者想要接入注册中心或者其他外部服务时（使用域名/IP），可以采用手工接入服务的方式。

### 创建 API 路由

参考文档 [添加 API](../gateway/api/add-api.md) 创建对应的 API 路由。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/apiroute.png)

### 访问应用

当网关 API 创建完成后，使用创建 API 时配置的 **域名** 与 **外部 API 路径** 即可成功访问到应用页面，如下图所示。

**示例应用的首页**:

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/webstorehomepage.png)

**示例应用的订单确认页面**:

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/webstorecheckoutpage.png)

## 结语

以上就是整个微服务引擎模块的体验之旅。在整个 DCE 5.0 的能力支持下我们顺利完成了应用部署、
启用微服务治理、配置并测试微服务治理策略、通过云原生网关开放 API、实际访问应用等操作。

### 更多能力

当我们的应用部署成功之后，对于后续的应用维护过程中，实际非常依赖 DCE 5.0 提供的可观测能力。接下来，我们会补充对应可观测能力实践。

- 查看应用部署后的拓扑结构
- 查看应用的日志内容
- 查看云网关网关 API 的访问日志
