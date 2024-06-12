# 基于 Git 仓构建微服务应用

应用工作台支持通过 Git 仓库、[Jar 包](jar-java-app.md)、容器镜像、Helm 模板等四种方式构建应用。
本文介绍如何通过 Git 仓库源码构建传统微服务应用，从而对应用进行流量治理，查看日志、监控、链路追踪等功能。

## 前提条件

- 需创建一个工作空间和一个用户，该用户需加入该工作空间并赋予  __workspace edit__  角色。
  参考[创建工作空间](../../../ghippo/user-guide/workspace/workspace.md)、[用户和角色](../../../ghippo/user-guide/access-control/user.md)。
- 创建可以访问代码仓库仓库、镜像仓库的两个凭证，参考[凭证管理](../pipeline/credential.md)。
- 准备一个 Gitlab 仓库、Harbor 仓库。

## 创建凭证

参照[凭证管理](../pipeline/credential.md)，先创建 2 个凭证：

1. 在 __凭证__ 页面创建两个凭证：

    - git-credential：用户名和密码，用于访问代码仓库
    - registry-credential：用户名和密码，用于访问镜像仓库

1. 创建完成后，可以在 __凭证列表__ 页面看到凭证信息。

## 基于 Git 创建微服务应用

1. 在 __应用工作台__ -> __向导__ 页面中，点击 __基于 Git 仓构建__ 。

    ![向导](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/ms01.png)

2. 参考以下说明填写基本信息，然后点击 __下一步__ ：

    - 名称：填写资源负载的名称。
    - 资源类型：本演示选择无状态负载，目前仅支持无状态负载。
    - 部署位置：选择将应用部署到哪个集群下的哪个命名空间。如果要接入微服务，请确保当前工作空间下已经[创建了注册中心](../../../skoala/trad-ms/hosted/index.md)。
    - 所属应用：原生应用名称，支持从已有的原生应用列表中选择，也可以新建，默认与名称一致。
    - 实例数：填写实例的数量，Pod 的数量。

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/git01.png)

3. 参考以下说明填写流水线配置，然后点击 __下一步__ 。

    - 代码仓库：支持选择仓库与自定义，本示例中 Git 仓库地址为 `https://gitlab.daocloud.cn/ndx/skoala.git`，需要根据实际情况替换。其中选择仓库是从用户集成的 GitLab 实例中选择。
    - 分支：默认为 __main__ ，此处为 __main__ ，无需更改。
    - 凭证：选择访问代码仓库的凭证 __git-credential__ ，如果为公开仓库，则无需填写。
    - Dockerfile 路径：，支持输入 Dockerfile 在代码仓库中的绝对路径，例如 __demo/integration/springcloud-nacos-sentinel/code/Dockerfile__ 。
    - 目标镜像名称：支持选择与输入，本示例中地址为 [release-ci.daocloud.io/test-lfj/fromgit](http://release-ci.daocloud.io/test-lfj/fromgit) ，需要根据实际情况替换。其中选择的镜像仓库是从镜像仓库模块中集成并绑定到当前工作空间的镜像仓库实例中选择。
    - Tag：输入镜像仓库版本，例如 __v2.0.0__ 。
    - 凭证：选择访问镜像仓库的凭证，例如 __registry-credential__ 。
    - ContextPath：ContextPath 为 docker build 命令执行上下文路径。填写相对于代码根目录的路径，如 target，如果不填则为 Dockerfile 文件所在目录。
    - 构建参数：构建参数会以 --build-arg 的形式传递到 build 命令的参数中，支持将上游制品下载地址、上游镜像下载地址设置为参数，同时支持自定义任意参数。

    ![流水线构建](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/git02.png)

4. 参考以下说明填写容器配置，然后点击 __下一步__ 。

    - 服务配置：支持集群内访问、节点访问、负载均衡。示例值如下：

        name | protocol | port | targetPort
        ---- | -------- | ---- | ----------
        http | TCP      | 8081 | 8081
        health-http | TCP | 8999 | 8999
        service | TCP      | 9555 | 9555
        
        > 有关服务配置的更多详细说明，可参考[创建服务](../../../kpanda/user-guide/network/create-services.md)。
        
    - 资源限制：指定应用能使用的资源上限，包括 CPU、内存。

    - 生命周期：设置容器启动时、启动后、停止前需要执行的命令。详情可参考[容器生命周期配置](../../../kpanda/user-guide/workloads/pod-config/lifecycle.md)。

    - 健康检查：用于判断容器和应用的健康状态，有助于提高应用的可用性。详情可参考[容器健康检查配置](../../../kpanda/user-guide/workloads/pod-config/health-check.md)。

    - 环境变量：配置 Pod 内的容器参数，为 Pod 添加环境变量或传递配置等。详情可参考[容器环境变量配置](../../../kpanda/user-guide/workloads/pod-config/env-variables.md)。

    - 数据存储：配置容器挂载数据卷和数据持久化的设置。

    ![容器配置](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/ms04.png)

5. 在 __高级配置__ 页面点击 __开启接入微服务__ ，参考以下说明配置参数，然后点击 __确定__ 。

    - 选择框架：支持 __Spring Cloud__ 、 __Dubbo__ ，此处选择 __Spring Cloud__ 。
    - 注册中心实例：目前仅支持选择[微服务引擎中的托管 Nacos 注册中心实例](../../../skoala/trad-ms/hosted/index.md)。
    - 注册中心命名空间：微服务应用的 nacos 命名空间
    - 注册中心服务分组：微服务应用的服务分组
    - 用户名/密码：如果该注册中心实例被认证，则需要填写用户名密码
    - 开启服务治理：所选择的注册中心实例应[开启了 Sentinel 或 Mesh 治理插件](../../../skoala/trad-ms/hosted/plugins/plugin-center.md)

    ![高级配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/git03.png)

## 查看并访问微服务相关信息

1. 在左侧导航栏点击 __概览__ ，在 __原生应用__ 页签中，选择原生应用进入到详情页面。

    ![原生应用](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/git04.png)

2. 在详情页面中， __应用资源__ 页签中，选择带有 __服务网格__ 标签的资源，并点击。

    ![跳转](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/amamba/images/git05.png)

3. 跳转到微服务引擎，查看[服务详情](../../../skoala/trad-ms/hosted/services/check-details.md)。
