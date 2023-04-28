# 基于 Git 仓构建微服务应用

应用工作台支持通过 Git 仓库、[Jar 包](jar-java-app.md)、容器镜像、Helm 模板等四种方式构建应用。本文介绍如何通过 Git 仓库源码构建传统微服务应用，从而对应用进行流量治理，查看日志、监控、链路追踪等功能。

## 前提条件

- 需创建一个工作空间和一个用户，该用户需加入该工作空间并赋予 `workspace edit` 角色。
  参考[创建工作空间](../../../ghippo/user-guide/workspace/workspace.md)、[用户和角色](../../../ghippo/user-guide/access-control/user.md)。
- 创建可以访问代码仓库仓库、镜像仓库的两个凭证，参考[凭证管理](../pipeline/credential.md)。
- 准备一个 Gitlab 仓库、Harbor 仓库。

## 创建凭证

1. 在`凭证`页面创建两个凭证：

    - git-credential：用户名和密码，用于访问代码仓库
    - registry-credential：用户名和密码，用于访问镜像仓库

1. 创建完成后，可以在`凭证列表`页面看到凭证信息。

## 基于 Git 创建微服务应用

1. 在`应用工作台` -> `向导`页面中，点击 `基于 Git 仓构建`。

    ![向导](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/ms01.png)

2. 参考以下说明填写基本信息，然后点击`下一步`：

    - 名称：填写应用的名称。
    - 资源类型：支持无状态负载、有状态负载，本演示选择无状态负载。
    - 输入或选择应用组。
    - 部署位置：选择将应用部署到哪个集群下的哪个命名空间。如果要接入微服务，请确保当前工作空间下已经[创建了注册中心](../../../skoala/registry/managed/registry-lcm/create-registry.md)。
    - 实例数：填写实例的数量，Pod 的数量。

        ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/ms02.png)

3. 参考以下说明填写流水线配置，然后点击`下一步`。

    - 代码仓库：输入 Git 仓库地址，例如 `https://gitlab.daocloud.cn/ndx/skoala.git`。在实际操作中请使用自己的仓库地址。
    - 分支：默认为`main`，此处为`main`，无需更改。
    - 凭证：选择访问代码仓库的凭证 `git-credential`，如果为公开仓库，则无需填写。
    - Dockerfile 路径：输入 Dockerfile 在代码仓库中的绝对路径，例如 `demo/integration/springcloud-nacos-sentinel/code/Dockerfile`。
    - 目标镜像名称：输入镜像仓库名称，例如 [`release-ci.daocloud.io/test-lfj/fromgit`](http://release-ci.daocloud.io/test-lfj/fromgit) 。
    - Tag：输入镜像仓库版本，例如 `v2.0.0`。
    - 凭证：选择访问镜像仓库的凭证，例如 `registry-credential`。
    - ContextPath：ContextPath 为 docker build 命令执行上下文路径。填写相对于代码根目录的路径，如 target，如果不填则为 Dockerfile 文件所在目录。
    - 构建参数：构建参数会以 --build-arg 的形式传递到 build 命令的参数中，支持将上游制品下载地址、上游镜像下载地址设置为参数，同时支持自定义任意参数。

        ![流水线构建](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/ms03.png)

4. 参考以下说明填写容器配置，然后点击`下一步`。

    - 服务配置：支持集群内访问、节点访问、负载均衡。示例值如下：

        ```
        - name: http             protocol: TCP      port: 8081      targetPort: 8081    
        - name: health-http      protocol: TCP      port: 8999      targetPort: 8999
        - name: service         protocol: TCP      port: 9555      targetPort: 9555
        ```
        
        > 有关服务配置的更多详细说明，可参考[创建服务](../../../kpanda/user-guide/services-routes/create-services.md)。
        
    - 资源限制：指定应用能使用的资源上限，包括 CPU、内存。

    - 生命周期：设置容器启动时、启动后、停止前需要执行的命令。详情可参考[容器生命周期配置](../../../kpanda/user-guide/workloads/pod-config/lifecycle.md)。

    - 健康检查：用于判断容器和应用的健康状态，有助于提高应用的可用性。详情可参考[容器健康检查配置](../../../kpanda/user-guide/workloads/pod-config/health-check.md)。

    - 环境变量：配置 Pod 内的容器参数，为 Pod 添加环境变量或传递配置等。详情可参考[容器环境变量配置](../../../kpanda/user-guide/workloads/pod-config/env-variables.md)。

    - 数据存储：配置容器挂载数据卷和数据持久化的设置。

        ![容器配置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/ms04.png)

5. 在`高级配置`页面点击`开启接入微服务`，参考以下说明配置参数，然后点击`确定`。

    - 选择框架：支持`Spring Cloud`、`Dubbo`，此处选择 `Spring Cloud` 。
    - 注册中心实例：目前仅支持选择[微服务引擎中的托管 Nacos 注册中心实例](../../../skoala/registry/managed/registry-lcm/create-registry.md)。
    - 注册中心命名空间：微服务应用的 nacos 命名空间
    - 注册中心服务分组：微服务应用的服务分组
    - 用户名/密码：如果该注册中心实例被认证，则需要填写用户名密码
    - 开启微服务治理：所选择的注册中心实例应[开启了 Sentinel 或 Mesh 治理插件](../../../skoala/registry/managed/plugins/plugin-center.md)
    - 监控：选择开启，开启后可查看服务相关监控信息
    - 日志：默认开启
    - 链路追踪：开启后可查看服务的链路追踪信息，目前仅支持 Java 语言

        ![高级配置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/ms05.png)

## 查看并访问微服务相关信息

1. 在左侧导航栏点击`概览`，在`原生应用`页签中，光标悬浮在某一个应用上，点击悬浮菜单`查看更多详情`。

    ![悬浮菜单](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/ms06.png)

1. 跳转到微服务引擎，查看服务详情。
